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
<img src="https://cdn4.telesco.pe/file/Oqe5BVaTAGytS1H7e0wiDACyV9cUVR48IMCqMDGZ_N045Yt8AnhZN9vl9Uw2Lg_QPBtdcr7pwpc3rLCbaDqFw5hAn2ZWnuYr8srwYve0oAjs-hye2AMQiP_6-wszFxTBwC62-qnc5Hrvv8UoTtEMHpu5NfEQ_ZGcfjgaJ6FF2DnLbm8xBnxQLJUvDCHv6g44LDoLYg00bLyNGHlpxrjoo4y6bkWXvohyTukW1wePZsWcqkqv6dfJTDf-R6UaTvyT4DGsapN9b671ulv44Wmqf_2L6RDkTvLKK-O1wSl-6qiESu501xjLupWxAf_HctM_yTo8gAHA62HtuWOoOQm5Hw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 262K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 23:28:14</div>
<hr>

<div class="tg-post" id="msg-11419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/withyashar/11419" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11418">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMJdBKQ74rjfcEJPXudL5Hh2F7Clw4p2hL1JeQDWhdHZxA8oklWdWHat67ts1GElTmbg_5v0y-vrxT-2uPXGx7r-ACZGXqKfGYJp4wH9Yvvjf6nSQ6YeqIslyEqDjy3sjJ-9PhIBDUB-9HF5d7dx2ilp6ytJzT1Anv5acm_fVFA1PQHWXmWFQGM4wZnO26B86QZvRmQKQ12qA3EWQRPBoaNgeuq-Nv_yBBkLUFUp5-7LRgrdO7ASzEibQa8E5lVzWKcs7W8y_Q66Vxqe3OYjkvnQAcmeCdgzuNGTQrCKAx6UomgSWd5TvllwTOKPVBl3rm8EBAJuI3psCLKFAEyX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاورین شاهزاده (امیر اعتمادی و سعید قاسمینژاد) ، علی کریمی‌ رو به علت واکنش ‌به کنسرت و آهنگ شاهین نجفی آنفالو کردند  @withyashar</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/11418" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11417">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شاهزاده رضا پهلوی در نشست آینده تکنولوژی در ایران:
ایران می‌تونه به کره جنوبی تبدیل بشه، اما به دلیل وضعیت سیاسی کنونی به سمت الگویی شبیه کره شمالی سوق داده شده؛ جمهوری اسلامی در ذات خودش قابل تغییر نیست.
@withyashar</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/withyashar/11417" target="_blank">📅 22:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11416">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در بالاترین سطح هشدار برای احتمال از سرگیری جنگ با ایران است.  در صورت از سرگیری جنگ با ایران، احتمال دارد ایران در روزهای نخست ده‌ها موشک به سمت اسرائیل شلیک کند.
@withyashar</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/withyashar/11416" target="_blank">📅 22:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قلعه نویی در لیست نهایی جام جهانی آزمونو خط زد و گفت باشرف هارو دعوت کردم.
@withyashar</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/11415" target="_blank">📅 22:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11414">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال استریت ژورنال : ایران و آمریکا بر سر یک موضوع توافق دارند در حالی که بن‌بست دیپلماتیک بین تهران و واشنگتن ادامه دارد, هر دو طرف می‌گویند که در حال حاضر درباره سرنوشت ذخایر اورانیوم غنی‌شده ایران بحث نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/withyashar/11414" target="_blank">📅 21:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11413">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو : اگه آمریکا دوباره بخواد عملیات نظامی علیه ایران رو شروع کنه، اسرائیل آماده‌ست
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/11413" target="_blank">📅 21:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFapo1414</strong></div>
<div class="tg-text">داداش ناموسا من اونجا بودم داد میزدم به شاهزاده میگفتم حتما با یاشار ملاقات حضوری بکن</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/withyashar/11412" target="_blank">📅 21:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11411">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hy4MG0Xs0crPl-bdKMTxSKtOtSGeLF7DuOiGwQYlVR_emiUhUl8ur6rXwGeJ8GlvnNKkoaCogPgkvzddFWddnT5VEaVY4nPZ9N9KkTZtYT6cPTB2b5Q7VxNirE5OejYHgRDMLUrunu_UyuPzQYD7o4GI75mNWRELKa2_usw6jJaKXFqbnhqWyIEiRl2fACbX-VjGGXrH2QzdQdXoTHYf787Eu0LEHWNyUPWZbo0Sv0M5p5HSegScKfRYFC24BYrlXF4g13q3-F0pNBA-hbqXsb8RRJdX6VtueRPpBJQhoGJpRDwq1o2AOyRhMznjw-iqxJ7cpYZcaVQXBdu_jiMMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سخت ترین شرایط بهمون روحیه دادی، تو جلسه ی بچه های تکنولوژی با شاهزاده به یادت بودیم!
❤️</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/11411" target="_blank">📅 21:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرهاد مجیدی با البطائح به دسته دو امارات سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/withyashar/11410" target="_blank">📅 21:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11409">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این ناو گروه در حال فرار هستن یا چی ؟</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/11409" target="_blank">📅 21:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11408">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromH.E</strong></div>
<div class="tg-text">این ناو گروه در حال فرار هستن یا چی ؟</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/11408" target="_blank">📅 21:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11407">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkk9VjPAGNuIHMLlMlS1fZGwCzD-L8oGMG0plfxK9E_1Pr-PQBqUbmO7vSSV6twCcja133KPKObNbBu3XhUrsbo37rvIIntvlok41uxkfxD3ROYEG49O1Kq_kA_UhKj9YWnC35d61FtN-VJtEYCtSfENK_pp-B_HNnlojd90R1lUS5DjNg5pElchVcQP7gJ60KD4GJ7B_NOUbKQLZ4ZjsVJkZK612QVlqTmjLbxZPA8U8uCGpjJiqcDZGbX8DAJW4j9YpCcRokfm5jiQ3nSeqtt3B86hm8ehq7QRFbLOtIhW9wkE9B6bQyoxBexNOrbUp2NDd12AB44zv-Ea7zkI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناوگروه  آبراهام لینکلن با سه اسکورت با سرعت به سمت دریای عمان می‌ روند  ، ۲۶ اردیبهشت. (مکان 260 کیلومتری چابهار)
@withyashar</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/withyashar/11407" target="_blank">📅 21:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11406">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شبکه 13 اسرائیل: هم اکنون ارزیابی‌ها در اسرائیل بر این است که جنگ با ایران در روز های آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/withyashar/11406" target="_blank">📅 21:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11405">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: اگه به آمریکایی‌ها آسیب بزنید، یا در حال برنامه‌ریزی برای آسیب زدن به آمریکایی‌ها باشید، ما شما رو پیدا خواهیم کرد و خواهیم کشت.
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/11405" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11404">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ در گفت‌وگوی تلفنی با شبکه فرانسوی «بی‌اف‌ام‌تی‌وی»:
آینده مذاکرات نامشخص است اما اگر توافقی حاصل نشود ایران روزهای بسیار سختی در پیش خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/11404" target="_blank">📅 20:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11403">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">العربیه: طبق گفته منابع آگاه پاکستانی، در بحث تنگه هرمز، پیشرفت‌هایی حاصل شده است
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11403" target="_blank">📅 18:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11402">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a350642e.mp4?token=gi16V0sFQm6YGa8oJpGWxo-C0SPq2BRi3RJbr_NBx_HqroTO2Bi843-R7h4wc8JhQ0mRbmc7Ul2b6T_QWpoEoOSH0zBC0KPte6X2uCdLP_uB-6GksBRi8ZzNuhKKKkqK3dcfMCxpi3b_50ryRGjGK44Qu7D667B1VTMjdQWqKcUTJvufMQxsjlUUtFcOWmLNrFgid51aKDBnE9hxLnTGHBII1Av7wU_zOs2MUKuhFftEoy-dFY3iTqT0xCjZfndfjCdCqk774Q_LkaRqKgFdI9oZdg3iP3oxrCdVmx1uQNJD_1NQSrVmBgXYnuPm3DVa_APrT8W6CqQvghnGlKYsEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a350642e.mp4?token=gi16V0sFQm6YGa8oJpGWxo-C0SPq2BRi3RJbr_NBx_HqroTO2Bi843-R7h4wc8JhQ0mRbmc7Ul2b6T_QWpoEoOSH0zBC0KPte6X2uCdLP_uB-6GksBRi8ZzNuhKKKkqK3dcfMCxpi3b_50ryRGjGK44Qu7D667B1VTMjdQWqKcUTJvufMQxsjlUUtFcOWmLNrFgid51aKDBnE9hxLnTGHBII1Av7wU_zOs2MUKuhFftEoy-dFY3iTqT0xCjZfndfjCdCqk774Q_LkaRqKgFdI9oZdg3iP3oxrCdVmx1uQNJD_1NQSrVmBgXYnuPm3DVa_APrT8W6CqQvghnGlKYsEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوئل نهایی ، وضعیت الان!
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11402" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11401">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTm bzx</strong></div>
<div class="tg-text">عرزشی ها اومدن که خبر مرگ بابای سپاهیشون رو زودتر تو چنلت ببینن
اخه از رسانه های دیگه ۱ ساعت حداقل جلوتری ستون
😂
🔥</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11401" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11400">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_TnkN0KtQR9To8UEHc0sTLdDRbEUrqFBYzZPelxAvsuV9_1xm6yWe5rlUAX7Dm7zFQqVRzHAxmoSNFuQ-0l2mhqX5xlKowToLgTB5ORwOYfEjjsGBDhqYq1q0yMJ7eKHljJL5AC6LTZXtpYMXcVHx7YL7rURYQYeOg1HqUVJDfcTR59XXq4v-X7WAAI2psespbuSkt5-w3H0gZHf0hijagejvwlK1jgz3Zf4IHcPN-CjpJAAyC3JGHQcRU00dza4t2kgo_Y-KHDwSORhT2aHoxTK269Uqwdx4UILErnqkMky1s9qqhMSO4rzdVcrHheMpwIKl2x_ykQU7RsEj7jAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ :
شوخی نداریم!!!
ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11400" target="_blank">📅 17:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11399">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سقوط یک شهر پاکستان به دست جدایی‌طلبان
منابع محلی روز شنبه از تسلط جدایی‌طلبان بلوچ بر شهر راهبردی دالبندین در پاکستان خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11399" target="_blank">📅 17:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11398">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فقط برای یک پست که نمیشه ببندم مهندس ! کلا ببندمم که یعنی میگی خنده رو از روی لب چندین هزار نفر بگیرم به خاطر ده نفر. ما اینجا هدف اصلیمون مبارزه با اخبار سمیه و روحیه دادن به مردم. اجازه بدید در عرزشی سوزترین رسانه ایرانی بسوزند و حرص بخورند</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11398" target="_blank">📅 17:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11397">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from➖</strong></div>
<div class="tg-text">میتونی ری‌اکشن رو هم ببندی داداش!</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11397" target="_blank">📅 17:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11396">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این پست اوناییکه استیکر خنده گذاشتن رو از کانال مسدودشون کن</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11396" target="_blank">📅 17:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11395">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐝𝐢</strong></div>
<div class="tg-text">این پست اوناییکه استیکر خنده گذاشتن رو از کانال مسدودشون کن</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11395" target="_blank">📅 17:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11394">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">لازم به ذکر است شخص اینجانب ، یاشار در اتاق جنگ هیچ رابطه و تیمکشی با هیچ گروه جناح و سمتی ندارم مسیر من مسیر مانوک خدابخشیان و فریدون فرخزاد است و هم پیمانان من فقط مردم واقعی و وطن پرست ایران هستند و برگ برنده ما همه با هم اینجا برای عبور از مسیر فقط فقط فقط خود شخص شاهزاده رضا پهلوی است ، یک بار دیگه خواستم اهداف و مسیر خودم را مشخص و کلیر کنم
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11394" target="_blank">📅 17:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11393">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مشاورین شاهزاده (امیر اعتمادی و سعید قاسمینژاد) ، علی کریمی‌ رو به علت واکنش ‌به کنسرت و آهنگ شاهین نجفی آنفالو کردند
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11393" target="_blank">📅 17:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11392">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9ZOj6kvQHacKmFNy8fyEj4sxzhJM-09bHrTkacAgS1QfK-yaunqtzWHbIoAwfVBzozNdofn0PEo5SnxPNQPzpT3wwbA4ivKzeSAPbtHoQagJ9MXdzcFyCQbtQ98ZeS-jXJ0zX_WYZuiWJFgmswS5PWiAEUpgu1RPgCz1YcntnhRQbP9Qu-jc43lfhc5AyOGADfIxBWgTxZ5DTh1o_SkPcMMsOEfqZIUbM8hhQv7sy_PdVst_AuoQBffyv_6RZXM4KpNqzfg2YE9RZt1_fwwfgbHdGd5lNi19GPJYDUIeOszTICGd5SxzXps-ebtc5zLkELqKUYhGFfkkwBbC4OGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی پسر بچه … به یاد جاوید نام های کوچکمون مبارزه میکنیم تا  نسل جدید این درد ها رو نکشه !
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11392" target="_blank">📅 16:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایسنا: وزیر کشور پاکستان برای دیدار با مسئولان جمهوری اسلامی ساعاتی قبل به تهران سفر کرده.
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/11390" target="_blank">📅 15:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانال ۱۲ اسرائیل مدعی شد: ترامپ بزودی با اعضای کابینه خود جلسه اضطراری برای پایان دادن به اوضاع ایران برگزار میکند.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11389" target="_blank">📅 15:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525b5bf33d.mp4?token=aTL08U-_JmEciKREnClO0PdepzG99n_IQ3bK5ACQO4grH8MWtdMFjLm_i8_BOm8b5RMQmQh-Kwa4nnIa4WOQJEB7qx_cfZ7v-qI4F4gXoKyzRvTJlFaN6MNQ1AbQM2vkPpDsL5RAonYp0rjtL-w9yg4zF4VXLxvpIiW3nWibCQZEs-l5HWWEZO4YNGqrQ0UDLn5yd6VpmV9r2cCn_FZhxzLbkS3YwGi9JQfqfM4TiWH0prg892exWD4q2oKfTYhabnpLWBMgnO7xt8aqpAlbhSSWRjyQ5kk_FyLb2KmEI1khJSUapMCqalWPE9iTin76FpE-bmpiU2X9Mv7kyrhhVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525b5bf33d.mp4?token=aTL08U-_JmEciKREnClO0PdepzG99n_IQ3bK5ACQO4grH8MWtdMFjLm_i8_BOm8b5RMQmQh-Kwa4nnIa4WOQJEB7qx_cfZ7v-qI4F4gXoKyzRvTJlFaN6MNQ1AbQM2vkPpDsL5RAonYp0rjtL-w9yg4zF4VXLxvpIiW3nWibCQZEs-l5HWWEZO4YNGqrQ0UDLn5yd6VpmV9r2cCn_FZhxzLbkS3YwGi9JQfqfM4TiWH0prg892exWD4q2oKfTYhabnpLWBMgnO7xt8aqpAlbhSSWRjyQ5kk_FyLb2KmEI1khJSUapMCqalWPE9iTin76FpE-bmpiU2X9Mv7kyrhhVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر کلی رسانه ها اینه که ۷۲ ساعت طلایی پیشه رو داریم
😬
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11388" target="_blank">📅 14:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شبکه فاکس نیوز: ارتش آمریکا درحال آماده شدن برای دور جدیدی از درگیری های نظامی در ایران است
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11387" target="_blank">📅 14:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایال زمیر، رئیس ستاد کل نیروهای مسلح اسرائیل اعلام کرد کشته‌شدن عزالدین الحداد، فرمانده‌ شاخه ‌نظامی «حماس» یک گام مهم و موفقیتی بزرگ در عرصه عملیاتی است.
او افزود اسرائیل «با جدیت» به‌ تعقیب و هدف قرار دادن سایر رهبران و فرماندهان حماس ادامه خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/11386" target="_blank">📅 14:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciz6o8CUMUD0-LuZsTqt0Ke338rJtOYQDEt996Na4dG1JDadcfKcONiOEqwTqfXmwWQ4FcGaZD1EGjKlnI_9Q-5OI1ChRdtyRnH2MEnGY3BVQPKstyLgihpF3L_hjV1HuiZy-80zwQHSYWy5BxwMvqHmAeWpya7cc_OIeFattQwuU_42OENo4BWUA837ZymN5bcrRQxpCozVifgh8EGtV_fSgx8ojg7IviSjA-w2-XfHOnOV_bpbVVrumq7Nk5x3G-UAqjoLvLbI-lXmeK3sqFfo3_Qk-DRnkD7sOfv-bG_7wqJeBEjtlmARrgWedUrt3pQA6hNgLxvGKjOOQzt-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما هم میدونه چی میشه داره آموزش کار با سلاح رو میده
😂
اینا رفتنین شک نکنید
👋🏾
👋🏾
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/11385" target="_blank">📅 13:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooria</strong></div>
<div class="tg-text">آقا یاشار عزیز،
واقعاً دلم می‌خواست یه چیزی بهت بگم از ته دل.
مرسی که با کارای دلی و عشقیت، بهم نشون دادی وقتی کاریو با دل شروع می‌کنی، چقدر می‌تونه برکت و موفقیت بیاره.
از اون موقع که تو نوجونی اون سایت برای پروموت کردن رپرها  ساختی تا همین الان که با تمام وجود وقتت رو پای این کانال خبری (تلگرام و اینستا) می‌ذاری تا مردم خبر درست بگیرن، یه چیز بزرگ یاد گرفتم ازت — اینکه عشق و نیت خالص از هر چیز دیگه‌ای قوی‌تره.
بهم یادآوری و یاد دادی که پیشرفت فقط با کار زیاد نیست، بلکه دلی و با عشق کار کردن توی کاره.
دمت گرم ، واسه همه این زحماتت، واسه الهامی که بهم دادی، و واسه اینکه خودِ واقعی‌ت رو بی‌منت به دنیا نشون میدی
💚</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11384" target="_blank">📅 13:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11383">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جسی واترز، مجری فاکس نیوز:
ترامپ درحال آماده‌شدن برای دور جدیدی از حملات نظامی به ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11383" target="_blank">📅 13:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11382">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: 5 بار با ایران نزدیک توافق شدم، ولی روز بعدش زدن زیرش
@withyashar</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11382" target="_blank">📅 13:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11381">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نشست آینده تکنولوژی در ایران، با حضور و سخنرانی شاهزاده رضا پهلوی امشب ۸:۳۰ به وقت تهران ۱۰ صبح به وقت غرب آمریکا سانفرانسیسکو
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11381" target="_blank">📅 13:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11380">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام به نیویورک تایمز : کشتی‌های ایرانی رو با ماهواره و چند روش دیگه ردیابی می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11380" target="_blank">📅 12:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11379">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آسوشیتدپرس: بازگشت ناو هواپیمابر جرالد فورد به پایگاه پس از ۱۱ ماه مأموریت
وزارت‌جنگ آمریکا اعلام کرد پیت هگست، وزیر جنگ، روز شنبه در پایگاه دریایی نورفولک در ویرجینیا از ناو هواپیمابر جرالد فورد و ۴۵۰۰ ملوان آن پس از ۱۱ ماه مأموریت استقبال می‌کند.
این ناو ۳۲۶ روز در دریا بوده که طولانی‌ترین استقرار یک ناو هواپیمابر آمریکایی در ۵۰ سال گذشته و سومین رکورد از زمان جنگ ویتنام است.
@withyashar</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/11379" target="_blank">📅 12:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال N12 اسرائیل: جنگ سوم با ایران نزدیک است
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/11378" target="_blank">📅 12:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نامه زرشکیان به پاپ:  ما به راهکارهای دیپلماتیک برای حل و فصل مسائل، از جمله پرونده‌های اختلافی با آمریکا، پایبندیم و بعد برقراری امنیت، عبور از تنگه هرمز به حالت عادی بازخواهد گشت
@withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/11377" target="_blank">📅 11:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز به نقل از یک منبع آگاه گزارش داد که متیاس گرافستروم، دبیرکل فیفا، امروز در استانبول با مقام‌های فدراسیون فوتبال ایران دیدار می‌کند و درباره حضور تیم ملی در جام جهانی ۲۰۲۶ «اطمینان خاطر» خواهد داد. این درحالی است که مهدی تاج پیش از این خواستار تضمین‌هایی از فیفا شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11376" target="_blank">📅 11:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کرملین امروز اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه ۱۹ مه (۲۹ اردیبهشت) برای یک سفر دو روزه به چین خواهد رفت. این سفر در پی سفر دونالد ترامپ، رئیس‌جمهور آمریکا به پکن انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11375" target="_blank">📅 11:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11374">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چمران رئیس شورای شهر تهران:
رایگان اعلام کردن مترو و اتوبوس در تهران کار احساسی بود و فردا آخرین روز رایگان بودن حمل و نقل عمومی در تهران است و تمدید نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/11374" target="_blank">📅 11:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11373">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شریعتمداری:
مذاکره به جای خود، اما جنگ بدون پاسخ پایان نمی‌یابد
/
با شهادت آقا شروع کردند بی‌انتقام تمام نمی‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11373" target="_blank">📅 11:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11372">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۲ اسرائیل گزارش داد انتظار می‌رود دونالد ترامپ، رییس‌جمهوری آمریکا، طی ۲۴ ساعت آینده تیم مشاوران نزدیک خود را تشکیل دهد تا درباره ایران تصمیم نهایی بگیرد. برآوردها در اسرائیل حاکی است تصمیم درباره اقدام نظامی ممکن است بسیار به‌زودی اتخاذ شود.
برنامه تلویزیونی «اولپن شیشی» به نقل از یک مقام ارشد اسرائیلی گزارش داد که «ازسرگیری درگیری نزدیک است» و اسرائیل خود را برای احتمال «چند روز تا چند هفته جنگ» آماده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/11372" target="_blank">📅 11:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11371">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qswIwrXNDZ32GsrOSx446M5vGYroHIaZ3hb46qj2R9uq9xhKhXHDmeJLLpDJPY92FzfL7xM-SqCBsoRhySTf9IrrXeAKfsKRc3iZyrAVWmqomN1uaKL9Z6sk4hwRzuTvVcByowZJKGdi5IGfZDZLOmPJim2rxCuznI49NCvSbrQNhJS-xuASQX5fzLrrUtaHRHOy4jxJB6mFRtA4bZsl9LVTPTVvNs0Zfuk6C1nzTRxlEXmGCmHShLRtYb1F0w9ni3GbIJFziUtYIAMnRTZbBa8ew5lsPqJrjUMFHqkn5pH52_NM8v4hcfImYynKLfmQYNzJSHOT-RIjuZZ-bloB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مشاور قالیباف تو اینستاگرام
🤣
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/11371" target="_blank">📅 11:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11370">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/11370" target="_blank">📅 05:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11369">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/11369" target="_blank">📅 05:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11368">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیویورک تایمز از قول مقامات نظامی آمریکا:
اگر جزیره خارگ تصرف شود ، نیروهای زمینی برای حفظ آن لازم خواهند بود.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/11368" target="_blank">📅 04:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561d76df7d.mp4?token=ijfZwJ9ELxGOYEdZXJjfabzYirzBJ9jdR8BTNGfcbyAhf_BY5Xn2kGpj8XtPcduPDfIxpZG1oUESZXY6jQYkmp3mDpVK0YZxtEyOAduD-4uJ3D4E-ITM8XdMxex7izKN99Ro42BzKe3koNh7SRPTJlYPS4XcAnmyBjFC6x6wnmff0N5SGPVINkppETtw83251IwDcVZQBptL8i_PkhK19dhvTr0eQXKF4C_fWYwlZxvQK7sc_yncmsrPkOe0Y9hKs3ouRXq0v139b_JGTnUmqpW7MUNIpbj1ro-iXzyz9ycSP7sUvkg-lq2OJ4A11fQH8pQTRmzDfWg07lXx1tKi_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561d76df7d.mp4?token=ijfZwJ9ELxGOYEdZXJjfabzYirzBJ9jdR8BTNGfcbyAhf_BY5Xn2kGpj8XtPcduPDfIxpZG1oUESZXY6jQYkmp3mDpVK0YZxtEyOAduD-4uJ3D4E-ITM8XdMxex7izKN99Ro42BzKe3koNh7SRPTJlYPS4XcAnmyBjFC6x6wnmff0N5SGPVINkppETtw83251IwDcVZQBptL8i_PkhK19dhvTr0eQXKF4C_fWYwlZxvQK7sc_yncmsrPkOe0Y9hKs3ouRXq0v139b_JGTnUmqpW7MUNIpbj1ro-iXzyz9ycSP7sUvkg-lq2OJ4A11fQH8pQTRmzDfWg07lXx1tKi_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها چیزی که می‌توانم بگویم این است که این یک موفقیت بزرگ بود.»
رئیس جمهور ترامپ پس از سفر به چین به کاخ سفید بازگشت و به خبرنگاران گفت: «ما به توافق‌های بزرگی رسیدیم» و این دیدار را یک لحظه تاریخی خواند.
سپس او به اتفاقات بیشتری در آینده اشاره کرد: «اتفاقات زیادی افتاده است و شما درباره آنها خواهید شنید.»
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/11367" target="_blank">📅 03:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: افزایش قیمت‌ بنزین مرتبط با جنگ ایران «درد کوتاه‌مدت» است که بسیار کمتر از چیزی است که مردم انتظار داشتن.
وقتی به کسی میگید که باید کمی بیشتر برای بنزین در یک دوره بسیار کوتاه بپردازید، چون میخوایم جلوی تهدید تکه‌تکه شدن توسط یک دیوانه، یک فرد دیوانه رو بگیریم، و آنها دیوانه هستن با استفاده از سلاح‌های هسته‌ای، همه میگن که این خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11366" target="_blank">📅 03:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/11365" target="_blank">📅 03:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">صادق هدایت میگه دیگه
میگه اگه کارت با سر و کله زدن با ادماس میفهمی چه ملت شریف زبون نفهمی داریم</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11364" target="_blank">📅 03:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83bfd5694a.mp4?token=BRiagJcpc-Kio3g1Jfb_kuH0COb5-auzQ_mgoXVbb3WnmLlQ3HcM1XEk2tLzxJjmIxc8PhzXWSPjPej220Z2MDHW0V9pV2Zj_tR1JXU6NMrd4LaNzmlG4Bnq04j8CDQRGiZ9sXyzA5XPfNERk6ZE8h508LbKvzYVEZ_NSqFJBCoewW-7pHwNCbylbqMDUVf70OYkbLPL8-ZNhn5S89RO0i1zEEoqtGREmle9xUFcicxSkXlHs8nXlkz6o3DrGRftfaHyMfq3SEWJeVFY3PXoVanoPKqIw8Wdi6FPxi2DoCA0_2JTR3ZVPRqhn8mEtCkxr-kcfWRGRXfgWM5nW4QaGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83bfd5694a.mp4?token=BRiagJcpc-Kio3g1Jfb_kuH0COb5-auzQ_mgoXVbb3WnmLlQ3HcM1XEk2tLzxJjmIxc8PhzXWSPjPej220Z2MDHW0V9pV2Zj_tR1JXU6NMrd4LaNzmlG4Bnq04j8CDQRGiZ9sXyzA5XPfNERk6ZE8h508LbKvzYVEZ_NSqFJBCoewW-7pHwNCbylbqMDUVf70OYkbLPL8-ZNhn5S89RO0i1zEEoqtGREmle9xUFcicxSkXlHs8nXlkz6o3DrGRftfaHyMfq3SEWJeVFY3PXoVanoPKqIw8Wdi6FPxi2DoCA0_2JTR3ZVPRqhn8mEtCkxr-kcfWRGRXfgWM5nW4QaGYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اف‌بی‌آی ترامپ یک توطئه تروریستی بزرگ را که قرار بود توسط یک فرمانده شبه‌نظامی تحت حمایت ایران در خاک ایالات متحده، کانادا و اروپا انجام شود، خنثی کرده است.
محمد السعدی - رهبر کتائب حزب‌الله اسلام‌گرا - بیش از ۲۰ حمله را برنامه‌ریزی کرده بود. هدف او اماکن یهودی، از جمله یکی در نیویورک بود.
جان‌های بیشتری نجات یافت
«بنابراین او به اینجا آورده شد و امروز زودتر در دادگاه حاضر شد.»
می خواهم در مورد این عملیات محتاط باشم تا کسی را به خطر نیندازم، اما همین کافی است که بگویم این تلاشی بود که نه تنها اف‌بی‌آی، بلکه شرکای اجرای قانون ما در خارج از کشور را نیز شامل می‌شد.
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/11363" target="_blank">📅 02:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc0ddeea66.mp4?token=eUncpEdSgGeDuHVPNKRDOCdF5aopnfYc76HyHl7atsxjAvOE6-mnNO_dLB8VLZcHsVFf6shYiGxtL4N4JvyKeqveuCfZgA5oSpCVQOYTxPagETmz2GOqCVaNxUP_vjYsxXaswaWiue2_IjaPSidCPkj5qP-UfdBawrxg29mbp5dxbe9CAFD9AhmIR6lBOG7K9m5KT2vXOIXWFMnLV5lh8zpjggDajXow6t5jZIk0N19X6YsnZdFkVWkRYtSM4OTORs0hK89fk5NZfEIVOBuyIWh6AA981c9WP1J5NnL8zgP58U2ZEKYqfoEMeebFNoykaK_uTMcD5GZxMbPPe9HB6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc0ddeea66.mp4?token=eUncpEdSgGeDuHVPNKRDOCdF5aopnfYc76HyHl7atsxjAvOE6-mnNO_dLB8VLZcHsVFf6shYiGxtL4N4JvyKeqveuCfZgA5oSpCVQOYTxPagETmz2GOqCVaNxUP_vjYsxXaswaWiue2_IjaPSidCPkj5qP-UfdBawrxg29mbp5dxbe9CAFD9AhmIR6lBOG7K9m5KT2vXOIXWFMnLV5lh8zpjggDajXow6t5jZIk0N19X6YsnZdFkVWkRYtSM4OTORs0hK89fk5NZfEIVOBuyIWh6AA981c9WP1J5NnL8zgP58U2ZEKYqfoEMeebFNoykaK_uTMcD5GZxMbPPe9HB6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۹ تا دوربین مختلف  در فضا روی سایت هسته ای ایران داریم
می‌تونیم اسم طرف رو هم بخونیم
مثلاً اگه اسمش محمد باشه، ‌که خب بیشترشون محمدن، تقریباً می‌تونیم حدس بزنیم که حدود ۵۰٪ اطلاعاتش درست در میاد
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11361" target="_blank">📅 02:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ : ویتنام ۱۹ سال طول کشید، عراق حدود ۱۰ سال، کره ۷ سال، یکی دیگه ۱۴ سال، یکی ۱۲ سال، یکی هم ۹ سال
- ما فقط دو ماه و نیم اونجا بودیم
- چین هم این هفته سه تا نفتکش پر از نفت ایران رو برد، چون ما اجازه دادیم این اتفاق بیفته،شما اجازه دادید
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11360" target="_blank">📅 02:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac35dbd92.mp4?token=vqRenKpmNo4Z_1WXwvwEqac8cyNVT_6TR3umM2bymDnt3-8gqJWTNj0ReHibytrNjP0ZwYRFW6YgdSxhkiVc1aGyuyxyTPFCOIAWcyKvL4eF-8gPnGHjVzU0l6fSDtJbsgEgErvWPM1Q4gs98DFFBE38tOczvHQiQyv6j4OD5xW_zROhL3G9xfqOBsfaG2aIN3UTowzyJy6p1Lj2g7TDz46N_rIZdvkTZSONiIcdc3Wtq62m4hc_ZHPbBITlXNlsOkjY9gVNl08ugZynt6lJoBXNoEMczf_hGtgmsuKqB5IxbF4haIEnm2eeHcMb6JrpEfQKXpi1P3f9odjAByZCxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac35dbd92.mp4?token=vqRenKpmNo4Z_1WXwvwEqac8cyNVT_6TR3umM2bymDnt3-8gqJWTNj0ReHibytrNjP0ZwYRFW6YgdSxhkiVc1aGyuyxyTPFCOIAWcyKvL4eF-8gPnGHjVzU0l6fSDtJbsgEgErvWPM1Q4gs98DFFBE38tOczvHQiQyv6j4OD5xW_zROhL3G9xfqOBsfaG2aIN3UTowzyJy6p1Lj2g7TDz46N_rIZdvkTZSONiIcdc3Wtq62m4hc_ZHPbBITlXNlsOkjY9gVNl08ugZynt6lJoBXNoEMczf_hGtgmsuKqB5IxbF4haIEnm2eeHcMb6JrpEfQKXpi1P3f9odjAByZCxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجریان صداوسیما برداشتن یه تصویر هوش مصنوعی رو گذاشتن و دارن تحلیلش میکنن!
😂
😂
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/11359" target="_blank">📅 01:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فقط حال من رو فروشنده های بازار که با مردم سر و کله میززند و جماعت زبون نفهم و میبینند درک میکنند</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11358" target="_blank">📅 01:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11356">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer"><a href="https://t.me/withyashar/11356" target="_blank">📅 01:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11355">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11355" target="_blank">📅 01:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11354">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات آمریکا:
دستیاران ترامپ برنامه‌هایی رو برای بازگشت به حملات نظامی به ایران آماده کردن، اگر او تصمیم بگیره با بمباران بیشتر از بن بست خارج بشه.
از جمله گزینه‌ها، اعزام نیروهای ویژه به ایران برای هدف قرار دادن مواد هسته‌ای مدفون شده است و ممکنه از نیروهای ویژه برای کنترل جزیره خارک استفاده بشه.
@withyashar</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/11354" target="_blank">📅 01:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11353">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRp3u062d5Q3JgITttJkkRLoqQh-54luzkieqw9KlWGSc6eKBNEIhh2gFN4xMPi5igkBD9sGKBlwA-No91CrrAx0TvWddYeD7bSK51Ir_rmtEc0gJT2BDetzf34j2Q-5G-B3cLitfKiEaS050eXZhgFEj8teJH-FM_Pcr0KCWEkmp9N5FnamQu20JH1gdlbLKVgW_MPSoiMnsgampVmKj5E7cmaHGurit_-wOtbpSzsWYgeU2hdvndhj5qJSbmN9IBhd3Mp6T33l6xkzxXOxkvli2dJIrVQ4RYz3dOiN0jN_6NuOp-2ERI9G_jy9Oy5cs-XkudPfEVSQ_xKk2kHirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد جدید مجله تایم: چگونه دیدار ترامپ و شی، نظم نوین جهانی را نشان داد
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11353" target="_blank">📅 01:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11352">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ خیلی عجله داشته هیچ فیلمی عکسی از رسیدنش نیومده بیرون ! عجبیه</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11352" target="_blank">📅 01:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11d28292.mp4?token=eFW9_EdNj6siI-q4b3qj3oq54V-KRDp62j27VDztisvDUCt98nxkMuKBqDCXAt4lAhiS_AHue8Pqgf8Zv1Mv-T2A_gDfDumjikTYKFyAkv5jDN2zgFds5ItfdXJxECPp82VwdCW9N8LtXJvm9SKSbZa19jBw5zxJgyrR49262iBsv9P8_yRDPo6P7XkXZupfjXY0lU-7P8UjW2LafnLfkdSGZAjdAIOdFbHzjz8q4NYuRne4YYzh6owdYFJ3RPK80ojVau-e2FvjXlFXqM-2yCaK5MzwLGCr6rmnm2gXkXJjtupMZTZR9cBHHuV3x1TZ0Dfvc10PW7sldErWVr4TzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11d28292.mp4?token=eFW9_EdNj6siI-q4b3qj3oq54V-KRDp62j27VDztisvDUCt98nxkMuKBqDCXAt4lAhiS_AHue8Pqgf8Zv1Mv-T2A_gDfDumjikTYKFyAkv5jDN2zgFds5ItfdXJxECPp82VwdCW9N8LtXJvm9SKSbZa19jBw5zxJgyrR49262iBsv9P8_yRDPo6P7XkXZupfjXY0lU-7P8UjW2LafnLfkdSGZAjdAIOdFbHzjz8q4NYuRne4YYzh6owdYFJ3RPK80ojVau-e2FvjXlFXqM-2yCaK5MzwLGCr6rmnm2gXkXJjtupMZTZR9cBHHuV3x1TZ0Dfvc10PW7sldErWVr4TzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/11351" target="_blank">📅 01:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در تروث : تینا را آزاد کنید
@withyashar
تینا پیترز یک مقام انتخاباتی سابق آمریکاست که به‌خاطر دخالت غیرقانونی در سیستم‌های رأی‌گیری بعد از انتخابات 2020 زندانی شده و حالا ترامپ از او حمایت سیاسی می‌کند</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/11349" target="_blank">📅 00:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11348" target="_blank">📅 00:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/11347" target="_blank">📅 00:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11346" target="_blank">📅 00:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیویورک‌تایمز به نقل از ۲ مقام امنیتی:
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری حملات علیه جمهوری اسلامی هستند،
این حمله ممکن است از هفته آینده آغاز شود
@withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/11345" target="_blank">📅 00:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه مسیج درست اگه تو دایرکت دیدی به من بگو ! انگار‌من کشیش کلیسام ! یا کلانتر محل !</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11344" target="_blank">📅 00:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11342">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امشب حمله‌ست؟</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11342" target="_blank">📅 00:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11341">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSea</strong></div>
<div class="tg-text">امشب حمله‌ست؟</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11341" target="_blank">📅 00:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11340">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYG02iHJlF3X-wrijhFXyar630gg7OuIJHa8smEOBCnK8as-FZx6B5Xhwif0R_Qc6sBH74xtQtDLJR9Q9pxqq3YJkRQjSW2duSqibepHtMvswJXu94C_BBQy3Z5dmzFeP7iOz1ib1Zf-SKPI007LPHwzTyk061tjK6mT79cO7E4CCwA8_LaTZpEHoJeo4tqUAfAdmz-HsG2Z7PuFKV7-CZBipCo8kMxofje8MbJJ5yts22Ykr0faN9Js3uUJmZcrN4WRWOM7Pth4j29yErkmuCcnPdiUnN5SphVP77EfRjqI-Qw_fMH5x6HHQUcQelGWUydcCFI3pU84WPAZV2d1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما هم میدونه چی میشه داره آموزش کار با سلاح رو میده
😂
اینا رفتنین شک نکنید
👋🏾
👋🏾
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/11340" target="_blank">📅 00:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11339">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اگه امشب شب‌زیبایی‌نبود و امید نبود الان رد میدادم ! با این پیغام هایی که دایرکت میاد</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/11339" target="_blank">📅 00:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11338">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">عمو یاشار ما امشب منتظر اومدم اومدمیم
😂
🫡</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11338" target="_blank">📅 00:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11337">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یاشار یچی خواستم بگم روم نشد ولی کلاهبرداریه اگه امکانش بود اطلاع رسانی کن  ما پیوی ینفر رفتیم برامون خاله جور کنه واسه معرفی ۲۰۰ از ما گرفت بعد شماره طرفو داد گفت یک میلیون ۳۰۰ دیه برامون بزن گرفتیم براش زدیم بعد اومد گفت برای تضمین ۱۳ میلیون بزنید بعد اینکه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11337" target="_blank">📅 00:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11336">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahd</strong></div>
<div class="tg-text">یاشار یچی خواستم بگم روم نشد ولی کلاهبرداریه اگه امکانش بود اطلاع رسانی کن
ما پیوی ینفر رفتیم برامون خاله جور کنه واسه معرفی ۲۰۰ از ما گرفت بعد شماره طرفو داد گفت یک میلیون ۳۰۰ دیه برامون بزن گرفتیم براش زدیم بعد اومد گفت برای تضمین ۱۳ میلیون بزنید بعد اینکه کارتون تموم شد برش میگردونم حالا ما بهش گفتیم ۱۳ میلیون از کجا بیارم گفتم کنسلش کن ۱۳۰۰ بهمون برگردون اومده میگه اون مهریه بوده دیگه میره برا خالهه
ولله به این پفیوزا اعتماد نکنید اگه امکانش هست بزار چنلت بقیه هم در جریان باشن</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11336" target="_blank">📅 00:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11335">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ رسید آمریکا
@withyashar</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11335" target="_blank">📅 23:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیویورک تایمز: آمریکا محمد بکر سعید داود السعدی، فرمانده ارشد شبه‌نظامی گردان‌های حزب‌الله درعراق، رو دستگیر کرد و علیه‌اش کیفرخواست صادر کرد.
او متهم به طراحی حداقل 18 حمله در اروپا، آمریکا و کانادا از پایان فوریه شده؛ این حملات به عنوان انتقام از حملات آمریکا و اسرائیل علیه جمهوری اسلامی برنامه‌ریزی شده بودن.
@withyashar</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/11334" target="_blank">📅 23:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7f890274.mp4?token=mvAcIpX7SIiaJOkiL6eBdMkAOYg0yECTYkBsYAy0pSI0l8jomsRHJKGKK28zvfJpcneDkWdZJUx9x968JDPMreCSUweL-2_4wmtlnTa44k3z7IjIaZRe7E0EY03ECTcKVyiRf_9NtQGIrYMjgIBKs1HAju-17rjjCiWiLnmihj7bOObuZNyNdg6vcWD80JnPCCTxT5I5jxPsEerX8MmLIGsYDjba_H_bkxZtQ7DaxftIxgu0QaZdGsJJK-O2c1rWn85GFowqKOtThriuJivEkHD0kIMo7ic2joaF7pHCFTAdXfR0ccoEbYUot0zR6J50nRUWITXP561B07Nq6n5qxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7f890274.mp4?token=mvAcIpX7SIiaJOkiL6eBdMkAOYg0yECTYkBsYAy0pSI0l8jomsRHJKGKK28zvfJpcneDkWdZJUx9x968JDPMreCSUweL-2_4wmtlnTa44k3z7IjIaZRe7E0EY03ECTcKVyiRf_9NtQGIrYMjgIBKs1HAju-17rjjCiWiLnmihj7bOObuZNyNdg6vcWD80JnPCCTxT5I5jxPsEerX8MmLIGsYDjba_H_bkxZtQ7DaxftIxgu0QaZdGsJJK-O2c1rWn85GFowqKOtThriuJivEkHD0kIMo7ic2joaF7pHCFTAdXfR0ccoEbYUot0zR6J50nRUWITXP561B07Nq6n5qxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه خداحافظی ترامپ با شی و خوشحالی او از سفر موفقیت آمیزش
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11333" target="_blank">📅 23:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7aab5fc3.mp4?token=i_3kTBJd2iajWUgJIRkbyvDtlyAQkXEegJpes_DgxTFnAFUMT4CXlMX66Sm-irk-8TgX9PpuO3WnRZClrV8vlZvk21QcVmafKCTMvn-DGGz00DUvX-p_ygDc6wtHDU91ymDRmVGJ6E9rodgQSWcja44aEv0UUiLPOmj12G4cR6RjLFO5FbPZi4AyN-kS6qLMnFRD8mSDg_GI3oGX_b1wgnuVKF_FgCIIF2X-JBSJwk32abq5D4lcAJtdF-y5UMmbRf0igMR-w-cq45cdMKbsnmLTbxO74i6E5ehKM1zwnbmXwriLWG2-VqfZBNWbezRbpw3kqAx_h0Qwtj0a5PljEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7aab5fc3.mp4?token=i_3kTBJd2iajWUgJIRkbyvDtlyAQkXEegJpes_DgxTFnAFUMT4CXlMX66Sm-irk-8TgX9PpuO3WnRZClrV8vlZvk21QcVmafKCTMvn-DGGz00DUvX-p_ygDc6wtHDU91ymDRmVGJ6E9rodgQSWcja44aEv0UUiLPOmj12G4cR6RjLFO5FbPZi4AyN-kS6qLMnFRD8mSDg_GI3oGX_b1wgnuVKF_FgCIIF2X-JBSJwk32abq5D4lcAJtdF-y5UMmbRf0igMR-w-cq45cdMKbsnmLTbxO74i6E5ehKM1zwnbmXwriLWG2-VqfZBNWbezRbpw3kqAx_h0Qwtj0a5PljEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مایک والتز، سفیر آمریکا در سازمان ملل ، می‌گوید که یکی از «نتایج بزرگ» سفر ترامپ به چین این بود که چین موافقت کرده از ایران فاصله بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11332" target="_blank">📅 23:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منابع عبری :
گویا ترامپ با یک حمله محدود جهت فشار بر سر تسلیم شدن موافقت کرده است
@withyashar</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/11331" target="_blank">📅 23:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واشنگتن پست: جمهوری اسلامی واضح‌ترین بازنده دیدار ترامپ از پکن است، با مخالفت علنی پکن با اختلال در هرمز، تعهد به عدم ارسال تجهیزات نظامی به تهران و توافق بر اینکه تنگه «باید باز بماند.»
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11330" target="_blank">📅 23:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">l وزارت خارجه آمریکا اعلام کرد آتش‌بس میان لبنان و اسرائیل به مدت ۴۵ روز دیگر تمدید شد.
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/11328" target="_blank">📅 22:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11327" target="_blank">📅 22:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed7b9efa.mp4?token=tLp-Gl-M373MRh8lO8qeeW_Vf1ZPKNDzgFwTypdfcwxDCUh3-LOGsOLuoQfNDIZ4foupgY6RQPxd6zZDAbCdXjPVyM3DndFKSVyQC9Ax7P7bGthl0kwLTYVgW59A-L3F4D36jgqSaqNVfobL52P0LwFRmOpBY08AO7JRh53eqUTjztvGCuuq0uEMLffy04jjjahg0bNZACRwLGZR_DMyUw8Sp7Q-1F-ZNWVe4cBLiqJIk1hiz8MAKz1YkNeXz57qPk0YjEiSUuJ3aLv4nXBsbFyQd6VSHCSyi23n5A6lyOj771i-hpBW4xyYyoY0CJg0SJjKlBkszFPay_ZlKZ7sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed7b9efa.mp4?token=tLp-Gl-M373MRh8lO8qeeW_Vf1ZPKNDzgFwTypdfcwxDCUh3-LOGsOLuoQfNDIZ4foupgY6RQPxd6zZDAbCdXjPVyM3DndFKSVyQC9Ax7P7bGthl0kwLTYVgW59A-L3F4D36jgqSaqNVfobL52P0LwFRmOpBY08AO7JRh53eqUTjztvGCuuq0uEMLffy04jjjahg0bNZACRwLGZR_DMyUw8Sp7Q-1F-ZNWVe4cBLiqJIk1hiz8MAKz1YkNeXz57qPk0YjEiSUuJ3aLv4nXBsbFyQd6VSHCSyi23n5A6lyOj771i-hpBW4xyYyoY0CJg0SJjKlBkszFPay_ZlKZ7sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/11326" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">میگم فالورایه شاهزاده داره کم میشه قبله جنگ ۹.۹ بود الان ۹.۷ شده</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11325" target="_blank">📅 22:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirali</strong></div>
<div class="tg-text">میگم فالورایه شاهزاده داره کم میشه قبله جنگ ۹.۹ بود الان ۹.۷ شده</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11324" target="_blank">📅 22:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11323">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11323" target="_blank">📅 22:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcdqJSmeNI4BA44893GNAoZre_neaQSnJhBJySZOLF7r9O2hMZb8B2zHd9PE9d9ir4KOYmlgJJ0lmtpZZK5eLk9YZ86OQt6YvuDUUAAgz1Rz9jS_Pkh-M4wsnBjLXWMtrWanbFpetMAxfl6S4Pr3xKfWKYSVFhJleFzl_XOHm1qeaq-C4gEZMRCp8ry7CFDuMZIevKCXQ2-FLf3YOKQWo5tc4zrpgpykA63ELg6sPqlDWu4bzqa4Y9rSGr1YtUSbA629KaigGOAc_70OX7ppO90cRt84sRrpi0-4S940HtJ_sMhBLu2ZxpH32RtMLObqPpt3Gc8zlWLuIRP9m5ZaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ آ۴ هست!
واقعیت اینکه شاید الان بشه جلوی اتصال به اینترنت رو گرفت ولی تا چند سال آینده عملا غیرممکن میشه!
@withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/11322" target="_blank">📅 22:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هادی چوپان، در یک مسابقه استعدادیابی که از صدا و سیمای رژیم پخش می‌شود،  گفت: «ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم.»
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11321" target="_blank">📅 22:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شاهزاده رضا پهلوی : هم‌میهنان عزیزم،
در روزهایی که شما با شجاعت در برابر رژیم اشغالگر ایران ایستاده‌اید، این نظام منفور و منزوی، همچنان به تجاوز به جان و مال مردم ادامه می‌دهد تا سرنگونی حتمی خود را اندکی به تعویق اندازد. در چنین شرایطی، وظیفه خود می‌دانم که تصویر عدالت در فردای ایران را برای کسانی که با جنایتکاران همکاری کنند، روشن‌تر ترسیم کنم.
در این راستا، از «کمیته‌ تدوین مقررات عدالت انتقالی ایران» خواستم درباره‌ دو موضوع مهم، نظر مشورتی خود را ارائه کند: نخست، موضوع مسئولیت کیفری افرادی که با ساختارهای سرکوبگر جمهوری اسلامی همکاری می‌کنند؛ و دوم، موضوع مصادره‌ اموال معترضان و خانواده‌های آنان.
@withyashar
این کمیته اکنون نخستین نظر مشورتی خود را صادر کرده و پیام آن روشن است: این اقدامات، همکاری‌های ساده یا بی‌اهمیت نیستند؛ بلکه «یاری‌رسانی به جنایت علیه بشریت» محسوب می‌شوند. هیچ مقام، هیچ دستور و هیچ بهانه‌ای نمی‌تواند مسئولیت کیفری فردی را از میان ببرد. بنابراین، هر فردی که آگاهانه و داوطلبانه با ساختارهای سرکوبگر رژیم همکاری کند، چه در داخل و چه در خارج از ایران، باید بداند که در معرض مسئولیت کیفری قرار خواهد گرفت:
خواه این همکاری از نوع گزارش‌دهی یا خبرچینی باشد؛
خواه از نوع مشارکت در ایست‌های بازرسی‌ باشد؛
خواه از نوع به‌کارگیری کودکان و نوجوانان در سرکوب معترضان باشد؛
و خواه از نوع تحصیل، انتقال یا خرید و فروش اموالی باشد که در جریان سرکوب از معترضان و خانواده‌های آنان مصادره شده‌ است.
@withyashar
از این رو، نه‌تنها افرادی که در صدور دستور، اجرای آن، یا تسهیل این مصادره‌ها نقش دارند در معرض مسئولیت قرار خواهند گرفت، بلکه کسانی که آگاهانه و داوطلبانه به خرید و فروش این اموال می‌پردازند نیز باید پاسخگو باشند. این مسئولیت، استفاده از اموال یا دارایی‌های آنان برای جبران خسارت واردشده به مالکان اصلی را نیز شامل می‌‌شود.
بنابراین، به همه‌ کسانی که امروز در صدد همکاری با دستگاه سرکوب رژیم هستند هشدار می‌دهم: پیش از آن‌که دست به اقدامی بزنید که به مردم ایران آسیب جانی، مالی و یا اجتماعی برساند، به آینده‌ خود و خانواده‌تان بیندیشید. به آن روز بیندیشید که ایران آزاد خواهد شد؛ روزی که حقیقت پنهان نخواهد ماند؛ روزی که اسامی آشکار خواهد شد؛ روزی که هیچ متجاوز و جنایتکاری از پاسخ‌گویی در برابر قانون در امان نخواهد ماند.
آن روز، ملت ایران حکومتی خواهد داشت که حقوق ایرانیان را محترم می‌دارد و ایران را به سرزمینی آزاد و آباد بدل می‌کند.
پاینده ایران،
رضا پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11320" target="_blank">📅 21:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/11319" target="_blank">📅 21:29 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سازمان سازمان مجاهدین خلق ایران (که در آمریکا با نام‌های MEK یا PMOI شناخته می‌شود) به‌صورت رسمی در تاریخ ۲۸ سپتامبر ۲۰۱۲ از فهرست «سازمان‌های تروریستی خارجی» وزارت خارجه آمریکا خارج شد. این تصمیم توسط وزارت خارجه دولت هیلاری کلینتون اعلام شد و همان روز اجرایی گردید
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11318" target="_blank">📅 21:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/11317" target="_blank">📅 21:19 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAM</strong></div>
<div class="tg-text">یاشار مجاهدین الان دارن از کجا تغذیه میشن؟</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11316" target="_blank">📅 21:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11315" target="_blank">📅 21:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11314">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آخرین فیلم مخفی وحید بنی عامریان، نخبه ریاضی در زندان اوین که از دفاعیه اش در مقابل بیدادگاه آخوندی می گوید. وحید روز 15 فروردین 1405 اعدام شد @withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11314" target="_blank">📅 21:14 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
