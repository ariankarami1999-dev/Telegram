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
<img src="https://cdn4.telesco.pe/file/EC21f-Q8JPnZIjq0ZRmTEIgkCCxPVZVI0BHmadmf0LxUKKbEhWe_bxK6dr1-vLdtZrOtEyZvXi2baUu934g6VAR-4p1UQ0ylVcx2QxxX2U7YvuyGDfHGYpb8HZpwogNqsWUf_sjDQsAAdsuO_fr5Uxny_lWLCKSctVNr0vMvcJy4VmZzrOYZWtaravpPz9mCs3Jcy3C0fhUnlRg-8VRKqDgtFdOaqRrXGCGzZ9Kq3jORbrhI1UFg43Z3ktdVPOXNyiVwXtNizvrfj5vAdS97TgX-w0vDbsroQ7pQ8NaZhhp2gvlbnocoAQupX39KZKsbu-xnwam6BC7_qJk5BAKL7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.88M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-466499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1896f7e6.mp4?token=RFvdnVzMSdpOk45RXgna5hLwmnBbvwVuks8tpQ46eGnEgiHkTPFFt1jtKSzF0jAodV8V51xmvXn4NY_7-PmhQ0BFQFwdC1iA3wSIk0EwatO4uQau2g7EjuOpGOo21O20Odqg8LQfTIrczlA1X5kD4xPmoUIX5jC-qUEeJD7GVAGgcRlhMyF00X6iUN69kD79FYwG9KOBIj1K3EYkYOZR80qryyhPYbw2ZtRERsup8RXSeuYTUTl2fFwRpTlTqL_1xtDMjSg0lml4BYMM4D30SjSGGoqX8OWNF3dHjq3c4fy1zQBawRRFAxwClRVzTR9l3yhK5XdxcXK0lSAkAXzbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1896f7e6.mp4?token=RFvdnVzMSdpOk45RXgna5hLwmnBbvwVuks8tpQ46eGnEgiHkTPFFt1jtKSzF0jAodV8V51xmvXn4NY_7-PmhQ0BFQFwdC1iA3wSIk0EwatO4uQau2g7EjuOpGOo21O20Odqg8LQfTIrczlA1X5kD4xPmoUIX5jC-qUEeJD7GVAGgcRlhMyF00X6iUN69kD79FYwG9KOBIj1K3EYkYOZR80qryyhPYbw2ZtRERsup8RXSeuYTUTl2fFwRpTlTqL_1xtDMjSg0lml4BYMM4D30SjSGGoqX8OWNF3dHjq3c4fy1zQBawRRFAxwClRVzTR9l3yhK5XdxcXK0lSAkAXzbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۹ شب عشق به وطن در کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/466499" target="_blank">📅 22:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466498">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4bc98f35.mp4?token=gxmaITBu10PyXYhewflNP_N18JsroCuEa05f7jhV3zvPfQLbqn-Da2L5nUMj7WpuICmlw_fX3WZOd6KrHiTf341U0Qat6v-Pq56vOXs24dtSTVL1jM-3U1ma6WUo147_b53EvpP6m3FtQNqrbYBvPKzQsjx5t3-ZM6QPprwyiwbjBMuI7BUd9OWGkL8WClOCjucfqS-VkB1CQfpat7BjcDcm2c2DdwmDgM4waN45Gi73QvefmOXHOKZHgyPqp_cGTsAfDXsGPsAJPN0ifDJUxoVFB2o7ljfnBZ3yQ6tKBptx5mOwYMOUVQYBC_9zw9IsY2Bnoux2KJ0ix2sNFl-cng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4bc98f35.mp4?token=gxmaITBu10PyXYhewflNP_N18JsroCuEa05f7jhV3zvPfQLbqn-Da2L5nUMj7WpuICmlw_fX3WZOd6KrHiTf341U0Qat6v-Pq56vOXs24dtSTVL1jM-3U1ma6WUo147_b53EvpP6m3FtQNqrbYBvPKzQsjx5t3-ZM6QPprwyiwbjBMuI7BUd9OWGkL8WClOCjucfqS-VkB1CQfpat7BjcDcm2c2DdwmDgM4waN45Gi73QvefmOXHOKZHgyPqp_cGTsAfDXsGPsAJPN0ifDJUxoVFB2o7ljfnBZ3yQ6tKBptx5mOwYMOUVQYBC_9zw9IsY2Bnoux2KJ0ix2sNFl-cng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از شیوهٔ زندگی مبارزان لبنانی تا اهدای چفیه متبرک رهبر انقلاب به فرزندان شهید حزب‌الله  @Farsna</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/466498" target="_blank">📅 22:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466497">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64b0a1f0c.mp4?token=s11sy94gMPHRB6g5TxgoL1JmafqZfR3Xu0acyzPfxBbgheT56ZX4EXMprtu14w_KOSFuYP5B8tC101cWD-LASWJAr72sBpiZJPFMPJ5JGCJC9C9zpZx3r1_pROKDaA3T9uPkYY-zdskle_9lDBOuXk2nQ0zjgkMtHcaAdfQOrztx_5rUmF63AsPTUqR2KswJ8Emssr8_wnk7SIYnIlA5q2xPo4HIqimmnR_E_C7GAxFaeFyhe9EjplwRS-w81nH9AsbaHy0lhnSws5Km0YmChdjQqva0nKZfnZ5c5fJqGFOYUF_DY-yuFa8RF64MAHHJV5a4lDkbuCUsU3_UrX4pjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64b0a1f0c.mp4?token=s11sy94gMPHRB6g5TxgoL1JmafqZfR3Xu0acyzPfxBbgheT56ZX4EXMprtu14w_KOSFuYP5B8tC101cWD-LASWJAr72sBpiZJPFMPJ5JGCJC9C9zpZx3r1_pROKDaA3T9uPkYY-zdskle_9lDBOuXk2nQ0zjgkMtHcaAdfQOrztx_5rUmF63AsPTUqR2KswJ8Emssr8_wnk7SIYnIlA5q2xPo4HIqimmnR_E_C7GAxFaeFyhe9EjplwRS-w81nH9AsbaHy0lhnSws5Km0YmChdjQqva0nKZfnZ5c5fJqGFOYUF_DY-yuFa8RF64MAHHJV5a4lDkbuCUsU3_UrX4pjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقدیر مردم شهرکرد از حافظان امنیت در شب ۲۱۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/466497" target="_blank">📅 21:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466496">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhoO67ZKEYY-wesTBTh6NqoOUsisLh_LksjbFzA1WiYHNOxMby-YKxjAAm19hXNWR3rbSGoQN4LqVBWIDMZgQn6bcSDqJ_Z53GgfWk9PwA7iXGDE10O-RdFr3bF_cFRKqndoxKlwz8pjkp9WBhDntomqqswubpi_pjNm0doMyoS9uD4KcfcAcuycnAy-mZeYhoZUy-JKXVNvvC7w0lC9kcNBRYyFWlcx1NdLNDesvcwAHq6fW6tuTAQ2h1rptAxjeC967mIdPBExn5vEY3x0UW0nJS8NENaLX8KDjjChDnONsDzf0D-kTpicxZp2gskOpbi6tLIz8kiR_9ZHYczCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای طرح محرمانه عربستان برای حمله به کعبه با پهپاد آمریکایی
🔹
منابع منطقه‌ای از طرحی توسط تیم امنیتی سلطنتی عربستان سعودی برای پرتاب دسته‌ای از پهپادهای لوکاس ساخت آمریکا به سمت مکه و هدف قرار دادن کعبه مقدس و تعدادی از مناطق مسکونی اطراف آن پرده برداشتند.
🔸
بر اساس اطلاعات موجود، این طرح ممکن است به اقدام پوچ آتش زدن دیوارهای کعبه مقدس و ریختن خون در مسجد الحرام در مکه و همچنین هدف قرار دادن چندین هتل در نزدیکی مسجد الحرام، از جمله هتل انجم مکه و هتل پولمن زمزم مکه، گسترش یابد.
🔹
علاوه بر این، عملیات تروریستی و قتل عام ممکن است در مناطق المسفله، الغزه، الشبیکه و جبل الکعبه رخ دهد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/466496" target="_blank">📅 21:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOTrYGXcSi1rT6u71Cq1Q4XWGvCaI9sRrws9DTjH1qJ0GYRXIpBtzoDLgwc0P2M9ZpHFHcqHvGsp2lyZe7AdypFAZRBgQViK7LD7DII_aN-QyK7nBW6uS6ze7b7BYpyK_GFIycRtjz6QhNsDJkhLBMkyNpwlzbnihkXN6SN_npfiJfsl3PXNqOw2nIII7r3RjVZXxlO6zAFQkRmKQenpbL0lHyPHmRsj_ci5HuF8yAzHiBcwft4gwmGk4Mt368KbTlUKJNcp7JyyX6i-VD__AhHoQWT0yicwfl7dx95rSmKOYgSI5cFjjINk4HF91CnDd4ZyOa1H5umMSzrURW9E8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سوال کوچک‌زاده از همتی دربارۀ دلار کارت ملی
🔹
مهدی کوچک‌زاده نماینده مجلس در گفت‌وگو با فارس: آقای همتی باید درخصوص فروش ۱۰ هزار دلار با کارت ملی به سوالات کارشناسی نمایندگان مجلس و کارشناسان مخالف این سیاست پاسخ دهد.
🔹
اولین سوال از رئیس ‌بانک‌مرکزی این…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/466495" target="_blank">📅 21:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466494">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۳.pdf</div>
  <div class="tg-doc-extra">3.9 MB</div>
