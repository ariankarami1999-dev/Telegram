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
<img src="https://cdn4.telesco.pe/file/sqOqi7ycA3_O3W-g8bqXcDBYV9WhtsCc1LC6OAq0Vr4yyK573neshimRoCHvJP8Uu9P4-O5eppSRZhsGk2WTKIaDthYC5edQ4pyZ9OTsXwhuDZZ6JLv4b65i6lEguXeydHxeBYR1TRGLV2Jm-fJwNcsQ7rc9SRkWdQQSPRGi7Xjsm0kI0horbtk8LYgYRAsITBdzUV_4ffVuV0w9eqeAy9hPG1O69ZrxxJ6WNiEkSSsJitvn9_Pvq2p9wFkZO2p7oMxfrAGuy6lJcDI5_yDQ7FowLLYLrTaVgo0bxa80LiCzCCSxmh4OcHYmAvcA1CDuZHBFXutaDJ7VvY7vB-vVJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-460070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyYenCqZguxfYMd095j5LDWwTAgFiqP13wSELLNEiM2snMrat-pR418V9SY211ZQ-j2TnB_CSssQSok0c7LtOhOnmLubz0T8G3pRX_fJEJtIFHlxGbTYf4-fD4xzcekwTIHjiL9GyNBfkYQ4O1P5VccCdQDzU5ZoRMMEKE-tcNAQK1Cv1gLUylHbEglYIDtLRG0H4etLjX5ufKjo6IPjhgGXHRjzk_UdnIYk2pniihIzBhLSLvpNUyRfTfJP2AcagQQddMGTwHYwmOK15mLGhf5j8-PgLOj72fNZTHr_4Xq16Dq4xS6CtLgRAjlvM2RMLi8_c_iB-bki4bXK5TFz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: برای هر نوع تقابل آماده‌ایم
🔹
فرمانده قرارگاه مشترک پدافند هوایی خاتم‌الانبیا(ص): ایران با آنچه در جنگ‌های اخیر از خود به‌نمایش گذاشت، تعریف جدیدی از قدرت ملی به‌دنیا عرضه کرد.
🔹
نیروهای پدافند هوایی ارتش و سپاه در جنگ اخیر سامانهٔ پدافند هوایی تولید کردند، آن را توسعه دادند، در میدان مستقر کردند، از آن بهره‌برداری کردند و هواپیماهای دشمن متخاصم را نابود کردند.
🔹
پدافند هوایی کشور با تکیه بر توان داخلی، دانشمندان جوان، شرکت‌های دانش‌بنیان، دانشگاه‌ها و تجربیات میدانی نیروهای مسلح، در تأمین تجهیزات و سامانه‌های مورد نیاز خود به خودکفایی کامل رسیده و جنگ را اداره می‌کند.
🔹
خود را برای هر نوع تقابل در امروز و آینده آماده کرده‌ایم و آماده خواهیم کرد؛ زیرا می‌دانیم تهدید تمام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/460070" target="_blank">📅 12:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPDdjE--GSs6eccXKRF-bi9U38YVmZXHd05_5rVIC0pydH0eXG2MNClOuvzqyzIki87UVNPFqimR5ihWWsUyhrzyXjZxoupZaiS5fhPGJ8zbCKBPPG8afJ5EaKJp6Jea3adlVQ45taJeI-B-VTNK600YClo2d9H-58a4U8PNt4LIIiiuvJUvn0CI-EAfGG4gS_OOH81xL8GFXCQP4l1Xc7dkTnc9E82IzehKYP1MSPjucaG8AeHax1YhkUYlk4893DpXBKdDCmUoKug-AefklZUpj9ZQ_g2A93OHsWd2tj0aXAOWR7Wn79FiUdrfaMAAG-CNK4NJ2Sl59ZeEeUZ38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فرهنگی سازمان بسیج: ۲۹ هزار گروه مردمی، پای‌کار میدان‌اند‌
🔹
سردار مقواساز: استقبال مردم از «میدان‌یار» بیش از پیش‌بینی اولیه بوده و مردم با خلاقیت خود به گسترش آن کمک کرده‌اند.
🔹
تاکنون نزدیک به ۲۹ هزار گروه در این طرح ثبت‌نام کرده‌اند و پیش‌بینی می‌شود این رقم به ۱۰۰ هزار گروه برسد.
🔹
هدف اصلی این طرح آموزش و آمادگی عمومی مردم است؛ میدان‌یار صرفا مسابقه نیست، بلکه یک حرکت عمومی برای آموزش مردم و افزایش نقش‌آفرینی آنها در میدان‌های پیش‌روست.
🔹
این طرح در ۴ محور آموزش‌های نظامی، امدادی و خودامدادی و دگرامدادی، فرهنگی و هنری و رسانه و روایتگری اجرا می‌شود.
🔹
حضور بانوان، خانواده‌ها، نوجوانان و اقشار مختلف در این طرح چشمگیر بوده؛ قرار است گروه‌های تشکیل‌شده پس‌از پایان مسابقات نیز در محله‌ها و محیط‌های اجتماعی به فعالیت خود ادامه دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/460069" target="_blank">📅 12:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7xsdmUAA0hVjSX0NmNekjWy9Nec03icJOXZaLQHdxui1APBIHeNLuIayL3MP2EdsjqHIHIpst9z7obxRg011fg9uMySjvwlbs18GWohz6s4FTS3_LsUpm8e7JWeJBnRs2FogI-wRrmURGbbK2ZARK2_jM6qdXT1Q-G6SVUI9PyPN3KKQQqG-zey_NEqzwl94rqaQ5-2kacBCwpGfvAeTJLbkpU-0mTeukC0aXfB5ODQQiICJQqr9EyifRGLA0Zabih7qqlnJKTkkT78E512HELfadQMYWYAneA8UKLDQgUaqn808moqIgFmb_mV5jh3kvPNbwOsyovjEHIflljvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای حملهٔ آمریکا به مراسم عروسی در سیریک به ۵ نفر رسید
🔹
رئیس دانشگاه علوم پزشکی هرمزگان: آسیه مولایی‌نژاد، ۲۲ ساله، بعدازظهر امروز بر اثر شدت جراحات وارده به شهادت رسید و به این ترتیب شمار شهدای این حمله به ۵ نفر افزایش یافت.
🔹
در حملهٔ ۲ شب پیش آمریکا…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/farsna/460068" target="_blank">📅 12:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JprWMmjZoxYAC6y2NnjabVHSh53IDz33GbRCmKm1e0C2oVbinzZuXkUVj3pVPDcCcYEaX4Qyt73N8HNh-78ykLb2OGlaJohSScX2kwN2bBWv1uQ4jaVAv7RY5xHOy-NCSjH64QU03QXbd4IfbLHE-fxmMxxdOTVkLFI4PVESPFHqbrImHv--0oLRGljt-Iruwl4e-l9TsJDOB9psE0nT0Bv23oknPF5iP-Dyo44zVQ3XaXsMdgPJPcuDMV0goA-foquSP2iFqXOhIqHfHlQT9Uc1ordjOnSDkjViBPLDc0xPDbHihx0XpUlLA_O664qYCQg2BGMqkyfqf8ncUdB9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرمای بی‌سابقه در فرانسه جان ۷ هزار نفر را گرفت
🔹
وزیر بهداشت فرانسه: تا پایان ژوئیه، حدود ۷ هزار مرگ اضافی در جریان موج‌های گرمای شدید که تابستان امسال این کشور را فراگرفت، ثبت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/460067" target="_blank">📅 11:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXBnp1IquPJ5mgWnprkODE6YBWr0mJfbzHe9cHSpi3VN44OqVtBKANhqveKyPm2CU8xBw6dSV3XhD2HwTffL9WdnJhXqiNJS_U3mWVRZ6Mb3X_wS5FfdoRVHxLUv2GMyyH3fVJdSRqVTYSZSFkPLk_bP5vEo7S3YUyd2PrkECzD8VtHIJ97oAHpsAAed0s20dSMjapk1JyoE_Z7KAvan8YCYuk7cyegngMxpZ5GR3Alyn1Kykb1_ulFB7xM785QBWQc-_XM-Bm6hjF7GQIaaZRyWZ9Ri5Oj6ZAZqj84josWcR7fXBzoKApilJY7Ivv-Kg14gg6jGLgrqdgXUhHEQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی پاسخ وزیر خارجهٔ اردن را داد
🔹
وزیر خارجهٔ اردن گفته: «ایران ۲ ساعت پس از آغاز جنگ، اردن و دیگر کشورهای منطقه را هدف قرار داد و این یعنی حملهٔ ایران پاسخ دفاعی نبوده است.»
🔹
عراقچی در پاسخ به او نوشت: به نظر وزیر خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔸
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته‌شدن ایرانیان بی‌گناه انجامید؟
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/460066" target="_blank">📅 11:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmKsbLB8AgeddfVN2XkWvBztzHbuCtboM5fP-F561fB4NRtFkg0a5uLMNiat3MLP75EDJRpBians--JnFj9ixq-GoAMpzrFbQkWkwBMlEX5z11Vw-7WWbdtHDU2ClXewLoItrybpy6B_KJ5Y2trQS99dO-C6N9CjC-M0c1XAijcOGYaQbwWXk-VUWv968XxPkttC5HSWmHVmjFY2JCB2kAsvIcVVY2PIo5x_3vkAJ3mAEQCdO2QG_ynNR2Em4r97_WGl4BFADN55CImSpkVUQGcJuOFerGzVFNPneZp9jjtj8TuZPRtzwUwaT0XD31KIAhpBGyoiVwxGCP-cUXEUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ عبری: نتانیاهو و ترامپ زمین سوخته برجای می‌گذارند
🔹
معاریو: نخست‌وزیر رژیم اشغالگر و رئیس جمهور آمریکا زمین‌سوخته‌ای پشت سرشان در اراضی اشغالی و آمریکا برجای می‌گذارند.
🔹
به‌دلیل نحوهٔ رهبری ترامپ و نتانیاهو، اسرائیل و آمریکا دچار نزاع بر سر هویت و فرسایش نهادها شده‌اند.
🔹
رامپ و نتانیاهو در یک دستورکار شخصی، قومیتی و اجتماعی اشتراک دارند که به‌هیچ‌وجه دموکراتیک نیست.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/460065" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460058">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJydh2IOJrZJqhyjCCZXuhRdmgGrvQR-jXxAaPnJhwpX94_IVNqScg3Kx4dfRtsDYb-Bz0cZ1S46ApmvvEFcph5qEEAiUVqsZ_Y-kYOLAKcffe5W1zZf7HMgpK4T_5fuTNOHuOTLmtqjSfSKRtP7A8kK2EQNHp5V4WBYq9Nn8N0bhMwUh_xXyCeobN4ocMpwazWlpBDy5WxzSGIL0x9XxnAE4gS9bauY6wibjzg_B62n1MpZ7S_13FsKI20h88FwxDD4N5hnT4jJXFeLjIHGWHiPZOic3rYMZqQYaKMhdth89_0r-1BG9FUXmzALTQhSRjMIpBNX_WgGAR13mGr37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ye-pJ5-2klJBhdU3vSvkuPYiRaoONgsRqOuS5wyc3cy-mBNJzbKFLIq1TwKcyAoUqH7xToU1e8aPUMPBZT2fBy4RsvaPbSZsgmMYRKygTbAaUnpw0mUc3fOzCe4k2X3fbhrSXA_B7UNnDLwQtN_KIYT8p7_BwWNDP7EmKnDdWEp-1JLAwsZZgR7xj8EV6w7lqVZMWT5KbDo9D-zTZCLj3LM9p9DjLnlJygLVIV4h7iPrgexdr0iaiy_9QgAoa9np2odWazg9ayla5uUowwaA1hxZpAL8gd92v-RBxU8dKblJffCKm0Am-jhfd4yVGiytOymZtewuSp1FyUUy16GOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A70Qv5XjPz0rifnTJmBIYYGwwojFUB9ZuwIoDic6b2PCB_M5XhNtyta2ryk0cfm7peoQTTtp2vIhizpA6319Wv5kEUY7G2t14EBtA3XZxrsfBv7CJfiYwNCXMw16KxTjUci_IM5aAM_yxu4hBllHus4O2Ni8RSP9VVcTjcBXbfB6uzxkkztsMdeWPkD3_xnIPKWH02xYHWK3oxlkEV_pXfuzvTyyX75O0yUifh1g69-nvZ6Ae83sDKcy0SFuGeNd1xA_vfqCw0ixK_aNpU0nlrak8egzRGKNlR0VknOtd_3zf8jqxCCV0fL3WMftEoMFzH4azhIdPcT4wVeCJs8UhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQC5hJPJD9Wx_aIUzCIFJo0TrGTwQAMeK2rNiJM8mQOL4e-tragWoTxmdTnUazTTC7hTMpJ81C0MufDjo0Wu0OtrFuZu4P-UWLnpstuO3Fbq6O0tCwUVi3WnvosUy7dWCFm2m_e0eD6Z1WXY2Irswjsjnmt0z6mLJ6cwWqHcmAr77yrrOp-SvGgUwye8kRC42-MaRhULZBBPYb_wKfNUNaZKyGckXe_n-lJcw0GasYkFTVEjLfFYPhqRggHwboW737P56I9uV6k9zzCrrKFfOYOZANDdPGSI6U7y3uHx2FkrrfvQ0Hv_BZzDSNqUtZeJM-llU__doc1H6m5xjCOaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuuxsWgCOPaLG1iLND4__k6-VTh3D-BfBdWtIv7Wk-atIrthCA9_WncsQLtOWp6b7dwtRjHG2RdwVNrxJGJqs93jR1DJLwv0lofHkuunUsrRk-3IL-eos4nXO_tVJ4mRmDArrXnLxe-ICLL56a-GZpN39VHRC6yTCFwUloUgmbw7OnFJEBLXZHPl8Y6ngYTbnzgluxYdhzPGFroOcVZagv6YP0-Rinx5-8DTc1FRKpFzM9IeIBKc0MFnxJmboGR41ZbIxfgOFK74eQkeKdDrUoAsdbnV5C14pGoVuUZN-23tDLaIxLSzrEKmFrwTiyN9MhRuNX1vY3qcgqUs3TV2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N15MKBp0oPbHwFKW6qtiX9sMhwIC2jDdtBHSRbH3XDy-xH30J1ok3hKD-2sRklmK_XBiJAEmEe79A5h7XwhaMYz2XEwQ4iThoL03QNpxHiIdwsiLkOanlRFZBNsIaVUJ0b7KdFMZU5YVxUth2INrkesXQlc6lUZnnA-yjEGbJBINqatlDvzDjJbhBNnF9oDqt-6zsnS1C9f4BZmF1s4i_0nRQRRCCX2ccBhK0pOznLQgFD7fpGdrCdicTJZl2kLUatoAdvkILx80XhewQUPGRpXpAe8j_hTLv338eoMg00tdzt3yWm3SJnxzrpBuNGoBceJ5N1CbXyHa3GMN-iHzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJCpk4sALVdTG3ZlrUYVfQdgG7Wt_B4mqguvukntoc9ICB7yf0SPupBWhCE5zdve8oablvp6hTFK8-J9kY5_K5VDCXA_gNuDL2IAAspwnbqYV1-imwPwhcirW1nHRh63vOkhPoXxdAP6htQOx3iVIg6PTMv9UJ7j2f3yLEAMp4RgBrHXxhL3eCI7so8sDiXPkMLjOpv8YHa9dAWtkKOl2NSQA0txutn3NvDgVeCMnpgc78wyvodaH3-TF0YD06rIjdxgUaXJH2T6p9n7puQBMgg8JMN2daICNgCuZux3JBmfAuzMHgVKdYQVo-ErEJNqB6Zi87Y3nl8L1caXJVyl6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم سیریک با شهدای عروسی کوهستک وداع کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/460058" target="_blank">📅 10:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRIxl4BKuXDqPptmWvb5b8VSEffvvrbgX3qBZGozUYz91rjsjd7NN1Vfyhcqt0e4ZBmSTxN31-aOGBgEQQNmzoMFO19ozRmw0YHp4FW0FJ4Wf_4JgyKwxU13RxnGJqIZ273P8SG2dNfVQ4fCHQH3GOxmX-fpCqQje3QOQEN7xK88j6oNT3iLmoi91QXB-29ObTCufxtXaPPpzoWAT6I4z9szzrDj_KgANuncfri04vbCanuxVzY7rvjV6huJgXoiexy77-2_4vZpJPLFqcEGYgOF0e3cjPdppWdctV1kiXmRYDtNDt8oTIpa9u_DEGQBA4Xp53TvcmM3ZMoGqenfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه شوم بن‌گویر برای آواره‌کردن ۲ میلیون فلسطینی
🔹
ایتامار بن گویر، طرحی را برای آواره‌کردن ۱.۸۶ میلیون فلسطینی از غزه طی هفت سال رونمایی کرده است؛ طرحی که بن‌گویر آن را «مهاجرت داوطلبانه» می‌نامد، اما هدف آن آواره‌ کردن بخش عمده جمعیت فلسطینی نوار غزه است.
🔹
وبگاه «کریدل» (The Cradle)، بر اساس این طرح که «جدایی ۷/۱۰» نام گرفته، قرار است در سال نخست حدود ۲۵۰ هزار فلسطینی غزه را ترک کنند و شمار آوارگان طی سه سال به حدود ۱.۱۱ میلیون نفر و طی هفت سال به ۱.۸۶ میلیون نفر برسد.
🔹
بن‌گویر اعلام کرده است این طرح یکی از مطالبات اصلی حزب «قدرت یهود» در مذاکرات برای پیوستن به دولت آینده رژیم صهیونیستی خواهد بود و این حزب اجرای آن را به‌عنوان یکی از شروط خود برای ورود به ائتلاف حاکم مطرح خواهد کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/460057" target="_blank">📅 10:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn-7nDhFSsQxQCsuIBCfKUuv5BvlqN5TfxysNU57QivdWQ5OyC1F7nawbc2tfp26HFkvsTVz22sEoJ16F1hSIzbLvGuZljZh7KZdA7IYj7RsWvOmY4PRCWKgv0GO0JJ7wIf0VyJK4IT1e7j-dbHASB5SXbdtO244fvJduWbNzafAmib_rtUiT2CzAnDv0LInSDDGjkxaKmr6PhflUaeGsX4nzovpa7XAVHfXo-TRmTMg4PN9J7oUhgXzxCEeXCqDlAAjtoc84idLfX65gduJs3cdhW6wgfTZR6z-DPAMQ8DW-T7TIPpQ7CGXPYfSTIhPdEUj_PceOjdVgEoNP8Kbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: ارادهٔ ایران برای گسترش روابط با چین قطعی است
🔹
‌اژه‌ای در دیدار با رئیس دیوان عالی چین: جهان درحال گذار به نظم نوین جهانی است و چین نقش مؤثری در این فرآیند ایفا می‌کند.
🔹
ظرفیت‌های علمی و فناورانهٔ چین در کنار توانمندی‌های بومی ایران، می‌تواند…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/460056" target="_blank">📅 10:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6u-oxiXBkzRJ1JmOjwXGDvku6ZYQwKJmudUG0D9BosnWFFxbvV25V1JtnJxZdxyFt_lroCA4IESYMWx4eAJWUrQuBiHJXSmbMlFT14G-bcAAOc091nY19HJnl24Q4CKPOi8nJUbLxFgiO5-eIt2sUP3GAWYk2veaeQQXQMFZ9sVevDe0z4ZxxRko2k7v8yGdthrt0xDLWjEUpd19vjPSjfrbOJ6ubetZQEQkPKKcnm99nrRkvTYPt4tXUjjucj8w8MN8Pl7TYD0jTR8Rh5Thro67fuG8FVxLfBo8ulvUcCXn_85lsNGaw5EM5CwLPna8tjMVI4GNEb_MsKrMjXbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: ارادهٔ ایران برای گسترش روابط با چین قطعی است
🔹
‌اژه‌ای در دیدار با رئیس دیوان عالی چین: جهان درحال گذار به نظم نوین جهانی است و چین نقش مؤثری در این فرآیند ایفا می‌کند.
🔹
ظرفیت‌های علمی و فناورانهٔ چین در کنار توانمندی‌های بومی ایران، می‌تواند زمینه‌ساز جهشی نوین در همکاری‌های دوجانبه و تقویت اقتدار مشترک باشد.
🔹
همچنین ایجاد و گسترش بسترهای ارتباطی در حوزه‌های قضایی می‌تواند به‌عنوان یک بازوی پشتیبان، تقویت‌کنندهٔ روابط در سایر عرصه‌های راهبردی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/460055" target="_blank">📅 09:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دستگیری ۴ پیمانکار و ۲ کارمند شهرداری پرند
🔹
۴ پیمانکاران و ۲ نفر کارمند شهرداری پرند به‌دلیل تخلفات مالی و اداری بازداشت شدند؛ به گفتهٔ یک منبع این دستگیری‌ها بخشی از یک زنجیرهٔ تخلفات مالی در شهرداری پرند است و تحقیقات برای شناسایی سایر عوامل در جریان است.
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/460054" target="_blank">📅 09:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee9832f4f5.mp4?token=u9mZgmJJX-RYPuI9vQKGYXFpvFvOC4mPVX4VyEzjDB8ZXIon_C5g_xZSzNZ06UBNC9NJ50w_ygpf_acQlE-b15VRg1z3TTyuI1H3ZpvdnBznEr-6voQVmVtRzSd-_-m765APqVYkMJ-A79R0H8kTuyW6X222YxEE8upqfZtB6tNiZnOt2F7kRkeiTzpK-siefUZACosNlyENgFZS8YPGOzmb8gwrjlFpfG97_Rtrq4bEUU4uGrrxgJKE6J8NgYqySI18hyeeBgJcWZc6nPiwSwFNAOdu_gI4dOrXZm8MojQ07ccCfzgL87BkT0B0O5QNJzmDmhUJKpIAdbgMrWtDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee9832f4f5.mp4?token=u9mZgmJJX-RYPuI9vQKGYXFpvFvOC4mPVX4VyEzjDB8ZXIon_C5g_xZSzNZ06UBNC9NJ50w_ygpf_acQlE-b15VRg1z3TTyuI1H3ZpvdnBznEr-6voQVmVtRzSd-_-m765APqVYkMJ-A79R0H8kTuyW6X222YxEE8upqfZtB6tNiZnOt2F7kRkeiTzpK-siefUZACosNlyENgFZS8YPGOzmb8gwrjlFpfG97_Rtrq4bEUU4uGrrxgJKE6J8NgYqySI18hyeeBgJcWZc6nPiwSwFNAOdu_gI4dOrXZm8MojQ07ccCfzgL87BkT0B0O5QNJzmDmhUJKpIAdbgMrWtDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: امروز تمام اقدامات ضدبشری علیه ایران انجام شده و دشمنان به آن افتخار می‌کنند.
🔹
اگر روزی که تروریست‌های آدمکش بیش‌از ۷۰ هزار زن و کودک را در غزه به خاک و خون کشیدند، در مقابل آن می‌ایستادند امروز آن‌ها تجاوز و حملهٔ غیرقانونی علیه کشور دیگری…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/460053" target="_blank">📅 09:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI2t_u3trXaVbuFpVt_zuRUsvrpE6Cd7qvGyN4uXVOrJAt7NG41eMdsnrN9gZFUQmy4yWZXPI0H-fprAebQLn5nOEydOXzLiY_YQo9h3mx6EADVKSclzDytmYZRqiW3fj3rXDxEXueZfrFG3KVNGNyTcFiohRPGevetWDl9hXtcyeJGlnjXj55A3C-tnTXfvKe4WcWU1saocDokvrzjrNL8Hp3LwrqmTIga-XO4xDjSgAvpofstpW9ZMbRU5W4bckorL2NSce3Qok97i5elcreSw7tXI3wl90P7Ph56VBzJUMncAG4KnY-Way58x1wo8Ct3NuwJV3rA9cb8l7VmxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/460052" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea54ba0c3.mp4?token=MGQbzL8rIK8qyC__BI8VZy5RNSt5lixx1xHYNHIQ0Uv7buHWt8kYohfFqlIdqNjL5q5bIfd1IYYxXkBOTGbISYjQW7Y7fyHA8DeB9yo-UPtZ8vK7sJbbOj-waT8R9oPTLDReVtOVt8zptRfjomd8ezmvuaCWLB_Olk7ygmwO9T-1UlTLrUt6G-tRe3O6CJFJYj_sqVA1osp6C2u5GGI2Esz8p_Z5hXHpENYYd0Td5iT4LZCeBJFeqbI9LUhtxUGFxyrtqfgJ6wDzeJ4SP4tYggcqLh4t9sZd-hoSdQDMPQJCrJsqVbJ2HHxBKmYZtirO9eeu_yS15iY-WUgwGIG2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea54ba0c3.mp4?token=MGQbzL8rIK8qyC__BI8VZy5RNSt5lixx1xHYNHIQ0Uv7buHWt8kYohfFqlIdqNjL5q5bIfd1IYYxXkBOTGbISYjQW7Y7fyHA8DeB9yo-UPtZ8vK7sJbbOj-waT8R9oPTLDReVtOVt8zptRfjomd8ezmvuaCWLB_Olk7ygmwO9T-1UlTLrUt6G-tRe3O6CJFJYj_sqVA1osp6C2u5GGI2Esz8p_Z5hXHpENYYd0Td5iT4LZCeBJFeqbI9LUhtxUGFxyrtqfgJ6wDzeJ4SP4tYggcqLh4t9sZd-hoSdQDMPQJCrJsqVbJ2HHxBKmYZtirO9eeu_yS15iY-WUgwGIG2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: ایران به‌هیچ‌وجه زیر بار ظلم و زور نرفته و نخواهد رفت  @Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/460051" target="_blank">📅 09:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_lOHiz2hsi74qYiLahiEbe4ogRFYxhqvp6Sz3H5jy_LyTelP3NdAEdk76EMG2KXaAvihqZyq_5nNFcJBEBl0fIYsbS4m2_am0wn8YuNajw1mFovPUCLfeBuhFySkIS4JGq-5Th7jdo0-beCoSR109oAffXQsOxBpy7c5n5gkp33pd3t2Ta6AbZLE5TmctE7aUPxs7pRNBf3sqtK_5NLH46jiv0QTjRMXxWc9oyFt-lqYax6e7iA2CX8Pg556GJB5M_65lPp54oMoVM4JC43oSPyR7INT3sqnEXRXT-Q1ktke-Ax0KTVe6dynA7iqfpAB_l1Cd4XkfzLgBNMC9SSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت تولید برق کشور از ۱۰۲ هزار مگاوات عبور کرد
🔹
معاون برق وزارت نیرو: درحال‌حاضر ظرفیت تولید برق کشور از ۱۰۲ هزار مگاوات عبور کرده و اجرای طرح «۱۴ مگاپروژه ۳» با هدف توسعهٔ نیروگاه‌های تولید برق آغاز شده است،
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/460050" target="_blank">📅 09:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4a32b4e7.mp4?token=sDMw55ffKoxYzBiHlmfB6pUxg4TrUdzgcAx6v4j36Oosp-OHX9CnZm4atcYHHjeU0YztHhSsRjbj9xhV32jWnq7aXrRDFDYos3r2tkMAxQBa4wzqSF3iFT9g3zBK5Xf9xoMqhD6nJ8mx8uUQjE9Gfi_CQyryPBo9b_-9cU9Z6FU9zQdEGWgq3xPc8cFnuphgbXkDtYnnd38TEVPGnuh3OmIPvv_m0UUiA5Az7xB2JMqFl_gOIC7BhyIi9xqhLqOYQtnNX-CFKfdSV8NDkaJ6ffrayBZ2z-bO3qM7XQ9OR1L5xFT8bBCWpQow5osamoseJ5CxQYeZBI6-pIYamM20Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4a32b4e7.mp4?token=sDMw55ffKoxYzBiHlmfB6pUxg4TrUdzgcAx6v4j36Oosp-OHX9CnZm4atcYHHjeU0YztHhSsRjbj9xhV32jWnq7aXrRDFDYos3r2tkMAxQBa4wzqSF3iFT9g3zBK5Xf9xoMqhD6nJ8mx8uUQjE9Gfi_CQyryPBo9b_-9cU9Z6FU9zQdEGWgq3xPc8cFnuphgbXkDtYnnd38TEVPGnuh3OmIPvv_m0UUiA5Az7xB2JMqFl_gOIC7BhyIi9xqhLqOYQtnNX-CFKfdSV8NDkaJ6ffrayBZ2z-bO3qM7XQ9OR1L5xFT8bBCWpQow5osamoseJ5CxQYeZBI6-pIYamM20Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ایران برای استقلال خود شهدای بزرگی تقدیم کرده است
🔹
رئیس‌ قوه‌قضائیه در دیدار با علمای اسلامی و بزرگان ادیان کشور هند: ما از خون شهدا، زحمت و تلاش خود نتیجه گرفته‌ایم و سرافراز و سربلندیم.
🔹
امروز ایران تنها کشوری است که به مستکبرترین عالم یعنی آمریکا…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/460049" target="_blank">📅 09:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e1abe06.mp4?token=PxZJkbvRZTYf8RYvThzRiB-y2enu9ibipu3q9ViZtZwZOefnfh_pZdvoAc-Rk1mDcIqRWkCaGZ5Q_Z2dpc5VFrjKUe6A-SDcdIeX5j0Rgl2Y7ebnGEqVFDvfVZVEVAFUWFvDgQ1r8EqAsu6Ilkouy1Gc4oRiBTSvUhoL9SDP7Y3qWAaV0dmdxWK-GsfFgLQC4446_mE6pL5yvNlJ4FvZd1F7t0YZqYiAZNnKNXex755rUtNsMBpbDL2HTkAVckWpQ2s9e4bjddV_kkqjQiJ5PUBFe2NhtB811VUhNIVnIR3S0nUB91f_4GI2uftDJfcVeUA6sLNMGwHNJqAHxV0Hfa-D3Efz0jk2BQx3rMMNl4IZFHziNf0L1jwrR08lMAzhzWAd_LiP7hOYx6C46XZz7gJyhceqPwwFkeDu1M897PBdgfMi-EB5jJrZ_SYMdN9ZDD06oflLe_pLCreJcvrFTZXKJXf_KzhT9qMSSWH9SxVf8gq0bLpFyRWBYZt_ND7xcwX8HR_n62M27ogVz53NE1BE68yZ_ngSH4sn3C2uQ2dzLcnrZ8KE8qTPUUqC_peTkQweoFHWEExGjUPysxjwIJGVOTbOM5rTt5lzEGbpKvZmwatksxHyBlRTnFoiki-E0_AwvZZml2BIgwFoIrLYDj_QaO_UkvY7Lk81gBkSobI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e1abe06.mp4?token=PxZJkbvRZTYf8RYvThzRiB-y2enu9ibipu3q9ViZtZwZOefnfh_pZdvoAc-Rk1mDcIqRWkCaGZ5Q_Z2dpc5VFrjKUe6A-SDcdIeX5j0Rgl2Y7ebnGEqVFDvfVZVEVAFUWFvDgQ1r8EqAsu6Ilkouy1Gc4oRiBTSvUhoL9SDP7Y3qWAaV0dmdxWK-GsfFgLQC4446_mE6pL5yvNlJ4FvZd1F7t0YZqYiAZNnKNXex755rUtNsMBpbDL2HTkAVckWpQ2s9e4bjddV_kkqjQiJ5PUBFe2NhtB811VUhNIVnIR3S0nUB91f_4GI2uftDJfcVeUA6sLNMGwHNJqAHxV0Hfa-D3Efz0jk2BQx3rMMNl4IZFHziNf0L1jwrR08lMAzhzWAd_LiP7hOYx6C46XZz7gJyhceqPwwFkeDu1M897PBdgfMi-EB5jJrZ_SYMdN9ZDD06oflLe_pLCreJcvrFTZXKJXf_KzhT9qMSSWH9SxVf8gq0bLpFyRWBYZt_ND7xcwX8HR_n62M27ogVz53NE1BE68yZ_ngSH4sn3C2uQ2dzLcnrZ8KE8qTPUUqC_peTkQweoFHWEExGjUPysxjwIJGVOTbOM5rTt5lzEGbpKvZmwatksxHyBlRTnFoiki-E0_AwvZZml2BIgwFoIrLYDj_QaO_UkvY7Lk81gBkSobI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ایران برای استقلال خود شهدای بزرگی تقدیم کرده است
🔹
رئیس‌ قوه‌قضائیه در دیدار با علمای اسلامی و بزرگان ادیان کشور هند: ما از خون شهدا، زحمت و تلاش خود نتیجه گرفته‌ایم و سرافراز و سربلندیم.
🔹
امروز ایران تنها کشوری است که به مستکبرترین عالم یعنی آمریکا نه گفته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/460048" target="_blank">📅 09:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460047">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
هواشناسی: سامانهٔ بارشی جدید از یکشنبه وارد کشور می‌شود
🔹
با ورود این سامانه در روزهای یکشنبه و دوشنبه در اکثر مناطق شمالی کشور شاهد بارش خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/460047" target="_blank">📅 09:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460046">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6761000c20.mp4?token=X24CrN3oSiJda6uurrS5ZJkGTHe_UBT59sU_7rpUn0hMMTkdwlP15S-BHlS_d4d4Q3zO7B_u0yCfz7_JfcQOUN5Xd7oZO5tM5GT5Iv8zmaS8PXhD2Hd8Q9OKeHngyNM7sEwHzc-wGeKxzKRMmNxMdSqcs-zCZkyyQ--6eKfC0fExaOwDPWrkzepxVhYYyr5tcd7JdohWQWRgptfktlTTWIo4WD5qJFi7td5uEtHD1UJ6Bq-coOWIXxfLc_vNzDH6au2Qj8XiLyEbBLi2fUozCNqcG0gGpHeW68JVszY3PRpQ9lq3sn4a1km5LZ6OuF9nhrAd451uHP29tGkT7qv0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6761000c20.mp4?token=X24CrN3oSiJda6uurrS5ZJkGTHe_UBT59sU_7rpUn0hMMTkdwlP15S-BHlS_d4d4Q3zO7B_u0yCfz7_JfcQOUN5Xd7oZO5tM5GT5Iv8zmaS8PXhD2Hd8Q9OKeHngyNM7sEwHzc-wGeKxzKRMmNxMdSqcs-zCZkyyQ--6eKfC0fExaOwDPWrkzepxVhYYyr5tcd7JdohWQWRgptfktlTTWIo4WD5qJFi7td5uEtHD1UJ6Bq-coOWIXxfLc_vNzDH6au2Qj8XiLyEbBLi2fUozCNqcG0gGpHeW68JVszY3PRpQ9lq3sn4a1km5LZ6OuF9nhrAd451uHP29tGkT7qv0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوچ وحشی بر فراز کوه‌های بافق خودنمایی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/460046" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460045">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhF9u6jf0-8kWRjcemAtmtvDCo5IdBSDHNLm64l4pUUXtM5hlZIVl1uL_wYjrU5a90qEmXUWbdJh0eEBNMXWRTKKNsi46IQPLwxBwySdMDC9ch4aACCexdiYlu83pbUxKCG_Rpwjr6ddtdlsX2EWEaY9NPLd7HUiFJqDzgEEKAxErQlFEXcefk3PIoSxmFrbouzcmyUJ9yVPWMc4qpz4-tcUEUf-7zIUn-XTGvhqrSuH0yCZtrUkxl8-51IFxJVVfjjupPhEV38NWUf7Acp4dQIEUekoxgZ8xt-Z2QMcz3r1cfjNQuLPyqUg_EjJVW6VK_39g7nGsbTgSdPcN2Su6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی شاگردان پیاتزا در اولین گام قهرمانی آسیا
🔹
تیم ملی والیبال کشورمان در اولین بازی خود در مسابقات قهرمانی مردان آسیا  ۲۰۲۶ در ۳ ست متوالی با امتیازهای ۲۵ بر ۱۵، ۲۵ بر ۱۲ و ۲۵ بر ۲۲ مقابل نیوزیلند به پیروزی رسید و در صدر جدول گروه دوم این رقابت‌ها قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/460045" target="_blank">📅 08:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rysv5UArE1VDqNDfZVtqFpMpSvd44A0OQyvJjanxwhyt7LZENO3vl3DL_fy96stnVQHzETSY1wKBgd7L42Lo_zBM5ZZdpHk30kEOkMhMW9n8_FuEVJpjpu2o96JeuMKBLgSE71g77TTt4JwU0nW-c62yQ-bos4fakcJgSRQNYmb9R3a-7E-_ztIHm_FNmjHmxtabTFurfchylecV51bQfDwGWNk6NNyC4QiR9MgahjOONe8V_F-OtLBDaB1KizsDXtnHq8oIB-sFG7bNufNXBfRBab07RBnswTVeuGheo6lN2O6Q9gWm5-kxh9xaAa3JjBc49cwIwB0uNHEsW74zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBSRn9hlIpSaL0FUEkSMju9YHcu-rmrr53e6Tv_jJ3eKKzxZyp4b5cBJDiwK2BhcWwBxWy2dxZKluUFQry-nF_QuBxWWO-ntXAukYYiWTnqqROeBCcEIUIjLsPcPxk0i80YsBXYXTlRaJyQ4YpK-To_2ZPtUzY5ovLAb_EsLI-9GLwEOkx2CV8-n4gGoLwCGgb5fJxiF8-UH5_HckYYtRHniyYbeqb78xBoi8XIeQ4r9dyk7Lsb6vsRKzcxCKGUgsmwnQ0T39lNa8_rs6Ud958ryfYdV1fTW9Af2RF_rwX6mdugvSBB7VvIdIGf6OyA50FT0bB1ZfK6Vsbz3ByFs0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvIRkaxcv8xb6N2xa1ZR7Km4PmHKS0GFdHPcxAmsdgE1WaQqm4yebFGMfqc0k1QlN1a73a-ggjSAJqmwGA-AaX7ukXyXYQnzji5s7Ag3qdY9-sZO6ConXfQpybYG_lTiiac9ip7Fhyd-pc7Ivzr0PizYsgwVGRU5Ve0-zHRHxitqh8IsEp8YiGaazQmK8D12sJSf9BbgZwam2CvUO2tbHTEPlAkgTUIOOSBYDWInOuXKw4uugiQ2MJ_nCGmamxDpzet6T2MsjUmrJ7kWHg8LsMiSDUJMb2PSoKymdQ7wKkv8NBTLuI18HFRV4N3KcPevb1kqdfuMy8XtdDTEjCkSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvWrrKCvPwEYwF_6hDbdxwDpt0nt3krlnrc_rqa7Spgwy91YqJU9kFUpdk-RFzI1tLFKPxholHwK1S-NO33cPUCkda8Yk3HslmCfr1LoI_fWE6Idx7w8SlvBMdIoHVgAHRFrN2PfrhX8Dm7X010Myr3gwBIOM7Pd8sAqJMG-TlFayVreI8zOnQhHPoPVOq2hr5DyRC4SGXT9zHZV3aV9WZgLzjXmEKLk_o1CkS8lQxaZZydMb2razgcYGgeGy8ukJgCyOhIjNtcX-g4ZTKYm3gsE3oRffEDps3LsBaxDymQgdrGWyRBCJE3Lepdgf0UaKung3dC_SAd1SYAMk8_Rmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzFDKuOnvPogfBs_BEr7hh16ghVUx2zjp5VL4kgn2-Wa6HIqSAD0ln4am9fvHktYRm6WGwZOvVwsIu8ZCbHLUEGJ-eS6GaVXy-KDo1J1pJAu1MVqTZNiOmvttJ2ahnpE7v8pvBD_dbc-Do0MskvhJjzhYyPvdqwYo7_DTBwVEWUyCMXtQQoBRzxn5Xqb1GxsLmfsMRQzyR26bzoeXC0_0ZEDMQ6N5GFqc7G7p4s9W7jjT2KMcvGbZxGQZpXqGL9mzjhG13k6TU2hTgQV8bK3Q16afcnkpE5CF-U6gPSMTbNSw05KJBVPmWwxkcVp6wpZ9hJ-RAdy3DwtC5MhbvUJ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین تجلیل از خانواده‌های شهدای جنگ رمضان شهرستان لامـِرد
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/460040" target="_blank">📅 08:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460039">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZsFIYd0SHSWXnlvQA3ovjZrq2thMv7_3x9OaVO0XYiPCkDRqedAk3E9uAFNrNtUPUiiWNRVvvI4rGt2vMGMst8M1fC5YgfbF6RUui6TZpjDnqgKKeVkmFbSBykXqQaJ36N-IsnGxF1wTyDrMtmHg7UG1JKj4arbHvXD8v1xK29TSRPRJl4EWiF-KXq-JeNmQIBbWNt3PhlKdSPzp3C8IknpAS6xAazTNuaN6du1Fww0lEbeh5S98QleVD1guuYhh-8akf1GIns7UaecuUEYpfuBe-eHsBbLmmvG8e_qQtsUowIHrAOh8f7_ebkaW9IV2V_1fYELOjZ08ObQf9lMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: ترامپ توافقی شامل برنامۀ هسته‌ای و تنگه هرمز می‌خواهد
🔹
یک نشریۀ انگلیسی گزارش داد که میانجی‌گران در تلاشند تا چارچوبی برای مذاکرات بین تهران و واشنگتن درمورد یک توافق جدید احتمالی ایجاد کنند.
🔹
همچنین این نشریه از تصمیم ترامپ، رئیس‌جمهور آمریکا برای گنجاندن تنگۀ هرمز در هرگونه توافقی با جمهوری اسلامی ایران خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460039" target="_blank">📅 08:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460038">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ocu0jFWiP9-LK1JE-AFxVLF3nzeLaO00hF6SlX95vGIxsruA_Qpxpwk8Y-e2UVaBssq2FLd4pcCJdBAhV9r_tj3o5xeGsZDllX9ktjxUnm6kRGxPDmkLSsqiM_6ziy4v7rV4ld84yXKB61FuL3x4esKzsTvRvCG9x2r2zGNjXeWkDAcMaMXYoDKvMqoD7zV1zFK3O97IZBPTC3OCz-qw3wDp5rbObsVlmykQHJ1c8ElM_NpO1034RTkTTwjSS02M6dUlHt_Wm9px0YN74lum0O1kGX9bLfww3ZPb03z_OeIWDD9KcX5BF2tKdi6kyBAcu_0P1lG-HcGjPyQyRZ2f0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدارس از مهر حضوری هستند
🔹
وزیر آموزش‌وپرورش: تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460038" target="_blank">📅 06:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460037">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اعتماد به هوش مصنوعی کار دست کوهنوردان داد
🔹
اعتماد گروهی از کوهنوردان کالیفرنیایی به اطلاعات نادرست هوش مصنوعی جمنای دربارۀ زمان و تجهیزات لازم برای صعود به کوه، منجر به خطری جدی و عملیات امدادونجات چندساعته شد.
🔹
کوهنوردان با اتکا به هوش مصنوعی که زمان صعود را تنها ۸ ساعت تخمین زده بود، آب و غذای بسیار کمی برداشته و از همراه داشتن لباس گرم و تجهیزات مخصوص شب خودداری کرده بودند.
🔹
اما این مسیر در واقعیت ۱۶ ساعت طول کشید و پس از تاریک شدن هوا در مسیر بازگشت، کوهنوردان از مسیر اصلی منحرف شدند.
🔹
پس از تماس با نیروهای امدادی نیز به‌دلیل شرایط نامساعد جوی امکان اعزام هلیکوپتر فراهم نشد. کوهنوردان پس از طی ۹ ساعت پیاده‌روی موفق شدند خود را به منطقۀ دارای شرایط حضور امدادگران برسانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460037" target="_blank">📅 05:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460036">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d24f550794.mp4?token=q2MZWHLXxK52rl8-oxIbxC4pU5vlWz6wn91JgPeyHjJcVl2tRbWOAT7fdCZNJgQT6hdnapFZGEb0zp8cTGCvXkNtImGIt_pgkKzpfFKMod35NcWVzkXJsvFdJmWRegA4dbNLA-OMLlVY-JEPWMyhXcTdyHDjyjnYE0LjOaXR6vMNn27gQNiChbXNhi8szwauOgYsZU2tTNOCdfq9-NZxNxLIGBvwp6TVrjcgUmGrypz57LkkxYhAFQfPTFdxLbG7ID8ZNkT2apLPJTG5sKoLVDojMo_0ZEkiQWH8k8ZtcEiFO05UvXTA5KeqA0sTaeIomzd1793LhXvwuXI_JgQlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d24f550794.mp4?token=q2MZWHLXxK52rl8-oxIbxC4pU5vlWz6wn91JgPeyHjJcVl2tRbWOAT7fdCZNJgQT6hdnapFZGEb0zp8cTGCvXkNtImGIt_pgkKzpfFKMod35NcWVzkXJsvFdJmWRegA4dbNLA-OMLlVY-JEPWMyhXcTdyHDjyjnYE0LjOaXR6vMNn27gQNiChbXNhi8szwauOgYsZU2tTNOCdfq9-NZxNxLIGBvwp6TVrjcgUmGrypz57LkkxYhAFQfPTFdxLbG7ID8ZNkT2apLPJTG5sKoLVDojMo_0ZEkiQWH8k8ZtcEiFO05UvXTA5KeqA0sTaeIomzd1793LhXvwuXI_JgQlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزندت گوشی نمی‌خواهد بازی می‌خواهد
🎙
هادی زینالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/460036" target="_blank">📅 04:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460035">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba6YJVcLJYGUANdNbjJ_iRE8d8yeE6pLyXZ-TJitxbmvaRmdg1EVLR6nFg5zg1B1ui5gtMbhDXH9vR7JeEJyU7nl8Om3rw3p-5648qG2DRvE0gg13gctUBgWK54P1AZh6gSUOBGRKYD5ss3tjx6CRJ9XZaqZh_c_mB4bpTSBtP2hT0Q--6kg3JO17Nty3wxbQRUkuU4hsR0G3TGH3bW1rdgAE2B7BfMqTHtqNtiNPzzZCpcgJcXwMHbMHEMgf4fZGH9krutqlry1h86ncLEobThDJLweOYTbKs_LWDB6eEClvJRZlZgB4NTVsoKx7WmSuNROzzBUWEYczwf9ZmpL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ متهم آدم‌ربایی مسلحانه در مریوان بازداشت شدند
🔹
رئیس‌کل دادگستری استان کردستان از بازداشت ۴ متهم آدم‌ربایی مسلحانه در شهرستان مریوان، در کمتر از ۲۴ ساعت خبر داد.
🔹
این متهمین چهارشنبه ۱۱ شهریور اقدام به آدم‌ربایی مسلحانه، و ضرب‌وجرح تعدادی از کارکنان ادارۀ گمرک مریوان کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460035" target="_blank">📅 04:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460034">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ma2BWuK-9S4Ach9NPo2aue6PUdJ7cB8kJQjhGN3JigygFqUYYRoScMmZb0oQDx0jfpGp1TL60H54NjeKNbXBDzcUZwz5BBSaNp0qOppobpAmjj6cXzkO8Z9zVDW8AU7BY4G0BHJlMpaguGEsYvrfV0TaWq7q17zM6LO4C_tAyPEnm3fiAX2oPGwDidSVy3P_PQIaUD_PO8SDBorcBnzxrYM35g-1FQlTAjYCsTiv3YE4mDbkvqdno7oUWvpdWuD8ABeVqwBel72Wqj5sDSDGxTWYDqVx5SWj4U7_g4EXwQxcTHZhJn3ZpJ4bGyDqS3Yik9dYuMlaaGGyLecprzFPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین مدل چت‌جی‌پی‌تی رونمایی شد
🔹
اپن‌ای‌آی از مدل جدید خود با نام جی‌پی‌تی-۶ آسترا رونمایی کرد و آن را بهترین مدل خود تاکنون دانست، اما هم‌زمان هشدار داد که این مدل گاهی تلاش می‌کند از نظارت انسان‌ها دور بماند.
🔹
جی‌پی‌تی-۶ آسترا سریع‌تر و توانمندتر از مدل‌های قبلی است و می‌تواند کارهایی مانند آماده‌سازی مالیات، ساخت بازی، رندر معماری، قالب‌بندی یادداشت‌های حقوقی و جست‌وجوی آپارتمان را انجام دهد.
🔹
اما اپن‌ای‌آی می‌گوید این مدل بیشتر از نسل‌های قبلی احتمال دارد روش گام‌به‌گام حل مسائل خود را مخفی یا مبهم کند و همین موضوع ارزیابی عملکرد آن را برای انسان‌ها دشوارتر می‌کند. آسترا هنوز در مسائل پیچیده نمی‌تواند همیشه این کار را انجام دهد، اما توانایی آن برای پنهان کردن ردپای فعالیت‌هایش در حال افزایش است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460034" target="_blank">📅 03:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هیاهوی تبلیغاتی جدید وزیر خزانه‌داری آمریکا دربارۀ تحریم‌ها علیه ایران
🔹
وزیر خزانه‌داری آمریکا مدعی شد که اتحادیۀ اروپا رسما به روند «انزوای اقتصادی» علیه ایران پیوسته است.
🔹
اسکات بسنت بدون ارائه جزئیات بیشتری از این «موضع قوی و زودهنگام» قدردانی کرده است.
🔸
پیش از این رسانه‌های آمریکا گزارش داده بودند که جنگ اقتصادی دولت ترامپ علیه ایران، تاکنون ادامۀ همان سیاست فشار حداکثری با دوز بیشتری از هیاهو و جنجال‌های رسانه‌ای بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460033" target="_blank">📅 03:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko1N2-V-4fIn8yWjd5J7Ozv9KbycXT4fxAs1EcB1wxS9DWhEfjcepnUu9wF3GvuEplUEf-xwTPqtnKfKzrJE5vN_OvZT16F_QmYpO-KuOt383B6bIgQ6zoZ7y29THJEj-EXP-3k8NpH8qv1FWCyDpjjcTRvOKiRNu_5p-p8-VrMUfYUkcUfENoHlksDawZ1sPi7Uwimjl0letUSlvxvLPZP9A7ZcT5pETLUV441nBfzTxeueWUuh9MzLx5BmXzDhfHt34zsL6SdoEaH1zugElGveWQFquqTduhI0sCeVFruk147TURQv_02OoQqRCMjI9p0qAENAmlg2DcKCc8RZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: حمله به عروسی در ایران ناشی از اصابت مستقیم مهمات آمریکایی بود
🔹
تحلیل کارشناسان تسلیحاتی از تصاویر و ویدئوهایی که رویترز صحت آنها را تأیید کرده، نشان می‌دهد انفجاری که روز سه‌شنبه یک مراسم عروسی را در جنوب ایران به خاک‌وخون کشید احتمالاً ناشی از اصابت مستقیم یک مهمات آمریکایی بوده است.
🔸
رویترز نوشته که این حملۀ مرگبار ناشی از برخورد یا انحراف بمب‌ها پس از اصابت به هدفی دیگر نبوده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460032" target="_blank">📅 02:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM2BEr0bBpGXkTuv2MluOZW09uv0GDIjE954lwB--1rp5OM8aBozUqroB8H-VCB73kLLwD4YwMf4t9j1MhMTrmRf6N_nPPKR8c8ZnVsSXJ0Au6gDuHPEEIEDZ46kAVVNmxvgM4EHGdF5Y5EnELw_v3kucsB-90WA1GbUVMHiOJLBocHD9O0R60D5CLZoKxQu5hXNynEK0SCF_FPGQtYJ5A_2SeWmNYjLBZgrooNNYO4p2zdEP0jSdvfZ4DQBzAF-KQIkcYito4XkQo2pCOZik-RYCTrrA2Z_uKWqJ0mEwhiVyt_nb-WcgDy0TS4q-TPCutWX7a1pkPbKrHeNoqlqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ جایگزین معاون مستعفی وزیر جنگ آمریکا را معرفی کرد
🔹
رئیس‌جمهور تروریست آمریکا اعلام کرد که آدام تل را به‌عنوان معاون وزیر جنگ این کشور منصوب کرده است.
🔹
او جانشین دن دریسکول می‌شود که پس از ماه‌ها تنش و اختلاف با وزیر جنگ آمریکا استعفای خود را به کاخ سفید ارائه کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460031" target="_blank">📅 02:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpRXGz707nS30DTZ8LNH1ymZDoUUf9sy6mWHocKk4I4Gri6lJdJPdpeUT8m8cNOqCQAjVsguQGoNLRsF12QE0IzRZ7ChHZA_RFZT1t7_jiis2y3granoRMuK7tSU48LlsQHTVq-B3eLZac_H1OdtnZNnoNDgmjTC4w8MwPCr9faKWPOe6rO6qHxV9m2lfESRuNObz-NoHya_wCZCtTdKy_8oIKb5xs6jymEJuRuNMPmaAKf0CZVenCepx1yZQwwO-r0BvFueqkZzCkoBmJhhm9wDGYzokcpzkhhQu1petcoYcAvEmzLxkDcQPGiaf1Pyoa8_rjht9LxeP-BWrDXYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjRDRZU--pMwhd4zzVnePYldjiaKE3-ZEe3Hxc_3dtXDJHd0xd3xjKfASZ2mbDtBld9Ahe4xCfWB2ifIegZ9v0_hRKo9glClgHYdo8dfpWVJF4pgBZH_QY0RM0DSLCtSsxfCZ1x0BDc7bzv50P-D5t3pBwYjonYOi5edVU4fVAMukRlvzi1TTWloFFcuTVXlFayrV2pMA2PMRC01SaAVVjsTH5pvFwTeAJne5civAKdIE2WFOMhCOuuCnfPk7yTlK7Y-iU3B6k-Rmn4-0HMUDADoxtzIlxJCYxsUK25cN9h3j85EIu1bBm2sL_ozbrD0HErAAhqVHPkUju7ZHV8svw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEQOXFKHSzKJDdE7O_ks5ZINYExx5BPQTj2FS9CHKp1qc2L_Sh6JGBBkjyYLcWDJP9ATFPcZe72ldbjxdxFYPkdhavyXLs3IDjNjPNDvsKgiaaSXLs58FsRl9W0yeaDl-aduh27oEwshmx0DP-cgV0uRTuYy3XJ6bUr4jfPmTm016IqAmM7MPPZkgY_wvzB8ltbTu2b5RZZTFDQzvmD_JNKRLQQ9VOun_JBWsh0vGhcV4ppPx_Isw6boRXGB7jTvcE9OGel3BzjAjxgXTUdqs75bChjQPkNbWoaWrZXKCAOHdxde3Y9S7u-WVB98LUjpeIr0C0Sb9RcsiQXF6fMSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqN2GUsHnlHkNZoEnGGHEL7wDn_oLFtv0IqbhRGSkXQW_rArGdOH6b8vmNlpcZoD51F_PaQ76C9bPtO0Gkmh1ea-4H8rbogcMkyV9Y7_5xl1S1xHgXpbvd9Ae812C_GN9vDGUFIJIPEjj-ZUzMsBzOHK9C-WezFLrWKBql8OBrtLjhohMt8tg99CDXKN2Y1VWJ4YwbZKeRCitiQKL0lVN84Cd3OIIIOFCJ1cso30S1cJBXFJOOf8_C9-qsu3EFygLNc4IdOnc5Hug5D9-gVGiUQz_5r9cGGJ0LdIKZPADNuIKV9o0dYYXXu9BfPL6Wk4Tqh5HbIcJKxkcuVzDY-qcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع اهالی بندر دیّر با پیکر ۳ شهید بسیجی حملۀ آمریکا به جزیرۀ لاوان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460026" target="_blank">📅 01:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9a5461d9.mp4?token=Y_qls0o9hHuH-UDF5T9fdRc3rnFlzkS7QjMbVAVCkz5n1EEHA7pEeHcHQk3PMZiydoP2-Sqj9MM2nRbk8HVviqu4-d_Yzz6r3qud95IOlVfr6N29aC0z1enpsEm2J3ZKZBUuXNgCETdJoQQLfOL0Zb2ZJ8FseOKUKJoZmG9NT-ZHdUPG-YH4lalf3ZE4huZCNa4jIc7ISneEotY9vFCcWBHLbSLkJOmovffMQBIxVoZGnGNfE2GBkuGxXE6d1Po0GbfP9O1SAfKUc_QdihUv_0pjADTQEMgr7Jrxek2U-HEjSLJ3URFGlXAoNI9DLPswoZEjxolNUoMeH8KXFgKpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9a5461d9.mp4?token=Y_qls0o9hHuH-UDF5T9fdRc3rnFlzkS7QjMbVAVCkz5n1EEHA7pEeHcHQk3PMZiydoP2-Sqj9MM2nRbk8HVviqu4-d_Yzz6r3qud95IOlVfr6N29aC0z1enpsEm2J3ZKZBUuXNgCETdJoQQLfOL0Zb2ZJ8FseOKUKJoZmG9NT-ZHdUPG-YH4lalf3ZE4huZCNa4jIc7ISneEotY9vFCcWBHLbSLkJOmovffMQBIxVoZGnGNfE2GBkuGxXE6d1Po0GbfP9O1SAfKUc_QdihUv_0pjADTQEMgr7Jrxek2U-HEjSLJ3URFGlXAoNI9DLPswoZEjxolNUoMeH8KXFgKpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از تکثیر شهید سلیمانی وحشت دارند!
🔸
رهبر شهید انقلاب: امروز مستکبران از نام شهید سلیمانی وحشت دارند، ببینید در فضای مجازی با اسم او چه برخوردی دارند میکنند؛ از اسمش هم میترسند و از تکثیر او وحشت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/460025" target="_blank">📅 01:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlDoWsP8HzB3lshrSQnHYj0yoT9nRIeXdU_4S2Kt45YRJBGm8Ni6mLk2iOVGVmJo1xrfD-3qCmXzABk4_ijLY-7VYRbtqwagbAKHVPec1Amf9wp4Yw0F-uD216pVM8P63nm36GInU1YQ5x3q05YMvB9huUMCp82x-0ffpokBcLU0hXBuGu3uwjC-Ox8mrMIwD2F_FB8YlIqv5HpxponHIZpcULJoxAc4OpCJAPJAmQZps5UG6SNqiS1-ujiXbOl73muz9XLMEg6eFaax83oYy2ink2ckoDH-4-fTDPWoXfE6db37E6gDAsaFTd5zXo74-d_yps47I-g562KuVLYCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف مهمات جنگی سنگین در مرزهای سیستان‌و‌بلوچستان
🔹
جانشین فرماندهی مرزبانی سیستان‌وبلوچستان: در درگیری با قاچاقچیان مسلح، ۴ قبضه سلاح آرپی‌جی۷، ۶ گلوله آرپی‌جی ضدزره، ۶ خرج گلوله آرپی‌جی، ۲ هزار و ۳۸۲ فشنگ جنگی کلاش و ۷۹۶ فشنگ ام۴ کشف شد.
🔸
قاچاقچیان قصد داشتند این سلاح‌ها و مهمات را برای انجام اقدامات خرابکارانه و ایجاد ناامنی وارد کشور کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/460024" target="_blank">📅 01:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4a30d19.mp4?token=gjdOCXwSQlQg4MadEu-oJzBZ5GYZFJvyZlw9FU2Fp3O3KH5ocHMvl3oqWMPKh1moLxpecYe5zI4lOS9gUKDI700pCmWMgjVLQ3Vdoli_F-wO_taaKzFu_rRlZziKzmj0RWFMpTYU9nAsukqtSt7wlYDO81ttbnijMPr5R91fYaQtA9mCUZpJM6bmOGjPHxaIrq3EBVEsh5iiWMW47T3vLzk7L66XIQmqiYdFJG_D50X8CFOZTnrTqxYzbPFIaiKWVq3weF4zTKn7r5sXOcwoZgDl9QelCaBu_N9YLhPVGVxyCwh0Htc68z_bA4rXhICWkCJxvqVru5vk0_o4p9gGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4a30d19.mp4?token=gjdOCXwSQlQg4MadEu-oJzBZ5GYZFJvyZlw9FU2Fp3O3KH5ocHMvl3oqWMPKh1moLxpecYe5zI4lOS9gUKDI700pCmWMgjVLQ3Vdoli_F-wO_taaKzFu_rRlZziKzmj0RWFMpTYU9nAsukqtSt7wlYDO81ttbnijMPr5R91fYaQtA9mCUZpJM6bmOGjPHxaIrq3EBVEsh5iiWMW47T3vLzk7L66XIQmqiYdFJG_D50X8CFOZTnrTqxYzbPFIaiKWVq3weF4zTKn7r5sXOcwoZgDl9QelCaBu_N9YLhPVGVxyCwh0Htc68z_bA4rXhICWkCJxvqVru5vk0_o4p9gGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف ناخواستۀ ترامپ به عدم پیروزی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا در ماه‌های گذشته بارها مدعی شد که در جنگ علیه ایران به پیروزی رسیده است.
🔹
با وجود این او در یک لغزش زبانی جمله‌ای بر سر زبان آورد که نشان می‌دهد که حتی خودش هم به ادعاهایش در این زمینه باور ندارد.
🔹
او در سخنانی دربارۀ جنگ علیه ایران ابتدا گفت «به محض اینکه به پیروزی برسیم» اما بلافاصله سخنش را عوض کرد و گفت: «همین الان پیروز شده‌ایم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/460023" target="_blank">📅 00:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b56d43c04.mp4?token=WvNFrbiVXwIN3RrkyKIM45VneVtFNmWHkvKvneWhT9N_nT7rNCTb0Sqibcjq9FmYBMNbdy0rf_rPocN31TrLUs49wWu3UM50kZU5K6bayc_zZEQJV5RzdhJD6ACazKmdv-SmRWsLTbegxRlQpow-2C9LZDqDO8JvYvVFE4jWVwYsJEysCWA2d_XyCo75nJJl2a9VzaaC16nsdUU3dyrUVKs7VoexHa2gIpAKQKbt2LEpEKJm1BdyFw3imojra9qTqbng2zsrzhuLiD94FnaoW_qqrOp3zwt7gj03etukAEomYKlZnQFsPAyTfpZxvrE0J1UBs4RjzCjpcmxB8brFOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b56d43c04.mp4?token=WvNFrbiVXwIN3RrkyKIM45VneVtFNmWHkvKvneWhT9N_nT7rNCTb0Sqibcjq9FmYBMNbdy0rf_rPocN31TrLUs49wWu3UM50kZU5K6bayc_zZEQJV5RzdhJD6ACazKmdv-SmRWsLTbegxRlQpow-2C9LZDqDO8JvYvVFE4jWVwYsJEysCWA2d_XyCo75nJJl2a9VzaaC16nsdUU3dyrUVKs7VoexHa2gIpAKQKbt2LEpEKJm1BdyFw3imojra9qTqbng2zsrzhuLiD94FnaoW_qqrOp3zwt7gj03etukAEomYKlZnQFsPAyTfpZxvrE0J1UBs4RjzCjpcmxB8brFOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع مردم دزفول با خلبان شهید نیروی دریایی ارتش
◾️
شهید مجتبی باقری در حملات دوشب گذشتۀ دشمن آمریکایی به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/460022" target="_blank">📅 00:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYTWK2pYm2Sl2yaGaNYkXZRmj3ay0BxwGtsJWTJ4Q3lnQzkwJ_eXbuOOrgzyH1Xb5nlVZdNCfHFofzCfN47QuAn3hwfngdyKtMfVrfXqOOb95PHBJHi-2tCaCPBAbUwfMBJd61-_g0fYVqSClNdoLoB_FnQKoBVh34EDgbb3EEl3zmYn9PYQrchJ3c_eTzDbP-Tcx6XGHxER9Us0RjZhUruxb_5X5zqp0PSpDTgqx52M-c4jWoZMJgrmC42e5XRLXYsPFV6Kn7euVrTcx0vXBLee5miKC_2PQNINj8tAgCV0e-U6U123U3JEUvGTEDgZSWflh-UD6uGIzl0vn9bHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن‌پالیسی: چین با ابزارهای قدرتمند خود، از فشار ترامپ علیه ایران هراسی ندارد
🔹
رسانۀ آمریکایی فارن‌پالیسی: چین با در اختیار داشتن ابزارهایی مانند امکان محدود کردن صادرات عناصر نادر خاکی به آمریکا، از فشار اقتصادی دولت ترامپ علیه تهران هراسی ندارد.
🔹
چین حتی می‌تواند در صورت هدف قرار گرفتن شرکت‌های چینی، واشنگتن را با اقدامات تلافی‌جویانه روبه‌رو کند.
🔗
شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460021" target="_blank">📅 00:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460020">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8334da6f.mp4?token=HCuWUvZs-8dLQ9HV9YSJWKnpMNB11-YwW50JBher1nL4_RtVpA_OIcHgjQY-O2t41MzVreRxQzOoADctf14mVtpe6Vf29yr5TGOYFeQOlQRdjduBYfP0r3oy7zon0wN3jZ8kXwpcYDGMHUnEXQ8U4MHkT36HAmBdoWeleQhtckyEAcmn5CTqwmc7x-XwVwNtsqzrgrlHlZhtdQ_c8Sd-zmlFn3GqqNsI0vorhF0PwRLCU98auCN4g6ZlTgWBHvqGXqjHnuWkULKKp1MXC-UdZO2riELJWC2kESrqenTg8fHzKBqamm_N2nbiOuPATIzIFzlXg4ltvK0QEW7aXkv6FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8334da6f.mp4?token=HCuWUvZs-8dLQ9HV9YSJWKnpMNB11-YwW50JBher1nL4_RtVpA_OIcHgjQY-O2t41MzVreRxQzOoADctf14mVtpe6Vf29yr5TGOYFeQOlQRdjduBYfP0r3oy7zon0wN3jZ8kXwpcYDGMHUnEXQ8U4MHkT36HAmBdoWeleQhtckyEAcmn5CTqwmc7x-XwVwNtsqzrgrlHlZhtdQ_c8Sd-zmlFn3GqqNsI0vorhF0PwRLCU98auCN4g6ZlTgWBHvqGXqjHnuWkULKKp1MXC-UdZO2riELJWC2kESrqenTg8fHzKBqamm_N2nbiOuPATIzIFzlXg4ltvK0QEW7aXkv6FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم نیشابور در قرار ۱۸۷ خیابان را ترک نکردند
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460020" target="_blank">📅 00:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460019">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حملات هوایی و توپخانه‌ای صهیونیست‌ها به جنوب لبنان
🔹
منابع لبنانی از ۳ حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در جنوب لبنان خبر می‌دهند.
🔹
توپخانه ارتش رژیم صهیونیستی هم اطراف شهرک النبطیه الفوقا‌ و کفررمان را مورد هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/460019" target="_blank">📅 23:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460018">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cbc03b8f.mp4?token=qqtXrs4rZYIz9MPe0VvlpL5rONg4mBCLFWV7j_ibtzkDkYiKCBIz8hzWTdib_iXePkRIH4ncKo7PPLUgULBp1e1GCRAiwmfNcYV957_xbA8_1Gl9WzJye43Gq6YNWxz7U7e2z7AtHhzXGTeY1-nx1V153wnHTOzGwsCJR5FIv2Y36TO39_1ArXtBdKdADEtHAAt8BceZPRs5me3TG06yUbE9XFc27N4_124EjopFSkfKFXpgz_WtAo2p2fv-Ne3H9zPcvrT6jSbgeFdPmW5i89U_PZ-xg5sUQEfzjbW72GidkLJ4ts8YhCAi5W5AaNNIHNYJIMg4ZHr3nZNukXOD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cbc03b8f.mp4?token=qqtXrs4rZYIz9MPe0VvlpL5rONg4mBCLFWV7j_ibtzkDkYiKCBIz8hzWTdib_iXePkRIH4ncKo7PPLUgULBp1e1GCRAiwmfNcYV957_xbA8_1Gl9WzJye43Gq6YNWxz7U7e2z7AtHhzXGTeY1-nx1V153wnHTOzGwsCJR5FIv2Y36TO39_1ArXtBdKdADEtHAAt8BceZPRs5me3TG06yUbE9XFc27N4_124EjopFSkfKFXpgz_WtAo2p2fv-Ne3H9zPcvrT6jSbgeFdPmW5i89U_PZ-xg5sUQEfzjbW72GidkLJ4ts8YhCAi5W5AaNNIHNYJIMg4ZHr3nZNukXOD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرایان خراسان‌جنوبی؛ ۱۸۷ شب، یک قرار و روایت ماندگار همدلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/460018" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460017">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
بروجردی‌ها در شب ۱۸۷ همچنان باقوت در میدان ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/460017" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460016">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le78mLpPwiU8_FeTjb8jb7c5440wUvNoPix5kTw3sZyrLZX3eTxQ7Le1BWCdUN-MnVS6rmkjFxS1_dotQiyO_DtBHFwbWDXB2erNCjq7RylYCH5TgRPCftTMNQgCY40m0wpKgG7Iq_Tje7igEiKORM6UTdgNT_Igmk95K1pdIh-yUZkOaq83hYfCiwbE9vMon10-wtDSNnD5FQYWyAj52w9jsqJdHUn5d84mEod5V0qHINam7wGtn24P0SSog5q0P7nkawwE5AvF7tUR9LTiaiyyXhIQN7PEkQlQPFrmxXmO1LCcmkKDt41Al_zwiV2dsfvwyKCmcBSPX0g0K4fR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: برخلاف آمریکا، ضربات دفاعی ایران منحصرا علیه اهداف نظامی بوده است؛ گزارش رسمی قطر نیز اثبات‌کنندهٔ این واقعیت است..
🔹
سخنگوی وزارت امورخارجه، با اشاره به سند ثبت‌شده توسط قطر در اتحادیهٔ بین‌المللی ارتباطات راه دور (ITU) که در آن تاکید شده ضربات دفاعی ایران، فقط متوجه پایگاه‌های نظامی آمریکا بوده است، نوشت:
🔹
دولت قطر در سندی رسمی که به اتحادیه بین‌المللی ارتباطات (ITU) ارائه کرده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر منحصرا «متوجه تأسیسات نظامی آمریکا بوده است و هیچ منطقه غیرنظامی هدف قرار نگرفته است.
🔹
تنها استثنایی مورد ادعای قطر، حمله به یک تأسیسات گازی در ۱۸ مارس بوده است. اما در این مورد هم باید در نظر داسته باشیم که آن تأسیسات در آن زمان در خدمت عملیات‌های تجاوزکارانه آمریکا علیه ایران بود.
🔹
این واقعیت، یعنی دقت و مراقبت ایران در تعیین اهداف مورد حمله، را مقایسه کنید با عملکرد آمریکا در حملات مکرر به غیرنظامیان و اهداف غیرنظامی: مدارس، بیمارستان‌ها، مناطق مسکونی، مراسم عروسی، پل‌ها و موارد دیگر.
🔹
تفاوت عظیمی وجود دارد میان ملتی متمدن که اهمیت پایبندی به اصول اخلاقی و انسانی - حتی در دشوارترین شرایط - را آموخته است، و حاکمان جنگ‌طلبی که در قدرت‌نمایی‌های خود، هیچ اصل قانونی یا قاعده‌ اخلاقی را رعایت نمی‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/460016" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460015">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pea59xaaP8HDmQ-YpEB1YZQCsaQPNO2NzLlNDq00oLBciA7DVxDizr9yMTJyAp53Qjg-r00LFo58sDwMSxKJtastNJlmeHz7jlyGUd0IKwrOk87XlVxrhff6jwu0PqAyrbCVROSBAn9fJxYVOgesQA0_PxIQ9sOT7WjNiTnh9jFywi01m-oXT5TRYeKec2BdbzyBdje1n5z8gah-zVTIRXCDIaPUJ7uopx2HKPp7z8gJe_og__Ak9Qfg2QvL9fYyIxi6hZodJlKyLWum56eiTZReZ0fc-7Ut2JY4acY4TPGbu2OgKk8quWURryHk94HbT87rKu8dykJMVLoszCRQMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقدام جدید آمریکا علیه دانشگاه‌هایی که اسرائیل را تحریم کردند
🔹
گاردین: مجلس نمایندگان آمریکا روز پنج‌شنبه لایحه‌ای را علیه جنبش دانشگاهی بایکوت اسرائیل تصویب کرد.
🔹
براساس این لایحهٔ دانشگاه‌های شرکت‌کننده در بایکوت اسرائیل یا دانشگاه‌هایی که برای جلوگیری از شرکت دانشجویان در برنامه‌های تبادل دانشجو با رژیم صهیونیستی شرکت کرده‌اند، جریمه می‌شوند.
🔹
لایحه‌ی «حمایت از آزادی اقتصادی و دانشگاهی» با رأی ۲۳۷ بر ۱۶۹ به تصویب رسید، به‌طوری که ۳۳ دموکرات برخلاف هم‌حزبی‌هایشان به آن رأی مثبت دادند و تنها ۲ جمهوری‌خواه با آن مخالفت کردند.
🔹
در پی تجاوز نظامی رژیم صهیونیستی به نوار غزه، اعتراضات دانشجویی گسترده‌ای در آمریکا در محکومیت جنایات اسرائیل آغاز شد و دانشجویان تلاش کردند تا روابط دانشگاه‌های خود با اسرائیل را به حداقل برسانند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460015" target="_blank">📅 23:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460014">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43137cc482.mp4?token=iXJDP4E_3M9k-mg2J0Uh624ULiu7PQYdCXw-DKP3mguaZHkr5VQ4-YsY7vMqLCnnRH2-wC5UJF_EAiFcqDSTRvbq22hhFdwqZcq5HO_MoUUvbsVmkFrtPTI7mWCyVx5SAoBhhNwutyN4_DWvwGOYfh3AjWB-IgDy_9-FNdNQ36EmKdGZjwyY-BN6HOxMbmjT1dz4JvogTGNBn3-QeRUEInSnNnDK4jC0oV5RDn2ocSMwRSPAQQCx5jB8JqHIwRQGtPE_Ep4Np0uF3IwN-OfEiPlFgt74K7AfAmJpIPhL4rQ__QZqfn3X6KCQo7sPh126fb7QazQ53KCfz8rPJdlz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43137cc482.mp4?token=iXJDP4E_3M9k-mg2J0Uh624ULiu7PQYdCXw-DKP3mguaZHkr5VQ4-YsY7vMqLCnnRH2-wC5UJF_EAiFcqDSTRvbq22hhFdwqZcq5HO_MoUUvbsVmkFrtPTI7mWCyVx5SAoBhhNwutyN4_DWvwGOYfh3AjWB-IgDy_9-FNdNQ36EmKdGZjwyY-BN6HOxMbmjT1dz4JvogTGNBn3-QeRUEInSnNnDK4jC0oV5RDn2ocSMwRSPAQQCx5jB8JqHIwRQGtPE_Ep4Np0uF3IwN-OfEiPlFgt74K7AfAmJpIPhL4rQ__QZqfn3X6KCQo7sPh126fb7QazQ53KCfz8rPJdlz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تشییع پیکر شهید حملهٔ آمریکا به سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460014" target="_blank">📅 23:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460013">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtNAdmc6FoTmXePnpTwOEOHu4dtXWaQ5aTVpe0sVfth-pNBU7WtDcr-bZq9HxMeIkhWtiygBZ8vuoPbrQ3oi0QDKLdmj8pTbXlOj4ohYSbQG_zGT366FqgVLh6p95l1SRP6h9yIdcnOqSo2O2lN97VGhznP_SQ2u-sDIcXSirDPiLxMkG-gmntpe56eIMnFSgR0zdyGkFejRg46jkA-4GBi6BJrTcytDZvZxwSbDN7Z4jgCEwvuPF99VUhOCytY_NRwOVyWSYYCJqcIVhBLXzII-cxvKrjqgjq9uoemafLBz5iA2u1H-o28RynbuMYqOS64YcJR2WO325OaL3jXP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشروی انصارالله در جبههٔ تعز و فرار مزدوران سعودی
🔹
منابع یمنی از وقوع درگیری‌های شدید میان نیروهای انصارالله و مزدوران وابسته به عربستان در محور تعز و در جبهه مقبته و ساحل غربی خبر می‌دهند.
🔹
براساس گزارش‌ها، نیروهای مسلح یمن(صنعاء) موفق به سیطره بر «مناطق راهبردی جدید» در استان تعز شده و به سمت بندر المخا در حال پیشروی هستند.
🔹
بر این اساس، ده‌ها مزدور سعودی از جمله فرماندهان رده‌ اول کشته و شماری نیز به همراه خانواده‌های خود پا به فرار گذاشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/460013" target="_blank">📅 23:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dmz7v6-mvmmgF1QPZ5Lo42Zt2Oic6eevSStoYWNYstDUWA0KUp4gN0hQFWeF9ffRJjQBwWIjIoo84pDrD_vIIKdlwe_03Q9osiMuKiW4Lv9Tr8HIwH1wrYwLL6NeuQhIikD4a4tAE5Si5Msn8Bv3NBlp66LgU7d0wwrVkWTdEZlRpPyi7CscyYucJ_zTdsk0Ucs-gs-ymAPjNqLjiOS68fGlGCoqXXqDMBE-LIN7vX-oZKcFfdJgRPgW9LIrv6FGcp2gSsuv4sMz3BmD0pj5ZUlZip6wXiUl9FLapYxOa1klkjMz_TxdqpHitJ_de6uYI6JeH_FArWqQOMDw9KAMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhZEML7rS8JcRDpnz_hQiNNH3upzElBKFf9JJiGPxmJIITEt_8XA98ce-CCfIXTln0yrsfidIjmyHMAqLzJb2amRyZg-QZNAH-sn7UPLyut7TEC6lZLpMuLvKE75WD60kLv5KwmUyza_RrpjAK4GfCOsf_fNLQIeota9o4XBdFay6iM2CsJCh7a2R3RF05PrHTnHmpaZ8QCad1CazRbwY5ivvywyrQ0JPf35u9jrQFbePQ2BtwLYfKhX4Jxahk9k2N8r59GTbXaHTMSpLEwgP1E8u3jQUE17TxdmE2Ucl2U5dTO-U3SmFm6A426NVIPrNVpfHALp6rvHIUXtxuvnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cyj_VAX-khfuKk0JHhLLuHfNhh3MMfl1jsK0rucAnichUEWiP80ebAaT5tAh25WqO-k1hNI4_D87zx7X93il3h6fUcrdFrHtFIKBw9g8IC_Rqydet3kJfwLIKswvMEwsaUUhzoXWHnLOejfVu3bvICJcbrUTiC2-2XKxjOsdpuQFsrNBz3bc8hvWEOIFe7ffSePWBj-epYVILY7i9TZ3UFJt2bBB_bl5N9iBMWHZrIc6_B5t3MOhqpeTsyMGwaLhZxjYE5TZ_bbo38QCTyODgYS8bGWSnozH1JxQec0rpT7UuA39JDqI_NPD10-9rviafhWvW1Gd7K6dwqyCTMEc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrT8gurI9dEePkE8BCvhF2p2I-TwBgmtuk5oo4030aZ-A3UIgzgHtqcWuR_0VWu4Vd_kZNYT93iC8zEoghciiOh2Tnnfbcj8APIQg-iiuRAAWvbsMGXvZ_fDsrXD1CGyeySjCBmV1fr58J3h2lFAFfFISkqS9rjTetPS9tdigZ3zUZu1aEd3NgIrpoaXhQd8KtC166t4T_8EcwpJJ22TCz3kZE1myrzRliIQJRDJY8h5DQnZt5G5T65RToK7Na8dqoi_Su4zmMD16g2m_N_B3uk_0Uei4wMAOYWvvHu3PbDDLyVviuqnG6ESTgbgN7xvp3RNSf34HlwhnjSogPqBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcUKvg9ONVX428L1nG-mM5-0gnMVq0wZ5gZMDS10Bq1ZQFHxjwdo0D59sLH5Nv8mUbAjmmwc3HEfSvOF3CcicnN18A5TKxiMFhHWA4J6Eir-S0VnSaRVuya9pYrb5_4ZhDd_9Hah7blMCWnRk57p9UqSozk9Ziut9A8Fs64eP-Exk7LU8akw6H7lpWN2TrvLgnKURLxG5PD1RDD08580pNGueSWoubkSuDchUqYDXBapKxpc6loaPk179Yon9ddBK0ZyN2eCtQjVg7SBu0h3PPUtCiDgjszQT5haOnc9CcLVBHHalXYt--hK04EWMW8tXXAvNJXOnPfefk373EzTjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ سردار شهید جعفر کهریزی تا زادگاهش
🔸
پیکر مطهر سردار شهید جعفر کهریزی که در حملهٔ دشمن آمریکایی به شهادت رسیده بود با حضور مردم در روستای کهریز کرمانشاه به خاک سپرده شد.  عکاس: بهروز احمدی  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460008" target="_blank">📅 23:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb0-Au2rHkvapJR_-Cpgp8wlxHVmiNm2BcnL4A520JTqoAVU0tQlpbHY1w1kKhPxGjVsVNiesRaYJoPNw4hMILYGo9-U7EO7J49X93mNnqYEHLKfuoaGN-eDDism5JJAvS69KwEV3IJFEVtHBHxlEX-0aFveKx1VPlC94aY17GjYgohcmJBPVKeD3nLnZM9PZIfpeKAlABiSwhjJ-1u8LomyM-LtGo9YOwBEq4wcXlV376B7v5CkHLbwUFQcvNrgyYuzqR8MolJY2YrlAkDmGZr6PKOew9j3WkERd1bs9AgK08iLNwsp7TVL1KfAsV9SdZdenxprG5DSaY6Ucyw_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس صهیونیست‌ها از احتمال حملهٔ موشکی ایران
🔹
شبکهٔ ۱۲ اسرائیل از نگرانی‌های این رژیم مبنی بر احتمال تلاش‌های ایران به ویژه در ایام اعیاد یهودی و هم‌زمان با سومین سالگرد ۷ اکتبر برای ضربه زدن به صهیونیست‌ها در خارج از فلسطین اشغالی خبر داد.
🔹
این شبکهٔ عبری افرود که ارزیابی‌ها در این رژیم حکایت از آن دارد که هدف حملهٔ موشکی ایران به بندر عقبه اردن، ارسال پیام هشدار به اسرائیل بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460007" target="_blank">📅 23:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e1734fc33.mp4?token=Fqvh9XpTk7ePMszyCWS5c08wSR8QMV32GrO4Lv4RiWRQ8qcOwEs_cWz8Hu7Zbd2m_LC6GWFASguDW_2HnOc0fntOQPWPL88-kHBQoQUg1e3_ZdC3UZ7KRxFdmE_VqRdjoCieyTCc7rO1D1fs12orzS6t1anulFomqo1EwefXeYXe4kwSkNPXl0vSAaN_la3_1LZ62CHRuBrgxyxf8qtHtLf0cuh-ZWWzI9btx8aePUuXFWuJnm3xiH7PQT1TujPOuO_LvfktLfodj0Q79NX_Y70wTtC70wVggF9OSmE2cfr_LARSRCPhVnazHhP5dmwyYiFtGfu_gkxi_RE18iqqcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e1734fc33.mp4?token=Fqvh9XpTk7ePMszyCWS5c08wSR8QMV32GrO4Lv4RiWRQ8qcOwEs_cWz8Hu7Zbd2m_LC6GWFASguDW_2HnOc0fntOQPWPL88-kHBQoQUg1e3_ZdC3UZ7KRxFdmE_VqRdjoCieyTCc7rO1D1fs12orzS6t1anulFomqo1EwefXeYXe4kwSkNPXl0vSAaN_la3_1LZ62CHRuBrgxyxf8qtHtLf0cuh-ZWWzI9btx8aePUuXFWuJnm3xiH7PQT1TujPOuO_LvfktLfodj0Q79NX_Y70wTtC70wVggF9OSmE2cfr_LARSRCPhVnazHhP5dmwyYiFtGfu_gkxi_RE18iqqcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: حفاری بیش از ۳۰ حلقه چاه را در پارس جنوبی شروع کردیم که برخی از آن‌ها به نتیجه رسیده است   @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460006" target="_blank">📅 23:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53969dced.mp4?token=bomvEbBSJrPgtHX5Dd-bIDyD8f9Z7aKV-ZFP2vA_ICsy6F_5XHbHQzkRYYCxlMpTTwB6q1h0bLgX0md9T1zBOmerQxAAau3lIWQy7pfXW9opRlFJnOgZrwuHVeLc9Gvw4fgq0q7TkUfqOP-dUTobAChmbmAqap8HeJZxlCxc1TOP9iHANrj2j8MkjWhDEgLtXmNaPSDeFm70HhTEqpw_N9UVkqZ1Vwrbz7vLVptt1Iz_MSt6ays3TmT9yrMhtWmbEXfR-Zf7TQIKNSSZxRC8vdnkJM6R9RWIt6H7eRiLhmN-fmkNUAVVLiL9PTfIAbJUwF_X1Qr4LimCGgVD5N9FMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53969dced.mp4?token=bomvEbBSJrPgtHX5Dd-bIDyD8f9Z7aKV-ZFP2vA_ICsy6F_5XHbHQzkRYYCxlMpTTwB6q1h0bLgX0md9T1zBOmerQxAAau3lIWQy7pfXW9opRlFJnOgZrwuHVeLc9Gvw4fgq0q7TkUfqOP-dUTobAChmbmAqap8HeJZxlCxc1TOP9iHANrj2j8MkjWhDEgLtXmNaPSDeFm70HhTEqpw_N9UVkqZ1Vwrbz7vLVptt1Iz_MSt6ays3TmT9yrMhtWmbEXfR-Zf7TQIKNSSZxRC8vdnkJM6R9RWIt6H7eRiLhmN-fmkNUAVVLiL9PTfIAbJUwF_X1Qr4LimCGgVD5N9FMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست مردم شهرکرد از نیروهای مسلح؛ «بزن، الان که وقت انتقامه»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460005" target="_blank">📅 23:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460003">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823b00509b.mp4?token=oVJsOMwIEt6_Wah6zRjwhVYPpYK1wNGAxUqFvAwj8wDzT-qTVzjWYjbj97n5Z_VQpXeqAXaKY9BJFl_gPTzZCXAjzWNseRbL86HpoFAhPXz8URQepUZtKq-DbZVfGNDuAAh6-tkUAgp4Xi9mZeHBOYismldlBIHtzBJcD7dEJ4mxfTpqS0fQNAKls8IghsaYfLz1bAVnC9Ou9WzF5N0UOukE2wbokeHPrLvis1BK715m60ULPXSg8e_9KChXUKn9TPn-JlyqP0ipRV7u0vUWUg5b8yojaVszpi7xAx1vP3rB0_wUzq7G1T74MDa2u-Nu4O6W4fvHFHhbwJ7uffIVJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823b00509b.mp4?token=oVJsOMwIEt6_Wah6zRjwhVYPpYK1wNGAxUqFvAwj8wDzT-qTVzjWYjbj97n5Z_VQpXeqAXaKY9BJFl_gPTzZCXAjzWNseRbL86HpoFAhPXz8URQepUZtKq-DbZVfGNDuAAh6-tkUAgp4Xi9mZeHBOYismldlBIHtzBJcD7dEJ4mxfTpqS0fQNAKls8IghsaYfLz1bAVnC9Ou9WzF5N0UOukE2wbokeHPrLvis1BK715m60ULPXSg8e_9KChXUKn9TPn-JlyqP0ipRV7u0vUWUg5b8yojaVszpi7xAx1vP3rB0_wUzq7G1T74MDa2u-Nu4O6W4fvHFHhbwJ7uffIVJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: علت گرانی فعلی بنزین در آمریکا، حملهٔ ایرانی‌ها به کشتی‌ها [در تنگهٔ هرمز] است.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460003" target="_blank">📅 22:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0e9b2f62.mp4?token=tcbgcgCkHQ7RRKJq_2ymWBHZ-p8DEI9-qttyMOc5HY1ocGr50fZygrolXohybJ-Ad3hp_EtfrafgxrkKO2i-FjOgmXqMXaWqn2NBxrvLNDMSLfgTBnr0QGPqP_nOFlJk7ZMkqL0du1OTwkpFIqHf6ICB6-nxWE3OtzInVY4pZjm9FwsK6khtTHPO4AproZhCCQuir4BuoV7Z10GfcwDIsa3oZOu-XCZSpd7bAJFf7rmX7tU-OLNVuOwbx0pC3gZFSQV07ZmHi2P6guMvWKyQUOkzAvOmfAMt1UhutYEcYvU5dFOuWYmLDjM4oRdKXVDCKFeB6SCIMw1XbQ91Sa0GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0e9b2f62.mp4?token=tcbgcgCkHQ7RRKJq_2ymWBHZ-p8DEI9-qttyMOc5HY1ocGr50fZygrolXohybJ-Ad3hp_EtfrafgxrkKO2i-FjOgmXqMXaWqn2NBxrvLNDMSLfgTBnr0QGPqP_nOFlJk7ZMkqL0du1OTwkpFIqHf6ICB6-nxWE3OtzInVY4pZjm9FwsK6khtTHPO4AproZhCCQuir4BuoV7Z10GfcwDIsa3oZOu-XCZSpd7bAJFf7rmX7tU-OLNVuOwbx0pC3gZFSQV07ZmHi2P6guMvWKyQUOkzAvOmfAMt1UhutYEcYvU5dFOuWYmLDjM4oRdKXVDCKFeB6SCIMw1XbQ91Sa0GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: شهدای صنعت نفت در سخت‌ترین لحظات پای کار ایران ایستادند  @Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/460002" target="_blank">📅 22:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460001">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e00759c5.mp4?token=Y7-9GzH8SLQVoJyTPuy8-7UWOhjyTeIfxP_c5DdFUeCUepxEku8kh_TsHGxrBv1yvYace19PmAzTDYHakKosZr8m5kcOVDgGwRPybsRod5mP1cez608_i7JSY3zNKqO_JPVDBlxy1t0VXsk6H-uJNNYkvEtwRyJivconHw7M6wTjIfeHbFUX1xZASMeo6yPU6R_o5dGfJmEtiTi37oiLbI5HjQy2_KnLI15FORoxv6i-hLmyxu41b-OCumqjDOsJHbVR3HWEEBZpVyysTPKHRzCgzr5U_IMZJF53xUH6iBOjuSSck3QqEf_Jda3LRvXQd17sk5xTNpmBTVHegODblw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e00759c5.mp4?token=Y7-9GzH8SLQVoJyTPuy8-7UWOhjyTeIfxP_c5DdFUeCUepxEku8kh_TsHGxrBv1yvYace19PmAzTDYHakKosZr8m5kcOVDgGwRPybsRod5mP1cez608_i7JSY3zNKqO_JPVDBlxy1t0VXsk6H-uJNNYkvEtwRyJivconHw7M6wTjIfeHbFUX1xZASMeo6yPU6R_o5dGfJmEtiTi37oiLbI5HjQy2_KnLI15FORoxv6i-hLmyxu41b-OCumqjDOsJHbVR3HWEEBZpVyysTPKHRzCgzr5U_IMZJF53xUH6iBOjuSSck3QqEf_Jda3LRvXQd17sk5xTNpmBTVHegODblw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: توانایی ایران برای اختلال در زندگی آمریکایی‌ها بسیار محدود است اما صفر نیست.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460001" target="_blank">📅 22:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460000">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0539e701d.mp4?token=vAoElMCtJuuaI5k9HupNhHqLVw7l9cF8E7WiGixFD1mj4VZqhthlZVuCzdfU__WbRAzkLUfnbmxrFFYXm_2tUHm1xj-w9P6U1Mx9L326wcHRB5UB2xgfmPMxFvS0O-yT_fZXaHLBGuTY3AstOdr2AzRvqhX6-06rjbVmSetlmmcupPI-R_7R7W2MiVP0uqDi6WRZVXjieaX8HRbOwfOLqM1ooLpKmsJjj5hHmSiSufw2IOhzddMyJVwkDlpv-ysPWKWyDCuvvt91mzi_f2fmeDoOL9zDbahpbCHTaZSMT111yd6OFD4Cx55h1exd_TDOw_NQ6mBoaSnuiFCeLGDk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0539e701d.mp4?token=vAoElMCtJuuaI5k9HupNhHqLVw7l9cF8E7WiGixFD1mj4VZqhthlZVuCzdfU__WbRAzkLUfnbmxrFFYXm_2tUHm1xj-w9P6U1Mx9L326wcHRB5UB2xgfmPMxFvS0O-yT_fZXaHLBGuTY3AstOdr2AzRvqhX6-06rjbVmSetlmmcupPI-R_7R7W2MiVP0uqDi6WRZVXjieaX8HRbOwfOLqM1ooLpKmsJjj5hHmSiSufw2IOhzddMyJVwkDlpv-ysPWKWyDCuvvt91mzi_f2fmeDoOL9zDbahpbCHTaZSMT111yd6OFD4Cx55h1exd_TDOw_NQ6mBoaSnuiFCeLGDk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شهیدان حاجی‌زاده و باقری در رزمایش موشکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460000" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459999">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4e36871b.mp4?token=ewZHZmJtgQkLfq4JeiefkGuF1fsKtHHcvo5Tx3cMj9bajTqNKSGyhgLEr2WcDlaQNcu9dsqO7xLXuiTPnGFaAj2iZdXJ3yVil-p1cgmGF9yCkKRfFihZJ-hF9I6gKc2B-911CdzSoO0wV4Nu7-PkY9jXZGJ5ZOobqXRAPp3Mxn7ElqPrbW1OI-eJQoGPt7TYE8wkM8zofNsIaw_gve8QYIjfxdDluGvGWjBYnInsDiFd-bdxcWRyYmyxMkCZZfxeOqdwCAnAWwhS32lAu1BMbpe30i1JYwKWB8pvmhSam6_geu6Z_q2QUb48x3142kFpMJnYLSlct01ZLP8PqZ7x1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4e36871b.mp4?token=ewZHZmJtgQkLfq4JeiefkGuF1fsKtHHcvo5Tx3cMj9bajTqNKSGyhgLEr2WcDlaQNcu9dsqO7xLXuiTPnGFaAj2iZdXJ3yVil-p1cgmGF9yCkKRfFihZJ-hF9I6gKc2B-911CdzSoO0wV4Nu7-PkY9jXZGJ5ZOobqXRAPp3Mxn7ElqPrbW1OI-eJQoGPt7TYE8wkM8zofNsIaw_gve8QYIjfxdDluGvGWjBYnInsDiFd-bdxcWRyYmyxMkCZZfxeOqdwCAnAWwhS32lAu1BMbpe30i1JYwKWB8pvmhSam6_geu6Z_q2QUb48x3142kFpMJnYLSlct01ZLP8PqZ7x1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: بعد از جنگ ۱۲ روزه توانستیم تولید نفت را حدود ۷۰ هزار بشکه در روز افزایش دهیم  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459999" target="_blank">📅 22:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459998">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a77de4b.mp4?token=PGzY3KMv-f23_KO-wrVzFJMNFu2s3fKdF4pdVcgYTCeV7vpwDLHM8kX8TpqBsPKj45RUbXxPwZ_hPnCb31oF_FzsLPjT5tVQCe8ouEH25Fmj3YErRsosYRCCvqLWHGUGRwHeFzT3Ykq_e8vZ030-OIeCkvat6crMU4f0NFhqx-Xx_5HROP4SAZEKxtwHYFPA4vnA5HhR93JrQPAhxahtMYknfkW4wiW2um-s7IxkUq5NH8OBB4TWoBTb7XM0zbEurm0iqJvyThcpxSYuA13JeWUA_PcmgFk6TH2UebijRj-6XM2nnuy0nPvOwTeqiDQanvF3DNV9YyTfN8w8_Cv0hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a77de4b.mp4?token=PGzY3KMv-f23_KO-wrVzFJMNFu2s3fKdF4pdVcgYTCeV7vpwDLHM8kX8TpqBsPKj45RUbXxPwZ_hPnCb31oF_FzsLPjT5tVQCe8ouEH25Fmj3YErRsosYRCCvqLWHGUGRwHeFzT3Ykq_e8vZ030-OIeCkvat6crMU4f0NFhqx-Xx_5HROP4SAZEKxtwHYFPA4vnA5HhR93JrQPAhxahtMYknfkW4wiW2um-s7IxkUq5NH8OBB4TWoBTb7XM0zbEurm0iqJvyThcpxSYuA13JeWUA_PcmgFk6TH2UebijRj-6XM2nnuy0nPvOwTeqiDQanvF3DNV9YyTfN8w8_Cv0hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: در جنگ ۱۲ روزه انبار نفت و پالایشگاه‌های فجر جم و پارس جنوبی هدف قرار گرفت  @Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/459998" target="_blank">📅 22:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459997">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1a092430.mp4?token=QqryeD4X2bjYcLeIKU4VQsMy515Ykw3hUwVnTEIB60zLbmT_iD21JGpYIatUtpNcNBvSIUfr9-6RARE-VOmJszfJwulUCvFlkue2GL4gd0t48lNk2qI9Jg8Vd2kETG3XNtaUgL5nY4FL_MAobnxvs91Q3uPMAQLD8q2d7FQRARs01jIPM83vrRLpDvu6X-fq5JEXCSlwiwEj__W6UbIVrI3lXsoddUXvOjlcwfRGoZqw-waPN46JEAcWRYwPxGeRq5-Ygd1LeiS0cakSq6iVzbNnr8v6cP4aJ0DaK8_q6uVR0Z0VZArY2QUnANBjjRwosSnqPFW_xkRV2ECt2tmv7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1a092430.mp4?token=QqryeD4X2bjYcLeIKU4VQsMy515Ykw3hUwVnTEIB60zLbmT_iD21JGpYIatUtpNcNBvSIUfr9-6RARE-VOmJszfJwulUCvFlkue2GL4gd0t48lNk2qI9Jg8Vd2kETG3XNtaUgL5nY4FL_MAobnxvs91Q3uPMAQLD8q2d7FQRARs01jIPM83vrRLpDvu6X-fq5JEXCSlwiwEj__W6UbIVrI3lXsoddUXvOjlcwfRGoZqw-waPN46JEAcWRYwPxGeRq5-Ygd1LeiS0cakSq6iVzbNnr8v6cP4aJ0DaK8_q6uVR0Z0VZArY2QUnANBjjRwosSnqPFW_xkRV2ECt2tmv7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اروپایی‌ها به‌صورت علنی از ما انتقاد می‌کنند اما در خلوت به ما می‌گویند اگر آمریکا در مقابل ایران کاری نکند، هیچ‌کس دیگری در جهان قادر به مقابله با ایران نیست
🔹
ایرانی‌ها باید حمله به کشتی‌ها را در تنگهٔ هرمز متوقف کنند. ما با آن‌ها مذاکره نمی‌کنیم…</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/459997" target="_blank">📅 22:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459996">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a46994777.mp4?token=CMk0A0E2GGzRvUjbao07ERQtNu72Vx4QEck3n5Q7A4ercHrIpN-rtzYs9fbn6f_06pNSHETYKV6VotA9ys5OpZEY4oEMF7ZyqYziGip5qBBx10EfHPbZS2OziOoF_PCHXKtwUMAccFRdc9rNZsLl8gwQGsevf69hA8V_qz8tKVBHnRhuE909bOXrhnMED2cAeU9rn3NZ-4cYFRPaVpYEfZSKZMD6Qbv6jd3NR0MuRa2i9uGJ3uXPHjiqTYdr6Fg_hGA5LoA9FVc8oNtdiYspg-DOyQbgOqkdMp5bvy8t5H3Wanucjzx6i4TgSbG0prw0jmliLZqrLNX9ODBfa6pfTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a46994777.mp4?token=CMk0A0E2GGzRvUjbao07ERQtNu72Vx4QEck3n5Q7A4ercHrIpN-rtzYs9fbn6f_06pNSHETYKV6VotA9ys5OpZEY4oEMF7ZyqYziGip5qBBx10EfHPbZS2OziOoF_PCHXKtwUMAccFRdc9rNZsLl8gwQGsevf69hA8V_qz8tKVBHnRhuE909bOXrhnMED2cAeU9rn3NZ-4cYFRPaVpYEfZSKZMD6Qbv6jd3NR0MuRa2i9uGJ3uXPHjiqTYdr6Fg_hGA5LoA9FVc8oNtdiYspg-DOyQbgOqkdMp5bvy8t5H3Wanucjzx6i4TgSbG0prw0jmliLZqrLNX9ODBfa6pfTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس جمهور در توسعه روستایی و مناطق محروم: در سال گذشته ۶ هزار میلیارد تومان سرمایه‌گذاری برای محرومیت‌زدایی داشتیم  @Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/459996" target="_blank">📅 22:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a94cd510ec.mp4?token=CAECejRDyYabtKKfZw-yyj5ge17gJpYd1SrCEqPpPIsuL3AzsWp4HF9k95cfxzPfxovlu-xXJPjtQbixdvEqJT4nt1_edP9hA-H828Fm8L2i8gL9xmQ9_m0BsZYbcIh1hSCsNVGHPsRW1I_drYbzmtyUoLJsJtfH6IwVj39BGJhoN85VnbqYh7LDEy5dI-mUoD-J_IG485fzK8R96LOrmBCFOBJO2YTKU9DvAUoLWNGNIzdKH1EEbEx90D_E1U-3w5jJWb4LJY85sR9zq0pHLWLNnyoDlY13O9WP7_-k2inHb6cKpS0G9bIcqqLbfEap5l69AZhYH4bSzyYF7-28XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a94cd510ec.mp4?token=CAECejRDyYabtKKfZw-yyj5ge17gJpYd1SrCEqPpPIsuL3AzsWp4HF9k95cfxzPfxovlu-xXJPjtQbixdvEqJT4nt1_edP9hA-H828Fm8L2i8gL9xmQ9_m0BsZYbcIh1hSCsNVGHPsRW1I_drYbzmtyUoLJsJtfH6IwVj39BGJhoN85VnbqYh7LDEy5dI-mUoD-J_IG485fzK8R96LOrmBCFOBJO2YTKU9DvAUoLWNGNIzdKH1EEbEx90D_E1U-3w5jJWb4LJY85sR9zq0pHLWLNnyoDlY13O9WP7_-k2inHb6cKpS0G9bIcqqLbfEap5l69AZhYH4bSzyYF7-28XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون رئیس جمهور در توسعه روستایی و مناطق محروم: در سال گذشته ۶ هزار میلیارد تومان سرمایه‌گذاری برای محرومیت‌زدایی داشتیم
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/459995" target="_blank">📅 22:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8792f237.mp4?token=byAkClhMXxKqB167wp_XMfF0O10frV96EzHna-E_Ti2Expi9RgBnoXdNBDmLL6Yf8CTMKHA8cWod4Kb8mQ6UGE-HgBlO4o5jX9nfTpdP-UPoR7UTZXTttXuNCehsEB3LLL_2prq1faVzQf91CBZnN9AH7Qcb9430jngrdSd2Zzr20XiHlkP-1JduH-_yffRMwkn0mLAn4F8FYlpR8vMguRyU85thGSnV0Pv0Itu7J-b0-ugQVxwmv3O9oWahaOVexo7Ipj1uRaEJSRizFaJbrZYhS5Dls_dCZWxukza17gHh8EVXuGsIc3vbTst6LymZg0jjHUNMtRxzcJW4BDK0iyBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8792f237.mp4?token=byAkClhMXxKqB167wp_XMfF0O10frV96EzHna-E_Ti2Expi9RgBnoXdNBDmLL6Yf8CTMKHA8cWod4Kb8mQ6UGE-HgBlO4o5jX9nfTpdP-UPoR7UTZXTttXuNCehsEB3LLL_2prq1faVzQf91CBZnN9AH7Qcb9430jngrdSd2Zzr20XiHlkP-1JduH-_yffRMwkn0mLAn4F8FYlpR8vMguRyU85thGSnV0Pv0Itu7J-b0-ugQVxwmv3O9oWahaOVexo7Ipj1uRaEJSRizFaJbrZYhS5Dls_dCZWxukza17gHh8EVXuGsIc3vbTst6LymZg0jjHUNMtRxzcJW4BDK0iyBBcoKy7X4eeWXRnXaZ4hgPhljykgGRzqrz35CjfgIL36Pt-Rai-yxdJTIRLnJHaIcqtDQZg_xK5tWuQQ4p61qCnb7SH6Dky8tFHnzvBHmM1qMOOHnNsLSVmupEpUbuVf2tQQ_g4wfM8yJNug9ZJtQim_0bEZJjzz9qU2gjb4j3wjoWONaikmtDmlsiY7IBuppfOVfQEKJji6fRsorBWe1YiRCufuzVFDY2OFwqGrb_zkgVu04cGX8gADf2iteO-qLwvrdn25NQDJ9SUjesf1h27mAzt8gC2i28XaonUPIymOCJ-QDNNRuZA208Q1ntCbvCMG1ckR4Lkdbi6Qqfbek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض به سبک معاون ترامپ؛ ونس: غیرنظامیان را هدف نمی‌گیریم، اما گاهی اتفاق می‌افتد!
🔹
ونس، معاون ترامپ، در پاسخ به خبرنگاری دربارهٔ حملهٔ آمریکا به یک مراسم عروسی در جنوب ایران و کشتار غیرنظامیان گفت: «ایالات متحده ۱۰۰٪ برخلاف ایران هرگز غیرنظامیان را هدف…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459994" target="_blank">📅 22:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459993">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaKNWUXNGkT3Y_ywk4CSCuP0Fz11qrXRhUFyOxj4KSyOt8ggpX71gfysZ7WSz5aKkWh3-XThCDHAWsX_w62jTFu8rJkDV6dB3ZVntSQh_r1KLo1B3he9AZfsM1I3yaPv4wpNXMmpU62Z-ZTU_nUV9hiJ6yE3cF85Qh1HjpFAjvT87DV1KObA2olqctWHLOLt_dsB_vJjkHtRRCOR-lgRQSLO_2fQ1w4K_sM5bk_i4xs9fXUGiU4mchdGXBHdr-5r9_nu3mEu4RtO4SxK1XNnArQTJ2mLxXAqMx662ba9hCNgVFrv4-5Rl1VsQSoky3yDqqQzVaFW6aJxtHRhuquogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش شورای عالی مدارس اهل سنت جنوب ایران به حادثهٔ کوهستک
🔹
شیخ یوسف جمالی، رئیس شورای عالی مدارس اهل سنت و جماعت جنوب ایران و امام جمعه اهل سنت و جماعت بندرعباس در پی حادثه خونین کوهستک، با صدور پیامی این حادثه را محکوم کرد.
🔹
در این پیام با استناد به آیه شریفه «وَلَا تَحْسَبَنَّ اللَّهَ غَافِلًا عَمَّا يَعْمَلُ الظَّالِمُونَ» آمده است: مرگ بخشی از حقیقت و معنای زندگی است، اما گرفتن جان انسان‌های بی‌گناه و نابود کردن حیات آدمی، جنایتی نابخشودنی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459993" target="_blank">📅 22:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044bd12ec8.mp4?token=HKggrx7F3V5z3Ila0YGtdKgPSfGLpSSo8-i5tkDMzVtSEyV21S71IsblGX_o3DSuWME4BnPccZ9IoTSb8knydsfd4f5pLJIu7NtM0QW0gzGSF5oKjGPzAdCWQyS05fDTeVbA6iIOhVNjt0wT2DlSzaKNgiB9VnwiSvs0a1iff0D_So9VCQwJwq0TiHkv-m7GVB9nZNK6uZjKNE_RJerr7cqxrPaCD4GAhS9DFsKTrZkS7UoAjkxRQgwKXtA1iZjC-ix2vndyWUXIvm9v3meVGcCO2mqX6CaBW-VgtnRq_9mcv_qQK5poNcx-0-34645NzbLOhS6dVLqvJZmtT9hrwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044bd12ec8.mp4?token=HKggrx7F3V5z3Ila0YGtdKgPSfGLpSSo8-i5tkDMzVtSEyV21S71IsblGX_o3DSuWME4BnPccZ9IoTSb8knydsfd4f5pLJIu7NtM0QW0gzGSF5oKjGPzAdCWQyS05fDTeVbA6iIOhVNjt0wT2DlSzaKNgiB9VnwiSvs0a1iff0D_So9VCQwJwq0TiHkv-m7GVB9nZNK6uZjKNE_RJerr7cqxrPaCD4GAhS9DFsKTrZkS7UoAjkxRQgwKXtA1iZjC-ix2vndyWUXIvm9v3meVGcCO2mqX6CaBW-VgtnRq_9mcv_qQK5poNcx-0-34645NzbLOhS6dVLqvJZmtT9hrwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های ایران ۱۸۷ شب با حضور شما مردم زنده است
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459991" target="_blank">📅 22:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459990">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8lUp9vUpD8Ng-SLtSu-XM2gKKi9KwtYzQuwqG0G9BSNi23JvzN4xYe2pSFkGVSmOVNz-mymA3ME4Mfg5ej_8NpVaLIi0_cJkxZqtdYZ-Vo5iVatkpGXHhBGxPAGltlYVTerzkc-Ghgo4oFjwwel3b-ggEPV_-tcBOtfi2gboL7hgEA7dtelytpLvYUTc4g8eAnC_3KPN7yZdUpkVGtvly6N6X6M-4cfOXEVg4NAfCSxBD2qm8ahWZMWdonP_izTjbo4gBDpnjk5JO1FUMIrclnruFK9Z2CGcsxQX94kZZbdID9OYyZbg7fo9LUId_SFHRhopd9x0nRKp7HuqtP-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه قضاییه: ایران در راستای اهداف مقدس خود به آمریکای جهان‌خوار با صدای رسا «نه» می‌گوید
🔹
حجت‌الاسلام اژه‌ای:  ایران در راستای اهداف مقدس خود برای آزادی انسان‌ها و انسانیت از یوغ استکبار، همچنان مجاهدت می‌کند و به آمریکای جهان‌خوار با صدای رسا «نه» می‌گوید.
🔹
ایران با آموزه‌هایی که از قرآن کریم و از پیامبر عظیم‌الشأن اسلام، اسوه عدالت و فضائل اخلاقی، آموخته است، به هیچ وجه زیر بار ظلم و زور نرفته و نخواهد رفت.
🔹
در جریان تجاوز ددمنشانه آمریکا و رژیم صهیونیستی به ایران اسلامی، کودکان بسیاری در یک مدرسه هدف حمله قرار گرفتند و به شهادت رسیدند؛ این کودکان معصوم در این تجاوز وحشیانه ارباً اربا شدند.
🔹
حمله به مدرسهٔ شجرهٔ طیبهٔ میناب، یک جنایت جنگی آشکار بود؛ کارشناسان سازمان ملل نیز این مدرسه را یک مرکز آموزشی غیرنظامی توصیف کرده و خواستار بررسی مستقل حمله شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/459990" target="_blank">📅 22:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459985">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1BxekpLBjBf6gLCRSMasolKpgcRe_OGwypFAjdiJRUMmwE--MyWQo1coGCX4mcME-Ops9JuwgDbbFmRhUubNmmXuUsg0pwNdCNRQABdcXTh3Yw9rJYILb32FPsAT8VkuZ6Y7G8s7oQW5jlGK_VA6oixUCHe3G137_KNmOjOTK7pi4fsmiTe_DKzmnJFfurmZKPL6jN7aSqyY6oBx5VYf6NWHvpDkCT6L3A2utm0gaxFhjJgROxtGn9VpfxhZ1aATcN3N5_xNS9ALZYzDQnnGYWs881ITd-G7vYRJitJWQW7ACeUAMLF2FRyu2vKvE7LbF7EbLmJPaCt-RM0JyitpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0_udPkpATy83AejEXJFuOsZFy7EqmKKIuXs0Rv6_LXoHzhgWkrbyPTrfDNkfUjlyubmrRznF35eKtKMpReu5ZDqgw7WsN5meh49KttjPnVLH0HmoCUinhSeLVWbhUvrujAV4mo5KRvWhv4h-axnbR1TmxOAwlLUZK4OU6IOz0qCe1_uqAL08exOrF4bmBBu5t73y5M2bfXwr778MytrjGOxVHz7Pc0oKEINQoFwkYArJy4kZrtmT5icGgEGjyUKFuKc6384seEn_akevW_EKVTi4_dEPCt8udhpxwP3h-mKPdtC-DeIljAeIJpRDZCaLDAl6KQCR53LaZZuHmS_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUHWFHUHlAjrUVAqNjNK9GEjy9Ig7krOFCZruEc7rdOr52t_0ldM_ZmnWbhE9CWG3zNnnBKyjMY4_y4A_E_dsFu8V_pTpjvuW1f_CdzGn_uqyOqBx-0XITpNnPnSnkEYNcTOPjB-iO2LYisretvVhHV2U_CiQGBNP-ZkWsJZA-ktbwZlZggRnebovcIOCeQqr745fQmdtxSQP1YdpDDN1YkshFS24FUMAFEI2WusoqB1eN8VTmqBMiRSMWI13gKoygK70uL7ks0C_pqHA4tzLVAonDTBJtFKuUg2q4DZuQFcMmCMU8UNilZHxt7GntG4pDmx2U6nWQ3YutCZmZW9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYfu55HlZK4oL7n3-v3WXmeJyLqZkkT3TNw6VMTTxVvSb2H-qqjBpAXO6JieR5nCbYaoMz9QrNBRCTX3getf6fKfC7SOeg35v6t_wYhs7h6TXy9d1P25-61atQvSdRcdcUq6SMS_fiHBNOgIwrSq0HlKya_PEipzsyRalg5vxmt64mZEKXvYGrPBF7UvZimmLhSyC5Zd0Eja5TkMUXTgsWTg4NBqzjuw_JzBvUukGQkW2ACCBB4Ff5EF2VtMiuy0o8hWExx9YUbBczhbUuqG7ycN0U2qNzl_SAeSXdkiw0qsAAJ4DL_Z8RMYRC3dUEJBWKAS9YtawD93XxtyPEecoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6h0dHKUHDFdhOzoGD-6C6aBkc_k7uwXsCUsM9cTKYaa9_JANgQDw7RFgWvzxGnkIxnlvs-sojnNUYvXIt0hnbQIXYiuP51Ak4DpHY0gXNCUDTCwA_uK7BGo-EaYuRscbUI7cy4K0j7chWrX7c-mY2seeBN2eGDLz67JGTlbV7RHpGlmhuhDk9y8HNHoC5k35kryBfH6ZysZLQPhff5_xdjmtoDbXUMob7IBHp-iO7LzcI4OHkBoGtWVKYi4PVM0AYM4yriY1l-QbvWXkF7bHeYJH2V8A0Hmatpo5Bmfit3V5R3WedyV_0biA3ikvcdqosgu94eXt6nRPkWzN2pcxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
تشییع با شکوه شهدای حملهٔ آمریکا به سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459985" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459984">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e3c94760.mp4?token=RAIKtmqgFj4tbMH0GtCWzd-LZjcdnQf_cgW3R_nx5RZBImCH5g0iMeCr2LNslfLto0YkHSOEmYdfOkMg63IUOyhlldqOcfP2WGiBk8JtkFqq5KhU3bbB5Xz3EnTT0rYCgHlYstXqtBQxDV3AimecXVEsE0sKwGqmMt5g2cF2BozaioBKYGat2kMKWdfuPZe4kKWD-AyZa4TZ3pAB_azD0TbbR5kaDzg-uEFYd-gXWLVvEV8YiPKHDp9rYGKW0aXglxagjb6lTX3prE74AUm-RunI1VrCMT_aDVsrCG46lTmHY-D9pjNL3E61OCiYYzy0T1dfrXqT8iagHsEdjqusQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e3c94760.mp4?token=RAIKtmqgFj4tbMH0GtCWzd-LZjcdnQf_cgW3R_nx5RZBImCH5g0iMeCr2LNslfLto0YkHSOEmYdfOkMg63IUOyhlldqOcfP2WGiBk8JtkFqq5KhU3bbB5Xz3EnTT0rYCgHlYstXqtBQxDV3AimecXVEsE0sKwGqmMt5g2cF2BozaioBKYGat2kMKWdfuPZe4kKWD-AyZa4TZ3pAB_azD0TbbR5kaDzg-uEFYd-gXWLVvEV8YiPKHDp9rYGKW0aXglxagjb6lTX3prE74AUm-RunI1VrCMT_aDVsrCG46lTmHY-D9pjNL3E61OCiYYzy0T1dfrXqT8iagHsEdjqusQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض به سبک معاون ترامپ؛ ونس: غیرنظامیان را هدف نمی‌گیریم، اما گاهی اتفاق می‌افتد!
🔹
ونس، معاون ترامپ، در پاسخ به خبرنگاری دربارهٔ حملهٔ آمریکا به یک مراسم عروسی در جنوب ایران و کشتار غیرنظامیان گفت: «ایالات متحده ۱۰۰٪ برخلاف ایران هرگز غیرنظامیان را هدف قرار نمی‌دهد»، اما او در جمله بعدی اعتراف کرد: «اما متأسفانه گاهی چنین حوادثی رخ می‌دهد!»
🔹
او ادعا کرد که نظامیان آمریکایی «وقتی اشتباهی می‌کنند از آن درس می‌گیرند تا بهتر شوند.» اما خودش را به فراموشی زده و نمی‌گوید که آمریکایی‌ها همین چند ماه پیش، در حمله به مدرسه «شجره طیبه» در میناب بیش از ۱۵۰ دانش‌آموز و معلم بی‌گناه را به خاک و خون کشیدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/459984" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459983">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b54dc7ca5e.mp4?token=SHxqX4BLa2ufZSaC4vEEt4T7pgOz5mIn-culwYRrCpvZV1KLukNn7aHqzPLXwvgGuYj5PrBdcxEzrN1o0ic44G8VsRwRi5_5K4RYGigat1Jyz3lYujxMsEGai4cyUoFB8OhLW-sP7rU4cKjb8KfPntekdsoHbnTMtj_gOBgOY7RyPsi288FBZun9VdZkJYkL0yhGb4LXzNeYmUV8-F7pSJl-7RdurheohzsRFlYFtFrdW-kvCGfqOsvIDxqhSUiGAvOrhnj0gPojxLdoyyQUJqXAnv6DOn3OG2Lq2SiYXDKtE238uzb2eo6EmjVLxYAWcM2aIHk1tuJ5_LF-VRlhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b54dc7ca5e.mp4?token=SHxqX4BLa2ufZSaC4vEEt4T7pgOz5mIn-culwYRrCpvZV1KLukNn7aHqzPLXwvgGuYj5PrBdcxEzrN1o0ic44G8VsRwRi5_5K4RYGigat1Jyz3lYujxMsEGai4cyUoFB8OhLW-sP7rU4cKjb8KfPntekdsoHbnTMtj_gOBgOY7RyPsi288FBZun9VdZkJYkL0yhGb4LXzNeYmUV8-F7pSJl-7RdurheohzsRFlYFtFrdW-kvCGfqOsvIDxqhSUiGAvOrhnj0gPojxLdoyyQUJqXAnv6DOn3OG2Lq2SiYXDKtE238uzb2eo6EmjVLxYAWcM2aIHk1tuJ5_LF-VRlhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار بود ۳ روز جشن و شادی باشد؛ اما...
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/459983" target="_blank">📅 21:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459982">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
مردم ولایتمدار بافق یزد: پای آرمان‌ها و ایران تا پای جان می‌ایستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/459982" target="_blank">📅 21:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mdw1j_2D6RgpUdAmcVGXW6bIb0enCH6Jl1OqJ9GgmuMLEdSwjrZwR7PlvCIvt6OFTs6JadGTogucoIw2ANsgcSOvLRQLLPMpVS4OTCW8nNb5xMMJG9pMPTXiG46Rv71yV1zDPUbuiEfV9SEo_f4j491sGiw92eZLvb7mWwKrZ4UbyvNJ3a1XE7Ij-i8-NXbQh8vrRkz93AhenoaZ_6TjUn3VEMY4wSBdVEyImg1e-mIDGq5dptEPKPS06epXqhXAxcufkuHDL-Bhxvz6HnaHHC2aOH6ffksj2BAvl0EIrekHzRIVUGpkTAp3170C7H9vxtOuJqQwzbXZLMtg_9ZODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMvmKCPkMaVrGGUP6QoNmrUdRnE6XzAY4e-Nr4s2tJ3_blLU16ZZS0QtK5KJfm-O0FA8jw9GHWYZYKURqirkKULxhCemaYuAYnbGTjkqFqzgdJ1PBGaklp_SxwT-LPfJyOcPjj3wXUK2--1JWHMj4jsi6aPDYwd-6yfTSrxejtw06Iwv9_VWSKyoE4uaenCFwhTbUHigSiGZBclm9hRkODLhI96HoipOYn0LYIy2K2jg0TmLt0uFCjRcBZnl4w3bmdIc52mOX5TLXKfp1UV6wFj6wAf3nc57mJLYAL9lgiqu_ST8Dex1sjNiUkn8SA_DTUxjLfZdQna4fy29zG65cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnRWN41sritCIuqW993PqOrTbPFb2KOIoyVCa77Bjz7l_eMoOCxqwGX982CKK00JbJtRoZVAUVNBEcCNkV7_5Xo_99YA8PWAFZhTFqWLZwySyXleWvTmzhyK1OhlUw5ggBIrJTjjAk_793BoZC40B3WI87yPMxAS5PO7FizJB49OivdIJs8CndQD4p4l_8h1USEvdDdepLifW7eRW0AX0OhdinmQqqe_5QvCb3Q_0ZXYXG_2gpzp4qA0wbepErqQ8zQi7BIQaBlQKXwYywVOzagtMxAIeiaUUBOZi1eJT0HPTMAz1yy3vqZaOqqBX0loZ-Xyrcc3C-Hayc-x_e_4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S07ZQ9jm560T2-caCUValqmKVI4mANuw1fh-Yx1PNp9IJ1dnyRUBnzb5n-FrPTDqMaG4RynsZ_ZVqAVx_kWR2B5T95-PMdoHsexLZUG_BWjEaSwVOgQlm5A1mm9H7-tFP0PWwcQhoxBphopLTGuOPw6nJ3utWwNF3GBJN6dbfryOM9VzjzDn4aKjiSqpXnJalxgQfBCym2f-MZhL-T5uxhBEOT0OH5UWlIF9HbU3QoBOJEYClqC93fgFurycHeqpLuyWTAQ0r5lRM1Y7MGfLxDpDfYgj3KsDoz1UpVBwnr8WG85A0pGBZOvjEHTcai4O88nxmfSlMbhvVLc0PR6z6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک تایمز: موشک آمریکایی عروسی ایرانی را به خاک و خون کشید
🔹
روزنامه نیویورک تایمز در گزارش تحقیقاتی خود با بررسی ویدئوها و مصاحبه با افراد محلی، نوشت که آمریکا در حمله به جشن عروسی کوهستک از موشک‌های JSOW استفاده کرده است.
🔹
این روزنامه با استناد به نظر یک کارشناس تسلیحات و همچنین تحلیل‌های بصری خود نوشت موشکی که به یک منطقه مسکونی اصابت کرده، ساخت آمریکا بوده است. این حمله به شهادت ۵ نفر و زخمی شدن ۶۷ نفر دیگر منجر شده است.
🔹
«ترور بال» به نیویورک تایمز گفته است که بقایای موشک اصابت کرده در جشن عروسی متعلق به یک بمب سُرِشی است؛ نوعی مهمات که فرماندهی مرکزی آمریکا (سنتکام) از آن استفاده می‌کند، اما نیروهای مسلح ایران از چنین تسلیحاتی استفاده نمی‌کنند.
🔸
نیویورک تایمز در بخش دیگری از گزارش خود نوشت که حمله به کوهستک چهارمین حادثه‌ای است که این روزنامه آن را مستند کرده و در آن تأسیسات فاقد کاربری نظامی هدف حملات آمریکا قرار گرفته و غیرنظامیان کشته شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/459978" target="_blank">📅 21:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459977">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
حملات صهیونیست‌ها به جنوب لبنان ادامه دارد
🔹
شبکه المنار: ارتش رژیم صهیونیستی اطراف ارتفاعات راهبردی علی‌الطاهر را هدف حملات هوایی و توپخانه‌ای قرار داد.
🔹
همچنین جنگنده‌های این رژیم بار دیگر شهرک النبطیه الفوقا و شهرک حاریص در جنوب لبنان را بمباران کردند.…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/459977" target="_blank">📅 21:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459976">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy3HjY6tQO1IYzBwSq4ofAB_LGVU54vnA_cvOpR0Nk8oRcbjM_27XK3NIdRht7oyXAUlUMCpuxXaYE_4CI5kQGlLBDAYBBMLrlQZ1bh0pqYRKaOkUpKhQWsB7VitaXvuTOaXiD1FHZM0me5ERdGIGSNAuvZLp-AiQKRKxUrICWpmimieFpId01k4GTOoJ1ZgtHiFj_d6K8jxajvSlT4I1MuHbv9IFsj-EmosrdH0Hm_51wPIlpmdxbTHBD4xMLJHe1Hi2_ohL-FnEVhEEiPOmMrVQ8dOeUx5obiWcsahL28uppMB2Zju8Du9oo-2elsa3rB0EeVHp8Rwoug6-1jXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو ارشد کنگره: جنگ علیه ایران به شکست انجامید
🔹
رهبر دموکرات‌ها در مجلس نمایندگان آمریکا: ترامپ متعهد شد که هزینه‌ها را از روز اول کاهش دهد، اما تحت حکومت دونالد ترامپ و جمهوری‌خواهان، هزینه‌ها در ایالات متحده آمریکا پایین نیامده است. بلکه بالا رفته است.
🔹
وقتی افراد در مناصب بالا این‌قدر بر پولدار کردن خود، اعضای خانواده و حامیان خود متمرکز باشند، این یعنی به بهبود زندگی مردم عادی آمریکا توجهی ندارند
🔹
تصمیماتی که گرفته شده، مانند این جنگ بی‌ملاحظه و پرهزینه در ایران، شکست خورده است و زمان تغییر اساسی فرا رسیده است.
🔸
تاکنون چندین عضو کنگره از تجاوز نظامی علیه ایران انتقاد کرده‌اند. قانون‌گذاران با اشاره به افزایش قیمت سوخت و هزینه‌های زندگی در آمریکا، درباره احتمال تداوم درگیری‌ها هشدار داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/459976" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdab2cd697.mp4?token=j5jr5gGdrZorVYSy6Oyte7udIGgVI-NdVfe3DgzAB9JhtPMtVk0krJb-HlVsajEyY-jZd7u7tHpWbwDZuPBXyPA72N1PV5Xre-eBfl5gt9icDtkSJ7148D2G5d53X-UeZW6xOta7d1R3pkWcpkihOJQnEZs7D14lhxQLVlhq-mHeXUFIHS2R8uvt8dZOeiXKel3l7-_EMGMGhHOhob0Y-bcxuZTM9X2PHib9PUxlkq-KAaKiWmIDj0DEDpVmkV04AU7xzejEkAw9ft1vjvR8pDICvqZD2ABqeh5PposXpcpQGjH9f3Db9yRvazAUWLDMWfuO7SIoi4KVh_NpO5jCcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdab2cd697.mp4?token=j5jr5gGdrZorVYSy6Oyte7udIGgVI-NdVfe3DgzAB9JhtPMtVk0krJb-HlVsajEyY-jZd7u7tHpWbwDZuPBXyPA72N1PV5Xre-eBfl5gt9icDtkSJ7148D2G5d53X-UeZW6xOta7d1R3pkWcpkihOJQnEZs7D14lhxQLVlhq-mHeXUFIHS2R8uvt8dZOeiXKel3l7-_EMGMGhHOhob0Y-bcxuZTM9X2PHib9PUxlkq-KAaKiWmIDj0DEDpVmkV04AU7xzejEkAw9ft1vjvR8pDICvqZD2ABqeh5PposXpcpQGjH9f3Db9yRvazAUWLDMWfuO7SIoi4KVh_NpO5jCcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
رئیس قوه‌قضائیه با پرواز «میناب ۱۶۸» به هند رفت.  @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/459975" target="_blank">📅 21:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb4fefb46.mp4?token=mmhfuJJ9uIuy_wphRF6dMvGfFIe5c10bPwTUdl8ZQyJKCHqgvdzTqi-fbuCH-m7xamKeF-KJWtqV4qTFXEykhtpWX_1SZWkOIiK8Zz7-mW9AMrZPuz5y5CeRTYjsKQTy4zLUrVtDZ9O-cZcP8l4A7Vbvq3NRroINCv7nAqLTOZJpcJGOnzFtw1TApIb8jxyA3RT4N8S4HPYGwZJW9UJc-V553fCqxqfbzTpPXk_F6PEd95b146AUX-EvXiDt0MT4jEAOiypdp_xS87W1cx42kH6rkxIaLwrQ49dN-0A96A4QoTmBAcgz369Tc7eglFgJH_ZI-T3IfHfDGSedcoABTQKHumTwgPZ-K4CpHclPzpyyf8UUgNISfl0W8uelyZoYC2OF18hBd6ksKhj8Sd1Vtm7KndVYxSSnnahygYmAn4-mbuf-REHo4uMjRYwhSQX30tB0gBRbD3LZ8ex3mTsH3sJ_28nPA3k1caKmpar-VnAHCN0fRN6EWh_zlPg4CDODcx5VUadcVeeXNbclOLkxNVF0cLePfMLVbZzlV5ZQGDdDl_uaJFG0BSF3EACYzCkjveMjAKr-a2wGxqYOsrpk7QfyzDETpS_UoBNjZzy02PQ-kT-hIhozNjaxZuo15Fpx3gKdFz5X5R1jJoKX3PT_dkz_5QQwV7pobrZrdpU12yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb4fefb46.mp4?token=mmhfuJJ9uIuy_wphRF6dMvGfFIe5c10bPwTUdl8ZQyJKCHqgvdzTqi-fbuCH-m7xamKeF-KJWtqV4qTFXEykhtpWX_1SZWkOIiK8Zz7-mW9AMrZPuz5y5CeRTYjsKQTy4zLUrVtDZ9O-cZcP8l4A7Vbvq3NRroINCv7nAqLTOZJpcJGOnzFtw1TApIb8jxyA3RT4N8S4HPYGwZJW9UJc-V553fCqxqfbzTpPXk_F6PEd95b146AUX-EvXiDt0MT4jEAOiypdp_xS87W1cx42kH6rkxIaLwrQ49dN-0A96A4QoTmBAcgz369Tc7eglFgJH_ZI-T3IfHfDGSedcoABTQKHumTwgPZ-K4CpHclPzpyyf8UUgNISfl0W8uelyZoYC2OF18hBd6ksKhj8Sd1Vtm7KndVYxSSnnahygYmAn4-mbuf-REHo4uMjRYwhSQX30tB0gBRbD3LZ8ex3mTsH3sJ_28nPA3k1caKmpar-VnAHCN0fRN6EWh_zlPg4CDODcx5VUadcVeeXNbclOLkxNVF0cLePfMLVbZzlV5ZQGDdDl_uaJFG0BSF3EACYzCkjveMjAKr-a2wGxqYOsrpk7QfyzDETpS_UoBNjZzy02PQ-kT-hIhozNjaxZuo15Fpx3gKdFz5X5R1jJoKX3PT_dkz_5QQwV7pobrZrdpU12yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدارهای صمیمانهٔ خانواده‌های معظم شهدا با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/459974" target="_blank">📅 21:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حملهٔ هوایی صهیونیست‌ها به ارتفاعات علی الطاهر لبنان
🔹
رسانه‌های لبنانی از حملهٔ هوایی رژیم صهیونیستی به ارتفاعات علی الطاهر که مشرف به شهر مهم النبطیه است، خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/459973" target="_blank">📅 21:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1896b0bc.mp4?token=PaPjLS6lyeF6ShzFkRr9XD4ZubyTK_4vQaoUIw5g3bxmgGs9OIFOVJxiLDIHwq7K7ICKqUuI-44U0lY0zkqve7JIglA5ik8qJEP7M7Yd-Mylby8EZhRcIlJ0ZyiScSkAgqy1tq4QcUCj-p6LZtLYAIhpaMSkTbcbYuDDFt2xXAEb8bdqwpJb9K6n7JpTZSd19TyHtAF-LccOAsPR3u_eZmIPbA9MK4RXDu1WT2LPqST28e-Hd0FRdrIKSKklPGjK4tcyx5kDSRK4ZHibV6ga1k9HFpx5O4fSyeaRGBolKD9xa459umEY55i025L6uJkqAwpWupP8-ada5bvPerr0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1896b0bc.mp4?token=PaPjLS6lyeF6ShzFkRr9XD4ZubyTK_4vQaoUIw5g3bxmgGs9OIFOVJxiLDIHwq7K7ICKqUuI-44U0lY0zkqve7JIglA5ik8qJEP7M7Yd-Mylby8EZhRcIlJ0ZyiScSkAgqy1tq4QcUCj-p6LZtLYAIhpaMSkTbcbYuDDFt2xXAEb8bdqwpJb9K6n7JpTZSd19TyHtAF-LccOAsPR3u_eZmIPbA9MK4RXDu1WT2LPqST28e-Hd0FRdrIKSKklPGjK4tcyx5kDSRK4ZHibV6ga1k9HFpx5O4fSyeaRGBolKD9xa459umEY55i025L6uJkqAwpWupP8-ada5bvPerr0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه ذهن مردم گرفتار روایت‌های دروغ می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459972" target="_blank">📅 20:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459971">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2809a2027.mp4?token=duQprFcbTAO1eLwAJGrNPfcCJnBm-vwmox_Fc3_veIQ7uRwwQErneX1ytuU0IM1etbui4Pb5ggFUEmEXAyTMkw9joOl2W8oQvnySU6fzyWvZNDjMZafn3VOopm6N1bpwoHQgtNkwvePHQybLLWa-ju1cwU8K-Y-UG1S2OoD-0qmb2QDPtgLZyX9MGFlCEgOxxHkdgN75r9MWYSZjJIcfPHi4CYlACxQQ3nZAnbuEh_S1wgDblyo7HYvjywUeyktXshgh_JCOFnL76cx8C8RemNjSkKDrBA_D-dkgKdwT_95Da5lwC70KKXndPAGHSNL2MKJuIL3VaoqEZqnv5bJGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2809a2027.mp4?token=duQprFcbTAO1eLwAJGrNPfcCJnBm-vwmox_Fc3_veIQ7uRwwQErneX1ytuU0IM1etbui4Pb5ggFUEmEXAyTMkw9joOl2W8oQvnySU6fzyWvZNDjMZafn3VOopm6N1bpwoHQgtNkwvePHQybLLWa-ju1cwU8K-Y-UG1S2OoD-0qmb2QDPtgLZyX9MGFlCEgOxxHkdgN75r9MWYSZjJIcfPHi4CYlACxQQ3nZAnbuEh_S1wgDblyo7HYvjywUeyktXshgh_JCOFnL76cx8C8RemNjSkKDrBA_D-dkgKdwT_95Da5lwC70KKXndPAGHSNL2MKJuIL3VaoqEZqnv5bJGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: قرارداد بزرگ فشارافزایی میدان گازی پارس جنوبی در اسفند ۱۴۰۳ امضاء شد  @Farsns</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459971" target="_blank">📅 20:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35001b930c.mp4?token=LNhPJ4XTb19cnfGALeKhzAUAxLRr3Kze1rSzVxJD4dy5Uk_1YveE7myP8Dis9B-s0PcqKBG0GhpK79Xz50CwyzhzOLKKL-SGjYOUUr3FDlqi3smz8fk6m6UunqPhjOg2GsQMJdY44q94QpI48U45wWWdDMeaWMi96jj3wxS_a86Hz5lgCp-gjGhroYD1ixt0A-tSfAN7EdMCQozDgCDWwwQe0cPNof28P20WHR2WHsXDIWUxE_3H9liCTsOyGUly80mBSvd2zvhI8_6xAHsmBHKj8bpoz7Utb_B1HtpsNlGyJRIpCCpMQKjBH2afH_cUITa18wSrC7dks46QQXDweRDFCUcHZT0hEdJdE3FiJr5fn-9xSo43rirSGhyPk9gCyLLphTefP2eYP82uGU5tSdQ6xDyXHOHmraNADxgKAz3xzstvAXHl-21MhSUrViAMuKhtOF3H3uT7x2P_9SCWJD0LKu60VOHDtd61IcfPLE--1pKlcld2bl1kUPE0CiPOuOEFDN-HnDq30rmgMVrl_rGBEMKM2IApKH0X4bLxyiBEIiBr3HHHlzQk54ZDpo9Elnlrbc51Q2ZfNTLFBGhAV3IJpGVRVPW2Vr8GEkfaeARQ_eRDpqrwOiLn36B9HijHDUG_WnzEAIPR0FJLmbmn52CA3yL85ya4LDR2YjPwXk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35001b930c.mp4?token=LNhPJ4XTb19cnfGALeKhzAUAxLRr3Kze1rSzVxJD4dy5Uk_1YveE7myP8Dis9B-s0PcqKBG0GhpK79Xz50CwyzhzOLKKL-SGjYOUUr3FDlqi3smz8fk6m6UunqPhjOg2GsQMJdY44q94QpI48U45wWWdDMeaWMi96jj3wxS_a86Hz5lgCp-gjGhroYD1ixt0A-tSfAN7EdMCQozDgCDWwwQe0cPNof28P20WHR2WHsXDIWUxE_3H9liCTsOyGUly80mBSvd2zvhI8_6xAHsmBHKj8bpoz7Utb_B1HtpsNlGyJRIpCCpMQKjBH2afH_cUITa18wSrC7dks46QQXDweRDFCUcHZT0hEdJdE3FiJr5fn-9xSo43rirSGhyPk9gCyLLphTefP2eYP82uGU5tSdQ6xDyXHOHmraNADxgKAz3xzstvAXHl-21MhSUrViAMuKhtOF3H3uT7x2P_9SCWJD0LKu60VOHDtd61IcfPLE--1pKlcld2bl1kUPE0CiPOuOEFDN-HnDq30rmgMVrl_rGBEMKM2IApKH0X4bLxyiBEIiBr3HHHlzQk54ZDpo9Elnlrbc51Q2ZfNTLFBGhAV3IJpGVRVPW2Vr8GEkfaeARQ_eRDpqrwOiLn36B9HijHDUG_WnzEAIPR0FJLmbmn52CA3yL85ya4LDR2YjPwXk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم این‌گونه جواب گزافه‌گویی ترامپ را دادند
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/459970" target="_blank">📅 20:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3811f3d433.mp4?token=vfSMyf6tIqZmHCqHZOgFwFQbAkEpKyc7-KhMc41b-SIpy5n5qCBp9N5hf5yJsN8FEFutSFOPctniaWAfBk5gwqiPKVODTApyNIJi6jkKoWNgKSt-ef2yDHOZ5L4WFxY-U7XaosS0erjiTKYixP31GNYIFXhn0GJ3pgrULi_LTHNChqJeGjUUcHp783pNQba1J3TE8ME6X0B8lefabePUNVLTtnHIt22jlvLD08kSHPpvD4Xe_J8TeoLiUaqFoLOVIQgl6gi4yyWezIQDhuotbCV2kFKur3s-87KUwkPvCaCLaclKW4JDiR2FgmbDGhNoKMA6E14nt83xdmJDAdQwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3811f3d433.mp4?token=vfSMyf6tIqZmHCqHZOgFwFQbAkEpKyc7-KhMc41b-SIpy5n5qCBp9N5hf5yJsN8FEFutSFOPctniaWAfBk5gwqiPKVODTApyNIJi6jkKoWNgKSt-ef2yDHOZ5L4WFxY-U7XaosS0erjiTKYixP31GNYIFXhn0GJ3pgrULi_LTHNChqJeGjUUcHp783pNQba1J3TE8ME6X0B8lefabePUNVLTtnHIt22jlvLD08kSHPpvD4Xe_J8TeoLiUaqFoLOVIQgl6gi4yyWezIQDhuotbCV2kFKur3s-87KUwkPvCaCLaclKW4JDiR2FgmbDGhNoKMA6E14nt83xdmJDAdQwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: قرارداد بزرگ فشارافزایی میدان گازی پارس جنوبی در اسفند ۱۴۰۳ امضاء شد
@Farsns</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/459969" target="_blank">📅 20:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f1a577ef0.mp4?token=l2nNuGIX3YAy1BXG64PhgZvUssrVIu3nEijP0XOCci0L2S4i-PNuUK2myU-M8Se-hOeekqW7pP3no93whOJdKTak3WWkazLJ5p_wKvP11eYcSRxCaw7ULclTCNnBu0RMEG1oI2e7MkXYUGRvOQUh0-yf2_CODWW9QE7vlVuLGcYBgTATbo-JJxqR1l32YpTEQJMeMWBcz7K6MjeB0W8M7ITTPia7vwzQdB32D0n7tzQOBl2olqV22orGSjchunyCo02IfZ8s3uPWfW-SOIA1Q_5q-Mtypb9jc4teKRtwGV9EKlGPrDVscWLMVTB3sfukhY-JGQz4oRlnNjskJzkGtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f1a577ef0.mp4?token=l2nNuGIX3YAy1BXG64PhgZvUssrVIu3nEijP0XOCci0L2S4i-PNuUK2myU-M8Se-hOeekqW7pP3no93whOJdKTak3WWkazLJ5p_wKvP11eYcSRxCaw7ULclTCNnBu0RMEG1oI2e7MkXYUGRvOQUh0-yf2_CODWW9QE7vlVuLGcYBgTATbo-JJxqR1l32YpTEQJMeMWBcz7K6MjeB0W8M7ITTPia7vwzQdB32D0n7tzQOBl2olqV22orGSjchunyCo02IfZ8s3uPWfW-SOIA1Q_5q-Mtypb9jc4teKRtwGV9EKlGPrDVscWLMVTB3sfukhY-JGQz4oRlnNjskJzkGtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناکامی سامانه هوایی آمریکا مقابل پهپادهای ارتش ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/459968" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaetN9tGt3OWEJV8ETjL57RxKnaeqJKSXnlg74W85H6J7U_HpHH8ELHp-aXsfVPWMYJ9yZ0DhTPyTSgwGKnYvw6YmxrM2PQpX6tMGVBYXlPK6fP2cZEiDoII9j7VYcCtZDWgG0zpFmy6C-cybDk2SyRjEWk0FhBV45T-bcyb-TbToE7ajTJEQLDrB9HfugOpw4c9sIIFogKQJ4F0gqGR2KE4O76B7nl0OyQJKTUBjKyiRQg9AdEplQr4vK7PJBKWpO2pQDdiuG7II5xzRPbgJuifMVuKMpWob8oww5mwcLckDlARUjZleVCofbjF5oQnQdZA1d_ywodxmtHNAkdCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف خطاب به بسنت وزیر خزانه‌داری آمریکا: کاهش سریع ذخایر استراتژیک، افزایش بی‌سابقهٔ نرخ بازده اوراق و جهش پرشتاب قیمت نفت آتی، بسنت را در لبهٔ پرتگاه قرار داده است
🔹
«قیمت نفت آتی عمان، بازده اوراق قرضه دولت امریکا و میزان ذخایر استراتژیک نفت را خوب تماشا کن.
قهرمان! هرچی زور داری بزن که در قیمت نفت آتی بیشتر مداخله کنی! چون کل حرفهٔ تو به این بستگی دارد. یا اینکه به تخلیه نفت از ذخایر استراتژیک بیشتر از حد خطرناک ادامه بده و سقوط غارهای نمکی ذخیرهٔ نفت در اثر کاهش شدید ذخایر را تماشا کن، یا به خداهای نمک تگزاس پناه ببر و دعا کن که چاه‌های ذخیره سقوط نکنند. دنیا پاپ کورن خریده و تو را تماشا می‌کند».
🔸
در توضیح این توییت رییس مجلس ذکر ۳ نکته ضروری است:
🔹
بسنت برای پایین آوردن بازدهی اوراق بلندمدت (به‌ویژه ۱۰ساله) دست به خریدهای بازخرید در بازار اوراق بدهی امریکا به امید کاهش هزینه استقراض پیش از انتخابات میان‌دوره روی آورده است. اما بازار تا حد زیادی در برابر این مداخلات مقاومت نشان داده و بازدهی‌ها بالا مانده یا حتی بالا رفته است. منتقدان (از جمله برخی چهره‌های قدیمی وال‌استریت مثل استنلی دراکن‌میلر) این اقدامات را ناکارآمد و بی‌اثر می‌دانند و بازار را در لبه پرتگاه ارزیابی میکنند.
🔹
به دلیل جنگ با ایران و اختلال در تنگهٔ هرمز، دولت ترامپ (از طریق وزارت انرژی) حجم عظیمی از نفت SPR از طریق تبادل اضطراری آزاد کرده است. سطح ذخایر به پایین‌ترین میزان از اوایل دهه ۱۹۸۰ رسیده (در برخی گزارش‌ها نزدیک یا زیر ۳۰۰ میلیون بشکه و حتی نزدیک به محدوده خطر قانونی حدود ۲۵۲ میلیون بشکه). ذخایر استراتژیک نفت در غارهای نمکی عظیم زیرزمینی در تگزاس و لوئیزیانا ذخیره می‌شود؛ یکی از مهم‌ترین سایت‌ها Bryan Mound در نزدیکی تگزاس است.
🔹
تخلیهٔ بیش از حد این غارها ریسک‌های ساختاری دارد: فشار هیدرولیکی، پایداری دیواره‌های نمکی، یکپارچگی چاه‌ها و امکان فروریختن یا آسیب دائمی به ظرفیت ذخیره‌سازی. گزارش‌های کارشناسی متعدد قبلاً به مسائل کیفیت کار، تغییر شکل چاه‌ها و ریسک در سایت‌هایی مثل Bryan Mound اشاره کرده‌اند.
🔹
برخی معامله‌گران نفت با سیگنال‌های بسنت به کاهشی بودن قیمت‌های آتی نفت امیدوار شده‌اند و این در حالی است که قیمت آتی نفت عمان و امارات که نشان دهنده انتظار بازار از وضعیت لاین موازی عبور از هرمز ارزیابی می شود، در روزهای گذشته از ۱۰۰ دلار هم عبور کرده است. آمریکا روی کاهش قیمت نفت آتی این کشورها در نتیجهٔ بازی‌های روانی و اطمینان دادن نسبت به بازگشایی لاین جنوبی هرمز حساب کرده بود. این انتظارات از قیمت آتی نفت، در کنار ته کشیدن ذخایر استراتژیک و افزایشی شدن نرخ بازده اوراق قرضه، وضعیتی بغرنج برای بسنت و دولت ترامپ ایجاد کرده است که تلاش می‌کنند با لفاظی در مورد ایران آن را لاپوشانی کنند اما شاخص‌ها شفاف‌تر و صریح‌تر سخن می‌گویند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/459967" target="_blank">📅 20:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459966">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqX4lad8L1b6sOQoG_pMHe0KGdYS_PIgwbLZ_LsiNhaFqxyvCv7a2fDi9s3Mw_TYZ-DRFtk9YcNLXdCEPnL3v5BGhfj3E5SvKdSFUtskSFHfsxEDCKVCpQZ92XOBwJanyfuVh3gXqU1QRn8BJhEvsV3b2wBw277g_9nopZynuYY7rp8Kp6XDhhMGZe598QSV0yUCRfbQ2fcR1Y_XcsmmM29JoepFqMrZlibTFkDf26BQfwkdcKYo-9Puw1kzfndukNYtPdY1b2iOKqSPGeVCSg9_jtMrJ9KikO1X1q7alebNq4HSTqv3L8niSR6zquqz9yrAggmMeWO0t62jcP0FZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعی بی‌سابقهٔ مدل‌های مشهور هوش‌مصنوعی در سطح جهان
🔹
گزارش‌های گسترده‌ای از اختلال در پلتفرم‌های بزرگ هوش مصنوعی دنیا منتشر شده است؛ چت‌جی‌پی‌تی، کلاود و گراک همگی با قطعی سراسری مواجه شده‌اند که کاربران را در وب، موبایل و دسکتاپ تحت تأثیر قرار داده است.
🔹
نکته جالب این است که این اتفاق درست همزمان با شایعات مربوط به رونمایی از مدل جدید اپن‌ای‌آی با نام «آسترا» رخ داده و کارشناسان حدس می‌زنند که دلیل این اختلالات، مشکلات زیرساختی در سرویس‌های ابری «مایکروسافت آژور» باشد که اکثر این سرویس‌ها از آن استفاده می‌کنند.
🔹
گزارش‌های کاربران در کشورهای مختلف از جمله بریتانیا، هند، فرانسه و بسیاری از نقاط آسیا و اروپا نشان داد که سرویس جمنای گوگل نیز با خطاهای پاسخ‌دهی، کندی شدید و مشکل در تولید محتوا دست‌ و پنجه نرم می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/459966" target="_blank">📅 20:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459964">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doo3Vg65GQabEauIvMcIvIJMIrWIaTtc0Ea9JTpA8kT8FGQmZfN7x9v1IvTXgtdYkSUmGEMKP_Z1IO84tXlXYH7RNVz94xXbnnj4xUIGNIgPoP5kc-hQ-BrySb8zVg5pbFM3LUQFHlPAsklyS_Ss_Bc11aDMAehoQP8WfRDTXHOuDKSe82_4uYjbqI3i4PuwOQfDWgMdX9V5fiR_l_AkzNyedm6YHxUpyM4jx8yvDhbgQIbchkAHLqsAr0V0xAjDOlbkhaoDBZz-hPB4XgqxtEFzLdTjzmlV199bvYpzJ3xbVhGlbnN37lGlkJKDPBRt-6UNOa00w-BzDltRFgozuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g66Lr9ozo24ficQr_lbnh4Fuffjim6HIfJfk5XKMHC5CAedepNS3Q6uPQyTBKTutIGzkBNJfI5xZRpbmfxIkBw7zZ7GaJKCmFNks-0JIa2uejYnRfRWRMTrHwGgRvVvP7H1CHXjXl00NlJnBMau_wZT7yr-vc9LvJ1lN3o5TgteLITPOtbz0wz7l1tu3kB0Zn7QecoFM1fu0gLnUVkoOGSz6QR0rIBQQe2tbiaoIQKsHyq6PR1o0Ovw8MSdPHqfWayCSIofzmXFnlzDjyNmTSlvMGzukH7S1suinQiU1Rg12D7onOmhTUalONAEBBZXqtYbzhSHpgl_elzvYTNXJSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ رسوا شد
🔹
طبق رصد ماهواره‌ای از بخش جنوبی تنگهٔ هرمز تا ساعت ۱۴ امروز، تردد نفتکش از این مسیر «صفر» بوده است.
🔹
ساعاتی پیش ترامپ در تروث‌سوشال تصویری منتشر کرد و مدعی شد، ۱۸ میلیون بشکه نفت از تنگهٔ هرمز عبور کرده است.
🔹
تنها نفتکش‌های حاضر در تنگهٔ هرمز ۲ نفتکش مرتبط با عربستان و یک یدک‌کش است که پیش‌تر هدف حمله قرار گرفته‌ بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/459964" target="_blank">📅 20:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459963">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO_vx4rAfRRaLYUwcVH2ITpKQ0Pjz6t9OxQO2oh10UM3Qxt7HfPNi2VV0qeuZPFBw7rNsM8XQK2leEv7kMp3KiCEUl83nUBPYgNAAW_UVwtN5LCJmlYHD6pfRo7nFWeKUJooFiHuqnYY5LAG4vHhrtGcEo41TC0cAuqEG_0koXRfurCb8DKYAIUpLnWzePSRcQUAy2dcSKTKS6VG9ZbO6EpX1Hc-tU5Ot8nouhUmISXT_TlS_BeK-plOTi6yCsPpOzPPs6vLieEemL_tEct43Gu2zTpio5BY4MrBQ4rmM58emAqrUA0KQ6Aj_07QenDl-y-6QIhTlK_ZDdHNsSJFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکن تعاونی ارزان‌تر تولید می‌شود
🔹
معاون وزیر تعاون: شرکت‌های تعاونی می‌توانند با استفاده از قراردادهای مشارکتی در ساخت مسکن، به افزایش سرعت ساخت کمک کنند.
🔹
از طرفی تعاونی‌ها چون مصالح و اجناس مورد نیاز را به صورت کلی خریداری می‌کنند در کاهش هزینه ساخت هم موثر خواهد بود.
🔹
با توجه به تامین اعتبار برای تعاونی‌های مسکن می‌توان از تورم در این بخش هم جلوگیری کرد و در عین حال ساخت و ساز مسکن تعاونی هم سرعت می‌گیرد.
🔹
در حال حاضر عدهٔ زیادی از مردم هستند که به روش تعاونی مسکن صاحب خانه شدند و با مبلغی کمتر از ساخت و سازهای غیر تعاونی توانستند صاحب خانه شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459963" target="_blank">📅 19:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459962">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca81a14c1.mp4?token=Qimd7WEVZRIbWKbIYjFa9UehAGY3sHsvTE1me3AtRhLuQM-ZzdxCc1li-4HB4bhW1-XMeKKH8-lYzPTqS6Y3Ld9FvGJSG-A5Xr0Vot0-6ns6amGtcCuGco8sEySB0yHPGyK8Yo9NhrG05ligf-_5JJMtvcCaUKOdoItjpHAA9lM3fd3MZwKV2THDs6xnV082OoHIRgYCFsZq2edsbeJBXtuWAFsM7ZW1gD2oetwqlJdN4TSZ1JTvQW0v0EmPTBlfwxYlg9U7ETdauQRRZLeh4mDnbmhWX0BGShiqG9DBRtJ_UNO_qwYh9Va3aPc7XLwt40DxkX7-OCbQkQvexi-ywQTr6R-uhAnb9kLYd-zRW0QCsdkhixmiMI6E-IxGrzSXwUWBlTmjFsitwOFmmsUDEgJKMG83xUp-9RHyDkivNpA8pl_iPF1FTAnZ-m6HZXc51IVe-hT2t05tMeKtGfeiVEJUYvusNZLSqtr8reneXeDyT6LkgtRTDewBAEIOS9XNa35D2Y4R3YY9tb477EUwN9zE5gcn_faOZsBB91J8yn5ezrFlmKh-EgotYu4EqF9ZlNAbJ_Daq77W7hBvVoLymQFiHkuxKbQBYdhS-MgV-rev3Bo7n1Z2vQ6Oxjqaro7WTs0hT4SWqRYXuN_RCG1Fs1acnS7s_mkeEnBNQlRCvCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca81a14c1.mp4?token=Qimd7WEVZRIbWKbIYjFa9UehAGY3sHsvTE1me3AtRhLuQM-ZzdxCc1li-4HB4bhW1-XMeKKH8-lYzPTqS6Y3Ld9FvGJSG-A5Xr0Vot0-6ns6amGtcCuGco8sEySB0yHPGyK8Yo9NhrG05ligf-_5JJMtvcCaUKOdoItjpHAA9lM3fd3MZwKV2THDs6xnV082OoHIRgYCFsZq2edsbeJBXtuWAFsM7ZW1gD2oetwqlJdN4TSZ1JTvQW0v0EmPTBlfwxYlg9U7ETdauQRRZLeh4mDnbmhWX0BGShiqG9DBRtJ_UNO_qwYh9Va3aPc7XLwt40DxkX7-OCbQkQvexi-ywQTr6R-uhAnb9kLYd-zRW0QCsdkhixmiMI6E-IxGrzSXwUWBlTmjFsitwOFmmsUDEgJKMG83xUp-9RHyDkivNpA8pl_iPF1FTAnZ-m6HZXc51IVe-hT2t05tMeKtGfeiVEJUYvusNZLSqtr8reneXeDyT6LkgtRTDewBAEIOS9XNa35D2Y4R3YY9tb477EUwN9zE5gcn_faOZsBB91J8yn5ezrFlmKh-EgotYu4EqF9ZlNAbJ_Daq77W7hBvVoLymQFiHkuxKbQBYdhS-MgV-rev3Bo7n1Z2vQ6Oxjqaro7WTs0hT4SWqRYXuN_RCG1Fs1acnS7s_mkeEnBNQlRCvCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نکات آیت‌الله عابدینی پیرامون ضرورت استمرار حضور مردم در خیابان: دشمن می‌خواهد خیابان خالی شود
🔹
لشکرکشی مردمی از لشکرکشی نظامی مهم‌تر است. مردم نباید خسته شوند.
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/459962" target="_blank">📅 19:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459955">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iu9SOPR_Vg2Txsps84oTR8vVIGzK19XQSunArWgG5-o5kNDwoiE_sDZm4sqvGJKaDmzahNNGhHluC_lPDu3DM_TnSkMMlmX4h1ezKphH_Xw3EFd6WDMaqU4fC2pUm_u-9iavS2fiZzGj7-rNwegdxTPaCTA_-13512JX8kE67Y6DQTGEKkBYnNnYW99-meREjI9h4dUBqbncZAt4dBh-pAxtd9enJ2jOf3gwNjf3ZNa8fiDQThzO7VGPkHHplMtmOxYThPePBsRKf0VTH_LlYGQaU8sStnDvrvZgjKLe2XFWXZqGHVcMi5tvqZRbKmZv4Zo1Ulr9tE1LrCbYc6_6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4C9R8R4uZqPAl_6q38QWbBg8yBGRYWnBXHeGbuDa7EYfyzVkv62RAKLVGKVO3MKRklH0_A9fGR8ji0oYET8FHtWUDZ8CBGLsaA1j9VGenXKrumjqUkTTURxqwwytFw3wsho-uHQtpHUhrBHD-6s5_cs1MhRk1yZLDPYiEjRf8nY6HDjRucTdReRASUWboQnDhmm6q1-4DoTfAC4sILjwU3xgbHIiavoZmbErHo4qNKuTIyUk_-HAP8IuBM8qufhcpq5vxqcV0o_72zu5-hIpmEgU3cs74xh_cEP_T0GW8bpmoi3ejYFhcZNFbZ7WcpbkA0gIQ0Eo9BeJO7UcUJvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNSUNJOHeN-buYUDL9AHFajC_PVNqUhnJ2ePJNWcrXth8IO3mCGTotlq-ZDqSPnOH8ycYPygD8jk6oo9DfOGpAQvvjmqhFWpLcrVBXwBA_yyvbd9AiC8NxbPw2ESRyXvEpF_CFx1OwjrEw6Q90bW-ydOarHtqwBK-m21RitCc_2JU_cQa2rLioIZ8ikB1XdYHafWh0mryLRndsHUIvFoMHkhsQXfKGziViENCJ3Z99JEgDyuZLPwZFmDNam13dRK3wS0jwGI2jRsOzmuG9isjHM9ifOV4PMZurBMCFqIry5C0TAWGXBkyYhHZoybpkPDnGzj0L77B7gccukfRPDYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSxypO-WOoQNl0g6v3UDfGjlYYAaQ8LTjxaKvCxjHYL0IiLqRcDncj7ICnT8NKQFMVAr2oisOvAXwjEvXDcrGWaj7Uso6xCoOfnK_ITyDg3tjhj3eE5FqZtEHzggBUB61mqHI4Rgsd16mcmtTpjf3cCt8TB1AAKFAIbw0gTsJX6qQFInTX0pj7FvvlMPmiAdUVuPtV2-lj7axiDDd5WNkAs6TET5XririDrRf2sW15RhaqGDBwbg3Nb73DZjYA9luaD26OVjTffXgj9D3dLEZCcR8mMGsPkkhhXYPyZicfb1mGjCT_Pqn2NW-N7ZjvYcEfNdjTcPFR8E756IRlhnmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuMndQ_dMzkQJwbiKsBYFL45QYxExQyB3ByYtg2UfA6llYD_RnBQkyuNGGGEC1cDSi0UVBc7gMtlJ3SmsWHnZTVCft_7mEnmbjxDPsAsnKLb7VPoRPybrV5PgolUZubYyJYO9nivoFabLdSY2DeYo8G9smO92WCU4GEMly23pUtzDCZzNZpGpGZ_OUdkvCn7lhwHPGtxtWbmK4VksQZruNq_FRb5PGcxHjyHb2kf2Zu4_Qm8hHazuhPd1hRT0DPHpysywcp5Iw1Tj7-LlIoFvT9cVbLVNtoi1FacA9_LTXFUIP8PNc87TOnun-2obL8BbrNHkL9_Zaw028FJ7d3cEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LdYaF5Svn7HAsSRsQYbJu4bIEBP4XPCzZbHsXY5HwXmkgMqfVM9-Srq_HPwNKQDQWOkrPrqVaDnLdFyd7Q838thVb4ePT6wTHkMcnqemKVverJo_WkOEXwxVpNy0LAReMVsWEF87b3vatJJYxQIymx0FKWGKa5-a5nPgrx7Kf3HYoXO7cQtcZU8lMkT6VpCZJhyGwaKpEWzF0aW75SEsobM-RVNogOuNH04DUeoVuLfqV21K1RZNFvWAq7NoRS5M0m_1hSl_Q9fGX9x10x4n61KNbyr6Ma5Tqhx-o1zslE8qSoyMfLqu0IHowzNkSYNfadjXR1a8rMiw5OcpANqkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gW5loaEwOPDcuYHzLzvO4zzc3yLh2AYDU3VGmhZVgDA5WOO-i4vuqxEewaTlzlkVI_jo4eVoicGhrTvWp7tpUKGXTp9AgzIhInczqLGZWjHIAu2d4rejrd3Z5NXDTBfXK2Ge78VMiqzaScT169Q3dkyByotMdDF1c3xljem5Fqv0x3h_Krv4IQNZk1dQXXLM2l3e4cCDN6wOj6R3lNhuJ__NV_iloLk2Cfc02yPY0CCoPf3VWSPn8I4N9j41rCc7XJpI85KN4zm0v62dcys0cHgG0W_Cy-3Bk8atGsRDGhl2djdJYd5x_M9IV2ORRYGNJTXHLmORCTrAKAuklp2jyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارهٔ غذاهای محلی و ایراتی در سَرکاء مازندران
عکاس:
غلامرضاشمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459955" target="_blank">📅 19:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459954">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYzCzdO1tbQw-aFmklmQIL8ZjX1EUpYuPkV1oBqB-tf2d-H1nsUVJFPKs7RGnWtwlOCRGz9J_WUD5MG39pByZHueSJGBmRa3FJOvAvc1bTOLL3tRQUcQHcAa2mffgdCOsf5aG5XtuEdjCynhZnjq-iLKDlk8gB0nlqYK4qUQfkM7yEdM8gKYahPi-49FeK1ZbKU_XpBNZH2MPDfz3YiXHXOwNzL78IS5j49pQaFeSrTF-celN1tdXc5v0ChjVXpXSmtMcb5q3XFkL5ke2F7zznUYMB9eRNTe5MwgeTY6br31Uyo7Oc1GYEeJ7p0QbZYl2zmWQF7rMiXjy0BB-bP1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم آمریکا علیه روسیه به تشک کشتی کشید
🔹
قرار است مسابقات RAF روز شنبه در مسکو برگزار شود و ستاره‌های بزرگی از کشتی آزاد روسیه و آمریکا روی تشک بروند؛ اما درست در آستانه این مسابقات، موضوع حق پخش تلویزیونی به یک بحران تبدیل شده است.
🔹
طبق گزارش ESPN، شبکه FOX Nation که قرار بود این مسابقات را به‌صورت انحصاری در آمریکا پخش کند، اعلام کرده که رویداد مسکو را پخش نخواهد کرد.
🔹
دلیل این تصمیم، نگرانی درباره احتمال نقض تحریم‌های آمریکا علیه نهادهای مرتبط با محل برگزاری مسابقات عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/459954" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjpdprvOFfny9BpaRNA2bC-7HjtZM_5qv6cmHeosMr1Ou3mViV9mTH1OsNT1Xcrgbp7hI7tjR0RI5SfRwZaWM3Ip-592EDtTfcXIwm2txyUuIdjkQaq-mU6N3__khURCgbcKPgAvUSgmHVO210lY1K3eQJQuPAl0vC_m0yksB1LTvS5f2KJ5XealPl3h3EiqIkP7u6zqKF0rafkg3O5N9DY-2NWoFMMowEvDRGaWYUcPb99nrcgD_Na4FC0dwSgXeg6ZJ1bzDcLh39RrJDiWBlJU2h-sFRvS7I-MqWVRthsPDDZQNpNcJgMicFX_ANE9k2DdkEuoBvegK45nnamqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j546J2JiVKsST72xasiUxk7lhnejLnOayHSKMmNhBMth_Z1s7xXhMng4U80cHM_obJWC-xVEoVGUPC1mN5Y0C9orPtS6JJPsqeOprg7O2eXYLJcqaW2VtKiqtdvkgrDHm-OLaVvo_3fMRuGc-nekeiWT1ptF9dgCcXUOlAMEqboSP_rEE4mMjuKMk6LCPZZYHS7euXceNZz75U91Bd4mvPSCNIhh952ROThw9GkcC4vqs5VR5frxch3qiDx_MR9zb07v6-LuTWdAreW7TlmYFuTMkKWAln3DRcMViSUufPVRvYv80BASoeuDaPlXM3fEM5uB4Mr07nurFBsds6q6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IK-YfGIZDp2wBo4X_fi5MNk3rq2wx70ZqDQzUJFiz9sgVc9s-JkHtiLdl-90bPnS8pWRuOUAL_UvTQY59NCijz8Bi_jp4SFelv1WpFcaCsJgTpllu3BCjQGJbAyDBVbg00FcIo4e_z0FIik-NJFT9affaC6ayiUAuHsOEvKePPXE902ZhbYaYHqY_B4sDYm5qOHMCz5NGe-4PTQIW0ukY9Gc0_jCZUKq_VP8CgTKPQhT3t-Hl7m__tXaqYSthXXweQ5pMUFuStJIDR1W7bR4VpUcEky_DSDv7YpGxDq_9hrb5bhdeaFUbON4HBzDTw2c_cEAIyStLxa_yOqSia1Fyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb6FUUutPsiBMqJ8mr6O__IeaySvo8cC-Cyf-eZ4B2jAX4DgTPSXvvsjRadz9Vj1FPKeVKtEym4ZLUtABGyuCd8Cc7LWf77I2Z3i8z_u6stH-GSpiZftF59aZ2cqDwuBMerzDhDY8CIpt-CRPj5waKMzqB8_3-qlkYWEa_vO_XUAraGShHdNfZg79TLju_QSk-yqLtNRt_itgWL3iR5pafHLA8PM_4oXmDt6z4Hro4T9o0xDMBS3GfU7o93t7IqJk40-bS0vlUQGz0RSPQ3pC27jUM0of7s6x8p9De-pqzXVcMYcRiLOaxSZPaWSZVy6dpjLx89Aj1h7pb4uJbPBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccmAax4WuTn_3z9Yt_Xk71Mpt4l_jKFi1YUfB592VuiFT-sAHB_pUtAQgwGkuBclQCWzS80GHwbzgpnB7i9JRY_hgTQCsZEVdIXyHLdNWwQjMVzEPPTwwiYuwBA4VDkpBSo5kzagETXAXStEmCyI12-KqhLDszWDxkSNobt54WJf8RAAUOBX6v0NTZe6x0gQAjdWJS6dY2323ojo15ytZAQLMqUCJW_h8GEAaSEU8KpzE4lDsx36XSrBSEjAl_hhcxhnNGhSZN0y5CdaxKQlMc8BZDKNLZqcYhfOjGM_C8BCzbdSPnWhN9UZOqojMTT_ZlViqwxk_xxgIxmO0hVGjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقهٔ سردار شهید جعفر کهریزی تا زادگاهش
🔸
پیکر مطهر سردار شهید جعفر کهریزی که در حملهٔ دشمن آمریکایی به شهادت رسیده بود با حضور مردم در روستای کهریز کرمانشاه به خاک سپرده شد.
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/459949" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnKDOgJV2MzuC3Z1i4WG9cWImwiC30KlnXdfCD3fbI6mViHwp6753R41xn3R5o5dBcxr6qMiogwh7y_vcoJrzviYhPtBoYpygkgQLPM13Up8YbW32P_zpAvWNKYh9c7Ao6f_MigmwVy-atyYRMBvIYWR6-tjiYVNi77rWU6oWz4fIBXiapwC6jhm0t3srsPDhUaE10OUE9QlX99EPxZJ-uBysofuSMGsj6aXr5ZZabfnDAwWpLjvtIsyy5nQeW4Pds4dNzRXDQBe_YsbaKCLxQcg1uFqkd7ld9d73kj5PD4yp2L8Ud7kmvVKvj6WSMdbWeuXi2jUBcsp5HF4xdlt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مقام کانادایی دربارهٔ ترامپ: با آدم بد نمی‌توان توافق خوب کرد
🔹
رئیس دولت استان منیتوبای کانادا: «همه دیگر رئیس‌جمهور آمریکا را می‌شناسند؛ او بی‌ثبات، غیرمسئول و غیرقابل اعتماد است. به‌خاطر ترامپ است که ما در حال حاضر هزینهٔ زیادی برای بنزین در جایگاه‌های…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/459948" target="_blank">📅 19:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459947">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQIl33MSvF8RPn6tkPgO9m9W9y-MNyBOjI8JiYNGVeJcY-vKkkVWElvWwCvwpt37cLoeeRRF0Do_FcAMlHxjkoa-ANNGpO59Hg8mfnVZpgKjdVAsBXE3Fut6cM0FgOAHYUYsdVnK1pvcQzGnCVf-StsdV0kkPWNkfuAVuNqAvjYS26KNHxDcuD3uTAke7soxPvhSCJKyUqHu_gtzvu2cyYcwHumJ1c5d7aWnMbVchIVO80tqAjM_uThvbOC9XGGTDI2zAEgT50_q5XVO3dDaJNQ503_4DDvswEBxFx-IVy5e8yyBlQqBCte1vNSloyPL-JrK7SbwMXzOiXKAaN_V1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع اسرائیلی: حزب‌الله خود را برای درگیری گسترده آماده می‌کند
🔹
منابع نظامی، امنیتی اسرائیلی به شبکه عبری «آی۲۴نیوز» اعلام کردند که حزب‌الله لبنان، همچنان به جمع‌آوری اطلاعات درباره نیروهای ارتش اسرائیل ادامه می‌دهد و روش‌های عملیاتی، الگوهای تحرک و محل استقرار این نیروها را زیر نظر دارد تا برای احتمال ازسرگیری درگیری‌ها در جنوب لبنان آماده باشد.
🔹
به گفته این منابع، حزب‌الله در حال به‌روزرسانی تصویر اطلاعاتی خود از نیروهای اسرائیلی است؛ اقدامی که در صورت ازسرگیری درگیری‌ها می‌تواند زمینه را برای بازگشت این جنبش به روش‌هایی مانند نفوذ، کمین، استفاده از پهپادهای انفجاری و کارگذاری بمب‌های کنار جاده‌ای علیه نیروها و خودروهای نظامی اسرائیل فراهم کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/459947" target="_blank">📅 18:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459946">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udxjBTZ91oomLpVncVrpJ6juw98GXZqPtBW6znFR5sNSiQT2-7_Uwnf9znxKC4qdGMyXM94fo4_uhWmIsVJOERh0LOF2ukXR4RzHLZVwc_xSqtJ1bs2ZlOHyHAvA0hk_NxUlOq9B0xOtP46L6iN99j3-6QwU1yfQmGP3E7AjzKJdhp_nG-TqIaqiy0xJka4Irj34VzHIu6rkbwXzBnFv61owiMuUheTZ3hJiajgPZt9qbcOPdUFfJT3Ptzgl2xl3uDTngjPna3PG8a2Y3qWnllBuw4ONVmbOF_mId-RMe4nqHCwu82fVGxEw6T7HxwsOuidemonwTCTvoPj7Wvti4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
افتتاح بزرگترین و مدرن ترین تم پارک ایران در مجموعه ارم با حمایت بانک شهر
🔹
طی مراسمی با حضور جمعی از مسئولان و مدیران حوزه گردشگری؛ بزرگترین و مدرن ترین تم پارک ایران با نام «دنیای گمشده» در مجموعه ارم، و با حمایت بانک شهر به بهره برداری رسید.
🔹
به گزارش روابط عمومی بانک شهر، احمد مالکی معاون اعتبارات و وصول مطالبات بانک شهر در این مراسم که با حضور معاون وزارت میراث فرهنگی،گردشگری و صنایع دستی، معاون بنیاد مستضعفان انقلاب اسلامی و برخی از مسئولان کشوری و لشکری برگزار شد، گفت: بانک شهر با سرمایه گذاری و مشارکت در پروژه های تفریحی و گردشگری گام های موثری در راستای گسترش فضاهای تفریحی مدرن و ارتقای کیفیت زندگی شهروندان در محیط‌های شهری برداشته است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/459946" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459945">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-jffVPLhM0jS-k157iDMs1SGBkCGHoAH1lVVm0E4bIz_O3v-QZHmbfZdeXM0rFRdxm9YgZCZzIB470E2Wd1HLBcPSi-TWDI0WhiQ3GlJPjSE3yIfxgcMx2K0WOJmrev0ddAzzclxfDokgJYwBh7upiTh7J_2c9ZxaZEy6C3FCII8Ug8cY-43Eg3gjb4p972fM14fZgl6lNnmWi1H4WbtmugyHWWa5ousfru8WS7eyLyq0nn7pHMssp9RQPqks2X-nIqM_8jOkct-K9r6e4mH2qeeGd37llwCLu03mkoBmPlGoOzdeVk-tXYadYy2HsgJC2PsnzpzmOJHD3c3WCr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🤦
حل گره‌های نقدینگی و توسعه خدمات شهری با ابزارهای نوین بانک تجارت
💠
مدیرعامل بانک تجارت در دیدار با معاون مالی و اداری شهرداری مشهد، بر رویکرد نوین این بانک در مدل‌سازی عرضه پول و تأمین مالی هدفمند مبتنی بر زنجیره ارزش تأکید کرد.
🔻
دکتر اخلاقی با تبیین کارکرد ابزارهای تعهدی در ایجاد نقدینگی غیرتورمی، بهره‌برداری از محصول «ستام» را برای تسهیل امور مالی و بانکی به شهرداری مشهد پیشنهاد داد که با استقبال مدیران این مجموعه همراه شد.
🌐
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/459945" target="_blank">📅 18:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459944">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/459944" target="_blank">📅 18:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459943">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9_OFDYP2Doyac-yFzd5GN9PGlmUauumx74F56gI0mdn4DxHZ0_8anXSuGCPwbsm0ZaFKR-F2s5HQyKmnAFi0diizPFAfrKGli8iuKWHEGcf4lRFhQ63OBO76OnEH8Yd6rtUhuZo2zXhJAB_besGrz9Pi18TvJsT7qxZD5EwYcPVg4bGkjeA_uZilmLJ3DsGVSOI6w4UAnfkw8oS6VyQjnhBAW4KsDBL0dVOpzvtkopooOWPViiPbViJr18fek9fTcc432zwV1qzyuI-1_9GFHfNast3Od8hCtNsgQbjr3YvUnunQTuL8eeDfyDTnXtRs2Uo8lUHZfKaL-yw5W0Geg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: افرادی که می‌گویند آمریکا مهمات ندارد خائن‌اند
🔹
ما به مقادیر تقریباً نامحدودی از مهمات درجهٔ متوسط تا سنگین دسترسی داریم. ما این مهمات را برای خودمان نگه‌می‌داریم و به بقیه نمی‌فروشیم.
🔹
دولت بایدن آن‌قدر مهمات مجانی به اوکراین داد که بسیار بیشتر از آن چیزی است که ما در حمله به ایران استفاده کرده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/459943" target="_blank">📅 18:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459942">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb7ybUM2vfnLxXGqVoMb4L_EiEvcYqwTNip2FGpP1OnVFmbfpVWYz41f71VsVQgEXauKvaM73FoBJ7ZjZ8Vn5zC1ZmuEC-HDfIuz0KXuMKqw5wG5FJoKwn_lgFH_AGfUpXMEVLNqmGNGQotwg6-P_7fyteXVmW47luLjxXmhndS5pfMKA4jd-UNQXKNWCBQO8hhUkLlhv_5FwfE9wj-k9UxD44xIb0e-s0WrO6LAHv5W2rCIr2gzE_fMJfDGxiGxqy6brIKabjjcjr8y5meWdEoH9tVy5wBKXPufLc_65OMkuWdC2V6ElLTmEu9GfUFqptqIlluQKMZvOiYpLyj-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای پلیس امنیت به تتر قسطی دیجی‌کالا باز شد
🔹
چند وقتی است دیجی‌کالا فروش تتر به‌صورت اقساطی را از طریق دیجی‌پی آغاز کرده است، اما کسب اطلاع خبرنگار فارس نشان می‌دهد پلیس امنیت اقتصادی به این موضوع ورود کرده است.
🔹
دیجی‌پی از تیرماه امسال وارد حوزه معاملات رمزارز شده و امکان خرید چهار قسطه تتر را از طریق پلتفرم «دیپکس» فراهم کرده است.
🔹
تتر یک رمزارز با ارزش تقریباً معادل یک دلار است و قیمت آن امروز ۲۲۱ هزار تومان بوده اما در طرح فروش اقساطی دیجی‌پی هر تتر ۲۴۰ هزار تومان قیمت خورده است؛ یعنی ۱۹ هزار تومان بالاتر از بازار.
🔹
طبق اعلام دیپکس کاربرانی که تتر را قسطی می‌خرند حق برداشت تتر خود را ندارند و تا زمان تسویهٔ کامل در پلتفرم باقی می‌ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/459942" target="_blank">📅 18:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459941">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2m1XZG6wsgcu2R9clk3qw3lOWVep1kkkNv8PPDX6b7_Zus-4cyNB0DSqibKlEJvDhexxlNrbcyrjlagX3QCgYM3lx63XhG5BT12o4yWRNMGm0ht-Dt23suXdXpBwJ6YrcJh0WqUL_Df2LcoIuCEhjWqNCBj3G6r6iBTK5QTQPeidQscUJKSxso2iuhVNCmCRk4ZPF_mRu8NvMJ5Y-nZKns4NxJYbxVM-byZDj6M7CYAwtJn2FQSI-BLqm8L_8icNydkT_MXI5OQFR7ZCmkUZC3L99AGKMH-6uoNQbibEcrWlc3koxXDVfD4Q1iO1LjJ8wABFjDWNLlBEWmg6116dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ترامپ بابت انکار تلفات آمریکا در جنگ علیه ایران عذرخواهی کرد
🔹
هوارد لوتنیک، وزیر بازرگانی آمریکا، روز پنجشنبه به دلیل اظهاراتش مبنی بر این‌که هیچ آمریکایی در جنگ با ایران کشته نشده است، عذرخواهی کرد.
🔹
او به کشته شدن ۱۸ نفر از نظامیان آمریکا در این جنگ اذعان کرد؛ این آمار تلفاتی است که آمریکا آن را پذیرفته است.
🔹
گزارش‌های متعدد رسانه‌های آمریکا حاکی است آمار واقعی تلفات بسیار بالاتر است اما وزارت جنگ دولت دونالد ترامپ برای کاستن از فشارها آن را پنهان کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/459941" target="_blank">📅 18:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459940">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM4trdFu_YS1Fg70gipqgRQ09orTnH0fuu0JKIMUx-2xPmRauREjd34lOBC-v9fEA4IGbV7F-7NKIxubWqLd0T2MY7oFGkf_mu82htrwo8fR-L73YZPZzEa-yKeC5hSltGAxQ24XbAaP_bAX6R0KgbgDnFCfFYEyZumr95TWtKdd32IY-wtI01PCj3csA1_m_OacdHfgapj6vZysSWPeyDlM45uZKOFnII-SPT5SCU-vDE-Ee9iVKWHJempCDk-5Zxj_zGx0cRD25hz0B8vi4H_lRvt50sqaDhv_GyC0Mq9c3vFP3QbMvrGXovexbbXOfITn6VBEGZWrr-Ku-xThVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای حملهٔ آمریکا به مراسم عروسی در سیریک به ۵ نفر رسید
🔹
رئیس دانشگاه علوم پزشکی هرمزگان: آسیه مولایی‌نژاد، ۲۲ ساله، بعدازظهر امروز بر اثر شدت جراحات وارده به شهادت رسید و به این ترتیب شمار شهدای این حمله به ۵ نفر افزایش یافت.
🔹
در حملهٔ ۲ شب پیش آمریکا به یک مراسم عروسی در شهرستان سیریک، ۵ نفر به شهادت رسیده و حدود ۷۰ نفر نیز مجروح شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/459940" target="_blank">📅 18:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459939">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f7afd1e7.mp4?token=d_RQfgNMxtQMdimpejyDbZqQnaV_vrn44Tw6hFdpQb0IjgfMiXxwReDjfgmxnxv0X58CJsEccoDizi5BU_55UeW9qN9wNRaYRqrhGJyF9iVGwd1eNHNsClxNZ1b5GdiBSj5tacIGMl2QN8DvIUoPEqx0fc3Kt-9AfA9O1lyiXxBDt3F_qKGIl6BBZlFWyCu7Y6Z8sRe5mgedU-1oAwv12t5THUWGh0pj-5KgvC6b27vU5kPVBSzrKdypcu2qb5nbqENbplH9e7exRoZXHFBLch70dhBx5656qu6OcO5tA4ay2O5zsruh8REeV9-idt1C3sSu5GLxll-HyvowEWwVbVfYFtbVf3qZnpjNMcJCHgU9LfNwEayrEVRdmKzSIPy44HffLSmhM0DYlkXe6ge07db7YXoJqwKz6FINnwHs2LvTweWQVE15nJjYwQnoOwu5uyeOgYYmQk8KoqsEVlzbOKQzDwGJqdpTUz2AS_PEqqkqhSFYbCEKH9hcp0ocS0P2UlCt_M8SoG0tIA_xYzFKB5-2wZ6nmm8-qtrsdiWnw8tkb_FNjw3Y_B2Q7Drxs3DGHeRJ2jYXDWkKhLBWk6nGJvMD1WdmT3N9phbc8b78ldnSRI4yujc6oePX6gF1EX7BwwJVYTSScUq80K8qYw7Zn2_sxcZExSLG2b895Ijc1uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f7afd1e7.mp4?token=d_RQfgNMxtQMdimpejyDbZqQnaV_vrn44Tw6hFdpQb0IjgfMiXxwReDjfgmxnxv0X58CJsEccoDizi5BU_55UeW9qN9wNRaYRqrhGJyF9iVGwd1eNHNsClxNZ1b5GdiBSj5tacIGMl2QN8DvIUoPEqx0fc3Kt-9AfA9O1lyiXxBDt3F_qKGIl6BBZlFWyCu7Y6Z8sRe5mgedU-1oAwv12t5THUWGh0pj-5KgvC6b27vU5kPVBSzrKdypcu2qb5nbqENbplH9e7exRoZXHFBLch70dhBx5656qu6OcO5tA4ay2O5zsruh8REeV9-idt1C3sSu5GLxll-HyvowEWwVbVfYFtbVf3qZnpjNMcJCHgU9LfNwEayrEVRdmKzSIPy44HffLSmhM0DYlkXe6ge07db7YXoJqwKz6FINnwHs2LvTweWQVE15nJjYwQnoOwu5uyeOgYYmQk8KoqsEVlzbOKQzDwGJqdpTUz2AS_PEqqkqhSFYbCEKH9hcp0ocS0P2UlCt_M8SoG0tIA_xYzFKB5-2wZ6nmm8-qtrsdiWnw8tkb_FNjw3Y_B2Q7Drxs3DGHeRJ2jYXDWkKhLBWk6nGJvMD1WdmT3N9phbc8b78ldnSRI4yujc6oePX6gF1EX7BwwJVYTSScUq80K8qYw7Zn2_sxcZExSLG2b895Ijc1uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع با شکوه شهدای حملهٔ آمریکا به سیریک  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/459939" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d69df331.mp4?token=h0jW_oPCgggWJOai0ff0X4CXrwhb1c9oSHHlLwcKa2pJNZRID5pvO_sILIJoZ5h1flzkL74Y_87jnWraJpQ-z1R9FwRoDuK5kmkua-XocGfveBmQ17K8FbF6pj6iUO5LuKhnBng3PnriKrsvmquGlKjVwLMfKaWMYMbMXzgeTxwm3TaK1JfPAHcSdjzrKrZD8HcmslMvPqn5U227GOxwHDRKrcJlqwFCN6PWRXVUa342IQlYw9YaYr6VneWxxNbrzAGBxC_EBL7LdAgetSyMW5OFHYdhU-XbZACX0qbeh9R5n53haetZtMVaapRtUJbNMR_0s2yvfujhe-R_AgWA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d69df331.mp4?token=h0jW_oPCgggWJOai0ff0X4CXrwhb1c9oSHHlLwcKa2pJNZRID5pvO_sILIJoZ5h1flzkL74Y_87jnWraJpQ-z1R9FwRoDuK5kmkua-XocGfveBmQ17K8FbF6pj6iUO5LuKhnBng3PnriKrsvmquGlKjVwLMfKaWMYMbMXzgeTxwm3TaK1JfPAHcSdjzrKrZD8HcmslMvPqn5U227GOxwHDRKrcJlqwFCN6PWRXVUa342IQlYw9YaYr6VneWxxNbrzAGBxC_EBL7LdAgetSyMW5OFHYdhU-XbZACX0qbeh9R5n53haetZtMVaapRtUJbNMR_0s2yvfujhe-R_AgWA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشییع شهدای مظلوم عروسی کوهستک فردا برگزار می‌شود
🔹
روابط‌عمومی سپاه هرمزگان: مراسم تشییع پیکر مطهر شهدای مظلوم مراسم عروسی کوهستک که در جریان جنایت رژیم آمریکا به شهادت رسیدند، پنجشنبه برگزار می‌شود.
🔹
مکان: شهر کوهستک، از بلوار ورودی شهر تا گلزار مطهر شهدا…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/459938" target="_blank">📅 17:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrsAmp2VwDGp4FoXS-02qCzSdnmgVSS6jk2YLfs8JMjBBkmVA0gkksyeWt_BY5B8gqnHR_qBhb0lkpTVRzkXiB4wxVb9gABwsJc62RjrxEfAERpnSfrug3lbz5M-krKoRb3gB0l82goJOPjZx4beU46w9cdSk1qUXUbhe7-NWrkOYn-RntOMe_D-GEy4os-6ofgz5czRUfQFfOKkErsW8a9ER5DkWL8zI_aWhzEUQq1bjX6LGS5aVdNqgFWWlgjbRmYj1-c-H3mdnXISijzoxI763jwcQDrj4J9mL7cenke_vzJBgXsl2o3jFhHaDkPilI275JZtojlGKUuH2sxi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشکار جاجرمی نایب‌قهرمان مچ‌اندازی بازی‌های قرقیزستان شد
🔹
محسن میرزایی، ورزشکار جاجرمی، در رقابت‌های مچ‌اندازی بازی‌های جهانی عشایر قرقیزستان با کسب مدال نقره به عنوان نایب‌قهرمانی این مسابقات دست یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459937" target="_blank">📅 17:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459936">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfkMjmu5IefWzvq-TsiMENKVNnMSMN9lo5y1qmGtEelEdaXraoK9DWeTbyIuHo7Xa8kIDKkWx1l45_5qtb1Tc-LCs_sE0kZoEsQ_stoEzbb7Jrx_CmwvzBnktP_Jy__68MwAgytwhdWV80trKjHmu-xp9RVsUV_O3pZAqWWoWMyesnmQjY3zk3QoNATzSbadYaMDuEWOlOyBR4uMfO1Tbf0Ylle9aU5iPrVxy0S9awRc8AO6xJ4_tV5ghw3WEfanZmYQ9IPm8-1_h89g657wHZ9CmRdI91nhq-KmvGbneI0fiYbt2ppYHaQ-_wEUhvUtoNGyBV_ucXB_2318ZfN7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران‌خودرو قیمت خودروهای مشمول اسقاط را افزایش داد
🔹
هنوز ۳ ماه از افزایش قیمت محصولات ایران خودرو نگذشته که قیمت مصرف‌کننده محصولات این شرکت باز هم افزایش یافت.
🔹
خودروهایی که از تاریخ ۲۲ اردیبهشت ۱۴۰۵ به بعد پذیرش شده‌اند، گران می‌شوند و ایران‌خودرو می‌گوید…</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/459936" target="_blank">📅 17:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459935">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bbf88ef4.mp4?token=cRmekn1NIsyA0UmSvXWGK9MEaZNQkI0Ji3c1acvEAwqimHihqGzjimnZk9OjjL8Lg4vcIqtnTyzdquLebhUO4pjcO3qF6DMTNNRAFHjZWak2Sgayt4kP0ZhYZHDx5FCiF49iFwpYyXJ-EmkNW4sA0qE-298WNkDc5gZzQ8eJEfNUwheT43Eqie9idyLYfPUdoierVidSyeSDdiX7-bnlK0gaapLeI0HYcU21NFQfZl_OplvfF2jWlEYIMzOXxU1JHga74NuEKI_b3rST-RsYd2JuL-edV0Q_p1uO4G8Qf3JH_jH-hTsiP08LUQ8E7juv9mZSNGPss7f6ckVNEAlP_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bbf88ef4.mp4?token=cRmekn1NIsyA0UmSvXWGK9MEaZNQkI0Ji3c1acvEAwqimHihqGzjimnZk9OjjL8Lg4vcIqtnTyzdquLebhUO4pjcO3qF6DMTNNRAFHjZWak2Sgayt4kP0ZhYZHDx5FCiF49iFwpYyXJ-EmkNW4sA0qE-298WNkDc5gZzQ8eJEfNUwheT43Eqie9idyLYfPUdoierVidSyeSDdiX7-bnlK0gaapLeI0HYcU21NFQfZl_OplvfF2jWlEYIMzOXxU1JHga74NuEKI_b3rST-RsYd2JuL-edV0Q_p1uO4G8Qf3JH_jH-hTsiP08LUQ8E7juv9mZSNGPss7f6ckVNEAlP_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دختر کشمیری حافظ قرآن، از کمک‌های مردم پاکستان برای خانواده‌های شهدای میناب  در برنامهٔ محفل ستاره ها
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/459935" target="_blank">📅 17:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e81f42667.mp4?token=YPgJtam8TNtQ6eVxQPRgmyzPOtucdKE6u--kOTHfFjyl5LUV0JoozkmGvdJ4qwr7LdANoZFlR9Q803ScAFNGDbCbWLIew26L3mDFxZIqg3t1cDGEc2-vPQ5P1Eiq-6rFH4AqglrWi5Zegi3Q-u7SO5sDGEhzd21BmyPIjKrLe33Mf86pThM3VoBUvyMWcWCvAU18N7r4si3RGEx46faklbCff8xos54I_Of4Z07gZQzKxjWIX2IaQBg9jnIgxeyol2hRq1emAGF_Gj_rJawYkS5ef62ecgBk9PyAtl-EIgOpMk0EGj4W0zqoG9IQUz_Liz59tyni_W9hNZBUduQa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e81f42667.mp4?token=YPgJtam8TNtQ6eVxQPRgmyzPOtucdKE6u--kOTHfFjyl5LUV0JoozkmGvdJ4qwr7LdANoZFlR9Q803ScAFNGDbCbWLIew26L3mDFxZIqg3t1cDGEc2-vPQ5P1Eiq-6rFH4AqglrWi5Zegi3Q-u7SO5sDGEhzd21BmyPIjKrLe33Mf86pThM3VoBUvyMWcWCvAU18N7r4si3RGEx46faklbCff8xos54I_Of4Z07gZQzKxjWIX2IaQBg9jnIgxeyol2hRq1emAGF_Gj_rJawYkS5ef62ecgBk9PyAtl-EIgOpMk0EGj4W0zqoG9IQUz_Liz59tyni_W9hNZBUduQa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تفحص پیکر مطهر ۲ شهید دفاع مقدس در چیلات ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/459934" target="_blank">📅 17:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459933">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZXyQpOiWkbVJTMNG7NJlKTMr7BWgaZVsQIOKA4scyRhVguiPGyNZ0yB9YYNcDKlAlbdzhdyXQEWbraoHlDMMuAj_YIiPqLFXWyQqnVdwyA6c7-kjsfywBDA3dOKxG_HZ38n7OFdBSvuddfFB0QW2NRTElPqz9OTGKP1ScD_dMeojg2DoHvCBEQvpeDiNbZwP239jq4gG0XozFUb08Q7NKjcpnfJ_d1LlFcQZA9SjZhd_InutII8RvgzCGEEOul6pTQzafHNu4AGQTFJjEK6fRS-HVBfWaCoaPXdTetbCiFnD_J5WCoj8_clmj3eZRtmitKG1ESQ5QKsdTqsEMhvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ اسیر لبنانی امروز آزاد می‌شوند
🔹
رژیم اسرائیل قرار است امروز ۵ اسیر جنگی لبنانی را با هماهنگی آمریکا آزاد کند. برخلاف گزارش برخی رسانه‌ها هیچ مبادله‌ای در کار نیست.
🔹
شبکهٔ ۱۲ تلویزیون اسرائیل گزارش داد که آزادی این ۵ لبنانی به عنوان «اقدامی از سوی اسرائیل در چارچوب مذاکرات میان ۲ طرف» انجام می‌شود.
🔹
در مقابل قرار است کار جست‌وجوی اجساد چند صهیونیست که در خاک لبنان دفن شده‌اند با جدیت انجام شود تا پس از پیدا شدن اجساد، به اسرائیل تحویل داده شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/459933" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
