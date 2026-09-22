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
<img src="https://cdn4.telesco.pe/file/vISDtCftnA20Twf5uc23E5YWsvus-NX9Fl1XBt3IuaK-lCAyQgU9itzXAsoZqITAjpCq3hsOexpKSyiQdKV6MTsenEBVnx8t-UMMh3Wr3oE_umV3hyotWM-ImHVDLGsIl7GPpLhrTTgQ6y-Eg3KZ7HQgKnwKruupHC6tyx8Rz03_sh5PHzyofSh2ZpCJazCXOp7Z_OdE40_n0DmoPnQhPCoF8B34YhHA-VsuseOBcn_V2I0P330I1C4lZcQ36KxgmlYmoHeAlQ3jGttBK_SwWoXoTHWtiQrvX2KB8d6lFts4QdUZzQeIM3QAluiRdDKu1laWRP4WPY_uuvaQLdSIvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 992K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-148826">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
روزنامه نوبنیاد به خاطر حضور عراقچی تو سازمان ملل اونو «بی‌غیرت» خطاب کرد و خواستار استیضاح و برخورد با وی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/148826" target="_blank">📅 22:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148825">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ویتکاف: دیدار با ایرانی‌ها خوب پیش رفت و در حال حاضر احساس بسیار خوبی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/148825" target="_blank">📅 22:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148824">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
خبرنگار i24: استیو ویتکاف و جرد کوشنر، مقام‌های آمریکایی بودند که امروز با هیئت ایرانی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148824" target="_blank">📅 22:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148823">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEHnYgUPqlK-1XL7bM3HvoAokNmGaeodKf9QdqmlxJYS2iY-1h7N-TtVh0GmcTO4Tg3lI_9t0NhmblVv4agXMiBBoERO2QyxwHGN-GQsulsy6_WI5_cn6YHhKC7DCMacs9ikxbOl7A6zx8zLWih_FMkxMz1UlrT-WXSyUJe6c0SEkkYHpowwthm3RJPoIn60OWSgQ_vnC8sW-ycS6kZ4CvoH9n-iaK3bPijJTn2tv7WEkbNMQkvUKNBJ32w2Ag4Ao1nSTs2At65WbwI7KpQjp--8aIj_DaA4qJa4VtGa2DahCX6mlttIHOKoRNdXbz30YOSnRRyVnUcm4YD94KiFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ریزش سنگین قیمت نفت بعد از سخنان ترامپ درباره ملاقات با ایرانی ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/148823" target="_blank">📅 21:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148822">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کارولین لیویت: گاهی فکر میکنم رئیس‌جمهور ترامپ بیشتر از مردها به حرف زن‌ها گوش میده. اون احترام خیلی زیادی برای زن‌ها قائله
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148822" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148821">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: جلسه کوشنر و ویتکوف با مقامات ایرانی در نیویورک بسیار خوب برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/148821" target="_blank">📅 21:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148820">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ویتکاف از ارائه جزئیات درباره دیدار با تیم ایرانی در سازمان ملل امتناع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148820" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148819">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «آن‌ها قرار است در آینده‌ای بسیار نزدیک، جلسه دیگری داشته باشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/148819" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148818">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: مقامات آمریکایی پیش‌تر به مدت سه ساعت با یک هیئت ایرانی دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148818" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148817">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
امیر قطر: تهاجم اسرائیل که با غرور و خودخواهی مشخص شده است، به کشورهای همسایه گسترش یافته و بر امنیت کل منطقه تأثیر گذاشته است.
🔴
ویران‌سازی روستاهای کامل در جنوب لبنان در پرتاب روز، یادآور تاریخ آن در فلسطین است.
🔴
مقابله با اسرائیل، پایان دادن به خساراتی که وارد می‌کند و مهار رفتارهای غیرقانونی آن، آزمون واقعی جدیت جامعه جهانی در حفظ ارزش‌ها و حاکمیت قانون است.
🔴
قانون باید به طور مساوی برای همه اعمال شود. زمانی که قانون بر آسیب‌پذیران حاکم است اما قدرتمندان را در امان نگه می‌دارد، معنای خود را از دست می‌دهد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148817" target="_blank">📅 21:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148816">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: صنایع هسته‌ای ایران را بمباران کردیم؛ باید کنترل خود را در منطقه حفظ می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/148816" target="_blank">📅 21:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148815">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCmmWpheS6B8c5OG5Xn6jTHUIr-FgDcXm6YkoATxBkUIfqzoxakvlNa9lKZdALZOu0NTgg_25_gQv-HrNy9QWLo6T_RS65Uizf0SjPQ6sHtO6pEmqGm2lOPjtFUQY3AKTO0nOFWrD1NOGek4s2XxfVSIBF5fidf0d1ptZmRHYpc0ECWrDJ474U36hAYCa6Q9TZ3U81Mb1FO3A7jt5sEjlYbUaSsFiQeYNIpg0CHO2GtSYDa_K25lPIDaGNmWIdKMBHu36b5SokPHsAHylTfi2-MKlaaZrHbv8f0pmqoKnsjAMDW-Vbh5BfE0KPSLE0luFJEToEC1OeMr7L_jJYmBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جمهوری آذربایجان هم رسماً پروازها به ایران را متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148815" target="_blank">📅 21:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148813">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGWh0MBWRVl5wF_mPQuvmAFtzIBlWtDbSv4ogBCsRxeVbwJatnlJQswZXsQueNYHMmSErnxMcUaKsavdqLJIotRDGvhsGSlHsd4MlLVVTInt6oLrSK4q6j9u2NgHVkymzOSoi6qhzBUcJb8Vo-x_3yUq4QP6iBmA-YQEU5EGZgk3n2B3tIRn4bPj2t21jaKxMqTojJ3SgsQthRYSTWDRQ9WfnY9vu-1Dq6oePwqrTOFuYPE-SJd9sYZgTfKKKX_7bua2ItXpHGZdNQpImktF3WJs_miwdI3Mh2YMq0Z995CfP6rOiN6pVmnvHpy0a3dPPo2XrAYtuvuspPvJ6abhtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5d86448edb.mp4?token=S3wVJbfEQotA8VgUg2rytWud67gtg6xg1ZAzYbrf79n4hdi0xRnY3yz2DeqAlMhXgt5GRGOTMO2ufGjfQsro03vDdtQN1EcNc7eK_HdTvQKpvitthXI4PyMS9JdoPfIuDRKNfpN9mkEXgtAkMy_N8Nkn2AxMrudKAEfEm44ijUv2-et8w7IhVTJapstF0LVfHX1XTBTokXSxcHt8_YOh9QSE1oGoc9BVr_yR3MpZyBqp54fKkzFFFbqoSHk5R23s5-JjL1FUddnFatD4GE3w9_ZVokO8gAmdwypcYdyYcqmOHET_-H94aVx1X-xsV06vbvfUuHJSQM4-6CxYf7vNIiyt8yyZA30eWrR_sLAAbk-ofm1_EjYbsVn8j2aXK-NaIBE7f98JcB3eNOyOXAghrfnWnsOx88gS_Wl5m3qCnH4gTMFj8thOL6X0lYJkDTCxd1eNPvTAovu-rp3vNdZGLyPfhLpArpSGoN9mnOixEnNjsIBXtPiWdSFfkO-4V_uyJSsNcJOPrq8-1JAHAttv9tEhnXv0jvg8kZbnJJNdJexdIuj908G_H49BA3i1jprupgoW5kZk2J5hnHdkSvYFDsRNuL6d1zOpsKnygiftFlGNfAT1vxUUmm5rjg0Ryouc5U1wED2CeSQhapXeJvAYhB5Xqu_Dr1q01WfHoQB5nwU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5d86448edb.mp4?token=S3wVJbfEQotA8VgUg2rytWud67gtg6xg1ZAzYbrf79n4hdi0xRnY3yz2DeqAlMhXgt5GRGOTMO2ufGjfQsro03vDdtQN1EcNc7eK_HdTvQKpvitthXI4PyMS9JdoPfIuDRKNfpN9mkEXgtAkMy_N8Nkn2AxMrudKAEfEm44ijUv2-et8w7IhVTJapstF0LVfHX1XTBTokXSxcHt8_YOh9QSE1oGoc9BVr_yR3MpZyBqp54fKkzFFFbqoSHk5R23s5-JjL1FUddnFatD4GE3w9_ZVokO8gAmdwypcYdyYcqmOHET_-H94aVx1X-xsV06vbvfUuHJSQM4-6CxYf7vNIiyt8yyZA30eWrR_sLAAbk-ofm1_EjYbsVn8j2aXK-NaIBE7f98JcB3eNOyOXAghrfnWnsOx88gS_Wl5m3qCnH4gTMFj8thOL6X0lYJkDTCxd1eNPvTAovu-rp3vNdZGLyPfhLpArpSGoN9mnOixEnNjsIBXtPiWdSFfkO-4V_uyJSsNcJOPrq8-1JAHAttv9tEhnXv0jvg8kZbnJJNdJexdIuj908G_H49BA3i1jprupgoW5kZk2J5hnHdkSvYFDsRNuL6d1zOpsKnygiftFlGNfAT1vxUUmm5rjg0Ryouc5U1wED2CeSQhapXeJvAYhB5Xqu_Dr1q01WfHoQB5nwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری جالب از دلسی رودریگز،رئیس جمهور کنونی ونزوئلا و معاون پیشین مادورو هنگامی که ترامپ مادورو را جنایت کار نامید و به عملیات دستگیری وی می‌پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148813" target="_blank">📅 21:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148812">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKTE8Nr_LjGnPOEIRQ5Q9EVS7xINGP3h6ZEz-dkFtPt3P5Hyeipr1Ph6yX9vh1fy1nTMkDwsXt2ycJ6xELTnNlHqQBuwYsn5iS4NNKvRLWVVrQOz59T_Xf9biH-txRjghecKasmnEnatcKO-gyXfHSUw6I8cOrlMfIGyBv8fd2rkbx4RRUHdQX6DTrVFOXrIockNxGXKr0c-jcEe-5M2WILdBygDGePJypFO8_YwtrqJnogV668OY33G1He6RSFwcxflwP6F0uko3n5EotN-ERdCVDvFWXfwOu9p4iHPqL5FsAlvv1YxmcxjdK_othc6Y5zDWxZGTxOZIq4n-5a-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قبل از اینکه جایی برای کنکور پول بدی، تحقیق کن!
🔎
پشت پرده کنکور
⚠️
معرفی کلاهبردارهای کنکوری
🎓
ادعاهای «فروش صندلی»
📋
انتخاب رشته
🏫
اخبار تعطیلی مدارس
📚
بررسی مؤسسات و خدمات کنکوری معتبر
🔥
با پشت پرده کنکور؛ قبل از هر تصمیم،
👇
عضو شو: با خبر شو
https://t.me/+2RvDbHy9KPFmNTlk</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/148812" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148811">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a35031cf1.mp4?token=cQaBlMyjOJi5O22AjkDSwb2E0SVKusf4jAfAQp7zWqFIKHpEWFTcQgs96dZV78oHM9M1ao-nOJ2Hc0J0isQ7yRr9Dloh8gFDpZ64I-jUbKFu1fy1kN4QsqUZwKVeUoKnW_rIXK-xgy73Z5zZmMhefmziZUEgUEU12aaWLbeWT7QhuBgP5RX7BgLK_cHL297yV8vdIQgjFAA_23HFc8mqWCcXDrtmHYGqz4DvGe5BgtQb29vHUA4IVIRjI6EdT-l6Tn2ldr47B9EVIa2VXrmmf04xc5iiqMNzFVu4A-I5jtC_KqPUGgSfE2hcI-3421K_jp1PKBlcJ6poObjFNnBx1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a35031cf1.mp4?token=cQaBlMyjOJi5O22AjkDSwb2E0SVKusf4jAfAQp7zWqFIKHpEWFTcQgs96dZV78oHM9M1ao-nOJ2Hc0J0isQ7yRr9Dloh8gFDpZ64I-jUbKFu1fy1kN4QsqUZwKVeUoKnW_rIXK-xgy73Z5zZmMhefmziZUEgUEU12aaWLbeWT7QhuBgP5RX7BgLK_cHL297yV8vdIQgjFAA_23HFc8mqWCcXDrtmHYGqz4DvGe5BgtQb29vHUA4IVIRjI6EdT-l6Tn2ldr47B9EVIa2VXrmmf04xc5iiqMNzFVu4A-I5jtC_KqPUGgSfE2hcI-3421K_jp1PKBlcJ6poObjFNnBx1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به خبرنگاران: از اتاق خارج شوید
🔴
تاکائیچی،نخست‌وزیر ژاپن:
«مایلم موضوعات زیادی را با ترامپ در دستور کار قرار دهم. چرا از خبرنگاران نخواهیم اتاق را ترک کنند؟»
🔴
ترامپ: «خب، خودتان شنیدید که ایشان چه گفتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148811" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148810">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=GVwFJRByMY7Vn0IZLPn2hRNwfaOaW2K2er2j9cr-RCBA3pUgEZiyJRrgtXPCO8VWIP3RaExzxeXKIhwi5TPsZ3jSPdU4GMfQe4zym2g_Tq4hrlGmjhIZIOB692tpQh5ocSRYJmHV83roXQEhMd8y4nGmAX3GOWB_4SmU2OEO-JPZBYUdKD79IHhx5_fwX7uHbfK7cMVAMr4ey1HP6W92SfGKyUUZpJklpJDsjM9pZYYIkTeAf6zc1h8FBebagk4hP3YVqAxdPe8nDzniUOI1nPjWMAPlUD9ni-BoVHovBuVTbh6ADb7NkhuV2DZ15kqESJDRqP6d3-1FxnTPRhZskg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=GVwFJRByMY7Vn0IZLPn2hRNwfaOaW2K2er2j9cr-RCBA3pUgEZiyJRrgtXPCO8VWIP3RaExzxeXKIhwi5TPsZ3jSPdU4GMfQe4zym2g_Tq4hrlGmjhIZIOB692tpQh5ocSRYJmHV83roXQEhMd8y4nGmAX3GOWB_4SmU2OEO-JPZBYUdKD79IHhx5_fwX7uHbfK7cMVAMr4ey1HP6W92SfGKyUUZpJklpJDsjM9pZYYIkTeAf6zc1h8FBebagk4hP3YVqAxdPe8nDzniUOI1nPjWMAPlUD9ni-BoVHovBuVTbh6ADb7NkhuV2DZ15kqESJDRqP6d3-1FxnTPRhZskg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اینستاگردی جولانی حین سخنرانی اردوغان در سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/148810" target="_blank">📅 20:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148809">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تمام پروازهای عمان به ایران و از ایران به عمان از فردا متوقف خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148809" target="_blank">📅 20:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148808">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abebcd591.mp4?token=XKKq4P9BaKySNSNG5O2yXBOiKY1qWEbU6aAyvb_wSmeat3SiXYeHPBhTasEyxWA5maswoeNn8K3xG6ZaehnZ8hDBc4TRNbUEUluLhr8Sdmm-JOUXwXogMXu1ZYNbRhag4HMv6BoJRaWfeIdsnsPQbr0bhbV-xFPoDvElzK0wXagmHHi2A4z-YChOFkFbrGIkpnml360Ha82GRFRkOoZr-pHhc6cIxu6UeQ4dU-99YFgTwi7L71ztFwu8xrPmNlUyxQfvPJt_YUTOAp1Fr-UpqZeFfJ1QPwP4FRH9MPDh1z2u9DuZhe4kEkU6Es0t3WlNH5DEFYBDYDOT46XdtjlDtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abebcd591.mp4?token=XKKq4P9BaKySNSNG5O2yXBOiKY1qWEbU6aAyvb_wSmeat3SiXYeHPBhTasEyxWA5maswoeNn8K3xG6ZaehnZ8hDBc4TRNbUEUluLhr8Sdmm-JOUXwXogMXu1ZYNbRhag4HMv6BoJRaWfeIdsnsPQbr0bhbV-xFPoDvElzK0wXagmHHi2A4z-YChOFkFbrGIkpnml360Ha82GRFRkOoZr-pHhc6cIxu6UeQ4dU-99YFgTwi7L71ztFwu8xrPmNlUyxQfvPJt_YUTOAp1Fr-UpqZeFfJ1QPwP4FRH9MPDh1z2u9DuZhe4kEkU6Es0t3WlNH5DEFYBDYDOT46XdtjlDtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: روابط بین ایالات متحده و بریتانیا گاهی اوقات فراز و نشیب داشته است
🔴
ترامپ: نه، من فکر می‌کنم که این روابط در حال بهبود است. به نظر من، این روابط اکنون بهتر از زمانی است که شما نخست‌وزیر قبلی را داشتید، به این شکل بگویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148808" target="_blank">📅 20:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148807">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1225327.mp4?token=fjQkrHJAdfU8LEX-wfZY6Stdwc-CrQsDauntuokanMo7KG0gb7JSfsB7WVKfwC-HaJyxhxluIyEdfxEaq3i2wcGpbXGo0mPJyPrCnpmP7NcPfBuwhs1Cgkyfyx00ebFmgMahCRD1TfMEoJCx6w0_VHy7eHWo53ERWeeP5rEbO1c6oOEcqZtgr7yQSy6cEntfHsRR6Y0r3scaOQ-zVti7V1b58mZAjc6x-8FDCEJ-D9mn_zr8DLJb6T9IiLJt1XWIque2TvjeWLH9EAHM3OGP0s3a1re4uLjenfnF95No1bNU2p6TYjuLNl3Me7PKVYmjPzCZsAy-ZreSEfk8VnrM4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1225327.mp4?token=fjQkrHJAdfU8LEX-wfZY6Stdwc-CrQsDauntuokanMo7KG0gb7JSfsB7WVKfwC-HaJyxhxluIyEdfxEaq3i2wcGpbXGo0mPJyPrCnpmP7NcPfBuwhs1Cgkyfyx00ebFmgMahCRD1TfMEoJCx6w0_VHy7eHWo53ERWeeP5rEbO1c6oOEcqZtgr7yQSy6cEntfHsRR6Y0r3scaOQ-zVti7V1b58mZAjc6x-8FDCEJ-D9mn_zr8DLJb6T9IiLJt1XWIque2TvjeWLH9EAHM3OGP0s3a1re4uLjenfnF95No1bNU2p6TYjuLNl3Me7PKVYmjPzCZsAy-ZreSEfk8VnrM4oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا شما از توافقی که به موجب آن جزایر چاگوس از بریتانیا به موریتیوس واگذار می‌شود، حمایت می‌کنید؟
🔴
ترامپ: من از آن حمایت نمی‌کنم. فکر می‌کنم این کار فاجعه‌بار است. فکر می‌کنم این کار پوچ و بی‌معنی است. این از نظر استراتژیک بسیار مهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148807" target="_blank">📅 20:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148806">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8088a12a2.mp4?token=CADuterQnzpnh0AxIAMyJYNdqu0uZ2quSVAoV8MM2SmNz3tqTscZb_WXfjIRB4KbNZIVHrPF3oxi-_sleJJFxfDJpi1H7SjAefoZIzMPe-C0Vos3M9fHlcU8Fn1brC3AJYJRW8XLfg_oZYkdiFzvxaLL8yTs0blxz5jdg0G108v8GVpcR1WwOQ4_vgdwO74deow3Y94YJS8YYTh-DmiFPPzeqJJRjok6cYentUjT7E3svSOtjgiSGoObLXNv-KH5PsFGsDhBTh-iTgaDH6VLqXJjBOC6L-IiE1W32l2JUTkub98HKV6EJ_ksl5mMRVU4KBol15xpvCHh-MMxVzLD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8088a12a2.mp4?token=CADuterQnzpnh0AxIAMyJYNdqu0uZ2quSVAoV8MM2SmNz3tqTscZb_WXfjIRB4KbNZIVHrPF3oxi-_sleJJFxfDJpi1H7SjAefoZIzMPe-C0Vos3M9fHlcU8Fn1brC3AJYJRW8XLfg_oZYkdiFzvxaLL8yTs0blxz5jdg0G108v8GVpcR1WwOQ4_vgdwO74deow3Y94YJS8YYTh-DmiFPPzeqJJRjok6cYentUjT7E3svSOtjgiSGoObLXNv-KH5PsFGsDhBTh-iTgaDH6VLqXJjBOC6L-IiE1W32l2JUTkub98HKV6EJ_ksl5mMRVU4KBol15xpvCHh-MMxVzLD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اوایل این ماه، بریتانیا تحریم‌هایی را علیه برخی از سازمان‌های مستقر در کرانه باختری اعمال کرد. نظر شما در مورد این اقدام چیست؟
🔴
ترامپ: من در مورد این اقدام اطلاعی ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148806" target="_blank">📅 20:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148805">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ : به نظر من، ما حق داریم اخبار جعلی را از بین ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148805" target="_blank">📅 20:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148804">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d689b673f.mp4?token=WOwIn8MUW1zGQtF6FVV32L07suANe4QgYKYsG9DscW1hxUMCV65bthOjDkVduOM7CAE9LH1Y22uLu3xGLFBMyVXc-3PhHQJnlwCP21085v2CQxiG5fl1kHDdlK1xbmYzTmz9YhVFP-rZuKkKG2eqYhEx2p7nEq3xf1r9e6-HYXC9KPwDCm4zCXd_W_4VbR6ySTMaB5Qv3Bul4WzAFFfqXKjp80bFqvd1hedJUHxq7AEiKMdLplqI42DdvFHtsS4l_JBVG7FaUiB5DNrePD0D4uS63AUKz0Rmo_wQ6qbXDTe93vTLKPugJ6xKePryo9wsxsEGo8iTgwBeLcBoBb6Iow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d689b673f.mp4?token=WOwIn8MUW1zGQtF6FVV32L07suANe4QgYKYsG9DscW1hxUMCV65bthOjDkVduOM7CAE9LH1Y22uLu3xGLFBMyVXc-3PhHQJnlwCP21085v2CQxiG5fl1kHDdlK1xbmYzTmz9YhVFP-rZuKkKG2eqYhEx2p7nEq3xf1r9e6-HYXC9KPwDCm4zCXd_W_4VbR6ySTMaB5Qv3Bul4WzAFFfqXKjp80bFqvd1hedJUHxq7AEiKMdLplqI42DdvFHtsS4l_JBVG7FaUiB5DNrePD0D4uS63AUKz0Rmo_wQ6qbXDTe93vTLKPugJ6xKePryo9wsxsEGo8iTgwBeLcBoBb6Iow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما نباید اجازه دهیم که آن‌ها به سلاح هسته‌ای دست پیدا کنند. و برای این کار، هزینه‌ای وجود دارد.
🔴
این کار باید توسط روسای جمهور دیگر، یا به طور صریح، کشورهای دیگر انجام می‌شد. برخی از کشورها می‌توانستند وارد عمل شوند، اما واقعاً تعداد کمی از کشورها بودند که می‌توانستند این کار را انجام دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148804" target="_blank">📅 20:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148803">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ خطاب به اندی برنهام: به نظر من، او نخست‌وزیر بسیار خوبی خواهد بود.
🔴
ما تا انتها از شما حمایت می‌کنیم، آقای نخست‌وزیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148803" target="_blank">📅 20:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148802">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «فکر می‌کنم توافقی حاصل خواهد شد.
🔴
آن‌ها حتی امروز هم با ما در حال گفت‌وگو بوده‌اند
🔴
بگذارید بگوییم که این رابطه در حال شکل‌گیری و پیشرفت است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148802" target="_blank">📅 20:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148801">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
هم اکنون گزارش‌ها از شلیک موشک‌ها از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148801" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148800">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
هشدار امیر قطر درباره عبور منطقه از خطرناک‌ترین مراحل تاریخی
🔴
تمیم بن حمد آل ثانی، امیر قطر: منطقه ما هم‌اکنون در حال سپری کردن یکی از خطرناک‌ترین مراحل تاریخی خود است.
🔴
بحران‌های کنونی، حاصل سال‌ها تعلل، بی‌توجهی و تکیه بر راه‌حل‌های غیرواقع‌بینانه است.
🔴
تنها راهکار عملی و مؤثر برای حل اختلافات منطقه‌ای، توسل به گفت‌وگو و مذاکرات سازنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148800" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148799">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
جِی‌دی ونس: رای‌دهندگان بیشتر بر مسائل محلی که اهمیت دارند تمرکز دارند، نه بر جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148799" target="_blank">📅 20:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148798">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804458d4cb.mp4?token=QZoQYcr1I6V3k1niLNL-OKsqFNxh2v2n8lnOmu6m6NUwOitxZ-No9x-vWivsazT_kOWXj8nA1YbCVyFpMxMmqYExEbguYCIr2Wx0u1YQhv7Gi2V1JzxlOXaLGIQBUY91RlhtTMdOFxQxLUsuU-gWj0ZTehJC8t2vCpjJgcq8pEDrrE0UVQhWqhDJjyLja5vrLu04t62VDdrKU9dSgXodo5TwG6OKL2Nc-LbSyrqDfh-WucSFd6xUX07MgMdVjleoeOtTmmmICa5dZ8I1bvhEQSitWR9YrNXtau3tfbpgAVPgB_4MMqNbLJyNfvjzfaKrM0S6xKhvF6vdfvUqj42njQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804458d4cb.mp4?token=QZoQYcr1I6V3k1niLNL-OKsqFNxh2v2n8lnOmu6m6NUwOitxZ-No9x-vWivsazT_kOWXj8nA1YbCVyFpMxMmqYExEbguYCIr2Wx0u1YQhv7Gi2V1JzxlOXaLGIQBUY91RlhtTMdOFxQxLUsuU-gWj0ZTehJC8t2vCpjJgcq8pEDrrE0UVQhWqhDJjyLja5vrLu04t62VDdrKU9dSgXodo5TwG6OKL2Nc-LbSyrqDfh-WucSFd6xUX07MgMdVjleoeOtTmmmICa5dZ8I1bvhEQSitWR9YrNXtau3tfbpgAVPgB_4MMqNbLJyNfvjzfaKrM0S6xKhvF6vdfvUqj42njQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
رأی‌دهندگان بیشتر روی «مسائل محلی و موضوعاتی که مستقیماً برایشان اهمیت دارد» تمرکز دارند، نه جنگ با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148798" target="_blank">📅 20:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148797">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362dd98739.mp4?token=vx1lXJbDO3SByrFwKf_w1lX96yJndG6kpNkirVCnjh69KziUk7T5lrRyz008IZjR6dVibglLGvSfWyF_-2mypN9v9myViULcAQ0QE24kpEJDcYx_HGHYhr9ka7pQtGQkYGojB9NocU6JijO8HRgUvATDZx-12MJ3bum_fSVdRjmedIFTakzQ6NOqkqubk-C1pYw83skh7nRWyZLaX4vccsC4eu06C2_wpq-OM5aqQK99j2LTQ-unwk_TFrch83RTPyfDcnRnb4XQGA_PXdWJmIxNAjAP2bjAwKlv86pMSCxZZ6cd7v9LqTvpiwxmalhjG_AquHHUzVKmJof-_IugZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362dd98739.mp4?token=vx1lXJbDO3SByrFwKf_w1lX96yJndG6kpNkirVCnjh69KziUk7T5lrRyz008IZjR6dVibglLGvSfWyF_-2mypN9v9myViULcAQ0QE24kpEJDcYx_HGHYhr9ka7pQtGQkYGojB9NocU6JijO8HRgUvATDZx-12MJ3bum_fSVdRjmedIFTakzQ6NOqkqubk-C1pYw83skh7nRWyZLaX4vccsC4eu06C2_wpq-OM5aqQK99j2LTQ-unwk_TFrch83RTPyfDcnRnb4XQGA_PXdWJmIxNAjAP2bjAwKlv86pMSCxZZ6cd7v9LqTvpiwxmalhjG_AquHHUzVKmJof-_IugZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
توی یادداشت‌هام نوشته شده که باید به سؤال‌های خبرنگارهای سی‌ان‌ان و پولیتیکو جواب بدم.
🔴
کسی از سی‌ان‌ان یا پولیتیکو اینجاست؟
🔴
نه؟ خب، باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148797" target="_blank">📅 20:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148796">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb233d3023.mp4?token=KsDh6hK8zRF08QLNNbpnobwOpQ5Jiwvxps8WoxiRe38ujU4he7FUIMD-V5sV1TBkR5Ng3DoGi8xeuYPeyhoS-mwUssIv89ZHyYu3GOd-bZbo-zarVE_nifbZ2QUCZvdi-OX_8aBlYRf_Ot7f07I7qUXRZUbKp9LKQbGzptQXoKhy1cC18Jm3Wc7MTqv5Abw_XAxz42Q57BRgQwBuVWwyXaTPldOs8Q1jTc8slu_NZVWlGmo0nkMGGPUW9oI3_bJS9lRtTwMJ6y5CHeXIeCY1d4EZ8WYXJKVxrlnl6QMb7evuhCjcTyyBimfzsTZJSaU4jK4Q_0-pvWs2ZBcHIdckGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb233d3023.mp4?token=KsDh6hK8zRF08QLNNbpnobwOpQ5Jiwvxps8WoxiRe38ujU4he7FUIMD-V5sV1TBkR5Ng3DoGi8xeuYPeyhoS-mwUssIv89ZHyYu3GOd-bZbo-zarVE_nifbZ2QUCZvdi-OX_8aBlYRf_Ot7f07I7qUXRZUbKp9LKQbGzptQXoKhy1cC18Jm3Wc7MTqv5Abw_XAxz42Q57BRgQwBuVWwyXaTPldOs8Q1jTc8slu_NZVWlGmo0nkMGGPUW9oI3_bJS9lRtTwMJ6y5CHeXIeCY1d4EZ8WYXJKVxrlnl6QMb7evuhCjcTyyBimfzsTZJSaU4jK4Q_0-pvWs2ZBcHIdckGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توافق ترامپ با دانمارک و گرینلند
‏
🔴
آمریکا و دانمارک توافق‌نامه‌ای بدون تاریخ انقضا درباره گرینلند امضا کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148796" target="_blank">📅 20:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148795">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
مارک روبیو وزیر امور خارجه آمریکا: تا این لحظه هیچ دیداری با مقامات ایرانی برنامه‌ریزی نشده است، اما این وضعیت ممکن است تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148795" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148794">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترکیه همه پروازها به ایران و از ایران را تا مارس ۲۰۲۷ لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148794" target="_blank">📅 19:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148793">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
آکسیوس: تا ساعاتی دیگر جلسه ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148793" target="_blank">📅 19:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148792">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe6c4280f.mp4?token=iJo0e7dV7Eir-qCf-PqL409uGpe2lIYMrzGNhMkHhO7JJqxdV4hGJ_1nitQV2dWWd3plhwJpDt9yX-cHFmBzpKsaOktQp-G7bMfHNWsnu-Rw2f8yzScT1GZRSWQR7ClMTWkFNSKg2niumUYYl1n2kECyBx1jC-6KmkP-4Zczd-zZjSR8z4mBcMB7Akij73kZgqJyEPBrmbVKQxRBzvlb00w6fVYCdviwxjgrIuCs_1ZcVptTMY-93CT34UAU6iXR3rDimAimAzKaCvwEZk7-DUKWQv_gOU2fG44qdh1DAHt4HCbgCfl2FAnZcyh0rSiGRqDRGJW_EVTtCZAvSZDwXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe6c4280f.mp4?token=iJo0e7dV7Eir-qCf-PqL409uGpe2lIYMrzGNhMkHhO7JJqxdV4hGJ_1nitQV2dWWd3plhwJpDt9yX-cHFmBzpKsaOktQp-G7bMfHNWsnu-Rw2f8yzScT1GZRSWQR7ClMTWkFNSKg2niumUYYl1n2kECyBx1jC-6KmkP-4Zczd-zZjSR8z4mBcMB7Akij73kZgqJyEPBrmbVKQxRBzvlb00w6fVYCdviwxjgrIuCs_1ZcVptTMY-93CT34UAU6iXR3rDimAimAzKaCvwEZk7-DUKWQv_gOU2fG44qdh1DAHt4HCbgCfl2FAnZcyh0rSiGRqDRGJW_EVTtCZAvSZDwXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیئت اسرائیلی در جریان سخنرانی اردوغان، رئیس‌جمهور ترکیه در مجمع عمومی سازمان ملل، سالن را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148792" target="_blank">📅 19:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148791">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlPkFLzCPbh8Yl3tr0ncWqfxaIL8fFSJKBv-ENethQW7WCeIhsLQREklIZqKD6L0qg-mbCp2K2J0Mc2HrCTPsdktbf86_W_geF5kO2shOr6MkXWZsVSR5stTqXZHBQdpL9TerUgQF3exVi0Th1TH82UF3Lc_HSZALTaXZ2hcVMFKmpHmobiT_w-skuumcKLHAqlGFVk6gbwTQp7tVeDa6Ba3oYiXK71331oQImZd2voRnGqCozrwQmmn_JuWUNYogbg9Ovt9Fzb-E8ileDzkNJ6cMC9RnHuAMsHVZ5sYetWxCLeiosJPg7jD93oMJ3zowhPhSMiK0vzPquJ0-oK4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عراقچی و کایا کالاس مسئول سیاست خارجی اتحادیه اروپا در حاشیه هشتاد و‌یکمین نشست مجمع عمومی سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148791" target="_blank">📅 19:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148790">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/imN9Wu4nKmTHN93ZCo71UBadCN2Y_ohrdnJp3DbgEo2KuNrSzmoWI78m2NSqGHxMRmQaHQVYysK-7qQVbyuurJI_fcnja4BZQO5bafGhRjtKNyexiuP3fOePX8z7NQUdfJdGz7EZZ5o5abkeIHouenP-mj4VoJLlU1yHRi96o8tecURA0QFMKKQioX_h0vzBN5Ie_-IefMj_0j1_zg_-GD5E7_gW1zNmippezKUqDXzbh0cxC4hUoFHepRUpYuohaNW4-336WUq1izbPnMtSevNbYWeEkBZsC0CRXCyoO5sr_G21sCw1thtd_OpAwR8Bj3_xg_r2LDUWt2AVu3HSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی هم برای دیدار با نمایندگان کشورهای حاضر در نشست سازمان ملل وارد نیویورک شد.
🔴
در یه اتفاق عجیب، ترامپ، نتانیاهو، پزشکیان و رضا پهلوی همزمان توی نیویورک هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/148790" target="_blank">📅 19:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148789">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
عربستان، مصر، پاکستان و ترکیه:
تفاهم‌نامه اسلام‌آباد، تنها مسیر دستیابی به صلح پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148789" target="_blank">📅 19:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148788">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgwgMysO-lGgtFtoUrxRMR_4h0-pAnBmeIvXdm0kNQ5ZcBe0VPRGDUNWUb5IduEZgXOEufbFHQE9MAgjH5BxPfxI-l9NmFD2hOT_lSe01KrSxic7418sWfQ5C3qBnQ7HQOQatEY19qdp4qZmem3JpD-iHRheitCyiePTsmQAkdhwyvoZLeCWS07sQP3ExsWaRNUoiw_K137D9oVMagnd3ZEjcuo68zd6E-ZCZEWSSQci9VRzVJ3CxKagSqkxVwFfFG8KQ-dzEc-QD-bTFyoA5t--q64v-4eMHTkDfm8eAPNII8_T0abMK3l2Qo63hrQfT4OM6h-SpJ3yBIxUUrQjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حین سخنرانی ترامپ، هیئت ایرانی سالن را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148788" target="_blank">📅 19:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148787">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزیر خارجه سوئیس پس از دیدار با عراقچی: آماده تسهیل راه‌حل دیپلماتیک هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148787" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148786">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12949eaa58.mp4?token=mxfy3vDAle1UL2FUyAgQ_2HnMWBAEo1FYAqE4irKrN7UpsVs3HCrZoPAQmvaSNfn-c1IiU_-9scSuPqwJOeSbtUx6qZ9ACL9mUcC-WrdYuR0tkxNIk9MRIVjuyA3di9dFqHvWsePAy40eQA-8uHjGOcyN8j3c7WkFmaTn-xuHrVk8LmHOBtxU1Mx9SlfOrXyCr2_BEPemoYtziNP5378EHwuE2sg3GDQfP10em9iBeBVSwWCDc1GBMwkcgX2Eb9kQRRD0mvnrQDI2wJQpDdxcMystSlxBXLdxIH-bCvJAEUq-1m6_kI-xez7XaPnyTYEE_Kyd5kPju4JEo2Iqt-n8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12949eaa58.mp4?token=mxfy3vDAle1UL2FUyAgQ_2HnMWBAEo1FYAqE4irKrN7UpsVs3HCrZoPAQmvaSNfn-c1IiU_-9scSuPqwJOeSbtUx6qZ9ACL9mUcC-WrdYuR0tkxNIk9MRIVjuyA3di9dFqHvWsePAy40eQA-8uHjGOcyN8j3c7WkFmaTn-xuHrVk8LmHOBtxU1Mx9SlfOrXyCr2_BEPemoYtziNP5378EHwuE2sg3GDQfP10em9iBeBVSwWCDc1GBMwkcgX2Eb9kQRRD0mvnrQDI2wJQpDdxcMystSlxBXLdxIH-bCvJAEUq-1m6_kI-xez7XaPnyTYEE_Kyd5kPju4JEo2Iqt-n8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جمعیت ایرانیان برای رد شدن از مرز زمینی رازی.
🔴
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148786" target="_blank">📅 19:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148785">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b140f553.mp4?token=uiRm6pYKb58qHjcxPGV7EnvY60dGm2F1qWHo-SZqkj8NGDm85kmLbB_hkSn8U-BeD2ZMvdpHsJy6kdYoHADvyqfxFT91MFQ_OIk7HhxOXhlM0AlwM144GAYHOsipDpjsLWsyhAmXNzvYlnq0-ceVu3ggbuddHjwzOu2OKPrmabJnCphwPug2ZwESfMpT1UOAJX22Ub53z8Zfio5P9KCGpYlsgRLMeWRvho4mracYoGHCQd9B7EBRrpvHIkePW_KzQRlsHzp8pSmMIzAf_zSjrRh2TwgovkfVgigRZuZ3okgLZTPIvow2C0nBlE78Ccf3l7ZcQM3Qk_Nqv7KzfZqTIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b140f553.mp4?token=uiRm6pYKb58qHjcxPGV7EnvY60dGm2F1qWHo-SZqkj8NGDm85kmLbB_hkSn8U-BeD2ZMvdpHsJy6kdYoHADvyqfxFT91MFQ_OIk7HhxOXhlM0AlwM144GAYHOsipDpjsLWsyhAmXNzvYlnq0-ceVu3ggbuddHjwzOu2OKPrmabJnCphwPug2ZwESfMpT1UOAJX22Ub53z8Zfio5P9KCGpYlsgRLMeWRvho4mracYoGHCQd9B7EBRrpvHIkePW_KzQRlsHzp8pSmMIzAf_zSjrRh2TwgovkfVgigRZuZ3okgLZTPIvow2C0nBlE78Ccf3l7ZcQM3Qk_Nqv7KzfZqTIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏
ترامپ در پایان سخنرانی‌اش در مجمع عمومی سازمان ملل:
🔴
با همکاری یکدیگر، آینده‌ای برای مردم جهان خواهیم ساخت که از همیشه روشن‌تر، امیدوارکننده‌تر و باشکوه‌تر باشد.
🔴
خداوند ملت‌های جهان و آمریکا را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/148785" target="_blank">📅 19:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148784">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423b258014.mp4?token=UbJXzznJc0u4kUWe705Xlk-4w0XZuIJ6Z7GD6GOCtGAb556RqoXTA2HPrY1Ix8_8lzojZ_OMC3pY-7uT2KvylKkkornyoB7eDxcsqXzWJG1iuVICsUxUMHM6lb4IrUx5V1_TB_SrN6ANba6vJ0m_mYstGid_x2j6sKlnJzlGKxy6mOlA7a2z1i-Hl57CGKIjp-RidlozLIq59JzXI7CXR9RueG8fwe3yUutcTzWVojEgZ_Os7n3dpppxxtkMGifsemBver5Zcx4n-WYfzevltumgQIEeG0g0NiScbZj-KJoR6nO0cfnBpaQkntUNWUU_mqJV5sLmLzHPhoB0d-6NnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423b258014.mp4?token=UbJXzznJc0u4kUWe705Xlk-4w0XZuIJ6Z7GD6GOCtGAb556RqoXTA2HPrY1Ix8_8lzojZ_OMC3pY-7uT2KvylKkkornyoB7eDxcsqXzWJG1iuVICsUxUMHM6lb4IrUx5V1_TB_SrN6ANba6vJ0m_mYstGid_x2j6sKlnJzlGKxy6mOlA7a2z1i-Hl57CGKIjp-RidlozLIq59JzXI7CXR9RueG8fwe3yUutcTzWVojEgZ_Os7n3dpppxxtkMGifsemBver5Zcx4n-WYfzevltumgQIEeG0g0NiScbZj-KJoR6nO0cfnBpaQkntUNWUU_mqJV5sLmLzHPhoB0d-6NnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۲۵ سال بعد از ۱۱ سپتامبر یکی از فرماندهان میدانی القائده اتو کشیده، سوار بر کادیلاک و با گارد حفاظتی وارد نیویورک شد. زندگی همین قدر می‌تونه عجیب باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148784" target="_blank">📅 19:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148783">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
👈
ساعاتی پیش 12 فروند جنگنده f16 آمریکایی به همراه 3 هواپیمای سوخت رسان از آلمان به سمت خاورمیانه حرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/148783" target="_blank">📅 18:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148782">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: حکومت کوبا سقوط خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148782" target="_blank">📅 18:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148781">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏
👈
ترامپ:
زنمم تو سالنه، کوشی خانم؟ کجایی؟ اون فوق العادست عالیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148781" target="_blank">📅 18:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=HisO0OhqTQ-gAlASIslOVoeqJnno_P5yDNNSoVfhVGbEbCMVYJ9JBuWImP4WAI7p1P0fFFkQX_keNWkIyYn7Um9JX7kONEJCorqe3ptqwt0SYhm_sdh7zKEn1K05JNW_c5-0TlskG9cYF3NMxghaQbidkr3BYsXjMZI6NSSV7FqkwGU5F4KlNgMTvyuT0G5YLmPMD3qYaX-iTqyo7eVi2rrIpJVyl8n7st1Xz6294LNtZxE1_Vjim-G6-1RO9YCg8-dy2OjEvPGTBRZsaKujJOrhvxVNK5rC5HITIDxX_GYMhK8JOpGypt7f-Hn1vnNzhbgx3cVzoWdS6UrA2Qy8_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=HisO0OhqTQ-gAlASIslOVoeqJnno_P5yDNNSoVfhVGbEbCMVYJ9JBuWImP4WAI7p1P0fFFkQX_keNWkIyYn7Um9JX7kONEJCorqe3ptqwt0SYhm_sdh7zKEn1K05JNW_c5-0TlskG9cYF3NMxghaQbidkr3BYsXjMZI6NSSV7FqkwGU5F4KlNgMTvyuT0G5YLmPMD3qYaX-iTqyo7eVi2rrIpJVyl8n7st1Xz6294LNtZxE1_Vjim-G6-1RO9YCg8-dy2OjEvPGTBRZsaKujJOrhvxVNK5rC5HITIDxX_GYMhK8JOpGypt7f-Hn1vnNzhbgx3cVzoWdS6UrA2Qy8_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
🔴
دونالد ترامپ درباره ایران گفت: «آمریکا و ایران قطعاً این مسئله را حل خواهند کرد؛ به هر طریقی که باشد، این کار انجام خواهد شد.»
🔴
او افزود: «این اتفاق سریع رخ خواهد داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148780" target="_blank">📅 18:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee7ed8073.mp4?token=h9vL7o4BDJ3_b0l5DkaxhGIdxB3hffL1yZSyecQ6rPjgYbEwY82M_8sAMatKZWgx216dbS_nMNNNlULTMDYCF8mZ66Xgky-HHFuoXAodGmVxJEhhX5BHUG70med-8-THne5QCjc7KUIo7CoLKzo3M7jyYEgkGc88flBpCjjsR_oAvwzUKPadheFNVS-7NQcJTrhe6LhNyIFvIS18S2WCtWoK7NqeyNkvtXHgmqR_JZgkzciKEt482w2K0cvDGsERIIkYcOSH1xLtdqS4JQx_6P3B5BZb7kBcP24bFe6vTIFfxMnyrAL1oIL2eYsOl-4ApzUuKAUVMymnfcwq7gDmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee7ed8073.mp4?token=h9vL7o4BDJ3_b0l5DkaxhGIdxB3hffL1yZSyecQ6rPjgYbEwY82M_8sAMatKZWgx216dbS_nMNNNlULTMDYCF8mZ66Xgky-HHFuoXAodGmVxJEhhX5BHUG70med-8-THne5QCjc7KUIo7CoLKzo3M7jyYEgkGc88flBpCjjsR_oAvwzUKPadheFNVS-7NQcJTrhe6LhNyIFvIS18S2WCtWoK7NqeyNkvtXHgmqR_JZgkzciKEt482w2K0cvDGsERIIkYcOSH1xLtdqS4JQx_6P3B5BZb7kBcP24bFe6vTIFfxMnyrAL1oIL2eYsOl-4ApzUuKAUVMymnfcwq7gDmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: جنگ اوکراین زودتر از آنچه مردم تصور می‌کنند پایان خواهد یافت
🔴
دونالد ترامپ درباره جنگ اوکراین گفت: «ما همکاری بسیار نزدیکی با رهبران روسیه و اوکراین داریم و این مسئله را حل خواهیم کرد.»
🔴
او افزود: «فکر می‌کنم این اتفاق سریع‌تر از آنچه مردم تصور می‌کنند رخ خواهد داد؛ آن‌ها دیگر از این جنگ خسته شده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148779" target="_blank">📅 18:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ: بزدلان و خائنان دوست دارند بگویند ایالات متحده با کمبود مهمات مواجه است، اما چنین چیزی درست نیست.
🔴
ما بیش از آن مقدار مهماتی داریم که حتی بتوانیم تصور کنیم ممکن است از آن استفاده کنیم و در حال تولید مهمات با سطوحی هستیم که هرگز پیش از این تجربه نکرده‌ایم. ما ذخایر خود را سریع‌تر از هر زمان دیگری افزایش می‌دهیم؛ مهمات و تجهیزات درجه‌یک.
🔴
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. در حال حاضر ۱۸ کارخانه توسط بزرگ‌ترین شرکت‌های صنایع دفاعی جهان در حال ساخت است؛ ۱۸ کارخانه در دست احداث است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/148778" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی تروریست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/148777" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148776">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=aZblgDWILJyHybee_eGaCMiW0F0UsplJJr6zx38OUIT0PRWwslD6b-u6GRGUJd-z3GLRiPdGy-Dqcy-XGjZ_t_Y-oqd-FIE2XLuGVeok_CHoYFxKppXlPoRJMI1G7A1pI8X0Usy0NcHzlASXs5ngNUVtO47czG80bhX5zfCRfrYHj2_mQrtY4mNBQYjm_Id7dfJZ90LgZeK9i3Zmb4SwmktEWF-OYkUCKpdWMXPoaVImZWIE6qNBllg8kyXW7EhJ0dLyLNKpMI2WO9a8g6naadN8iVeOysCfM3stAg9MycNn0cpSdjdlJb0lxzOHfwzi-DoMlA7GdOIEoFBjNjOXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=aZblgDWILJyHybee_eGaCMiW0F0UsplJJr6zx38OUIT0PRWwslD6b-u6GRGUJd-z3GLRiPdGy-Dqcy-XGjZ_t_Y-oqd-FIE2XLuGVeok_CHoYFxKppXlPoRJMI1G7A1pI8X0Usy0NcHzlASXs5ngNUVtO47czG80bhX5zfCRfrYHj2_mQrtY4mNBQYjm_Id7dfJZ90LgZeK9i3Zmb4SwmktEWF-OYkUCKpdWMXPoaVImZWIE6qNBllg8kyXW7EhJ0dLyLNKpMI2WO9a8g6naadN8iVeOysCfM3stAg9MycNn0cpSdjdlJb0lxzOHfwzi-DoMlA7GdOIEoFBjNjOXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد
🔴
دونالد ترامپ درباره ایران گفت: «برای انتخابات، در ارتباط با ایران، مطلقاً هیچ اهمیتی قائل نشده‌ام و نخواهم شد؛ حتی به ذهنم هم خطور نمی‌کند.»
🔴
او افزود: «تنها چیزی که برای من اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/148776" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148775">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: رهبر ایران(اسبق) کشتار زن و بچه یهودیان در ۷اکتبر را تبریک گفته بود او تروریست بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/148775" target="_blank">📅 18:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: من از تمام کشور های جهان میخواهم که به جنگ اقتصادی تمام عیار آمریکا علیه ایران بپیوندند تا زمانی که ایران برنامه هسته ای خود و حمایت از شبه نظامیان را کنار بگذارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/148774" target="_blank">📅 18:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148773">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e99476e.mp4?token=q8-R3vQVaPdWihNSFVEAUqj8W7L-otVgG2Y331i9I0jI2pz-tf_vu_FvsbTy4yW98cxqIs4yary6Egc3itHvFEteZkJrQXTsdJEPTaAc5WHOAvM_Ou6CB6J0GAvi8NZZ_JNnxlAevLoqfvMRkreIDN50-nmwhPYxaorGELAGJihek3-BIEQYccwXDvtwfWyF75Y8GDn7jFhJRVdtNVsp-df0BCrt2gwy1zpv37NLrrJ5w-UeH--ZccCDeTZFoo4tRnSp9tPpGL-N4yRGLM__GDz5SR0muzPF-8nxvD5FYfTTo7CWUNPnF7-PYlIEYf5A-HLqGkdRSIWlXzddMbM6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e99476e.mp4?token=q8-R3vQVaPdWihNSFVEAUqj8W7L-otVgG2Y331i9I0jI2pz-tf_vu_FvsbTy4yW98cxqIs4yary6Egc3itHvFEteZkJrQXTsdJEPTaAc5WHOAvM_Ou6CB6J0GAvi8NZZ_JNnxlAevLoqfvMRkreIDN50-nmwhPYxaorGELAGJihek3-BIEQYccwXDvtwfWyF75Y8GDn7jFhJRVdtNVsp-df0BCrt2gwy1zpv37NLrrJ5w-UeH--ZccCDeTZFoo4tRnSp9tPpGL-N4yRGLM__GDz5SR0muzPF-8nxvD5FYfTTo7CWUNPnF7-PYlIEYf5A-HLqGkdRSIWlXzddMbM6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران ۷۲هزار شهروند معترض بی گناه خود را به قتل رسانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/148773" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🔴
فوری/ترامپ در سازمان ملل:
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
🔴
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/148772" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: جمهوری اسلامی معترضان را میکُشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/148770" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: به مدت ۵۱ سال، حکومت افراطی ایران با خونریزی و کشتار گسترده حکومت کرده و در سراسر خاورمیانه و فراتر از آن، مرگ، ویرانی و هرج‌ومرج به راه انداخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/148769" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=JCDmrQAVOSBQOaN1YzPbPPVgkOmBkI10jhWwmX0ChGEyYlQgagcH5k9OL-G-0gRBsrVU95vkrnpSnUgHIfpU_5TNSMyEUYl8JuXd38lDMPHvEQlhw23953ufdWUfpemSXzQxWrAC7AfKAz5XHEh7A7anGZT0Hu6XmLj_1sl95Zm5HaKWTgsuXgqKwDxZlA3MD2XWndg_F796MurIKrz07h_DmPeBltUYaMS1uONHcUeFHRzg1MROQM5887EaBd0BDxTIL-GnKQHH_Ci-0IbkTPI6Ui79NAyN73Zvo3YtSSABYJ1cC4W_cz2DizI2TmPApL-UJVhggEyjZiVf1VRtYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=JCDmrQAVOSBQOaN1YzPbPPVgkOmBkI10jhWwmX0ChGEyYlQgagcH5k9OL-G-0gRBsrVU95vkrnpSnUgHIfpU_5TNSMyEUYl8JuXd38lDMPHvEQlhw23953ufdWUfpemSXzQxWrAC7AfKAz5XHEh7A7anGZT0Hu6XmLj_1sl95Zm5HaKWTgsuXgqKwDxZlA3MD2XWndg_F796MurIKrz07h_DmPeBltUYaMS1uONHcUeFHRzg1MROQM5887EaBd0BDxTIL-GnKQHH_Ci-0IbkTPI6Ui79NAyN73Zvo3YtSSABYJ1cC4W_cz2DizI2TmPApL-UJVhggEyjZiVf1VRtYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
🔴
دونالد ترامپ درباره ایران گفت: «آن‌ها موشکی ساخته بودند که قادر بود اروپا را هدف قرار دهد و به آن بسیار افتخار می‌کردند؛ امیدوارم اروپایی‌ها این موضوع را درک کنند.»
🔴
«هدف ایران این بود که در پشت سپر موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.»
🔴
ترامپ افزود: «اگر آن‌ها موفق می‌شدند، این حکومت می‌توانست بدون محدودیت به گسترش ترور و مرگ ادامه دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148768" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=X43mfrde7DNStszNIgAc44x17FuVfucgeYTgaoAmrMaXKab78zLm3Z8AH14Gkj_VyX21FchcuC7OwH-G8ZHxJJMYbZM2NYx6b2lodJtirnwCqt7hIsxR9UZv9Kvp9DpAG4EIrj43Bavem6qo1URRuIW_XehiEJFjIbOhpvXmXxaxSRrNDYmFSJmSl0-sOtkSBdY-6seJkUhUyrDlcUT7whEAhImF5RGoEP6uzWJhmdAhE6LM2f8zI2cFqDVcDJfYkIM_BUbwtk4joV5nLK3iFEjiWbT5qf02Fg1XV4PM8R08WHWc_74wwljD67ATIFUyrqcw6L3QM5UM2mlDRVaZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=X43mfrde7DNStszNIgAc44x17FuVfucgeYTgaoAmrMaXKab78zLm3Z8AH14Gkj_VyX21FchcuC7OwH-G8ZHxJJMYbZM2NYx6b2lodJtirnwCqt7hIsxR9UZv9Kvp9DpAG4EIrj43Bavem6qo1URRuIW_XehiEJFjIbOhpvXmXxaxSRrNDYmFSJmSl0-sOtkSBdY-6seJkUhUyrDlcUT7whEAhImF5RGoEP6uzWJhmdAhE6LM2f8zI2cFqDVcDJfYkIM_BUbwtk4joV5nLK3iFEjiWbT5qf02Fg1XV4PM8R08WHWc_74wwljD67ATIFUyrqcw6L3QM5UM2mlDRVaZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
🔴
دونالد ترامپ درباره ایران گفت: «پس از آغاز به کارم در سال گذشته، مذاکرات با ایران را آغاز کردم و در ازای پایان دادن به برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی را به آن‌ها پیشنهاد دادم.»
🔴
او افزود: «اما آن‌ها این پیشنهاد را رد کردند؛ این یک اشتباه بزرگ بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/148767" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد
🔴
دونالد ترامپ درباره ایران گفت: «آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.»
🔴
او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/148766" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=TMn7_fDkysYTjP4b-4DNdO_L9x1zqRYVPdr57X8DSfb2TpOQwdKnTDCbkXhMFoZfYyDCX3DIY-6PKGunIBACD2qxnEd-r1yEYvnXdayYJUMy0U_CGJOJt_XqewZqA-vZySF9J--uxo8i-XRkCE7CPsmXlbGpUCLb7jDHNjoF4ECDKDAltTDnsMC8GTZY5jnkhEXB561-PTstdIUEWpd2ug0XUpDsA4cS_p5nQNhBxTjjvowZmI2r0et_6PmeoLsn-6o1XsbRgUWoZ5disXLZ6JHykXAmJ6JEZHrgb1CQ5n__0fle4WGHFGslMe-0DWKHORlfKN2pGs8r_8EeMST2lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=TMn7_fDkysYTjP4b-4DNdO_L9x1zqRYVPdr57X8DSfb2TpOQwdKnTDCbkXhMFoZfYyDCX3DIY-6PKGunIBACD2qxnEd-r1yEYvnXdayYJUMy0U_CGJOJt_XqewZqA-vZySF9J--uxo8i-XRkCE7CPsmXlbGpUCLb7jDHNjoF4ECDKDAltTDnsMC8GTZY5jnkhEXB561-PTstdIUEWpd2ug0XUpDsA4cS_p5nQNhBxTjjvowZmI2r0et_6PmeoLsn-6o1XsbRgUWoZ5disXLZ6JHykXAmJ6JEZHrgb1CQ5n__0fle4WGHFGslMe-0DWKHORlfKN2pGs8r_8EeMST2lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران دیگر قلدر خاورمیانه نیست؛ هرگز اجازه دستیابی به سلاح هسته‌ای را نخواهم داد
🔴
دونالد ترامپ درباره ایران گفت: «آن‌ها قلدر خاورمیانه بودند، اما دیگر قلدر نیستند.»
🔴
او افزود: «از نخستین روزی که وارد عرصه سیاست شدم، موضع من تغییر نکرده است؛ هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148765" target="_blank">📅 18:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
پیام مجتبی به دانش آموزان: تقوا داسته باشید تا قله‌ها رو فتح کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/148764" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBrG8VzrXWMdyycLn8VLo-FlAIXOelPC1chs4-W8COPSMA-2yA0thgCMp3cNfVJoV5c4BUPDlOsRjlWrIKrQw8_ZuzOtXVoItUzp7qPmcVFL9IhKpbj3L89P1LooCbkZrvUhWw_ma4pkjvXrBaK3csAutOPsVdwi5LosOf8R2GBuKtHB093KjG5YKsvq7xvZhXZ7x77KAha90diMNjhVYxMipp8cgdfI-9MhYX44uByTK3SssqY5kbmyWW8dKNAl4KxKOCcl1HpQzBOovFgHa1jDuMvYgFHgdNpMb1kqAx7vNcT6qJPJC3oZQbj1PX-h-wJk-P4HXHp70KqkhPu_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف :
ترامپ در حال بررسی گزینه‌های مختلف درباره ایرانه؛ از مذاکره و  تشدید حملات و افزایش فشار اقتصادی گرفته تا حتی «منفجر کردن کل ملت ایران»!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148763" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری/هم اکنون پس از شرکت‌های ترکیه و عراق، شرکت های هواپیمایی امارات و قطر نیز پرواز های خود به ایران را متوقف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148762" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjZi8bbkbOMH9PKQecwognsBlY8_h_KHDjrwY6LzGyl_umXx6MatT88-DY4u0DqVvMjpiin3tJIIBs2hQGPzKhaWiFe-OO_stfyfJLUEFKdzRRDMh0tPEo_56Y4UJRrAftamn9dt1TWWVGWytBrNGg70dKXQy-LpApDPPGnlpPVX8owr7NUkbP6Pf1CoOQdNVeEp1vBdHBpoywSw_eXCDMBuzyTgTrCl1U5wLE9-_I4Q6LMxwAVVkM0yGPE3vdGz2n4H9_w5RSvcupG78KjQDEdMjIurJhF3VcDjytocPIuGu5-HTfe25hFzLHoQCBuudHwgNBwghFdAw5EPs4YPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJkPPJOp4fkAEXlqyPHsOV9yDSkjQZNaCo_dBXn1HZtae_Hh8mA_LCpkdDFGIRfXAoX6LqWLd2FMqECN1p7UWb4wxOGEFb9TCYA-JNW-MhG949kryUTBUaSCoeUsEwV5j4WhE4dHYm0T-rl0idD2Ri51fTlNimZBoKwoLhv1N-EGpJmY2-ax6v07lDBcA3apfMAOUVOvREuQi79NsuEPPf6l604Bs42oT6D3xJb54CX_IiO1g0wJBKyGwnJSly6VeguflU_cKAQ0H35UVEfY6wGhc9wZp52Uw2f05CKdwLGtCRYd8a7UW4dktVEHei2YF4Dm1jJNC9P-f8IffXNv4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عرازشه:
پزشکیان باید ترامپ رو به قتل برسونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148760" target="_blank">📅 17:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148759">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
طبق گفته اکسیوس، ترامپ قرار است در سخنرانی خود در مجمع عمومی سازمان ملل این ها را بگوید
:
در آمریکا، به‌تازگی بیست‌وپنجمین سالگرد هولناک‌ترین حمله تروریستی تاریخ را پشت سر گذاشتیم؛ حملات ۱۱ سپتامبر که در آن حدود ۳ هزار نفر، تنها چند کیلومتر دورتر از اینجا، کشته شدند.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های مورد حمایت مالی ایران، ۱۲۰۰ غیرنظامی بی‌گناه، از جمله ده‌ها آمریکایی، را شکنجه کردند، به اجسادشان آسیب رساندند و کشتند.
رهبر جمهوری اسلامی ایران این کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
همین حکومت امسال بیش از ۷۲ هزار نفر از شهروندان خودش را به قتل رسانده است.
فقط تصور کنید اگر چنین حکومت نفرت‌انگیزی می‌توانست در حالی که زیر چتر هسته‌ای قرار دارد، حملات تروریستی گسترده‌ای انجام دهد، چه وضعیتی به وجود می‌آمد.
این همان واقعیتی بود که ما مجبور شدیم با آن روبه‌رو شویم؛ واقعیتی که بسیاری ترجیح می‌دادند نادیده بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148759" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148758">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=a6SLyd8-W-Fd3PfQeJwqlIeeSLaqy86ZhsQkco0DSSmcje5as0MBATzKNgF-asMku2fcoeMBLLY2_h-SeKsTD_MdxnHE-abGQHQYx6FGoyxDRmElQ89UQboqU4d9SZyHAG08XEBy5v3VtyA0xS0t6TdYkrKLnvWdUuYVitDlfRUcTXHd7ui06VaL9IsP-Wlz4J0X12VTdV73SvUTHnmEXYkc7cPFfdi-AuE9ejbPfazPp1IWs0Od5JX-GfZbDVnVheGTCZ-SO1hvm7jghnG8sfk4gb9KliwvXu-YyX6IhMKXfijBp5BMCDlkxI6eAAOzDs4OE_Q-qCJm0qz0R0wNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=a6SLyd8-W-Fd3PfQeJwqlIeeSLaqy86ZhsQkco0DSSmcje5as0MBATzKNgF-asMku2fcoeMBLLY2_h-SeKsTD_MdxnHE-abGQHQYx6FGoyxDRmElQ89UQboqU4d9SZyHAG08XEBy5v3VtyA0xS0t6TdYkrKLnvWdUuYVitDlfRUcTXHd7ui06VaL9IsP-Wlz4J0X12VTdV73SvUTHnmEXYkc7cPFfdi-AuE9ejbPfazPp1IWs0Od5JX-GfZbDVnVheGTCZ-SO1hvm7jghnG8sfk4gb9KliwvXu-YyX6IhMKXfijBp5BMCDlkxI6eAAOzDs4OE_Q-qCJm0qz0R0wNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ هنگام ورود به مجمع عمومی سازمان ملل خطاب به سی‌ان‌ان:
🔴
تعجب می‌کنم که سی‌ان‌ان اینجاست و اخبار مربوط به مرا پوشش می‌دهد. شما نباید اینجا باشید.
🔴
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مرا پوشش دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148758" target="_blank">📅 17:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCuZnlQr4093-Zfzs5SC_hi-8RWxdL9ccW36856Cc32S98QhzZuPmbMuoFOb2enfja8Um3BiX4mc7ZQzBG_gGe-VMAbQGBd03y_UqyvgnONsN9oUipHI11qdozuzKo7Xzn-rzQpdLbGWbciUkPX1MZ8ymbOKwyP-kboy7Ttb3wGaEZfhcaHlUB7IEozUUXCGAygWPVTwmycnjjCbYQ92D5AA8WZGd9LSJZCMVe1yKliI-B0FFBF4mHT2UPiFraUQqiHKf184Dq1hURnHCOOIS_koaWCmKfS3FG55k1yeqwFz-2TTzeWwPmIJpV-x_6HmcuFWOzhqGXk9l0eKbRRqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ امروز یه شبکه اینترنتی به نام "TRUMP TV" راه انداخت و قراره 24 ساعته سخنرانی‌ها و برنامه‌هاش رو پخش کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148757" target="_blank">📅 17:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148756">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
کمیته امنیت ملی مجلس: آمریکا جرعت نزدیک شدن به تنگه هرمز رو نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/148756" target="_blank">📅 17:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm5EUY0T1zPniiS96gl15_CC2-TQXHDR_Tqy7fgDnVjr9KqHondciFTRUqB-qmBv0ZLNLysrKx4ThOzvJAmHA6qQGFqv_O6HtHAvh9sn3EwagahTt8UQjSeigjOS-1t-MOz73D6ajZC792uMPIX7KTmaG-RYVnLt5aQSLSsAtRF9rAqvhwhMEL7KEhxXDMssVe9o8MzQFcaljOoXfktnOBJwSoc23ucgQ2_heDLn4MAXU4tnec4LuOc6ideMj-Jt-NXL8vPx0a1fxfUeQBklwVdhMgIEGwf1PAojsCYWgdaiuK1QstwHsxSRv_1ZtEfEL-aiyIw_-tW9LMU3P-CW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامینگ سون
🤣
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148755" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
آنتونیو گوترش، دبیرکل سازمان ملل متحد: «ما نمی‌توانیم اجازه دهیم راه‌حل دو کشوری در برابر چشمانمان از بین برود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148754" target="_blank">📅 16:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca659922b.mp4?token=HMRqCLuPknTFeYYtuY7k5EvpCIVuABiBGzfK6e1F1j4ie7JYVPlmALqVvuCvGP8OqPuNH0RjDxFpKxyi5Y2FGKdqiJc32MhgJtjXW_BKqBEW6OrPAa62qLvNKNFlZkdS0Ek24DfwaRy8VJB8uv9xv0osc-H3GXUOCKcD5mX5i8Gu5Q8hL5Q7mHYYd_QejNDZ1UK9YRNzb2kBsCi-oUckonilRU119t81o9ZFZq1OF6fIH1CYHDNy167fqNBfdwU5TiGN69uw-N_e2122qzTkpF43Z7cgwYocN7zBn9AvL3TZ7Ti8pdjfqd-iQWBqHrNBrA28FaLqdqKsmDgOtVQgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca659922b.mp4?token=HMRqCLuPknTFeYYtuY7k5EvpCIVuABiBGzfK6e1F1j4ie7JYVPlmALqVvuCvGP8OqPuNH0RjDxFpKxyi5Y2FGKdqiJc32MhgJtjXW_BKqBEW6OrPAa62qLvNKNFlZkdS0Ek24DfwaRy8VJB8uv9xv0osc-H3GXUOCKcD5mX5i8Gu5Q8hL5Q7mHYYd_QejNDZ1UK9YRNzb2kBsCi-oUckonilRU119t81o9ZFZq1OF6fIH1CYHDNy167fqNBfdwU5TiGN69uw-N_e2122qzTkpF43Z7cgwYocN7zBn9AvL3TZ7Ti8pdjfqd-iQWBqHrNBrA28FaLqdqKsmDgOtVQgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی با وزیر خارجهٔ ایتالیا دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148753" target="_blank">📅 16:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔴
مردم توصیه‌های بهداشتی را رعایت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148752" target="_blank">📅 16:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f8382345.mp4?token=BPajr9PhQme0IQxdU0seW-gnvlz-56q-RtVFd1Xm2Kv0Um0UoRnVSC3__Cew4TNeIelM_aw9jSNoMT_3g_fNcQJHNeiwPAiD1un8a_WYxvfW_PCUoNrK-SrvuVZVDwwX1gH3naRSja0B1LNw4anY5mt6NwadI_UJfSaIjpAbZRbhNYRX7Ol08l1HrVozGo_jRSZemsZ2CigDnNUiVAqbw9wuvHvOKLBJ7BarElDeqehxvJO2ZZFnBjKaidPqnPqVO5vlwpnij_scg0HxWp3dLw1J6qF7nVsZv3ilu53ZicAo348GVt5b5frWjiVFHi8d7tweOdCWV1NERNDGIS6QWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f8382345.mp4?token=BPajr9PhQme0IQxdU0seW-gnvlz-56q-RtVFd1Xm2Kv0Um0UoRnVSC3__Cew4TNeIelM_aw9jSNoMT_3g_fNcQJHNeiwPAiD1un8a_WYxvfW_PCUoNrK-SrvuVZVDwwX1gH3naRSja0B1LNw4anY5mt6NwadI_UJfSaIjpAbZRbhNYRX7Ol08l1HrVozGo_jRSZemsZ2CigDnNUiVAqbw9wuvHvOKLBJ7BarElDeqehxvJO2ZZFnBjKaidPqnPqVO5vlwpnij_scg0HxWp3dLw1J6qF7nVsZv3ilu53ZicAo348GVt5b5frWjiVFHi8d7tweOdCWV1NERNDGIS6QWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ورود فیصل بن فرحان بن عبدالله، وزیر امور خارجه عربستان به نشست مجمع عمومی سازمان ملل متحد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148751" target="_blank">📅 16:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148750">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a14e65bfd.mp4?token=Uk_dN4IP3z5TCPUIHeSHnL_PKMMf7hXWQG22tDTWd_mbnVlw1hRVlWdl_SJQuuO45Y4gLWNnQn9NPOVJAK4RYkQGexpeQgmS8tvCso1cqB1ZsAOHzBcJjfk5xInJMtraQuP4DXJTRqxCrGQY2RJuC1487xh5UQtu4zwhsT_ndksWxxUMoTkMR1x6uxbZ0ZzzlOKExIaaQHSfaJlJwTpCzXuRj6e4ylVZ929TmDimv5cHdN4iFFEoJ4k2xKKXz04Gj3VT2LTy_rAOdKuzEnSgq0Nq8CZHKQIPwqtzb_xd27tB9kstPV-fPZyGIm8Pj960MbzLUep0rqzVlipSLr5seA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a14e65bfd.mp4?token=Uk_dN4IP3z5TCPUIHeSHnL_PKMMf7hXWQG22tDTWd_mbnVlw1hRVlWdl_SJQuuO45Y4gLWNnQn9NPOVJAK4RYkQGexpeQgmS8tvCso1cqB1ZsAOHzBcJjfk5xInJMtraQuP4DXJTRqxCrGQY2RJuC1487xh5UQtu4zwhsT_ndksWxxUMoTkMR1x6uxbZ0ZzzlOKExIaaQHSfaJlJwTpCzXuRj6e4ylVZ929TmDimv5cHdN4iFFEoJ4k2xKKXz04Gj3VT2LTy_rAOdKuzEnSgq0Nq8CZHKQIPwqtzb_xd27tB9kstPV-fPZyGIm8Pj960MbzLUep0rqzVlipSLr5seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرادویسی، تحلیلگر اینترنشنال :
اینکه ترامپ، پزشکیان و عراقچی رو تو خاک آمریکا دستیگر کنه و مثل مادورو بندازه زندان، احتمالش خیلی کمه اما صفر هم نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148750" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148749" target="_blank">📅 16:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سی‌ان‌ان: دونالد ترامپ به مشاوران خود گفته است که اگر "شرایط مناسب باشد"، مایل است با مقامات ایرانی که در مجمع عمومی سازمان ملل متحد در نیویورک حضور دارند، دیدار کند. یک مقام آمریکایی این مطلب را اعلام کرد.
🔴
هیچ جلسه‌ای هنوز برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148748" target="_blank">📅 16:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148746">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رایزنی تلفنی پوتین و بن‌سلمان در خصوص موضوع یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148746" target="_blank">📅 16:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148745">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
منابع دولتی عراق به خبرگزاری العربیه:
تا کنون تصمیمی برای ممنوعیت فرود هواپیماهای ایرانی در فرودگاه‌های عراق اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148745" target="_blank">📅 16:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148744">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگو سپاه: به فناوری موشک خیلی دوربرد رسیدیم، منتظر دستوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148744" target="_blank">📅 16:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148743">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a8258249.mp4?token=aNtaSdBi0p9Tpj_ZXbcHtetao7GQs3JhV_MMjb7tCPZdG81cDKiBR-J0e4KPuOSH-k16Liv34ZgHvQOyRzxwntZ6ViqAZIQ8yIaydai-HM221PtTnFnJLuk7-0rkvAwQviviVqEy4R5BsfJSP0XbCkrKjigBxGrGgetXixEVQ3ltP0pgScQOR-Z-AJ78xszXLnH6Q0WlssnWt0-JP58DzCUkK8ljqCcOFdEbOTKq49BBReSZthMIWWra2WkGrt60V021HlBJ9yIoU1CI2ZySDkYu0vCgJsGvCnrE2HwhruwpYa_FlkVeA0Pz76Rn3IMLmJUpfkP03mmmh-zPUg3qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a8258249.mp4?token=aNtaSdBi0p9Tpj_ZXbcHtetao7GQs3JhV_MMjb7tCPZdG81cDKiBR-J0e4KPuOSH-k16Liv34ZgHvQOyRzxwntZ6ViqAZIQ8yIaydai-HM221PtTnFnJLuk7-0rkvAwQviviVqEy4R5BsfJSP0XbCkrKjigBxGrGgetXixEVQ3ltP0pgScQOR-Z-AJ78xszXLnH6Q0WlssnWt0-JP58DzCUkK8ljqCcOFdEbOTKq49BBReSZthMIWWra2WkGrt60V021HlBJ9yIoU1CI2ZySDkYu0vCgJsGvCnrE2HwhruwpYa_FlkVeA0Pz76Rn3IMLmJUpfkP03mmmh-zPUg3qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی در حاشیهٔ نشست مجمع عمومی سازمان ملل با وزیر خارجهٔ سوئیس دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148743" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148742">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ارزش بازار ارز دیجیتال، از ۳ تریلیون دلار عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148742" target="_blank">📅 16:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148741">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7frxh0sA91_JDeljGCmQi5Csku7u24bJ-NHGFEIkBH76g9XIUUaybT-7p8S7VGk01-TKg4r-tXJ3YJyWGX0co0ZiByfcCUnt1OcWY1G2LZ1lXuX6Fr_DDOvbAEnfm4SlTOtb2P0lmHzIOrFxe6nr4rQbZgVAPL25YMW3dJpYKqhR0O_U7eaWXOr667GJhBvFP_y3CEnNSrNDoS7pOB37ZznrrlE5IdN7fGaOLdcppKzdAyX0X0LAC_feFgIAd8YHbn2ULALw4miDMRVMzv9HELxrcBBzuuvgRbcI17BgvNod8cobaiUWKGgGT5gZ8nHZ_-nxl3QBWcjdZBIYHwBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استقبال وزیر کشور الجزایر از پزشکیان، در توقفی کوتاه در فرودگاه الجزیره، در مسیر سفر به نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/148741" target="_blank">📅 16:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3MYVAQGVf-Mx3XqGv-0dxKLxK3Hza1UmHtkk8Yizqcizos7wiTcfKDTfo9sOSEolGVEp5l-xbguRiuPB9sQil9mQpC2sVtlFXlgiYN5se3GVtg_xzDkCwkgCLmMAeJDMSinTkieVu1CiD9mW64LgAh0uQIBwG5LU942EbAd66hpRFQBldZEyJcrXxmIzrdULPZHwfM069TJExAMb51mLEgK6IwBE669fL-Mbl1i55SZW2zX8YFExikbvVudWGp8fIVsLNocEG2VxKIu7HLrk_xNSvNM0mnTc78EWIhQJSBKtUS0umIdCVNkm0p1V61BoCI2HNPARZ6NLulNhnGbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای A330 MRTT متعلق به نیروی هوایی عربستان سعودی از پایگاه هوایی ملک عبدالله در شهر جده برخاست و به سمت جنوب و کشور یمن در حرکت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148740" target="_blank">📅 15:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148739">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دولت اسرائیل قرار است طرح فراخوان و بسیج حداکثر ۲۰۰ هزار نیروی ذخیره برای یک دوره دیگر از خدمت در ارتش اسرائیل (IDF) را تصویب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148739" target="_blank">📅 15:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148738">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idD7SzBzEIjHHJcwUJMjoQHlOWgaxS_rYZlR__IJII28TiQ7UDYli_F8YrmpBLsZXuea7Kc8_tiDrqKG3BvFMnezh4x1ONN4bISbCV4OLZXl2K9hdpFRi30f-5nKgBXxdsTtoLifZn25EnNfn_ZYocdlh027u256NprYL6ZywbvnigQKnNsMBTkP3uXfp2VI6fdhaYtKLdfI7mCuDd-2vpTSn2mg3wjet9aum_6VTsNZ8h2LQR7J9Cgn0Z3fvM8X0POCl7O6SaqBoCyC2flCxr9No7vcln1cK2drqBuvs7X9ZGLitLU64lbdDeN62Gwn4JbLbCM9hmEyu-Ic-rD7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه‌ای از وزارت خارجه آمریکا به تاریخ ۱۸ سپتامبر نشان می‌دهد که سرویس امنیت دیپلماتیک آمریکا (DSS) در جریان سفر عباس عراقچی، وزیر امور خارجه ایران به آمریکا برای شرکت در هشتاد و یکمین مجمع عمومی سازمان ملل، برای او تیم حفاظتی اختصاص خواهد داد.
🔴
در این نامه آمده است که یک «ارزیابی کامل» از تهدیدهای احتمالی علیه عراقچی در خاک آمریکا انجام شده و ترتیبات حفاظتی نیز با نمایندگی ایران هماهنگ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148738" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148737">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
بلومبرگ: کشورهای عربی حوزه خلیج فارس در دیدار روز سه‌شنبه از ترامپ خواهند خواست از تشدید تنش بیشتر با ایران خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148737" target="_blank">📅 15:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148736">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d59f3d89.mp4?token=aqhWZl8TxFR6mcK31S_kW0aNnbvTedhBffxhJsakRb-C96xhIo0B-boevVfgbrfOhEsSA_YqUW95dXp3Vryzh2AePUzVSMDpSON2T2KrmxT6-0ArVOAANwUFDVPhR3XXgR2ngqi9GzQC1gVkbXcvRnV6McgI4-3psIQ35QwCcgYzeywMeQBiy7LMhbNOVWJOI45Bp14GRY-Onc1cmUPqtdMajfwRFCP8_bkK3k4s9qVXZn7LwQLVvEoO7lEcrfwOTuYOHzLXWiu1LALYa4XbcrCJisgAhlAONJqrKZLVjGW8iAlt8Pk_-eLyq4FxHh3q9_ysISmYa61eBUu_cD0QjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d59f3d89.mp4?token=aqhWZl8TxFR6mcK31S_kW0aNnbvTedhBffxhJsakRb-C96xhIo0B-boevVfgbrfOhEsSA_YqUW95dXp3Vryzh2AePUzVSMDpSON2T2KrmxT6-0ArVOAANwUFDVPhR3XXgR2ngqi9GzQC1gVkbXcvRnV6McgI4-3psIQ35QwCcgYzeywMeQBiy7LMhbNOVWJOI45Bp14GRY-Onc1cmUPqtdMajfwRFCP8_bkK3k4s9qVXZn7LwQLVvEoO7lEcrfwOTuYOHzLXWiu1LALYa4XbcrCJisgAhlAONJqrKZLVjGW8iAlt8Pk_-eLyq4FxHh3q9_ysISmYa61eBUu_cD0QjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ناتو: «اگر در شرایط اضطراری نتوانیم از پایگاه خود استفاده کنیم، صادقانه بگویم، پس اساساً داشتن این ائتلاف چه فایده‌ای دارد؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148736" target="_blank">📅 15:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148735">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759912fdab.mp4?token=VZcJ901JeNpLbYjn0P0aabgB7t91RDwLRXbFwHII8O2Frq1peMgMZIZ5lmij3H55tyJqU322aiT8pHW7q3QFpXK3-8mjLqKnIakFm0nzJna1cttxafloBRldebJXAaRTr7onjnJu8xssEkibyQPLoo4YilA2zUslErVoX_w_j1V8nasks1w3acJf35A5TtAdhFOHitgmYDkKPbgaAM41qcJQyCEf669EjmGaWi2823eAVS0BJnDahGvVDy1z7Ud44YNX__CimWV1_CpGLLcjCvTVGOkUAecmvuSVRvJfkA9E2Kuy_W0wxqZyD7MYR2VZEI9kusck40XQ56UqXbJJmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759912fdab.mp4?token=VZcJ901JeNpLbYjn0P0aabgB7t91RDwLRXbFwHII8O2Frq1peMgMZIZ5lmij3H55tyJqU322aiT8pHW7q3QFpXK3-8mjLqKnIakFm0nzJna1cttxafloBRldebJXAaRTr7onjnJu8xssEkibyQPLoo4YilA2zUslErVoX_w_j1V8nasks1w3acJf35A5TtAdhFOHitgmYDkKPbgaAM41qcJQyCEf669EjmGaWi2823eAVS0BJnDahGvVDy1z7Ud44YNX__CimWV1_CpGLLcjCvTVGOkUAecmvuSVRvJfkA9E2Kuy_W0wxqZyD7MYR2VZEI9kusck40XQ56UqXbJJmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره گرینلند:
«
چندین رئیس‌جمهور آمریکا
اهمیت جغرافیایی گرینلند را درک کرده بودند. اما
ترامپ نخستین رئیس‌جمهوری است که واقعاً برای آن اقدامی انجام داده است.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148735" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148734">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8d10b7d9.mp4?token=L1jpD8UmQGRfPOXlYZQEYJWWWMsaGi6SfoHBSxm0VppzIrnlBDNAcy36JtUIW30oYrYN5euP-To5f_L8GKjDT021UnHW7pA3UkrHF0Ax8SR3-Bo-bl2pCtUXY756W4oHPoiFz-Z0HkOzXT5sBi_ZJXKNXlFkPOJRadKosgRLdR-aFLnbvtrnkMgf31oUhSnrdlTOUHR9ZEkVRroqAljhGCo-6cC70D-CkVT24e_QOvuQZtM0t_tA5vxpYBWqBU1qV9hypES0UNp0z_CVmtTgwULyYRy_UTkxrJf37J357kq08G2smmIuVgmm8VbhNBJldRbP6KT0G-0UXGXum5ITAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8d10b7d9.mp4?token=L1jpD8UmQGRfPOXlYZQEYJWWWMsaGi6SfoHBSxm0VppzIrnlBDNAcy36JtUIW30oYrYN5euP-To5f_L8GKjDT021UnHW7pA3UkrHF0Ax8SR3-Bo-bl2pCtUXY756W4oHPoiFz-Z0HkOzXT5sBi_ZJXKNXlFkPOJRadKosgRLdR-aFLnbvtrnkMgf31oUhSnrdlTOUHR9ZEkVRroqAljhGCo-6cC70D-CkVT24e_QOvuQZtM0t_tA5vxpYBWqBU1qV9hypES0UNp0z_CVmtTgwULyYRy_UTkxrJf37J357kq08G2smmIuVgmm8VbhNBJldRbP6KT0G-0UXGXum5ITAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، اکنون می‌گوید
کتائب حزب‌الله عراق
مسئول حملات پهپادی اوایل ماه جاری به خط لوله شرق-غرب عربستان سعودی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148734" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148733">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c33e10f9.mp4?token=YlG_YCf50vaIGqrzTfkklaDIB47NojQU1ZtKToQr4RcY1oQPKxpu8ikmV5jhXMdBDSiQmZFiWJABTf2Xn9GyXHpyq0O9FewTynmhX--kLd1iPVDEsTBcxglHaB0rKROvNaalcg3Y1Sa_rSLbJ1nDLkdmXSllOP3rAiyf919iiy6b_R5J9QUJAFtvvOCu_-LT49Iwgi2n9I1gYNmXPUE5-CHuRA3pj7qqiCtvrnFF6_Aq3touy7Hwr6JwdDLSfsowf2ngiz7o8DR8HQ3FkswRvzMbCRyLnEbwNoiw2sIyCC8hLwDhhXn1BIRPWcq9nJ_vihaWZY6_RVM7zh8iwCxVEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c33e10f9.mp4?token=YlG_YCf50vaIGqrzTfkklaDIB47NojQU1ZtKToQr4RcY1oQPKxpu8ikmV5jhXMdBDSiQmZFiWJABTf2Xn9GyXHpyq0O9FewTynmhX--kLd1iPVDEsTBcxglHaB0rKROvNaalcg3Y1Sa_rSLbJ1nDLkdmXSllOP3rAiyf919iiy6b_R5J9QUJAFtvvOCu_-LT49Iwgi2n9I1gYNmXPUE5-CHuRA3pj7qqiCtvrnFF6_Aq3touy7Hwr6JwdDLSfsowf2ngiz7o8DR8HQ3FkswRvzMbCRyLnEbwNoiw2sIyCC8hLwDhhXn1BIRPWcq9nJ_vihaWZY6_RVM7zh8iwCxVEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره اوکراین
:
فکر می‌کنیم آتش‌بس در حوزه زیرساخت‌های انرژی ایده بسیار خوبی است؛ به‌طوری که زیرساخت‌های اوکراین هدف قرار نگیرند و در مقابل، تأسیسات و منابع انرژی روسیه نیز مورد حمله قرار نگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148733" target="_blank">📅 15:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148732">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78825914c9.mp4?token=uYvEkbOYBrp5vfd5apS9j6TAcSuphHi_j4I9gMYxgKPdIersazxFtxYgxrTr-CB9ES-G3ey-_23RL0G8qpstCy4aQ-FK2NsJDV8OaNjL0_jUnrqNUoPVfpE5La7sx3jxlkS0YQm50axENGjjRkSmeVBkNoRVcp1sNMYKsPshCiIy4KfQWZvyJR5M7eGkoJ3qN-rmZyAAE8bVnmgxYM7TwQGdNy2eZlx3JAOSy82gDeK42OrkuAZL-GRjWeiWesSmAfJ57bBKHs3awJFBHC02Ekd5gmvp2LxClV9qRp-Vtubbkpt_zgsHoVc7tuLiBBXomXwKwJmbRQn0FB5OA8bTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78825914c9.mp4?token=uYvEkbOYBrp5vfd5apS9j6TAcSuphHi_j4I9gMYxgKPdIersazxFtxYgxrTr-CB9ES-G3ey-_23RL0G8qpstCy4aQ-FK2NsJDV8OaNjL0_jUnrqNUoPVfpE5La7sx3jxlkS0YQm50axENGjjRkSmeVBkNoRVcp1sNMYKsPshCiIy4KfQWZvyJR5M7eGkoJ3qN-rmZyAAE8bVnmgxYM7TwQGdNy2eZlx3JAOSy82gDeK42OrkuAZL-GRjWeiWesSmAfJ57bBKHs3awJFBHC02Ekd5gmvp2LxClV9qRp-Vtubbkpt_zgsHoVc7tuLiBBXomXwKwJmbRQn0FB5OA8bTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره اوکراین
:
در چند ماه گذشته، در چند مورد کشتی‌های مرتبط با آمریکا هدف حملات اوکراین قرار گرفته‌اند؛ احتمالاً این حملات عمدی نبوده، اما به هر حال این کشتی‌ها هدف قرار گرفته‌اند.
🔴
نمی‌توانیم اجازه دهیم چنین اتفاقی ادامه پیدا کند و این مسئله باید حل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/148732" target="_blank">📅 15:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148731">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd254ba0c.mp4?token=XToTl5sFeegqt_YnSRUeC4vG3TBTd1Bh7CxuEFP_CwgqW4VbEI10Xr6SWJjfT6YA_R7IZ-RxTDX9RlwrxwAOYZVgdi_AUQn6P0V4aqy2om5_KUt9kqWZtzqzBnGdZZ1IpgkSWQPC7f0wEgIWJ82Nic3SON8jMAuL0SKm55bhvY-4JfNC0KFHJZwNbE7BvtgVEIjY9UPxq0iampreSQUeWVMbtaDkUTLsRxip1OUZOUpaBzPbjIeNHjm8_pI2J-FwZIs0dxrwddExCHyQtZKG4PQmJew8kznoGFirefptieHMF1bbZODE43HAYbRmH7j6Vaka3O6uzn7d8VhnpOWfWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd254ba0c.mp4?token=XToTl5sFeegqt_YnSRUeC4vG3TBTd1Bh7CxuEFP_CwgqW4VbEI10Xr6SWJjfT6YA_R7IZ-RxTDX9RlwrxwAOYZVgdi_AUQn6P0V4aqy2om5_KUt9kqWZtzqzBnGdZZ1IpgkSWQPC7f0wEgIWJ82Nic3SON8jMAuL0SKm55bhvY-4JfNC0KFHJZwNbE7BvtgVEIjY9UPxq0iampreSQUeWVMbtaDkUTLsRxip1OUZOUpaBzPbjIeNHjm8_pI2J-FwZIs0dxrwddExCHyQtZKG4PQmJew8kznoGFirefptieHMF1bbZODE43HAYbRmH7j6Vaka3O6uzn7d8VhnpOWfWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران
:
دولت بایدن به‌شدت به‌دنبال توافق با ایران بود و چهار سال تلاش کرد با امتیاز دادن به ایران به توافق برسد، اما در نهایت نتوانست به هیچ توافقی دست پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148731" target="_blank">📅 15:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148730">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1ebf6542.mp4?token=fgBykVyqsYvJ-IT6mSnopWSazlLemT52yPhc5g3YP4z3J13cziCHapDBy6PRLdF6ngrtndKD6Ewcni6x5ucwEAnqLEjGyX52BrgAMlWX3u1QXlS-dZpHvl8cBSm7r8ZueHd5efKiUdx3NwjE7zcViYUS44Vk0IIrmvcklzUhi19PZLdqVjWfXIQJd3SXocdF8_tD6FJC6Zv_FNcOrKWEVXLLfsex5veD15ZUCl1GDd11HeowOrkbdhhjX0tD2vuC5ukuxz2_HQuQc0uVy0W8e8zHRWZp0YC0R4DNCBvapKjTAT_mmLl4oRabJWwKRM4z6e89cvOzYtOu2VMc8p-YVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1ebf6542.mp4?token=fgBykVyqsYvJ-IT6mSnopWSazlLemT52yPhc5g3YP4z3J13cziCHapDBy6PRLdF6ngrtndKD6Ewcni6x5ucwEAnqLEjGyX52BrgAMlWX3u1QXlS-dZpHvl8cBSm7r8ZueHd5efKiUdx3NwjE7zcViYUS44Vk0IIrmvcklzUhi19PZLdqVjWfXIQJd3SXocdF8_tD6FJC6Zv_FNcOrKWEVXLLfsex5veD15ZUCl1GDd11HeowOrkbdhhjX0tD2vuC5ukuxz2_HQuQc0uVy0W8e8zHRWZp0YC0R4DNCBvapKjTAT_mmLl4oRabJWwKRM4z6e89cvOzYtOu2VMc8p-YVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: «در حال حاضر حدود ۶۰ تا ۷۰ درصد از جریان نفتی که پیش از این از تنگه هرمز عبور می‌کرد، دوباره در حال عبور است و این میزان رو به افزایش است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148730" target="_blank">📅 15:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bb79220ba.mp4?token=D-QbHzYQw3T91g1wXB741Z9FmHcTVD2MRMlFxLqKeGyYRdKOmKjZv3k1yXykCcKga3SGND9ru_JIIBfe4uBM6lf2xE9efQO4hb1j-ivdk6N-lhzSrYWJRt9ghxhQt7NpKEIiAtNsW0Cwyo6Asg1hOWfn5-1OyjL0f4RYHyTCDe-UzFbfbpnqfiGg3WfnUKNnNFbhUMPMX8GkwaJjSiU1Hv9ZUnAWRR054h3aJO6mavkBBV-WGtaiGfRcfLdSS6gk--rzJe7I0846rjTyF5SwWUVirgWkr2o7pTZMHSReGnOcV3XxPdHJcPMvJOl0tG5WqSPWW_JjyaZ3gl4sKZHVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bb79220ba.mp4?token=D-QbHzYQw3T91g1wXB741Z9FmHcTVD2MRMlFxLqKeGyYRdKOmKjZv3k1yXykCcKga3SGND9ru_JIIBfe4uBM6lf2xE9efQO4hb1j-ivdk6N-lhzSrYWJRt9ghxhQt7NpKEIiAtNsW0Cwyo6Asg1hOWfn5-1OyjL0f4RYHyTCDe-UzFbfbpnqfiGg3WfnUKNnNFbhUMPMX8GkwaJjSiU1Hv9ZUnAWRR054h3aJO6mavkBBV-WGtaiGfRcfLdSS6gk--rzJe7I0846rjTyF5SwWUVirgWkr2o7pTZMHSReGnOcV3XxPdHJcPMvJOl0tG5WqSPWW_JjyaZ3gl4sKZHVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: «تصور کنید کره شمالی در خاورمیانه وجود داشته باشد. این وضعیت برای جهان فاجعه‌بار خواهد بود.
🔴
در آن صورت، دیگر برای گازوئیل ۶ دلار یا هر قیمتی که امروز دارد پرداخت نمی‌کردید؛ بلکه باید سه برابر این مبلغ را می‌پرداختید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/148729" target="_blank">📅 15:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=qqh25qiID7IyHJPWMRCJVMw0bfEgZcqE44QwOQJowZGd6fjNpPQTVEtbwqACrSbO7iKmyweO-AetXPZXuRQupJJGSPGlrdYBf8B_x7VLSXF7KM06eAkvrCDfvIxAePoC0l82XYmkemQDVhgFtGxr8Py3Gt7hK_mJb_lbCTwHVKmOCZJaUB1ZPEfERxCGtarANWtz3F0iNuClnybSOO2AA4NR0e1I7dspQxNI_Km0WQV99nfa27p1I2szDhpHdYJA50Zx9x-zzUQdPz1LvQBBxogNh4WvB6pAUZssnGuWqRxqtNexAqyRtxC7nm11-9fVPtmMLNINfxm-dVP_rCFWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=qqh25qiID7IyHJPWMRCJVMw0bfEgZcqE44QwOQJowZGd6fjNpPQTVEtbwqACrSbO7iKmyweO-AetXPZXuRQupJJGSPGlrdYBf8B_x7VLSXF7KM06eAkvrCDfvIxAePoC0l82XYmkemQDVhgFtGxr8Py3Gt7hK_mJb_lbCTwHVKmOCZJaUB1ZPEfERxCGtarANWtz3F0iNuClnybSOO2AA4NR0e1I7dspQxNI_Km0WQV99nfa27p1I2szDhpHdYJA50Zx9x-zzUQdPz1LvQBBxogNh4WvB6pAUZssnGuWqRxqtNexAqyRtxC7nm11-9fVPtmMLNINfxm-dVP_rCFWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: «مسئله اصلی اینجاست که ایران توسط روحانیونی اداره می‌شود که دیدگاهی بسیار افراطی نسبت به دین خود دارند و نگاهی آخرالزمانی به آن دارند.
🔴
این افراد هرگز نباید به سلاح هسته‌ای دست پیدا کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148728" target="_blank">📅 15:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان: هرمز بحرانی بزرگ‌تر از کرونا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/148727" target="_blank">📅 15:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148726">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فارس: منابع داخلی گزارش‌های مربوط به توافق‌های مربوط به بازگشایی تنگه هرمز را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148726" target="_blank">📅 14:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrVIVlsRXsfqHj_35NPaPndFB5-Uqsh5MwbxzMGCdouhKCFCXja_X-nxplH5qm63-6n_vPd2vIHpNknVA5HSyPf1V3IV5a2-l438fMeKgojfoMB9hWESK6LRNVl6205khjaGo0QXQdnbEwppETC5US6v6w9YvDAdsbM3Z9Utl4-ETDniC5OG2-JxYa1VX1S2VqvJQ4aKWpBAP7_9GnQ9DJG82X7Fs6auArO4KORbnxArT8m1ulKiLo3UXC5FBfVrclv7Wf_umf7EUwQCjxfp5hdlr-UEpAvfauinfaohB1Hm_Gpif790C44JzABzmAYnH0pAoFRlMUIKFDteH7fUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ترسوها و خائنان دوست دارند بگویند که ایالات متحده کمبود مهمات دارد. این درست نیست.
🔴
ما مهمات بیشتری داریم تا اینکه بتوانیم حتی تصور کنیم که از آن‌ها استفاده کنیم، و در حال حاضر آن‌ها را در سطوحی تولید می‌کنیم که قبلاً هرگز شاهد آن نبوده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148725" target="_blank">📅 14:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری / روبیو: برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148724" target="_blank">📅 14:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / روبیو: برای دیدار با هیئت ایرانی در سازمان ملل آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148723" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
