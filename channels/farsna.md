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
<img src="https://cdn4.telesco.pe/file/O3qqrC_VM5RdPJcUjat4xUugGxfuysmQvU1ou6z5q1gHTt_1Y5B8vGHxlxocbX05x7GXzNNlcOk9oU-64XOe2ebxHeaSscWf03NmPrujQWo7UuMbraMDhOSlWlg6EhKyiZT7Wct-9UK1Z05Sj6zlqWCN5F4X-jQQAdo9lFqcLH18mKrfIFAep6bhJfiAmCXprVMd1dnLIgBLqczxYc8b_t18W3QlkUpaHS7FqmRDrqgJop__ywuWgytNogpcSCBSwdqt99a-uBTU1eo5YagceRxGUg5V-5Dl0T1U5h9ea_9oDhOxdC6obm71T4AnKwaWPpVK4stsm2GrA2mPB0Mfzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 22:28:37</div>
<hr>

<div class="tg-post" id="msg-462544">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
لطفاً صدای ما
بیماران سرطانی
باشید. هزینۀ داروهای مورد نیاز بیمار سرطانی برای هر دوره شیمی‌درمانی به حدود ۱۰۰ میلیون تومان رسیده است. با حذف یا کاهش حمایت‌های دارویی،  خانواده‌ای که درآمد متوسط یا پایینی دارد واقعاً چگونه باید این هزینه را تأمین کند؟ خانه و طلا بفروشد، قرض کند یا درمان عزیزش را نیمه‌کاره رها کند؟
دارو کالای لوکس نیست
و درمان سرطان انتخابی نیست. خواهشمندیم مسئولان برای
حمایت واقعی از بیماران صعب‌العلاج
و جلوگیری از توقف درمان به دلیل مشکلات مالی، اقدام فوری کنند.
🔹
دولت اعلام کرده به خودروهای بالای ۲۰ سال بنزین سهمیه‌ای نمی‌دهد. طرح خودرو فرسوده هم که تعیین تکلیف نمی‌شود. خواهشمندم در این طرح بازنگری شود.
🔹
هفتۀ گذشته با کارت شخصی،
سهمیه بنزین
۱۵۰۰ تومانی‌ام را مصرف کردم و تمام شد. امروز برای استفاده از سهمیۀ ۵۰ لیتری بنزین ۳۰۰۰ تومانی مراجعه کردم، اما با کمال تعجب دیدم فقط ۱۳ لیتر در کارت نمایش داده می‌شود و ۳۷ لیتر از سهمیه‌ام مفقود شده است. این ۳۷ لیتر سهمیه
متعلق به مردم و حق‌الناس
است. چه کسی یا چه کسانی مسئول این اتفاق هستند؟
🔹
در منطقه محروم
کنارک
،
پمپ‌بنزین اصلی شهر
بدون اعلام دلیل
تعطیل شده
و این موضوع مشکلات زیادی برای مردم ایجاد کرده است.
🔹
بعد از بیش از ۱۵ سال پس‌انداز، امسال با همسرم یک خودروی صفر خریدیم اما پس از دریافت کارت سوخت متوجه شدیم خودروهای نو شماره از سهمیه بنزین ۱۵۰۰ و ۳۰۰۰ تومانی محروم‌اند و فقط ۱۱۰ لیتر بنزین با نرخ بالاتر دریافت می‌کنند. سؤال ما این است
چرا باید خودروی نو شماره از سهمیه یارانه‌ای محروم باشد؟
بسیاری از ما نه خانه و نه دارایی قابل‌توجهی داریم و خرید یک خودرو به ‌سختی برایمان ممکن شده است.
🔹
لطفاً
تخلفات ایران‌خودرو
را پیگیری کنید. بعد از ۳ ماه از موعد تحویل خودروی ما، امروز از نمایندگی تماس گرفتند و اعلام کردند باید ۴۰ میلیون و ۵۰ هزار تومان بابت اسقاط خودرو پرداخت کنیم؛ درحالی‌که حواله ما مربوط به طرح عادی بوده و
طرح اسقاط برای خودروهای فرسوده
است.
🔹
تأمین اجتماعی
چند سال مبلغ حدود ۷۱۵ هزار تومان به‌عنوان
کمک‌معیشت به بازنشستگان
پرداخت می‌کرد اما امسال اعلام شد با احکام جدید این مبلغ قطع می‌شود. این در حالی است که همین مبلغ در شرایط اقتصادی فعلی، کمک‌خرج بسیاری از بازنشستگان بود. اما عجیب‌تر اینکه در شهریورماه هنگام پرداخت معوقات حقوق فروردین، همان ۷۱۵ هزار تومانی که در فروردین به حساب مستمری‌بگیران واریز شده بود،
از مبلغ معوقات کسر شده است
! اگر پرداخت این مبلغ اشتباه بوده، چرا پس از شش ماه از حقوق بازنشستگان کم می‌شود؟
🔹
ما جمعی از
زائران ثبت‌نام‌شده حج تمتع ۱۴۰۵
، نسبت به
ن
حوۀ تعیین تکلیف هزینه‌های پرداختی و عدم اعزام خود اعتراض داریم. هزینه حج بر مبنای حدود ۴۰۰۰ دلار محاسبه و در آبان و آذر ۱۴۰۴، زمانی که نرخ ارز کمتر از ۸۰ هزار تومان بود، از زائران دریافت شد. پس از کاهش ظرفیت اعزام بسیاری از زائران بدون آنکه از سفر انصراف داده باشند از اعزام بازماندند و وجوه آنان نیز مدت‌ها مسترد نشد. مطالبه ما روشن است زائرانی که به دلیل محدودیت ظرفیت اعزام نشده‌اند باید
بدون پرداخت هزینه اضافی در اولویت حج ۱۴۰۶ قرار گیرند
. در صورت عدم امکان اعزام نیز استرداد وجه باید با لحاظ ارزش واقعی مبلغ پرداختی و مبنای ۴۰۰۰ دلار با نرخ روز انجام شود تا کاهش ارزش پول موجب تضییع حقوق زائران نشود.
🔹
لطفاً مسئولان فکری به حال
رانندگان استیجاری شهرداری‌ها
کنند. نه قرارداد درست‌وحسابی داریم، نه حقوق کافی، بیمه، عیدی، پاداش، سنوات و
امنیت شغلی
. با هزینه‌های سرسام‌آور استهلاک و قیمت خودرو، ادامه کار برای ما بسیار دشوار شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/462544" target="_blank">📅 22:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462543">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSin7Qg5-o8HIKj4zpEvNfpQLfGYQRLI_iPaHqEM7-RnEglLPt_WnX1m4g_4Ryhx9W1_epOHzY4WagK2heytotPY1zxfDAoNl80vylyyNWKsVo7932de5aNa3UGPfbjGLNWqA1mNMzNP2HRwFVLEYATLRtxal62oLCoUT7d05I1mWeXomtum4TM6KYmlV5FXiIFL2HkhnW1Lu-1tvpB2w3FBgoBwPBytBhNR3mGmX16rK43Z5haAxsQMTgNFRcqVK_cdfeeBcbwzPgD-J3YJY-J2JqpbgKDbQMCbp_n893YiwD-dtQ5Of18V0fniuFdX8W6nYWF6HdFSMNOh0PcCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی در ساعات گذشته منطقه‌ای میان شهرهای زوطر شرقی و میفدون، نقطه‌ای در اطراف بیت یاحون، شهر المنصوری و منطقۀ حدات را بمباران کرد. همچنین توپخانۀ اسرائیل دره زبقین را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farsna/462543" target="_blank">📅 22:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462542">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8032dc77.mp4?token=CUMv6rmX1ev4FfwFPRWIa8h_TUSnoajgFiwFHcODXLMzJCmYdMPEq7lVhXdbE12622y2WZxGx8FcBdRzSrZB6pi48Nylm9AQwzt6LFiJ167jecYwU4idJNRY3bb3FQvonCrX-qMs8Uof-O6LqV3Vy0xD7zx38QP2dwC-3Ga60M_FLECu-ztt480caYlphNry9dtIe03NqEJLni3Ljg93u7-C7LiqPoZP6_v9Sz0hSVhd4RIh19DqCVI5fox7lnl_x5pCzIDbZOqeJKedA1CJgkVp6sGylqZi8Sfp8ZecTBchBYumwEqazIJjsKVgrTl2iXdpXQyWIZG2J6GwDKRsAnuJVmGm50fZvvwWSFx117TDcT24VwJ6ZTgO3hvLlm5OZCF4NIef0mhb3G3DoHpt1R_Y029duPnCoPpBAse5NnVJZuxrlbS9eHqYqNTJbXchGAa28mU1qRoiE4Kd63H8QopzSwtq2R5c4Lrq1LJ4yAhv97HHf_xaeqs41abddxRYt677aFrMfpp3yG2rjOpJ-hVHpT-SC9z4EZDBhqJOV8urY2uOlRmGAX0CHo20NlNoFQJP1MCPF9NmaRVLf_JNoEcGTFdiGhgExh96EBCeJJFPGmBt0hPq75xzwoCXTBjX2RKQCFeS3Dkc7TYUQsUZOqtAmOaU_VNXScOl_fg8u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8032dc77.mp4?token=CUMv6rmX1ev4FfwFPRWIa8h_TUSnoajgFiwFHcODXLMzJCmYdMPEq7lVhXdbE12622y2WZxGx8FcBdRzSrZB6pi48Nylm9AQwzt6LFiJ167jecYwU4idJNRY3bb3FQvonCrX-qMs8Uof-O6LqV3Vy0xD7zx38QP2dwC-3Ga60M_FLECu-ztt480caYlphNry9dtIe03NqEJLni3Ljg93u7-C7LiqPoZP6_v9Sz0hSVhd4RIh19DqCVI5fox7lnl_x5pCzIDbZOqeJKedA1CJgkVp6sGylqZi8Sfp8ZecTBchBYumwEqazIJjsKVgrTl2iXdpXQyWIZG2J6GwDKRsAnuJVmGm50fZvvwWSFx117TDcT24VwJ6ZTgO3hvLlm5OZCF4NIef0mhb3G3DoHpt1R_Y029duPnCoPpBAse5NnVJZuxrlbS9eHqYqNTJbXchGAa28mU1qRoiE4Kd63H8QopzSwtq2R5c4Lrq1LJ4yAhv97HHf_xaeqs41abddxRYt677aFrMfpp3yG2rjOpJ-hVHpT-SC9z4EZDBhqJOV8urY2uOlRmGAX0CHo20NlNoFQJP1MCPF9NmaRVLf_JNoEcGTFdiGhgExh96EBCeJJFPGmBt0hPq75xzwoCXTBjX2RKQCFeS3Dkc7TYUQsUZOqtAmOaU_VNXScOl_fg8u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور جان‌فدایان و مردم انقلابی درگز خراسان رضوی در راهپیمایی شب ۲۰۰ تجمعات
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsn</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/462542" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462541">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697ece007e.mp4?token=E1TC0hiyDCo37-wAdjCW86dzEiOVkvt6-2G6Xg6NEc5-NpUhAfZOmzNgnlikL0AFdTMQtCW4ma2j3Ee6GP9R5h_wcbEC7cfc9815QJ9w8jmTh1CiRkGeYpR2rQEOE6p7yuG_aBosxE-RMCeAQC2ZF1MMmirkvgpZLCq7eWjrwcX29u-2T8ss7fOuHwjKpzScsI8riRhDRCiCiM4APUZPJAPHce9_ucD-bag0YmlV0o5maPsk0vTpd9nsrNiWamtiG-Yf-aChlOIeOZ6wIlxPU6JODKnIGGKLg22cqjQBJmy4WHUNLhITV4bKYuUM-od5Li4NhYzoISiL9a2rFZjnFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697ece007e.mp4?token=E1TC0hiyDCo37-wAdjCW86dzEiOVkvt6-2G6Xg6NEc5-NpUhAfZOmzNgnlikL0AFdTMQtCW4ma2j3Ee6GP9R5h_wcbEC7cfc9815QJ9w8jmTh1CiRkGeYpR2rQEOE6p7yuG_aBosxE-RMCeAQC2ZF1MMmirkvgpZLCq7eWjrwcX29u-2T8ss7fOuHwjKpzScsI8riRhDRCiCiM4APUZPJAPHce9_ucD-bag0YmlV0o5maPsk0vTpd9nsrNiWamtiG-Yf-aChlOIeOZ6wIlxPU6JODKnIGGKLg22cqjQBJmy4WHUNLhITV4bKYuUM-od5Li4NhYzoISiL9a2rFZjnFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان‌های خودرویی مردم کرمانشاه در موج ۲۰۰
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/462541" target="_blank">📅 22:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462540">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba163c954.mp4?token=MEzD9_7m8H7coYyjAgvU2R1cOOz0xPntyPFvos5cKBSWlGiUPCNMly3tKMUJ9KT_QLjgA4AyNNXDJJ0hV1qHw8kjHr95--FfLvmdg2TdemyWAjaWkL5Mi4YCoYjmCbgsCHKv6WH2AIpXwmaUGdQg2c0L1_yKFaep3LPhB2R3KjPlyku1PHm2urqqS2EycdBazT-Hz-rGoAFtQKil71k7f15L_2QVez3mCJ8ejmVNfhQd6qqMbQppv2axZY3hTiGgUsNpg54TZeDxzNiXw5fOlePyS_fIcz21XddF9Wh8wZZhKhbOfFL342RmD8FCttgPtUvTa7m6jtMqokBzhrnk3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba163c954.mp4?token=MEzD9_7m8H7coYyjAgvU2R1cOOz0xPntyPFvos5cKBSWlGiUPCNMly3tKMUJ9KT_QLjgA4AyNNXDJJ0hV1qHw8kjHr95--FfLvmdg2TdemyWAjaWkL5Mi4YCoYjmCbgsCHKv6WH2AIpXwmaUGdQg2c0L1_yKFaep3LPhB2R3KjPlyku1PHm2urqqS2EycdBazT-Hz-rGoAFtQKil71k7f15L_2QVez3mCJ8ejmVNfhQd6qqMbQppv2axZY3hTiGgUsNpg54TZeDxzNiXw5fOlePyS_fIcz21XddF9Wh8wZZhKhbOfFL342RmD8FCttgPtUvTa7m6jtMqokBzhrnk3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس‌جمهور در امور زنان: سن طلایی بارداری و اشتغال یکی شده است
🔹
امروز به‌دلیل شرایط اقتصادی زنان ترجیح می‌دهند در کنار مردان کار کنند.
🔹
سن مناسب ورود به بازار کار و سن مناسب برای فرزندآوری یکی شده اگر از مادران حمایت نشود، یکی از این ۲ فدا می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/462540" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462539">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8198d3da4.mov?token=LloZS9nDisx6c2TUPUYXHuVaOMycof_xprRj6OrWRr5PhT1iJSw8Quu8VoUzb9nD0wLYVaI_3z6OhLILtBF2gdSM84Gm-_RQbu_invPW4ltScJCoJXdqLj1M-Q2s5QH21nWowNoPiaiqW3xYbOJBMhSnOzdnDBm0EgjbGkUncqLnaA6LHAhpz7WiNw9psxEyD9HOfOhAGPgmahi7agRnBts6wD4CrOmVk1opw_aBb0q7EHeL5rttcXz4D6oFgeQH9yiHHWGkiTTWVnsuetNcVaZ1SCgX_DKYV2xc1Vy7S-tU0kI1MlYpWe0_0puqvjwfZe1PeCYCMWQlrFH0UeAkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8198d3da4.mov?token=LloZS9nDisx6c2TUPUYXHuVaOMycof_xprRj6OrWRr5PhT1iJSw8Quu8VoUzb9nD0wLYVaI_3z6OhLILtBF2gdSM84Gm-_RQbu_invPW4ltScJCoJXdqLj1M-Q2s5QH21nWowNoPiaiqW3xYbOJBMhSnOzdnDBm0EgjbGkUncqLnaA6LHAhpz7WiNw9psxEyD9HOfOhAGPgmahi7agRnBts6wD4CrOmVk1opw_aBb0q7EHeL5rttcXz4D6oFgeQH9yiHHWGkiTTWVnsuetNcVaZ1SCgX_DKYV2xc1Vy7S-tU0kI1MlYpWe0_0puqvjwfZe1PeCYCMWQlrFH0UeAkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب گذشت؛ اجتماع شبانۀ مردم جنوب شرق تهران ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/farsna/462539" target="_blank">📅 22:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462538">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021dfa4acd.mp4?token=p4py4Yr-yfEs8OKCMZJXo-Jr3PE67WwzxImRwPwrcBYZu24TejM2-xHdhU33bQxLtnONjosZS_ZkxUAg_XGlVEaL0stx0VGbmAQeH6FsnnfngizeEUYg7qIVlSQU0Ai7St3hFknQhSVNmBvD7N77rb-ZC0_zZoLFRoPRFcyGRwwTWmicDrI8u-HFe3O94jfwmzghR7OYdVfpPGOnKEkJ23mKAN9eOgS0Aqk7CohDEHZuewS28JSuh0hL5s_X1LXH3My8ed_h1vu98Q-RAY-i5i4cUDHym4ssyefSkgmg4TqQMpPLJTZC02_LJmgKhgYHr8o7BWsH4zFXSxn8JqCIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021dfa4acd.mp4?token=p4py4Yr-yfEs8OKCMZJXo-Jr3PE67WwzxImRwPwrcBYZu24TejM2-xHdhU33bQxLtnONjosZS_ZkxUAg_XGlVEaL0stx0VGbmAQeH6FsnnfngizeEUYg7qIVlSQU0Ai7St3hFknQhSVNmBvD7N77rb-ZC0_zZoLFRoPRFcyGRwwTWmicDrI8u-HFe3O94jfwmzghR7OYdVfpPGOnKEkJ23mKAN9eOgS0Aqk7CohDEHZuewS28JSuh0hL5s_X1LXH3My8ed_h1vu98Q-RAY-i5i4cUDHym4ssyefSkgmg4TqQMpPLJTZC02_LJmgKhgYHr8o7BWsH4zFXSxn8JqCIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از تندیس سردار شهید حاجی‌زاده در میدان ابوذر
تهران
@Farsna</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/farsna/462538" target="_blank">📅 22:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462537">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملۀ رژیم صهیونیستی به حومۀ دمشق
🔹
ارتش اشغالگر اسرائیل با ۴ گلوله توپ شهر بیت‌جن در حومۀ غربی دمشق را مورد حمله قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farsna/462537" target="_blank">📅 22:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462536">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=VDHUzvW6XogrxRfejmFxUr6zPlAnco9a3YQZK_xmmVW7JOB0KpnGIXKE2P1S8G0S1ey5_lGjqfr7Y8F3OFu3ndx1AF2JWWolcRLB3MkutmwemX-T54R15EIcZ3pSRG86IN8i3ACQLfLFmAm0bhq_awaSTDkeLjfbL-eXoD38H6KQ5Ipjv1VPxo9pBeuEa089JkYIDbGcofdvc1I_okjT5w-CnhPLgalcb0SEFT6WaDTq0um9Y5pidwYIvr250I_NRs4h_luwMZ0pU0QnKx20j4K0iAUSwmKXRFYEqvJtMxoh3OZ12N6DfxkMMNtcuw_TalndZymc1Ph-5RnPlHt4Dx_0Tb788K8CpX4YqsGY7XOfzqC47xfIk1jZV-HkLK1lIhgq2KTfrgR1D9KSEPmiOFXF18vVU7JZmnNtBYGXYL67KD6WTRDbZvSeQwUh4vNfXHZ1Q2D3VHSg78HPPuOz-QOeiXAFE90ShzuMrFsy5xezHD8jBgh8cZsK6imzDsfvE6cG572_8aBPhX3LZxqIxfAodHNuUgeB619xz56NZFCE51TBU-GhI8-H_PBRxuwLlmKmYz_U6E5Cl4BUjfAxpGtTz6zOnpX2j-RxXU57Jbdpixaq9ogafGMxhhHaiiJX1gjAWcmVGi3oEXG4bvyyDyGj96qG5qBDvP4BN2-vqAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9585b17f3e.mp4?token=VDHUzvW6XogrxRfejmFxUr6zPlAnco9a3YQZK_xmmVW7JOB0KpnGIXKE2P1S8G0S1ey5_lGjqfr7Y8F3OFu3ndx1AF2JWWolcRLB3MkutmwemX-T54R15EIcZ3pSRG86IN8i3ACQLfLFmAm0bhq_awaSTDkeLjfbL-eXoD38H6KQ5Ipjv1VPxo9pBeuEa089JkYIDbGcofdvc1I_okjT5w-CnhPLgalcb0SEFT6WaDTq0um9Y5pidwYIvr250I_NRs4h_luwMZ0pU0QnKx20j4K0iAUSwmKXRFYEqvJtMxoh3OZ12N6DfxkMMNtcuw_TalndZymc1Ph-5RnPlHt4Dx_0Tb788K8CpX4YqsGY7XOfzqC47xfIk1jZV-HkLK1lIhgq2KTfrgR1D9KSEPmiOFXF18vVU7JZmnNtBYGXYL67KD6WTRDbZvSeQwUh4vNfXHZ1Q2D3VHSg78HPPuOz-QOeiXAFE90ShzuMrFsy5xezHD8jBgh8cZsK6imzDsfvE6cG572_8aBPhX3LZxqIxfAodHNuUgeB619xz56NZFCE51TBU-GhI8-H_PBRxuwLlmKmYz_U6E5Cl4BUjfAxpGtTz6zOnpX2j-RxXU57Jbdpixaq9ogafGMxhhHaiiJX1gjAWcmVGi3oEXG4bvyyDyGj96qG5qBDvP4BN2-vqAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
جان تازه در رگ‌های فلک‌الدین خرم‌آباد
@Farsna</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/462536" target="_blank">📅 22:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462535">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d53337f51.mp4?token=ZalulPoIs4FEZS98ScDl_w4r2x8vs2RJV23Om5LAfvdeWlsztEg2-YCvfmaWBnGeI7psbRixG2gEl7yInaYnSXJnm3KOu0hUJ27yhn-FJXLd5HlBOYsgXwtHPgD2dzM4yaXN1gNWW78yhfUFcgyF5ZqljnBmG7_9a412aEZ17FJeV_6CyY7oFnvY5YfbJoTILVNfOzkjZ_0wrhIhf0Uj0Shi6IC17n85ZrPrxwVWiHYvn9h36RONCbkVXBrWnpaxVsoguozbV7zSWbP867Mo6usxXeik01va3ao3nFDsgMY8Vxe5R6ZL142kn3CYbXeJtyRo-srk8Tf32giJObWbUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d53337f51.mp4?token=ZalulPoIs4FEZS98ScDl_w4r2x8vs2RJV23Om5LAfvdeWlsztEg2-YCvfmaWBnGeI7psbRixG2gEl7yInaYnSXJnm3KOu0hUJ27yhn-FJXLd5HlBOYsgXwtHPgD2dzM4yaXN1gNWW78yhfUFcgyF5ZqljnBmG7_9a412aEZ17FJeV_6CyY7oFnvY5YfbJoTILVNfOzkjZ_0wrhIhf0Uj0Shi6IC17n85ZrPrxwVWiHYvn9h36RONCbkVXBrWnpaxVsoguozbV7zSWbP867Mo6usxXeik01va3ao3nFDsgMY8Vxe5R6ZL142kn3CYbXeJtyRo-srk8Tf32giJObWbUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب حضور مردم؛ میادینی که هر شب شاهد یک روایت تازه بودند
@Farsna</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/462535" target="_blank">📅 22:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462534">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9322fee6.mp4?token=Gtis9Ahf1GO5-v1SqVtWtJpovfOkmk-lUoNNp2TZ1sZdAxx0fN6jehgkv-6_qbMTOwCbDS6TD3cjTGSBGBF2WBsGhSxlW-oFkkTBxYd7vRYTxI2nPnbM2SYnroQYwBw_ehtjAx3dfAxll3QeZj781OIXtslHe6tfjOvVi2cBtVbHJF9nODSxw0kfAN_X5c_MMlfmsP35P2kI4FCyssW2bKxsJB-Z6FtmTCOPr27v8KJqrShtjTX55ZiM3RB3M0LK28rdu78FX2NStKy7V4FyR5F_RI_393JIr3eZ3s8f-Pg78jZ0es7c8Xxc4wYSR9uVlAoYfRrenxh8IK_tAINUzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9322fee6.mp4?token=Gtis9Ahf1GO5-v1SqVtWtJpovfOkmk-lUoNNp2TZ1sZdAxx0fN6jehgkv-6_qbMTOwCbDS6TD3cjTGSBGBF2WBsGhSxlW-oFkkTBxYd7vRYTxI2nPnbM2SYnroQYwBw_ehtjAx3dfAxll3QeZj781OIXtslHe6tfjOvVi2cBtVbHJF9nODSxw0kfAN_X5c_MMlfmsP35P2kI4FCyssW2bKxsJB-Z6FtmTCOPr27v8KJqrShtjTX55ZiM3RB3M0LK28rdu78FX2NStKy7V4FyR5F_RI_393JIr3eZ3s8f-Pg78jZ0es7c8Xxc4wYSR9uVlAoYfRrenxh8IK_tAINUzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تنگه‌های راهبردی تا بازارهای جهانی
@Farsna</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/462534" target="_blank">📅 21:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462533">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0z2qWEUPXPQs-cfBt_YKUVZ9PVakNNgaAGxLayogCxiwF_UxBIQveoGlwnLiglwck05I2jYW4RPquJC0_t89mpWMkOCFHWnsZhHkX9v6BkFSKhvkwpugxKSracq66-EWOOruv81uP5tnLuvCMeOF73bqUWcSUekK_gtVOYjRNNUubZE32XoW1xvyJRb7L_s_DLS8hYhkROsJz4NRvKpe8ApK0mytIJ4T7Dam0DsHt8d-TaBytkahJ2Vo__xVBAd0lv1zKw3AW06LvF_VIu65XpZCrwTsa0L1Xvwicp8AKvJqSN4lrdZ663-Albysh_7b6YbnAqsr5r2Qo9hgRzAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای دروغ سعودی‌ها؛ سناریوی ساختگی علیه مکه شکست خورد
🔹
«ادی کوهن» روزنامه‌نگار و تحلیلگر صهیونیست به نقل از منبع اطلاعاتی غربی فاش کرد که حکومت آل‌سعود یک پهپاد چینی را با هدف جا زدن آن به عنوان پهپاد یمنی در آسمان مکه مکرمه به پرواز درآورده و سپس آن را به قصد جلب محکومیت از سوی کشورهای اسلامی و اعطای بُعد دینی به جنگ علیه انصارالله یمن ساقط کرده است.
🔹
کوهن افزود سعودی‌ها به دنبال کشاندن پای کشورهای اسلامی به‌ ویژه پاکستان و ترکیه به جنگ علیه یمن هستند به خصوص پس از آنکه آنکارا و اسلام‌آباد پیمان مکه را نقض کرده و ریاض را تنها گذاشتند.
🔹
در پی این ادعای کذب سعودی‌ها چندین کشور عربی همسو با ریاض نظیر بحرین، دولت لبنان و مصر در اقدامی هماهنگ، حمله پهپادی به مکه را محکوم کردند.
🔹
در همین ارتباط، محمد الفرح، عضو دفتر سیاسی جنبش انصارالله یمن تصریح کرد: یاوه‌گویی‌ها درباره هدف قرار دادن مکه از سوی یمن، کذب محض است، ما از کسانی که پرده کعبه را به جفری اپستین هدیه دادند، دلسوزتر نسبت به مقدسات هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/462533" target="_blank">📅 21:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462532">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bcbf379b.mp4?token=CT4xNZhZUXu4D8gcuk-n2G6YJQVH66U_RZ6FJ92pPLUn7zL1BX1pb5H827i4p-rdB7tKy0tgL6_pY1AijmhhGd8Qoexb6Y01be2ARmMG7izET60VqoqZsj8M-3sjEA5ufBKGfhDwfw4NQaiUUFoqxoA4EMWaF6GpU91YcNMN7hYgV6Gkf0Zyjej-hYri8PWBCGvJadtpmFex6nu2W49T03RE_Tj6dP1WUhk6qOdm6WoVTprxsVe9PRqX_NE24GP00FbZTn_aMJRnuepjmEIGegyB9AAqB4j7GS_M2E8Hjwyt-KpzfNLAxxbI4PCtxkfJZLqYITtjRlci3ZxbZUToobocGnDOCI60pMOA7Zppif24e3lozz2xzx6hHutLz9mPTM6BrHEQgYdO_P_UvD4qx0rIO54IH1JvMwUQS0doXmwSAJAUxKsN6mexQdAGoaBb-YCnN1RP9ZyBLQ42KhyygUjFhiLDGKgT83kDyYK8FBCPEMAVo0mTVtiqvL_fLbM1NKHLk83WSLd2SAfOg1NbffEuOlapETGspL1ZQDi3rrbuXmiVzkJXhvIfaB9lYjuGVwAuGn68skIVIlnXdsv5v_qjyfTNN946sh5aq0gvWB66K6FStfRfkbXaBVr6vO6WZpifuOpEl-KuB_4lw7QYKjpZcq0WipGk4GjZp3z65sY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bcbf379b.mp4?token=CT4xNZhZUXu4D8gcuk-n2G6YJQVH66U_RZ6FJ92pPLUn7zL1BX1pb5H827i4p-rdB7tKy0tgL6_pY1AijmhhGd8Qoexb6Y01be2ARmMG7izET60VqoqZsj8M-3sjEA5ufBKGfhDwfw4NQaiUUFoqxoA4EMWaF6GpU91YcNMN7hYgV6Gkf0Zyjej-hYri8PWBCGvJadtpmFex6nu2W49T03RE_Tj6dP1WUhk6qOdm6WoVTprxsVe9PRqX_NE24GP00FbZTn_aMJRnuepjmEIGegyB9AAqB4j7GS_M2E8Hjwyt-KpzfNLAxxbI4PCtxkfJZLqYITtjRlci3ZxbZUToobocGnDOCI60pMOA7Zppif24e3lozz2xzx6hHutLz9mPTM6BrHEQgYdO_P_UvD4qx0rIO54IH1JvMwUQS0doXmwSAJAUxKsN6mexQdAGoaBb-YCnN1RP9ZyBLQ42KhyygUjFhiLDGKgT83kDyYK8FBCPEMAVo0mTVtiqvL_fLbM1NKHLk83WSLd2SAfOg1NbffEuOlapETGspL1ZQDi3rrbuXmiVzkJXhvIfaB9lYjuGVwAuGn68skIVIlnXdsv5v_qjyfTNN946sh5aq0gvWB66K6FStfRfkbXaBVr6vO6WZpifuOpEl-KuB_4lw7QYKjpZcq0WipGk4GjZp3z65sY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب؛ مردم اهواز میدان را زنده نگه داشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/462532" target="_blank">📅 21:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462531">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d17ef81a.mp4?token=fMm1WKWepBlVxiaDycEpeMs_8o297-NW7S6ZwssfCN0VRCgqK3oQb09j3WxqGMmSKF6hdcOiWTOX_GdVfltGfR3xJgApywbs0D478Ng-4bWhx4oSc0D4aN_PrjPMlGlHTx8dEsXgpRSSl0f30qSbfW5QYL1IIdHh7O-Qzxt3ldxx0c85KaqsCcVClpdrTUa1Nh77voE5M9H4kD4ZoJhEtMyzGJO9aqVGTD7UtXpj_k0NnEqDq49S_w_qZ3KMvXFiZ9W8mxhT0S_CKLC5GzSvJ9XpSHUvCNe4c_8azCKYua99mD4BFZFb22FWggDOF1qCxZ7tCWz_kJ99eGQdkw3To5v-ms8TPKXB0tEBiTQZoT84NNbKVSHOQXcKz0jUTjnb29omR-NmG-8wxTb74RLPZbHdl-RW4DOSZ1nzPp9IUCU85NhOeJvt8ZCzhfaZIwId0yvOUlH-yqFQFHjXuESEH3Spdnqvwpb1FclKmpWNv4lmoOKVqgs6SpFPJJrLrBn6ts2HqMAbnMdx34dIoBYD4fop04ML_TgQcjOQm9OdxxaTF7psNcO12be_9rnE4faPl7JeNMWD3iZ7Seytwkez3C7Fuiusx5J_T6Ds-YhIVMiY5EH8Hex3BRhp9y1zbpNyQrY5wtgK-iEfOY3o58xMpfJeDoMDZ8U6MorWAYBnhFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d17ef81a.mp4?token=fMm1WKWepBlVxiaDycEpeMs_8o297-NW7S6ZwssfCN0VRCgqK3oQb09j3WxqGMmSKF6hdcOiWTOX_GdVfltGfR3xJgApywbs0D478Ng-4bWhx4oSc0D4aN_PrjPMlGlHTx8dEsXgpRSSl0f30qSbfW5QYL1IIdHh7O-Qzxt3ldxx0c85KaqsCcVClpdrTUa1Nh77voE5M9H4kD4ZoJhEtMyzGJO9aqVGTD7UtXpj_k0NnEqDq49S_w_qZ3KMvXFiZ9W8mxhT0S_CKLC5GzSvJ9XpSHUvCNe4c_8azCKYua99mD4BFZFb22FWggDOF1qCxZ7tCWz_kJ99eGQdkw3To5v-ms8TPKXB0tEBiTQZoT84NNbKVSHOQXcKz0jUTjnb29omR-NmG-8wxTb74RLPZbHdl-RW4DOSZ1nzPp9IUCU85NhOeJvt8ZCzhfaZIwId0yvOUlH-yqFQFHjXuESEH3Spdnqvwpb1FclKmpWNv4lmoOKVqgs6SpFPJJrLrBn6ts2HqMAbnMdx34dIoBYD4fop04ML_TgQcjOQm9OdxxaTF7psNcO12be_9rnE4faPl7JeNMWD3iZ7Seytwkez3C7Fuiusx5J_T6Ds-YhIVMiY5EH8Hex3BRhp9y1zbpNyQrY5wtgK-iEfOY3o58xMpfJeDoMDZ8U6MorWAYBnhFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معمای عجیب نفت عراق
🔹
ترامپ چگونه با گروگان‌گرفتن پول نفت عراق، دولت آن را کنترل می‌کند؟
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/462531" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462530">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=o4jqj4uDBuDOQt3JYHfTTbb8M8HysuwkDZtkUEn_afITFAe4adLowM-jK0LBkKdUBYlYwMv6K4OK9IBFh3tFK9gg5YHgUfkSH_360nFcHQRa5rTnLh8LnDSkyXQBH1EwK0Tu57CYZvlviCo_B2ATCPp2optOLB_c-hdwndahN76gKU0g3cRdsUSN7BheN1iTpEDOmZx0_j4AbkLZf5sD2ZEwfUd4Dm7W7j7bodajpciIG9wuf1u8cTl2bDWMHtHReyLI-vOP7wds00s0j43VfnCa1vXmrix-Hk_-9eff0zC0-OCwIsVo5jQjqaqWTb5M9YN9uqJHBjWUcWwKgkIdMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e516ccdc77.mp4?token=o4jqj4uDBuDOQt3JYHfTTbb8M8HysuwkDZtkUEn_afITFAe4adLowM-jK0LBkKdUBYlYwMv6K4OK9IBFh3tFK9gg5YHgUfkSH_360nFcHQRa5rTnLh8LnDSkyXQBH1EwK0Tu57CYZvlviCo_B2ATCPp2optOLB_c-hdwndahN76gKU0g3cRdsUSN7BheN1iTpEDOmZx0_j4AbkLZf5sD2ZEwfUd4Dm7W7j7bodajpciIG9wuf1u8cTl2bDWMHtHReyLI-vOP7wds00s0j43VfnCa1vXmrix-Hk_-9eff0zC0-OCwIsVo5jQjqaqWTb5M9YN9uqJHBjWUcWwKgkIdMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در آژانس بین‌المللی انرژی اتمی چه گذشت؟
🔸
روایت رضا نجفی، نماینده دائم ایران، از رقابت ایران و آمریکا در آژانس و اتفاقی که معادلات رأی‌گیری را تغییر داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/462530" target="_blank">📅 21:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462529">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaZgN4XxYXyc3ePPRg_jWdO9w78IgCchFXxpK7b8KVarKCSmheeRboD-etVdDKOCmXEIvYRj9u6Ud2f-grzDWvtwUW6u_iTu3twVmmvpjOo3D7noNAcl63g_IWsEjlC0UQg1qVQDRNCJSk3TjrisOUuSJ0euWY_zmQXQYy5dwNdP2h7SUc0gpL29vexooqavR2QyuMwbkPwgQs5IyFYWydXzsaf5hh4Ed4S9nPn0DTKGUs8yqx4s09DsDByTaBFx909fpR4QNiSeY1zQkHZ2E1Z9eaK47sT7m_3V5c5IzOAGiPYgmbludUOB7db3ZIT_kU4ncc_G9OQjS4HLVL19Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس به تاسیس «تیم ب» در لیگ یک نزدیک شد
⚽️
پیگیری‌های نشان می‌دهد مسئولان پرسپولیس با باشگاه بعثت کرمانشاه به توافقات خوبی رسیده‌اند و اگر اتفاق خاصی رخ ندهد، پرسپولیس با خرید امتیاز این باشگاه در مسابقات لیگ دسته اول شرکت خواهد کرد.
⚽️
باتوجه‌به فرصت…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/462529" target="_blank">📅 21:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462528">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af5db818dd.mp4?token=PaB0Ik9GT67fRIH-G6I64qn2Suhic-bEKyDdaUvFEejNH251Ij9T10HHnKJtnnte-2BO5wr5DC8jxb1gbuzwLgI5BbKJ8V4M4Y7e1EKv6zIhHRvg66mKS8MIwj531xLIujooWlfWhVke5Sf8uk9PjnZ_8FKDcXsIpg67YoBQzAdSh8n9ID1l5N-t-UsqxzLX6p_dcaQAVsQDvpHm82ywS95ARG-SfbqWM_LdlRPDP4Sh1fhax6KaY0AvXtyISM4OvEPWyCM9aZQ6hcbp66sy3ilS6qyrHCR0Gr2dd8rd3uGNFAonevQkwAsZe5A6iy0ON-t11-2oC00TvUgi78OV2iglQlx2Vdb2l-07qr7Bp8wrUjr5oCYOwdBxbVr0PVFHvYWWdudd1A3HzpvZ3k_7qLcGOQE_h25PLHqtMp3MBYSkYDVfU3uvQoL_Vr4f6iZ8rrx6UIdurfFrAQBdCkwskBHhWgpKJDV2aUlhgnQsyFyAs7EiK9Hz7fiaozp14QOJkwnbF1gXCmR7eYINu0O_ZnF5pf7LINlcsLyfGtz3Eeh-XkwMUSIAKDKNA7FqYCe_cKVQQeM8P2lsNxpKywyHcGxGgt-ZcCy6RqZJ5pxGkFrdy7s4S1BgZMpFT7TvgGxCUezfFNybmW1-t9tkUVJur1wNTFqTd4lFc3upSdT3YXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af5db818dd.mp4?token=PaB0Ik9GT67fRIH-G6I64qn2Suhic-bEKyDdaUvFEejNH251Ij9T10HHnKJtnnte-2BO5wr5DC8jxb1gbuzwLgI5BbKJ8V4M4Y7e1EKv6zIhHRvg66mKS8MIwj531xLIujooWlfWhVke5Sf8uk9PjnZ_8FKDcXsIpg67YoBQzAdSh8n9ID1l5N-t-UsqxzLX6p_dcaQAVsQDvpHm82ywS95ARG-SfbqWM_LdlRPDP4Sh1fhax6KaY0AvXtyISM4OvEPWyCM9aZQ6hcbp66sy3ilS6qyrHCR0Gr2dd8rd3uGNFAonevQkwAsZe5A6iy0ON-t11-2oC00TvUgi78OV2iglQlx2Vdb2l-07qr7Bp8wrUjr5oCYOwdBxbVr0PVFHvYWWdudd1A3HzpvZ3k_7qLcGOQE_h25PLHqtMp3MBYSkYDVfU3uvQoL_Vr4f6iZ8rrx6UIdurfFrAQBdCkwskBHhWgpKJDV2aUlhgnQsyFyAs7EiK9Hz7fiaozp14QOJkwnbF1gXCmR7eYINu0O_ZnF5pf7LINlcsLyfGtz3Eeh-XkwMUSIAKDKNA7FqYCe_cKVQQeM8P2lsNxpKywyHcGxGgt-ZcCy6RqZJ5pxGkFrdy7s4S1BgZMpFT7TvgGxCUezfFNybmW1-t9tkUVJur1wNTFqTd4lFc3upSdT3YXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش بزرگ جان‌فدا، امنیت محله محور و مقاومت در بهارستان تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/462528" target="_blank">📅 21:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462527">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af808b6067.mp4?token=uNuc2muThSsJf1SRUuEnz17uM0pvbrcRhj_hFmrvmNbrcbbEJKx9_O6RyS3S92Eb6Ddjg4ASVG-IqAp8wd8jzTaq5btz0TJUMRQYYlL_4KmE1zSfwBiQK7RIOVZ1qaUYYoHfU3tEW8RTiOYtNUhom-R6AC9NlYKZBGToyKFvsmcJLCmOCap05vCcE5isl4LRBzOOdPuS2XMsS3BzIyzIg2qZRKXMBi8tkcDiiUDcGMZFHMU0kJtiXwqMAj74t0vL98411aJ20IHq6HrDO8Iaw2Umzot7Yn5lZ8fdIO5cmWj6sKQlYL8z2UFgYxKtShzG36FtWmkxdqfmp2g_RJYPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af808b6067.mp4?token=uNuc2muThSsJf1SRUuEnz17uM0pvbrcRhj_hFmrvmNbrcbbEJKx9_O6RyS3S92Eb6Ddjg4ASVG-IqAp8wd8jzTaq5btz0TJUMRQYYlL_4KmE1zSfwBiQK7RIOVZ1qaUYYoHfU3tEW8RTiOYtNUhom-R6AC9NlYKZBGToyKFvsmcJLCmOCap05vCcE5isl4LRBzOOdPuS2XMsS3BzIyzIg2qZRKXMBi8tkcDiiUDcGMZFHMU0kJtiXwqMAj74t0vL98411aJ20IHq6HrDO8Iaw2Umzot7Yn5lZ8fdIO5cmWj6sKQlYL8z2UFgYxKtShzG36FtWmkxdqfmp2g_RJYPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر سرنگون‌شدن اف-۱۵ سعودی توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/462527" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462526">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cce86436.mp4?token=LtqxoUsRLxONmhWGuBSnVzW9c3QhlH4t5RfL1dQYEqMJo7zpYF3O3T0GM1rd-FBdA2o5SturKg_WCgEPEFKXXc1wpMZDWFIHyYk5vKhTvm6MF9VfpB-PhKalEcyvTYquSKwICagXUnjCqOCFpuxXOqbjRsDcSRS6j49nK2R0Wcz9HSeQftDfm0Z-qgX8T3AuFRwN6pQTswik6m8nFj9M9iXPrPalZDQ0B_in4mOY1rGkUVxiUJ3mFQt7mWT1U5w4aQWNlbJUg7ZRo8KSM7UvCL8PTB9buwH18hQCUrNqnO2dc_eUrT5dWBXoHbZNPexMSpJ7BW8jkof8Tccg7D2ruQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cce86436.mp4?token=LtqxoUsRLxONmhWGuBSnVzW9c3QhlH4t5RfL1dQYEqMJo7zpYF3O3T0GM1rd-FBdA2o5SturKg_WCgEPEFKXXc1wpMZDWFIHyYk5vKhTvm6MF9VfpB-PhKalEcyvTYquSKwICagXUnjCqOCFpuxXOqbjRsDcSRS6j49nK2R0Wcz9HSeQftDfm0Z-qgX8T3AuFRwN6pQTswik6m8nFj9M9iXPrPalZDQ0B_in4mOY1rGkUVxiUJ3mFQt7mWT1U5w4aQWNlbJUg7ZRo8KSM7UvCL8PTB9buwH18hQCUrNqnO2dc_eUrT5dWBXoHbZNPexMSpJ7BW8jkof8Tccg7D2ruQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج: تکبر با حرف درمان نمی‌شود؛ باید جایی که نفس می‌خواهد تکبر کند، خودت را بشکنی.
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/462526" target="_blank">📅 21:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462525">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj8JtYuSmWahsAMEHYvQR1ldTUW-P0ZNYus06X0epJb8TpskcrJOt35p9v4nqIFZdjkoJ5pQCU22myO7vInRZywSr-VUoaCt1tkhubx_3BQzfWP7RGZWi26JtSO23oj5njBrPRLTHhmgPYcuPlV_HamXnXwUWXa8D2gUSubVpSv1R3ifA-GUY9LV6WXGHdUQHQLRcgZtjBtaaTtZs8ltrYmrNWQH0ATnHYyO_yFY8JgoFiFR2I5rtOixX6Q-mFice40iKe73EUmVS_nNCO26hH2CQWBhUf1lp5CPGxtePsdEIcUn3je7VG6daeERVGxwD1-cvgCR7XgQWvFamtC5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویش ملی «برای پدر به عشق پسر»
🔹
به‌مناسبت میلاد امام حسن عسکری(ع)، مسجد مقدس جمکران، پویشی در جهت ترویج «همسایه داری اسلامی» و با هدف تقویت و نمایش وحدت و همدلی ملی برگزار می‌کند.
🔹
با ارسال عدد ۱۴ به سامانه پیامکی ۳۰۰۰۳۳۱۳ می‌توانید از جزئیات این پویش ملی بیشتر بدانید.
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/462525" target="_blank">📅 21:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462524">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5375928a52.mp4?token=JnqXwMqAGv8G_a3M9nuT80wuL9uTUlOgvP3RPyNwMvesBi77MN1P5BLg81szcmNHLpiLaTzEmgnrmr4VkzY3jNoFViTpbY8NqmwKHspF6kU2pV7LWSCpJwg9jAHbOl9is6b4oweyPSgmpd1XQhgxntmjQcz65_ekULOVgb1fcKmADuSzOLCgSst_hB_M3BhMTELLjtEKl3YsqTUiAF967Oo1jYmYNZZWeTu7liwU43YiQfvyoNGd30bMaSoK7Jhq28NSkhrUs811JpyIk0Iolg9zl4cRfHeZtPbHXGk-FV8Te4N53p480H3gM-NA1k9uzAdEsW1LnuygHU_dtUlwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5375928a52.mp4?token=JnqXwMqAGv8G_a3M9nuT80wuL9uTUlOgvP3RPyNwMvesBi77MN1P5BLg81szcmNHLpiLaTzEmgnrmr4VkzY3jNoFViTpbY8NqmwKHspF6kU2pV7LWSCpJwg9jAHbOl9is6b4oweyPSgmpd1XQhgxntmjQcz65_ekULOVgb1fcKmADuSzOLCgSst_hB_M3BhMTELLjtEKl3YsqTUiAF967Oo1jYmYNZZWeTu7liwU43YiQfvyoNGd30bMaSoK7Jhq28NSkhrUs811JpyIk0Iolg9zl4cRfHeZtPbHXGk-FV8Te4N53p480H3gM-NA1k9uzAdEsW1LnuygHU_dtUlwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید: انگلیسی‌ها به رضای پهلوی گفتند برو و رفت!
🔹
اگر غیرت داری بگو نمی‌روم، بگذار تو را بکشند!
🗓
۲۵ شهریور، سالگرد تبعید رضا پهلوی از ایران
@Farsna</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/462524" target="_blank">📅 21:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWmokbUE4iEehMZPMhrps917NwyppAz8frTgMJ9VD4odilk3ksAYeFGBH8IMbcfvOqBB7wzNb88BjK_Qph7kZT22v5yZO8kv519gfB1bUmMaK4Uc0oybzUZXF3c0szZGqmtcYk9U3h5G-TL9kaQUbVkFRJ9W9Q9Oidu5gzdAxIH1yeV9oOEmKgRLihUspoZlh08ezmzj4_qp_pDAncLkjREzbkHA7Lh4wQVuKz5lhjgde4UbVmu5qe4Zlzn6aQmvHvfq-TJoxTMpa8twnV_NhO4CyZl0vMDjIyi3AELUMuoPcFsuMHPrntyy4dEg8E6Hz0qbc1kU3CrdfaCeEnkLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-K-1C_37vvDVVum2VkrMObu_5dGbZvja-lW1j1rBZbFbvdYphne_UAld1FwSy3EiEus7Oz6RlZEkwJGp5zSjK_1gy1YvxJobBk_8wLlvAk5iNddzgA5p8Q2KpifnkEMyeqhSN-Tf7tA7ARksw96gmtRu6_Dbrttbh0s2EZgo19URci2DzPV790FwDRfwTBS_tInj4AormTy6XbBRQEfDYS3nE4sV-Fw49F6mghGJPc-726vqyclpEeOtWCmWqAvhV69GD3s4xD0giKexYuSBh6XSmtZ4e4Le0cEbQiOaBAkrmwFDZ8pcHuzV3MRMY8OgaVcYvyDZFQr4tni3HsX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPBzotEpEiED0owQllCv1BT8d12ohTcapSV3u500GnKUQMPuEvXyBK9Tqf0CKzwAKH391erAJ4nfDw5Re96QHZUy2P5YV-_5RrEkBURCd6p-kNV_RIzoTAToxSCxJr58NYzeBRPq7D-j5gyZRlYF1cnHsjoruiDHopCIVCBogSkEcPOQHqB8P1vYfJu36xPd6_tO7-QbD_SkLUQFeaL94ujWcj15CacpAz0LoU_v_uwb5AzrvKwqi2LDpLRYkFcNkktGJph5nbeIzUweP48CKPjAj-05-hEAGrRYLKj2FM-jCiiY4g9yES-WYRqw1lLJJk_dYj3eQl4BySWkEDujvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLJzQqRAnpsW-_Arr3ed6xQ-oXS9Ko-rvvgO9wrNrAzxxqLjWDgoAeGPEgZ_uRLH4XS9ZskfDVpBhf7jmDoB7rJ5BxZrQ_jhVpegboqWO2sTSkL_n0gnA2uoLPVdM6WV-TqKLaMqH777C_HRBJh6fu9Xw9SIXM9FAPJY2RP_aCU6P_gKarpTlSKpsx1K-Der_QxfgKv-JfTnanUFFOd0-aqlrOo0zUIE8G5tKpFQfMjvwI1dmvHwr3TPC2cgXxuu4_3C2tTBIk2jKTswGMot3pWAfLIfaIabvjaS1HWN_10iy-5tiKyKuJ1jdk1dn_aHVfHta2t_d_My3Csc1VNMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufNDycMzo0rynfG7fplxGg0VY2_7k2_nVwbeNmw1oAeX7POyPnZnFTvuMsW0LLeMWUVTZqhejxQbHThf9gWeZIQBZ3GpSnX-qdrZ3Uu1S188unfZqnh78S08eimpRf2PaL8PJLOkp2nH4YGYdnAkz3lGDMrFOa3sWRdaqbW6-8iaUuvErA_McM0VNhB8i5F4H2WPpRsNK5GLqr4058kt7U7KnvYWknP22kB8qsoTlJtYMEpmYXM92lmpyFh7n68KqMD7x4EqWIEWpdHwdG45S9_N15gtp9FJswI593qjkiFt2N-KZShgMciOkmcTz74VZJLnCTqV-Cl590VkiqEcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_BRLbdUa3SaILHpgjYkft-rTdY0MIcQO-QgR6ToDwKsto8ld8H6XBfSn1bjUrFp00qjNy_-YSHnyA1WDQKBGva-lVdItZjk1Zfwo1y5u-4VqOERveKNhuAVSBfvWg1vsPsP1jt84wkUNZsbmDbGEKCMq4HdhLJKf0NS3IfUCq5zEGTRB9Ij-2S1U4GR4SmhkK4GfjUk1UjTeicC4IWsk2KHcBE7psH1uNBr6i2KxCZDU_p2-nmqS0jDkhwGnI3osTKXDBBEQGIht07qM2hYwAUbq1y6RlXEB0Ua_R6o8u14Mlevne_dzLISEalB_dvUt4nk8uLi-dx0ymmi30nruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBE7exWNjxH_1po7tmakL704Kib1b7hUqoiAVBg0hcH-3m7XUtI9vWKE-7lsTcIYrysnSqa9vzkoePh9k-0xizDJruCiL-RPuBN-IqrRwia1pB-GmGnGlU8vgd2Wd7bzZAoylI1l-JQ10_3Apfbor68kKVr3agC9zSME4xlLEj9Y_ckXYjcoJCdD9OKdiW6zvnr8sP1Ejtb83Cqv0Msxel84QNfomIl2UCPin-7LAoN2ArFTkOgt55dMcg75Vr016eLgL6_NomMfqHbEN2UGIKjY8hoV0jziN17OkWGy27L__GeOF9cua7zcDNXx79BTmhqcZxqrYytfizUDiGXHQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
موسم بادام‌چینی در باغ‌های خرم‌آباد
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/462517" target="_blank">📅 21:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd104da5f.mp4?token=o1F0T355M-gX64gG3VjVB73XrwApQ7d_s0F1r-TQSzZDiGmGiycuZ7YE4_9vwkNvch5JgNShAzHVHsfRxMq2uaA9YRcQP6QedXIpRo0v7Cud9qIElI4GvqiS4CyVdiijytjIvvSrX6ETzcgm-tmdaIBiZvmj6T6EbCz9KbXYG9ufjSS5HWbMkqdUEAgSABLJ-ArqE6-UZzfDBEMC5jKMCfudc6tKuCD6pgGqdteBcbrJkAYTn5usqzgwluhGyLw3dqs6cYJDUE24XcsAqNHMIT6vtKPviqlDMBENL6f0XjTfcyySahlD6UybGbFrvd-aW-xSAqmBkkzhCfetNxg67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd104da5f.mp4?token=o1F0T355M-gX64gG3VjVB73XrwApQ7d_s0F1r-TQSzZDiGmGiycuZ7YE4_9vwkNvch5JgNShAzHVHsfRxMq2uaA9YRcQP6QedXIpRo0v7Cud9qIElI4GvqiS4CyVdiijytjIvvSrX6ETzcgm-tmdaIBiZvmj6T6EbCz9KbXYG9ufjSS5HWbMkqdUEAgSABLJ-ArqE6-UZzfDBEMC5jKMCfudc6tKuCD6pgGqdteBcbrJkAYTn5usqzgwluhGyLw3dqs6cYJDUE24XcsAqNHMIT6vtKPviqlDMBENL6f0XjTfcyySahlD6UybGbFrvd-aW-xSAqmBkkzhCfetNxg67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آهوی زخمی پس از یک ماه درمان به طبیعت قصرشیرین بازگشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/462516" target="_blank">📅 21:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089c9ef32a.mp4?token=ehOPjH9nsfLcKMRnnh9Q0FXHDiJGwZTIIR8kwdhfxql-DIDjE2fYpps0lYlqMTuHCICfYPfUfwlF5eutJdCZevufQar2IMc3uWT-tGDEU9Piv2QoHMrkApstndAqn3Jm9O-HTIEYtD0mzWy1f_6NbRGvnCPgXGqF0NA9rI9mhADRU_csj4kjpqENG0qP8Es8hY8flvqKAVimXshj5st7Xq3LnyXAq2xlYq62LhxGO4rmY9HUKPoW0YAwebnPTgMkWfkFIsgr8bAJmiRdhn0z9EZ0ht42eKJixbyjf_eXT1_hPjGNMn8_RtrRlQSJk1JzULqRAoBMsdnRwzSLbTJLgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089c9ef32a.mp4?token=ehOPjH9nsfLcKMRnnh9Q0FXHDiJGwZTIIR8kwdhfxql-DIDjE2fYpps0lYlqMTuHCICfYPfUfwlF5eutJdCZevufQar2IMc3uWT-tGDEU9Piv2QoHMrkApstndAqn3Jm9O-HTIEYtD0mzWy1f_6NbRGvnCPgXGqF0NA9rI9mhADRU_csj4kjpqENG0qP8Es8hY8flvqKAVimXshj5st7Xq3LnyXAq2xlYq62LhxGO4rmY9HUKPoW0YAwebnPTgMkWfkFIsgr8bAJmiRdhn0z9EZ0ht42eKJixbyjf_eXT1_hPjGNMn8_RtrRlQSJk1JzULqRAoBMsdnRwzSLbTJLgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۵ هزار نفری گردان‌های «جان‌فدا» در شهرری  @Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/462515" target="_blank">📅 21:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389a3dbfe1.mp4?token=D2QjZhyndp8ckqYBjSQF7xoSRYunz2zAAuIBHY7LjBGpOtYP5r2B53pTTPtHYO_ak4JMf2WwdR88M8bXzALAZd3Pm8MyT2ttkLSyXmgGy_hUFcPttQmiDQKAcyZzqmHW2ci8zWUPLAD-2ZC-C4JPyY2xjaKZ13pD3Dql4O7cpqPMGwjQQ5lOw9SuGIB71xwbrYu88xoFMqLTcTMjUIeRAgXM384fzHB1o4IefKAlLh-G1Swugpo4oR86uetY4mbIilPuF6g4XQ5-Zdq-9JmTL_eJxqFMth9DfTDumdE_N7lYokUIvXGiaL4Vj2jraZu1kZQyhnDT7AJzTPKUQugSfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389a3dbfe1.mp4?token=D2QjZhyndp8ckqYBjSQF7xoSRYunz2zAAuIBHY7LjBGpOtYP5r2B53pTTPtHYO_ak4JMf2WwdR88M8bXzALAZd3Pm8MyT2ttkLSyXmgGy_hUFcPttQmiDQKAcyZzqmHW2ci8zWUPLAD-2ZC-C4JPyY2xjaKZ13pD3Dql4O7cpqPMGwjQQ5lOw9SuGIB71xwbrYu88xoFMqLTcTMjUIeRAgXM384fzHB1o4IefKAlLh-G1Swugpo4oR86uetY4mbIilPuF6g4XQ5-Zdq-9JmTL_eJxqFMth9DfTDumdE_N7lYokUIvXGiaL4Vj2jraZu1kZQyhnDT7AJzTPKUQugSfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا از قدرت موشکی و پهپادی ایران پرده برداشت
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/462514" target="_blank">📅 21:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c39512b85.mp4?token=RgDeo3rqplo3_qZK6I5O8KrjIQtvovt0M1WbLN5rEnC_9MvddzuyttyM-Hs5x_6wPDY_CByy-WZDEwWP_BR4oXHKGfIT-8jPsXwmaARM7Xh-fikRdW-zM9vVYMTmPjs9JJabRO_mRluP28lXerrY96J00rUvi0p5pnY3BE_n4-1nVtX3z_s3f0AWw5i74hFegxdeHyQrblZDytugNBDvYOmbVihKECEnTi52wh5_ibm0R-frWMrlRFeUCKkXPcQ-IDFYOP2Vo-f9JdhP9BF71qY4VbDb3hZJLiPIopPy76_S7u-I6iFWADxpTBFUJdLXyY34Lp9unVjPVNBaOLzeKxRhoZKnzBVq9HNCo-ZjL6oz-76YrpHFfyezTP-xMJnz7coajgX-RkoGd6YwepQDabh1ZsqZR07TSnCv_-dZYTPA1lWjj0yKf8jpu5dx1m7OY6H9lT7GlEr-jBevGp4l-2vMk5ePMd-qdKVTEArBCSLnyRvxfeWTYVYQpmk8lyHZgn3-0IOj9DI2fKXn4kMVWUyKMw7eDE_6TlvZjdn3blS4n8YjGyWusAWtuwf1IlnthPRLmzOA3atXtDdooFP8hEil26bi0CVc-Lgjt1xlQzOzFZmb3H68NQxtDbb7VuDf-3lYqRrx91IA_eQaBpErONvQ9p7wZE2xe3Syxa_6k2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c39512b85.mp4?token=RgDeo3rqplo3_qZK6I5O8KrjIQtvovt0M1WbLN5rEnC_9MvddzuyttyM-Hs5x_6wPDY_CByy-WZDEwWP_BR4oXHKGfIT-8jPsXwmaARM7Xh-fikRdW-zM9vVYMTmPjs9JJabRO_mRluP28lXerrY96J00rUvi0p5pnY3BE_n4-1nVtX3z_s3f0AWw5i74hFegxdeHyQrblZDytugNBDvYOmbVihKECEnTi52wh5_ibm0R-frWMrlRFeUCKkXPcQ-IDFYOP2Vo-f9JdhP9BF71qY4VbDb3hZJLiPIopPy76_S7u-I6iFWADxpTBFUJdLXyY34Lp9unVjPVNBaOLzeKxRhoZKnzBVq9HNCo-ZjL6oz-76YrpHFfyezTP-xMJnz7coajgX-RkoGd6YwepQDabh1ZsqZR07TSnCv_-dZYTPA1lWjj0yKf8jpu5dx1m7OY6H9lT7GlEr-jBevGp4l-2vMk5ePMd-qdKVTEArBCSLnyRvxfeWTYVYQpmk8lyHZgn3-0IOj9DI2fKXn4kMVWUyKMw7eDE_6TlvZjdn3blS4n8YjGyWusAWtuwf1IlnthPRLmzOA3atXtDdooFP8hEil26bi0CVc-Lgjt1xlQzOzFZmb3H68NQxtDbb7VuDf-3lYqRrx91IA_eQaBpErONvQ9p7wZE2xe3Syxa_6k2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی پویش ملی جان‌فدا: در پویش ملی جان‌فدا تقریبا همه مسئولان تراز اول کشور با هر گرایش سیاسی ثبت نام کردند
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/462513" target="_blank">📅 21:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ7Gq1nUKFLT04fp9DnZDQcrreANO_NbBCWu0K_n_jR9LSfaiG1WoEzHln7w972FAX8RDcOU-0CE84ATWwZGFi5jpxAfsOJu9hifa_wG2KRDHNzsS_BAsUQ5Igr25D5Sfw9CCgPgSmcABSFqMtrksgIlgG5vJOF3bsJjVRzu7DIjKDGbwQ_bS-FgV05PGCwg7KycMwnYJ6RFET3ObaMq-tvuka5xOB9naWjM0MP9jB9bvhgt_dFH9082Tz0Yuzj3dNdp3BFj0U6J4EhJn7dDuHUIAOttELfSwiRG3JtYbrwRUqHJs5ksfttiawMYHHC7dqnn_rny2GbK_JeDzutElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکاف میان ترامپ و هم‌حزبی‌ها بر سر ایران باز هم عمیق‌تر شد
🔹
در رأی‌گیری مجلس نمایندگان برای پایان دادن به جنگ علیه ایران، سه چهره جمهوری‌خواه دیگر به مخالفان جنگ پیوستند، موضوعی که مورد توجه رسانه‌های حامی و مخالف ترامپ در آمریکا قرار گرفته است.
🔹
به گزارش سی‌ان‌ان، مجلس نمایندگان روز سه‌شنبه به وقت محلی طرحی را تصویب کرد که بر اساس آن، از رئیس‌جمهور آمریکا دونالد ترامپ خواستند که جنگ علیه ایران را پایان دهد. این طرح نیاز به تأیید سنا نیز دارد و حتی در صورت تأیید، باز هم ممکن است با وتوی ترامپ، رد شود.
🔹
اما تنها چند هفته پیش از انتخابات میان‌دوره‌ای، این رأی‌گیری یک انتقاد سیاسی جدی از نحوهٔ مدیریت جنگ توسط دولت ترامپ محسوب می‌شود.
🔸
این سومین بار است که مجلس نمایندگان به ترامپ دستور می‌دهد که نیروهای آمریکایی را از درگیری‌ها با ایران خارج کند. با این حال، دموکرات‌ها می‌گویند این رأی‌گیری مهم‌ترین تلاش آن‌ها تاکنون بوده است.
🔹
این بار ۷ جمهوری‌خواه از این طرح حمایت کردند، در حالی که در دو طرح قبل تنها ۴ جمهوری‌خواه رأی مثبت داده بودند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/462512" target="_blank">📅 21:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a37ba4c21.mp4?token=Yz6yz60twU85jX7NhxxJKwpxypZH-CGmE2Bf_KmC8Hj8umKZMf3aOzfxIz5pCLW4MKfiJpiMf8rtTQbTwmo_wHv3RKuLr6kcI0NrN11eBFQrPGDSCP5dcMup348G8VpoUHuoVswvVcCy0svaa2Kl_9bfT4Iykd_AAxfs_etB9SaouEQXfyuUQdse6BTtaS4X8hDGnAtfELIY2-JrsrKAoAEbp0gPhBYHgYVDpe8Yaz0mqBvKM6QCqz6rxlRninR9mXDNaq4xPBKrjMlCA8TSm63zM68vBal2cayDmJuX_5pL2lfE6GDvFIGUhKfbkuLaYDeLhGLPZM9eYqrFaeITng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a37ba4c21.mp4?token=Yz6yz60twU85jX7NhxxJKwpxypZH-CGmE2Bf_KmC8Hj8umKZMf3aOzfxIz5pCLW4MKfiJpiMf8rtTQbTwmo_wHv3RKuLr6kcI0NrN11eBFQrPGDSCP5dcMup348G8VpoUHuoVswvVcCy0svaa2Kl_9bfT4Iykd_AAxfs_etB9SaouEQXfyuUQdse6BTtaS4X8hDGnAtfELIY2-JrsrKAoAEbp0gPhBYHgYVDpe8Yaz0mqBvKM6QCqz6rxlRninR9mXDNaq4xPBKrjMlCA8TSm63zM68vBal2cayDmJuX_5pL2lfE6GDvFIGUhKfbkuLaYDeLhGLPZM9eYqrFaeITng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قریشی، تحلیل‌گر سیاسی: نگاه فانتزی به صلح خطرناک است
🔹
این‌ تصور که به هرکس در منطقه یا جهان علیه ما اقدام کرد گل بدهیم و روبوسی کنیم جالب است اما امکان‌پذیر نیست.
🔹
بزرگترین حملات تاریخ سوریه پس‌از سقوط بشار و عادی‌سازی با اسرائیل اتفاق افتاد و تمام امکانات…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/462511" target="_blank">📅 20:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39c85ba54.mp4?token=TYMQaix-n_XPf3cavyrVAi9A7K3QfnZ1_-RsNvqFsmuyo4MTlwrY_lFze3_ItPnWQrJ694HmuZgznHi1akmzHzjMZzXFDw9L_ZV1nH7T_F_rY_QaF8f3yAD_x9op5oYt4fEhkrSwSohRRAWVXKHBzimDGlecVwgjavdA1mbJDLYlUXV25k5UXr6vD12fjJQcT0jBqAJguHRuIMP_dcD_2eojRuXpyHgi2Bt6EwZ_x6yQuQ4nyFk7-Mqb3ngN437_UKCYqKCv1I4vxS9jnTTD-FhCtAkQrR4qYA1VQIe5JlVX87k9djPNpgGCapyXgMvPfkbt5ag6k8ITED9Hs7wbxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39c85ba54.mp4?token=TYMQaix-n_XPf3cavyrVAi9A7K3QfnZ1_-RsNvqFsmuyo4MTlwrY_lFze3_ItPnWQrJ694HmuZgznHi1akmzHzjMZzXFDw9L_ZV1nH7T_F_rY_QaF8f3yAD_x9op5oYt4fEhkrSwSohRRAWVXKHBzimDGlecVwgjavdA1mbJDLYlUXV25k5UXr6vD12fjJQcT0jBqAJguHRuIMP_dcD_2eojRuXpyHgi2Bt6EwZ_x6yQuQ4nyFk7-Mqb3ngN437_UKCYqKCv1I4vxS9jnTTD-FhCtAkQrR4qYA1VQIe5JlVX87k9djPNpgGCapyXgMvPfkbt5ag6k8ITED9Hs7wbxIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بازار فردوسی سنندج
🔹
با نزدیک‌شدن به آغاز سال تحصیلی جدید، بازار پیاده‌راه فردوسی سنندج رونق گرفته و خانواده‌ها برای خرید لوازم‌التحریر راهی این بازار شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/462510" target="_blank">📅 20:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رکورد تاریخی عدم بازپرداخت بدهی وام‌های خصوصی در آمریکا
🔹
موسسه رتبه‌بندی فیچ می‌گوید که حدود ۶.۳ درصد وام‌های بخش اعتبارات خصوصی شرکت‌های آمریکایی طی ۱۲ ماه گذشته وارد وضعیت نکول شده‌اند.
🔹
یعنی شرکت‌های وام‌گیرنده نتوانسته‌اند پرداخت‌هایشان را طبق شرایط قرارداد انجام دهند.
🔹
این آمار جدید درحالی‌ اعلام شده که بازدهی اوراق قرضه ۳۰ ساله به بالاترین رقم ۲۲ سال گذشته و رقم درست پیش از بحران مالی ۲۰۰۸ رسیده و بازدهی اوراق ۱۰ ساله هم دیروز به بالاترین رقم ۱۹ سال گذشته رسیده است.
🔹
اوراقی که با شوک‌های انرژی سرمایه‌گذاران را نگران شعله‌ور شدن تورم در اقتصاد آمریکا می‌کند و آنها سودی بیشتری برای این اوراق درخواست می‌کنند که تورم‌زاست.
🔹
حالا که قیمت نفت آمریکا بالای ۱۰۴ دلار و قیمت بنزین و گازوئیل رکورد زده، نکول وام‌های خصوصی شرکت‌های خدمات درمانی و صنایع و تولید در صدر قرار گرفته و در ماه آگوست ۴۵ موارد نکول در مورد تمدید سررسید بدهی بوده است.
🔹
فیچ تنها عدم پرداخت اقساط را نکول معرفی نمی‌کند بلکه مواردی مانند تمدید سررسید بدهی و تعویق پرداخت بهره، ورشکستگی و انحلال و تبدیل بدهی به سهام و موارد دیگر را هم از مصادیق نکول می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/462509" target="_blank">📅 20:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزارت دفاع عراق صدور هرگونه گزارش اطلاعاتی دربارۀ قصد عربستان برای هدف‌قراردادن مقرهای الحشدالشعبی را تکذیب کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/462508" target="_blank">📅 20:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao_A1RCU6CUNLOODo3NKpb0Ej9SuilCTS-L9CreuznlLrL7fYK3FqwD6cYGaF027pjrHPm_P_YroL2t0VyunJsgGuHR1N1u7d7dZyz6ia6OTR0OV5fOxTTVIONk1VoJ5t7NbNbZLLgssD-LNDUyiHCpd7M372OOSWEL5CC8GnJkGJZGVgKo1VhwkkgfSesOte7Nuz1sf5F5wgoAftM7lTYak-tuzOY1o6Itnvgws1pAO9TXObfxUJ85VCaVTVczD_PI1R0n29KE0-IfOT8g8CHcyg54lOPCfH7PO4nhaYXhdxuorlmPvv6V4LEuDHbMqvtS42KTdhnwb_vfRWv4kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس ستادکل نیروهای مسلح: از میدان رزم به شما مردم خبر می‌دهم که حضور مقدستان باعث هراس در دل دشمن شده
🔹
این بعثت مردم، یادگار امام  شهیدمان و ابداع مردم مبعوث شده است.
🔹
مردم عزیز ایران! از میدان رزم به شما خبر  می‌دهم که این حضور و اتحاد مقدس شماست که موجب تقویت روحیه رزمندگان، افزایش قدرت‌ ملی و هراس در دل دشمن شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/462507" target="_blank">📅 20:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنگنده‌های سعودی را با پدافند فراری دادیم
🔹
یحیی سریع: نیروهای مسلح یمن دقایقی پیش موفق شدند دو جنگندۀ سعودی که از پایگاه‌های خمیس مشیط و طائف برخاسته بودند را در استان صعده رهگیری کنند.
🔹
این جنگنده‌ها با استفاده از موشک‌های پدافندی…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/462506" target="_blank">📅 20:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49232f1f4c.mp4?token=RyDUg_GthW1K-R6FBACpb3K0JyP5xew0dIJTRX3x3RJgHdApj9pqK0fvvNS9AX4_cjy2_bWBZDZNNyVH76e9Z9lXnGUfmdZYyz_5qUdC4VBJideMUPghXOtBck2t4w80VIsnLObAvKmNMd1xxQ4Qo-ISOKQCRwuggBHneBJ9YqjYbvCuJQGYuuOun9tjOeJ_AvZcP2vXtG_iPb7X5pVAoIWsHQb-2A2t_YwbneJQE7viKYp_szlapsen94Wtgjzv9kT0f8XvfvfJq_QL7TvVmRY9UtjDTG_YcSAFXynoSIqymLgD9eJlFW9jhjKXHECrcXyBBwJAl8vrtfifVJ3S4ZwFzAUYeT53j4iJdP6OT-4zpx4QAVK-FfjtxQpL-lKCyBqVgBDOAt0tU7kTru8qhztH8FUfHtNrXGO3a6YspHr_x1uD4yIB5vDZrGScKsy2FAT97Dkp94NddneZotxt95uPA2wNja7ZUG2gfwWWzCQVf2bDwHBTTLhomIXY194wFkBspbLj8D7wp7K6veahhjbCtHh9e02PcoVA9RIkDwfYy0A6XPjjgbEXW6HWC-tVZ7wdaytmxumsXhpvLSRo4xqABGGXQHzCa3HqoapGITHX_3Dgzv9z3jqr15NZlWycVAEn7hRCmZ2rYZo6EyGisT7i6fNkNTp1LNpDfRNtifo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49232f1f4c.mp4?token=RyDUg_GthW1K-R6FBACpb3K0JyP5xew0dIJTRX3x3RJgHdApj9pqK0fvvNS9AX4_cjy2_bWBZDZNNyVH76e9Z9lXnGUfmdZYyz_5qUdC4VBJideMUPghXOtBck2t4w80VIsnLObAvKmNMd1xxQ4Qo-ISOKQCRwuggBHneBJ9YqjYbvCuJQGYuuOun9tjOeJ_AvZcP2vXtG_iPb7X5pVAoIWsHQb-2A2t_YwbneJQE7viKYp_szlapsen94Wtgjzv9kT0f8XvfvfJq_QL7TvVmRY9UtjDTG_YcSAFXynoSIqymLgD9eJlFW9jhjKXHECrcXyBBwJAl8vrtfifVJ3S4ZwFzAUYeT53j4iJdP6OT-4zpx4QAVK-FfjtxQpL-lKCyBqVgBDOAt0tU7kTru8qhztH8FUfHtNrXGO3a6YspHr_x1uD4yIB5vDZrGScKsy2FAT97Dkp94NddneZotxt95uPA2wNja7ZUG2gfwWWzCQVf2bDwHBTTLhomIXY194wFkBspbLj8D7wp7K6veahhjbCtHh9e02PcoVA9RIkDwfYy0A6XPjjgbEXW6HWC-tVZ7wdaytmxumsXhpvLSRo4xqABGGXQHzCa3HqoapGITHX_3Dgzv9z3jqr15NZlWycVAEn7hRCmZ2rYZo6EyGisT7i6fNkNTp1LNpDfRNtifo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ اتفاقی مردم را از میدان جدا نکرد
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/462505" target="_blank">📅 20:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8Hz2xWoYcpOs88qBE8Fi6lc4iN05wbbMVzeUrdYtEWMk6-AS_uD3NGQBX2GrkBtJauaihtCVXjZzm2UPqStLT6RdrMe5rRHomQPsEog4XZ4fQYDRslUexuNTMOGZUmLcM55kJdJZJ3MhJ7CWvvTmaGcWSNyeoiITmIoLplUC9J7BcKmZdT5dvpkMNITIhYVOPbTKgZ55i6IyFnd3u7ji-z9iocLy6ywCTQfam2fc2LoBuBhgd7_UAgZI5wIGM1HFFbAGulxKvUTsmhNJkIpW79alwZA0Jzw5zaCPqG-rd0t6hDWpf0fiCE1jjApJM4fx5Ipqa-KLNTJ6srK93Ad7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: به‌هیچ‌وجه به آمریکا اعتماد نداریم
🔹
سرلشکر رضایی در دیدار با رئیس اتحادیۀ میهنی کردستان: باید به موضوع گروهک‌های تروریستی، ایجاد امنیت در مرزها و افزایش همکاری‌های اقتصادی رسیدگی شود.
🔹
باید نسبت به تحرکات رژیم صهیونیستی در اقلیم کردستان عراق هوشیار بود.
🔹
به‎هیچ‎‌وجه به آمریکا اعتماد نداریم و آن‌ها باید اقدام عملی انجام دهند و اطمینان ما را جلب کنند.
🔹
بافل طالبانی هم در این دیدار ضمن استقبال از ارتقای همکاری‌های اقتصادی، امنیتی و دیپلماتیک، بر لزوم حل مساله گروهک‌ها و ایجاد امنیت در مرزها تاکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/462504" target="_blank">📅 20:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7770270e1.mp4?token=Q9GcQ1NOa1fK_lRbnlYIBDIPi0cvgl_0FzcW-zLnNaHBGXBNADwTc6HN6M1xr79ZJvolnsbCMHxAJS4Cx2yzOTGp-XVOYoQOii3Tus1y4QuSA9L6uZnztoqplsbD0MpI7XG3rGnuSYAmyvATvLVkWRlJPTMT_9QKuMnZ30GQ1VbrrcP-J63DrWSmyyNVLdqO1YLx0GJPSzx-WPI76G5F3CtqanNpNlnCc0qP0hZTNJGdAp65beHc33qxx_jAxQ-IeRB_mu40pvj2Ub4cz8joIu_ghMl6zwiD3Dtw42yDbzx8arnkTiZMK6Kl7usq1auf0RTEmUcFpdfjYaYhT3wvgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7770270e1.mp4?token=Q9GcQ1NOa1fK_lRbnlYIBDIPi0cvgl_0FzcW-zLnNaHBGXBNADwTc6HN6M1xr79ZJvolnsbCMHxAJS4Cx2yzOTGp-XVOYoQOii3Tus1y4QuSA9L6uZnztoqplsbD0MpI7XG3rGnuSYAmyvATvLVkWRlJPTMT_9QKuMnZ30GQ1VbrrcP-J63DrWSmyyNVLdqO1YLx0GJPSzx-WPI76G5F3CtqanNpNlnCc0qP0hZTNJGdAp65beHc33qxx_jAxQ-IeRB_mu40pvj2Ub4cz8joIu_ghMl6zwiD3Dtw42yDbzx8arnkTiZMK6Kl7usq1auf0RTEmUcFpdfjYaYhT3wvgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۵ هزار نفری گردان‌های «جان‌فدا» در شهرری
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/462503" target="_blank">📅 20:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4HcOM8nNtGaOKhXRucBkbxM8sNInTCeND_sclPFnk-5b3ED3HjNc3Iun0D2Q9gyImwK_Q0-t9NZ5e5BvyQSoqTT-6SD7d5mmdvKtoDYVLb81R7HB2MYQ2tN1LNew2AgV_rAPszDKovqL1qJMJ4-7vZ_P9SbhnAtanfloX_dE31O_y_u24D9dO2_mR0yiAWpewdOlrGL4oGFtrIfX089sf41jJT-jG64KOqrxQqNYoQNyUI0bDuHIQILLJzVaQbcGzFIoVtqX2XmRbde61lmarwHI2GSDnWxOOcLRyeVC57kc7tCgw-TPI3nvas-_EfoSaDQ_UbgVaHIrmNNRb9yXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمک ۱۱ میلیون دلاری آیت‌الله سیستانی به آسیب‌دیدگان جنگ ایران
🔹
هیئت اعزامی دفتر آیت‌الله سیستانی در سفر به ایران، از اختصاص و توزیع ۱۱ میلیون دلار کمک مالی میان ۳۶۰۰ خانواده آسیب‌دیده از «جنگ رمضان» خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/462502" target="_blank">📅 20:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXwa-ttpT2hmGR3z55amg77rY0nqS4dhehaKIOmpQP2m6YnQlwcjRRjeorawl7N1ukqULLmYPINxJC-V-ouwTkkk6vN1epWY40oDVWojif-MbOQvk1_lamqnqm0uyH91JkTzfC1tAVQpE_SFwSsJDevx0Z9TQDbJA7-JMEWlZD-YVJtwQaKow1erRRCtaiBYCDmoCih7JmTzfTrxd2kGJuH2LCs6IXpVWuXJMvaF8F0TMX_ZkImZiqnRy621TMnT9BGxDNTq0YDkKnO-AJ19NNgrs9VPWTN5aT8dNz4ZQMFH11bznxKe5si4k7UfrlPSXh9Uxzr_-41m7XRhoYJflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ جانشین رئیس سازمان نظام وظیفه: بیرانوند از یکم مهر باید در اختیار یکی از تیم‌های نظامی قرار بگیرد؛ البته پرونده ایشان در حال رسیدگی است.  @Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/462501" target="_blank">📅 20:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51468d3e5d.mp4?token=n63992A17IGBm7MSfyyypu_9eHRBAzF8DAWnX84n2bIC_xkHzB1KcDe0wUKTXwJSbqfeWaHHRpdNV2AVrsbC-yiFI6VYKmzDOnGflDTbie3VJhN5oXuS9TNeC9zckDY9CfuD2Ium03cMbCPjNjSFQlqYBCwHrKpdpW9ThpkC3W3QJz7QrpKCKxSssimdBOH2RckVqSC7SY_mun2upLu9tPTyjRTuPJ4ySMVrNj7P_QYlwoD6bIPAjSqFlMRiMIxXaU6KjPAIaXixch8nKXkkvVBCI0zqyr714qW7AwW17d5wbWpZvhj1OvqTQVPXqchZh5wPa1bipf2FmDm-rY_A7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51468d3e5d.mp4?token=n63992A17IGBm7MSfyyypu_9eHRBAzF8DAWnX84n2bIC_xkHzB1KcDe0wUKTXwJSbqfeWaHHRpdNV2AVrsbC-yiFI6VYKmzDOnGflDTbie3VJhN5oXuS9TNeC9zckDY9CfuD2Ium03cMbCPjNjSFQlqYBCwHrKpdpW9ThpkC3W3QJz7QrpKCKxSssimdBOH2RckVqSC7SY_mun2upLu9tPTyjRTuPJ4ySMVrNj7P_QYlwoD6bIPAjSqFlMRiMIxXaU6KjPAIaXixch8nKXkkvVBCI0zqyr714qW7AwW17d5wbWpZvhj1OvqTQVPXqchZh5wPa1bipf2FmDm-rY_A7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین فرمانده سپاه: دشمنی که درصدد بود نظام اسلامی ما را دچار فروپاشی کند خودش امروز در وضعیت نظامی پرمشکلی قرار دارد
@Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/462500" target="_blank">📅 20:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d6604c6b2.mp4?token=Q2zB4GfHfXYR8p0dax4BTCltnfyd-q2AhCJRLGlozt3x-Swvochg6ERIcUYINhSvkJHvKUyrWbbImmqs0v3UOjK2vqFq8dZXpyDYQlpu2hIQlEuVEW_yP7DYEJj45Pc5DA8EmFPDsMggXU4_28uknAHUeSlmTV47CXQ6FetYhOu3u3AtbWTm0Ngtux9KwwL0nVXguUKxTXYkJ-pUlnmTxB8O8S2NVi3Uc725EcxSQpgQFqLdUVTduipoi0qsoQsZ59qA0OpVmr8Fn_D3W1pLDpPBtK_tDcvNGA1LAJjxxO2gGdEeYPUKtxl4E2hZa4DNYCE34l2jhbZnPTPVPgA9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d6604c6b2.mp4?token=Q2zB4GfHfXYR8p0dax4BTCltnfyd-q2AhCJRLGlozt3x-Swvochg6ERIcUYINhSvkJHvKUyrWbbImmqs0v3UOjK2vqFq8dZXpyDYQlpu2hIQlEuVEW_yP7DYEJj45Pc5DA8EmFPDsMggXU4_28uknAHUeSlmTV47CXQ6FetYhOu3u3AtbWTm0Ngtux9KwwL0nVXguUKxTXYkJ-pUlnmTxB8O8S2NVi3Uc725EcxSQpgQFqLdUVTduipoi0qsoQsZ59qA0OpVmr8Fn_D3W1pLDpPBtK_tDcvNGA1LAJjxxO2gGdEeYPUKtxl4E2hZa4DNYCE34l2jhbZnPTPVPgA9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قریشی، تحلیل‌گر سیاسی: نگاه فانتزی به صلح خطرناک است
🔹
این‌ تصور که به هرکس در منطقه یا جهان علیه ما اقدام کرد گل بدهیم و روبوسی کنیم جالب است اما امکان‌پذیر نیست.
🔹
بزرگترین حملات تاریخ سوریه پس‌از سقوط بشار و عادی‌سازی با اسرائیل اتفاق افتاد و تمام امکانات نظامی سوریه نابود شد.
🔹
کسی که دنبال سازش و تسلیم است باید نمونه‌ای بیاورد که کشوری پس‌از تسلیم مقابل دشمنش به موفقیت رسیده باشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/462499" target="_blank">📅 20:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahVYB4f3OGwSHSyescUQ4B-rEJUvBSCRELl0OoyX46RRRXu0rzi80QYvyJWWKlQIa0kVf1MyyuSuxZ2XnLetchBEt9c1e5mdN7omBuTfMo0bqxl4QA_7tHGqf5XuHCo22dlGFAyj8XdaPwDlnVrTxUQDox0XXpKCQNP2Tfs6pI8bvLw-gyastL4kDTLqECCdVgiQgioNFgrrAm1kpS0ZihkZrcjhXO-_9HOeVboGXmX2mOdIwyGgEkcSxqexujH391A-12f524a-Qd0pRKnbO3gqNsJhaOa1F7l6MgcodMxl23lXrqME_KzeV1zJd2QGGbkuIaXuZMM2eEEUVYIXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گازسوزی شدید تاسیسات تازه هدف گرفته شدهٔ آرامکو
🔹
تصاویر ماهواره‌ای نشان می‌دهد که فلرینگ گاز در ینبع در بالاترین سطح ۱۰ روز گذشته قرار دارد.
🔹
مفسران تصاویر ماهواره‌ای می‌گویند این یعنی که یک حادثهٔ غیرعادی در آنجا در حال وقوع است.
🔸
ساعاتی پیش نیرو‌های مسلح یمن اعلام کردند که تاسیسات آرامکو در ینبع را هدف قرار داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/462498" target="_blank">📅 20:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462497">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe4a3e84d.mp4?token=qhEe5cHAfn5iZ-9Svrqofwzq1QKD8XX0fQM8W0HHkV3fBrtuZhJMMSHRI4gk14TXim_p5uaPJTFN-Myuyd4gJtXNf198bxl2ArgqSw-XnW6KXyuyY7r5TtZBtTQPpJhfsjreDq8aGs1cuXdqaJKoXI6tkdO-5LvZOYZFgPhka-Y8odKuO-zR_sTP9wff8I13rkJeUny6RzGPEUIbO1ZVBydjPN4hWaLBzOSEGfarjx_DoB7yGENo69CpfQi8PZoBe3htoTdqAi0OWl6VpgOqYkSu8iMQ602HZLns-pHjQdAFI6IkLXoPdm3sNxV7wnHF_nVaakI3rlQcYaFJ0JxbQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe4a3e84d.mp4?token=qhEe5cHAfn5iZ-9Svrqofwzq1QKD8XX0fQM8W0HHkV3fBrtuZhJMMSHRI4gk14TXim_p5uaPJTFN-Myuyd4gJtXNf198bxl2ArgqSw-XnW6KXyuyY7r5TtZBtTQPpJhfsjreDq8aGs1cuXdqaJKoXI6tkdO-5LvZOYZFgPhka-Y8odKuO-zR_sTP9wff8I13rkJeUny6RzGPEUIbO1ZVBydjPN4hWaLBzOSEGfarjx_DoB7yGENo69CpfQi8PZoBe3htoTdqAi0OWl6VpgOqYkSu8iMQ602HZLns-pHjQdAFI6IkLXoPdm3sNxV7wnHF_nVaakI3rlQcYaFJ0JxbQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۰ شب است که در میدانیم
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/462497" target="_blank">📅 19:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462496">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCIFICk-JJFMfjX9Agi8LPsCrThIwIQAVbzT6kDczZR0PGS4Xhm1CG1SbYl-vnitbVehalu8yWowxR86YFn6kE_3dg0s5WaoVfKl0d91yxx18EUrmkfvynLvd9YZQcocH6puO0iOVMEyNq5aWPziIuBEjSuACIAxS6AxwLEn3HT0iSlQH61Fch8a590_ahFuWROvPN2FEUkX7_KiqYY1X_ockEviavjkM9bQa-35Drlh4yZlwh7D-sST-39s8zdTVFnKmWdOjk6sLUxm-bCQCRJdEZcQU5Qj3geBf-eVNNZJpkTVLGArb8-s1W05JkOTyHYorFB-JyVwoTaImD-9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: برابر مردم حاضر در میدان سر تعظیم فرود می‌آوریم
🔹
دویست شب حضور شما در صحنه، در کنار ایستادگی و جانفشانی نیروهای مسلح، جلوه‌ای از عزم و اراده ملتی است که در روزهای دشوار، ایران را تنها نمی‌گذارد و منافع ملی را با تمام وجود پاس می‌دارد.
🔹
دولت در کنار نیروهای مسلح و پشتیبان مجاهدت آنان برای دفاع از کیان کشور، با همان جدیت در کنار همه مردم ایران ایستاده است.
🔹
تأمین نیازهای ضروری، استمرار خدمات عمومی، حمایت از تولید و اشتغال و رسیدگی به مسائل معیشتی و اقتصادی مردم با جدیت بیشتری دنبال می‌شود.
🔹
در این روزهای حساس، بیش از هر زمان دیگری به همدلی و وفاق ملی نیاز داریم؛ نباید اجازه دهیم اختلافات، ما را از منافع ملی و آینده ایران غافل کند. دشمنان این سرزمین، انسجام و وحدت مردم را هدف گرفته‌اند.
🔹
از صمیم قلب از شما سپاسگزاریم و در برابر صبوری، بزرگواری و اعتماد شما سر تعظیم فرود می‌آوریم.
@Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/462496" target="_blank">📅 19:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462495">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVndIJ3vF6pGn1Fi8l9CfgSQ4yqF89LNmdW4W3B7taSJKQ9DVixwbjKSuli74Zdlv3q6nxOoJGhH6H5npvW6dtuEAcx1q3b-_ZcGLRf_1FDPqWfnpASh3_0O_YFH0gicVX1RBXsN1Ei5ZUIHTtClDFEEgopx4sX62KV18yXTqJDUZb8-ZxCR4RKZ47jQJNZayf_9rzwclIdMInktaa8VBPvCjeLPIh-EMBL4Yt582FFl5GlFhgBbLmroAIfDxPsEhNKx_a3duxwyVtGnxfwlrahcoDcoHndyCJKL8HnspWYYSybs4fbrrzt2vGA0L9AEOkarfCopBjONFQMJzp9m5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه: آمریکا به ویرایش تصاویر و ساختن روایت‌هایی به سبک هالیوود عادت دارد
🔹
بد نیست نگاهی هم به لاشۀ آن جنگندۀ اف ۱۵ که در ایران هدف قرار گرفته بود بیندازیم که قطعات آن با فرغون جمع‌آوری شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/462495" target="_blank">📅 19:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462494">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سپاه حضرت سیدالشهدا(ع) استان تهران: ستون دود مشاهده‌شده در اطراف دماوند ناشی از امحای کنترل‌شده مهمات عمل‌نکرده دشمن در یک سایت نظامی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/462494" target="_blank">📅 19:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee610ee67.mp4?token=mYQgMP1WSa1gbOmGimcUVfOG084NKQIC8SPTEvEvs0atCSvDJ426KIXsGi6HF8xwPpSifaa_AlJXgfyQzBsI6panJCayy2NnpEDWh-Ding6YBkMdSYUc_dmwqEucHQzkex1WW8LPzO4-BKgAJc2q-nD7ZVrrb2HBGs2FLKVlFhyGVk0XFtBX9oBq4bXq413YM0aHoY5A0f920phcy-gToPTGgVbEApbgyPuQaBZEOKZLYFAGIU5yBPdMQtr04NoGjTfh-SjfK9sPieSpx7v-Ly2dm9xk2Lcn02qFjZeOpXiXpAYQy8BIlSEWYjOnr1jBxZv3WX0pLkP0GutoxYhxBFft7xJGQ450o5obbjdIu4SdFsqBMTbuFgkQ2jFY-8VIVgmlX_LIqXIyJiQA0qf8eZnUHSBGieWKMxVZvAiKvq4We62h-nDbKA3VYx2PAXNTDIytd7oOxRAj8ZiJVlTp26e4dXzKx_E2RkVdP62nhFGNCLk4qrlTv-2Yd3mxv0GDFzt9GqCFQrIhrYU4tFUa0G4ppgZ3arRk-lE-j8OGhDPeESEGOmHfmgWzohvDNJGY9ci3cDA8j-dDn2Nm9vEgBO9eyz9HH4FHagSITg23Zk6X-KoR9gjkKMzXjbq4NjSHsCIzu0WuFiJdBe6qAfgnkQK-YMwntwbccQ_qVYVZJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee610ee67.mp4?token=mYQgMP1WSa1gbOmGimcUVfOG084NKQIC8SPTEvEvs0atCSvDJ426KIXsGi6HF8xwPpSifaa_AlJXgfyQzBsI6panJCayy2NnpEDWh-Ding6YBkMdSYUc_dmwqEucHQzkex1WW8LPzO4-BKgAJc2q-nD7ZVrrb2HBGs2FLKVlFhyGVk0XFtBX9oBq4bXq413YM0aHoY5A0f920phcy-gToPTGgVbEApbgyPuQaBZEOKZLYFAGIU5yBPdMQtr04NoGjTfh-SjfK9sPieSpx7v-Ly2dm9xk2Lcn02qFjZeOpXiXpAYQy8BIlSEWYjOnr1jBxZv3WX0pLkP0GutoxYhxBFft7xJGQ450o5obbjdIu4SdFsqBMTbuFgkQ2jFY-8VIVgmlX_LIqXIyJiQA0qf8eZnUHSBGieWKMxVZvAiKvq4We62h-nDbKA3VYx2PAXNTDIytd7oOxRAj8ZiJVlTp26e4dXzKx_E2RkVdP62nhFGNCLk4qrlTv-2Yd3mxv0GDFzt9GqCFQrIhrYU4tFUa0G4ppgZ3arRk-lE-j8OGhDPeESEGOmHfmgWzohvDNJGY9ci3cDA8j-dDn2Nm9vEgBO9eyz9HH4FHagSITg23Zk6X-KoR9gjkKMzXjbq4NjSHsCIzu0WuFiJdBe6qAfgnkQK-YMwntwbccQ_qVYVZJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضری چندبار این‌کار را انجام بدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/462493" target="_blank">📅 19:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqdq4eE9XP5OVDKS7XwRUnFStLvid9ci3dl6rh_SrapNGcXBOptQ7Om-NxA7yFkRNaXaVcm3v6aGZ0mC5akJzaXD8xyczwp3W2gTTl1S6VYayLdDSqseq8sxrHwsleqDAvq4wXt0bY5ShKQ5akoIGY57UHu60MSfi6ZBhp3_0Gi_CTxYJlRsnD_jhg9D_NQpTlaHsUoNPeZHFok7YOVM4JsUyqTGwQ8FJqvCIEHgLGyzjFN8F-kVXft1I7a4zdauQgY8y6vVpdhcAbtH1kAtGpYvby52-8ag_lfRvbzQWin_9QdMDUtS6Xb7rFUT5eN6lNCJ0aB-Uxt5_huDz55mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۲۰۰ شب پایمردی و شجاعت
🔹
بصیرت و هوشمندی ملّت بزرگ ایران در واقعۀ اخیر و پایمردی و شجاعت و حضورش، دوست را به تحسین و دشمن را به حیرت وا داشت.
بخشی از اولین پیام رهبر معظّم انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/462492" target="_blank">📅 19:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS-SiSzveGl1gDw2jFNysl8h4umaPGgy78FWnzPd6Mg0C5tc81Z3lb_WdoHg7EhcIKsBJKe-wT4ulAK9Z_2guA9prkbZJCFcMakNYxeKKdU8muymAKhojk3i0w1kQ2ZkEPGu1opJ7wkb9m-3w2XOGFHGvGvHJLezYiislZ0oLKX6m-VRa-GDicn1dRgiYEneI-k3SaZFCpH6SOfT8J22HVq4dpwMgj4KR7xYa3rkmCWxd1hWsoX4l5MVQuJTGnmf7Xw8RPqidR9GnVC-FT21GyeukmW4-VvBGBjTLNXD-RjywtpghIyoN8eWtQl2dgvmKFNjg60nctMGFWhYenx1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  بارگیری نفت از بندر ینبع سعودی هم متوقف شد
🔹
رویترز: عملیات بارگیری نفت در بندر ینبع عربستان سعودی در حاشیۀ دریای سرخ متوقف شده است. @Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/462491" target="_blank">📅 19:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎥
رهبر شهید: حضرت عبدالعظیم؛ الگوی دانش، معنویت و جهاد است  @Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/462490" target="_blank">📅 19:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwWI30WgrMw7uTG2Hg0jL8Qrknyd_PJoNLHAmqb5IDNbdiavAUcNC5SWgt7d37CsgbjWieLL5bUZnsRLO8gVqKb0moj4b53GISVsbwOg9J9A7ECb7YlBRVgS9667UJ59mVbF25PJJaAF1lsfqnCwEO9PS1-f1FT8uUxykZQhY_vCOnVESZcfUn14O3BnpQGt57dhG3_mNGKp38quq1AtSKH4pibM8ZJC3ehoQQRw0CJq9wDMgvaqpIzkhTicuCSkiM8X_iaM0dvgssTu1z_SDN6s6fPsOLUOEVt9PDL63wcqIr21NRsIqcD66PjuzXGVoWnt5M8rRomdDNXYE2EK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: انتظارات تورمی آمریکا به تنگه هرمز و باب‌المندب وابسته شده است
🔹
بازی با نرخ بهره نمی‌تواند شوک تورمی در آمریکا را مدیریت کند؛ ریسک تنگۀ هرمز که نرخ را مشخص می‌کند و کنترلِ این ریسک اکنون دست ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/462489" target="_blank">📅 18:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a56430d0.mp4?token=aRejoE4XwQ0j7m1EstZ87glOQOpu8ZpaUvdTeELmI2xnRapxvd24j3Hi2BXJiO6D8OOb0EkDOw0N0_WQ4E3BeMNmGwIHSjt83O3cj0_cnckf374HJS9tF4ksFta8412tvC0lWj1Oiwo8KchiTtJTZVEInThfZqD64kMWrDst06WLqKc5Ajjwv053Zi6OTdtyhMAKqvU7pjL-Sq-ck3xKOSW4NUGzyr6HNdDj_m_0EE7vf_yYAiFEntn7INa6SNZBhNmzuHl7Gd5Z8kbWW_R5lhA3HxoK3o9jZU-af17Nv-AleYq8N56rM6ALiAaWUoCiV7td-4jtWN-2h9WkggEDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a56430d0.mp4?token=aRejoE4XwQ0j7m1EstZ87glOQOpu8ZpaUvdTeELmI2xnRapxvd24j3Hi2BXJiO6D8OOb0EkDOw0N0_WQ4E3BeMNmGwIHSjt83O3cj0_cnckf374HJS9tF4ksFta8412tvC0lWj1Oiwo8KchiTtJTZVEInThfZqD64kMWrDst06WLqKc5Ajjwv053Zi6OTdtyhMAKqvU7pjL-Sq-ck3xKOSW4NUGzyr6HNdDj_m_0EE7vf_yYAiFEntn7INa6SNZBhNmzuHl7Gd5Z8kbWW_R5lhA3HxoK3o9jZU-af17Nv-AleYq8N56rM6ALiAaWUoCiV7td-4jtWN-2h9WkggEDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پویانمایی لگویی دربارۀ پیروزی‌های جدید یمن
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/462488" target="_blank">📅 18:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRD-nOB_XaqWTxpIRR3QUyR6YlnEL-4y43hMjXM92UI9v_AxDsE9H5jPt9EAByK5-jcSfbqaua4qPxbTonuNY-c48DC2oDKxxFQrM5F-RVc38KcLGA352e2Z7DU6sjlY9xg4sbJEr1uRLssx7dlGnHbSM5QuaNue75mKwzFbkFYWT48MxdCzrTh4H4F-WCNmIFcudhZyRVNCmkiO339jKhm4wXUyaAu0jwXacAkmXuMUyUNhPbOkJf-O78vqdhjVsO1U_5NW2jBzWECdjSaLQ0OqdvY1ubiiKI-pr057DjZjpinZS9QlpA7PEl6-67vaCTRifdTNwNvdSOl8Jni7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمز بلای صنعت اروپا به اعتراف رئیس کمیسیون اروپا
🔹
فون در لاین، رئیس کمیسیون اروپا: از زمان آغاز درگیری در تنگهٔ هرمز، اتحادیهٔ اروپا ۹۰ میلیارد یورو (حدود ۱۰۴ میلیارد دلار) هزینهٔ اضافی برای واردات سوخت‌های فسیلی متحمل شده است.
🔹
این وضعیت بار دیگر نشان داد وابستگی کلی اروپا به سوخت‌های فسیلی وارداتی چقدر پرهزینه است؛ اگر قیمت انرژی به‌طور ساختاری بسیار بالا باقی بماند، اروپا نمی‌تواند به‌عنوان یک قدرت صنعتی باقی بماند.
🔸
براساس داده‌های پیشین کمیسیون اروپا، هزینه‌های اضافی انرژی این اتحادیه در ۴۴ روز اول درگیری حدود ۲۲ میلیارد یورو بود و تا اواخر آوریل به بیش از ۲۷ میلیارد یورو رسید. کمیسیون اروپا در ۱۳ ژوئیه این رقم را حدود ۵۳ میلیارد یورو اعلام کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/462487" target="_blank">📅 18:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiIVBq8yGjZ6L2z3ii2fOFV5N9OOSFmjkgxhqw3Lj1DNsNwnx-i5J_qndNcAXW2s2lYCNgRi0mmmOTFq8JtNIIzUiBaa2MI-keadVtrK8fek7bFoac5_h4OthJsJY6-Ekn9H91Dn_08Ju2MBOlvlCMIPrXQIXT0Z-ff4dJrTjQf3nw2Asi08IBPhVYhJi6MoQT0LKIdysqMS3dRJgOOSheF1NWtKsPwxmgW3QL4PRM2fZb3NKs_7kOtIhGITA-LIPtz6OSe2RrVY42_MPee1O73qGao_RhgF2LiND612_aMhKR_IECry-BxXZwvTI7EfHSa547oQSrvSnXqq9cTptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قائمیان: نتوانستیم جنگ ۱۲ روزه و رمضان را آن‌گونه که باید روایت کنیم
🔹
فرهاد قائمیان، بازیگر سینما و تلویزیون، با تأکید بر ظرفیت هنر برای روایت وقایع جنگ‌های اخیر گفت: این رسانه عظیم باید برای انقلاب و مملکت فعالیت کند، اما ما نتوانستیم اتفاقات جنگ ۱۲ روزه و جنگ رمضان را آن‌گونه که باید در مجامع بین‌المللی روایت کنیم.
🔹
هنر در دوره‌های مختلف تاریخی تنها ابزاری برای سرگرمی نبوده و همواره یکی از مهم‌ترین بسترها برای ثبت و انتقال تجربه‌های جمعی جوامع به شمار رفته است.
🔹
در همین راستا، فرهاد قائمیان بازیگر سینما و تلویزیون، درباره مسئولیت هنر در شرایط فعلی و نقش هنرمندان در دوران جنگ و پس از جنگ در گفت‌وگو با خبرنگار فارس، اظهار کرد: واقعیت این است که در رابطه با همین مسئله، باید اتفاقی بیفتد که بتوانیم برای نسل بعدی و حتی الان، در وضعیت فعلی، فرهنگ‌سازی کنیم
@Farsnart
_
link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/462486" target="_blank">📅 18:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۵.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/462485" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۴.pdf</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/462485" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462484">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یارانۀ شهریور دهک‌های ۱ تا ۳ واریز شد
🔹
یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/462484" target="_blank">📅 18:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9ni-QI3UjuLSi4AuJwBJ7YUm9Z8DBPlY1SY_Y1ht_ylHng76nuHLwHzcd3uRK-nUQPtyUBCApaxPc4H2qOzUj_gPTTfmvIWpKynKb_rkoAcH_Rt-qNfA3JEB38v6gp5DycSxuVLgQsIAAGNzNTl8bsMoBCvNh4jIa-x38OFcdZRMD7hKje1BHB2pq5-Knfmr0c4-OFwYtCAM5Toe27NpKu-Tn6qpoyHLCD_2AIZwPG7LSynNUswmQSf0Sjt8Bns7YJQhEVEov8kBCZk7hfjp7yzO-LG3JkoJDLdQEysYxkCfHMm7oEmjq9yoA_MzttmiL1bfxO1tG8yeihe-xzjJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصاویری از لاشۀ جنگندۀ اف۱۵ سعودی ساقط شده توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/462478" target="_blank">📅 18:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59ddcc549.mp4?token=qI5HyMYk-JqeRq_EJRBqMtaxZc5_OXs7AapGWqsBeelT6tE0Gyl8F-FrMfNlJi7RFnUbwjCM4RxD6G-kO8M4Yg1-Cv9uT2hmGyk4lQtvsEAKhgsfcfJKJENjGCzHVZcCVlIEwTuct7iNxXHvGfORqj6KMN_-N54CnLtfIZ9tsoye368x495iX_xMLGcUrWSlqAaMl5hZMvDZTy8nDSVnU1gygwZRSsNC9VpMUyj_-alI5APrV8RNoUIEDv_sr2UTI4v38FE43M7BC9Fk2PBOp5GC6dd9tkM1zFUkwSwpc3hIAwWqsXRpv1TrPKvtV9-LCI0n1ENhKQXAjqSgXR543TJzWO0AGdrVgF6Zui1pF6kpuiM-q27Zv900SscnUonojrypjPzTaPG5E-6-z0lEZ_At8hxjwy1VPkendDLuYmQs0c58KibLBTJQ1v2hvY9Sy-_TuYKDjykhjrj3ion5xwYYufGZtCZMY0O0qZdOSByWE3F8nc9FLr9UNUV0XkReqUr2C6ZOSdNcp9zsBY-8vKA8HQNq6xUkvQ1RzNnmFrjMaFYKRNbev7TALNTmEiCjBlgmzEkUJ4USkBCEr4-zzNK2B4We5iaEliwyR-7H-Fg4ux9lafcKf8SnImBktF43_Pel61r6yHonQPLgU-4SsV85cB0RCBdxoVthHVxvIL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59ddcc549.mp4?token=qI5HyMYk-JqeRq_EJRBqMtaxZc5_OXs7AapGWqsBeelT6tE0Gyl8F-FrMfNlJi7RFnUbwjCM4RxD6G-kO8M4Yg1-Cv9uT2hmGyk4lQtvsEAKhgsfcfJKJENjGCzHVZcCVlIEwTuct7iNxXHvGfORqj6KMN_-N54CnLtfIZ9tsoye368x495iX_xMLGcUrWSlqAaMl5hZMvDZTy8nDSVnU1gygwZRSsNC9VpMUyj_-alI5APrV8RNoUIEDv_sr2UTI4v38FE43M7BC9Fk2PBOp5GC6dd9tkM1zFUkwSwpc3hIAwWqsXRpv1TrPKvtV9-LCI0n1ENhKQXAjqSgXR543TJzWO0AGdrVgF6Zui1pF6kpuiM-q27Zv900SscnUonojrypjPzTaPG5E-6-z0lEZ_At8hxjwy1VPkendDLuYmQs0c58KibLBTJQ1v2hvY9Sy-_TuYKDjykhjrj3ion5xwYYufGZtCZMY0O0qZdOSByWE3F8nc9FLr9UNUV0XkReqUr2C6ZOSdNcp9zsBY-8vKA8HQNq6xUkvQ1RzNnmFrjMaFYKRNbev7TALNTmEiCjBlgmzEkUJ4USkBCEr4-zzNK2B4We5iaEliwyR-7H-Fg4ux9lafcKf8SnImBktF43_Pel61r6yHonQPLgU-4SsV85cB0RCBdxoVthHVxvIL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر شرکت توانیر: حداقل ۶ ماه حبس در انتظار اسخراج کنندگان غیرمجاز رمزارز خواهد بود
🔹
طبق ابلاغیه وزارت نیرو، محل کشف‌شده از برق یارانه‌ای محروم و به مدت یک سال باید تعرفه آزاد پرداخت کند. @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/462477" target="_blank">📅 18:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462470">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbp1QEK5C1QHKkNXs-CBPiW-eAWX5GVouw13CatgTOrolEJDs4n5ahIiVVFZTSwYrjXVjC5RqeWx7B-Lwpn84Uk-cz90GAQoQTFATcFuWBtYt2Zf4KPEgpAuiybAwmnfkuCXnQTFl-vZSzh4ze1gObsNUfNGI9b6SSbba9hgjD0BpctdsfArBnr1OZff13E9F9v52MIjwpikZLOZmpQgJGDVvPwKIgxgVRuFi-dJl4aGm9_z5d2ElOsNNRKfYgIIgPyePqbypedffpINjQHtZclMjJMZe3IitsmNf9bG4eCO7TvTPjr5duMPBdSIpy5lkp89EqAJOI5uZHg8d39KZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGR2OwJCxEeZPCCxuw9B2GobP7velspDg1YIIh6D_xh4crU5RBTV3b1lmn66X2pZBncXAyGhN7gJofAn_RhHjZKEI_1xu_y_l99xz8w_xpVLFp-3BUUdzMoVyDenZJ5-_FFjBx6Mj_5hCS_MCyr7EDmsrT2mZhyWW5GjE_VuovCwXQ99MvnZQWcN_nu-tgaTLdvHpydfyQmuZwtzHKpu5loJcVCi_NMtEFKjfy4oA-bUCgOeJGQClbiagVVxW34x3-45ChtM6ifWkMGGSdOQQi5NJweD7PQ_LLtFAzLxtYNfgYVnRO_q2QmRGhLh8p2uTaApLPET6afJ44MMohLpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyUxVJKMEAwuTygalD1qsLpDWKIKg23w6lx4ydrsDuhBgHFMdgAeAFKjAXOj8L5NWq39yJBGvSBaRd9XCO3UtBh6EIvB0dj9cGs3QWkxERbUCPZh9y33qSwfIKR7LfMVgRNN92Uhh7njFxqEQRS-CkFTP80KzxaJX41XpbCZwNblGmPZVCSzCVqmxb6VOA4zmaU42yWmA7X393NiA0geC-0aE-V3oIOMquQbyo-0a5b02vEaceS-i6r8oC_dWeUhlpcD2CaQPUJxf2n2DqYPmyBcp6UEaKDCUOETJS7buHEPcCc6Z4rCNVbdow8hRJk0ZrpTdXTNGU-L5Mzl6oAu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtCWRXHVUKGbR6yQcgq_hm8Z47eXs_WNfp-G3wD6QBeM5X8JHmn53GaDifglqICiY7wCgtxX2BlV6WXjTaISAv0EOh5i63R53fI1mFzGXUZ7kvGtFrqiLsFNaHqkxzZJ6aMfpHX16ChWiX6JD1eLvmfyo94MS8-lJZOG203JKGrLUIETKEahMGSnj6WjJvUnxwwb-zDHucIYbhMW_EJi6WrXXZ636kG-vSvefzJl8-y8TnDJhZuIlp2kQLK_DQQV2s8oMxjhL7BCZ1hUaNC3fraTaU_2MEVxyrtqxUfr2yljFCkXW3QouaaPjfluzcDRNGs8H34V9ADXaBGvaNr1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bD0YCkvcygHJX-F9aYscbb7VAlr3MtiW4usM6uH-uygBT79ijmmrGW8UvE-ffn5DJxXRsKqmLkbOvBtajEAvuaEDKkq87p6Dd1cds5jUeqlf1a2xzrjKAVZ_H_KboeUsAPPRO7bV8cQIauslRpUPgjeuIkV3CLZzAUR_2enF_fveGWu4OT_vgf2iwfYWbBr7tw0JUcDVZ3Zf7FHL6TPURIaQ_WHCF2NlZ5iHiXkb5AQlRm4rKZ4CvI52JtEjTi-FiWU3uv-PiZW3tN38kHgrVmutcpfNf7T2uxTYwaC74KvWXqv04W5FIJoGDgS9m5tPdrVzidSlsKPRZbJsEoiSKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edpL7R9Mxpu69Oi-Wfhmb4n2AJ2QlIA4kwU3I8cmsKFcQSnvE6-KjPZgToHWZJL2NSqy0Zs5IBKkL5GYbX4OP1IKzKep81afb0fXGz6iy2uPka2pPw7H13fJMVzHp-fevKqqQZTPJvzsDxeOn-ky22KNfvHVlVzX1eEqhflbV5-Uxe3sx3f4hvrakooZ-rYH5TkER8Fnlt7WpxnAcP_yTAAOLF1qjaMpYhoWuYX-qES3balVOPjlw8cPVomSgL7fL_D4NLGBuoTBDD774krB0LzsT8bD_IKBNKMz5dc9GurL__yIWvw7bFPNUZiEOm4CbuaSKPctbD1-QoGmdTFl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knfLLwAYwziRHU2ZYrJod_9GxEeqqCvfzhEQe_DgVn9JaLIj5NKBZVeAcD7y0xYKOIerejc6kFKPjKrLggs2tc14Bgsll4FR_AYkQdKaSIXBxXv-jQl0njvH6VFiXb5v-xCaR1LLYgdxyUaJursB5MIRYQcropbC2vN1D2LjMHrMOxXeqUJCqipwEuWVPfGuGBwu4JAFPhc8_S9mI3sF-KYGPOs-gMQI4AN_L2XOyaL9AoZ21yZtVeLHkvj8szvATTZ4oy9_p5vTVSSe3eSDwvEixNve3TGlYCQMBkcNAOM-uRef41A0GMUft_sQus4xEv9LB5ERiJkiUuYWzIFBMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تصاویر سرنگون‌شدن اف-۱۵ سعودی توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/462470" target="_blank">📅 17:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462469">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مدرسه‌ای که قابش از کلاس درس به رقص و قمار رسید
🔹
انتشار ویدیویی از صفحه رسمی دبیرستان غیردولتی «صعود» شهرکرد، حاشیه‌ساز شده است؛ ویدیویی که در آن صحنه‌هایی از رقص، بلاگری و استفاده از ابزارهای قمار در فضای مدرسه دیده می‌شود.
🔹
این تصاویر این سؤال را ایجاد…</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/462469" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438df848a9.mp4?token=go4miVcsi51CwJ1_5Lneg-NIkZyRcmRmjoGNYpK_N7CQhCkDzPotG6dEI0vYefW3Ak9K2WEZ7KbgIwfmLBji4si7mep2VoOV225Dq-cUnL_rVg5lLiiK51PQ_oFkVsW4EgKf7w6LKM4iwO_nTVXX7M5qeNkkzqif8nAjd3DjjmKDu4gh_HkLGKDJnVje5KegFpn44czK0eNLA_aG-k0iX91lnkWIuPyrYGfAJUtDbxU3-QcsXmxI8EpRRYdLzFHCEs4Lmhl_aHK1nVRNGdw6sapqWTgSCOic7-MnfFrvWMVpj3gT3WEG9IgYneO7tA2UH_uw8ONjAu4in2tTyOmOOxAwdoQBA6y95f-6i9pgJ2XXcumu0fWjdv9gqwXyyibh4Xrlwtsbyo86T_oF27mbKxtZTIp6y06Dc1RDneu2q-wnE12xz8jVOJKMGaYLtbOVGlUHbjs26u91KvWgYzTwvDRjs_qRAenBdAGiwPDFGDdIfabz34qa5Xf7xxAgTIRP_EXA8ZG1jrRbsml_MWo3HHq5VbX_aofAHbJ81__ITy2XZ7TSxf9jHCqXEYUPLIC4hN2Gb_IRNGiSZKGqQ4HHVfVKEdH9DaBPu28pKyWVPxsSjkeZG6BrcMt-qjS1rsZV_zyawLd1lsD2QREK4RUFzjgxOU_mDzgyDz2WSTmca0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438df848a9.mp4?token=go4miVcsi51CwJ1_5Lneg-NIkZyRcmRmjoGNYpK_N7CQhCkDzPotG6dEI0vYefW3Ak9K2WEZ7KbgIwfmLBji4si7mep2VoOV225Dq-cUnL_rVg5lLiiK51PQ_oFkVsW4EgKf7w6LKM4iwO_nTVXX7M5qeNkkzqif8nAjd3DjjmKDu4gh_HkLGKDJnVje5KegFpn44czK0eNLA_aG-k0iX91lnkWIuPyrYGfAJUtDbxU3-QcsXmxI8EpRRYdLzFHCEs4Lmhl_aHK1nVRNGdw6sapqWTgSCOic7-MnfFrvWMVpj3gT3WEG9IgYneO7tA2UH_uw8ONjAu4in2tTyOmOOxAwdoQBA6y95f-6i9pgJ2XXcumu0fWjdv9gqwXyyibh4Xrlwtsbyo86T_oF27mbKxtZTIp6y06Dc1RDneu2q-wnE12xz8jVOJKMGaYLtbOVGlUHbjs26u91KvWgYzTwvDRjs_qRAenBdAGiwPDFGDdIfabz34qa5Xf7xxAgTIRP_EXA8ZG1jrRbsml_MWo3HHq5VbX_aofAHbJ81__ITy2XZ7TSxf9jHCqXEYUPLIC4hN2Gb_IRNGiSZKGqQ4HHVfVKEdH9DaBPu28pKyWVPxsSjkeZG6BrcMt-qjS1rsZV_zyawLd1lsD2QREK4RUFzjgxOU_mDzgyDz2WSTmca0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: اف-۱۵ سعودی را در آسمان مأرب سرنگون کردیم
🔹
یحیی سریع: در مواجهه تجاوزات وحشیانهٔ جنگنده‌های سعودی به کشور و مردم ما، نیروهای مسلح یمن با کمک و فضل خداوند، موفق به سرنگون‌کردن یک جنگندهٔ اف-۱۵ سعودی حین انجام عملیات خصمانه در آسمان…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/462461" target="_blank">📅 17:48 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgts4IKoDOdUVwHoKjBALdCAN41Jnwiwt2ijKu9odDoQBHEt5wbbMpwB3qU2O-ZMZtFuEQLWrxGLzamhDWGBNmC75XWriBVYge-gN---SoMegWp7bU3gxGhCGxl8u35HEC6KfP-LWvMfqzYYJh6RDodmN7cLos_5BlC5mT3c5zzCsj0bAlVwyalCyEsloZX32Zj9Ii_27dTQVPmZQ7yQftItIXyiYFA5GeDmO0_76wNigFx43XgDjS07blIEB8EBcfPeip4EGaAROVzEpp-U05nW-nbbChvmHZt5SggglBgOb4DXa7yfuf7Su_zjSZYwze2XFFASYFIaagftbXnnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: آلمان نمی‌تواند آشکارا از «کار کثیف» پشتیبانی کند و سپس خود را قهرمان صلح و معلم اخلاق جا بزند
🔹
سخنگوی وزارت خارجه در واکنش به ادعاها و اتهامات صدر اعظم آلمان علیه ایران نوشت: صدراعظم آلمان از جنگ ایران، برنامه هسته‌ای نظامی آن و نیابتی‌های ایران سخن می‌گوید.
🔹
این، یک روایت کاملا تحریف‌شده است. این آمریکا و رژیم صهیونیستی بود، نه ایران، که جنگ تجاوزکارانه را آغاز کرد. آلمان حتی از حداقل شجاعت اخلاقی لازم برای محکوم کردن این عمل تجاوز هم برخوردار نبود.
🔹
مردمانی که برلین نیابتی می‌نامد کنشگران مستقلی هستند با آرمان‌ها و محاسبات روشن خودشان. آن‌ها برای حق تعیین سرنوشت، آزادی و کرامت در برابر اشغال و سیطره‌طلبی می‌جنگند.
🔹
ایران هیچ برنامه هسته‌ای نظامی ندارد، ولو این دروغ بزرگ ساخت اسرائیل را بارها تکرار کنید.
🔹
منطقه ما نباید بهای احساس گناه آلمان یا عادتش به تمکین در برابر قلدرها را بپردازد.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/462460" target="_blank">📅 17:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a090c47eb.mp4?token=TC7ZOFfQEIGKT0sQk3z2HzjnS4y95t1pr7XhNgPY5zrUiMznwwH5zNdn-Nc8AG_rlKuc98kl3u9PaHSdxTkaywsH9XB7P9yOd3ufHcNmWzXTy2QsVQsvgdh5KDibE1NIoKXHi3yBbEs5u0q6q8iwSlu6PYWryYLE1kqzs3I67LwcaTEQObxldJF4-1sjm6iXxcjEwcFzF94dFdrOwNv0ijjeNZj5i-qdmwCFCnj8bJCTDUTjYpHkWzWyrGuVjuFpQI6FqPHg5KWaP_dlBRpNak8bD04pl7evLnjqWYTyUduFIjYoMhC7xxSbATq21eL-hJvq4p6qfiVbkeGyMMmTNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a090c47eb.mp4?token=TC7ZOFfQEIGKT0sQk3z2HzjnS4y95t1pr7XhNgPY5zrUiMznwwH5zNdn-Nc8AG_rlKuc98kl3u9PaHSdxTkaywsH9XB7P9yOd3ufHcNmWzXTy2QsVQsvgdh5KDibE1NIoKXHi3yBbEs5u0q6q8iwSlu6PYWryYLE1kqzs3I67LwcaTEQObxldJF4-1sjm6iXxcjEwcFzF94dFdrOwNv0ijjeNZj5i-qdmwCFCnj8bJCTDUTjYpHkWzWyrGuVjuFpQI6FqPHg5KWaP_dlBRpNak8bD04pl7evLnjqWYTyUduFIjYoMhC7xxSbATq21eL-hJvq4p6qfiVbkeGyMMmTNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مالکان ماینرهای غیرمجاز یک سال برق یارانه‌ای ندارند
🔹
مدیرعامل توانیر: با دستور وزیر نیرو از ۴ شهریور امسال، دارندگان دستگاه‌های غیرمجاز استخراج رمزارز تا یک سال از برق یارانه‌ای محروم و تعرفۀ برق آنها تا یک سال با هزینۀ واقعی برق محاسبه می‌شود.
🔹
مردم…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/462459" target="_blank">📅 17:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac83f5d453.mp4?token=hyg93MUdc-Nbzk3aWiNoTkrhAiCx0gBLWE6UUmCjldid4qUoLGBvHdMx3bo8C06dh6yLli9Rk-rT3FjsTAMAiiJLqgdIHCDLfyjZIn6wSUckFnUnrCiUokLUGlXG2Lu4xpwXro5naFw2xHWrS-0rvHVCqAafk7c4j6Vov-CT5fJCVdAQKOVnNY01_DWqDxXk6M8dyfNeahRO8NVg7DG8UB1UbVjJJnvLXSkqcmuv1Kkv4LyBAM88yrj36zrvvJ0mvUWWMvIZy56gFgRBwimaA7edkdE4IkjpPU13NntJ3rNx4FiDX2R4ZsX_iT4cmDnELlieOGtPjlV4O6StjLx_17lz3_zKDbLsg4nyCPMPBolpPehXp8hKjIBE08JzIQ9IpSb5RDuyblhkYstHYJOrvOWjiDQBCUrgi6fIALID8gLCys9v6mzNnqf1XTze8X9UXEDYFwwSelupw5hwFz1KQcEpj25avZ05HKrSUHKcQZCC24XgY_bIKeCMdoYrks7I4zFFLVKkCGSZ0W4f74JuHTPshSe9_6rW4AkP8KZOBb7RmV5eqgUO1U2vUQWbRseaDTnEYM7OTLkqHIhsgy3Xss-pEe_l2YnAX41xr7t3RMZHz3mUolaNiZ5swo7I64fZiqqzGjABzSIK0QWsBHdGYT2jW4ZVL_DIdhFtV4bnH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac83f5d453.mp4?token=hyg93MUdc-Nbzk3aWiNoTkrhAiCx0gBLWE6UUmCjldid4qUoLGBvHdMx3bo8C06dh6yLli9Rk-rT3FjsTAMAiiJLqgdIHCDLfyjZIn6wSUckFnUnrCiUokLUGlXG2Lu4xpwXro5naFw2xHWrS-0rvHVCqAafk7c4j6Vov-CT5fJCVdAQKOVnNY01_DWqDxXk6M8dyfNeahRO8NVg7DG8UB1UbVjJJnvLXSkqcmuv1Kkv4LyBAM88yrj36zrvvJ0mvUWWMvIZy56gFgRBwimaA7edkdE4IkjpPU13NntJ3rNx4FiDX2R4ZsX_iT4cmDnELlieOGtPjlV4O6StjLx_17lz3_zKDbLsg4nyCPMPBolpPehXp8hKjIBE08JzIQ9IpSb5RDuyblhkYstHYJOrvOWjiDQBCUrgi6fIALID8gLCys9v6mzNnqf1XTze8X9UXEDYFwwSelupw5hwFz1KQcEpj25avZ05HKrSUHKcQZCC24XgY_bIKeCMdoYrks7I4zFFLVKkCGSZ0W4f74JuHTPshSe9_6rW4AkP8KZOBb7RmV5eqgUO1U2vUQWbRseaDTnEYM7OTLkqHIhsgy3Xss-pEe_l2YnAX41xr7t3RMZHz3mUolaNiZ5swo7I64fZiqqzGjABzSIK0QWsBHdGYT2jW4ZVL_DIdhFtV4bnH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ قهرمان پارالمپیک از رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/462457" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462454">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hw_PrYnrH9U0tAdHTUpNGwYKnPMYdNWuGlZ5YdA64Uucjtck0d6YphqKlmARgMQB0Egu7ZBIgU1rBkpKKYbjqGeZbtQ4J9VBwn4nnC9m1No4ABBikCPE5c3EZ81632DhUMXJeL30-uLa9qSp3dcmYPZGojUJtf_hBwL7y7bP70Q2wAqnoqF5rFae5FVFQHvgdPitX9W6GuFxDwAAHLNo3LKLdJjBAT1DV1M7QpoW-3pIyf5Is9ly36MZP6ifjCHzuRKmEntBlKLe-L_sdIN2R7zuSlpq-7OsJeMsVpSjHXZhp1oaR4Sd1Keat-P-26tLtNolvjoLsr113wbUvc2m6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YD8N0u6dVtEjVZhCgk_S7qg1TqucC2VwrTem1Nn6dq-nsfwSia8UaNDM67d0x0j6JegKNm7t-LFOQvcFOGKX_kiQjzCvg9tuvWGKpBV6DXHZsAfi3kB_tS3SmFKRD0287xYEI_AmLXz1_l5WYnGE2COXJSuuO5BdfOMbOyVsAr8vlUo9kcZmjLT3t5HlkzogH9Vx10suv5M_UWbou00r__hDUq6FR43ydraXuDw64Ltl_d2rzoIRRGSzrroAW_LguG97_GHhf3lNnCbVIlKdK99s2X3Uo1gq5CzMkjVmKddwMvDZi2QLBd7ATXECFVebAfQ3kA6vuV6xGuGE3qsCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDOd96SGHPCznR33JYaQI2-_rdyiPRGRb8DQA5tIeyCI9OKLhKruSE5Ie8ocAT_Euyveb7zQniSY8QRmkRTFpPPhifPo1Q5HvP0dFmOKd0oW0OvbeloteE5FejK1QN92iPZm8L-b3wtKi-gQuu41MtlmOO-lO5tCQoxuU4F4AzxwHlJJHT4AoWFtGR_z59Wm7BJWJjrGx7wx9HwmIdK9BrOIcHOjfFFnrsDHEfdAGR1zlr4KqbQZNgnx_vx4l0hZe5YlpKevXpNiL577TbYRdZWgIclsIyzBfbkDbTAYv5cgKlKYbybxLP1k3gDqOenmnFYMQuXLznbbUC8tn1W7ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار رئیس اتحادیه میهنی کردستان عراق با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/462454" target="_blank">📅 17:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462449">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQ18vBq--8f8h0jJj2CKp4FzryffQHUu0aG1-h470sJpFf0119JCUwh2hIvp20Nqf6L935KS95VfiDho4gK-6RhFuFWQbs3k1WEcMeHu6QAV9sr_pDDdR-1qndbvoyCnEgb3amVo5M_vesciXC2_ySvTVUrRmwQVJK1Wwz9nvaB-69uaEnGKrzTBNLDCIZLp9qPGqEuSf3p_F82NC2JdIySHjWqWvYpe9m2SvpRitGZMXyF4kUw0qFmQo7l1qJN1iXMpHMBIt5wZukWk_69uwRD1a8tr9BczbKDJWPbHJFdn8LsiYJUFGNXZ_gXUuiShNoCIhHVt2hch7AGm3zvB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOh1k3GCeAUkcHZv395TW81CXP8WYSChSsMflxGBNUNfj1uhUMB1QDUKnILFXi-UYpcBebWpo5_kvgEUF88SrYaOxN99ec92G6tNJCjTogRHgA-OgKTLPS7LthzEV_AveyP6JoZwl8VFV1aD22zJ7qsEaPt6ce4gCMB_E_ukm3g1dBD_NaR5LoQcDv8p1-X_SGcqyL3j9sFLKP_jXOuuIaB9eCuMS3k-bUcISFiNzgT5toLQJD8yjhWOWkg92_ZIwwtwYLO1PYrziZIv0jsCgninkJGJ5XS11jtHH7H_NovNoppltDXVPkcx4cAD12AdxRaYaR9EF_N8cppz19_pAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QC6grhHofRuXM9dHeLGvkFuRCIIDzKKz1GacQZEKQW49uOjv5iasHUA0YlnK4pnjMcWsWjMk1b2hcVPfx5Xf9usFnGID6E1S7yVI2xALw71223akHHhTWHdhK2Ny_f0SVD7H9GmwXZVBgs_VISkTzuqwb-eytEqvA71r3PrK9lYMQlsjHAa4H5elCGaprzGNEr12KOabWN_WB7SCCUA8BfdWe5zfpERB5XJ3hHvpWnWymSsEd0vWLQRQUTP9M3gXAIIzWYEWzpa72R3KvQhhEFbmvfwM-4SRh2b12nk9cLle0wrLfudXOBskC8RO5gERsgZIR8y4qQusv_mV3h7FEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tB6tOLqnIX06pgg7WQlGgOOdBkrWVHIQniJnd_GwQm9wjBei5vTL6Y2IGQDwLFnD84dPhMDeHH_Jo-X_fTMQJF2k6hjNl6cIMRCfmzcm5Pm9yjStVl2derGXIYA0AijKG8gTAg9wN-H4WNP5sYKNCQV8rQWWN9L7n50-J5QHDZCiTVNGITrgONrpQG2f4Ugoe4SyHh2ZTRPjQPmB-nGIAuzOr2sGEYRvKNlTQC7sqi4x1xnMpxUXqSrRXFv7COHPIbcs3Ao79CxASt49CKJpLeDVFIicgc4kMVNKZhNGWVFE65Ydwr9tmhERyGAOb7sgCPJNRegS443byjBU0D-M8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saACTVhYJvCm2WnEmWra2JmF9u1xCbgUhgWCO0-c0HyYyf2twGrnsj39l-TzpagwGqC_z38SjmtQ2QQGKO-a9pFlNe-SrrOwlR8TGkdR-sKMdGOKui_XP0eTt185MiMwnlBMxX1V2QuJ0Gom6Rtp1XqzweR2EccmwsJLpGRblyZvkY3lP8b6olKyoe6ngfUhMOEQ1Kf2iasz3k2cskDAPN2d-o-b6-6IZb4gXHNOx36uCQApFgpkmgr2xSwhGzLqz57YYje-rXkVsLH05Zi23ozohvqQoGE0M0XdCRKtOmtlRfHbpO2e_x6pQ4ZXOtu37ZHAiQysxUwuGSbUuKbaEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایشگاه خودروهایی که نمی‌توان خرید!
🔹
هفتمین نمایشگاه خودروی تهران با حضور ۳۵ شرکت واردکننده و تولیدکننده در شهر آفتاب برگزار شده و بخش عمدهٔ غرفه‌ها به خودروهای وارداتی اختصاص دارد.
🔹
برندهایی مانند لکسوس، تویوتا، مزدا، ولوو و مرسدس در کنار برندهای چینی و خودروهای لوکس حضور دارند، اما جای برخی خودروسازان و مونتاژکاران داخلی خالی است.
🔹
با این حال، قیمت بالای خودروها فضای نمایشگاه را بیشتر به محل تماشای خودروهای لوکس تبدیل کرده است؛ قیمت برخی خودروها از حدود ۵ میلیارد تومان آغاز می‌شود و در مواردی به ۸۵ میلیارد تومان می‌رسد.
🔹
برخی بازدیدکنندگان نیز با وجود داشتن چند میلیارد تومان سرمایه، خودروی وارداتی متناسب با بودجهٔ خود پیدا نکرده‌اند.
🔹
طبق گفته‌ها نمایشگاه امسال با وجود تنوع بالای خودروها، برای بخش قابل‌توجهی از مردم بیشتر یک ویترین خودروهای گران‌قیمت است تا محلی برای خرید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/462449" target="_blank">📅 17:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462448">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سوئد کارمند سفارت ایران را اخراج کرد
🔹
سوئد در حمایت از رژیم صهیونیستی، یکی از کارمندان سفارت ایران در استکهلم را اخراج و سفیر ایران را به وزارت خارجۀ این کشور احضار کرد.
🔹
به‌تازگی وزیر دادگستری سوئد، بدون ارائه شواهدی، ایران را به انجام «رفتارهای خصمانه» و تهدید منافع اسرائیل در خاک این کشور متهم کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/462448" target="_blank">📅 17:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462447">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Venj2OIiSfoX2Rc_GG1ojDXrikL7Ov487srIG3R-CHoMAwEx2VgC-GLCjbXjDTH_opWiPztiyz7Qe13TVlZhkSm2k8xOr39OobSM1ApFM0TXN2hkbEXN7WHOD_ZDMx6KCEE4CTVObypl149AbweKt30jgSnOaxSuxhXpenodkPstxZB2H0yGjgqED1fpZMu4ntiC5uJ63RcSvZSLw-UH13m9NbXWgSDFRuFVt2y0pSmy-wASWwTU5qa7gQ3gi9NXy9mTzNz2Ft9LUUCN2L0Au62nKX9Cy6N0MlYXjtsw7u1-fWKeIqnV5BepJwTj-RIgtVK-05BFPW9opq7uoQ8bzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرشاخ‎‌شدن آمریکا با چین باز هم بر سر ایران
🔹
وزارت دادگستری آمریکا خواستار مصادره ۶۱ میلیون دلار رمزارز تتر در ۲ شرکت چینی شده که مدعی ا‌ست این رمزارزها حاصل از فروش نفت و محصولات پتروشیمی ایران به خریداران چینی بوده است.
🔹
دادستان‌های آمریکایی مدعی هستند که این پول‌ها از طریق شبکه‌ای از کیف پول‌های دیجیتالی مرتبط با شرکت بایننس در ماه‌های می و ژوئن سال گذشته منتقل شده‌اند و بخشی از بیش از ۱.۵ میلیارد دلار شبکه تسویه درآمد نفتی ایران در چین هستند.
🔹
نیمهٔ اردیبهشت ماه بود که وزارت بازرگانی چین با اعلام یک دستور منع حقوقی برای مسدود کردن تحریم‌های آمریکا علیه ۵ شرکت پالایشی چینی که به خرید نفت ایران متهم شده‌ بودند، اجرای تحریم‌های امریکا علیه ایران را ممنوع اعلام کرد.
🔸
حالا امروز هم وزیر خارجهٔ چین اعلام کرده است که پکن آماده است تا «قاطعانه از حقوق و منافع مشروع ایران دفاع کند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/462447" target="_blank">📅 17:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462446">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ed0cc5c4.mp4?token=PU31enobzmyavxJO60t47gk162aaQ0YkXL73AcUFLfPoNl_9PwRUlMss6pJ71mY8AV_3tNehNPskBkMy0udYA46BowngiUIChd_TjWC7fC4EUD2d5Uf94Xx3N11t9ReUT-RCkWPbSomCcMAZ2_zNbbaodngh-_wpQ-axxwtM5eV9xGCT-Nr1_ewY-Z66xay8IxxCYM426pfUN6HhkbuBfL7_gfJG7qrMl3ERCB6yVgTDt6Qhx_dR5w3qcONEu63Uldyuq8UN6XFu0b2LXV4CKjcVQ6EK_IWiWoVClTnorRUiws_gH3GRNzargD9w6obHIA0pZdK6tbtQP4Nx7DFVuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ed0cc5c4.mp4?token=PU31enobzmyavxJO60t47gk162aaQ0YkXL73AcUFLfPoNl_9PwRUlMss6pJ71mY8AV_3tNehNPskBkMy0udYA46BowngiUIChd_TjWC7fC4EUD2d5Uf94Xx3N11t9ReUT-RCkWPbSomCcMAZ2_zNbbaodngh-_wpQ-axxwtM5eV9xGCT-Nr1_ewY-Z66xay8IxxCYM426pfUN6HhkbuBfL7_gfJG7qrMl3ERCB6yVgTDt6Qhx_dR5w3qcONEu63Uldyuq8UN6XFu0b2LXV4CKjcVQ6EK_IWiWoVClTnorRUiws_gH3GRNzargD9w6obHIA0pZdK6tbtQP4Nx7DFVuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: توقف غنی‌سازی هم فشار آمریکا را تمام نمی‌کرد
🔹
دهقانی فیروزآبادی: اصلاً به آمریکایی‌ها نمی‌شود اعتماد کرد؛ آن‌ها قابل اعتماد نیستند و به تعهداتشان هم پایبند نیستند و حد یقفی هم برای آنها وجود ندارد.
🔹
آمریکا در مقاطع مختلف با طرح موضوعاتی مانند حقوق بشر، تروریسم، صلح و خاورمیانه و مسئله هسته‌ای، ایران را در یک گفتمان مشخص «تهدیدانگاری» کرده است.
🔹
من تردیدی ندارم که اگر موضوع هسته‌ای هم نبود یا مسئله هسته‌ای حل می‌شد، در گفتمان دیگری ما را امنیتی می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/462446" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462445">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVkWh90VojEX563F4Az0JLBOjzNZDHUyyFCRT2cSkwFr4RPQFo66Sjy3DrppbnsmiN2sqeZ_1oe_Y2tFAhtHb_rh_Ntjis5VChZaJTsVIsHzmJQYSzlRJ7B8J64_LkpTavLeoQRPPalu3aRHzDYxX1aN3iJ5c0_ihEOmZpKPpfg4-LUoA1zkSYYZaFKjgjmJ0psye8usxAZC9WiXoH3HoyCXJ7lJvmshLAN0uqhGQa0TT_csqgum54O3u7U-oi8jm6lWcmD8a2Enp4qNnHZc__--ChpFuXcYqSaKg_mGMJJOvLL7YvCbD-ceCp5aZdZFI_TtwJgzOxgS4_aBliDtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست فعالان دانشجویی برای تعیین تکلیف پرونده‌های انضباطی دانشجویان هتاک
🔹
نمایندگان بسیج ۶ دانشگاه‌ تهران با حضور در میزگرد فارس، به بیان دیدگاه‌های خود دربارۀ عملکرد وزارت علوم در رسیدگی به پرونده‌های انضباطی اغتشاشات اسفند پارسال پرداختند.
🔹
مسئول بسیج دانشگاه خواجه‌نصیرالدین طوسی: وزیر علوم در مصاحبه‌ای از اتفاقات اسفند به  «جنب‌وجوش دانشجویی» تعبیر کرد؛ این نگاه نمی‌تواند توجیه قانون‌شکنی باشد.
🔹
مسئول سیاسی بسیج دانشگاه امیرکبیر: اتفاقات اسفندماه از شعارهای رادیکال و توهین‌آمیز تا درگیری و خشونت، فراتر از یک تخلف معمول دانشجویی بود و برخورد با عوامل آن باید به سطح بازدارندگی برسد.
🔹
معاون بسیج دانشجویی دانشگاه شریف: از ۲۴۰ پرونده ارجاع‌شده به کمیته انضباطی این دانشگاه، تنها ۴۵ نفر به کمیته دعوت شدند و در نهایت فقط یک مورد به اخراج رسید؛ سه پرونده دیگر نیز همچنان در وزارت علوم تعیین تکلیف نشده‌اند.
🔹
جانشین مسئول بسیج دانشجویی دانشگاه علم‌وصنعت: هیچ‌کس نباید بالاتر از قانون باشد و پرونده‌های دانشجویان هتاک باید مطابق قانون تعیین تکلیف شوند.
🔹
معاون سیاسی بسیج دانشگاه تهران: برخورد با دانشجویان هنجارشکن نباید صرفاً با عذرخواهی متوقف شود؛ اگر اقدامی طبق قانون جرم باشد، باید فرآیند قانونی آن طی شود.
🔹
معاون سیاسی بسیج دانشگاه شهید بهشتی: در حوادث اسفندماه آنچه در دانشگاه‌ها اتفاق افتاد، صرفاً اعتراض دانشجویی نبود و بخش‌هایی از این جریان تحت تأثیر عوامل بیرونی شکل گرفت.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/462445" target="_blank">📅 16:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462444">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92e547cc7.mp4?token=lFSvHSv7ey6vmOJ2TOmGsMWilVjFI-F_hsPyWP7KAoygp9lWW9-Daf6JXhd1G54kyy3hk3ZCHnD1VgES8vIve-veUPKqMgZ2B4Uq3BpWmnu29PCZH9VYF_x8YurSQfFVwOosAV-chVc4i8Hcw-MzPhxnyMEMExYjgoaN4C1zg9u7ReAIgVWZgjkxPLQCTIsJ3bu7N5bRsJwuVcvAQs_wSqdrR0QODioJ6gj2BnJWiBpRwFyLAgyJ9eWrzlnDDEMXxW5yEI0wICaPF5UMGEMoePT-hoEVS8PTMjYajKZZs6UP6itvUWAFqwoPecXckqAaaLlYssr_KhamaIDXm82pFgm5JZ3AugG6KbziZsPy_whaEL3dfUmSJuHEjzdCgpgQHHDkI1iqfvuVI5Te2-NkAQ7RGYJMJhinPebAJ85rIq6R-aWFkW61fK0tdKg0Fy37E_YkAlOJ2qsoNpcxtaDzkkpcgvwtS5kiP3q9j-kmjHEmxycCrVJHx-UtfvSWWzJBk-ACHQaaaxSBVA50zmadhUuadCIAC4DASLIdDvwKcU-wuP5CRJnbqd15CViXSlPez65_G-RXCC_ZG2drkxYs2moxUbcV058vXHEXI9Lu58QCAPj8bystwevZmaz2JFm_q4CVYhbYdTOYm834x34fEYR7hyQGJ-lb2EFPjhKsGaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92e547cc7.mp4?token=lFSvHSv7ey6vmOJ2TOmGsMWilVjFI-F_hsPyWP7KAoygp9lWW9-Daf6JXhd1G54kyy3hk3ZCHnD1VgES8vIve-veUPKqMgZ2B4Uq3BpWmnu29PCZH9VYF_x8YurSQfFVwOosAV-chVc4i8Hcw-MzPhxnyMEMExYjgoaN4C1zg9u7ReAIgVWZgjkxPLQCTIsJ3bu7N5bRsJwuVcvAQs_wSqdrR0QODioJ6gj2BnJWiBpRwFyLAgyJ9eWrzlnDDEMXxW5yEI0wICaPF5UMGEMoePT-hoEVS8PTMjYajKZZs6UP6itvUWAFqwoPecXckqAaaLlYssr_KhamaIDXm82pFgm5JZ3AugG6KbziZsPy_whaEL3dfUmSJuHEjzdCgpgQHHDkI1iqfvuVI5Te2-NkAQ7RGYJMJhinPebAJ85rIq6R-aWFkW61fK0tdKg0Fy37E_YkAlOJ2qsoNpcxtaDzkkpcgvwtS5kiP3q9j-kmjHEmxycCrVJHx-UtfvSWWzJBk-ACHQaaaxSBVA50zmadhUuadCIAC4DASLIdDvwKcU-wuP5CRJnbqd15CViXSlPez65_G-RXCC_ZG2drkxYs2moxUbcV058vXHEXI9Lu58QCAPj8bystwevZmaz2JFm_q4CVYhbYdTOYm834x34fEYR7hyQGJ-lb2EFPjhKsGaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر جدید از اصابت دقیق موشک‌های ایرانی به پایگاه موفق السلطی
🔹
یک حساب کاربری اوسینت  با انتشار تصاویر تازه ماهوارۀ «سنتینل-۲» نوشت که نشانۀ دست‌کم ۴ نقطه اصابت موشک در پایگاه هوایی موفق‌السلطی اردن، پس از حملات موشکی ایران در روز سه‌شنبه، وجود دارد.
🔸
بر…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/462444" target="_blank">📅 16:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462442">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOUlWdQvlfiafCJLmirX9lDl8BKa4Qv7BnXI1qPRkej_lghwQ6KXp8tmecU7q7W-Z5qUeUos595xerA6kyOOLmPncmrvBpst9Rsd819x_jIVsuf6zvcgJjRWxaidFCLjg6X-aJmSzjTgqPcYGIihwUf-aXeltop-0ii8x-V9xSkrTwOL_x5K0ZY3lexuRCB9nbrvx1cjnG86R2mosMPtbzUqFqq1TShpG6fJpVCleHc7OlbnnBzWEUEgLyByGM-CgnU5lzkXRK0qDQ_SNxqq4wS50j4-5PxHS1JYpQkgR9BOb_NHxVOPrgCRlQyeKS3PM_XqRfdCQ8aTcppzl1rLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرانی بنزین یک سال کوپن غذای آمریکایی‌ها را سوزاند
🔹
آمریکایی‌ها از زمان آغاز جنگ با ایران حدود ۱۰۷ میلیارد دلار هزینهٔ اضافی برای بنزین و گازوئیل پرداخت کرده‌اند؛ یعنی به‌طور میانگین روزانه بیش‌از ۵۰۰ میلیون دلار!
🔹
قیمت گازوئیل با رشد ۶۰ درصدی به رکورد ۶.۳۰ دلار در هر گالن رسیده و بنزین نیز با افزایش ۳۹ درصدی از ۴ دلار عبور کرده است.
🔹
بخش عمدهٔ این هزینه به گرانی گازوئیل مربوط است که با افزایش هزینه حمل‌ونقل، قیمت مواد غذایی و سایر کالاها را نیز بالا می‌برد.
🔹
برآوردها نشان می‌دهد این افزایش قیمت به‌طور متوسط حدود ۷۷۰ دلار هزینه اضافی به هر خانوار آمریکایی تحمیل کرده و قدرت خرید و پس‌انداز خانواده‌ها را کاهش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462442" target="_blank">📅 15:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مجمع هلدینگ خلیج‌‌ فارس این‌بار به حد نصاب رسید
🔹
مجمع عمومی عادی سالیانهٔ شرکت صنایع پتروشیمی خلیج فارس امروز با حضور ۷۶ درصدی سهامداران و نمایندگان صاحبان سهام درحال برگزاری است.
🔹
نوبت دوم مجمع فوق‌العادهٔ هلدینگ خلیج فارس با دستور انتخاب اعضای هیئت‌مدیره…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462439" target="_blank">📅 15:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462438">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCNjc9thfuxbUGrR7eMwr_Nv5XMo6txRtqTHAAfltv48seyvr7e10gSFWqjSzQHigUH-ryt2Eec0jBYc1e4HBkuk2jcW5eKJW7q5uYL_YbaERhCFI4gKkO9nzvIuY7aJiSkSi4a_Dl4RXnDXkNFkeWhM2WCRBujS2h-vgleMvuHfoftmcSvbDKaD0k3FHcJZnXPri6IQ_jno87M0vnJU5djrcF26CeiNxUQsaR65ogVyKKYYrZW5XeZeutopMpQxZ9tVMu81P1qvZN_3dSlmBat9jbZsLKqH1-gdrlD4ZjL6C4RNgIe32wpVVCPVsvqi_b2yKFzBVFVQ75xzY760-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: تأسیسات آرامکو در ینبع و پایگاه خمیس‌مشیط را هدف حمله قرار دادیم
🔹
یحیی سریع: در پاسخ به تجاوز وحشیانه به کشور و مردممان شرکت آرامکو در منطقه یَنبُع را با ده‌ها موشک بالستیک و پهپاد هدف قرار دادیم و با لطف خداوند، اصابت‌ها دقیق و مستقیم بود و باعث آتش‌سوزی‌های بزرگ و خسارات گسترده شد.
🔹
همچنین پایگاه هوایی خمیس‌مشیط را با چند موشک بالستیک هدف قرار دادیم و با لطف خداوند، اصابت‌ها دقیق بود.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462438" target="_blank">📅 15:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462437">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0880aaa698.mp4?token=C6kjuvmcL03Op0Ird5hT4ew-TEZzLB_orlJ-EMWXuT9sw-LVN1Yzwc-3DwHqpd2N1mapMtMFMXrR4sQ4CeEFzbuVtgEqObEn-xXQN5k0RTo0hRSAOAAjJDRQmDWikpLzP8uwm1UCcPu0kFHtmZlji1CCsfRzp-KKbmpG7SdwVFtfCvHAnG_8qeIdc3NchHlyq7JQqm5xn0gifpT-Yl1RWQDHbRpZRQGMjHZ0AxX8Iy8cT5VeLVcM27ulh_51NXAo1SSyRnR5bXCLs3QKkXmUJ_lGCt9xtxbC_4u2AbGN_B2RVJQko0jyj198uSS0YKVPK54bAuynidLVgb5StAW8xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0880aaa698.mp4?token=C6kjuvmcL03Op0Ird5hT4ew-TEZzLB_orlJ-EMWXuT9sw-LVN1Yzwc-3DwHqpd2N1mapMtMFMXrR4sQ4CeEFzbuVtgEqObEn-xXQN5k0RTo0hRSAOAAjJDRQmDWikpLzP8uwm1UCcPu0kFHtmZlji1CCsfRzp-KKbmpG7SdwVFtfCvHAnG_8qeIdc3NchHlyq7JQqm5xn0gifpT-Yl1RWQDHbRpZRQGMjHZ0AxX8Iy8cT5VeLVcM27ulh_51NXAo1SSyRnR5bXCLs3QKkXmUJ_lGCt9xtxbC_4u2AbGN_B2RVJQko0jyj198uSS0YKVPK54bAuynidLVgb5StAW8xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسۀ شورای امنیت دربارۀ وضعیت «باب المندب»
🔹
منابع دیپلماتیک می‌گویند شورای امنیت سازمان ملل متحد روز سه‌شنبه جلسه‌ای اضطراری دربارۀ تحولات پیرامون تنگۀ باب‌المندب برگزار می‌کند.
🔸
تسلط ارتش و نیروهای مسلح یمن بر خط ساحلی تنگۀ باب‌المندب و عجز و لابه‌های رژیم…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462437" target="_blank">📅 15:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462436">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34aa499ac9.mp4?token=M1qyUqsmQqisI14YCGEfQIH1S_aUGKeBpcZ2w249H802AhXYy4JDiZlYHmSCvVC3d4dzSonSWhU2dk07W0fiDgPqiISNm02bcEFE1sXEGaYabl5yTnOy5ODRvEDqmJn2apGFhn4_6rVdF-5668nvEH5WAR1VYsjGiWLw0DZnye6DITGKJKVOICYcN3CcAU4Z8XiR28snOqA9krCj1kFWhmhiLyijX878yn9ky-qBcwZ2WD2APRBza4Jo8EwO8lCnN4hcU2l1bQxVqQ01Gwhb0pmTU4Oq32hAj6iN_WHRrcULULgLnjEQZ3ZbmHRq2ZkUbgqEvhhSYsdUtNiadqzSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34aa499ac9.mp4?token=M1qyUqsmQqisI14YCGEfQIH1S_aUGKeBpcZ2w249H802AhXYy4JDiZlYHmSCvVC3d4dzSonSWhU2dk07W0fiDgPqiISNm02bcEFE1sXEGaYabl5yTnOy5ODRvEDqmJn2apGFhn4_6rVdF-5668nvEH5WAR1VYsjGiWLw0DZnye6DITGKJKVOICYcN3CcAU4Z8XiR28snOqA9krCj1kFWhmhiLyijX878yn9ky-qBcwZ2WD2APRBza4Jo8EwO8lCnN4hcU2l1bQxVqQ01Gwhb0pmTU4Oq32hAj6iN_WHRrcULULgLnjEQZ3ZbmHRq2ZkUbgqEvhhSYsdUtNiadqzSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶ میلیون دانش‌آموز یک هفتهٔ دیگر سال تحصیلی را آغاز می‌کنند
🔹
وزیر آموزش‌وپرورش: همه‌چیز برای شروع یک سال تحصیلی خوب و حضوری آماده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462436" target="_blank">📅 14:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462435">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec4abd008.mp4?token=Gbw3HgOFApz0_zawoKfxXLRBG0d6E3H8p25xD0BvKWnSGO17d6Cxx9DeTlox6opTveK8hHXGdhg0W-Mgf4nlqwi8do0Lp1jTuIjCBzP13g9jF8FnYnOZt9Mz5W-cO3MJMJhClfprUEDFp55wO-drJDweOzC6rEDvBz30vdCbPf50YV9lThNGkmUlsqWEQ4zqrBNv46RlftZls1xVEnYZh8eqTMdTotGpmTWgid5p9dnFi1pRIV4yvWNnGqS-Ua24cCH-WiGsMM2-2Wv8ecm5njb58Z6SFI69g0VZvc23Mc8RD_CiqIDzpCA170jJiA7qav11dpVVr0InOrf0Uog-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec4abd008.mp4?token=Gbw3HgOFApz0_zawoKfxXLRBG0d6E3H8p25xD0BvKWnSGO17d6Cxx9DeTlox6opTveK8hHXGdhg0W-Mgf4nlqwi8do0Lp1jTuIjCBzP13g9jF8FnYnOZt9Mz5W-cO3MJMJhClfprUEDFp55wO-drJDweOzC6rEDvBz30vdCbPf50YV9lThNGkmUlsqWEQ4zqrBNv46RlftZls1xVEnYZh8eqTMdTotGpmTWgid5p9dnFi1pRIV4yvWNnGqS-Ua24cCH-WiGsMM2-2Wv8ecm5njb58Z6SFI69g0VZvc23Mc8RD_CiqIDzpCA170jJiA7qav11dpVVr0InOrf0Uog-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتیجهٔ گزارش پنتاگون دربارهٔ جنگ با ایران اعتراف به شکست بود
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462435" target="_blank">📅 14:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462434">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
یک شب مانده به ۲۰۰ شب حماسه‌سازی ملت ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462434" target="_blank">📅 14:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462433">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b8df15dd.mp4?token=Yx-comXsY6t5Sc8Six5HdLOVbxAKks8OEBkD2KVpFvdX26DV07TU0IHjYzce9mRq847b4zRCn2qMBsovmfclddYvJgPbjDyCpon-Il2Uu89bDYYvCnM0dw-FXBKWFHTUbSwhlfAS_webvYIIPnSDZgGLJVWroN8-suY8U2339aV47nCRw1gwXdjLrlesXLbtqO0XKDQXBnW4noa45xDj9pxEunpq1ZK5Pd9V7NGSeXvYwIO2_JZAMPbtkEmG5QxXCkzVaLUTgj8SZvb6c5Kos4lEslRP_ztk6GvFTMZq13ufCFX_2_PK-Gk5uj_A6tDTUNV16Li1zVdqW3UXZQxfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b8df15dd.mp4?token=Yx-comXsY6t5Sc8Six5HdLOVbxAKks8OEBkD2KVpFvdX26DV07TU0IHjYzce9mRq847b4zRCn2qMBsovmfclddYvJgPbjDyCpon-Il2Uu89bDYYvCnM0dw-FXBKWFHTUbSwhlfAS_webvYIIPnSDZgGLJVWroN8-suY8U2339aV47nCRw1gwXdjLrlesXLbtqO0XKDQXBnW4noa45xDj9pxEunpq1ZK5Pd9V7NGSeXvYwIO2_JZAMPbtkEmG5QxXCkzVaLUTgj8SZvb6c5Kos4lEslRP_ztk6GvFTMZq13ufCFX_2_PK-Gk5uj_A6tDTUNV16Li1zVdqW3UXZQxfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۱۰۰ دقیقه ۱۰۰۰ گردان جانفدا تکمیل شد
🔹
با اعلام ستاد مردمی پویش جانفدا در کمتر از ۱۰۰ دقیقه ۱۰۰۰ گردان آموزش نظامی و امدادی جانفدایان ایران تکمیل شد.
🔹
افرادی که در ‌ادامه ثبت نام خواهند کرد در لیست رزرو سازماندهی خواهند شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462433" target="_blank">📅 14:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462432">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9xk-3FqxAMvIKXcJWBmSs4IVkwzsvXWvJeAxJeE7mMcGPtMi-RqkBH4zvmbACQYy9F3T_AZPCI7fNCASa97a5_0sIlWyjiT97v4OQfJTpegQGONp7pY9Z1eJFW3bXGMwzGg4Fmzg9ku_80FGADQ-wuFIJvsUSkp-TnZI9U125ogfNUGV_novBOjgziAbH2S9j_CGeNlLal3W_-kcrhtLaNTAjT7r6Ene012IDi6njXGQ_6FESlBZ6lXbdsK3sA2eGqnc9Yg-KsJxLsS8FXQO73hcVHIT5EZubMA7rn4gNE8F9fmR9aO6qxp_w7c1Rm7lpUfwdFcTbVQcLa2nLuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آغاز ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی
🔹
پذیره‌نویسی نخستین صندوق سرمایه‌گذاری ارزی کشور با هدف جذب بخشی‌از سرمایه‌های ارزی و هدایت آن به بخش تولید از امروز آغاز شد.
🔹
سرمایهٔ اولیه صندوق ۱۰ میلیون دلار است و هر فرد حقیقی یا حقوقی می‌تواند حداقل ۱۰…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462432" target="_blank">📅 14:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462431">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiRhZ5iTUeevxg0JpGwbhgI4EC1-MbAAl-l0e-2vRI4jRsNTyfsRJs1LvLIJRgo9zbw8q1_KZX7036A2MLq0MAgpXCKuDa4-OK_n8uzm9AiRF0elzSAo3hdRnhWTnpfcSQW16bWvINDYcn1tqgx3IZ4tOcQDFD2IxWjqcsLpOLTuVbLYnU2GgXa3LchPjv45JxuT3z7RfYj3M-A6O3HdR-cz80IFXuRZ8GaN8Mi6V5wpHw5HBQtGTP30CuK0QUthCaeK3crb2vG7w13O7g-LKpUgdy4UMyL8MG9phURBkDNpTkmWzgSMkMgBWzWfvfo898WVmr_uO30MTXVLmE3CZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ جزئیات افزایش کالابرگ مشخص شد
🔹
پیگیری خبرنگار فارس از وزارت تعاون نشان می‌دهد رقم افزایش اعتبار کالابرگ درحال بررسی است و این افزایش در بازهٔ ۳۰۰ تا ۵۰۰ هزار تومان خواهد بود.
🔹
وزیر اقتصاد هم امروز اعلام کرد که ۳۰۰ هزار تومان کف افزایش اعتبار کالابرگ خواهد…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/462431" target="_blank">📅 14:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462430">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT_oqm5pGN6iHGWYFcxincq8-Rh0IpL-s3-uHezvV0D3JyeLHvDfTzX5CSFk8hCK1agr_wi52pPPzTpqPnpdiyWZS8nYDaepr94QnwE8zhKw0blaJDbWUwzH31PlKJmbSBGjM3ii40mxdyCXmk6tBy4dEaR8ASeHD88kT5trAmAujs7xcy3Fr-a391_idaomjOlEPbvqxoJMTBqckipxRPukv9xmw6gI6PlYIhzHsSPro6KAYSUrOzoM3PKSGTzg2vrh-JvVUI44cKRRoHjr8hXxcT2pz2gRyxATGf1hfPxEPGDSec40Cm6NHvdh8HUFMnxdZHqB9OQkDCFOXLQy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه‌شنبه‌ها روز بدون خودروی کارکنان دولت
🔹
رئیس سازمان اداری و استخدامی: به همۀ دستگاه‌ها ابلاغ کرده‌ایم که تا حد امکان، روزهای سه‌شنبه را تا پایان سال به‌عنوان «روز بدون خودرو» در نظر بگیرند. @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/462430" target="_blank">📅 14:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462429">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سخنگوی دولت برای چهارمین‌بار: کالابرگ افزایش می‌یابد
🔹
سخنگوی دولت امروز گفت که «در حتمی‌‎بودن افزایش رقم کالابرگ تردید نداریم و حتما این کار اتفاق می‌افتد.»
🔹
روز گذشته رئیس‌جمهور هم گفته بود که «رقم کالابرگ حتما افزایش پیدا می‌کند.» این درحالی است که قرار…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462429" target="_blank">📅 13:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462428">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS4zxt6Xefi8hYsNk0b9Ldm_0qq01YI_0G1V4e253E2T_w70RMu5XTO-BA5Xy7WnWMt-sBvL5BAdp2UgSMqKHO4Qzd8NkQMQVvOq-KHzucGPHOGpk19zz9Fa8dgpaXyuTjwoLMa_xpngmwZ1DNQz9gjqCxOv9etP73ODqzEJJahTbSjtyVnrdpV9ld6YgvAPih8CzNCcdkEZvgnXJQHs4qkMi5rzljnVnkudlhZBmjv7p5iqOMtddVCmaw6FvBV5XLt3ibSOcWsnjLnBcH_q7MNPxjCMHhNRfvjUcH5y1L7e2Z6xho3ZS3zfGHHd8HWxsCcsNn5GHUdFtp1gmJmEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز اولین تولید آزمایشی گازوئیل یورو۶ در ایران
🔹
پتروشیمی نوری برای نخستین‌بار در ایران تولید آزمایشی گازوئیل یورو۶ با گوگرد کمتر از ۱۰ PPM را آغاز کرد؛ ظرفیت متوسط تولید گازوئیل یورو۶ این واحد حدود ۲ میلیون تُن در سال اعلام شده است.
🔹
برای اجرای پروژه از سال ۱۳۹۹ تاکنون حدود ۶۷ میلیون یورو و ۲.۵ هزار میلیارد تومان سرمایه‌گذاری شده و ۷۰ درصد عملیات آن با توان داخلی انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462428" target="_blank">📅 13:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462427">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diAJtMDfRTIagx6ISkZRL-e55pWuvGpZpkJjVWQAFoG3Od8-0Face0PwGB8QBntai6-iVRJcrBihGdxc7P8x9iKqT-bFeEWaDzwoecn-T9whXRF2m474kEmD5qXwLKXJBC52shQn513QUtmIdBTddUy-ketXYNOsgPfy-uZFUbjRJ5m40-Ppb5EiiTH61jZEgpN5PMSioUuJW4CiXXbC-x8fJkvlICCqzGC7BOKMjOzTF8aGiJkOxQVM2oK4sELtOef7UxgWRMTC8dGaJM85p3H2MTZLlrTEbWJ563TpFnO5lnGqeXj_zSK6HDzwH0xYWtHLSFSYOD5nod-TplHMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر حیدری: اگر آمریکا جنگ را ادامه دهد این‌بار نیروهایش در آب‌های منطقه غرق خواهند شد
🔹
جانشین رئیس ستاد کل نیروهای مسلح: قلۀ توانمندی آمریکا، نیروی دریایی و ناوهای جنگی این کشور است؛ اما چند شب پیش موشک‌های ایران ناوهای سنگین و ناوچه‌های آمریکایی را هدف قرار دادند و آسیب‌های جدی به آن‌ها وارد کردند.
🔹
آمریکایی‌ها در این منطقه دو سرنوشت محتوم دارند. اگر جنگ را ادامه دهند، قطعاً انبوهی از نیرو‌های آن‌ها، همان‌طور که تا امروز به درک واصل شده‌اند، در عرشۀ همان ناوها به کشورشان بازخواهند گشت و انبوه دیگری از آن‌ها در قعر آب‌های منطقه فرو خواهند رفت.
🔹
امام شهید ما فرمودند که اگر ناو سلاح خطرناکی است، خطرناک‌تر از آن، سلاحی است که ناو را به قعر آب بفرستد و ان‌شاءالله این اتفاق خواهد افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462427" target="_blank">📅 13:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462426">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی از هفتهٔ آینده
🔹
رئیس‌ بانک مرکزی: ثبت‌نام نخستین صندوق سرمایه‌گذاری ارزی با هدف جذب منابع ارزی، تأمین مالی پروژه‌های ارزآور و توسعهٔ ابزارهای مالی ارزی از هفتهٔ آینده آغاز خواهد شد.
🔹
براساس این طرح، دارندگان ارز می‌توانند…</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/462426" target="_blank">📅 13:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462425">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0d_nXiyebxQlIGBX7KRdsFZj6XCWiEy9vUMbQCLq2Gs3lmLcW-7gGtYiXBhhM2WIl0x8KorhZoe_nOAkuPb9PSmSkCkhoO4bDo45rZVhUahsywWeXfegTvtetygbIVQrn9FZDZ7hqC-9foT3H_f4ffHSJJw12-5tvhlk6nGDv4qZLrRkKzFWa5vKBGuftNVT4CExn73-8CCYvL-CkwHsOqs5w9__JFA_pl4ktmDVtM851MOmPg6d5MIaet0tl78LI36l71oLkZBGvsDNymoSwlNl5YlYtm9yqqakX17tNtWp_FcaTh_3YI2OkoM2l3qXQppSzPj-iC0vYeIR7PSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایگان‌ماندن مترو و بی‌آرتی تهران ۲ ماه دیگر تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/462425" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462424">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqBt3vsU_uElTKM8DdShCFtuYibLFOV_IcOyqVQ7-JYcVxgMOwQjHtb3nfXISZStim2CtshzReiZGB9XmyXpzxgOk-nurmbpA3K_jwltwtu_bGK3oqSctS81f6ihYYiO2KpORxYd4003jQYBJ3VNa67n5rDpw7T4FjAmEWpx8XeorT84MOOXPAJyE8CTmWVM1ihFZ4_ra7oTvsd6Jpe3nMonBat_hOUZpfuCDN480PBHhtKaAeBI7w6h1a3afK06D5eX1wLyq78YYfX92MMOYfz1mxla6EopKZdy2Uuab7pwyfJAzDHa9UeOEQt2ROG5aHSayLrjtPo4HY0lrZnZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی شهرداری تهران: ۳۱ اتوبوس دوکابین در دل محاصرهٔ ادعایی آمریکا وارد ایران شد
🔹
محمدخانی: این اتوبوس‌ها دیروز وارد ایران شده و تلاش می‌کنیم با انجام سریع فرایندهای گمرکی، در نخستین هفتهٔ مهر وارد چرخهٔ خدمت‌رسانی در تهران شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/462424" target="_blank">📅 13:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462423">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAYE4g7_grIT9wM6KJ-Sxgl25bQY6KxO48aNDjB_K_ipdiMKUDVrjQNJsSFurQD2cio-xAUU6293qD483S19D9GMV1EMZhJhmhcL_XfRDvBo-a4wInSvbKNVfY9OLorntDtfw4g_DsKe8hxLGARYH68hoq2plpKoTKnyv-6NU_92zoqbt8QJNRlBs5-jGcZBlUUeRPlQs8PDDoUZK_QkEih2lLbF_YpT58j5-hMy5nJAx1FfGhWjX8HBOdVUIU7icYb9xEp9HO70zOmvgP7-jqvBG4h1p89ao3rG6N3cOaTycP9ZCgBIh8UgvwmT-vtxssRWryOh6cUrR6gEedc-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی مصرف CNG پس‌از تغییر نرخ سوم بنزین
🔹
عظیمی‌فر، معاون وزیر نفت: یک هفته پس‌از تغییر نرخ سوم بنزین به ۱۰ هزار تومان میانگین مصرف CNG در کشور نسبت به نیمهٔ نخست شهریور و مرداد، تقریبا ۲ میلیون مترمکعب در روز معادل ۱۱ درصد افزایش یافته است.
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/462423" target="_blank">📅 13:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tliKV4XL-RQvtAb3_1i8I095pHy-E2fDbPYLz8WVBRy1D7QG0oxNpzyDSkRfJn2bAU_UPYNtnXfexD2Teii1_1v2mshtM60EhLGRXhbMdjo6cfyX0JOAyXBMaSITiReYVZG-CKMHq3kNsAMXpYFNyTr4fw7qsNYZDWhICSQPgxJiESZhvNaE3FuW83yoahuZI9zZ-h5dYh86D_D_CC4CaiyBqjDEauFTT_P2MrkgwvsUZPFreFGk2DoXJGy50yyfi87gia-SbOKvZsGq_IeW9Bxa8e8M_Y4dqLVUi9Nh_SS55p7STrpivmou88ykl-BU090ev3EBEQP_LjR1ezIz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: آماده‌ایم قاطعانه از حقوق ایران دفاع کنیم
🔹
وزیر امور خارجه چین وانگ‌یی امروز در دیدار با عباس عراقچی، همتای ایرانی خود در پکن، با تأکید بر شراکت راهبردی پکن و تهران اعلام کرد که چین آماده است ضمن تقویت گفت‌وگو و همکاری با ایران، از حقوق و منافع مشروع جمهوری اسلامی ایران دفاع کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/462422" target="_blank">📅 13:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQoDhpl1lV3Xh7r9x5hRQeZ2JgWDdF8CydJrSSFihEAOnm-AzYV6uWfpD-_4bbatMIfO3TXk0al9GcPUFMBJobi57ZwjDdXNrc7iuIM_zAMmYByGRbNQOr1Vh1OTndeUjtouyMa2Gj1mdHeDuw46MxG1Fp8lAQwZLFwgj-rS-dnUYua0NXpeASrwm3AQVwSAw2wmt-8IALpgEfz456igUEzgPX2y7j8BhL3YiOK1G3nJTRZzTKTO6eWFpa2YuNW8ZdYnrhnuo4DuCsVUvIyvIXD8SoGoHXIsKCqMfcv-c3_2vNXCe7t4VOA6MhGH5mhuC0jeFImWXY9JCI7ay4ayeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: آمریکا به مونتاژ تصاویر و روایت‌سازی هالیوودی عادت دارد
🔹
سردار محبی در واکنش به روایت رسانه‌های آمریکایی دربارهٔ نجات یکی از خلبانان این کشور در ایران گفت: آمریکا عادت دارد روایت‌های هالیوودی ارائه کند. از ابتدای جنگ تاکنون نیز رئیس‌جمهور آمریکا بارها در خیال خود و در فضای مجازی پیروز شده و ایران را شکست داده است.
🔹
آمریکایی‌ها برای جبران شکست‌های خود، بخش‌هایی از فیلم‌های مربوط به مناطق و حوادث دیگر را کنار یکدیگر قرار می‌دهند تا چنین صحنه‌هایی را خلق کنند.
🔹
هم‌زمان با انتشار این روایت، تصاویری نیز در برخی رسانه‌ها منتشر شد که نشان می‌داد قطعات جنگندهٔ F-15 هدف‌قرارگرفته در همان ایام، در داخل فرغون جمع‌آوری و حمل می‌شد.
🔹
آمریکا باید بداند که این‌گونه روایت‌سازی‌ها دیگر کهنه شده و نمی‌تواند واقعیت‌های میدان را تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/462421" target="_blank">📅 12:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امحای مهمات عمل‌نکرده در خارگو
🔹
بخشدار جزیرهٔ خارگ: درپی انهدام مهمات عمل‌نکرده از ساعت ۱۵ تا ۱۸ امروز در جزیرهٔ خارگو، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/462420" target="_blank">📅 12:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462419">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGAprHb_xA1UMB-0nJ7DEMwUy48Pjsale6j0PcX3ltbX3MfDmst9HtJyGx0shiFe0c_oXGn1-3akpmuNNFAmu5WdvdE_xQDzyCnfwWdHif05RwvpOWckkbAiAZuMfwcTYdvCSyd20_6DPyil8d2erCzZjHCmZ706yWr90pZ6rRQp2znhMYpa7X1dZmTSbwVmE9rIc3fCS6-ykj5AefmmsVJGvNWg0jkYWXJnY8gI4TgiM8FoWuluEov42ykun6TKztHfazAqvc8oP_ofwqMymhs6fCfcbWcb4r3P3xlISY_uL1eCfj8xHjt49fAw_rxLjh3j8p1_ynfQPPRm8nOqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۳۶ هزار واحدی به ۷ میلیون و ۵۵۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/462419" target="_blank">📅 12:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462418">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx69Z9fbhIXB3Eu3CvelOV4KwUvMMYN0OdbQjZT1qE3w_LTuOWu6tsG0orL02Ystqw8Y4Q3Tnih7dfVostJmGoH8S3pejMuZys8VjCyY-npBwxrwco1BEbpraWbK9TaDAeU2wIePQZ5Jic7z19g42A3M21Bdm8iBKMG-sDjKJaaVgFpvRC2zhFULgmdzW_cSGSJhs5Js7xR4ePK0VYmq3pbBLaqKt61vT_FpCZYWOmPVuo9UGNsBVXXmw3y35ICgXMDDEQ4x7wKIHYpecEe7-2xpSnxhbsA8m_ieVExzn3is9c3Q0WqdcuqEOjgndiAe1yLHzNIet8-UaGXY9F0eYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریکس؛ فرصت ایران برای فعال‌سازی دیپلماسی معدنی
🔹
اختصاص یک بند مستقل به «مواد معدنی حیاتی» در بیانیه پایانی اجلاس سران بریکس در دهلی‌نو، در کنار تحولات مشابه در اجلاس گروه۷، از افزایش اهمیت راهبردی این منابع در اقتصاد سیاسی جهان حکایت دارد.
🔹
در این میان، ایران می‌تواند با تکیه بر ظرفیت‌های معدنی و زیرساختی خود، پیشنهاد شکل‌گیری چارچوب همکاری بریکس در حوزه مواد معدنی حیاتی (BRICS-CMCF) را مطرح و همکاری میان اعضا را از سطح گفت‌وگو به پروژه‌های واقعی و مشترک هدایت کند.
🔹
با توجه به ریاست چین بر بریکس در سال ۲۰۲۷ و تأکید این کشور بر تقویت همکاری در حوزه منابع معدنی راهبردی، فرصت مناسبی برای تبدیل بند ۶۷ بیانیه ۲۰۲۶ به یک دستورکار عملیاتی فراهم شده است.
📌
دیپلماسی معدنی می‌تواند یکی از مسیرهای جدید ایران برای نقش‌آفرینی فعال‌تر در بریکس باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/462418" target="_blank">📅 12:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462417">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎬
پیشکسوتان سینما‌ از اهمیت حضور بیمه دی در کنار خود می گویند
🎥
گزارش ویدئویی از   دورهمی اهالی سینما در هفته بزرگداشت سینما با حمایت بیمه دی
#رونمایی
از آمفی تئاتر و کتابخانه خانه سینما</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462417" target="_blank">📅 12:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462416">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/462416" target="_blank">📅 12:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462415">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محدودیت‌های ترافیکی آخر تابستان در جاده‌های شمال
🔹
تردد موتورسیکلت‌ها از ظهر امروز تا صبح شنبه در جاده‌های چالوس، هراز و سوادکوه ممنوع است.
🔹
در جادهٔ چالوس، محدودیت مسیر تهران و البرز به‌سمت شمال از ساعت ۱۴ جمعه آغاز و از ساعت ۱۵ مسیر پل زنگوله تا تونل البرز بسته می‌شود؛ مسیر مرزن‌آباد به تهران نیز از ساعت ۱۶ یک‌طرفه خواهد شد.
🔹
تردد کامیون و کامیونت در جادهٔ هراز نیز در ساعات ۱۲ تا ۲۴ امروز و ۸ تا ۲۴ پنجشنبه و جمعه ممنوع است و در صورت افزایش ترافیک، این جاده در روزهای جمعه و شنبه به‌صورت مقطعی یک‌طرفه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462415" target="_blank">📅 12:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462414">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2c10ff6f.mp4?token=XUYJtJtYx3Y0_aYs4lFi6uQ5AJ8fT0hmbnF4iatBxQ9J2xv4LsVySfXpoyraJam3rMHSvaa_3cSGIJMMYgUWZCyKS-YhOkoh8trLFOIvvT-Zn86QrDnU6BL9lc5A0vNTlmWXuqMMwxdpYi5TM3oz-WhUwSKxWbTF_j_8TNot2Pz7LhgQYr7oPRDsxaEyh-k4MxxBqDKLROVEUXokzM7Z9V-j6FZbHyExWUvob1eZgm9WTeR_fPsavj-bcagB1UdaXOvdUZ2RZcL2Cau57njhyoUbSYBSmGP2184duMAr1H39anHaCdXPpND7Iiq0Zs_9RsT3PG30pyvGeosvfpYmEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2c10ff6f.mp4?token=XUYJtJtYx3Y0_aYs4lFi6uQ5AJ8fT0hmbnF4iatBxQ9J2xv4LsVySfXpoyraJam3rMHSvaa_3cSGIJMMYgUWZCyKS-YhOkoh8trLFOIvvT-Zn86QrDnU6BL9lc5A0vNTlmWXuqMMwxdpYi5TM3oz-WhUwSKxWbTF_j_8TNot2Pz7LhgQYr7oPRDsxaEyh-k4MxxBqDKLROVEUXokzM7Z9V-j6FZbHyExWUvob1eZgm9WTeR_fPsavj-bcagB1UdaXOvdUZ2RZcL2Cau57njhyoUbSYBSmGP2184duMAr1H39anHaCdXPpND7Iiq0Zs_9RsT3PG30pyvGeosvfpYmEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسارات جنگی آمریکا «رسمی» شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/462414" target="_blank">📅 11:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462413">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">استانداری اصفهان: انفجار کنترل‌شده تا ساعت ۱۳ امروز در جنوب استان انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/462413" target="_blank">📅 11:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7-tHDgkzbbOR5K6BdnNNgV2Bz43LjaTl5k2l5R9XBdT59bLMS9g0PbWWLRzrJgtTVSuWzzW5lsa9vll8wC9xFD2pKPi6oNRnGWuPg2iClnVE4q9gJsnrit52db2by5stTJQKN8kQffsKTQle7AgymCdVrL8TMCyU7gX0Xj5u_ytAw1gtzFyftASN0RcdycLK1I2Mguw0cLiZEgzoVbdpKQp5qFDcdTKIDHggs5ZllA1Xq_e_avbYw4fKOWuPbSo1SWeSXYLU7aea1d4JXloRDn7SqdCw7UpIWjnOAacMcsWZHGIPH9pBhyZlHAW7ITfeHHDzAQ7TFo_LwioxY_enA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ثبت نام بدون کنکور در دانشکده رسانه فارس
رشته سینما و تدوین، ترکیبی از هنر و تکنولوژی است که به شما این امکان را می‌دهد تا داستان‌ها را از ایده تا پرده نهایی خلق کنید.
در این رشته با اصول فیلم‌سازی، فیلم‌برداری، تدوین، صداگذاری و جلوه‌های بصری آشنا می‌شوید و مهارت‌های لازم برای تولید آثار خلاقانه و تاثیرگذار را کسب می‌کنید.
✨
مهارت‌هایی که می‌آموزید:
🔹
فیلمنامه‌نویسی و داستان‌پردازی
🔹
فیلم‌برداری و نورپردازی
🔹
تدوین تصویر و صدا
🔹
جلوه‌های بصری و گرافیک سینمایی
🔹
کارگردانی و تولید محتوا
💼
فرصت‌های شغلی آینده شما:
🔸
تدوینگر فیلم و برنامه‌های تلویزیونی
🔸
کارگردان و دستیار کارگردان
🔸
فیلم‌بردار و مدیر تصویربرداری
🔸
طراح جلوه‌های بصری و موشن گرافیست
🔸
تهیه‌کننده و مدیر تولید
📞
همین امروز قدم اول را بردارید!
⚠️
مهلت ثبت نام تا 26 شهریور ماه می باشد
☎️
تماس: ۰۲۱۴۲۰۸۲۹۴۱ | ۰۲۱۴۲۰۸۲۹۴۲
📱
ارسال
عدد ۱۴
را به شماره
۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/462412" target="_blank">📅 11:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce0e6f6d6.mp4?token=AHn6-PjgOvhL7v9975-T8yAxdWcui-14HsczNO7ChnkuUWokeSzmZwBnLlCn6KmhamvwjWOKCNhTcIHgntWDzdbqHjWOMxz4epqEHxOSy3TmKAozsxI6pfvKnirrRIBQ_aWKZ_wkvUlwkPi-xMW6Gkl1QB85i4WHstcaJ-eRm7DvB9f8rNID34oPlqzayu4in7q1rVJQVkFrGvZr03BOb2XteXSyqv9d6S76NH1bKzTrH3NITkE7Bu2qdsdO-wIY9GXUcx3XciHV4540j4eouxviMeiPQUxl8L5JAZXaPXRkZpk_zPnLO7kXJ1kazZ1EwztqPghmVbOnWAgEpld4NZC4hE45p3ye8EOMPcTtkQwR20iKjQ3DSRdavkM1QiNcYMpf_srFaUKaFyE8AR7fgitgpkke7rlaErn2uEHaud2paQ42BN1y-v74JB6Fmzj9KClSG0Z0qPRlqBKLDHEl0Zz0zFvbyZfNF1pTg6cr5uTLV7eCkBHqxZem-TiDsUWTNiYjor92xKYLic3hwUWXRQOST5Y-PqVGGWagO3f9iN0oL2pzE589LZhQgQcxxE8r3QPZqZB6eaM2mT5OPS7TGY4_a_aOtPmXus8ETNwL5OQHZuvhCrPaWuFQID3cyN1p_Fu_7qdxMMSYBP8giGdXOd5HJX-Dm4TFQ6J6xSd75tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce0e6f6d6.mp4?token=AHn6-PjgOvhL7v9975-T8yAxdWcui-14HsczNO7ChnkuUWokeSzmZwBnLlCn6KmhamvwjWOKCNhTcIHgntWDzdbqHjWOMxz4epqEHxOSy3TmKAozsxI6pfvKnirrRIBQ_aWKZ_wkvUlwkPi-xMW6Gkl1QB85i4WHstcaJ-eRm7DvB9f8rNID34oPlqzayu4in7q1rVJQVkFrGvZr03BOb2XteXSyqv9d6S76NH1bKzTrH3NITkE7Bu2qdsdO-wIY9GXUcx3XciHV4540j4eouxviMeiPQUxl8L5JAZXaPXRkZpk_zPnLO7kXJ1kazZ1EwztqPghmVbOnWAgEpld4NZC4hE45p3ye8EOMPcTtkQwR20iKjQ3DSRdavkM1QiNcYMpf_srFaUKaFyE8AR7fgitgpkke7rlaErn2uEHaud2paQ42BN1y-v74JB6Fmzj9KClSG0Z0qPRlqBKLDHEl0Zz0zFvbyZfNF1pTg6cr5uTLV7eCkBHqxZem-TiDsUWTNiYjor92xKYLic3hwUWXRQOST5Y-PqVGGWagO3f9iN0oL2pzE589LZhQgQcxxE8r3QPZqZB6eaM2mT5OPS7TGY4_a_aOtPmXus8ETNwL5OQHZuvhCrPaWuFQID3cyN1p_Fu_7qdxMMSYBP8giGdXOd5HJX-Dm4TFQ6J6xSd75tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد «تو جنایتکار جنگی هستی» بر سر وزیر ترامپ در کنگره
🔹
جلسهٔ استماع بسنت، وزیر خزانه‌داری آمریکا در کمیتهٔ خدمات مالی مجلس نمایندگان این کشور با اعتراض‌های پیاپی فعالان ضدجنگ به تحریم‌های غیرانسانی علیه ایران همراه شد.
🔹
طبق گزارش تصویری شبکه ان‌بی‌سی، یکی از معترضان خطاب به بسنت گفت: «تحریم‌های علیه ایران که غیرنظامیان ایرانی را به‌کام مرگ می‌کشاند را متوقف کنید.»
🔹
معترض دیگری گفت: «اسکات بسنت! تو یک جنایتکار جنگی هستی. تحریم‌های علیه ایران را متوقف کنید. شرم بر همهٔ شما که اینجا نشسته‌اید و اجازه می‌دهید مردم به‌خاطر یک جنگ ناعادلانه و غیرقانونی بمیرند.»
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/462411" target="_blank">📅 11:35 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