</div>
<a href="https://t.me/farsna/466494" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۲.pdf</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/466494" target="_blank">📅 21:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466493">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Scllskb9XVo_llxfJbOPeapS4ejrIX0nBu4BWZrGzke51_Tx8tTgOC0BH0KFZNrANv0swecT9Iej5Q7kwpYS84K0LRX45iKR0peGy53Pdl8_AUe2alTIt2h_rYbFM84vkbxH-rFqkj5E7WskFbflrJ5TJ3XWdP_I4SluWg6VNTFTe3UyTUk4xzkROWDLZ9jztufSaP23EM7tRScVFlzXiPRihTVCcBPs5HFSanXdCsGY8019-6f7e8jRDgdRDft4PcfBVjjQI308VGLF_wmMNsIo5OwacFVRR7Lei-PAFZcOOc9tg-HvgPAiJBjEdMwAPhPdjIzmgYuxc-HArbPskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون ترامپ: ایرانی‌ها عامل گرانی سوخت در آمریکا هستند
🔹
ونس: «چون ایرانی‌ها درحال ایجاد ارعاب و تهدید در کشتیرانی هستند، قیمت انرژی بالا رفته است. ما هر کاری که از دستمان برمی‌آید انجام می‌دهیم تا روند این قیمت‌ها را نزولی کنیم و کمی از فشار روی مردم آمریکا…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/466493" target="_blank">📅 21:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466492">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc19948f.mp4?token=KNEAFjZavv7J1aQnwnlWqSDITpM23_3MM9RSS3JMncQ8l25aO-zA6KRBD9GdK5PRgSGrfp65K_gHa3-3RZLJt-kZt5dW5vBq1BPQCzSZq4Ix0bsObweBRBrnou-u2Urw7uZq5j9z2ChkHZopPxFcnz1ZGOZYL81Gel4O1AzRimC0nJYqiOWoD0ylLVHxskQ8BghR3EWpVBylP9rOMzm-6bwubaYT_zSuSGGVDHwbDStt285aWr8vm_cIHcGlrim0LO0KZy7WPn3UGV6VSc4Q5Ddj4UjJnYRgzmmhgeq0A5Vi2_ob2NbXzA72otifT9wfsvXv6Jgyo68_8-OOVweo8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc19948f.mp4?token=KNEAFjZavv7J1aQnwnlWqSDITpM23_3MM9RSS3JMncQ8l25aO-zA6KRBD9GdK5PRgSGrfp65K_gHa3-3RZLJt-kZt5dW5vBq1BPQCzSZq4Ix0bsObweBRBrnou-u2Urw7uZq5j9z2ChkHZopPxFcnz1ZGOZYL81Gel4O1AzRimC0nJYqiOWoD0ylLVHxskQ8BghR3EWpVBylP9rOMzm-6bwubaYT_zSuSGGVDHwbDStt285aWr8vm_cIHcGlrim0LO0KZy7WPn3UGV6VSc4Q5Ddj4UjJnYRgzmmhgeq0A5Vi2_ob2NbXzA72otifT9wfsvXv6Jgyo68_8-OOVweo8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی ترامپ به روایت ربات‌های فضای مجازی دل می‌بندد
@Farsna</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/466492" target="_blank">📅 21:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466491">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgv9DC1ft_G1NHbmPC5kyPskHIT58mdA44iJuYBX1DKbEnkmtYZko3ozOgp1LbEvRf7vuCO4sIDEH23VGvPpTGRcn257FxbrXJvuqzfkjGf1tuxXQ9CH7v7RmnT-SvvDPbjdtY0PWf8qvFgMqMrqcVGdETtRj42WfWPDYRsYJeVaNa-xPnIZmvjWWE1vDqdZB_veg0iaXG2SKo82TuYJVse_5grjFy3NtbjFHldLx8h6sIX2XIMRhbkiRWt6cxfDdtqM2TWRMadbCVFLU4xi-7bbuHfYi6XD8jzCkokxd5_S7KAyfmEn4YJ-kY1FR_4iUcFD_eHaW_sv9H70YU0v5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله: در حومۀ باب‌المندب فقط نیروهای مسلح یمن حضور دارند
🔹
نیروهای وابسته به سعودی صبح امروز تلاش کردند در استان لحج پیشروی کنند اما با «طوفانِ قدرتِ سهمگینِ یمن» درهم‌پیچیده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/466491" target="_blank">📅 20:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466490">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edec37e973.mp4?token=F2B50kGKP_YpTvLKBkwRNYpA02yjIg8CtH2HF3SDwuNkVvP8HXtQWCEsJ9eZC2BkRVimt2Mg9NCg-K78kEivm7E83TWHZ2DN8HTVMPwqb-thgx-6sMuvIDGS9yc1s_pFNGqXahBe3W7m2cjUICpSWqlLXR2mlegOv_2rXe_SbvIAVOARb_rtleuPtrI2A-TF3A9mm9Pt2lxluzFfSWwnU_YtxjYtWMdVF1YUYDrthOoQsX8LGuQyhaP8m-MtSHbciCqNO3P_mjkDkzH9WF5Fff9Jkk3BwKEzBR-Ul4cDA08it3hAzFQbx2igX7Ku4XMcBRFa7e-UNjJfjGg153IjaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edec37e973.mp4?token=F2B50kGKP_YpTvLKBkwRNYpA02yjIg8CtH2HF3SDwuNkVvP8HXtQWCEsJ9eZC2BkRVimt2Mg9NCg-K78kEivm7E83TWHZ2DN8HTVMPwqb-thgx-6sMuvIDGS9yc1s_pFNGqXahBe3W7m2cjUICpSWqlLXR2mlegOv_2rXe_SbvIAVOARb_rtleuPtrI2A-TF3A9mm9Pt2lxluzFfSWwnU_YtxjYtWMdVF1YUYDrthOoQsX8LGuQyhaP8m-MtSHbciCqNO3P_mjkDkzH9WF5Fff9Jkk3BwKEzBR-Ul4cDA08it3hAzFQbx2igX7Ku4XMcBRFa7e-UNjJfjGg153IjaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح جدید کارت سوخت، مردم را پشت جایگاه‌ها سردرگم کرد
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/466490" target="_blank">📅 20:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466489">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b1a1df1b.mp4?token=Or0t9rHPIAjXdUzNOQ6hMu0BOJJ7Yhf8bn_7diNEmK7PhEDNObS4GS7AyQbV-xvSeppfGI3A-nURh-lAL0UJcAjborrRmm71ZijC_as5tvlXLhCxpnZXSXZJmfwH5_NHZzONZzq1Ymwv5riElTNUZui4wRTpjCwJ_BOhYHhsAN6q4znLdGgKgAlAo_7yzpVXqjmYv3_OF3jO45KgO2agnEW-xmeVOWYdzcXZZl1x6EOZBng8POwEoyeVHcROH2nq6cbZEU_Jfvd6C7AlyN4MWEpol6IQmkzSpnKF_xbMG1Hvj0Av-faOIpMUYgWpUYK3jAGvxGCMaY9KaNl-o8534A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b1a1df1b.mp4?token=Or0t9rHPIAjXdUzNOQ6hMu0BOJJ7Yhf8bn_7diNEmK7PhEDNObS4GS7AyQbV-xvSeppfGI3A-nURh-lAL0UJcAjborrRmm71ZijC_as5tvlXLhCxpnZXSXZJmfwH5_NHZzONZzq1Ymwv5riElTNUZui4wRTpjCwJ_BOhYHhsAN6q4znLdGgKgAlAo_7yzpVXqjmYv3_OF3jO45KgO2agnEW-xmeVOWYdzcXZZl1x6EOZBng8POwEoyeVHcROH2nq6cbZEU_Jfvd6C7AlyN4MWEpol6IQmkzSpnKF_xbMG1Hvj0Av-faOIpMUYgWpUYK3jAGvxGCMaY9KaNl-o8534A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ نفر از عوامل اصلی جنایت منجر به شهادت مظلومانه ۴ مأمور پلیس در اصفهان اعدام شدند
🔹
علیرضا سپاهی و علیرضا رئیسی ۲ تن از عناصر جنایت اصفهان که اقدامات فجیع و وحشیانه آن‌ها منجر به شهادت مظلومانه ۴ نیروی فراجا شد، پس از رسیدگی به پرونده و تأیید حکم در دیوان…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/466489" target="_blank">📅 20:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466488">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
منابع رسانه‌ای از شنیده‌شدن صدای انفجارهایی در پایتخت عربستان و توقف پروازها در فرودگاه ریاض خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/466488" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466486">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
پزشکیان: هربار بازرسان آژانس به ایران آمده‌اند، مراکز هسته‌ای و دانشمندان ما شناسایی و پس از آن این مراکز بمباران و دانشمندان ما ترور شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/466486" target="_blank">📅 20:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466485">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌ ‌
🔴
پزشکیان: حملۀ آمریکا به ایران با هدف سرنگونی نظام، موجب انسجام بیشتر ملت ما شد و به امید خدا از این برهه نیز با سربلندی عبور خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/466485" target="_blank">📅 20:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466484">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
پزشکیان: فشارها را خنثی می‌کنیم
🔹
مردم ما استوار ایستاده‌اند. همسایگان بسیار خوبی داریم، ارتباطات خود را تقویت خواهیم کرد و فشارها را نیز خنثی می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/466484" target="_blank">📅 20:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466483">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
پزشکیان:  آمریکایی‌ها تاکنون ۳ بار پس از گفت‌وگو به ما حمله کرده‌اند و این نشان می‌دهد که آن‌ها دنبال گفت‌وگو نیستند، بلکه هدفشان ساقط‌کردن نظام جمهوری اسلامی ایران است. @Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/466483" target="_blank">📅 20:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466482">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌
🔴
پزشکیان: با دشمنی که هر روز ترور، تحریم، فشار و تهدید می‌کند و پیمان‌شکن است، مذاکره معنا ندارد و ملت ما نیز چنین رویکردی را نمی‌پذیرد. @Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/466482" target="_blank">📅 20:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466481">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
پزشکیان: مشکل ما با آمریکا این است که هر بار به میز مذاکره می‌آییم، بلافاصله جنگ به ما تحمیل می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/466481" target="_blank">📅 20:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466480">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با پزشکیان هم دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/466480" target="_blank">📅 20:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W99xReirGv2twbiNlADocES19enBZ7sdBIIb_1lz3bHE_6Lnl1xu0MT5jvDyGQedSIOW-BkwzU220QUo2-i6ARtd2SfMAZH9OJtvkmFf_54GWRlTfJZWgM9D_-wenvpIq6NBVhIQezfL7MybE2xkGnKnVHnPKL3UDUvvFq0p0R8PNI0qsMcE6Dp4nJHC4fMGDmZ74L3mmDShCu7zuuTXVwP_DEDmzNFv2wuLtjGIG6SI-Csdl7q5WwT16qeSbX-6CaOwRSU0jVYjHmaqiOqA-bfo8UuFPBhBVPhsqcVLmWtKPvdfGmizkgfYw7YOtXOYLi_nGgeRLEBY5Gh74lPPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/466479" target="_blank">📅 20:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466478">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWIGfb7xea2LRp2NMXY9bi4eIRHJvA1PUZpy-gVbj6EGiSxwusLYMh3G6TG9Kaf-0l7OxqJs3_15Uq5kLkHOYxl7ZPk_0yCu_saF0Unr6mnFOnoRrWYE93iRRMG0PXhpgWvoL0OICJM-ZE6GGawESpBBSURqcnNvFMOLONq9SjGdv29BT3YUpHVSMP4IjzocY0ahoJtvBXVLF7Y-Y6VzeJGPHenCh9YYu-y0bj0STjSDh6N9-47eZKKfDQ-MciXk6R-mmoyf1cOMImIQKgL57n6rJqDRhm8hMYMw3CieBBq9Wt-eqNc4wvdzVmPGFPdm5E5j2Yyb9O8mpmSqpxo1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طارمی ۸ زندانی نیازمند را آزاد کرد
🔹
مهدی طارمی، کاپیتان تیم ملی با مشارکت در طرحی خیرخواهانه، زمینه آزادی ۸ زندانی نیازمند استان تهران را فراهم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/466478" target="_blank">📅 20:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
یمن آسمان عربستان را منطقهٔ پرواز ممنوع اعلام کرد
🔹
مرکز هماهنگی عملیات بشردوستانه یمن در صنعاء به شرکت‌های هواپیمایی هشدار داد که حریم هوایی عربستان به‌جز مکه و مدینه «ناامن» است و صحنه عملیات نیروهای مسلح یمن خواهد بود.
🔸
صنعا اعلام کرده پس از این هشدار…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/466477" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033bb92fbc.mp4?token=PCk_xgI7d1xaJE0449efWnqarMYy9oDahfdD3N8vwMdFGDQMSUv9aRHwLzJFhQR8m2flT-QSkP7n8LbIFwC26D2gzgAHwmNrqhdUU3PJjdshgA1JzGAaPPK1Iw3uMFsxYRKdwm4zeoA2t8GRRsenC4t-QUrVb5fwNlGOp9xmIMq9pMUjIwjkK8bCYcR7LyO63MOvCRzy74DOUPlnFqVB37jRkrHNiSnmy-z8hHtx3XOZ5vwjHa5lg5olAiLSFZMXT7BXRafpBNYkhqWUtTtJQvnM_N4b4ELDh315AkYWJk4llwN9r0Y1at3f1n-DYpypXUZghMPSY1Vmo0U4kxq-qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033bb92fbc.mp4?token=PCk_xgI7d1xaJE0449efWnqarMYy9oDahfdD3N8vwMdFGDQMSUv9aRHwLzJFhQR8m2flT-QSkP7n8LbIFwC26D2gzgAHwmNrqhdUU3PJjdshgA1JzGAaPPK1Iw3uMFsxYRKdwm4zeoA2t8GRRsenC4t-QUrVb5fwNlGOp9xmIMq9pMUjIwjkK8bCYcR7LyO63MOvCRzy74DOUPlnFqVB37jRkrHNiSnmy-z8hHtx3XOZ5vwjHa5lg5olAiLSFZMXT7BXRafpBNYkhqWUtTtJQvnM_N4b4ELDh315AkYWJk4llwN9r0Y1at3f1n-DYpypXUZghMPSY1Vmo0U4kxq-qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناراحتی اینترنشنال از شادی ایرانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/466476" target="_blank">📅 20:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هشدار لندن به اسرائیل
🔹
یدیعوت آحارونوت: سفیر انگلیس به مقامات اسرائیلی اطلاع داد که لندن در صورت عقب‌نشینی نکردن اسرائیل از بستن کنسولگری انگلیس در قدس، ۲۷ دیپلمات اسرائیلی را اخراج خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/466475" target="_blank">📅 20:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0u3oPP9tY9igjfofWGA7N9w2f0EUXL3NYQppy-c5ceZwXsBEQFYBi8qBv1Kg9CrB1WLMz9Urc7uW76q2VZDyQJVAZxmHHTl80P-x7LyW1l6sm03YK6LcEPcDUFjfcsGONUH2RPo0Em6MB7uyRUWXXIoV4I2c24YNxEOEHQ1MBdmnLBwGLQZv2fQXvsrtq-yE5_pgE0Io5yAMlUku21ffUhU_C66expnWl1RupT4bSnhE8I-5L2hVNRxtEl6ns3_d-hljvhUs9XVed-Sp1nX7YbMLweeUvueUM338DfvqZaoOhyzmkxD8HYcg3CA75mYUhNGq6B0F_WWe_WP551jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور وارد دوحه شد
🔹
این سفر به دعوت رسمی خلیفه بن حمد بن خلیفه آل ثانی وزیر کشور قطر انجام شده است، وزیر کشور در این سفر با همتای خود و برخی از مقامات قطری دربارهٔ مناسبات دوجانبه دیدار و گفتگو می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/466474" target="_blank">📅 19:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0094da11e.mp4?token=mx8Tw0YBVhIuc_gI4o5NJbZizUxHXJCRtxlSqTEomb11Nn4sIfCrH0ieJmnANHBpcboQ_vaGZ6uAS-r7rrAxrJd8rtNaJoxH9OSnl8GgkC4E_v6wImjY-PWyj9HdvEhkxQOJbqpGGou3POEckdUAlUaIFOekuQloNLgshB92QFxijDyHnVv7GFlU8GTjnbjkCYIDgF3P7vcLOndetQVqrTrf23dWAok_2q6etVAhm7Walxq0Y8a8b77PzpRYVhfAUa29fFcmuGceG8anKlCf_CEdrU2E5zPLjVNpgbsBi3ninYyga9-WE9YxMgFOKTy_YgG6D2gx_lddoaAIjnyo-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0094da11e.mp4?token=mx8Tw0YBVhIuc_gI4o5NJbZizUxHXJCRtxlSqTEomb11Nn4sIfCrH0ieJmnANHBpcboQ_vaGZ6uAS-r7rrAxrJd8rtNaJoxH9OSnl8GgkC4E_v6wImjY-PWyj9HdvEhkxQOJbqpGGou3POEckdUAlUaIFOekuQloNLgshB92QFxijDyHnVv7GFlU8GTjnbjkCYIDgF3P7vcLOndetQVqrTrf23dWAok_2q6etVAhm7Walxq0Y8a8b77PzpRYVhfAUa29fFcmuGceG8anKlCf_CEdrU2E5zPLjVNpgbsBi3ninYyga9-WE9YxMgFOKTy_YgG6D2gx_lddoaAIjnyo-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل اسبق بورس: عرضهٔ ۱۰ هزار دلار به مردم کار بسیار اشتباهی است
🔹
رحمانی مدیرعامل اسبق بورس: نباید خزانه ارزی را خالی کنیم، الان کلی دارایی ارزی در بانک مرکزی است که می‌تواند تبدیل به حساب‌های سپرده ارزی شود و از طریق صندوق های ارزی یا از طریق صندوق های ریالی عرضه شود و هر واحد صندوق برابر یک یورو یا دلار باشد و قدرت بانک مرکزی هم بالا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/466473" target="_blank">📅 19:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466471">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiEfnR7_cDB2_dVVUdbWb6uqzRmoqWX59qd4SUU_gc3KS0x1EXTSFion2Lmx8FIBZcu1DB6WCMl7dw8MuSYc3hxMwtUkM7C0wQ-iWXCt28GWBtD9Z4MBhri_EIYcka6iNgYyF-rDxjK7SiAIlbFAye16sdNkJ-jvIhoDdG9EX4E5vwNgjXfJbHte8SJpMj2KKC-ztaJYL_k8gaHoJ5qvToZrHbTLw_dZbK9Bado3I5Uob8fFKa-KDq0Fgt0Ab2HUqzn6BY5g0XS8dEL9JtDHKKl8ec07nutBLWyDzj2x8oB8tY0uUEuIggSCGa6Qf-_Xw8W7T9spgZIUy9M4I08ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه ۱۲ کنکور: شهادت رهبر مرا از درس دور کرد، خون‌خواهیش برگرداندم
🔹
گاهی یک داغ فقط دل آدم را نمی‌شکند؛ مسیر زندگی‌اش را هم برای مدتی از ریل خارج می‌کند. رضا سعیدی ابواسحاق، دانش‌آموز روستایی چهارمحال‌ و بختیاری، بعد از شهادت رهبر شهید آن‌قدر از نظر روحی درگیر شد که از درس فاصله گرفت؛ اما یادآوری توصیه‌های آقای شهید درباره درس خواندن جوانان و ساختن آینده کشور، دوباره رضا را پای کتاب نشاند؛ همان پسری که حالا نامش با رتبه ۱۲ کنکور گره خورده است.
🔹
حالا رضا سعیدی ابواسحاق، دانش‌آموز بسیجی روستای ابواسحاق، در جمع برترین‌های کنکور ایستاده است؛ جوانی که می‌گوید امکانات آموزشی روستا با بسیاری از دانش‌آموزان دیگر قابل مقایسه نبود، اما تصمیم گرفته بود خودش را «محروم» نبیند و کمبودها را با تلاش، کمک معلم‌ها، حمایت خانواده و استمرار جبران کند.
🔹
او می‌خواهد مسیر علمی و پژوهشی خود را ادامه دهد و در آینده بتواند سهمی هرچند کوچک در پیشرفت کشور داشته باشد.
گزارش کامل را
اینجا
بخوانید
@Fars_Chb</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/466471" target="_blank">📅 19:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466470">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6Pqkzg0pgh1hs5jZRdBYUgOs4fyYRWKVfaDj_drQMwVKohmuF_we2XIvxrRRtN9NsVK6NgKvi0pVLrpEo5BInKdCPlAVgTe2FzGiNRt0t-qa804lmEnICKt7FpJdHS8ari5C29UPWsjqba4ZwEcp_twi6rEya4824dkMlu6n5rwaF9oL-_Yb84Ak8ieL4L6tkB6RdhKB5qDHZ70rnCGdicDo-0Ac1CSRhCQ1jplGpTmjPQxHq5ajl_PBxWWT4ANTfmI_gZLixxB--2QxQnMomi4LK0LNBmgqW_9ml_HMl3lK0I6GTLjzzX-H8I3P6FN0emBoPrKcKPbuA-1qH-4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قفقاز نباید به محل رقابت ژئوپلتیکی قدرت‌های خارجی تبدیل شود
🔹
رئیس مجلس در دیدار با وزیر خارجۀ ارمنستان: امیدوارم به زودی معاهده همکاری راهبردی میان جمهوری اسلامی ایران و ارمنستان نهایی شود.
🔹
قفقاز نیازمند آرامش است و این امر باید با تحکیم مرزهای…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/466470" target="_blank">📅 19:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466469">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCy_hJqPDsVbefBSqhC2Ca06Eqk8cGdM9d0C1_7MfjcCyf8AwCm4-xpRZ9AqrpXgtGD7QNsxl1kYum2SCRcGOdCZPdNFk3Zc2Ljpjh4ziJD-CLHaRRZjubBQl83SQQkDvrbGEe-2WYzkRPJHF0dkUNUxIKVttaa86CcX28zK1k-lHCBJbCAnGt4KoY38A1MqM-OP4HjvNiB3MQuK-RvHC8HG-WFtaBM-CjzGi2vnO0Gw-4b9TbUbd3VkNPTGgWYn0fC3tADzUl7SntIMrfICoiiMIsX0wzReoryjWQJ6jZRwO4MsxJqV6zBnK57hjzQ9bsVwHnJvPFtvI36kesWpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/466469" target="_blank">📅 19:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vL7a7cQ3ci3KcposzaYievMkjFUjO3wkV1E7fxIKkDEgxR6aaXJDex8he2ojZ7MccO-YeOXbwUAHMD29z42X_RLwCylkx2Q2QnNVvHSI3HsXTpaUV6UbbK9yY3KHfK0BDcw5eITyAu7BeH-q3oodMMF56JfXWzdZYmwAlbwbTqH8pzDA30BTbE0aHChBTgcVXEhyijffPjdZ3ODUnrV9-mTM34IWXh03WTNK9TllhOBS8KHqr99K9FndN9rpubv6GXlE2zrwF0K13gpGZlHJC2bii5h3BZ3bgxtxQQFs84kL9NWNDsde_Y-YLzjD5j9lalabG49muAZ3Skby3xscdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxGHtTqp_pjV7wolQYos_E3ZpiUmCw3pLBfqj3mBiljMgUbKxO6ahVT0uCMaEcD_mNXUuuEvMieXW21lGYCUcIaupWnityRO0vRMsC5nsZ3qnWvvLChdFXhpEv6sE5-4iJpYpkQgTOP32hrJ78LTrz_ojeumUBbNiD10zHevWL1RwouNR6U6aVrer3FvKF43ciN7tgINfw4bXX3aPEZCcocDyDNPSdNm_UvT7q0gMq2Cg4L9jUM9rIzqTX6V6I9U6BwCboqO9IVPa6pspYROaljMvx_G6FkNqQtdWShFpK1p_i_YVFkSKw7-L5-vrruH60YPx0mKGsWSUvtCkoqTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sBbxHZOhT08ldJi_6iaairdt9WIFGMrwjd2jz91M2bkwIkU_lL9_4YB9UtbHYYNvXu4tb2dbSZ2jTttcDxbBOtSekW1BlWdmFyM7AGoOXRxrhLTXcB0Hjtg6vEarpNachv6HPsik9orVx7REO-r27fkSqFS9glM9yx4IEHCUroyh103ckvxLx01tOCp1OPWU56_v0i963m_6nB57E2nA28jb4UozgjzPhWITZfoExPcdiUdK4M0XwzTZGKfyqGAziuaGnu1vO81cYaWrYwHZS9XzmAF6HCx8yxwzIevs9GT1WKT6AwA5ZAtXybWXH6HikA8t2n_46zJmpQRCyq3LKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر خارجۀ ارمنستان با قالیباف دیدار کرد
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/466466" target="_blank">📅 19:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5885c04db.mp4?token=upBcWRRnGJ2gh2YKXtqrjX13MuTGZ6lUGyWi6eFb3O8WNCE-FQFWw5ADg5T6lc50YCnrI7D0w2rv3wWzZF-6LuTipLeexLdcciUN1PMDfpfNlhXwmgIlFufxbaApAW4ovqH9fWCsuOiXatgEyLD1qXVW_xzJoyNw_vtpAdQuvyKWUK81TDJztvT21CjVv6rVxAVeU05td5UdL8gP-3TiprCY8t0QzSphWx7TdGPHbwnTnabGE4Rc1dXZT0BZy3WtVSZwO8xupNei2BNl87cG7_OBS_lkmPFKL5xDI19z8WZHbkmiU0cIReUQ0ED4093Ga8-qkHPkxyDNkljvFuKTU3051Ha2jRHr0_awm0nQrxz-zSmG8XyIbBO3IjTnK01iz_AqdVG6RGZiarym6IBoe8XEl2voBQGPbSjJK7qDh9NnTzjqgJ8AEN66gKIiB1i_atis8tH7bML5Eh4nIAnJ3nYi5Y3RhebUUMuIbz7k3I558pNjHSh72ZvoneIb6OEfybAh9ZkXMRVISpEr1lpoZBE3qiWd3jxBoiblyEyVd4EksrqxsGImo_I_Z_IfZZsEB-vU4vl7yMupODWMSG9MUl47GvFyg0yAH13HeVFT9dEe_qXFcPdjboXyaj0C2PpIFlLFySZrvNaAap5RI04uiGxlJDY1fL6tL0jbKAp9mW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5885c04db.mp4?token=upBcWRRnGJ2gh2YKXtqrjX13MuTGZ6lUGyWi6eFb3O8WNCE-FQFWw5ADg5T6lc50YCnrI7D0w2rv3wWzZF-6LuTipLeexLdcciUN1PMDfpfNlhXwmgIlFufxbaApAW4ovqH9fWCsuOiXatgEyLD1qXVW_xzJoyNw_vtpAdQuvyKWUK81TDJztvT21CjVv6rVxAVeU05td5UdL8gP-3TiprCY8t0QzSphWx7TdGPHbwnTnabGE4Rc1dXZT0BZy3WtVSZwO8xupNei2BNl87cG7_OBS_lkmPFKL5xDI19z8WZHbkmiU0cIReUQ0ED4093Ga8-qkHPkxyDNkljvFuKTU3051Ha2jRHr0_awm0nQrxz-zSmG8XyIbBO3IjTnK01iz_AqdVG6RGZiarym6IBoe8XEl2voBQGPbSjJK7qDh9NnTzjqgJ8AEN66gKIiB1i_atis8tH7bML5Eh4nIAnJ3nYi5Y3RhebUUMuIbz7k3I558pNjHSh72ZvoneIb6OEfybAh9ZkXMRVISpEr1lpoZBE3qiWd3jxBoiblyEyVd4EksrqxsGImo_I_Z_IfZZsEB-vU4vl7yMupODWMSG9MUl47GvFyg0yAH13HeVFT9dEe_qXFcPdjboXyaj0C2PpIFlLFySZrvNaAap5RI04uiGxlJDY1fL6tL0jbKAp9mW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از شیوهٔ زندگی مبارزان لبنانی تا اهدای چفیه متبرک رهبر انقلاب به فرزندان شهید حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/466465" target="_blank">📅 18:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466464">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‌  علیرضا سپاهی در روز حادثه بنزین روی مأمور ریخت و او را درحالی که زنده بود سوزاند
🔹
با توجه به اظهارات متهمان دستگیرشده، تصاویر مشرف به محل و اظهارات مطلعین، جنایتکاران در طول مدت این سه ساعت مشغول هتک حرمت و رقص و پایکوبی بر بالای پیکر مطهر شهدا بوده‌اند.…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/466464" target="_blank">📅 18:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466463">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEQHBo7h1nAIWXzlVpyLwaMftmfQqLNsav61E7DObU4J_VxmDiaGrP8kA6e2mQdpLZm_k7p3DJwgsP6AgGYGdElH4j78_tyGfZK4Zq3Nnh8htR6pBa1dz3RkoQTv5osdOMGRTCeQP3jmFgAnm2ioRQEEHuIfMT38JGA55xqC-NWQXQ-JEJ5PcRXhmsdS3rgns8uLG4paXKlSmRHlYHCbtFW1LlA9CfeYIimTMlVrNMIpxQRGABTw7D7qxASYISg9gO59m8n2SWzoOpDBoNbP4iEUB0dPFd-bhZ4UmvmFrPNvJD-ffLavohbH4IeiV2PN6qWzo7kysI4UUxuKqQxIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه علوم پزشکی بقیةالله(عج) از میان داوطلبان خانم و آقا دانشجو می‌پذیرد
🔹
پذیرش همراه با بورسیه و استخدام رسمی است.
🔗
شرایط و جزئیات:
وب‌سایت دانشگاه
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/466463" target="_blank">📅 18:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-_XJ79I2jretP3peR3-J6sZCCLwkLaXqGunOHXgNX5iqDrkeWNiW4JrdDZ_7YshG7tIyawb9TCo9Woj6O3nx5QIBamB5zOvDstC5hqrdBkDESABAH2OW9pJIw2ycWrrvQeQRFnpQQXDu17XiOd51PgCz5E6RLpSNFVYItjaLVf5LXD-qN9VEzZEUj749W9RuEyTvZ4CdUcyC5CSgvjdxCLJ6Pn9jBLWrQYnMu8a0eH77QEOeSCtM_64TialeL2gmLcHS4qFBWtIJ2esXY9qReuKoP0inQJFCK3zdYeVhYGY4exfpLlqfiLjWnSYZwoOlcw0B4PJfViarEJNFFbuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدرقهٔ کاروان ایران برای بازی‌های پاراآسیایی ۲۰۲۶؛ محمد معتمدی در میدان انقلاب می‌خواند
🔹
مراسم بدرقه کاروان ورزشی ایران برای حضور در بازی‌های پاراآسیایی آیچی-ناگویا ۲۰۲۶، امشب، ساعت ۲۰ در میدان انقلاب برگزار می‌شود. این مراسم با اجرای محمد معتمدی همراه خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/466462" target="_blank">📅 18:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lth64xnLtDkR1Xubc4M2TPI8Qs6FrMjngSk9WbWQ-Cx0nxS2vWxCdh_QkGQuQbxAnnK8oVYL5ifSj4sJIGTXuylEJQeSWpn7j-4u8xwTwTs2vlr8_6M9IMUJjOsatwQaSBQ36qt6Rxq8VPOLqQ5JToxpHGXp3bxbCwIhzwMrpqnpT4cmjn4OfEA5g-SrmEGmCMN-qhSkWQTE3InMBwV7Iu_kPuERMQFUBSDTXpqDsr6qcODpcP6-YEbITKPHvkVWfLCkWTbp5H5viPjp45g-c8b0mb7XkyIZJv4eMfxkqF-wQKfh9kqm_Zg_vSmhjziNMbD-LgUQjVtogp9WZtQAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانۀ حساب‌های مازاد همچنان پشت پرده رونمایی
🔹
طبق پیگیری خبرنگار فارس از بانک مرکزی قرار بود سامانه «حسام» هفته گذشته به‌صورت رسمی رونمایی شود اما با گذشت این موعد هنوز این اتفاق نیفتاده است.
🔹
نیمه شهریورماه بانک مرکزی اعلام کرد شهروندان بالای ۱۸ سال می‌توانند…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/466461" target="_blank">📅 18:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466460">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
یمن با پهپاد جدید به سراغ مزدوران سعودی رفت
🔹
در این عملیات پهپادهای انتحاری «شواظ» که تولید داخلی یمن است برای اولین‌بار استفاده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/466460" target="_blank">📅 18:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466459">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfLEsADLs4-5cBDp6rS_nIjuvAKg1KCUiiG2ZZa0zKpF3Ir_Qbbcvku0mBESuaTTf0G29sqpPV01lKtxH8ntdTIbVjSQYGceNbn8m-R0p-doHo2hcigOZ3_CtQmkbhxBiB6bCXTMtTXoaWKanBudJDncuQ6tkKlu7eaGa40AMn74zImAeKDq8ITCZDrN1p_RKOFuv-hVEKduVLdpvahbXAmSm71-R2eEXOBvFzwwGUhTJQUqgxgW2GzM_YR417YwlQeOPiZWI-AA78r45WLySHDc2Ya35NlWFATt3Bcnd2_DYbwxh-9xEX93fzAOxa5y_nXb3jjdznxhHaMh_yochQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: خطای بعدی دشمن، «جبهه‌های تازه» و «غافلگیری‌های بزرگ‌تر» را درپی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/466459" target="_blank">📅 18:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466458">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌
🔴
خط لولهٔ نفت عربستان بار دیگر از کار افتاد
🔹
خبرگزاری فرانسه به‌نقل از یک منبع انرژی عربستان گزارش داد خط لولهٔ راهبردی «شرق-غرب» پس از حمله به یک ایستگاه پمپاژ در شرق ریاض بار دیگر متوقف شده است.
🔹
به‌گفتهٔ این منبع، خسارت واردشده به این ایستگاه «شدید»…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/466458" target="_blank">📅 18:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466457">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hir-A1rIA50EXyuTl51b8yHJ-DFZbDfRwsdrFdRjioF_Lgw0kOF3ze4PBF6Jxk9-Ivo6aNqRoYQwv_dKdSqAZ3UTV10OeXADot5ZKY6odQyYMDFgafqATZxylxR17VAYVvGmXeAnKcJKmUB_dqle0MqFN6qQFbBE2HxC2loA7D_bdgIY0XCZs3sB14kL7GTF0aZLJ24XCmz1lJ5xBbNgA_WUw3j6j18ep5-gqg6UKQzxwrJTildn8R0vHPq8hSD2O_LRoIup643dAXYeF4Z7YGKPV_AIyqWqDQd1ANbvlYqkCTW99KBNQQ6pn9HNSrekzH4OoVc9G7kfDeAdNOCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح «تورم صفر» در ارومیه هم اجرا شود
🔹
جمعی از مردم ارومیه خواستار اجرای طرح تثبیت قیمت ۱۲ قلم کالای اساسی در این شهر شده‌اند؛ طرحی که به گفته مطالبه‌گران می‌تواند بخشی از فشار هزینه‌های زندگی را از دوش خانوارها کم کند.
🔹
در این پویش از شهرداری و شورای اسلامی شهر ارومیه خواسته شده است با بررسی سازوکار اجرای این طرح در تهران، امکان تأمین کالا، منابع مالی و نحوه نظارت بر اجرای آن را بررسی و در صورت فراهم بودن شرایط، این طرح را در ارومیه نیز اجرا کنند.
🔗
برای حمایت از این پویش، روی
«
حمایت از طرح تورم صفر در ارومیه
»
کلیک کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466457" target="_blank">📅 17:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466456">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atc_oaXorT_okWElvT6vwil8b2W4esBctB6V9IoBt9MbqBE7JnI78d3QLk_Z0AMC7hGfWQX7tIuaJXSFS9KSl3Mk3qciueURPDyGTD9d-qU_Q7irT9hn-2topT3Yk4N7q4mjr6h0SCV1RrWuqs_wUnC3R6l8987YUhYTvS7pxgfx4b4SZrWN9j_CUolW9uwqE8t8kh2AFgi-S9AT_2ZaNR1_cIffERvO7JsFNIzukCpNL5XyJdbliib2mG9z-PBhHsLiQiwUoroOuTJxYQP2xJGRL8FltmWCLlzcw1H4oCIb-sBvVuNCw3WaWcaeO-_1GYAY9jRHd7FGdutREoSmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور از مسیر غیرمجاز تنگۀ هرمز، به روایت ملوان هندی
🔹
یک ملوان هندی با نام مستعار «سینگ» با فارس گفت‌وگو کرده و روایت خود از عبور کشتی GFS Galaxy از تنگه هرمز و هدف‌قرار‌گرفتن آن را بازگو کرده است.
🔹
او علت اعلام نام مستعار در گفت‌وگو را ترس از پیگیری حقوقی شرکت مالک کشتی معرفی کرد.
🔸
سینگ می‌گوید: کشتی باید چراغ‌خاموش از هرمز می‌گذشت. رادار خاموش. بی‌سیم خاموش. کاپیتان گفته بود هیچ وسیله ارتباطی روشن نکنید. حتی ملوان‌های ارشد هم بی‌سیم استفاده نکنند.
🔸
مسیر، باریکه‌ای است نزدیک ساحل عمان. عمق دریا حدود ۱۰۰ متر. عرض مسیر به قدری کم که کشتی‌های بزرگ تقریباً شانسی برای عبور ندارند.
🔸
مسیر عمانی جایی برای دریانوردی نیست زیرا عرض آن بسیار کم است، عمق در مکان‌هایی کم می‌شود و صخره‌ها بسیارند و خطا یعنی مرگ. عبور مفت و بی‌خطر از اینجا ناممکن است اما کسی این را به خدمه نمی‌گوید.
🔸
پیش از عبور، کاپیتان به خدمه گفته بود: «آمریکایی‌ها مسیر را داده‌اند و مرتب در تماس هستیم؛ جای نگرانی نیست.» ما هم چاره‌ای نداشتیم. باور کردیم.
🔸
در مسیر بودیم که ناگهان کشتی هدف قرار گرفت. عرشه به هم ریخت. صدای انفجار آمد. کشتی لرزید. همه‌چیز در چند ثانیه.
🔸
پس از اصابت موشک، کاپیتان تلاش کرد با نیروی دریایی آمریکا تماس بگیرد؛ اما پاسخ‌ها دیر رسید.
🔸
خدمه به کاپیتان اعتراض کردند که «تو گفتی امن است» و «ما را به کشتن دادی».
🔸
به ما گفتند که آمریکا همه‌چیز را هماهنگ می‌کند. اما وقتی موشک خوردیم فهمیدیم که آمریکا کاری از دستش برنمی‌آید.
🔸
کاپیتان گفت آمریکا هست؛ اما وقتی موشک به کشتی خورد، ناوهای هواپیمابر بزرگ فقط تماشا کردند.
🔸
اکنون در شهر کارگری می‌کنم. حتی با ۱۰ برابر پول بیشتر هم حاضر نیستم دوباره به این آب‌ها بروم. جانم از پول مهم‌تر است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466456" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466455">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
یک منبع در مجلس: مهرداد اخلاقی برای تصدی وزارت دفاع به مجلس معرفی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466455" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466454">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مهلت تعیین‌تکلیف وزرای ۲ وزارتخانه به پایان رسید
🔹
سخنگوی هیئت‌رئیسۀ مجلس: براساس اصل ۱۳۵ قانون اساسی، رئیس‌جمهور می‌تواند برای وزارتخانه‌های فاقد وزیر، حداکثر به مدت ۳ ماه سرپرست تعیین کند.
🔹
دولت از ۱۹ مردادماه با اذن رهبر انقلاب، ۴۵ روز فرصت داشت تا تکلیف…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/466454" target="_blank">📅 16:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466453">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbdaac517.mp4?token=LTZEtjMLPaZYz0xn3_8WbpLJdqqvGw2hQ_rn4BWboano-Dr8c-EArlfkVDpfrQiXdBh5ZoRXGS5N5Z8DAft8CIEa0rfugM5HOJvivRaW_1SnjBOV5ZlCVs8LTUCAEboxlImp8hnvpsdOzpfoCB_EcUd9wXRb6lQYe220iRYdaXrQoh_94MtJFVVtKrTMLmykksQXFs7YZ2k_LWozC7ZOVJeITzbYOiFSnv-_weVsdrkq8W__Q-fC4FPiC1gMouwBI4myMlrL8fDm7iPrmvA8iudzV1QCVh7WHl-OniXxN_SITcqn0BDWuBd78v4QsdKd0coO5A30b8XphtyyaDcywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbdaac517.mp4?token=LTZEtjMLPaZYz0xn3_8WbpLJdqqvGw2hQ_rn4BWboano-Dr8c-EArlfkVDpfrQiXdBh5ZoRXGS5N5Z8DAft8CIEa0rfugM5HOJvivRaW_1SnjBOV5ZlCVs8LTUCAEboxlImp8hnvpsdOzpfoCB_EcUd9wXRb6lQYe220iRYdaXrQoh_94MtJFVVtKrTMLmykksQXFs7YZ2k_LWozC7ZOVJeITzbYOiFSnv-_weVsdrkq8W__Q-fC4FPiC1gMouwBI4myMlrL8fDm7iPrmvA8iudzV1QCVh7WHl-OniXxN_SITcqn0BDWuBd78v4QsdKd0coO5A30b8XphtyyaDcywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
حضور وزیر ارتباطات در خبرگزاری فارس  عکس: هادی ه‍یربدوش @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466453" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466452">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3e3b132e.mp4?token=Wso5dBYu8qmeE9HgyqJRfLEcOqdd1jfdnYkizt0NnKfhMgYfXE_UE9tK4HwTBLKFFyqUDdFi4lIp0l_Kjiq_sFGTgeONsxndAww9jPVO06fRu67FQMVX2j3ySqbHFevNIX7JalAUGw09D0hHkFsndIrE9lRan2aYA_tg-sReRoOOBJISRg0mI2SIf6XpqSmqmGK3c1Q1JazgOF5JLUG_y3FmmWeJ0k1BI8AWdZYO7v2dUUVgcPsx5c1yo_yC4IcSpddGjBPe-R1Ou8U18NCo_tdu4_CVB1s2jlALKxt4uTwo40HWJuZg2N5IR61aCm84UFt-cZx6JHUtnrpVcOLpag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3e3b132e.mp4?token=Wso5dBYu8qmeE9HgyqJRfLEcOqdd1jfdnYkizt0NnKfhMgYfXE_UE9tK4HwTBLKFFyqUDdFi4lIp0l_Kjiq_sFGTgeONsxndAww9jPVO06fRu67FQMVX2j3ySqbHFevNIX7JalAUGw09D0hHkFsndIrE9lRan2aYA_tg-sReRoOOBJISRg0mI2SIf6XpqSmqmGK3c1Q1JazgOF5JLUG_y3FmmWeJ0k1BI8AWdZYO7v2dUUVgcPsx5c1yo_yC4IcSpddGjBPe-R1Ou8U18NCo_tdu4_CVB1s2jlALKxt4uTwo40HWJuZg2N5IR61aCm84UFt-cZx6JHUtnrpVcOLpag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسیدگی چهره‌به‌چهره به مشکلات زندانیان
🔹
با حضور رئیس دادگستری تهران در ندامتگاه تهران، زمینۀ آزادی ۳۰۰ زندانی فراهم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466452" target="_blank">📅 15:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffcc2cb6f.mp4?token=Dt5KDZIa3NBHX8xkyB3TnRilAqR1ZMju4gMi9Ylv6DEA533fKlxZYjxNOkhus7wZmwKo3IFPOrmhMvOwfWZJM70xau0JGVfl46mlUZ8Gxs_qmZw6KhI1F0_JzExaA-e5OX_7rQWwBPviOR8rKUz5KkYy7byZySQs3argBdZV6YcyZXn9UqmYCNphdSsRkT4hqs-UNPepp7EHAYlt3DltS5VpP8PL5TKvj64RqfeoeLOnokXkS3rc0V-1-nAv-C8v2agO3o6qWdjPxG9ApBPor0R6450i0rfqavwdAR2tGb7bwLBOToRy3HCJb2nZWHKx9l-r_Ei56SA6s26owxn4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffcc2cb6f.mp4?token=Dt5KDZIa3NBHX8xkyB3TnRilAqR1ZMju4gMi9Ylv6DEA533fKlxZYjxNOkhus7wZmwKo3IFPOrmhMvOwfWZJM70xau0JGVfl46mlUZ8Gxs_qmZw6KhI1F0_JzExaA-e5OX_7rQWwBPviOR8rKUz5KkYy7byZySQs3argBdZV6YcyZXn9UqmYCNphdSsRkT4hqs-UNPepp7EHAYlt3DltS5VpP8PL5TKvj64RqfeoeLOnokXkS3rc0V-1-nAv-C8v2agO3o6qWdjPxG9ApBPor0R6450i0rfqavwdAR2tGb7bwLBOToRy3HCJb2nZWHKx9l-r_Ei56SA6s26owxn4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز انتخاب رشتهٔ کنکور ۱۴۰۵ از امروز
🔹
فرصت انتخاب رشتهٔ داوطلبان آزمون سراسری و دانشجو-معلم از امروز آغاز می‌شود و متقاضیان تا پنجشنبه ۱۶ مهرماه فرصت دارند حداکثر ۱۵۰ کد رشتهٔ محل را در سامانهٔ جامع آزمون سراسری ثبت کنند.
🔸
هر داوطلب تنها یک‌بار می‌تواند…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466451" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466450">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cc6cdb21.mp4?token=DZmi_L-549DQDvN1ClCmOgQK3gvX4ut0d98HOOxhE15tmyZhD0w92AH1oehm93suBylBGsM5Rnu79Zb7Krp4XLvReu6h327DAuoaVYDqq5C5d0rTLYWYLt3RQm5PNgspbaRwz0ytZnAqMZ4oXsLsVi60QcyAZQo4IiTPQY5nzvW-bKs71ns-mcFfLbHWrSyelJBp2h17ixSinYL2ErHxUVjYd6-8E2ydfPj_gzXYIa5OHjKWe0tWdJAmxUJdhz3xhgSr8-7Axg-xb18NOAtcX-McrO8dPZ-7fM5Lc3rPzW_Ej_HMDmd6r4f7umjxl940ZsaHtYtwNeRFSdOuRIO0WoTXRf8ayI9_K8YGMBoWimkv0pZtS5PyYkLVnMK9gmd-a9wKjm1_MrEO9wo0TC9-R3MaT6cc-PjloVlzhf7_6L_CmkiOL4LknpDk9YlKZRTtGrRWOqgv7wcUu1iCqBvLB9SO36aTbqmq-CJZSHN9AZblCuyl79Xi0ZHoAP1daEdQha0EGD-HZO3AATbLHZY5hY4lLoer0C4vNlx9RIXyHyMHmrY1tG2Lbo9d_L5MaWB1IxeYIRX7GYzC_x-eUAmmp_RsJSwiaC1R9xO9z6yYEJ6c1J2zoAw992qPR4piIPaf2n9xbK5xgHuup06joQ_mFIzO7aOy2ODvMLMUn9hSHDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cc6cdb21.mp4?token=DZmi_L-549DQDvN1ClCmOgQK3gvX4ut0d98HOOxhE15tmyZhD0w92AH1oehm93suBylBGsM5Rnu79Zb7Krp4XLvReu6h327DAuoaVYDqq5C5d0rTLYWYLt3RQm5PNgspbaRwz0ytZnAqMZ4oXsLsVi60QcyAZQo4IiTPQY5nzvW-bKs71ns-mcFfLbHWrSyelJBp2h17ixSinYL2ErHxUVjYd6-8E2ydfPj_gzXYIa5OHjKWe0tWdJAmxUJdhz3xhgSr8-7Axg-xb18NOAtcX-McrO8dPZ-7fM5Lc3rPzW_Ej_HMDmd6r4f7umjxl940ZsaHtYtwNeRFSdOuRIO0WoTXRf8ayI9_K8YGMBoWimkv0pZtS5PyYkLVnMK9gmd-a9wKjm1_MrEO9wo0TC9-R3MaT6cc-PjloVlzhf7_6L_CmkiOL4LknpDk9YlKZRTtGrRWOqgv7wcUu1iCqBvLB9SO36aTbqmq-CJZSHN9AZblCuyl79Xi0ZHoAP1daEdQha0EGD-HZO3AATbLHZY5hY4lLoer0C4vNlx9RIXyHyMHmrY1tG2Lbo9d_L5MaWB1IxeYIRX7GYzC_x-eUAmmp_RsJSwiaC1R9xO9z6yYEJ6c1J2zoAw992qPR4piIPaf2n9xbK5xgHuup06joQ_mFIzO7aOy2ODvMLMUn9hSHDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک حضور
🔹
با آغاز تهاجم سراسری عراق به ایران در سال ۵۹، رهبر شهید که آن روزها نمایندۀ امام در شورای‌عالی دفاع بودند، راهی جبهه‌ها شدند.
🔹
حضوری که از جبهه‌های جنوب آغاز شد و به غرب کشور رسید و تا دوران ریاست‌جمهوری و اوایل دوران رهبری ایشان، در پیوند با مسائل دفاعی کشور تداوم یافت.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466450" target="_blank">📅 15:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466449">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84aebc9db1.mp4?token=PHiwmbhd-bzAPO-ma0GTudMyEisdjcS-qvrmZ-K2dR16rA9Uvf9OJi32XS_vWiF3-HGxQ0-pVWi6Fpp-uarxKdHrWOIKwbXE0_CjUUlGUJh5YzJS7-ZPtzavgxWXTqmR7kBAdYdXBDbhmsnZQk2OJNv9jalNcMVlcwWkvop8qChgIe_8h5ycnbNNa7bXCp4muuIjSzCBxKnd4LNkxvFcMzXZfSQoUriyxip2bScqBUt2tZ-qZOT-CZyDztTFtBSxxQ3pobSVtu7gRVo5mDpodpz_M-cTYufYvOv9xwxr7DwO8wmc5Q2YMvapwvDiPHTEd0IVvd6ni7OTk6m7uAxbTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84aebc9db1.mp4?token=PHiwmbhd-bzAPO-ma0GTudMyEisdjcS-qvrmZ-K2dR16rA9Uvf9OJi32XS_vWiF3-HGxQ0-pVWi6Fpp-uarxKdHrWOIKwbXE0_CjUUlGUJh5YzJS7-ZPtzavgxWXTqmR7kBAdYdXBDbhmsnZQk2OJNv9jalNcMVlcwWkvop8qChgIe_8h5ycnbNNa7bXCp4muuIjSzCBxKnd4LNkxvFcMzXZfSQoUriyxip2bScqBUt2tZ-qZOT-CZyDztTFtBSxxQ3pobSVtu7gRVo5mDpodpz_M-cTYufYvOv9xwxr7DwO8wmc5Q2YMvapwvDiPHTEd0IVvd6ni7OTk6m7uAxbTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمع‌آوری ۱۵ میلیون فوت مکعب گاز همراه نفت
🔹
متخصصان ایرانی موفق شدند با راه‌اندازی ایستگاه تقویت فشار گاز بینک و نصب تجهیزات فشرده‌سازی، امکان جمع‌آوری گازهای همراه نفت و کاهش گازسوزی را فراهم کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/466449" target="_blank">📅 15:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648bfa8f07.mp4?token=U2-MRn_8NRQKlUIUpMfYWD4EteM3jG759MovW6pfgnNlGwlhJuU-yL4_Px0abbev-A6y-scsr7eenfpSBYZbMQbTgLEWBiZPXUJ95fLXFjseug2r-IMc7Hz-HJ87LYKSp0wDbHRRzCHFBvtoL7yJze5fLtQFEquAOZkcHAMNeCITlvkmc5AwSnlpIGvnQU0YWGCQU7VGoAx39fUlbauclJu4ydqWa6P2PU-g-Dq2EecoC1BApfN6ZrLBVpS1eFiaargZVdKgD9Ofc0sgI1ucilog8TJMKhPX472Ta9WefBx6LWSIhWJviTthUhZUbvNdAetS8FMW1rBEfo54ROq7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648bfa8f07.mp4?token=U2-MRn_8NRQKlUIUpMfYWD4EteM3jG759MovW6pfgnNlGwlhJuU-yL4_Px0abbev-A6y-scsr7eenfpSBYZbMQbTgLEWBiZPXUJ95fLXFjseug2r-IMc7Hz-HJ87LYKSp0wDbHRRzCHFBvtoL7yJze5fLtQFEquAOZkcHAMNeCITlvkmc5AwSnlpIGvnQU0YWGCQU7VGoAx39fUlbauclJu4ydqWa6P2PU-g-Dq2EecoC1BApfN6ZrLBVpS1eFiaargZVdKgD9Ofc0sgI1ucilog8TJMKhPX472Ta9WefBx6LWSIhWJviTthUhZUbvNdAetS8FMW1rBEfo54ROq7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با این کار، حمله دشمن به زیرساخت هوش مصنوعی کم‌اثر می‌شد
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/466448" target="_blank">📅 15:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbpVlYoQybMHHypCSqwI0zN2df0FbN9iREV-p14ipd-PEqVDSyOFCaJel6uHoghg4MrJItnJIoTebhO-2GuN6GR_48y_mFl_cc0TeAIYhgNK5UYHASlVpf-An5wARzkspQRxP0EXCnSWOL3_ZQRk7vDQH_3wzMu5xQgiRwf-pi0YxDyqXrEotvvJOZMc5BUw-bCg9rtoNP2Oq3ux7KqCJykm1xIXGWRjf9b5EdO-VYBUCHU6ikbxivx02V_ul0ahD8QCaTTPMlqzwIWDaQ-rxIg23xM5FX_ibu2Gdv7VQuCYJEG9-XJAXMQOJIYKKDHJgCCxhX_VxNuvORqu3eJZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: دولت پشتیبانی از نیروهای نظامی و انتظامی را افتخار می‌داند
🔹
امنیت از بنیادی‌ترین نیازهای جامعه و زیرساخت زندگی آرام، عدالت، رفاه و پیشرفت کشور است و بخش مهمی از آن حاصل تلاش نیروهای انتظامی است.
🔹
در جنگ‌های ۱۲ روزه و  ۴۰ روزه، نیروهای انتظامی با مسئولیت‌پذیری و فداکاری برای حفظ نظم و امنیت مردم تلاش کردند.
🔹
شهادت بیش از ۵۰۰ نفر از کارکنان نیروی انتظامی در این دو جنگ، گواه عمق فداکاری آنان و نماد ایستادگی و دفاع از امنیت کشور است.
🔹
تقویت تجهیزات و فناوری‌های نوین، ارتقای توان حرفه‌ای و معیشتی کارکنان، حمایت از خانواده‌های آنان و فراهم‌کردن الزامات لازم برای انجام ایمن و مؤثر مأموریت‌ها، از ضرورت‌های این مسیر است.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/466447" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8e7475a0.mp4?token=UtM-iRBjT3iqDWBPhJeq6zJrUpMhb_hwgT08u2zWA1zxl12McNd0VMm5tRhfvohNi9mi94Zpn02H4GnzYm-u_s-9FHmLmyZJzmeSChI0zfNvuA4uzwByzUfYgS4AAZBQ_nbZtj0L74gOSQ0KFhOrZCQ5QbR6_a2FeTEfiq8tmDtDaennErxD0cOPQ66TSrI8V03sQ3QHs-Q7is2zsxrf6z7FzKAgX3YyGHnm96g7fen_6sOIap5ZHn-dw1O3OYWt9FpHTr3depi3T4ep84EM6XI3kiXKvRQ8A8cbTtLrl2i_rwGRm4lYs6MJPfjIHbS96xR_D-uEytLNKMIDT82QNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8e7475a0.mp4?token=UtM-iRBjT3iqDWBPhJeq6zJrUpMhb_hwgT08u2zWA1zxl12McNd0VMm5tRhfvohNi9mi94Zpn02H4GnzYm-u_s-9FHmLmyZJzmeSChI0zfNvuA4uzwByzUfYgS4AAZBQ_nbZtj0L74gOSQ0KFhOrZCQ5QbR6_a2FeTEfiq8tmDtDaennErxD0cOPQ66TSrI8V03sQ3QHs-Q7is2zsxrf6z7FzKAgX3YyGHnm96g7fen_6sOIap5ZHn-dw1O3OYWt9FpHTr3depi3T4ep84EM6XI3kiXKvRQ8A8cbTtLrl2i_rwGRm4lYs6MJPfjIHbS96xR_D-uEytLNKMIDT82QNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدارس فرانسه به دلایل امنیتی تعطیل شد  به دنبال اعتراضات دانش‌آموزان دبیرستانی در فرانسه شمار زیادی از مدارس این کشور که در کانون بحران قرار دارند تعطیل شدند.  @FarsNewsInt-Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/466446" target="_blank">📅 15:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انتخاب اعضای هیئت‌رئیسۀ جبهۀ اصلاحات برای سال دوم دورۀ سوم
🔹
در جلسۀ امروز مجمع عمومی جبهۀ اصلاحات ایران، ۵ عضو هیئت‌رئیسه برای دومین سال از دورۀ سوم فعالیت آن انتخاب شدند.
🔹
آذر منصوری، محسن آرمین، سیدحسن رسولی، بدرالسادات مفیدی و جواد امام به‌ترتیب به‌عنوان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466445" target="_blank">📅 15:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aovfDYChlzkjnDSvhRV3kJHVgNkkAz8jyGOEbxgudnZTxRskFTyCi98edtbEV7Y5HgVp6EYFDxz_5l8MYJlF-Rf3P92uDFxeyKturCyqPa22q_FVnXt_LxFg8zOWPaFCceOJyE9NV3psW6I_gWGlIguq9Lfr01KOtPPORkGY0TumeMbjStQdVmw8PhdnDJEhGbHi-4llhTmabt_2zp5E8wqInDGOScg_tBVH7ndvcDGmI4uHhd0jB5wWX7fEUlBYF358muTBusQU-eWcdnysr-tojOXSk6muHIBZZYXydXhHhreds6Hv7j9tpLVWliq_-rW7zoElQL20ZkcUHC3TIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkQs_nmA_Zi58NuTfgeDTIIQc8UOSv7LmhXLqeXQ6LaIaDwIxRpGkxTdAY5xriQlXVHTRbI_D9EmlvGWxfPqjLfVgxxraVhHY82ffrOMimPL8vmOvflpkO0ghOXcpH2XsrREo1FcezayafLyZDZpgC4yBfhuwJBLionkGb-nYxllGqRqogrU0Dc_6SfB9eaeNWx0s9_We0zsZK0IJl9oppuiqrSucr0Nm9xzKW4BESdUrUbPg60VUa1qFJrZmASFkFLZWSAB9hss84HBldmkgF8ZOFYNkJCvbPe239ZUGiKkxV7EugU55U5btvgyQmS5tcMR-1SazyvipjeNuTqEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTdJiVVQtVU_7FxfMNytXont7XyWmBdPxtV3HjdsXLi6mQY1zh3fPd1KNL9nGI_J_MNC2Mg3wrvD2TvXS5qiYt87tGaoezMsL74LXGJfAkkNSahTnRAtEjnbElDdEdI9Q9fER9n6_mKtzySU1L8rAsTKng-AS4NuwJMYKsTQlPKjmZ9nZLtq6T_cMBeI1WUeFh4FgGtubY38-_QqiZoGDByhszgLIKm9DLTKmGxl5qfOCjgHpYjL2OD_sQyt_0YKucCWcwtMeejChi2LX1T5175p_XkU1GiZoHLJmDP--TokjKDu2J552vLMhHxe9L57NNg6OhbPW_scD7QQOQly6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rvn2fwfK7cSmwg4Sc8QC906YKm1KPer6ou82Dk9uTXLvWIcsWVMo2o34TV2iR8Tkm9uP7jTubqRi_GrdDmkRQpo0Ub6FpeNyKfqbBRPiNAPjqoRvlaF1EUvVeL2Mmqt9GWjiSROlPtGyPUsCNxJkhpMJmjug4ZdWSVpVnTPkDhkckar8XeIfUqO9jJ3pdWmXemDcqep6jbcMKm-NvdhbXiwJDHUjKxUD90yuOmiXrOlN0fmaoVQWXV1B246toKEleoNpXumiRpO3r6kFHiuAA9AAuq9jc_7DBMKQTv1AD0NawdDVjsER4DTPjlUGuSNdufTnanWTXmA7vRqE3dMFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz-ReBU2GWKRM2ySJ9sa2nMcbkcyBZqPQ59XYfBrmPe4nxZYqRLPNvpu3bSYZsVhDyhL85TlpxPbbvXP2ZZrXdDYQbEyhNOEw0oJXn4Dao8LKoe_STPR7U-c1bTY47ZZUQ_PCjNP8mxYOEe2gE06Bc36ENkmMb4t6ubCbvwlDwBsald27ZjtuKBRQJ6KhEmOxl8Frv50mSgz3oLBgqcta3VpK_3KOyZNSTnVcqmfKCx_9bXDNix_v-s4vpxN7TaXhye4DfWzhQHPsX_YuOBludkayM__S1jppDzTnxGmXMLPegHzTGu8_CxV3BEgaJgOccsaMXtaeQ9t2mpGIRawjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BX6K7IL0SXEC7WcQJqfWrrVa6RB9Xq6tnl-wmgcrRAjS3S1n5nOUHRwDnoe79mFQ4jYJ89GqjJ-Y5G3WoFNSoldmDoXuUg54pVKAgn5RXnXQnL27PfJUnlTCfRVQYT0RdBwfVjFViLc9YWrpNChojW8OozwnzGyKE_Kt9OHrgG1GLvrH-2xbRckR9NvBME-PobeynSUrfDqNBBEPEvpfvs1nJVbN0tTenErtRNZch2jknCETDZkVLIJ-YN2sPC0Wm0ZL1uBvO02ty_WARaQesuV37plO6yftzqBLJlBbXkkftsvA_w6jg0FRZV0oxAwTPq581Yl2nxQ0kvCZ7TsUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gq1TjEPUFf6KGazOLlyyWu59MfifjiSbpOyOCyAbjmMTdOlBW5rQFMI8sc_LCujT84Y4C-d9ZpKJ5Mo5-Tnh8PyDzxz2e7_tiEtAkRZ_CjteYj5AjlDyTubqdv47Eot4a0bK2RLAGF6APTqa0zekcZHuXeTbDCzXWQdaTq6cJ5V2ae1crI5oXOpsfFx-sanFlZ65-FBuXP8lMl2TcbyobGJ9ncNVpd4n-bpJMjhaPndcfMX1cT_YfnNGrOp2JLz3qTnOcpwliNW3_zjcOt8qD95J6cwF9sX3VQhlH2SiQ9BiBlUeMfFn5xCaCm9-scNOQN8gVv_K_lTsoE2QBEay6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت برنج از شالیزارهای لرستان
🔹
فصل برداشت برنج در لرستان بسته به نوع بذر، شرایط آب‌وهوایی و منطقه جغرافیایی، معمولاً از اوایل شهریور آغاز شده و تا اوایل مهر ادامه دارد.
عکس:
نگار ده‌دهی
@LorestanFars</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/466436" target="_blank">📅 15:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466437">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d174ccaa.mp4?token=BYZv_EsLw3CqmpzsdaQ3HjPxtGGHd62aoaY4cKbDXCRuB7x7pV07GhVMeFcQ1QhKz46uRoEe4MoDnpk7Bl1X1HrBQ2sCkSRcAAY7iCL74QctiyaY4wNSHrQYuQgY3Ebhr8e-ZYs2nMudt_bH-tHpRoGoymdQjII1MhDZ4T2WLQJE3kDFz7wy-Nd0DLNKOYPhUr2PKtwz2JDTBR2AKCubos_7QHCGRmGCLULgVPTrLnXxyXLDV-BMYGfuuxzZWDR8qUq_s01xLZNa0wZm-QfQ5it0lSAw43CqtXNl96M8aGA8C3-Mo8LixTgq5Cpzf52f19F0pkMN8FYX9cE5O1UBPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d174ccaa.mp4?token=BYZv_EsLw3CqmpzsdaQ3HjPxtGGHd62aoaY4cKbDXCRuB7x7pV07GhVMeFcQ1QhKz46uRoEe4MoDnpk7Bl1X1HrBQ2sCkSRcAAY7iCL74QctiyaY4wNSHrQYuQgY3Ebhr8e-ZYs2nMudt_bH-tHpRoGoymdQjII1MhDZ4T2WLQJE3kDFz7wy-Nd0DLNKOYPhUr2PKtwz2JDTBR2AKCubos_7QHCGRmGCLULgVPTrLnXxyXLDV-BMYGfuuxzZWDR8qUq_s01xLZNa0wZm-QfQ5it0lSAw43CqtXNl96M8aGA8C3-Mo8LixTgq5Cpzf52f19F0pkMN8FYX9cE5O1UBPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تقدیر از برگزیدگان نیروهای برتر فراجا
🔹
افرادی که خدمت به مردم را در هر شرایطی وظیفه خود می‌دانند و در دو جنگ تحمیلی گذشته، این موضوع را به اثبات رسانده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/466437" target="_blank">📅 15:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd905fdb4.mp4?token=bMGEYLNCGTsytDG7_Rklo3JCyhD8sCv1yaEM7sr029WPay2sgAUq8DKOZCq6QyBfZvYghABhD9t70T8f0U03t40DjqXY_qt1z1S0Yr9Rmelg4VL_aWwlU-5IM8hw-1488Qkg6fu5pvltWu7JwABcmmZrKWiYXo2puxXW57Hh3bzrqGWa7ksCOwKTFo_TMchco-2C35JO1M-HRecXg7YQehRH_oyuI9HRT_2PqkbD8ecQ5j492nVeO-c_xRotaxpr0kYrFjtBTr4BRLSYYzB1Z5PYv16UezCdMVYDRgnMDFFFLmxgneFitAM44zQI0FTT-D3idhaehDEO-ax2rEy7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd905fdb4.mp4?token=bMGEYLNCGTsytDG7_Rklo3JCyhD8sCv1yaEM7sr029WPay2sgAUq8DKOZCq6QyBfZvYghABhD9t70T8f0U03t40DjqXY_qt1z1S0Yr9Rmelg4VL_aWwlU-5IM8hw-1488Qkg6fu5pvltWu7JwABcmmZrKWiYXo2puxXW57Hh3bzrqGWa7ksCOwKTFo_TMchco-2C35JO1M-HRecXg7YQehRH_oyuI9HRT_2PqkbD8ecQ5j492nVeO-c_xRotaxpr0kYrFjtBTr4BRLSYYzB1Z5PYv16UezCdMVYDRgnMDFFFLmxgneFitAM44zQI0FTT-D3idhaehDEO-ax2rEy7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدور گواهینامه در کمتر از یک روز
🔹
رئیس پلیس راهور: با اجرای هوشمندسازی، از این پس تایید و استعلام درخواست گواهینامه به‌صورت برخط انجام و در کمتر از یک روز، عملیاتِ صدور انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/466435" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d70ec41ef8.mp4?token=YQoo5pqL3Hpo3pFSavmKLn8zAd3-DuUJBCHEvGa7BBOMZ2NKbI6fUIWIK_tVZrIoXodWqW3s__uu5tRSgXTceTHz9fL1Gbq0-ZuYDz1slp_QyIV7S7_bT8S-T3PXo4HBqTSoDcRRU7cTLSzbRcZbgtZksSNQgJafpsauiJmUvHPGIuspJ4X6Xs3IQKMzfEGYgLwIRm7HKm4RdL9ULVU5EF8KxX30zjQw-KL3KJzI88u65hbRx4wpt-bTBQyyqwHYWU279eDhGmwAORJsZTo050s5mJ7JWDuY_e1yKsB8d2S7yyhB15_2bw7VH6ET21Nn7HMhPz-N6TTQpRZvDvQ1RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d70ec41ef8.mp4?token=YQoo5pqL3Hpo3pFSavmKLn8zAd3-DuUJBCHEvGa7BBOMZ2NKbI6fUIWIK_tVZrIoXodWqW3s__uu5tRSgXTceTHz9fL1Gbq0-ZuYDz1slp_QyIV7S7_bT8S-T3PXo4HBqTSoDcRRU7cTLSzbRcZbgtZksSNQgJafpsauiJmUvHPGIuspJ4X6Xs3IQKMzfEGYgLwIRm7HKm4RdL9ULVU5EF8KxX30zjQw-KL3KJzI88u65hbRx4wpt-bTBQyyqwHYWU279eDhGmwAORJsZTo050s5mJ7JWDuY_e1yKsB8d2S7yyhB15_2bw7VH6ET21Nn7HMhPz-N6TTQpRZvDvQ1RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرلشکر حاتمی: در صورت اشتباه مجدد دشمن، پاسخ کوبنده می‌دهیم
🔹
فرمانده کل ارتش: در جنگ آسیب هست، اما آنچه اهمیت دارد، نتیجۀ جنگ است که به‌جای تسلیم، موجب، عزت و سربلندی کشور شد.
🔹
جنگ هنوز پایان نیافته. دشمن پس از ناکامی در میدان نظامی، به روش‌های دیگری روی…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/466434" target="_blank">📅 14:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c42e0d6b.mp4?token=YvbmuaS6JlEwZN5FgtEEfNt6BA3xlyKoMg2Jqyq7Eu_BpF5adV38IOuLNIeOMjYxidSDVSPsKvyT1eB_ehxgxfSpC4uHjXmd9zcgJ2SushlcqaTTbe4hz8qK41tF5RhwdO-Pfth9x8VkmBpb_VMcFpslySisWwumWrm_mZdCU1KMIl6Uh_S6pbPNOd8HK33w1iXLnvHQ9xbRzxrgVUDw5NSXnuR678puoEO1JUj2QEjEyty06IshMYEeqSsPCvhxn5nro-wgrXm5TrKWJx9i6TdJv0osDv9OQnKAsUJar4a_I1L2-u-8nAMjl3XqFuyHLYut-wlqVZEijXRnW8IDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c42e0d6b.mp4?token=YvbmuaS6JlEwZN5FgtEEfNt6BA3xlyKoMg2Jqyq7Eu_BpF5adV38IOuLNIeOMjYxidSDVSPsKvyT1eB_ehxgxfSpC4uHjXmd9zcgJ2SushlcqaTTbe4hz8qK41tF5RhwdO-Pfth9x8VkmBpb_VMcFpslySisWwumWrm_mZdCU1KMIl6Uh_S6pbPNOd8HK33w1iXLnvHQ9xbRzxrgVUDw5NSXnuR678puoEO1JUj2QEjEyty06IshMYEeqSsPCvhxn5nro-wgrXm5TrKWJx9i6TdJv0osDv9OQnKAsUJar4a_I1L2-u-8nAMjl3XqFuyHLYut-wlqVZEijXRnW8IDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احیای مجتمع فولاد مبارکه با دانش بومی
🔹
دانش‌بنیان‌ها موفق شدند تجهیزات و کوره‌های آسیب‌دیدۀ فولاد مبارکۀ اصفهان در جنگ تحمیلی سوم را با ظرفیت و توان داخلی، بازسازی کنند.
🔹
با این ابتکار، بخشی از کوره‌ها به مدار تولید برگشتند.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/466433" target="_blank">📅 14:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUZloGQooRA9PWKOuzCuEJMS9jInutNo7vMcRa0o4LWODYsLkAYsmftHuavpRFkINxInrlaZN_b-9rS0b522PMiT8rjaIXzr6qIS863oH1OprMBsZHyh9P2KTO8oUZwGSAR0IrcmYbEqqNuezoNLmVolqMS33XPiSxwhR9rSjlMqYyViuAY3smzCajIcyrilzsnYa6bLJmfd6BNJaX7Tr_b1MHONBdjQLKeVOPpuCoKvFxzaGSBi9MFF5jXMT9N3394CEXYnC4xLjfcdSSw9QMwr-Wf12z6M2kApNr4G0qy_7-Tgkg9qiSn0pfF9sI1ZsQWw7dDPdZLY8t5d6SC5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QseGOe2xGbagOMTcofJMckHAgVq1FeF9bIXn9JP6u9N1k0DqfbtSC4vVAmWcIowD3HkBVLeAA0BjRMght0I0n7gzhu40iQkAmNFc6FfMv-f6V0TjpwUzkzAcfFOpzc-IFJIBA-i8YuysvQWgdSpDWKaLV96n0FosDNwIdS_xlIkMfnFgndrESd9KH9PfW0QpQejqTV6EnHGmJ-d7ayt7bFbjpXepHWSOu_g_-QWFTi_3XXWZOVfPCUCz5oQiej3USG5LhvXtc5eIPD2Vhw8142Qi1L7FsNsES5l8AROphWqN28lniOSOgLq5SpWoGcUAuwKifzMPZRh2F8TnUAPvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STmudERkj5H9eWUkNFmf2bV7AkvjsE5ggrgsoQW7_6Qj-Z0nJF_J07aklLZuZUBWCV4iSC67apC-ggUtDnruT53b9ScKOhzTHYHsE9qHMJGTdP_Z6t1UfkLj8DiCmFT-BVnNGY-Z5YzBBSEATmovOhhzwdtKWHCs2fVjwlOZX6lSSHNfFEOEJGKPbjWUvOf19ytSRlIle-NOxMz7YNee_AV-zkM_VrQijtv6lXx-rL0y8zgJXRqY07t1oeQi0TXVp7Zq6owrjnqDCRxmNTupekAPkRybbsLZj2lRK3lsDklaDsA_DoKy62SSF4bkvtxrW5D2q9hNlF0WQvKoOVuCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7wYw7UcRLTtu26VMNdb9mxPGGB3G3Hl_y-Yubp3G9XuxDAYMspgJcF9hsKv0ZdMRvgWyuV46zPBF9Atv17c8TBTfjVFXLrKoCfnsHJzds1bl-hjIRAVAlqVy2K6hpRWP5rKKNmUzsnkI2AjATP4yC6EWwS8hvEEbG81d7pEzR_XwJNlHeqs8jPDZiIGBGAwSDthF1x2ux0t1wKV52TdQYvyH5Jit6-PbbVX_qIVNWWfMATPUoCjZc-aqBGri5FHK-fVwovsOyvABidT_balQ-1XA-mOCgnjnG-qgCtgga9LmGiJBNpZC3Qu5na8biefjLZJoMPQ3loztL51PACg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6kxAIqJ5JU1yqMiPf3xJOOxPZvuHau3Z2bpeRBHPyaTPBes39mAX7kPhmxM83FsWWkqOaNOzFf_pAxDKoogylQf36ermuursHd2aXsPSYCaaLQiZ_q3rRkeae67dTKi8VznOwqjvqYrRGfsJCpcfy0Xm23vaDO-cDnTtxbgPPXNLOvTdodkeV_v3fiTxnZpNYE88LzFW4rAMSpghT9xeHw-rlx28YuZdp6egwLpfLBZ89E1e_RVvz-bJjGz1Qcm_H36iBQ9qpFdm2DTGFnJwyiUvRGmrNq1mbOOZc_0FKcq9yTIurP_hG8t41CRU0ES_fOpSR9P_qx2J3WkTeoSKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3ai9weabtgC5XcywgbGBqDQIMuIWc4SmqEZoYxJPtf1on9Z573Z6S7Bi7F5OYSnSWFvhwMI4SyoCV5YF24OAdi3Cmn2TrNV-d2DCy8sOP8sESHiSbel1Wjbt5pqI5J6kver7mxYjKAhvO9to396citBmpfipDm2CgFT78yVUbvOr-KpxvcroFHW7M1ubtR26T0TLcbgYvAnpPttPlbyBKso4fZeqrVUiGR7FXEmFO4SvK9nNOsMQQ3ekV3-TuOpGHVhZKJmCnrilgJ--2kPjYMaxWCnHc1FwmixmnlS2mFTD4xObechTE1hjNHVuN41-hGFYeuYxJIG3NyMoCQpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfgQ9pXkaAw378u5IMq63qSnSJhiE1Cbzl5cuc5t4OaMSnb-b3Z8_MKG8H-t3UBXJkJp1QxFigjnXXmUtVhu3blGJgzu_2CkLJNEiHqy6F4kHHeDfAs5upwTMAbQu76zwbUqd7C09v6ljmlL9l4E0FhEZwtDFhuqMilWjwUCdCnS3S_XnnpoB-B8MfzFKT7UN76alqHSxlR-T7EyImZlAupqkawg0CkJYaRSOUfReUTHxCOThDcexAxb3gF4CTahHLB5vN-hE3Bl6Q0WBtueaxU63jiZYSvr-Yn37cvSD9ktHnHhYCR9k6wkITzdoS02v78himhqnnhMzCl0TaKu6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور وزیر ارتباطات در خبرگزاری فارس
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/466426" target="_blank">📅 14:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌  علیرضا سپاهی در روز حادثه بنزین روی مأمور ریخت و او را درحالی که زنده بود سوزاند
🔹
با توجه به اظهارات متهمان دستگیرشده، تصاویر مشرف به محل و اظهارات مطلعین، جنایتکاران در طول مدت این سه ساعت مشغول هتک حرمت و رقص و پایکوبی بر بالای پیکر مطهر شهدا بوده‌اند.…</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/466425" target="_blank">📅 14:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۲ نفر از عوامل اصلی جنایت منجر به شهادت مظلومانه ۴ مأمور پلیس در اصفهان اعدام شدند
🔹
علیرضا سپاهی و علیرضا رئیسی ۲ تن از عناصر جنایت اصفهان که اقدامات فجیع و وحشیانه آن‌ها منجر به شهادت مظلومانه ۴ نیروی فراجا شد، پس از رسیدگی به پرونده و تأیید حکم در دیوان…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/466424" target="_blank">📅 14:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcCIIF_eBBYrm9RhNsy3FPFM9Zt2OHLr66UVxIjblOvKlEiN0H5_8EFYYZsDAT5WX65wDL_FHoEynqDZbsjdNkgNgg_vp4iUl0BzwT8NRIdt9MFUA2px7tFkV1ztUFEP9rGZOlbVzHauNJWkXvAeFhI8ZUsM40narp-8KRI3_YxSXaCdobqAgIpcnJldpaMA8PIAD2Fpx0lxfhaTnnxYv0K9h1TR1k09SDMRE0iwHZnPiDjOljvY-5KvAQ72qmxTYExqYCXYQdU-OSsIYMMpSM3LbTxnPd6BIikAJd5XcrWfy3eF3X_2nJsFc8IwU002ZOkDCM7YjtCX3_YU7R8W3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ نفر از عوامل اصلی جنایت منجر به شهادت مظلومانه ۴ مأمور پلیس در اصفهان اعدام شدند
🔹
علیرضا سپاهی و علیرضا رئیسی ۲ تن از عناصر جنایت اصفهان که اقدامات فجیع و وحشیانه آن‌ها منجر به شهادت مظلومانه ۴ نیروی فراجا شد، پس از رسیدگی به پرونده و تأیید حکم در دیوان عالی کشور به دار مجازات آویخته شدند.
🔹
در جریان کودتای ۱۸ دی ۱۴۰۴ در اصفهان، چهار نفر از مأموران نیروی انتظامی و حافظان امنیت به طرز فجیعانه‌ای به شهادت رسیدند.
🔹
مطابق مستندات و محتویات پرونده، در جریان این حوادث، گروهی از آشوب‌گران با در اختیار داشتن سلاح گرم و انواع سلاح‌های سرد از جمله قمه، چاقو، تبر و قداره و همچنین مواد آتش‌زا و کوکتل مولوتوف، ضمن تخریب گسترده اموال عمومی و خصوصی، به مردم و نیروهای حافظ امنیت حمله کرده و با آتش زدن ساختمان‌ها، کلانتری و اماکن عمومی، فضای منطقه را به صحنه‌ای از رعب و ناامنی تبدیل کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/466423" target="_blank">📅 14:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMMPthLhpj-uwWuDZoy6PVEq5tBEB3Wq4WsN5ai9gmN9zZ2tqtZuxJ1v65aDtmiwB2PLO2liXfLBjvMrvkzmEb8jEmQ3tQiAVcUzP5a8Pv4MB-MWxcLBKmsMJ3zDbGJ_CU_swn1bplUJXRjUm4SRLwh81DiMDTJ9OhCCsT7PZhM3pyq8eZ-ng178HbnyW5rA8LWezS4y6hMUwsYMyN5gQKPNnlJ9xQsujP_hq9FMMoOhpvJwAYFv2Uin6kazykducHzfJLD186LPJC3dPt7oDy59OMdpjoDfXsBBWFe8bLmT0GlStMdhWx0mfGERywwmPdBPka3gGfwi40-_vWHsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش حادثۀ امنیتی نزدیک تنگه هرمز
🔹
سازمان عملیات تجارت دریایی بریتانیا از وقوع یک حادثه امنیتی در ۱۱ مایل دریایی شمال خصب عمان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/466422" target="_blank">📅 14:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOkrtYTGjeWLoHoJdb2u8r4afyGSI4RqtD-_IsS9ZMITDkhaYI9yrJ2BhdtKPa0doRaA9iJKiXEfcEVZ18hlgpg5jSAh8rKjoS5cYbpjFCKjNy-D-EHMHy3zycOK5F5IFNleTCPWVvT-jJvK6VBByWQndnsmn_iQr6HcRziaiLF6ngF3CSHL82Y7vRrVvLCBrovuGGIEmH1yguOyiDUzRCPv7P88FhZf2DDkCapPr0yNTVnuoafphoCrkk1-y9MNMY_5mBcyFPNovSCRyC2qwCBPnYvl_CO38Ku124rHitMMT4ASI5aKLXy3iGkgIMW9M5qWMYhONUn3U1406x3E7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCqX7bfnXl9JDa4YdapKzX0G-nxx3QO9dqZ4ol7LQDBspInhfKojQPyB033eFzLT_75dK2YZzwLQsIwAMAq3sEdGgbnPAlv9kRItxca2hxnmsfuIwNCsqVyjlT4cu-QTKuEoKx6zEfc_xBFKXmg3Z_ZKSyn8WSkNdjP6Xo_wj3dmHuxxNii2p5o5-oJE0SYkU5VJ5p9uplIK5vwGQ0zjXPn--aXKXTqOnx7PIi1qoKnmBYg-NYYBySlMyibGX77lPSjMdtfE_r4JboH0E4kRq0djW69-5Dp8SNwkRtJ6lBWAsgshnM9_MsyHBH0aXSGfCF_Tdxs3dITaGuPb6Zzf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFkD6MFuQaTJtzYuk0OhY2TtAkL0ASTooqEX2aQobGReaTg7cAZrEozAtk2kpVIz4AHItv1ohYzAkgCy8AEpMcj9WiQSOiQfsFBj7Q4n4L_cedofqzKUjkSnhVxQ77EGVYHyi8X5bADqSBqEdLjfm2N195W1d536qqkk0FjxnQDKL56VG7BWrD3e6d9ajGNGG-OBpBxlFYoTsWLEDMokD5VAft10KsQomCU58KDG4r9OZWkUYv6S8PozTZaLUzTqiTaJJUXcwhH82lIe_zHb_h1BJw4sss6JkBK18UwRmnuZzFW_tyEWG_76JNfskQGjGwZhCEr1ZbQdWqrKjPtRlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تنظیف ضریح مطهر امام رضا(ع)
🔹
عملیات تنظیف ضریح مطهر امام رضا (ع) جهت رفع غبار و جلای بیشتر توسط خادمان بارگاه منور رضوی انجام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/466419" target="_blank">📅 13:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E27SVXICk37-3Wd4mejVju7btsgdsXa3yGyvACrf9o_1e4qSPRKcz36ULx1iNsorhXLk0CuZiWDf7dYvXDR28U7ZaNQ8RTrUgHgi0Om_u_6toKUH_CgkTsGI1F97Bxb4TzdHdwBTgsybSEAdgsY_cmyV_AtUkhouIZ7SqqGNvBmPskmBDhjzuakjMeMe0cj_n679Kr7Imdtco6bYGwFdH7f1DScvZiXc_qb3jckFE7UNz0zihrP1zJeSMovtqzhggFuceetX86JbsU-XBgofgDve4U0Tyz-AJr6k4hwe9usUclNV9r4iBavJjoCh32wrs1RjRFIc8A2eMo3HW5vV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام برندگان نوبل پزشکی سال ۲۰۲۶
🔹
نوبل فیزیولوژی یا پزشکی ۲۰۲۶ به‌طور مشترک به پیتر هگمان استاد دانشگاه هومبولت برلین و گئورگ ناگل استاد دانشگاه وورتسبورگ و کارل دایسروت استاد دانشگاه استنفورد تعلق گرفت.
🔹
مجمع نوبل در مؤسسۀ کارولینسکا اعلام کرد این ۳ پژوهشگر به پاس کشف‌های بنیادین خود دربارۀ «کانال‌های یونی کنترل‌شونده با نور و اپتوژنتیک» شایستۀ دریافت این جایزه شناخته شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/466418" target="_blank">📅 13:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6ernjjWFqsacKxFgUlu0gRHwFAEJXCZjBiRO4f5Yiw62Hjf0EWpGdtCdnQs4R-_Z1cJNaCQgasZlvS4joq7Bi28jc48-TZw5im0sy3ueclwiblIwVP9dOr10oJSXjxVImRTpqyzF8_nPOp7m24LOnvohBdifdA5tXS4L46GfsrZ8PRUOIXomCv4cgNmjFSwk7E0dyiln1gUL19-bTvND2_gKrpi8rCftESJCFFXrxC1kA-U81Lnf06GB04IjCA7dG8nZF84KnJmZ1lLUUCL_3EIpjbuygFkDIK00GWqo7eokrqmE1YHeQGhumU_NVxVfo-_kYOPYyUEUnaTUDmFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: در صورت اشتباه مجدد دشمن، پاسخ کوبنده می‌دهیم
🔹
فرمانده کل ارتش: در جنگ آسیب هست، اما آنچه اهمیت دارد، نتیجۀ جنگ است که به‌جای تسلیم، موجب، عزت و سربلندی کشور شد.
🔹
جنگ هنوز پایان نیافته. دشمن پس از ناکامی در میدان نظامی، به روش‌های دیگری روی آورده و با تحریم و فشار اقتصادی در تلاش است تا مردم را تحت فشار قرار دهد و در کنار آن، اقدامات زیادی برای ایجاد ناامنی و آشوب را دنبال می‌کند.
🔹
نیروهای مسلح با حفظ آمادگی و هوشیاری، در صورت اشتباه مجدد دشمن به تهدیدات او پاسخ کوبنده خواهند داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/466417" target="_blank">📅 13:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769e70ae06.mp4?token=DP_KOWQ8GIPQJZ1KxewGPZQRlghxPIFJ2ovRN0LZHFkW1tdu2aAG5uzhgqesA6cuU1N7KL-meWhSmu1lC81FOrl05a7Ju6ThETzeWC0v_JpLzHqA-R8wUVadGmZaBVg7b3sHQYdAKvJO56-bk_eqVxAQHZaXV4P6La83oo60DG7TxaJriThyexNQUOdtLcK9G6yXS-APuQfOjQCaH2_ef7zIAc1GJrSt-DSq4R_vNormo7jgipu7wBFYSEJxo-ZTlbjSTwd1MXvaTpAS8tdgW6v_3izR7zjJ1k341uNUHJxpcJkkCocVA3hWmCI0A-0LvSA55S8inRWY0EAH_BQ3iqKViMVZlPRbcnwojv85r9CCmQbGL8xmM6cDlsBGUHQLSLJVXGM9hCfseY9bog13YShfDp1N49AxTHvaOUZdbo697puzzad38cldpmqpYc2op5g1TTr-10tPB3WGnpzVau6SuqxJe0iyNzQPFI3acHs6Yk4oyuf_akas-20tS4x07ALjfkEbScGx-Iq3VLIDXFmoi-y6MNcJ-e0qGwL-kqNRnkGEY5uWCrfDJys8k2VedBt4JqZgFwbKPUgVZy2oWlb0MqlfJbg3fQNg9HWg7EtyB4QTm3RrtS6kPumg0Tp8J3LDgBLH-c6ArqPqVcBexvV2KTfYHMqHlzTg5td2LYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769e70ae06.mp4?token=DP_KOWQ8GIPQJZ1KxewGPZQRlghxPIFJ2ovRN0LZHFkW1tdu2aAG5uzhgqesA6cuU1N7KL-meWhSmu1lC81FOrl05a7Ju6ThETzeWC0v_JpLzHqA-R8wUVadGmZaBVg7b3sHQYdAKvJO56-bk_eqVxAQHZaXV4P6La83oo60DG7TxaJriThyexNQUOdtLcK9G6yXS-APuQfOjQCaH2_ef7zIAc1GJrSt-DSq4R_vNormo7jgipu7wBFYSEJxo-ZTlbjSTwd1MXvaTpAS8tdgW6v_3izR7zjJ1k341uNUHJxpcJkkCocVA3hWmCI0A-0LvSA55S8inRWY0EAH_BQ3iqKViMVZlPRbcnwojv85r9CCmQbGL8xmM6cDlsBGUHQLSLJVXGM9hCfseY9bog13YShfDp1N49AxTHvaOUZdbo697puzzad38cldpmqpYc2op5g1TTr-10tPB3WGnpzVau6SuqxJe0iyNzQPFI3acHs6Yk4oyuf_akas-20tS4x07ALjfkEbScGx-Iq3VLIDXFmoi-y6MNcJ-e0qGwL-kqNRnkGEY5uWCrfDJys8k2VedBt4JqZgFwbKPUgVZy2oWlb0MqlfJbg3fQNg9HWg7EtyB4QTm3RrtS6kPumg0Tp8J3LDgBLH-c6ArqPqVcBexvV2KTfYHMqHlzTg5td2LYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس امنیت اقتصادی: با سایت‌هایی که قیمت دروغین و حبابی برای ارز اعلام کنند، برخورد قضایی و پلیسی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/466416" target="_blank">📅 13:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7eCxI-xcQnnEg14PjasxDmMtO8CLm8RYgjPZ_2gd4cYnQcg7CjG7mnp-w0IEWtqCTRdZ5gCgqWOVcyD2dVaDmYo05m0W8C8ScFMBbVpFccGmN3f9RfI72rb9KR_JPP1qK_EnIU8DN1apiHS35YFJJ49Raqp_j-R_o_uyDBUXlPbZeztkkt4FyHQbmBiFX6f0i0BvXzHtwmsi80I2CMfpfkmBYOJ8EqEX7RdEN9ycJX9-bhk0xB-GJjQrBrk6Mlyo5ntDPJP20WW2gIBUGIfWnM7oIrcNtrWcgGsROUwP0NgdsQF31sIxrQUMDWm-kbnoygoKbuwAdONAitnKibUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توفیق اجباری قلعه‌نویی در بصره
🔹
با انصراف تیم ملی فوتبال فیلیپین از حضور در تورنمنت بصره عراق، تیم ملی فلسطین جایگزین این تیم شد تا در کنار ایران، عراق و لبنان در این رقابت‌ها شرکت کند. این تورنمنت قرار است از ۱۸ تا ۲۶ آبان در بصره برگزار شود.
🔹
با تغییر برنامه مسابقات، شاگردان ایهاب ابوجزر به جای لبنان مقابل تیم ملی ایران قرار خواهند گرفت. در بازی دیگر نیز عراق به مصاف لبنان می‌رود و برنده این دو دیدار هم فینال تورنمنت را برگزار می‌کند.
🔹
حضور فلسطین به جای فیلیپین را می‌توان اتفاقی مهم برای تیم ملی ایران در مسیر آماده‌سازی برای جام ملت‌های آسیا ۲۰۲۷ عربستان سعودی دانست. چرا که فلسطین در مقایسه با لبنان حریف قدرتمندتری به نظر می‌رسد و می‌تواند محک جدی‌تری برای شاگردان امیر قلعه‌نویی باشد.
🔗
در
اینجا
با تیم ملی فلسطین بیشتر آشنا شوید
@Sportfars</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/466415" target="_blank">📅 13:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از حریق گسترده در خط لولۀ عربستان
🔹
تصاویر جدید از عربستان سعودی از آتش‌سوزی گسترده در نزدیکی ایستگاه پمپاژ شماره ۲ خط لوله راهبردی شرق-غرب در شرق ریاض حکایت دارد؛ آتش‌سوزی‌ای که دودش حدود ۵۰ کیلومتر امتداد داشته است.
🔹
این خط لوله در ماه…</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/466414" target="_blank">📅 13:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce185ecea5.mp4?token=QZgLHMPcKptzjeK4MM4OLjI_AxhuPO2g5U-KyALQyGt7dAbSAWGRscTSK-RXFGtc-byIliXj22PFWV8OlXBfsleeIvDL_uLgNPOoKchgD7Ts5wd2aPi7Fw2B-P5aF8RHUEL1K8572oCFNWlAxRHTkNlJE3S8KwqXahbD-UlnoRrdS0qKtUb2EP3si0xrmsW_mRxnUN8vZ8ZbJkHPLbSRbMUWGfDYs86EnKTP2MyYvsZzjwquKQ0HjPrZxbLxFWnyIcHhrc_OYkzLi9aJGgNBjSzqyX9FSUIPdC9TwFlweX9KsMnuvY3857seAzsioKMvViVeX_PZSa9Pefl9J0rfNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce185ecea5.mp4?token=QZgLHMPcKptzjeK4MM4OLjI_AxhuPO2g5U-KyALQyGt7dAbSAWGRscTSK-RXFGtc-byIliXj22PFWV8OlXBfsleeIvDL_uLgNPOoKchgD7Ts5wd2aPi7Fw2B-P5aF8RHUEL1K8572oCFNWlAxRHTkNlJE3S8KwqXahbD-UlnoRrdS0qKtUb2EP3si0xrmsW_mRxnUN8vZ8ZbJkHPLbSRbMUWGfDYs86EnKTP2MyYvsZzjwquKQ0HjPrZxbLxFWnyIcHhrc_OYkzLi9aJGgNBjSzqyX9FSUIPdC9TwFlweX9KsMnuvY3857seAzsioKMvViVeX_PZSa9Pefl9J0rfNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله یمن: تعز آزاد می‌شود و آرامکوی ریاض و خریص عربستان در آتش می‌سوزند
🔹
با بیرون‌راندن نیروهای وابسته به عربستان سعودی از منطقۀ التربة، مسیرهای منتهی به تعز قطع شده و مرکز استان تعز تحت محاصره نیروهای یمنی قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/466413" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466406">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKPDJ_fjrYG5yqS6CVjOGca7psD5djT6qBCbyWDrBepge_hCx9oDJJ7pxtwB3b5SQYYt8w0oXFzM8Sd42LPcOP9kWelaQsuDQpMzKKb0ehoTDsLrWskUt8ubyviuS1l0JikMSudNJ6yD7CoRishtklzk6MD0U3sx0pp29vPeRkVirc4Xplpc2YDXF1LmuFT28rsLrGYjqStP8vF5DwzmzjZ3ZTXglvN0MpAmMnn3C5q3rvziRGkm7Vr2lsrOiMgMVfZPpmRzbQdk8R316fuDKTo6P_zLg8PxvgINfPuqbEYxsfQoLzgReEWmmvBsK8wCvwniip2WFmmCCSNZsm7itQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiOjdZSyLPYUl_B8AS85vd5zGXpUARuTHFq9RyG9yE7_ZESe4PZigj7z7S7V0968wbtp5yR1vMYfsmv2TvrdiOZVKG1BOvnkvOisDHQlFw5IS3xQ_PEF-56MS6mkXm9mi4lwJaISV-oylMBjKk75u9drOpqWQW9bcMS1HCRBPo8pw5Q870XQhLGuc-VZFOqpmlsy7xNEMFxH6IP2V95JIztMl_NQlA8jxg7P6GmPtTD-OGinRrPNT8pKtI3UiBwOBB7wAChxMcFN4CJIlFPJFEJZ6aL0vajzsddXJdDc-pSVmcfFGbDvAznCaBfPN_qM3fcw5M0kRm44ys9qmNexSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/luvfyvyunh52oqCGzBu5zarSXZus8ZFqDuFwYFrzKYfSmlXg7iNoILtOTTr8ENEhay-z1Xr-NGwsb69owcCQUA2nWv3IFkonxdv2jTi14Zf8riz8zHqWk2ogWhNgwiP6uanf9JjYSZQc1MFMshNs3AbPWj1fonHUNXrSlRxVKlcIy8-LdeeS7iLpcvoPTro20ppImSBZ9bcILsGMjlkTBPhVcQsTRjxconcZxIQ20RLjWrit57jMBMpXubnq6jwDFP7ueAw-MHDcWFlOzJfI4QQQRXTjzLyPXNGqr95yM2U1bX0u-kVqXmunmTN4GWp9sEu1Ptnv-kUUUmDJk83FSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XqZ_rQJNw8EPkc7czfhUoWog9Rw3STRmBqaT1V75VTY9YrX615KgrvAK9nngYo2yMUghIP7lDq_CoC_b7mbnZpal_-XIAyTuL0A1g4ag3lIiYlLRUQI-RU1NOfdwcHzGVj7eygJ8voaWKqkMfFHjz23B6z9RxGaTO-K7w8pMCbRkKgYG8j_Tuz_e6uz9I6c7ut2FGapr1jaTRDphHlqswnZFeFY-RoeByhe2eAR2ZsBBUSVWVlDziomGCpcLGuc2ECI1gH0XL4Y5kKi8NekO0kzmSKDwh5nrS-aMkBhZfUc5Poa52Fl2KnPjvjZctT8wJDfDsaXEUIE-KvOjf23ozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWHXkSDTLO4KMmIAuC0iqLrWKKxYRys1Ipjh04FStiGlINEW3ADigY_1MkkC0eSG31x6baIwATREq9VxmTvayCOlrqf1Uy4jlYSqbXUW7a9i3qEOZfSSRe0hAGh1RKoYlVvF7dE-mVrinX2-KFIpu-XKvBK5OC6v7r612kL6U2jwhMKnTG5D0m0I3UunLHt4z1sjWNN-mljL-X5cMtcObHyrk4QVGLcLo-XYci9lTXjzJd9yyIPystr8OFvQQcB7juS_fINqnmuC6AZ0GFFr9S7duglDLMQk-1AUjZhW4R2XsbIx3KLO3YkT2LXsoY17qjmQ4u5M0Lrq1_NddvYa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQBafuHyfABeABCgBMta-Jp_nxWbFD18ULm680yb8PoENI9zo5LVBiIlX1f1RsUfKXIJObIO0NrGj4cGhXXo4cY8KhQcYKLO_GbCvEYC-YEXN-voaMg9Mr4-W3eAOZxxWMxdJ0P-bXEQmZvbkA7OSZ_v-ZmK7X_fC9GlM5F9F-UWSys2SbhpojivxcFj28vCprWge6GwYrCn-Ga6XylF1XT5tQa7OLRAqm3gZkz-xR5byUwK2uHzbIruVakdrWsPs9KrGIKcwjrQy_TKRcjdxp-DeMj7eBjlM2nv1M1osdQbmQdyYDnBplVPQQau8w47djDAo_f5FvVlxx1F2CVBaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QC1bECGfB5eixRdp87UcWc_guOgHkJI0MIfTvpxuUQsfYor-8mPk3IOmP-c938BQdu-ir8sAPkO558GBTynQEp-kPE4d-tvlZzaftT7aD5jbK42ihpwMfDRa7N403wRDuGMrobTJgv6oDW5slD7h4H_g6w_zKRnCuiePmhl1BiyesKUVfK2BoZmnGG-BmMxlrm6CIuHkLu3vuUaF1jHUDPb9kozpQmbLZbl4Bc05CNAIzBAqjtALKHBjFQDBy35TwxKvjtaHPoeS1Ct0SRp3jSzoh3Y_xapFNKn9itan3hfJxqGta1kS5QMrasMjYdouv7oJ69x4eQLW8ydYPIejHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار عراقچی با وزیر خارجۀ ارمنستان
عکس:
زینب حمزه‌لویی
@farsimages</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/466406" target="_blank">📅 12:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466405">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A66os9pAKA4mj2oIyqgrJtVD68Zqtl2df2auN0Inhj98lIB19JtyOYiwNfvN-5-2TXa9engXetBkIC2Y3DEUQ3e6z8SyaS6JIAgrf5nRAJf4pU7cKYqnV6qIDi9yM6pkKOBzw7r06aXzlw2HiNFU0nsIbMgnF6nBIh5IrOpbZnaghAPdeJzP78ni6DR3WFoM5h1bIvDZCbxJTspFbj_kClvOqM7YCj6h0-sJP4ULGfkBnW0qxnTf9cBIcxPpKUteZu0_S6IpsBqY0QxgyqyinhTZRNx1NBBMLQlh3HBWHbt6Uc6wsOEH9-U1yivSXjG_fM1ZjiCw6NnqP0F51w51qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور: همه دنبال پروژه‌ای هستند که در دوره خودشان افتتاح شود
حسین افشین معاون علمی رئیس‌جمهور در جمع نخبگان و سرآمدان فناوری در مشهد با انتقاد از نگاه کوتاه‌مدت در مدیریت گفت اگر هر مدیر فقط سراغ کاری برود که نتیجه‌اش در همان دوره مدیریتی خودش دیده شود، پروژه‌های بزرگ و ماندگار هیچ‌وقت شکل نمی‌گیرند.
به تعبیر او، «اگر هر مدیری فقط درختی را بکارد که خودش زیر سایه آن بنشیند، هیچ‌کس جنگل نمی‌سازد.»
بسیاری از زیرساخت‌های علمی، فناورانه و توسعه‌ای ممکن است سال‌ها بعد به نتیجه برسند؛ زمانی که مدیر آغازکننده دیگر در مسئولیت نیست. مسئله این است که مدیران فقط به دنبال درختی برای سایه‌ی خود نباشند؛ گاهی باید چیزی را آغاز کرد که ثمره‌اش به نسل و مدیر بعدی برسد
کشور با پروژه‌هایی ساخته می‌شود که شاید روبان افتتاحشان را کسان دیگری ببرند.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/466405" target="_blank">📅 12:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
🎙
گزارش "دی نما " از نشست مشترک مدیرعامل بیمه دی و نخبگان شاهد و ایثارگر
🇮🇷
این نشست  به مناسبت روز ملی نخبگان و با حضور مشاور اقتصادی رئیس جمهور ، قائم مقام بیمه مرکزی ، مشاور عالی رییس بنیاد شهید و ایثارگران و جمعی از نخبگان شاهد و ایثارگر به دعوت بیمه دی در سالن جلسات هتل هویزه  برگزار شد .
#"دی نما‌ "مجله تصویری شرکت بیمه دی
گزارشگر: حسین زاده
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/466404" target="_blank">📅 12:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/466403" target="_blank">📅 12:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1b081cda.mp4?token=Ar3CTj7Ata4im4rYsYFH-89IEHXxgJBJOGJu2PY4Tv2t2hr4ennSCl37XRbYSRd3VvVjVDaCdI993wEwWn_SQgml5ieETlWN_j3yYHg1NXvRTNySTZaeKXiKeAKv1GKWw0rwuN0amRoyg1LirV3jcnSO4lcB8ncVaAcsde3VkTPTSNSUgiiy79NxfPo33ftjnl_UX_ZfB0nChv_DEnxgX8xjQtTiIBABKVP_3faUME26G1OCVQh3_z7S3bwNoj_xr-LT9WvMYB0yBQWDWB_jye2Hu8j8J571sqPj-R7c-oeyKuc-1LaIfMyzIte4X-FiVwKFNX_sgNK1o4J-z4NplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1b081cda.mp4?token=Ar3CTj7Ata4im4rYsYFH-89IEHXxgJBJOGJu2PY4Tv2t2hr4ennSCl37XRbYSRd3VvVjVDaCdI993wEwWn_SQgml5ieETlWN_j3yYHg1NXvRTNySTZaeKXiKeAKv1GKWw0rwuN0amRoyg1LirV3jcnSO4lcB8ncVaAcsde3VkTPTSNSUgiiy79NxfPo33ftjnl_UX_ZfB0nChv_DEnxgX8xjQtTiIBABKVP_3faUME26G1OCVQh3_z7S3bwNoj_xr-LT9WvMYB0yBQWDWB_jye2Hu8j8J571sqPj-R7c-oeyKuc-1LaIfMyzIte4X-FiVwKFNX_sgNK1o4J-z4NplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مراقب باشیم دشمن از اختلافات سوء‌استفاده نکند
🔹
رئیس قوه‌قضائیه: دشمن به هیچ کدام از اهداف خود نرسیده، اما زخم خورده و کینه و عصبانیتش بیش‌از گذشته است.
🔹
دشمن به فشارهای اقتصادی و تحریم‌ها امید بسته تا پایداری مردم را کاهش دهد.
🔹
باید هوشیار و مراقب باشیم تا دشمن از اختلافات و دوقطبی‌ها سوءاستفاده نکند.
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/466401" target="_blank">📅 12:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE_skjxjoR2mjhrfwOTzQZV3pCud0FmuGtPkq_vlO3xk3pInRGvM11c9DALGvUBkLKKWbnRIqtphvOm40AR6wdMkp0zyHdr7ivhzYp0DIdNjCA5zpeLnORMJeqbywG_4rcslsxyudo-sSkWH6Lk3C2Q0Cul0fKAqsu7_I0Ee_Jj09RA70zw9_GWELYF3-NQGkFFjjtVZPiHqYlSpVX7D_Ur0q4d9QHpP35_9Ok_n_UqUcZqC_i2k3Xj4uJ5TKPbWJtzs4SHeLRfDzR4lYNMZKH-bqOadrsO0p_vLuqZMGLKn9tZu2vU-yGs06EdC6vOsfOY74u716AykclTxjCLCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور جدید پزشکیان درخصوص تورم صفر
🔸
شهرداری تهران از هفتۀ گذشته طرح «تورم صفر» را در پایتخت آغاز کرد. در قالب این طرح، قیمت ۱۲ قلم کالای اساسی تا عید تغییر نمی‌کند و این اقلام در ۱۰۸ میدان میوه و تره‌بار و ۱۸ فروشگاه شهروند عرضه می‌شوند.
🔹
حالا با دستور و…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/466400" target="_blank">📅 12:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
سرلشکر عبداللهی: قبل و بعد از انتخابات آمریکا علیه ایران اقدام شود باشدت پاسخ می‌دهیم
🔹
چه قبل و چه بعد از انتخابات و با هر نتیجه‌ای اگر خود و یا به تحریک رژیم کودک‌کش صهیونی، علیه ایران اسلامی اقدام نماید، نیروهای مسلح جمهوری اسلامی ایران بلافاصله، با…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/466399" target="_blank">📅 12:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
سرلشکر عبداللهی: ترامپ بداند، ایران منتظر نتایج انتخابات کنگرۀ آمریکا نبوده و نیست
🔹
رئیس ستادکل نیروهای مسلح: رئیس‌جمهور خودشیفتۀ آمریکا نیز بداند، ایران معتقد است سگ زرد برادر شغال است و منتظر نتایج انتخابات کنگره آمریکا نبوده و نیست.
🔹
بلکه این مردم…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/466398" target="_blank">📅 12:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سرلشکر عبداللهی: جنگ جدید دامن همه را می‌گیرد
🔹
هشدار رئیس ستادکل نیروهای مسلح به سازمان‌های بین‌المللی به‌ویژه آژانس انرژی اتمی: حضور رئیس باند تبهکار صهیونی در منطقه و اعلام این مطلب که برنامۀ هسته‌ای ایران وارد فاز نظامی شده است اولا از روی توهم است.
🔹
از…</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/466397" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qENSZxqVwkaKnIzcXOVlMggmd3gC90zH-SZ6JIFZB6q7aao5e-ztO5F5TIPKrrOxoBtcb0fWDZH4j_0s0os61nrKRZN_nZemGMQWSlvlYmzyzNDpceST-ETpx-jx0fzUQGt5wl_538GuUFlN6YOXuGX0DZEUnaJt3aNy9DS2Od5a01G6Bg1AeyI5zICkzS-mtnkydwKTXvD8Cmx3V6Y9lzGx0DAhlK52TEWZ2nC9nS77QcDrTRBCghJI2wHyEpAJvFtRWFoT6Br1hCAkYRztsbEyAqKvs7009iuv3RyixNr6V6A43IWJfwh4LHUmyk6bhq3g1lVJQkL4RP7IcG7AUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: جنگ جدید دامن همه را می‌گیرد
🔹
هشدار رئیس ستادکل نیروهای مسلح به سازمان‌های بین‌المللی به‌ویژه آژانس انرژی اتمی: حضور رئیس باند تبهکار صهیونی در منطقه و اعلام این مطلب که برنامۀ هسته‌ای ایران وارد فاز نظامی شده است اولا از روی توهم است.
🔹
از ادامۀ ایفای نقش گرگ در لباس میش خودداری نموده و از ادامۀ اظهارنظرهای بی‌اساس در مورد مراکز هسته ای ایران پرهیز کنید.
🔹
آگاه باشید اگر جنگ جدیدی علیه ایران آغاز شود، آتش آن دامن همه را فرا خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/466396" target="_blank">📅 11:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2AKGjgH-myBd6hNAoH7SYEjX3w43O1X7nNW-qSaqBjdYfU7SEI1c5nz6j58xJ4XD7p_r8k_hjMO-z6Zoapo_r0RZ3Cyah3fdSjWX-j37uUJ5fCsZGL8gKbErnxgo-H3z_bVaA56Rd7n44Do17vEJMbuP1LUeEkJJn6vp0DsJau5Oxb6mG4jyacssZ9B68b4epeOpAVC8D9BWndBaeEbw3b4tggYW6eGTyrwjQ6kQX8LgFgDWiD82ZDaFY3E-XDJ1YqrcJLoNEyGaRxzoOs1gmKBppDTHomAA9h2QFEzsk9R6KY23Atyg3D-ArxxEck4g3jubctshQxcUg3E9fiyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌قیمت کالاهای اساسی «تورم صفر» اعلام شد  برنج:
🔸
برنج پاکستانی سوپر باسماتی: هر کیلو ۳۳۵ هزارتومان
🔹
برنج پاکستانی۳۸۶: هر کیلو ۲۲۰ هزارتومان
🔸
برنج هندی ۱۷۱۸: هر کیلو ۲۸۰ هزارتومان  گوشت:
🔹
گوشت منجمد گوساله یا گوسفند: هر کیلو ۱ میلیون و ۵۴۵ هزارتومان    روغن:…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466395" target="_blank">📅 11:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbDGekd3-N2WujSk-4xdogxRitBSQzwsGVGoaKNSg11hcIqWxYl6xQCTCYVNePDCdHqvRlpRZHR8Osq3kbrcuALLtD8sxUDb1r8re8Y7DGroUoSr0ueLJyXH_zgCqBGAk4rOBdWZZFVXyFeBp5dJRmMPCjpwQFutSRS8ZKVYMSpzpgbXhKCtmGxpUsKs6vEpoNgrkZmC5_YlxxqNA0EBOJ7ufabhuxDcGu1d2es736kEwR1_aL_Grvnx0oJJu6hKTI3v4baAKOUpis3yv-9QgemBhUerFAB7XhhauDWHStNV08PUdKbI5GiCYLLrJFeMVk9JL0ujmRoMlyGvM27vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: موضوع طرح فروش ۱۰ هزار دلار بانک‌مرکزی را پیگیری می‌کنیم
🔹
کوچک‌زاده، نمایندۀ مردم تهران در مجلس: چند روز پیش اعلام کرده‌اند از روز شنبه به هر فرد بالای ۱۸ سال برای رفع نیازها ۱۰ هزار دلار فروخته می‌شود. سود فروش این دلارها تنها به جیب دلالان و رانت‌خواران…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466394" target="_blank">📅 11:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466393">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c7ea927e.mp4?token=hWAU9qexrSkLKJxnvV2k73EBRRtCwfal33ZlyWcevCNsD-9U6Tp4NPOcLrZevvtmylnxhLz_QJtGXD3Zr5gJzQ_dYVvst-poBkJLUQb7hFODIa2MaSmGdB4UsxPb04rc4j2xmSPCr60DhAs-0b4Zya5QbA3djKPhrPBpnxiU4VrWPuJi2XQ8EYu4XOj5qf95wMORvXC0igwd2cqtnTHAvderSjUHQeK1l8HFXVjp36v9MjqWeWCpuuTfilT6gIznQZHke7eOsNGCKI6O-E3IE63HhcGLjOiSBqr2hyt4Hv4zjQacTmczGdeQ5ZP0gmYx6yt5YG4o9v5UKwJIb5OkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c7ea927e.mp4?token=hWAU9qexrSkLKJxnvV2k73EBRRtCwfal33ZlyWcevCNsD-9U6Tp4NPOcLrZevvtmylnxhLz_QJtGXD3Zr5gJzQ_dYVvst-poBkJLUQb7hFODIa2MaSmGdB4UsxPb04rc4j2xmSPCr60DhAs-0b4Zya5QbA3djKPhrPBpnxiU4VrWPuJi2XQ8EYu4XOj5qf95wMORvXC0igwd2cqtnTHAvderSjUHQeK1l8HFXVjp36v9MjqWeWCpuuTfilT6gIznQZHke7eOsNGCKI6O-E3IE63HhcGLjOiSBqr2hyt4Hv4zjQacTmczGdeQ5ZP0gmYx6yt5YG4o9v5UKwJIb5OkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازدید ۲۰ میلیونی نامۀ سپاه به مردم آمریکا
🔹
نامۀ سپاه به مردم آمریکا در سکوهای داخلی فضای مجازی با ۸ هزار و ۳۶۰ محتوا و ۱۵ میلیون و ۷۷۰هزار بازدید، بازتاب پیدا کرد.
🔹
این نامه در سکوهای خارجی با هزار و ۶۶۰ محتوا و ۴ میلیون و ۸۸۹ هزار بازدید، انعکاس یافته…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466393" target="_blank">📅 11:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466392">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M640Xi7SwltAA635Q11T2YFJtr8bisKYdmr-yUD5kGopeZ4rarmlMFDB-CGwJDDr1YHOAXLGK8VbQ58PT7hq67ecueK3Mq17T2S91x4dwITrL4LB9a5PBoiNZQJEfTSr9Fugrm9x0alGKsYsKlfJU3QhqVOh3F7H_J6W4L2PytvrdtbPfBUEbXFICWMxzbhXij7Wj94H_liqjXfierDbei8Uz3gOyxGsmOol7LRg1zbgLiiX0IdBas7Qj9RO5lob4qmIEzRH-YH0QilAda5udzjMzKjE0mnlV-UuHmgV1yXU9lNWt7U0-UGvf1U5bMovWPARD53gNz4vTJW6hAhkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقامیری: در کودتای دی‌ماه پایانه‌های استارلینک را از کار انداختیم
🔹
دبیر شورای‌عالی فضای مجازی: در کودتای دی‌ماه، سایت‌های غربی گفتند ایران اولین کشوری بود که به‌صورت مدیریت‌شده در بازه‌ای که می‌خواست استارلینک را از کار انداخت.
🔹
البته ما چون خودمان انجام داده بودیم، می‌دانستیم اما آن‌ها خودشان اذعان کردند.
🔹
ما در آن دوره یکی از فناوری‌هایمان را درگیر کردیم و فناوری‌های دیگری هم وجود دارد که از لحاظ فنی کاملا عملیاتی و آماده است.
🔹
اگر این باب را به‌عنوان ابزار جنگی استفاده کنند، می‌توان به عنوان هدف مشروع نظامی در آینده در نظر گرفته شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466392" target="_blank">📅 11:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466391">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLjdnV8fQWWvKI_yXrrf__mEK6oTh7K3Xw4ap8-yay4ldBK-j0LCSmVlhpxOPM5RcTcALse33JHXwEvDv5bF_9AdQExBPDdg0BwfLRCeyS9-gTpbEnvkTHwaeqYAyVQu1HSTaA4x-tiUPfM6qG8AgDejPxoXWJl24bpgaVTXwzc7pfXXip5PFww7QJsBgOr9Aivlm0BAuWkjejXKbmduTAhMunX8i1bbHeMmGHOEvbEQ6N7cgG7twlroVHNdTKjXh8TgrhUR2rBmUjQfhqCaxOe_TKEkM-Pl1uAphiRVLZwCdNcAEISMMiNprEtkJr1HQaFpwtLJmTwTfkS97IssSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار عراقچی و میرزویان وزیر خارجۀ ارمنستان در تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/466391" target="_blank">📅 11:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466390">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D77YDam32BwsKGfXRFGGDbVf4BXbBo2160ZsA0Il2pP1QH7DlEsybHGWFhA9lj_Lnqbz8KL-chQr-1_CxTZK8URbnHM1u5qngJfF03PJkgXCIw9tvfcsGKToeVq7f8fvgC82Q2jJhnM5CWD7w2RloZL_Kr8_YpF3nEfGzz0JT4CHTG57XKu7jP2BqXJEx0T2jU8Nt5DfqDT3AEwV7ZLQy3MLSZVLMgfiaCCF5KQRV5_LLD3qeQUfmQDIDlzjLHhpc086GC24-MhnQWy9wNkoTgEqPjSrY_Tp0JdL7sQU96Cjhyd1UV6VLnJ9J-9CUZGInfXj9C1gVMmDz1WiSfaA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسات مجلس از هفتۀ آینده در محل دائمی صحن برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسه مجلس: طبق مصوبۀ شعام از هفتۀ آینده جلسات صحن علنی با سازوکار دیگری تشکیل خواهد شد.
🔹
براساس تصمیم جدید هیئت‌رئیسه، جلسات صحن هم در محل دائمی صحن و مکمل آن به‌صورت وبینار برگزار خواهد…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/466390" target="_blank">📅 10:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466389">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgShqAsLJZP65P_qEThlCVm3oidUzQvMvZF0ZLyjdczgARxtSj6PRFr2IL1h7gSqmRWywC0xp25F6QQKC4pCo-osVuRmVR6smPN1drI6MupAqXqlcGR_dNg6c-h4W_J71xNKHx8pCSMfrV4aNBCuJZd_0M2A7Z0GnjG1idWLDtfqTZlUy_OlPeJRLJv4o8hhZlCM4HdbnggX612jM36waEyDrZUyldAheq_S5wJy3jWaI0-r32xc-_g5OXgietyLRX-D6bAQaxbp2Kvvld7PRyBhNI1kw1_Mr-q2xreIF81hlrM_iSbvlBMUvXAP8MYF_8wGwQNQiQCMgQdlGb6IyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش مجمع وزیران ادوار طی نامه‌ای به رئیس جمهور به رئیس جمهور از عملکرد دوساله مدیریت گروه صنایع پتروشیمی خلیج فارس
✔️
هلدینگ خلیج فارس با عبور موفق از تنگنای دوران تحریم و جنگ وارد دوره «جهش سودآوری و توسعه» شده است
🔹
این هلدینگ «دوره رشد و تثبیت» را پشت سر گذاشته و دوره «جهش سودآوری و توسعه» را شروع کرده است و اکنون از نظر اندازه، سودآوری و ظرفیت سرمایه‌گذاری وارد مرحله و موقعیت متفاوت از نظر خلق ارزش افزوده بیشتر شده است.
🔹
سود خالص ۱۸۷.۵ همت سال گذشته نسبت به سال قبلتر ۶۷.۴ درصد رشد داشته و تولیدات آن به میزان ۲ میلیون تن نسبت به سال قبلتر افزایش یافته است،
🔹
در صورت تداوم وضع موجود، این میزان در بازه زمانی منتهی به خرداد ۱۴۰۶ به ۲۲۰ همت می‌رسد.
🔹
در مقطع حساس دو جنگ تحمیلی و محاصره دریایی، علیرغم تمام سختی‌ها، روند تجارت و صادرات هلدینگ خلیج فارس به‌صورت شبانه‌روزی ادامه داشته و در بازه زمانی دوساله اخیر، قریب به ۱۰ میلیارددلار ارز حاصل از صادرات محصولات شرکت‌های تابعه هلدینگ، با استفاده از سامانه نظام مالی-بانکی فروخته شده و به کشور بازگشته است.</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/466389" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466388">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3vpoiZOZrW4L01AxHY9cVogowqszyX_p_vINvsMj8LZrNxYtWT5rb0kAmrKLwX5vrOE_r0hr6gB8DPZpBxNAxfPjpYccLv6fxRg7-Yisd0x0GaiHjYdTROGpEDqx5eRNazKwL0S2AKI61GbdKO_vVKNLDJghRuagD-hl0IhH3vqn26d3yvIxnuq3w4opP6KLaiKvWXCs9bpOS9kzzkyc4NjU4ovtnsXDroc7iZo1cK8scttfc_x6LJj7zAv8FYoMbE40xY3jYeC54ad4d3fFkJgoFqOT3OqDQlVkCJvXqvCQcDjLfJF9LeKgxHdgSDoPAWrOfTuXpJA3kIW4M091g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت 8800 فقره تسهیلات فرزندآوری بانک پارسیان در 6ماهه سال 1405
بانک پارسیان در راستای حمایت از سیاست‌های کلان جمعیتی کشور و تقویت بنیان های اجتماعی، در نیمه نخست سال 1405، عملکرد موثری از خود نشان داد.
به گزارش روابط عمومی بانک پارسیان، این بانک در راستای اجرای تکالیف خود همراستا با سیاست های کلان جمعیتی کشور، طی 6ماهه نخست سال جاری، 8،861 فقره تسهیلات فرزندآوری با اعتباری معادل بیش از 7هزار و 860 میلیارد ریال، پرداخت کرده است.</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/466388" target="_blank">📅 10:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466387">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/466387" target="_blank">📅 10:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466385">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4-SzHDXSMmYVANiJOE7ciA4hpvzkCka9t-a0WmrfHez_eEAy1Cpqf4yQQkmlJEuCkwFhNQrBwEkT4KWagOHYrUs5ALdPnpF66IRgcQxwWYpwyKO3eeQKHrj_D0tkGDMfMif-EQUH7Emr7M5vNz7eoUrGTTI4nwfzrkUjc9zRUr1GkgwU4QpbvogRrAH6M2nd_wDdWXEw111t-0nCUAB_0ppmelahFbJ3xLww_VazfH8tSWxS-v9_G2yaGBC_qalG8KQOxtuoEIm4jej2j_B0RYoMy1UXTqddavMIvKr6k4i79e62B73rSIyy_smFQ0U7GXtdJ5JSMePlJzNjx86Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2jSgQc8zMvKt8J1gtKtMrcfGzVp0E6LGKJh_jzK-85lOP2GELHz9wYJPXRfSx3klcsAyKV55AauK8KmuRpxRZpPUgohYkZMcsfHgnTCS2ybzitJw-jTx_SgMM4bJ5-hbRkVtChXt11wtCaD7OFvP18TfJusiuy441-NcORkn_TfEk7iwMCNz2lqXToSxUWUfa4tozsu_SdJybypELLw0v97kTSzh6nrIwC4BDfuTYnTPysXyib5goO2hfOG71UKiZ5gtcexQfGm0vXA2Adr0ru4hCOU76VcY-naNarZhGTzuRxNBT1-F6eY4Pza68SnC2lTH2gQu8j2sUz8_Q1c7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهادت ۲ نفر از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
ساعتی قبل، تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو فرماندهی انتظامی شهرستان بمپور که در حال گشت‌زنی و تأمین امنیت مردم بودند، حمله و به‌سمت کارکنان انتظامی تیراندازی کردند.
🔹
پلیس سیستان‌وبلوچستان:…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466385" target="_blank">📅 10:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466384">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYh-v9x2WuE75w_rZyGeqUHfkJqX-4BkscsWdk4zUFWkrcms9dwywU3kPHH3fE-Uz6HRUDiwGG2Hm9qBNsqoYdzAAAennE0IkkXuE1xsIljG-DhIZiXD9QtHitJgzhJGOb_VRJ8zPQXdrqwI3Io_WJQX0cD2ORr1M4LqBW6iXU2aVP-MN6pp4XSt4IimOMjizUCt92wqCeZ4lk6yrd46AeXQCEXr2NxGtr_m0qd-YEEBTwt4K46WrWCkBuR1E8ZlSBxEbkI9ndT65yhxdvujKn8uziOCqpbA81Z2r0U5XGgrY4bviNr-LjMDOWPV1eQg3Z4vOpFocKVWyUjv2-LhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466384" target="_blank">📅 10:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466383">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f778845b4d.mp4?token=a3nW16eO6oEyVIoXVFhXcj2ecXIi7-h3wynt9C4KJIDQqTNw7_UL-8EoJPHu__7wbbAGrXurx_TC8sXl5CykmN1KNFWoplgTbIFfI2JpTvPYyFrnee1jrx3PMql_I7819SF2C0WPeW6OJ4YpEy7XoYvW6Y5V7mqC7qrgQo_2pNIKNLPRihmFBo-CodmdoWLsw0YCQDMluYibTkmi0P0U6WGfE5XNcQspSaFobYAp2fSS2DcbEgr_fd3K08Zo4pHU8MW-tVUFlEssfs2wKBa-8MewMtUFDHvnJDUqv6Yu1wJFdYt-JRN589tFS6J0cDVTOypMCYFA9CW9nEVy8HCiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f778845b4d.mp4?token=a3nW16eO6oEyVIoXVFhXcj2ecXIi7-h3wynt9C4KJIDQqTNw7_UL-8EoJPHu__7wbbAGrXurx_TC8sXl5CykmN1KNFWoplgTbIFfI2JpTvPYyFrnee1jrx3PMql_I7819SF2C0WPeW6OJ4YpEy7XoYvW6Y5V7mqC7qrgQo_2pNIKNLPRihmFBo-CodmdoWLsw0YCQDMluYibTkmi0P0U6WGfE5XNcQspSaFobYAp2fSS2DcbEgr_fd3K08Zo4pHU8MW-tVUFlEssfs2wKBa-8MewMtUFDHvnJDUqv6Yu1wJFdYt-JRN589tFS6J0cDVTOypMCYFA9CW9nEVy8HCiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا دانشگاه است، مبدأ تحولات!
🔹
دانشجویان دانشگاه‌های خراسان‌شمالی این روزها با برافراشتن پرچم ایران، پایبندی و وفاداری این محیط به حریم وطن را نشان می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/466383" target="_blank">📅 10:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466382">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شهادت ۲ نفر از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
ساعتی قبل، تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو فرماندهی انتظامی شهرستان بمپور که در حال گشت‌زنی و تأمین امنیت مردم بودند، حمله و به‌سمت کارکنان انتظامی تیراندازی کردند.
🔹
پلیس سیستان‌وبلوچستان: در پی این حمله استواردوم امیرحسین قاسمی و گروهبان یکم نظام دست‌گشاده به شهادت رسیدند. یک نفر دیگر از کارکنان انتظامی مجروح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/466382" target="_blank">📅 09:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466381">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5BlecaF9A2eYVtnkO3A42TtN_zGV-yz_d-dxlwCiNJAbRAysUnEnJqvM2FcDkYJslt5oYaoDAlr4i6v4t6hA2nS2jF6CgbyvnANYtgEwdxh9JVLluSE1gF4KGXBFD6Jc25P7Ou3f9VpnNFLtom7m2-a--0BsmaCZausvSPJJ8jx-dQe6nZ4TZHyt9uuiiaR3ER-9u9WOlwZfvFnf1xj3PExwh45cKnQMus_V6nOFFNyJX9t5KaPVo5jGjiun8XF4ZU8EgbE0UFxGrAgfgndKZqw7g0E1e5nlgfZKqG3MkGs3Kz-5R5aFE1BfqC1TZidlTnCpweScZfR4mTy6D1NDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد انصارالله: تعز عملاً آزاد شده است
🔹
عضو دفتر سیاسی انصارالله، با تأیید محاصره کامل تعز پس از آزادسازی مناطق اطراف، این شهر را عملاً آزادشده خواند و تاکید کرد که این پیروزی با مشارکت نیروهای بومی استان و حمایت مردمی به دست آمده است.
🔹
حزام الاسد در گفت‌وگو با شبکه المیادین همچنین تآکید کرد که نیروهای مسلح یمن جاده میان تعز و عدن را قطع نکرده، بلکه آن را ایمن کرده‌اند، در حالی که این طرف مقابل بود که آن را مسدود کرده بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/466381" target="_blank">📅 09:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466378">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuhMLxzTHZBj83wdI8Rmyn8sYQQlnDC68Lg1DOT5VpvPCEXlGr407Yzhfo6EZbfWBW_cuxANzfLmJGU0tnTFIiDdYjGcnT503emxZ0AUymHLLR_2jzWann-rX6ZfHrUGyUFSTzux39EC9cwoRFP-PNidcqi725U0CjvAJjtyGjarNkKLA78JXZHlxH86_r7WajfqQAqs64tZ9cUo0-25bEWW6EhhAEGLhAhHPUTd77cDsflmiTAAa_PzdVECOrOY9EArobfTajMo0rZFaTFwKlqi7OS8EwmGZJww6jMJ4Rwks6QZiUo-Qe1MGqwKFrlrHiA00o8pfm5WNmOF7D7fJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fb3MSZp9equvFlqr8_Ih-UuvkpJtD2woRfuPiyKe_RW9vwptp04sMdeyVNu-FaBw2KD2WnZuN7iXvEg57mXDYjmmxQM1Q_GDWBO5Mx3OposXRiVFUHOGUIhQqDFCLj4jKXzGuFEsCmUNinA2DF1M26cYLV1_8162mEECWR3gLwXOc6RhLDJsnCP-TmxKPEv6-9ho_3r1slYv5vY4dqsEGXUFv3NxSnnCeeF6L6kdWs6K1PVgyQH6kQiqRdZLeXpHe4Sp1s_Zj2eYqTsiQ0AJXqbhDKB9suDDBKpJD8BHOBjIrmcsNBHRdn4uPBfNmGpVMLavkUtWtiJlj6ETk0VIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHU5WvlZwq3olJhnMapr3nr4hds_xRlKTgh98IhDENVDQk8_yBaVg1DdmVdUJl1srq1-aCR9KUSbONcVBiGSHPpn5ydN5LsW8ks-TEjWrViugbN-ezInwmNkFCwkSq8WsqWPb4rUuHcVTFoxZ_xVuTsJ9bV9pVUi_1H6JLpxW75VLyAoJ78xXUpmouey1MJnTj14qVDUUFoi89M9-XjjktYQ_tZR_yFZtJqI5rmaVpMXskRzWjsFjnXKBMc_uy5jmSbmR10YeFVxTcUC9wuox4aFNB6msUDGzLvxrAuhyO1N33N8SeQ6-tqiRVWQKPE6UlEbvzQpwaKq92wdVBBXPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
زهرا زارعی در دوی ۴۰۰ متر مدال نقره را بر گردن آویخت  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466378" target="_blank">📅 08:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466377">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316cf2ab4e.mp4?token=HE5q0MxrdIX1BTopEFirkDfP_U3u5ANYFH9-3W_FDUMU0CW45odyYfOtdoVoQw_Ug9TwLJ7E_cC7iqp9ORrYyXFNBPurLevNoFRccD1A5i-5UhxmneuVoafZmD7wAksWkS4WWqazaxsz80v4Udho9vgGWnWTIbEvLjLIWym6yZLMIrJlPirVzDiFtDRUHbIxTrAYZixfOsTgNa9sIBj4dF9nyoqxGalrJ_DIKgqWJdK0fZ7EC5LFj0rs0YMLbFH_gqVCOIGouZzTmgZ7jcKUuUNzy5M4xg-sILq5tYNz1DiW1I9pl-xPx_b-Vfp-oQl-0pOTElMLDFTpf0imIeTtXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316cf2ab4e.mp4?token=HE5q0MxrdIX1BTopEFirkDfP_U3u5ANYFH9-3W_FDUMU0CW45odyYfOtdoVoQw_Ug9TwLJ7E_cC7iqp9ORrYyXFNBPurLevNoFRccD1A5i-5UhxmneuVoafZmD7wAksWkS4WWqazaxsz80v4Udho9vgGWnWTIbEvLjLIWym6yZLMIrJlPirVzDiFtDRUHbIxTrAYZixfOsTgNa9sIBj4dF9nyoqxGalrJ_DIKgqWJdK0fZ7EC5LFj0rs0YMLbFH_gqVCOIGouZzTmgZ7jcKUuUNzy5M4xg-sILq5tYNz1DiW1I9pl-xPx_b-Vfp-oQl-0pOTElMLDFTpf0imIeTtXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دزد خانۀ آقای سفیر دستگیر شد
🔹
پلیس تهران سارق سابقه‌داری را که از خانه سفیر فیلیپین سرقت کرده و به اسلامشهر متواری شده بود در کمتر از ۲۴ ساعت شناسایی و دستگیر کرد.
🔹
سرکلانتر دوم پلیس پیشگیری تهران: در بررسی‌های اولیه مشخص شد فردی که به‌همراه همسرش برای انجام امور سرایداری و نگهداری از فرزند خانواده در این منزل مشغول به‌کار شده بود، پس‌از دسترسی به محل، اقدام به سرقت یک ساعت مچی طلا به ارزش تقریبی ۵ میلیارد تومان کرده و از محل متواری شده بود.
🔹
اولین اعتراف سارق: با حقوق ۱۲۰ میلیونی سرایدار خانه سفیر بودم؛ ساعتی که دزدیدم ۵ میلیارد قیمت داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466377" target="_blank">📅 08:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466376">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انتخاب اعضای هیئت‌رئیسۀ جبهۀ اصلاحات برای سال دوم دورۀ سوم
🔹
در جلسۀ امروز مجمع عمومی جبهۀ اصلاحات ایران، ۵ عضو هیئت‌رئیسه برای دومین سال از دورۀ سوم فعالیت آن انتخاب شدند.
🔹
آذر منصوری، محسن آرمین، سیدحسن رسولی، بدرالسادات مفیدی و جواد امام به‌ترتیب به‌عنوان رئیس، نایب‌رئیس اول، نایب‌رئیس دوم، دبیر و سخنگوی اصلاحات انتخاب شدند.
🔹
هیئت‌رئیسۀ اصلاحات از ۱۰ عضو تشکیل می‌شود که ۵ عضو آن شامل رئیس، دو نایب‌رئیس، دبیر و سخنگو، مستقیماً از سوی مجمع عمومی انتخاب می‌شوند.
🔹
۵ عضو دیگر هیئت‌رئیسه، رؤسای کمیته‌های پنج‌گانه جبهه هستند که پس از انتخاب توسط اعضای کمیته‌ها، به ترکیب هیئت‌رئیسه اضافه خواهند شد.
🔹
لازم به توضیح است که هر ۵ منتخب مجمع عمومی، در سال نخست دورۀ سوم نیز همین مسئولیت‌ها را برعهده داشتند و مجمع عمومی جبهۀ اصلاحات بار دیگر با رأی خود به آنان اعتماد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/466376" target="_blank">📅 08:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466375">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ba26dbe8.mp4?token=dv-LrwjNzkg8daBvzuCxBIAnxzNkkVRh-irH64FgAgMOCN7qGbGl6ZkpNFD9jQQ5za39GslQyJqPfd7EHSMGwpofiDP0yOrSoIw7B659dv2eDYmjnh5kJGaSFGgzqFs3AAFaOABlJl7xablDbmSGAPLWoRU7DQMvRox0Pv0SqERr0cVBjwOYD1o4dNmgB54bCveYa53FTXwnyRTr7SwSQyawI87m7ikNjeaePQKrQjEl1btvx-2jx_pJXXRnSGmTPB9fvEX6ryNiDRTNGDsmCJHU7KK5qUuJ7xnDie56Gk7EKe1GxuhSnsCo2nBgQUWxOlDVf5ZdOv-WT-xW6GezkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ba26dbe8.mp4?token=dv-LrwjNzkg8daBvzuCxBIAnxzNkkVRh-irH64FgAgMOCN7qGbGl6ZkpNFD9jQQ5za39GslQyJqPfd7EHSMGwpofiDP0yOrSoIw7B659dv2eDYmjnh5kJGaSFGgzqFs3AAFaOABlJl7xablDbmSGAPLWoRU7DQMvRox0Pv0SqERr0cVBjwOYD1o4dNmgB54bCveYa53FTXwnyRTr7SwSQyawI87m7ikNjeaePQKrQjEl1btvx-2jx_pJXXRnSGmTPB9fvEX6ryNiDRTNGDsmCJHU7KK5qUuJ7xnDie56Gk7EKe1GxuhSnsCo2nBgQUWxOlDVf5ZdOv-WT-xW6GezkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا ۱۲ بمب‌افکن B-1 را از انگلیس خارج کرد
🔹
پس‌از وقوع حادثه‌ای در پایگاه هوایی فرفورد انگلیس، آمریکا تمام بمب‌افکن‌های راهبردیB-1 مستقر در این پایگاه را به آمریکا بازگرداند.
🔹
این پایگاه محل فرود بمب‌افکن‌های آمریکایی برای انجام حملات علیه ایران بود.
🔸
طبق گزارش وال‌استریت‌ژورنال، این تحولات پس از
حادثه‌ای
رخ داد که هفتۀ گذشته در نزدیکی پایگاه فیرفورد در غرب انگلیس اتفاق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/466375" target="_blank">📅 08:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466368">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIhtaRkAyzTzeZNrz-zB4QHAKkoVs6ECAfTYuVq5XgCr63KJA_IryPbfbFaAin2aGLbTgbbpZuFd9QaLhyCcPswlBdUoSgtXTQrxwPXj_UQlN-5YxRQZNfqZbVLzyvqv-8_3B89H2K_66Cva6MQMbZLy4kLupTPfmFC2uhCNNp2Zek88CUeXolQrTv0CiLAKlStt_UkaanXZR1YnVyjgSgaWbm_Gw9gGO1r1bJvvr692_5IaWktUKqUFBGAeTGfvK-4FiRN_SObodCQSZMzO0rPcVpxwSxrSv8UTJjnFh0orK7uavt48hHBspzt-5ZGNzyEP-OuQWhKhrDPaakpSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTTxLpUTfVOa5st8Wo7nnQqZpPARY0ireQlgNSVhuGurzk5pgjnYbXQrdgh8mhMEAh7MGZBULL1CU6k5fxILGhOvkCplrFOQRfdII_d1JC2ia_9nZ3aSJZkaYo1sSCwqF6OHb_RRuEc-yyYR-C5BrkE5Tf3wawH7QtlTp7FstG9m_Q3FfchTlvg48q-EaWIbyGXtN5oJ98bKu4yOJRw3Zkjc6R0DImnsoSnKhen57E9r9lhZaUKA_aM9AXZi-aiDQ7adrIJLTBQTaPzcgTYgtvW9nA3cJvb9nYF1ArIMAKVya6yHBsyGGZo5Bt7n54_IQoAtOmIpsW-U_GA9_kUj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBwBesw5eVGYnDmOQNPKfLbdWTGS-UYUhWl-9yHPCrwyC6fDpXEUK9I679nw3qwiyXE_N3zWxY9m4ZpDiVPcZe84K4yf7FBf4g9w4-Uv1zs8Ts6RCxy51aODyV4WvbaRcwtLuezrPHNgGX1MagO2OrhNCbCpUoIAePzdy67w7SB66Bb8P6IgI77CEq6xtm5A4a8zpFPbrhi5Z-1ufKpCw1vcFWILruOh2zUKSYTyqQwEnPPivkOWAlcerSEKAQZO0CdiEXPIgyeyIPDVLC8idXKkPT5fEHVqX08Pfu8Y3RewsXrcNszIzpJhXD1G-x2sbocheEH_DXaKHsUD88RQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDNgNLFRE1K4NhhcfZ3yoPukca1gvcNZooVOCAkN6J9OpOWAeoZTh0pGu767BGa4KI-9OL4v3aO8S0ehaGHTR4DEGwiHjAmndkQ3QqJ6fJKqb4_vOAiWdORbNnrWotPQD3Z8dOvSFOAtRiE0L2Hwdx4wTbxsCNnskyAlCBCPNFDojXwBPIHMzanF3OLHQE6rEOK6uAbcZUvc86cD_JAIBjUNhSUgANJmPXqbDqblMzuNLSC0tXAklTBDtf-HAYt2Ou9H6zED6gsCo5HmV_ooxRA_ULEowgkCTsWfmaWg4g04hiyRpwkOnuniAbjQgVQjtbqr1ByL0T8yqK16VxAqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ye925VUs5aAxDzbDHYJDWPYZTWsmLd25UXshtESH6UANKIErTZOMpPe2tjz9aV6ms7k2e5U8kxBseIxqho15CHZpeyVeK6sMbhxtUCvoiuHNwWfSa_fonD8lw2DSYgLNqw1xaMHx9J-x_Df4x0n_kkcmQqstORYI24VKBhDkJLg-nYWfcEkJ-KhtkoN9qswPc10Mngzzty3ETd7S3wnD5ey_GPbUMXCkHvUq-M26rdSpGcfO82M81pwtvglNugPu6MxlV1n9vhEuxcBmokxo4dNfp2NbiTK-_xWtaCA3vNbfhc_lEJstm98xrcxJXGYbB6YXeNQL-xzP4yiIJxIRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2qsus671cNnt45ZSdj6-e0VsKfUBUW8Cz9Xv4acMzZNGClThwkhU4QzmjNOnsIJTl9OzRbvzJmTF6CzWcRfZ0oJ95WFXw8RtsUhkYQ2yl-3AVgx8UA2ksmH0e0HbrvBwaPvpkZkTT4NEmn-uFMletKwHrQxYFJl3fY-2CM-jzCjfSVv14vhUrDDYvFByQtdSbkyZtde8A6HWM7PZjN31LZ_fiptPQfUfeAK_wC7KcUZusb9dG009pOW7EAtL8KvOsVg2RXUMaoqQ6RXCtd2zccikQA2S2zSI6c6aKZCpUCqPbq0EJW7f9wYh-lNdw1YZ-ymY_PfsbcLDP2_W4ikwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCJSJpvLMjmXbhwM-uhBdOZA8xwQf4QWPY92MICIurQB2i-7B9IigQqe3FZjzfwArnVbIruNObVb80FkDOP3eif2-S0YJTdBcBxzi8abm4lF4_sz-ST4iL2kJLT-K5bufarSBFXsWN11ZP1obRFeGBi0S3Dz96UGnthoAqf-WSRPyV39DYl63aBYE9YhzAY02-PNDp6b31nEPLm_1VDZQNXDbnFNDabD4JKDLNH5RwrM0hc9EinADGAkPfXqioT12T6kb7NmlYlcNYqH0vV33gVx_xNnYcyEQHIVajTOP_rEgl0srsBS5fribDJIsceSojIklVDowqJCHGV9NeAIXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عرضهٔ ۱۲ قلم کالای اساسی در تهران با قیمت ثابت
🔸
شهرداری تهران با اجرای طرح «تورم صفر» نرخ ۱۲ کالای اساسی را به مدت ۶ ماه در مراکز عرضهٔ تحت پوشش این طرح ثابت نگه می‌دارد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/466368" target="_blank">📅 08:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466367">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af80ea68b0.mp4?token=rZgxplVR7u9xa_EbDaN3cndUn2qgzWNxHGUPQooLcRlp_Iu8fVSWa0Y-F97p4fK42hQely1k1IeQ_bsPX6HsURlXeP8FEc3rdDqH1HxQhyIwFXKeuXLJpBvE9unDPw1FNu5B-VkAzqc_yhDEB4deZ7HRfeJquZ8ISZF9eEdzU9i3tjcNG762YiSyK-TpeCDw-zCLAzDNGuokjKGWMh9JIdpUkeuyDsjaEy9keC0k885U53ZrNUYgqrZvISqAlXnhl9pHtBluPOk0R3xSoSMUTt6d8bqsXuZeAXjSYEi6MwLoJiM2td0oFsWM_g1ZPxV1LpTUx3BY25aR9V52hiB8EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af80ea68b0.mp4?token=rZgxplVR7u9xa_EbDaN3cndUn2qgzWNxHGUPQooLcRlp_Iu8fVSWa0Y-F97p4fK42hQely1k1IeQ_bsPX6HsURlXeP8FEc3rdDqH1HxQhyIwFXKeuXLJpBvE9unDPw1FNu5B-VkAzqc_yhDEB4deZ7HRfeJquZ8ISZF9eEdzU9i3tjcNG762YiSyK-TpeCDw-zCLAzDNGuokjKGWMh9JIdpUkeuyDsjaEy9keC0k885U53ZrNUYgqrZvISqAlXnhl9pHtBluPOk0R3xSoSMUTt6d8bqsXuZeAXjSYEi6MwLoJiM2td0oFsWM_g1ZPxV1LpTUx3BY25aR9V52hiB8EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چاقی بیماری است!
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/466367" target="_blank">📅 08:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466366">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp6cWtMsTuk3wi8fkr-1-xFF84RmmEt-ofcNS8qBOsnIYD474Qn8tBDMk2eCnzAmzU77S-uBLQx5rW37BqTCbXbaY09obyh6JXERexO5uviaF2Xxr6PADkvEFjTrL1BUgdmYLkaAMwtD0NpxQTrxGXBtPKyIxn_DbcT-aJG61RtjcaW_Ke4ANqinS-5m9DqaIGVGRH_kqJd10p8OZ1KkintwCh6Dc6fdHqngX3oLqvaoXy4PomI8a3XDO7t7v537W9hNH3sovhkQrMhbgPuFJX0BCz1JCDuH25LyAhBN6atrD3hCxRT6RPX0t-_DsLsB-MJPqWw20T4Afei1Or6lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح «تورم صفر» به زبان ساده  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466366" target="_blank">📅 08:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466365">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Km3jEbDZKYf3SWEqaQTuMbKMTUDQbQI-TlYVsTqW8KVCz9DyUeDfpbaFMzSgS9atv2whoGwnSdP2LOvOfcDHBRvcyRVeh483HGMsG1sVE43OvG52Tr6Z6vVzSP89Wm15Me__z1R87jjlu5A3BhEV582aM_mCfCq1QF3qdw_1ulvhgX6s7qftjGAsNSitoDjXZjHSG-l0YC5jiWJQOHUf87WpgiSH_H72bnie2u1Wawvphd5HsmRJ_qtIfUrLh_P3wI-ymEno9UWIhgRridTWQR3rdo7tmIGswOg-ef5FJzKNCJPrqfYcbNr0LWjeBJdEDpqmhdEu0Qyasu1oY3k6yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبهٔ ۹ کنکور: می‌خواهم به‌یاد شهدای میناب معلم شوم
🔸
هانیه قربان‌پور، دانش‌آموز مدرسهٔ نمونه دولتی مطهرهٔ مینودشت که رتبه ۹ منطقه سه و ۷۳ کشوری کنکور علوم انسانی را کسب کرد، می‌خواهد این موفقیت را به‌یاد شهدای میناب و در مسیر تحقق رؤیای معلمی ادامه دهد.
🔹
او می‌گوید: ماه‌های پایانی کنکور آرام و بدون دغدغه نبود، شرایط جنگی و خبر شهادت رهبر، شهدای جنگ و دانش‌آموزان میناب بر روحیه‌ام تأثیر گذاشت و برای مدتی برنامهٔ مطالعاتی‌ام را تغییر داد.
🔹
آن سحرگاه را هیچ‌وقت فراموش نمی‌کنم. شب‌ها گریه می‌کردم و خوابم به‌هم می‌ریخت؛ حدود دوماه ساعت مطالعه‌ام نوسان پیدا کرد، اما تلاش کردم با وجود همهٔ این شرایط به هدفم برسم و دوست دارم این شادی و موفقیت را به روح رهبر شهید و تمام شهدای جنگ تقدیم کنم.
🔗
شرح کامل گفت‌وگوی فارس با هانیه قربان‌پور را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466365" target="_blank">📅 07:45 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
