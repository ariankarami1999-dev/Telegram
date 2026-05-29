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
<img src="https://cdn4.telesco.pe/file/fQYvqGzRE0SKhC4z7cWwHNAsdDrQUWsUBW5DYnr23rG_zXk9n90U_6mCyhcKCvUpnqLWDyOxoCVp1qfl6R_dmIg-Btfxrc7Dxxgbv0i446N75ByPAA-mntxPNOAVOzYXIwGMhvwR-FsB-i0DTk-NQBwbu_Nb7tQSHt6YFQaorr1sBu7EiWdIAZVVvl_s9KBtpRWIzVl2hUA7_4mPozPIlK5hvXs4KwgdDkDkySUSmhJRFx8c7pIoUxafJVvhsHra1gWWLnqeg-L75NDjAYVFVQzMkkz3o7B3yNNagcWFZJwvirXbFH3e_NcOErdaGkEYxlKc3qAzd2gPgwHw1a93Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 179K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 23:22:49</div>
<hr>

<div class="tg-post" id="msg-76301">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVuaqMbyNwOmPIo7rMeTFYK5SfIeJduRIL2Nfp58sE8X0i7aRO35zDHhT1QLbcUtbWMImfbV_H8nwoVUZRaCkzgCx5q7CPqZe7BNlYfjSyUSf5FN70xLPx4jqVntJs58Q3UdCmGFaqczU_B7aBtA9NkpLdb7m4qM10b8DR1rgmX_snKErmBjxW4p3nv_M1RHHsodo-7er-8xeonmWcmuSMVwZNHMREbh52VnxDLMRZZ6idHo35yJdzzUbfTg1wJpek4SHRGy41Y22yw1XFdejqohlq0HdAxVkHIzYkKsENFpeK1KycM9J5QPrbcfCpvH1wW6dilLoBTCVRcyHZD4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/funhiphop/76301" target="_blank">📅 23:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLLMwdOp622uO9kopY8oPWYEZQe_gYe2uN9acHDoyZbuFnXi9KZSiuKvUepgwtAIFot0EREl6UKWsUqErxLpaH4VEjWABcCF30NyXG4l2zEnyqQQICgUQyGzF9nXBxWt13ifB6KYUh62UuWfhWIY2_6XegTy9N5E2FYmNZvK8F6kc7lKJ86OrU3gdlboBuMw5pwbdGGhDdkzNDhqcWThyqqzu6r5DKpAulrKklwB-CGxVwMc6yaEA_hQYe5j3Jp9VeSASZyGpYOVtHClrhe1E9_dShOLraZohDoJsA-Gp47dMEnWrUU9fYQQGnTVWGdH0pFcADEH5xEr_83YciVI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکش شبیه شوالیه هاس</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/76300" target="_blank">📅 23:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUKRd5FDHuMqAhlRTKLFyFpDPfBhauzhEbVd8nRsKupABP7qMI4-GOeCT7MS60VMsWpVEek6b6vYCEJ4WGdCFRWyjzXsiCVm8EuHpZdSx_UvLKraXSC4rbi93_2mO-1aKHWPQQW98cr48jY7st8S2C33mc26GNoHXXCevWckzONNEj2-qYT4PAU6AL_XTgRceemy5XEfpuJskbA1DmVbZd_BerlBNu1ONFp0Ok3awXCu6ZKddRyZo45AZcTV4DTyREWuH9E_PNS6MntIwgL1pXk_Uh89242VbX7vwOi8Bed9OKy-78slJeyyF1Hewq5Yu269xJEPjjjnFBUcU-QfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس قدیمی گوردون با لیونل مسی
یادش بخیر</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/76299" target="_blank">📅 23:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">از گوردون پرسیدن تو که انگلیسی هستی چطوری اسپانیایی بلدی، گفته چون از بچگی میخواستم بیام بارسا یاد گرفتم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/76298" target="_blank">📅 23:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پست جدید کاخ سفید: اونا بین ما راه میرن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/76297" target="_blank">📅 22:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=rLd67zUyUthFgA5td6spwk_U2ndgqrADy1BVVTl3SLQuhd8eKUuj3_yUMmgYaNoQg1HxWPYFN5Yk7X9qdIMNTfFWpm45Ijd7i9c4wDJke55epRZN0PG8msT6lmELhJHfTZ8RmYu1a0dpDbNXJ3Qi6umuvcdoLq3MVCS9b_O24QCl1I7p1s1NjF3RLslM5rh1Z2edHixh85gxfJ4JQ7W3rAQNdCla88CQ8TnM9Qw4W8mU0v4i5MsdtDh2QUoDignS6Kqa_f-0T6ciaQDKmr_r05yhhGb0ydrtZUCqNXIch2zZ5camEdSMuPrIflKKzgCgS7O-uA9sX9GYAntv49z76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95e3a0cee.mp4?token=rLd67zUyUthFgA5td6spwk_U2ndgqrADy1BVVTl3SLQuhd8eKUuj3_yUMmgYaNoQg1HxWPYFN5Yk7X9qdIMNTfFWpm45Ijd7i9c4wDJke55epRZN0PG8msT6lmELhJHfTZ8RmYu1a0dpDbNXJ3Qi6umuvcdoLq3MVCS9b_O24QCl1I7p1s1NjF3RLslM5rh1Z2edHixh85gxfJ4JQ7W3rAQNdCla88CQ8TnM9Qw4W8mU0v4i5MsdtDh2QUoDignS6Kqa_f-0T6ciaQDKmr_r05yhhGb0ydrtZUCqNXIch2zZ5camEdSMuPrIflKKzgCgS7O-uA9sX9GYAntv49z76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید کاخ سفید
:
اونا بین ما راه میرن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/76296" target="_blank">📅 22:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ تو پستش گفت تصمیم نهایی درمورد توافق و برداشتن محاصره رو تو جلسه امروز می‌گیرم.
الان نیویورک تایمز گزارش داد:
ترامپ حدود دو ساعت در اتاق وضعیت جلسه برگزار کرد اما هیچ تصمیمی درباره توافق با ایران نگرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/76295" target="_blank">📅 22:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سلام وحید جان قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود  @FunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/funhiphop/76294" target="_blank">📅 22:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=gecGtB8Bg9I-iT3OBtUDSKuKXZXXaj2bGhmxj560Aqkf2exAnQG9sBfP-nof8ARByUTUE3UDi0D7DOEI8w_XzbEzwTFl1pKhAsxdNhcbG06fhda8ckFZgMjsVWkj_btuOB_xjc6v-jv5lzXIDnuN533Is8PtjxbRWXFejtWACKLcNpY0NC_GBprhB7TJJLcq-a3u4lwtkWtGnyS5boYhxQjRp3iW4Pun6XcWEfLtYnMfBO80sgVr6GWmdYtvzB1J9ILamkBbtTYV2QT_ZlODd7TW86zETFx_JZKS0Oomajm8TLIid8u3quCAXs9XshjlvgZHUdC_GsEp-V0l4cy4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158dd2ae98.mp4?token=gecGtB8Bg9I-iT3OBtUDSKuKXZXXaj2bGhmxj560Aqkf2exAnQG9sBfP-nof8ARByUTUE3UDi0D7DOEI8w_XzbEzwTFl1pKhAsxdNhcbG06fhda8ckFZgMjsVWkj_btuOB_xjc6v-jv5lzXIDnuN533Is8PtjxbRWXFejtWACKLcNpY0NC_GBprhB7TJJLcq-a3u4lwtkWtGnyS5boYhxQjRp3iW4Pun6XcWEfLtYnMfBO80sgVr6GWmdYtvzB1J9ILamkBbtTYV2QT_ZlODd7TW86zETFx_JZKS0Oomajm8TLIid8u3quCAXs9XshjlvgZHUdC_GsEp-V0l4cy4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/76293" target="_blank">📅 21:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سلام وحید جان
قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد
پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/76292" target="_blank">📅 21:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اگه نمیاید بگید باغ و بیم و فدایی پست کنیم اینو  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/76291" target="_blank">📅 21:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr9pAsucseWooCcSwnDoywvuGAGghB5UBl5ZvU3iOQYxOIKP8L0bgewVqxCs2CG8tFIW9uVAPYcrzz9YD65V4sE4bkfYrFNbv05qVXf_NlUk8I57yfiwCQz4JAduE7ZIGlv-OMK0MBVOlWhmWeGQDmgWQJHpTT-H2LHEiOBmaKsjvQ2DcImKhffC1PzCJlO5FK4Ieo3qMt30uqmt7sqUoy2CCGBmWKGiWASLBieXwhtpmNpnGlb1qdangSks4ZSUaX2eIrKv8reBVpQvRpD27ti7H77Kpy2_Alx0pfL9sX7Ch001FrOPpGYd0bYLAvg5Wa73UHh8LrA3LEBg2MEcXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نمیاید بگید باغ و بیم و فدایی پست کنیم اینو
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/76290" target="_blank">📅 21:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هیشکی خایه نداره موزیکای اصلیشو بندازه بالا، همه دارن هرچی موزیک کصشر که رو دستشون مونده رو میدن بیرون مارکت زنده شه بعد شروع کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/76289" target="_blank">📅 21:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تا حالا شده در پی پیدا کردن یه پورن استار خوب ساعت‌ها سایت های فیلم سوپرو جابجا کنی و اینترنتتو بگا بدی؟ یه چنل داشته باش که اطلاعاتتو در زمینه پورن‌استار ها ببره بالا تا بتونی یه جق باکیفیت بزنی :)))
👇🏻
•
@PornHubCom</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/76286" target="_blank">📅 21:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام بیدارید؟</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/76285" target="_blank">📅 21:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpFL1a19OZiIprDwz6D2P4mzhHX5twNheXZ7-IRNkb5ScRK59RBujeEy8THpkfpLe6gOhMzU5aCwZfEgmuWCrrqeBGDFC4FAhbrJ7Tw_VcgT9l-Rjx-7v_k3CTPhoxOOZW7ONr6UujmJTlBh76lr7GoHc85PJyzWyzw2GCR6sCe-UE000UvSrtmSsmAOFi8NhBmSZxpAJVA-r_78M3peUEAKtCziYUNtADBqOcQDIRgIXZUux-23g2TYiBfTwfGQnmM1EFrz-5bwmQkDD_ex9C1SSZptQM1d8jppYkIkxQUi0WjWRTJtdHT5IgWgEqIxSOlG8TxK436IIIDZ07_Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشن خنده دار
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/funhiphop/76284" target="_blank">📅 20:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تیم ملی جمهوری اسلامی از تیم قدرتمند گامبیا گل خورده   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/76282" target="_blank">📅 20:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرگزاری مهر به نقل از یک منبع بسیار دقیق و بلند پایه درمورد پست ترامپ:
هنوز اختلافاتی در مذاکرات وجود دارد و ترامپ آرزوهای خود را بیان کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/76281" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تیم ملی جمهوری اسلامی از تیم قدرتمند گامبیا گل خورده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76280" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tcNZnY3VV6D4fcNe2gMo-nJaejJK6fIJyMucsW4cCGlrUsPEHAxIKhExB0oGEuJtvMqtpi7iGo7eSDQVp1IYtBS7yk2EUSGDs_EJ7CKjqRLHBQYlMRo8ZW9y2iRYm7Muw_FQ2_szHNoRFkdrvi_9LMiAS541q9OSYJTpboMoh1blEWpN-mt7q3y5lvCYbOW_PMsnMKz_fZ9UYr-8uD73dNYmWWawkzB3FlDJyJzvMNl83rbhxrERvM6-tvcJFSt3qz0oh_Y9K7A_0hAeKoFA0PAnxE281YypAExpqRYu5pza907QPyJldNjCxnJKx-FY-J5qiTXEl4Bd3Fe9hPF5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfKX8ENdybU3TL0YSrMkWZXpXlZmQHWh256IEk529RE2P_lXz3kESBpfWvnQDYMRJ67itvyTd6texYEmHw3IDfeIZ9D2Q7ZvxI6WU6vouQToq0iKeytAhLhLqF41AUU1uDTZu8j8xXQXainGxUHyIsTrndrNLvhnHNRPH1_ewJ92LPdk2gL-38finc3bC99uUzeTR-IoQd0fsxbD-qmRrlVNpewhHsSgy7Fa3KOCy7Vm2-rHIf6KzFAvV3dLDb39mWYHJPIo6dgJ4l55wrVf-zQQFkktZip8DcOCnv9eB2Ku-BETULRC4xx080RNxgt_RsSbIjfdyr1JVuVukPAx3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه اتلتیکو مادرید : بفرمایید! ما همین الان ایمیل پیشنهاد انتقال‌مون رو برای بارسلونا فرستادیم :  4 تا بلیت کنسرت بد بانی برای فردا اشتراک یک‌ساله روزنامه ABC 1 بسته تخمه! الان هم با اشتیاق منتظر جواب بارسا هستیم تا ویدیوی معارفه انتقال رو آماده کنیم. …</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76277" target="_blank">📅 19:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRycxP4sGN6XSeqEB80C8Hnsl0adDSLPhgeaaZ63E-b6a_q47Mt65tnU1jPg9XnP8PVXZr_fL4ZXXBjNG1I09_OrIpayZW9jOzufO2e4QWK5xnicsuQ5qGI60-x_PJ8pd4eCjAGThsHo6G6vguttPLY-mmB4aFKdy8BThz0h1OrIa0_zb3Xib0v-laiWozrewT1eBu8YUXAs3hDVAzpf7-AuZ8ZFRvU9pe0eRWsMP1a0J5B96sfd2zb-uLkioEQAlcb3XtiivPA9L-1u0660C_NUqNN9K2iHmQLzl2Rroz-kSdH_zOwGSIZ9Hjhp-LnwORD3yj8zBvjn6xQYltMqxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه اتلتیکو مادرید :
بفرمایید! ما همین الان ایمیل پیشنهاد انتقال‌مون رو برای بارسلونا فرستادیم :
4 تا بلیت کنسرت بد بانی برای فردا
اشتراک یک‌ساله روزنامه ABC
1 بسته تخمه!
الان هم با اشتیاق منتظر جواب بارسا هستیم تا ویدیوی معارفه انتقال رو آماده کنیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/76276" target="_blank">📅 19:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">غیر منتظرانه ترین اتفاق ممکنننن
فارس و تسنیم:
منابع آگاه جدیدترین ادعاهای ترامپ را رد کردند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/76275" target="_blank">📅 19:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حرفای مانوک خدابخشیان رو گوش کردید؟</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76274" target="_blank">📅 18:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حیف از خون هایی که ریخته شد و خانواده هایی که تا آخر عمرشون باید با این داغ بزرگ زندگی کنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76273" target="_blank">📅 18:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76271">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کل هدف ترامپ کبریت بی خطر کردن جمهوری اسلامی بود که به هدفش رسید و تموم شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76271" target="_blank">📅 18:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76270">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: توافق انجام شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76270" target="_blank">📅 18:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76269">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
محاصره دریایی ایران از همین حالا برداشته خواهد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76269" target="_blank">📅 18:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76268">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: با همکاری چین و امارات اورانیوم های ایرانو منهدم میکنیم و هیچ پولی هم بهشون نمیدم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76268" target="_blank">📅 18:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76267">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رسایی با اینکاراش میخاد بگه من طرف حکومت نیستم درحالی که نمیدونه روزای آخر عمرش رو داره سپری میکنه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76267" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خوش چشم، کارشناس ارشد صدا و سیما: ایندفعه دیگه جنگی نمیشه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76265" target="_blank">📅 18:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twWwndvHnbmqJWgfhtzyUPBKF-ISo7xKfPULudN1lk8dZio44NoS9ib8mbnyF0Qo3kGl3lm_wcA3ZMkAItbEBBcS40wzqhot0u3SglIi4CZTz0d7EiyUyyRHigocvZy669OMci6gPLF-tfIhHBWzFOb6MCiC7RU1RYq3T02QyBPbpoCUP8NEUF6s2r1VoIdI3JieuTeWbSvMHtLBKTvss3K7wuRrCdoVTEPDP01Aq6x_o5nHijh-Uti-UjV_dAMN4ePhfN5nXA8XxCdofC_bluR85petV7Hj6Eh83L68UzmUr5E4hxh3gbTAwB2G7iH6MBfdi4Wp_i5EUz5ZMfECkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی مواد میزد تو وحشی واقعی بود پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76264" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Xe6ImMXv3u_cIlREnD8WMN5X5WYwb_ApwwnhZAslOzPo5DPzsmvXXN9E1VaybkbOm_vKxX-kRlg1PQpAy_M9sTh_pWzcZPCD6qElozorZ-mFgNPtWYz16LF0ybyZadNlEy_oe31b00aiQuKk4qkXCxibFoOWBMcSEdFxrSX1JxcoDzmcT2MNprNqHBwj_vsshLL4lMxUgngfXI2riaHA1P8a3r-oJVPHZlgkv9fJEozDVusvt6kXYo9frS2F7kz1ZfH4xzG0h2sY4YeJDFlWnTGN723BiJVetPS5slI4o5E7s5xXGVee0i3UMkchxS9Ljs3iMRlZouzChTLuDd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g8
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76263" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76261">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به شخصه حاضرم ۵ بار ترک تیجی و ۳ دقیقه از ترک باغ یاس رو گوش بدم ولی ترک پیشرو رو پلی نکنم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/funhiphop/76261" target="_blank">📅 17:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76260">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عمان هم باید مثل همه رفتار کند و اینکار را نکند، وگرنه مجبوریم آن‌ها را منفجر کنیم.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76260" target="_blank">📅 17:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76259">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یجور میگید برگردیم بله انگار من از اول بله رفتم که برگردم
جمع نبندید بابا</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76259" target="_blank">📅 17:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">واقعا تلگرام ریده، میبندی بازش میکنی ۲۰ تا پیوی میپره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76256" target="_blank">📅 17:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اینارو خودش لیک کرد که کسی لیک نکنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76255" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76254">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قبلیو نمی‌فهمیدم چی میگه اینو میفهمم چی میگه و کصشره</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76254" target="_blank">📅 16:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76253">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وایستید یکی دیگه انداخت بالا</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76253" target="_blank">📅 16:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76252">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Demo
Amin Tijay _ Members Only
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76252" target="_blank">📅 16:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76249">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یکی تیجیو نجات بده</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76249" target="_blank">📅 16:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76248">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محسن رضایی: محاصره آمریکا رو می‌شکنیم؛ حالا چه با جنگ و چه با مذاکره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76248" target="_blank">📅 16:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76247">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر امور خارجه عمان: امروز با معاون رئیس‌جمهور جی‌دی ونس دیدار کردم و جزئیات مذاکرات جاری بین ایالات متحده و ایران و پیشرفت‌های حاصل شده تاکنون را به اشتراک گذاشتم. از مشارکت آن‌ها سپاسگزارم و منتظر پیشرفت‌های بیشتر و قاطع در روزهای آینده هستم. صلح در دسترس…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76247" target="_blank">📅 16:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76246">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0gP2lOi7StsABOqcmvnv2GkyyVA9uUKeX7wBPK1C_Ph7Uj84WnRYdweM4AKEb23-7b1anBew1UXLw22-4aSBCS785I9Ag5Xc5KHl5kx6k9wBn1DPeQiaTMFCYGH6s9pg_RfgyR36ANGY6s7eiNHIMg-vQtlN4izIcatRPZ0tC5-jiqSfak2tsiTRl_rZGeCFW2dIgvX5OXrVPlPxFfsW-01nFkqddWU1gPBtc9gPp2nlhwMYJaOmsBarvdqya6957pAXXNWa1i-JQvmKD0aJ4g1HsPRxEEUaIuUMUO7jGKCblVDvt7ZMCYzeuZgurtnAjggpZ3OM6_Zy6TtpWxYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه کاملا آماده مذاکره و امتیاز دادنه:
۱-ما امتیازات را نه با گفت وگو، بلکه با موشک‌‌ها می‌گیریم، در مذاکره فقط آن‌ها را تفهیم می‌کنیم.
۲-اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است. هیچ اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد.
۳-پیروز هر توافقی کسی است که از فردای آن، بهتر برای جنگ آماده شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76246" target="_blank">📅 16:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76245">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76245" target="_blank">📅 16:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76244">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟ هوش مصنوعی میگه برمیگرده  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76244" target="_blank">📅 16:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76243">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تا حالا شده گربتون فرار کنه برگرده؟
هوش مصنوعی میگه برمیگرده
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76243" target="_blank">📅 16:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بارسا هر خریدی که میکنه فناش فرمین و اولمو رو میندازن نیمکت، تهشم این دوتا از همشون بیشتر بازی میکنن</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76241" target="_blank">📅 15:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گرمه خوارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76240" target="_blank">📅 15:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObPfgWSHCHnizKRNGsHLKLJiP6JYw5cdGmzfdrMq5Kc0YwcQ4ZtOVDzmdd-sXObExOl-aCbxcPuTkeQFdd8HGRd6aHSEFqu9NaaqwdOARcf5lYX0DFvtfA9MmObA3ASFY4dsEVMji5Berv8pJoDv_UogAcdpVfBDw3A8Ya5Gr4pmvquh8QfC6vijWylYLq8F7JZZop8j9QHu8mV94sC70sniri5pwiir8s0u0GzF0Ud3wKOYGVx8Ma3qWt-x3OzzQ_R6Lqb-TP62VdxKC-Qq04MF9CHVLH4fzoMvGvM1d0Nc2w36N24Iw51Bk0X_SZKhOid75eYXjnNmTDv8TOSndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76239" target="_blank">📅 14:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76238">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده: مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم جدیدی در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده. شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76238" target="_blank">📅 14:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیویورک تایمز می‌گه توافق نزدیکه و آمریکا قراره ۳۰۰ میلیارد دلار بابت خسارت جنگ به ایران بده:
مقامات درگیر در مذاکرات می‌گویند پیش‌نویس یادداشت تفاهم
جدیدی
در حال بحث است که به تأیید هر دو طرف نزدیک‌تر شده.
شگفت‌انگیزترین مورد در طرح توافق صلح ایران، صندوق سرمایه‌گذاری پیشنهادی برای ایران است - که طبق گزارش‌ها حجمی معادل ۳۰۰ میلیارد دلار آمریکا دارد.
ایران در ابتدا این را به عنوان غرامت خسارات جنگ (که بین ۳۰۰ میلیارد تا ۱ تریلیون دلار آمریکا برآورد می‌شود) طبقه‌بندی کرد. طرف آمریکایی آن را به عنوان «صندوق سرمایه‌گذاری» بین‌المللی که به تسهیل آن کمک خواهد کرد، بازنامی کرده است - چارچوبی نرم‌تر که از کلمه غرامت اجتناب می‌کند.
به نظر می‌رسد این ایده از سوی استیو ویتکوف و جرد کوشنر مطرح شده است، کسانی که پیشنهاد دادند پروژه‌های املاک در تهران و مکانیزم سرمایه‌گذاری گسترده‌تر به عنوان مشوق‌هایی برای این معامله تقویت شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76237" target="_blank">📅 14:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76236">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مدیران اتلتیکو:
خولیان نخواهد رفت
مذاکره نخواهیم کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76236" target="_blank">📅 14:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ناتو: روسیه شب گذشته یه ساختمون تو رومانی رو هدف حمله قرار داده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76235" target="_blank">📅 13:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آه رسایی اینترنت و گرفته
هر لحظه داره ضعیف تر میشه
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76234" target="_blank">📅 13:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76233" target="_blank">📅 12:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzLe4dFCzhoAb9Bg1kMiYaLRPUmj9ipmsYnTvI9cqJP-9qMrhdDVKX_9LoV79tMBR80jUlSfMzYf9R1hFEeCpmIwswdSurrvP5UJmenWEL_MlHYmYlC7JbQorgFLWJ_Pb9vJSwbAPl0jLnlNt_hkanV4BIBL2emqTq_OB8B7KdDelM8v08GMtftSO3xOcV2hCKLbxpdnvgi0gH0_SNf6bb-ov6QqVEV5qVNVdvpMBwZzFNz6S5MeClGSn6Y2dx7W29YrWV4mouBKOU_zqO23qBG5by7H7lZMC3NjMpe24Z6idKpkpl0RVbNBYPuQ9W_XDfOwyw9pfKySIWxqlCkAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی آقا مجتبی رو به پسر نوح تشبیه کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76228" target="_blank">📅 11:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8334aba596.mp4?token=rEencnGDKZAG7pov0d8yKumUZeMaVSuFkMZQPiFxbsVfXM53XDGFDLzoj1yzMm9ta5GBEz4gLBtPYYoqNsVavbELqnwwnw73oSx4UwrXqqnb-mOy6jiKe4klq6fJmtqjT1LLx9XlgnATRKrsWba7ys7RUaYfCu2zX996M1mNuCd7E5EIsGt45zp_dy9FV9Ou9dmvU_UHykU1pzcwTkGY50sBBaRgzVr6a52kBn4pML0HHz09rPm5SKko1AUCyue1LFa6cT3xDcirmSFUebscyyvrYLN2m9Ipf9F3-wBG-n2Bn-JHlnPIdmXaXD7FZXItfMQY7-P-bEZPXGmSvl2Elg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8334aba596.mp4?token=rEencnGDKZAG7pov0d8yKumUZeMaVSuFkMZQPiFxbsVfXM53XDGFDLzoj1yzMm9ta5GBEz4gLBtPYYoqNsVavbELqnwwnw73oSx4UwrXqqnb-mOy6jiKe4klq6fJmtqjT1LLx9XlgnATRKrsWba7ys7RUaYfCu2zX996M1mNuCd7E5EIsGt45zp_dy9FV9Ou9dmvU_UHykU1pzcwTkGY50sBBaRgzVr6a52kBn4pML0HHz09rPm5SKko1AUCyue1LFa6cT3xDcirmSFUebscyyvrYLN2m9Ipf9F3-wBG-n2Bn-JHlnPIdmXaXD7FZXItfMQY7-P-bEZPXGmSvl2Elg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب ایران ۱۲ شب به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76227" target="_blank">📅 11:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چرا وقتی اینترنت وصل شد انگار قطع شدیم؟
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76226" target="_blank">📅 11:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3wdyz7oQZpJDXodRk3JUZgg9epY27uYmUh-p-eMFZCJs9XyC0dJRefh2f9dJ4PUBeX0Zys3Ir_OnylAR1B_JmKtvJL7dFj3ljPEWAwkk1DvhvF5qEHS2jzrZqbdHB9wXJDSat2yrLtlpDynxhSomAPOb1jlW2MVmBvKybLoEve5ZEm2wwpnf7nv41y3l4kfwxOY4_9ZmFegxFJQJMyphmuPUavgDV_ox3wZQwxdQq8m2C6sdrpu9Dux5UPRDhtfM1Rj_HJzXenEqwjDL6hU0YlBO-9m2oIbx6RiG-j036_jybkX5wX7kmKXjNioMWmF09rkJ0XFLPELlKaMu3euNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت کتاب پاور آف نگوشییشن، امروز به دلیل تخفیف، ۵ درصد افت قیمت و تجربه کرد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76225" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه  @funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76224" target="_blank">📅 10:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi8qVRcBFtHEsxv8RE92ib7UI7SB-fvqrsoL-XHGcdzlLwRW4k7EhhYX9DPvG9PodZPq2WpgdfoKQfeqt5rr0UDMMKiwXx-zgQqNfjwQ3NwkHgx2ZQphpeoAXWXJMVKg-EWsK3s0Z4BBBi-t29NlrxpK1296hHmIe3adEYfK8geYQR02-GtETGx0ppETPqeob-n_keeEZ36sNvDTzD33G0H7f_I6QmPyhSv98ijyGXAymHqwX9_UUZTRiBq3pTi4NzkTC_HC0J2ZSSqmUDWg4EXLwkQmqDgbsg69h0xUo_PLMb4mX8RIJCIAFw1WwLKTnnCEfZCmCFzNDj4yNrNx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک جنگ آمریکا و رژیم اسرائیل علیه ایران را تجاوزکارانه خواند و اون رو بشدت محکوم کرد، او تاکید کرد آمریکا هرچه سریعتر باید از این جنگ خارج بشه
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76223" target="_blank">📅 10:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhixyyaI1tw8D6lW4QdmJoJTOp94skGhYjIWo-AH4_D1r9hgNHL1t85I2UW9JDGnwb37LuBG4iZsyw09QH1kX63aBvt0jyBZbGR7ET0DO3t-2mztyS-RRrxKwIar0AbtwB9jHV29IcSchCZHcPAPQ2_oOPpsKVPXhYtCKiQlhpS8YgaYZEkHI9Hc-k4Ir_VAYdtO3n4x7NtTiftmGceqf2NELFqyElv77zs6-e1L6Tmw7J83ti2T2Jkfs5CU2_p213m_0wQpSwdSF34-1N_MFKZqGUtK7wWxeHyw0NgDW3sPeoJNV1bYMuZlH-ouzrf5z-5o3Qv_SCBa7iKVirBtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا افتاده دنبال گواردیول میخواد باهاش قراداد ببنده.
@funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76222" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76221" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwzM5RpsMAqjD1hgBPd-AfsC4NMAE5hSE0MYJ8Ya5cb4jjn19KcSi8jpKda-znCY1WH9y4HB7iyQUgWvDEqCY71iZ4SzOuKLK5oJpiEQBvUt3N9W06L7_Ry0WSx9hCmxkoIl7LbfGyuFh5o5bppuyOfTEhyhm_r1jnxXLOucarnrMfZJMfo4YtjuOVJBF9yfgz2h6MDIO2_6qzgMTH2jJ6PO4pMFn41332qseeDSlMXOYF5rsI8V1bYkKesQuGC8pdUVJApACh1_6_JcyIbjmfJEStPvAirVNp-yRzJ2jxtQdSYajybiF-oID5M-5Kq5KCsBInE3JqKPVTW5CSQyWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r8
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76220" target="_blank">📅 09:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سی‌ان‌ان:
حداقل 50 تونل دسترسی به شهرهای موشکی در ایران پس از حملات اسرائیل که آنها را مسدود کرده بود، پاکسازی و تعمیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76219" target="_blank">📅 09:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری مهر: هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76218" target="_blank">📅 02:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دکی واقن دکتره؟</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/76216" target="_blank">📅 01:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/76215" target="_blank">📅 01:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۹۰ روز از تـرور سید علی خامنه ای توسط اسرائیل و آمریکا گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/76214" target="_blank">📅 00:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76212">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/76212" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76211">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=ddH_FCuzba59rbtHZ1DTvzRKdEgr89HliKRmQQ4ujOYeWKyT8j6iBkvkuS1AtKfSEho0nSiyNdYa8sgz043gRrEONJ0gsezHEyBzR2nkZuyBb62bKXxYe6bzVzXizTY46Zw2EK-0Jx0tKYGCxMH4NzahbnyQL7TyouH7_0zt4hKA_ZJLkknbA_Wfbd9Cs9dbnkHTYl5spoqle0eGqYSOzY0CJYbTrt2h45iIitgRRc8sxMepF5SPjjTSmIyt-wsXtpVfYOyBQQ6GuDl1zL3bjC1nsffYJORTfzbli-D0xK08kZWFfwOP6Cslgj598ZTXJ3UXMWgCK7OoxGbPIGmYHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=ddH_FCuzba59rbtHZ1DTvzRKdEgr89HliKRmQQ4ujOYeWKyT8j6iBkvkuS1AtKfSEho0nSiyNdYa8sgz043gRrEONJ0gsezHEyBzR2nkZuyBb62bKXxYe6bzVzXizTY46Zw2EK-0Jx0tKYGCxMH4NzahbnyQL7TyouH7_0zt4hKA_ZJLkknbA_Wfbd9Cs9dbnkHTYl5spoqle0eGqYSOzY0CJYbTrt2h45iIitgRRc8sxMepF5SPjjTSmIyt-wsXtpVfYOyBQQ6GuDl1zL3bjC1nsffYJORTfzbli-D0xK08kZWFfwOP6Cslgj598ZTXJ3UXMWgCK7OoxGbPIGmYHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هنوز مطمئن نیستیما ولی فکر می‌کنیم یه پهپاد MQ9 دیگه از آمریکا رو امشب نابود کردیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/76211" target="_blank">📅 23:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76210">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی، منم همینطور  ولی دیگ بسه بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت. کانفیگای اختصاصی خودشونو هم میزارن  خودم تست کردم عالیه
👌🏾
🤌🏽
…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76210" target="_blank">📅 23:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76209">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">میدونم برای وصل شدن داری سرویس میشی،
منم همینطور
ولی دیگ بسه
بیاید یه چنل آوردم براتون سوپره کانفیگاش، کانفیگای رایگان میزاره که وصله
همه کانفیگاشونم از قبل تست میکنن رو همه اپراتور ها، خیالتون راحت.
کانفیگای اختصاصی خودشونو هم میزارن
خودم تست کردم عالیه
👌🏾
🤌🏽
اینم آدرسش
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404
👉🏽
📡
@VPNir404</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76209" target="_blank">📅 23:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امشب وحید جان خبر از چند انفجار مهیب و لانچ موشک تو جنوب کشور مخصوصا بندرعباس داد و تسنیم هم الان گفته به سمت ناوهای آمریکا و کشتی‌های تجاری‌ای می‌خواستن از تنگه رد شن چندتا موشک و پهپاد شلیک کردیم که خب چیز خاصی نیست خاورمیانه‌ست دیگه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76207" target="_blank">📅 23:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIoMoHcurnaDfW3gmVoY_EHx1rmeMne-kXwr8j0MGhiB39rF4JpeOTAEHWRve1aXTBd-_kcPvuc5xd8kYuYik7KTeOC2d63og2u4ooKURmtVflwn_QHqsepzEQZMkLjIVKjnMPjeaAr_GOJsAIP3T8-s5UJYe5W3gZJzLaBxA16kxeTdaO-73GZVtxFfyQ8z3eF35o8xAF2YSmRnHiT3Zu_R27cgRP6zuh-Vx9kaQSt8ZYpZEYlWV3N_6YCHg7ZCfIJ3QDD61Lp_KcRcIbhhtfnIZ0UXBhOzxVWRQEOWHkceBdXgRzKn3-nNRl-1MA4g5gQVPoFvlSuLE1k5eLkGhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه داداش بخدا من خوشحالم از این که اینترنت برگشته و مردم میتونن وصل شن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76206" target="_blank">📅 23:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این گروهو زدیم که فقط میشه موزیک فرستاد
بیاید موزیکاتونو ول بدید و ی پلی لیست خفن درست کنیم
(فقط میشه موزیک فرستاد نمیشه پیام داد)
@Hiphopiplaylist</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76205" target="_blank">📅 23:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیمار:
حتی اگه جام جهانی رو از دست بدم خیالم راحته چون برزیل وینیسیوس رو داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76204" target="_blank">📅 22:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzverVLt2Nq_910ILnuopf0727y98GQ4rXq7BP0diLVKytg9CE3b_sfU0ZAm198EbfkzKECjVDayLk9tB-yzJxmmgdVz9kjdxa2cFoppc2_vZoW2rnN6ETwNz98f9j3k9Ls-Xbv8hS1jRhBmFMi3ZDE42dpVRlYHbFJL7l99eHkZtkX1KR1RE7iAlFjyxaFI9YI962O8BQ91xSnSNAed7bbklMIdz8UQ3vE4diGPTKOkpy8CsXoJzgGHtwkBRnIqQGvakvsrjmcvD6bQduYQIBIbwcNIUcXombPrPBEAg3u95WP0xZ6DAK8nGi8-eZlwEdDZDQoSAYBk_gbopn0FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی انقد کصخلید یه توییتی رو باور میکنید حتی بدون این که به تاریخش نگاه کنید یا ادا در میارید
یا واقعا با این شوخی کصشر خندتون میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76203" target="_blank">📅 22:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیمار تو تمرینات برزیل مصدوم شده و معلوم نیست به جام جهانی میرسه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76202" target="_blank">📅 22:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76201">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76201" target="_blank">📅 21:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پرزیدنت پزشکیان:
ما مذاکرات را برای تحقیر و تسلیم انجام نمی‌دهیم، برای این انجام می‌دهیم که از اول هم گفته‌ایم که به دنبال داشتن سلاح هسته‌ای نیستیم.
ناآرامی‌ها در منطقه تقصیر اسرائیل است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76200" target="_blank">📅 20:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76198">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فرید رومانو:
برناردو سیلوا به بارسلونا
هیر وی گووووو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76198" target="_blank">📅 20:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76197">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">من کاری به این که ویناک قبلا چیکار کرده ندارم، ولی تمام این فشارا بهش سر موزیکاییه که داره میده و اینه که سر پرونده هاش بهشون باج نداده و زده بیرون از ایران
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76197" target="_blank">📅 20:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76195">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofhkavuhxLmYS3W6TEhJG4y93EO9k2MR6INyH7TYNLjpw1ztmaGBhaKuC0sMjbeYg7q9RB08J6-tLj8ArZXSycXrl-CP-3TliJy3IKFJwdkQUjGZ4KAVT4KkaiNd2lY_ppeWkELrgvamEKkeAe8q46U_wP8wfPyRxdXLSNDB7t8rrZzExobiT3CuvOw7JVDPFcbAc1AYDQsq3DiTCZhQR42zBSuD3Lp3aJguWQR2ChO112FmgtMjlpw2EzkuHqXkQGmeAvVlkkJjKVo_Lc0RyAGTpMn-Gar2QiKkQy4BSdnEfN32PV-VkXX9WgA3nXVsze7q4NxPoHSUb-IAgYUj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/76195" target="_blank">📅 20:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76194">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">امین منیجر سر کیری که ویناک بهشون زده و از ایران فرار کرده فشاری شده و داره میگه تو ایران بودی خایمالی مارو میکردی الان رفتی بیرون بهمون دیس میدی.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76194" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76193">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان من تازه آنلاین شدم، ترک هایی که سورنا و بهرام بخاطر اعتراضات و حمایت از شاهزاده دادن رو بفرستید گوش کنم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76193" target="_blank">📅 20:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76192">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل: تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است. اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76192" target="_blank">📅 19:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76191">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک دیپلمات ارشد اسرائیلی به شبکه ۱۴ اسرائیل:
تا جایی که می‌دانیم، این توافق توسط رئیس‌جمهور ترامپ یا مجتبی خامنه‌ای تأیید نشده است.
اگر توافقی وجود داشته باشد، در حال حاضر هنوز در سطوح پایین‌تر قرار دارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76191" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76190">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4aUprdIyW1mIiINkbne6qqG5eR41rKklbwycWv8Nl1zzYl3jGv6jheRJ6KrQ-CXyeAnmaSOhodfQm5gCJG80SlbYFmSOs3D91UW2cjJBWeRwxEAWZpPFsKd5w9QoMEq-vzIrpBN3VYadBtxN6YTz3t3WPpcc_SICVQXIuX5-5hR0MVoQ5AYeUi3DdOxMCddZLnjBkz67eHxQlCS_HvFAWQH7JgDMEMlOlwTpaHWdwCTAkUZzpxGGFnQRmdzD9ygAwhtXautK9LZsgFjNA0cxc_l0XcxsaDp1wgbud7RuU5JSEJ4NVMU8mqUqJlqeI_7sLNIZjjjON1iHhSKOYLTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76190" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76189">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76189" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76187">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل: مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76187" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری i24NEWS اسرائیل:
مجتبی خامنه‌ای، رهبر معظم ایران، یادداشت تفاهم با آمریکا را نپذیرفته است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76186" target="_blank">📅 18:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند. سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است. دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76185" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
ایالات متحده قصد دارد دسترسی خطوط هوایی ایران به حقوق فرود هواپیما، خدمات سوخت‌گیری و فروش بلیت را مسدود کند.
سازمان مدیریت تنگه هرمز که توسط سپاه پاسداران تاسیس شده، مضحک و خنده‌دار است.
دولت ایالات متحده هیچ تلاشی برای تحمیل سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
روزهای ترساندن منطقه و جهان توسط تهران به پایان رسیده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76184" target="_blank">📅 18:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آکسیوس: توافق در واقع همون سه‌شنبه به دست اومد؛ حالا فقط تأیید ترامپ باقی مونده تا همه‌چیز نهایی شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76183" target="_blank">📅 18:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واسم سواله سود این تفاهم نامه واسه ایران چیه دقیقا؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76182" target="_blank">📅 18:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جدی جدی حزب‌الله و مثل آب خوردن فروختن</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76181" target="_blank">📅 18:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76180" target="_blank">📅 18:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فوری از آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76179" target="_blank">📅 18:00 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
