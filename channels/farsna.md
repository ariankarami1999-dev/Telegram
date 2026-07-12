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
<img src="https://cdn4.telesco.pe/file/O_5R1VxoJwHHpPyHiBZWQwDdYeiB6LkgetkJemPDZNoPmJ06JefkeicR0BqDiBOHhPeOIXeeUSTA24k4FzPM5nd7i7UBuvh3b_G1U59QTl0HVMpXQ2_P5QCVM-7O-d9q4miWJ9qTMH0aYMbnXYuF5HkXOQIFqX0N_-_0M68x04WiC9ufbxnZXDk5GPUePC5sDbUyB2RlcNraWOvvIcG3h2wDdkBU41Ph0u6Ymj2UUAS5tONxBTUlojpJhrrda84V1JhKycXBnAQFkwG5gu9521uNOv2t02rycHZS0ARoV0IIoPcSXqBb6bxhPDxDMldsgbehpn0XbAhTizpj7avnnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-449342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/449342" target="_blank">📅 08:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اصابت پرتابهٔ دشمن به ویسیان در لرستان
🔹
استانداری لرستان از حملهٔ هوایی صبح امروز دشمن آمریکایی-صهیونی به ویسیان، از توابع شهرستان چگنی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/449341" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20121c07f8.mp4?token=uim--37sPE1aV-C_Gbhm2C810RX4YY8jvyBX8eb1V5J7JgeusBmXGaDC4C5gNIgjcrHf78vmm6sS-iArMHMXz49y-d1A_-A74Be-T80p-HjETx4RRXbZkXEfULXrpLZExAQbUvTk2iSh50_8KGjkjb6FcvmrfHHwl3vgaN5rFTSVOnz8CChpWIzoxTCMi8Y1afzp0WUt3n6Y3ncm1fBtWND8I5-DVg7chN7MAgjDlI-5yyYFTzk5TFJ64X78N9uhBsOPRv62YMvyasEKZewx-3JhskkCc-LNVflUZMZ5De3a25QV3goOCw1n1Qj8coTdfiFvgGFG6u2zY3XSB6QIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
وزارت کشور بحرین: آژیرهای خطر به‌صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/449340" target="_blank">📅 08:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/449339" target="_blank">📅 08:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
سخنگوی ارتش: آمریکایی‌ها باید از مفاد تفاهمنامه تمکین کنند
🔹
امیر سرتیپ اکرمی‌نیا: مداخلات آمریکا برای ایجاد مسیر غیرقانونی در جنوب تنگۀ هرمز باعث ناامنی شده است.
🔹
ما موظفیم برای تأمین امنیت منطقه و تأمین امنیت عبورومرور کشتی‌ها تلاش کنیم.
🔹
نیروهای مسلح مقتدرانه از حقوق مردم ایران در تنگۀ هرمز دفاع می‌کنند.
🔹
بانک اهداف نیروهای مسلح دائما درحال بروزرسانی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/449337" target="_blank">📅 08:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
منابع خبری از حملات جدید علیه بحرین گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/449336" target="_blank">📅 08:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8QN1oWo8S8mmXso3uYRXbE6GZHKVucuabI04t7-0sByKpVca9ctTUm8jWscLMtrQA2p7mABn0TYa70NPx4dBRGLLE1RXUh2g_xZ2LQhn6fRK4rxW72hn33SiD2HzO26VgfPdi8RxZuFa2lSH3p3QXxW8Ljd3b1ewtA93qJ3dCoIsiY-Y-pFYt54iuUJeoyOSNPcmHu5TAMfOKlR27ATVaiwPi8y6Sv14GWbtINintHDjlkhgIX2sKR-BkIY6iSxF67UmgcFrnuPUefHMrSCiAz375Kwmy90WHn2x8uK3dd4tfWxe_gulItJOo0p7cjxZs2fVK9dLvD-P35UMM_UZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بلند شدن دود از پایگاه دریایی آمریکا در بحرین، در پی حملات ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/449335" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449334">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
وزارت کشور قطر از ادامه‌دار بودن حملات موشکی خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/449334" target="_blank">📅 08:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449333">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار مجدد در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/449333" target="_blank">📅 08:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449332">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE-BCY_y11UCut-v53QS1keBV8rBj5-oGNqijT65OPYT1yGLU_x20J4El5BqmC-gU8oAfCTc2XZhFK7HnZGPvclMiyr4OIQighxW2Bv2QIjkGjTCa5PwR34UzUCfJ1ZNU2byjU5p3wjhXwDUhNj97hCNRJezcYqHXKEth8vUNK4cHrDI6BLFuJmeBli7AH5PDbGFulnbtATPSe_dHDFy-OEJEML5lcBc2Y91M5y1FfAlgFtU5EcoOWa_MR0qW3VNEi_pwq3_Ral_PjFG0ZbSWLS82jIF_qaCFRMzmYmHdBaBW1HLIw5kuiUVs7nCYwMnumGwW0EutqcnX1xKEj8nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم به قول و تعهداتتان عمل کنید وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبه‌رو شوید
.
🔸
همچنین او بخشی از بند پنجم تفاهمنامۀ ۱۴ بندی را که در آن بر بازگشایی تنگهٔ هرمز با رعایت «ترتیبات ایرانی» تاکید شده است، در ضمیمۀ توییت خود منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/449332" target="_blank">📅 08:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/449331" target="_blank">📅 07:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/449330" target="_blank">📅 07:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
آژیرهای هشدار در کویت به صدا درآمدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/449329" target="_blank">📅 07:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449328" target="_blank">📅 07:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چندین انفجار پی‌درپی در قطر
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/449327" target="_blank">📅 07:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
منابع خبری از شلیک موشک به سمت ناوهای آمریکایی در دریای عمان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449326" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
منابع خبری از شنیده‌شدن صدای انفجار در قطر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449325" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWhYM8yzYYBfJgDtQGw68dAng0nXmwxAcOiv0ayyNqabVETlyL2jLrWjp2SEFIoZTI7UgBmGaan9yIMLrSzvFEFfPteqKpe2rTk0cVK62qndpUjQKMMaidnw-4JPMnNBTKbtT2I3yPqW7lvdp1WdDrkP1oTQEJo2XSHHQsiSyFES5BxiRtNXAW_Zzvb6shnDVE62z8ltVCb4vhW1ysWCSy9-CojZRch0LR_z6AALIeHBZ65nAIg3dZqVxCbgesi-aubWbUBGHyags7mCcsIwHV67mseptIfXVf1OtccQ9MLQ8MS7HCoUu-FBcU50ulRjKf5-vTZFYRWgkHKRSQlSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با عبور از سوئیس به نیمه‌نهایی رسید
⚽️
آرژانتین ۳ - ۱ سوئیس
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449324" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
سپاه: دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز فرماندهی نگهداری جنگنده‌ها در هم کوبیده شد
🔹
در پاسخ به ادامۀ تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگۀ هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحلۀ دوم عملیات مقابله به‌مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های مرکز فرماندهی این پادگان درهم کوبیده شد.
🔹
دشمن آمریکایی-صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت. بجنگ تا بجنگیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449323" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be502e4e4.mp4?token=VtvejXhfypa5djMZX_aruq76Etw_DtVi7UtdtegdjtzuPXoPHHIJin1AN_wirJTlQr807i7Oyo4D8Ldwr498Hc5YSs90C8OVdMvRGKza_jzY3sqsmlqivboLbmtW9O_5RVWtjI7OPKkuz8rEOQIpJr4g6BFPHQRkZQOu4rBB1g2XrvUqCaAw0X4mWr7ypc-KwS9bmIBUySfEjbjsve5OvRg1P7qPIs1XTJsXnmdlbQT2HuyKeUduV61UTm_-CkpQShWK9bua7E4JF5OLxRd4M7ydErEY_P0a412lZ0wda_U9n2G1eTR2sC8quLAFxjVRajKFc7eUPFkvi970tttkmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be502e4e4.mp4?token=VtvejXhfypa5djMZX_aruq76Etw_DtVi7UtdtegdjtzuPXoPHHIJin1AN_wirJTlQr807i7Oyo4D8Ldwr498Hc5YSs90C8OVdMvRGKza_jzY3sqsmlqivboLbmtW9O_5RVWtjI7OPKkuz8rEOQIpJr4g6BFPHQRkZQOu4rBB1g2XrvUqCaAw0X4mWr7ypc-KwS9bmIBUySfEjbjsve5OvRg1P7qPIs1XTJsXnmdlbQT2HuyKeUduV61UTm_-CkpQShWK9bua7E4JF5OLxRd4M7ydErEY_P0a412lZ0wda_U9n2G1eTR2sC8quLAFxjVRajKFc7eUPFkvi970tttkmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449322" target="_blank">📅 07:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f88fbf80.mp4?token=IYILEE8fiy1Im972YQCQFVwDZibVB2fLtnk3jQ7LfUWdyZOeOJkzduVjGwiIZyjsHIZNZpWjrb6DVg46H5jsyERBEOyPX67LwlnLxHhKU_7vkcw-q0tJXA1VQKHqyW5X4acM1cDFJtCooVXhGMj5epVJ1WHs55CnsMNzmjVdOhfBC4P9Anzf7sDK3xxghu47zCovN9y1n97uE0OXu-JlhVRyIsE1Fahl3PjIK7eoPGnHzJh9PXHwomLO5LPk3qnKPXwX-VG82W93ihyVZhfooo0sbZrZubmqZN_j1e8hhggod1mMhxxNG71OqjoQLS2QpmRGmoXO_HnbaKrjgbTEyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f88fbf80.mp4?token=IYILEE8fiy1Im972YQCQFVwDZibVB2fLtnk3jQ7LfUWdyZOeOJkzduVjGwiIZyjsHIZNZpWjrb6DVg46H5jsyERBEOyPX67LwlnLxHhKU_7vkcw-q0tJXA1VQKHqyW5X4acM1cDFJtCooVXhGMj5epVJ1WHs55CnsMNzmjVdOhfBC4P9Anzf7sDK3xxghu47zCovN9y1n97uE0OXu-JlhVRyIsE1Fahl3PjIK7eoPGnHzJh9PXHwomLO5LPk3qnKPXwX-VG82W93ihyVZhfooo0sbZrZubmqZN_j1e8hhggod1mMhxxNG71OqjoQLS2QpmRGmoXO_HnbaKrjgbTEyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
وقوع انفجارهای دوباره در بحرین
🔹
منابع خبری گزارش دادند که مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف اصابت موفق حملۀ هوایی ایران قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449321" target="_blank">📅 06:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
وقوع انفجارهای دوباره در بحرین
🔹
منابع خبری گزارش دادند که مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف اصابت موفق حملۀ هوایی ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449320" target="_blank">📅 06:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d674470e9c.mp4?token=mzItUD4qsvcr6Zw5NUYYOaR6tzZ5aReiBrnW1qpcw1nyDSffVYY8yJz7ktg6SghyIcqoZ2v2JiMZZIISyFrGAZtMaqdjOfYKKnsEcseZOFQtWLjp7FVZHZGeeqM07HbEJ7O_LGB107su_MyZTL5mEOgS2MwLBTLyuftvv45UljfUABL2jyUjN6OaJOW52M4QLT4_91EGobquLwrOqOLwa3vEst7NSqY9VlARleubphZQbDV1nw2wqo3z1gLEr0q9AE6QvjUTro3MPy2ynyiEbnumswQ_27C1MKiq2k5pJO1gCRg6YK-xoIcw3gqfC9FADW7PRmW68lp9oK5ZQFhCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d674470e9c.mp4?token=mzItUD4qsvcr6Zw5NUYYOaR6tzZ5aReiBrnW1qpcw1nyDSffVYY8yJz7ktg6SghyIcqoZ2v2JiMZZIISyFrGAZtMaqdjOfYKKnsEcseZOFQtWLjp7FVZHZGeeqM07HbEJ7O_LGB107su_MyZTL5mEOgS2MwLBTLyuftvv45UljfUABL2jyUjN6OaJOW52M4QLT4_91EGobquLwrOqOLwa3vEst7NSqY9VlARleubphZQbDV1nw2wqo3z1gLEr0q9AE6QvjUTro3MPy2ynyiEbnumswQ_27C1MKiq2k5pJO1gCRg6YK-xoIcw3gqfC9FADW7PRmW68lp9oK5ZQFhCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449319" target="_blank">📅 06:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس‌حسن اردن منهدم شد
🔹
اطلاعیۀ سپاه: رژیم جنایتکار آمریکا با تحمیل ارادۀ خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی‌آزماید و با تحریک چند شناور، مسیر غیرقانونی در جنوب تنگۀ هرمز ایجاد کند، که با پاسخ قاطع نیروی دریایی متوقف شد.
🔹
ارتش کودک‌کش آمریکا برای جبران این شکست دست به حملۀ هوایی علیه تعدادی از پایگاه‌های ساحلی و دکل‌های مخابراتی در سواحل جنوبی زد. همانطور که وعده داده بودیم بلافاصله پاسخ کوبند۸ تجاوز خود را دریافت کرد.
🔹
رزمندگان غیور هوافضای سپاه پایگاه‌های نظامی آمریکا را هدف قرار دادند. در مرحلۀ اول این پاسخ زیرساخت‌ها و تاسیسات مهم نظامی در پایگاه هوایی پرنس حسن اردن را هدف قرار دادند و مرکز فرماندهی و کنترل این پایگاه و آشیانه‌های پهپادهای MQ9 را با چند فروند موشک بالستیک در هم کوبیدند.
🔹
ادامۀ تجاوز آمریکای عهدشکن پاسخ های شدیدتر را به دنبال خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449318" target="_blank">📅 06:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449317" target="_blank">📅 06:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">قطر هشدار امنیتی صادر کرد
🔹
وزارت کشور قطر اعلام کرد: سطح تهدید امنیتی هم اکنون بالا است و همه شهروندان باید در خانه‌ها و مناطق امن باقی بمانند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449316" target="_blank">📅 06:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
منابع عربی: انفجارهای متعدد در پایگاه‌های نظامی آمریکایی امارات و قطر همچنان ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449315" target="_blank">📅 06:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449314">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
صدای انفجار در قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449314" target="_blank">📅 06:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
صدای انفجار در کویت
🔹
منابع عربی از شنیده‌شدن صدای دو انفجار در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449312" target="_blank">📅 06:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌ وزارت کشور امارات: پدافند هوایی در حال مقابله با تهدیدات موشکی است.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449311" target="_blank">📅 06:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
گزارش‌های از وقوع انفجار در امارات   منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در امارات خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449310" target="_blank">📅 06:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
صدای انفجار در قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449309" target="_blank">📅 06:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
گزارش‌های از وقوع انفجار در امارات
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در امارات خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449308" target="_blank">📅 06:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449307" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
صدای انفجار در کویت
🔹
منابع عربی از شنیده‌شدن صدای دو انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449306" target="_blank">📅 05:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449305" target="_blank">📅 05:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
برخی منابع از فعال شدن سامانه‌های پدافند هوایی در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449304" target="_blank">📅 05:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
معاون استانداری خوزستان از اصابت پرتابه‌های دشمن به مناطقی از استان خبر داد
🔹
تا این لحظه شهرستان‌های هندیجان، ماهشهر و آبادان مورد اصابت پرتابه‌های دشمن قرار گرفته‌اند.
🔹
تیم‌های امدادی و کارشناسی در حال ارزیابی ابعاد حادثه هستند و اخبار تکمیلی پیرامون جزئیات این حملات، میزان خسارت‌های مادی و آمار مجروحین احتمالی، متعاقباً و پس از جمع‌بندی دقیق به اطلاع عموم خواهد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449303" target="_blank">📅 05:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355a926ad4.mp4?token=BZn-f_pPgDoHDLBcFAbRswxzKI4AWDsIEydwevq8Kkuyo5L1UmjD4gnj7wXO-ASvCYTFHg9os0q5Q2UZLT5HPecJaqKcdASFXs7g9hGzaqzj6UFzDwii2j9DkdSqDIH9d0HbBiZ4dGBwv69aYoRmpV0HT9dIxEbmPrLTrC1Rm8wczAiHk2AmooqR4ia9jcQ08QeoZT-ZKsgl6znRxASRJYKAqYv2msaba8Kvu83VTEYtqsE7h1WeMfB4UB4_Rnp-Noe8alboB6z1sPo5zFQRqYYQa9qi7a3QH34oQmMDz7V4bGbPtlh58SpuFIpAvZ2RWWKg5t1Y3Y3TMyBdjV_obQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355a926ad4.mp4?token=BZn-f_pPgDoHDLBcFAbRswxzKI4AWDsIEydwevq8Kkuyo5L1UmjD4gnj7wXO-ASvCYTFHg9os0q5Q2UZLT5HPecJaqKcdASFXs7g9hGzaqzj6UFzDwii2j9DkdSqDIH9d0HbBiZ4dGBwv69aYoRmpV0HT9dIxEbmPrLTrC1Rm8wczAiHk2AmooqR4ia9jcQ08QeoZT-ZKsgl6znRxASRJYKAqYv2msaba8Kvu83VTEYtqsE7h1WeMfB4UB4_Rnp-Noe8alboB6z1sPo5zFQRqYYQa9qi7a3QH34oQmMDz7V4bGbPtlh58SpuFIpAvZ2RWWKg5t1Y3Y3TMyBdjV_obQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پول و مقام لایق هدف‌شدن برای زندگی نیستند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/449302" target="_blank">📅 04:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در جاسک
🔹
دقایقی پیش مردم جاسک صدای چند انفجار شنیدند، که منشأ آن هنوز مشخص نیست.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449301" target="_blank">📅 04:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
معاون سیاسی امنیتی استاندار بوشهر: در حملات دشمن تروریستی امریکایی-صهیونی به شهرهای استان بوشهر شامل شهرهای بوشهر، عسلویه و دیر تاکنون گزارشی مبنی بر مجروحیت و شهادت مخابره نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449300" target="_blank">📅 04:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126027adfd.mp4?token=b_D8QsT95QgNgAFFBeCFvy1O7jXU71tBF2T7ijmiTbtQPbNVHZFeQSlvWLwLHZFQuV0l01d74HMfgw9k_YyLrsBArL84SZpKpDBwBZsmFRcy8nkI0V1jvR9JuuwYdVWXGEnZBTrdAGNu-6CJNEWgxwhqsu2PhD1NcqOw4XfZeqN2wQB7r8w890qm_4veDAyuNf2xEJPi4weNObdEuPKwdFUqPcoV8nIa8Atef675F8JzJIs2GXQNgXNyeYve-j2KZdjrWs0MLWAsTQM-OYih1oHva8EvWzuf5ntIv7OCodwCGulhJRWlID7ObV9e3P3jIxYuYFV411Wu4shnKJkk7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126027adfd.mp4?token=b_D8QsT95QgNgAFFBeCFvy1O7jXU71tBF2T7ijmiTbtQPbNVHZFeQSlvWLwLHZFQuV0l01d74HMfgw9k_YyLrsBArL84SZpKpDBwBZsmFRcy8nkI0V1jvR9JuuwYdVWXGEnZBTrdAGNu-6CJNEWgxwhqsu2PhD1NcqOw4XfZeqN2wQB7r8w890qm_4veDAyuNf2xEJPi4weNObdEuPKwdFUqPcoV8nIa8Atef675F8JzJIs2GXQNgXNyeYve-j2KZdjrWs0MLWAsTQM-OYih1oHva8EvWzuf5ntIv7OCodwCGulhJRWlID7ObV9e3P3jIxYuYFV411Wu4shnKJkk7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صدا‌وسیما از جزئیات و تعداد حملات به شهرهای بوشهر، کنگان، دیر و عسلویه   @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/449299" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42113266c.mp4?token=LwGgEGg21zbAQh1-OyZezT5iuCTRVAFN2khcZGpG8cIbFDTOXubmJZdDzFczVpg2F8UDdSBAeclE_8onW4w1WUDS8fttFhGOJRfsm6eWhNgnnTjxQT0aVeLTMKcueyFumUiSfap-cPfv8L6DfzDLxqyJQw1jxAjrDbwF0i3GAUDxUcmoFg7cbSZByx4hBPqKsRPFE3HAoz7aTOCCdWbxRNcTIiuNaFb1bs85eF3NYh2eA524XEFxLqk_oH67zpB6-fFZLx5fvFCdTLV_DSs5cO7cJPyH4j4xtO3o_qRG4TAjhq8qRSXMcYfEcqEqi8X7N0OxT9PEyiA9h7GvYZ1uB3mDJtMxoUpdEGLcoOEZoC145v4V4bsWDuHB2GqhyN_mKTpm52JEYIDAd_yt1CNxEq3vPsk2S6pSsMAsjW5kIc7gr3ivfTS_TDQl0KiQ55Pte7IyKFpPhNwmIFTn7VFJqrUeRFQQAewVMR63XQGTf2ry_k_qbJy-j2qkuRBwNpnW2GirpyyKVbW50BOv3F8u7UnbDKawcgOyhB4gcArq-knEdMG3B3P1M8Alskqzh9sSyDfkopn9aTuQM2fOWdg6vXHJag0v4eiaWWFyF9ey35CNCRJE_A7SXTfvSoRG5aiBXTe31wnpQ7kAW-5B94pqXo9UuuvIZ3JfsFjBpzMzs4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42113266c.mp4?token=LwGgEGg21zbAQh1-OyZezT5iuCTRVAFN2khcZGpG8cIbFDTOXubmJZdDzFczVpg2F8UDdSBAeclE_8onW4w1WUDS8fttFhGOJRfsm6eWhNgnnTjxQT0aVeLTMKcueyFumUiSfap-cPfv8L6DfzDLxqyJQw1jxAjrDbwF0i3GAUDxUcmoFg7cbSZByx4hBPqKsRPFE3HAoz7aTOCCdWbxRNcTIiuNaFb1bs85eF3NYh2eA524XEFxLqk_oH67zpB6-fFZLx5fvFCdTLV_DSs5cO7cJPyH4j4xtO3o_qRG4TAjhq8qRSXMcYfEcqEqi8X7N0OxT9PEyiA9h7GvYZ1uB3mDJtMxoUpdEGLcoOEZoC145v4V4bsWDuHB2GqhyN_mKTpm52JEYIDAd_yt1CNxEq3vPsk2S6pSsMAsjW5kIc7gr3ivfTS_TDQl0KiQ55Pte7IyKFpPhNwmIFTn7VFJqrUeRFQQAewVMR63XQGTf2ry_k_qbJy-j2qkuRBwNpnW2GirpyyKVbW50BOv3F8u7UnbDKawcgOyhB4gcArq-knEdMG3B3P1M8Alskqzh9sSyDfkopn9aTuQM2fOWdg6vXHJag0v4eiaWWFyF9ey35CNCRJE_A7SXTfvSoRG5aiBXTe31wnpQ7kAW-5B94pqXo9UuuvIZ3JfsFjBpzMzs4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🔹
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.  @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/449298" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚽️
انگلیس با برتری ۲ بر ۱ برابر نروژ، به نیمه‌نهایی جام‌جهانی صعود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/449297" target="_blank">📅 03:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
تکذیب شایعه حمله به اهواز و آبادان
🔹
معاون امنیتی استانداری خوزستان اخبار منتشر شده مبنی بر وقوع انفجار در شهرهای اهواز و آبادان را به شدت تکذیب کرد و آن را شایعه‌ای بی‌اساس و ناشی از عملیات روانی رسانه‌های معاند دانست.
🔹
وی با تأکید بر پایداری کامل امنیت در استان، اظهار داشت: نیروهای امنیتی و نظامی در آماده‌باش کامل هستند و هیچ رخداد خاصی در استان تا این لحظه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/449296" target="_blank">📅 03:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار از سواحل هرمزگان
🔹
دقایقی پیش مردم از سمت نوار ساحلی سیریک و میناب و بندرعباس صدای چند انفجار شنیدند.
🔹
هنوز منشا انفجارها مشخص نیست و اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/449295" target="_blank">📅 03:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=jmPgz4lvtosWUNWnrH12dW6qt07UT9keu2Px3eCdjwEC3hJBklBU2tBm4_SZ-PAhVBFx85x3gUkT4KSSUlDOUbRc4Izb2OjmT-rSM8pZUtvqkIFm_8RHucWoUY5AP8__lHcyQd8X3A9INN7RGg3yqHP-6tz7St50GeWDGFGylEvyCM9WXDllvq_EkGu-A9691lrSxF7zzpe1P5BqhS1XMePvlAyCajI3-jnwuiwjViDCZWWFprJS9_czo_JW6N_MQCU50kRLr8-Sd_UWgx0cTErShcElL0f4zQQ74gwyRjcNG-hcAbr9NiNMdNGKuIuWTb0bvOu3RBusmLbLm8T47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=jmPgz4lvtosWUNWnrH12dW6qt07UT9keu2Px3eCdjwEC3hJBklBU2tBm4_SZ-PAhVBFx85x3gUkT4KSSUlDOUbRc4Izb2OjmT-rSM8pZUtvqkIFm_8RHucWoUY5AP8__lHcyQd8X3A9INN7RGg3yqHP-6tz7St50GeWDGFGylEvyCM9WXDllvq_EkGu-A9691lrSxF7zzpe1P5BqhS1XMePvlAyCajI3-jnwuiwjViDCZWWFprJS9_czo_JW6N_MQCU50kRLr8-Sd_UWgx0cTErShcElL0f4zQQ74gwyRjcNG-hcAbr9NiNMdNGKuIuWTb0bvOu3RBusmLbLm8T47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🔹
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/449294" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLl9WjHs4HTwnELA6Vd1qx6xv56LT6munC26z7T1ZmfQ86ErwY6ijPoDVn2KdE6zAyIOugOSTmapidrMGUaM0ZcS_mR61UXy6xg_9nLwcuRVmXToH2ydrkyCWS3vB5ev6RS30IDG5358AyUuH_MKa7rMANDD-79mVHFSQXQN-_OLl1XL5lNsWmw9cucuvbnzs_No_mwk2GCDawEQXHjaIAPkXFWqY9ZYnyltAyHYDZxw5tG8QJQHLa02fu6FK70idq2knv4548m-OUHr47C49waNaqei3q2cLYOGq-zr-scrYz9XnGqbsjDn77ZoTyMGzpkxS8XsU3-TOuMRa4WEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شنیده شدن صدای چند انفجار در عسلویه و بندر دیر
🔹
دقایقی پیش مردم در عسلویه و بندر دیر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/449293" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
شنیده شدن صدای چند انفجار در عسلویه و بندر دیر
🔹
دقایقی پیش مردم در عسلویه و بندر دیر صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449292" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
برخی منابع محلی عراقی از وقوع انفجارهایی در اطراف اربیل در کردستان عراق خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449291" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFTb94rJAPQWFQIkq-LFMiML1_nmc4a7_An3bJ_v5-UykKGnH-NrgzQhcIFRbvMh6jMMX_Ynh4PqWi_Nvikn1A344iyf-hVX5L8ZJFaZwSjj4uWboOu00H1JIdUTsj2LVA0CqpSeWKKebmw9LDSwraJ5HKPbEnBI6o98iKGM_7GdYIARfJCumr7VlUgdmlI_rFYo9DYO3U3bnqKspVUFS8FT64e7CY1rLAsu91eJ_eT5h_cnR8uqSFqBM6K9U2hz9GEKkstcGF5a1k5TEhxgK-BTs4cWkAMTbvzM9fK0q5YzCij-Z5iP8kVA1M9vVATojNYxsDegFTdjjDG_T47nRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bA43NFfK7H6A8o62RNPvPJcCTg_9uj6rKUojzHVV75AtXdn5IfTJUKSindSpXm-_-CjdybctadK_NywRr5Ky7lIlWR3zduqaNUxnOP68JgDYZt7t8aE-qHsjOVoie5dyOYXwVWtsAgISt7FOiyDkOOmRVTZmIA6QW8px36SYEGaJkse440LqEKhLMkRExGwngy0EatxU-7_XLt4aPTXzbl3x0ZjKV0dSVF9ByXGxh45nip07UuofID4ZOfY8GHxw1n5RNXF8IL46j6VLoZKuJWzsk8sz0-mlyTHetJHCpqws5GV2gsr3j1jeHF0QjPDSf4YmjtwmpevdaZhIvNArRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4Tli7xBj3OmSI0Os3ov2E5TxhLfWsKfscce7TIgPyh2Bin-uedY7p-QCMhgLllZXfB5wkkoidSI_I6FMiq9282ZROD3rsCnWix3dlRZRMtBo0CwO572QaKrEJGSZPA5HlEuPiqRdpIEXjFYLPWEsQjrRaN1LaJvgj-NOz82hjVLs_SJtUNdUi5B2nM1KMWPYtaP4jJwbQDWe4gP2XNvmqcICfS821mbyQs_syVQrh-a7amOydOkDcrbJUfeHOGMMczJnbo0dDVBM7POa8j4XJlp6DjkUx29fSzA7gRi1IlT5KRJAAJ2StkyvzA6Cp4QU1HR9NyBesLslctVBIS01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGAo22yr7eDOOU0Jiov3lxsfy9j8pmh3a2wV1VGiJ-LIlmO-kiK5TJ-qEuJZs_7iUOgxkv1wRE-vkxAvyTUxmFCwuMT0UdMM5D3h5sqe7xaWYpFCfiZA7hx1OMkgSaBBQTUq1P3DlDCdEnQb8XtsUoGQOWn2eufUcpezYMiK6C5yPvhS_lyTwIndxkkqJvcshEJEaXGrA0hpWb_M6Wsq2_1Y61LH9T_kJfOMMF_cjmaC4196BZQsH8lZhEZroUIcFkAS8XJfott4cDBF5UwiwqwGusly-Ve3uorD1g7sSzTYsyCoAV-xQCY2WzGrHy2lHDIXSgDwnvnzBkxX6KpBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3om-7f_wOyFlMy71R3o7y71TlUk-qRBy6DRUL9Qk8E6rRdcGQl5A2I8Kq507cTbRNu5NqrsXTn5VDdgq1_P6Ykamfupg3wwDrtwBH0_01iGPbhzmrb4oX2aPJzDI0zY2Ft4iJZBEs6OYfAjrTdIURWBzrn9MEBXz2ZpWdXJWdpFp3ISzmRC2MkEKOyYHa--kPPhxhy4h7ai7rdgAYn4OSChfo0fj9qKvo7dkQOpJYlrrZ_P9YPpjA8huVJnAYXdGP5XGEVuX70ohjouLkyuHnMR5YpkkHuuXxjx-Lh9tcuctUoxsmhLuq4Wk25mPeGvYN3LY23uucasdxx-KYIVLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNKlKeQG6oo0Jp8YuY6DCoJAZoy23lQoh1bgUChbLsV84k_0T6sJpVejh0W9ymvDF9_dN0FjFuyNdb629oUaRHl2zruRVsDOYVAVA8Qorr6XBJ08-59x9ay0pnyUu6cnFqBXo0VVIkXmr7fRNNWJJd1fXP9jYyuIp7osR9FwMPDFl3Gsa8l6RZmJHf5VEFsWl0yoxOxPgIvDvfTTFuWaGACLRwzcdZi7x_D0QBcm6zG9gUPGP7KvMeVADg8iaY5tmMJXrUUIJ3BivOWIaaOY88Edg_CE-ZvN403V1wH321uWWUvZhAppPtC0k5MdTzKNFDj5n-30sNKY9_YllqdrTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت آقای شهید ایران از سوی آیت‌الله سید مجتبی خامنه‌ای، رهبر معظم انقلاب در حرم امام‌رضا(ع) برگزار شد.
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/449285" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qr1QV6spBhHn9gKlK3NtL9jSBaca6NvexCTy8Vif5UgjizDQo2zy1RAFuNmxSM9UVzAIZbmMeHQqF_l6c1PS9tfXVLn_PQ78MpMSNklZc9zjbIuFda2CftlTjsYNeeWLPitd5_u5OcIaMbG3E90mw0YGaVq0NyhrNsnz8kpB8ZkbxOg7denIgTHndLYMh-JTWf9ToAPYk29WBO1u66G_kBQhRfMsi3H8Bt8WPzBdMj1eCOimKzzD7cWAxRkRdpNvHUBK6_sIUSwb_vkG9dHzfla6C_DHLKN1dh0C0w6I50crlNKMgL3FUQbsDXSv2X6JTGEiPb4nBm1OSr_XCupxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3D0XY1ZOKZrPg4sUzfsLuM1AAhjvySPZj3fvPYEB89b7N0u5x8IIONtGjZglNTBXBgT9wGH5Pa4xCqqPJXWABrcbkBnHxiX4MKjmcx44ftVN_emTNOuVVTnHl5LXujNPfOJm3r3V0CnirDBoJgG0eQROjtfa_V3y_gUTaT75D20hoeAWWFanrBHV5ZPcTMmbyWgVopoXjtJlEroIiw6dOUml30tlymQrUboDhEMjtHDLj4nfdUHTvzd8a76bFmRXbeaTOL3bcCLta6oLwRfAKYmBVsnx61HeAUpQdiGhDoncYQpREyiZdos8PDEoEEFPrV90Qijco3BCWD9Z2ladg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMUKBYeOCTTqH3G2ltlp8CElww_l2ROlBpli7wZrFBxIBnZV9-dx9BUmgUeVrDxpT2hTO5GcMF5_TVyXY7yO1Rr8Lnek3g9DhtdfPVu53_Ee61yt-UtEFyrN8orYsCoatmq0KRs2C_pHlBZK8oucPeAcEomwR9pMH3lPJ1jQkM4etHYu8W44Fmo-dNHgQKwTDn5sUyklAsF1W78-pdMOb1XLr5lTXiQau9oPCrZHaV2rCltuNjM0oF73LXUj5svGh8wx_c-cKxAqBQZEWpHFl3nsxRz7qPgKy24VAupUmDExIU-ApFwJkW65FjKCE9zPi1ZYzwmUbXOZrt0rBz8B0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jphdolqmlgsbZeKiZiNrhUFcG28UMqnXfWhh67-kZSzGp2oF9qR9BYmiVr6pzOpAshK95RS_mCF1a2uM-Tq-6kDWzKQ15fDCldIx264LdCdqf5Lr5qCUvxxsv9kLAQKlZeqbyWlLqmPabatweLWXLaHY4Dg_73Yd9QrkI0mumBiNaTm4tt6yCcPt-8XrJbU9wJNAZhpD-oWSi7KN4dBBVi63XXSIjadXwOv6gtsAzC6v0RFJVjCoJnA0rv_NRYlYhl9aYC0-H_osg81M91R3wpH1Dq-11WCWAdjgNRy8LnMks1CXp1ewYu6cZTxrajDJE7qoHG-_u08XPJv8DagjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bp8LqjoDFkc5H4EnO98LIQ3l5Fn06hEadeIjdo0SfBVfbCy2trKdLpcVd2B4fVgSxRrLBJUjoXbCodHqYm3rJaT4mgd5agGY_Shp13j2WYaispZW-ataNc5ugMJcIkAQBLS0GOtVr2wFK0WiXcEF2d1rEx6zuZb-YaVibapxYcUTwTixRyLy3EGbbEIl8JVt5DzA87voU7FpvDOpdUBQ0Dp3gz4oq0uZuf7K83VJlMP4z0PeEWQZuXLLGc_ZHYHOLA4XwtPKA_iTjLK-D0RVC2-R9e3qwBN99r-DLVs41t6KZWiSnC64YsGaYTviJL60Pt-2e-01HCKzTAml3k4AUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf-J-IoEMEFOOmY2qnkoZuIkxReoWSs4qRm4ppAEUZ9L9bRpJdKMMuoSTyLt_t004-Gn9REPEJPoG2rdL5VoZC7_3ZMvVaSFP1KgmdGK-HC_LtMnm6kJP6X47M0h4mNX3z9_dMxV238XKVdeB6KDZ31xtBLXF2jstlKfSYstBdkru-JU-3A8rSufdqrRsNgdO3-ERzIMdG057HSukvt6XvXpVcJmC6lwOQyB0-f6VTTMMKFGKL8UjXz26JMcKtutpicUTl0fBs_VIwuhP0nPLasyExhpylebbxPakj6HHtXBQviN3qSib4X-q8GBWYEq0DdiZd8otifVKJWOir9cfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_CRtujcnlSflTLEJR_toFBJRLM9Q1OyPJRFPKYJGZSxIw5Jw6zVj5ykkueMk2SInE1eyTy0JpMVzN36yvsYo24FY0n0fLpCXHAlbmeNtO0yDRhhOqq4iPCjk7u-nEKEFBtLNopwfNg_X4VY0MA5hOYCD-s6Ms8ovG3HcBpHfCs-CLgtB3Xiq-PaI1OojxE0myW5ZYDh9E0WIMQtuAg5AyjeKT1arBrsKdf4oQYe_WGyVUWjaM84Gr24AEI-r_N9kkuuWRDiZdvUUsL1EZyZHQ48P2UInj-pYeMO1x7B9WyCjHGwcMienspaOqrub24e2YEIV_vOiH_fumM7g2_pBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
#گزارش_تصویری
| قاب‌هایی متفاوت از رواق دارالذکر و حضور مردم عزادار برای زیارت مزار مطهر رهبر شهید انقلاب در حرم مطهر رضوی
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/449278" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449277" target="_blank">📅 02:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/449276" target="_blank">📅 01:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
🔹
نیروی دریایی سپاه: در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.
🔹
ساعاتی قبل، این تذکرات نادیده گرفته شد و با تحریک بیگانگان چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی‌اعتنایی کردند.
🔹
به ناچار یک فروند از کشتی‌ها که با خاموش کردن سامانه‌های خود امنیت دریایی را به مخاطره افکنده بود؛ مورد اصابت شلیک‌ِاخطار واقع و متوقف شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/449275" target="_blank">📅 01:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9fcade4ba.mp4?token=E0TsVVm9yEKlTeL4O9U6fVxfYaS-hgjdd5NfRK1gpJcmhbeC4SknKOVZMONJCabnWcxEuFpOlzA1HmyEdEOJL7TFgrg7SsYzy4cg5OvJll_ntirho0Z0haKuZ8OVCTeAqJTgxDVFBvFsY0lNeUDE_CRW83bLYIbtL2cyAVUkhUfSyJhgQZakioPtxzEmkTUwryv3wjrY0D1wRywd2yWLA7IY4V7yyPW0dgAnmdjNqwCi7bNXjabzJEb2p2_zPaaXM_k5IOlNOjEjaDs9pSJLYfF8PSBSPQJTzLF7M8hxhaF4aHZl71yhDYiGG5Aqys0gRxpE4vZlfRLweM4BW8NF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9fcade4ba.mp4?token=E0TsVVm9yEKlTeL4O9U6fVxfYaS-hgjdd5NfRK1gpJcmhbeC4SknKOVZMONJCabnWcxEuFpOlzA1HmyEdEOJL7TFgrg7SsYzy4cg5OvJll_ntirho0Z0haKuZ8OVCTeAqJTgxDVFBvFsY0lNeUDE_CRW83bLYIbtL2cyAVUkhUfSyJhgQZakioPtxzEmkTUwryv3wjrY0D1wRywd2yWLA7IY4V7yyPW0dgAnmdjNqwCi7bNXjabzJEb2p2_zPaaXM_k5IOlNOjEjaDs9pSJLYfF8PSBSPQJTzLF7M8hxhaF4aHZl71yhDYiGG5Aqys0gRxpE4vZlfRLweM4BW8NF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بحرین برای دومین شب متوالی، با وجود تهدیدهای رژیم، در سوگ رهبر شهید انقلاب به عزاداری پرداختند
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449273" target="_blank">📅 01:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS5hP77a_19Gkq7FGCBnR6USueBK5OPSNH_QGOiWHIgMbRux_jByG2G-uha2oUZGifg1h2pRLNBrw9SaSWC5ClbhKJyvXQUz4JtDFBc2nKSId2K1T4AyAwiMMFCWqratOgVLyxBxW4eULKVom-eJ0pLdtOLI0QN0IG1IUYYstZFin86q9xxGfDaE09MdslmA42bgm0Vw8v8qF3eDrEsL-v7aVzWzWXLjrxb3DImx1JsUMf1NsOaTmOrI3eCdG7bhFs9jQ-VgqZu8IIUuZxoUZ5zjIWFrYQvucMYoIpFc5Qi34ryX6Luzj8OgOWDEwFR7HyZ6uLhn4dMZWsLZ9-TLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تساوی انگلیس و نروژ در نیمۀ اول
انگلیس ۱ - ۱ نروژ
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449272" target="_blank">📅 01:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBOaDBzNXEYdiPSZBYNOnJ8YpDjsK11PnuvSmnBVyncAI27HbAgVYdwiPBfzn351aIHuy37wIa5Gyv8zHpApTevDOQMq0uBDHXkaiP5MzGjZyjMNk3oKJh4GPDym5bt-vtRApskvAbUFMKZc84rDk_J-LCS64M36gH4fQfrGT6bdqowUQbxbwRu5Ma4lk_QWLtKr3upgkbNU9eR6-V6M6tOdu-E7_Qo6VgHISj-NmWGX8sfrhGaUa8aYD7XYez9Sy8z2UF_meEZnBNVKte2ypwgzVAIZPErM5ATpFqg_F3c3_yeKMsAMQ3x5x2eJzi9s3lHFfv-bq0gEXC6QnyirbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ بزرگ نساجی پیش پای پرسپولیس
🔹
باشگاه پرسپولیس در روزهای گذشته دانیال ایری، مدافع ملی‌پوش تیم نساجی را به‌عنوان یکی از گزینه‌های تقویت خط دفاعی خود زیر نظر داشت و مذاکراتی نیز برای جذب این بازیکن انجام شده بود.
🔹
شنیده‌ها حاکی است که نساجی برای صدور رضایت‌نامۀ ایری رقمی حدود ۱۵۰ میلیارد تومان درخواست کرده، و پرسپولیس حاضر بوده تا حدود ۱۰۰ میلیارد تومان هزینه کند؛ اما این اختلاف قابل‌توجه باعث شده مذاکرات به نتیجه نرسد.
🔹
از سوی دیگر، شنیده می‌شود مدیران نساجی در نهایت تصمیم گرفته‌اند این مدافع ملی‌پوش را در فهرست فصل آیندۀ خود حفظ کنند و اعلام کرده‌اند قصدی برای فروش وی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/449271" target="_blank">📅 01:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da88cf4c0.mp4?token=PKF2JyaaadKd3xlDW_XcJU0SUyVslvIp15-_FwV5ucVyzO_29bvd42cjDZYy8rqydmQDeG9TlQjlQ-T16ZB07TZ5T4fz1vRS2-cH6cPXaOB-r8yHS-Sn-YGpAYtKsmjbSdwz-Hji5BQN5NiGj-LJUaW17HTpM3b7RabD6ODp-eF87GVq3iTst6uzEakwDhmp53W8UkgWnBZTZWXrugDHw1ykXOirQT01tNt9pWrabSSTMw7fQjhDBylMThP9sGAjGKZztyHH8kKWErT4pqIwYpgurWKwCIlzIu5_Q6okiZwWaiD05ufbBBpBnlauYZLhYlyPUSNVHjHb6c_JvYcfLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da88cf4c0.mp4?token=PKF2JyaaadKd3xlDW_XcJU0SUyVslvIp15-_FwV5ucVyzO_29bvd42cjDZYy8rqydmQDeG9TlQjlQ-T16ZB07TZ5T4fz1vRS2-cH6cPXaOB-r8yHS-Sn-YGpAYtKsmjbSdwz-Hji5BQN5NiGj-LJUaW17HTpM3b7RabD6ODp-eF87GVq3iTst6uzEakwDhmp53W8UkgWnBZTZWXrugDHw1ykXOirQT01tNt9pWrabSSTMw7fQjhDBylMThP9sGAjGKZztyHH8kKWErT4pqIwYpgurWKwCIlzIu5_Q6okiZwWaiD05ufbBBpBnlauYZLhYlyPUSNVHjHb6c_JvYcfLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار انتقام‌خواهی مردم دامغان، در شب ۱۳۳ حضور در میدان خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449270" target="_blank">📅 01:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجار چند ساختمان در جنوب لبنان به‌دست ارتش رژیم صهیونیستی
🔹
اشغالگران اسرائیلی در ادامۀ نابودی منازل و زیرساخت‌های جنوب لبنان، چند ساختمان را در شهرک «حداثا» واقع در منطقۀ بنت‌جبیل با بمب‌گذاری درون آن‌ها با خاک یکسان کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449269" target="_blank">📅 01:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0mwyZ1UrP6r3ypWBQgNzrUCB3Knpcw1FI592YtIhioIu5asu7ZFzgXw8p3pxOk_asfX3Q7Uz94uJ_MOzjfJhrS84-O5NnlO4FyTD6hUwwJFZzl3SjQV-18HIWwyFc6EEii9CEynJ53dxYhn2U80-Rcb802JSsXBPeG3AXkHP_emtEgYGvnMwUl90q5dze2dqjwW7AKohSab2eqHjtGLw5St7MBtaJ70QohMFHUtv-9xWbzrvf3b92K1_4nvJfScM7JMi4x7QGEgp-g7XZmQyhmUTwj94drlV9UCJom2h-6uUZYQEX7XzAsZgiv6HoxbVDQShI_aauNdqlBlgmeysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8lLq-VW9468kvTl1ZT18hifS2K1yBvhsYlAwZtB4Ranv5u8ourLa8evnaAGGY7SN57f3xG7er248u9YlxCtyw4sDiXzWBjXFXvFRb2_73eCpmrsDL2LGOqRNmtevNXzRlVNdbSTzgau5XNEGhecKvwglEywlu27Xu38-0mPNACDTfD3G75baKFWAEezRO6UU_vETvjA8kC2U167w3W5EBhhJfDbkVV2S_aTj2l1eNFrlJkPGwo6X3u1VNlEssL_jVut8asrJND1q_zLWNyIsHtK7cPWVtgYPrg6_ZWP5SKQOTmnJD82a8EroAEHAc2Wj1b93W2ByLnfKucl7I8NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLiTh8pbKl_ERhvr2z62VrVXo5hqtnU_XpBo0xjT-4hf9i_rox1UbkZ-mS-CnIPMaMwYB1C0G-BtSsirgdcX72pIgunEfcLAk5ZFRIRrhXtdhkBLqv_AefFCRlK4mJJAIVJ5-vnGDQdS11xLl-KScNNhhPwMgoguZUhtizqD7QNVxK-rXwBqrjH40K73ALma2LdMytXcZJqzHhAS9nmKP0pitNfVyh1_9YulfuQlbHxswQpYwqHG7VfkFnQnOZLk_EQMynom_nFdQPgNTAQjkNZPU5SYXnAieHDpLsNlw847iPds6-9XX6zbcxnnmsYyKYQTDX5CYmdc-pcegjy9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-aqBe1rgULii5CIVVDw5Y4LL9cTnfPheZiGHDbVSb4Nptk56CZpAMzLu_03Tblv2gp1UnDURZND2Vn-0iTfOwjMwBTwURgjaLujX8O0l5yITAF-AErWLg4PhgLdlO0h-NKokCEDVCucat3uBSU9RCuLXJuqcjx0ss7sgm72tgm6ikUNJciMBWVm2USPXUz5k8sdqPJjQPIc42J0IF1N3AHFpAKVhr_wVr6zU7RpdkPUCcYE384C4xkESHQn8yYMwqRm4jRmipRhFo1lraU5tHbpSPUeaiAinmm0g9KTaz62h12tk5sc2p6ASSzihcZRcVRF-lsa6qMQlSyhViP4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OW7arzMsVO5iA5ReUdYG8LFOCcgOygeIq2toDpC4KRHycNrJ4wrTeV7KnIwxN3cXYF-QTtQnN6ZUPCi5NSQGrYTkXpwebZrg-N5Tm-rhZ__9DRx3BvK_G6oqyCpp9h3r0C7oNvfrZDTrfRGCiq8GitjreeyxwgZzTsH2R8n_uQIDe0Uch1hSjngd1rCnW4vjqj-dO22Yja7IJ3sRkMWTdxgajt9PU9k3zICTYAQj9-neHOEUtQc9G52EqoEkhBTQfKP5R2mTYiHSmNsWR02G2r9b8OHik1MUN0sXrpVZ6aF0-qY7HTPUWjQdNqtiSUiTNdQ3RYoS62AaZWaQtMpU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMAyLBr9o1qXLArqPciozH2O7Rk73niff_EIpZRS7V4VVx4n0t7hCqMqWB9StKtPd45s-L6xgQKfmoDiDDV8r107z89gwOZiWL-OlPR3paOWB4cyQych2hR_ZSbAcgvNhaGsfzDdGflMxjG3nA0Veja4gfkRG4hyhu2NNDmpPBgQGs9cVJy0OauJ43KaAfbx19d-qvV4qpsYC4RLmXw5P2f2zVw5dFNqo3TDrnUK1iMgS58qsa1vxSsDvbuDAsaAl1X-2GqkjVsJEipY4YdXkZXdg6TSnWY0DSZ5fkP6tHWghKw1UZ41cGjmoX6MeyeeuRV0MPEqigFrKjKgBqN5qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۲۱ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449263" target="_blank">📅 01:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-XNWwEjsSS5iP2ldpXAxjUODoRc1Nqe2pWR5bYu2H2ZM1PQfKELx1roD-tHOY35oGNZ0CNMAnWYacvwyjamwCupAYyyZej4OxOF1M8hNQDMzISXtM44JjGpwKRWG_zijwPXj_1H0_cTd3IpYl4G2U2E1OWOApnoNKm8RXrl6GzfyicoPC2jldSbdPMm7j2cULbGRLptTjSq-gjTKkqZu3gjCoJlaSsECSLWKhSkdPY2Tn3Z0liynAHBoJz_Ry9E-6aQ3GQsQivFMuQOcJNYuQqgiy9EmDp2aBK4QMGC02kq3Jc2L9sryPs_qMlE57jB4OGyoBDI3HX43-kujvmq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ByQa4QXhXQrFjJHuJQk4BMe7_km7fYni7oAQMZGeouEN0EZI9gpf0t_frEKsoOSCq0En8lkJXlYidDKSoO5OewSaziv6uzHS-VcEtM5pneptrTnSjbM2UFkhSpDTG23i2oh8HBqkoFc7G9pQ8RisP417UwJSFE-kR6R_HIm5eUomd5eiRgNfBpLft97HX5m1-KIWKzYbg4M1uZskK70fSVthVpYj5HdSO8wMrHVvfxUKqUJdmqEyGbED4o87vtfYZKwUpRt9A3iEexrWKbGHlGSKuceX3QLKNLf9hrlSJnhTUMu6x7moLqaQVv-krzfn-U7qgMASBs44kX8Ao_Fuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrbCy145ap1V9i2DpB0648iJnfl8oq2ffZCeP4aVe_87u5DE8WjCObcOaK9Yp36V9akPhz8NeZSN4HugK7Qb6kJNU35r0mt_o8M0mmAj0yyBEUfzRN6n_s1shVelIAvX3upVCFUzNN841L2i2q3qDAPUin8wOYdS-2cjO9hWPvLjWZo3OWGtnxalvZBswugaj-7h9cA9U5AH931DsIeMeGmCr8iqkVmsu_vi6MrvPJnhOV7hwN0hRZFp3IQgPIyT3JmBhvD0Ma8Kf5xOlLFz1QjL7SNjgrn9l8cVAJZ8xcwDABfS5yg-nf_XE3E7239u9i5EAfyKgilsqOlBouJ-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnoOkp3SZ9_CFddSkuqfg_THgtkXAFbb4rtVZgnf8LjFfYPLLkuoeX97-5KWGxUqltFUj9ZgcuwhAOepM6a5Dz_7jzqJsBfO5pbpfUdFMSKZD7qJSSQLmKJTHLUdbDpDfvIj7j3ZneP_aNYWWYQJ_P6kbDDgsT5HYNVtXxU3ydIT1mPJA2YS00kxq3AC95BG8QGzHZ13CM1oA0wR0kKP-LUQ7qhGgivF1_UuVFVVuiBHdweJJQi1m7N_GB4QrGQt-Uvgb71mXTfX2vieKNXggX4e3J2pIskipweyrP7FqQfJYouJI7fgRXWQEufs2Az8YIsOhloZ7KvI-g6EHraNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnE31rto323xBslJ6rubyZa8hyjJYQK_-tfm7yx8LQEntgO_CpViAvs00gkEaPqHtp_zYf4MmlqEuM6PIbub4w_E0TjjBiTpc1UXc4MGpqB4iovDkUyuJHZTXEyK1RPiGQMwm4PHuhX3HWt_oo1Q5AxfQLGukE4xXCxrfT76EVES5TQSaJr2nrv2xRhIG2eXjPEwsYhaf8Jrog_skbxCDM6KEsRqxuzoGhq-lBywtplRL-MbIUnwuOsPZHJCq-obpGexOxjEOCEqBHE5MlDTG75iPNSA0fRXupnI7FDf4z5OfCeQefZSWXAqbS59mngo-k3zDS0qs3D7pcQEU-zpaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T56bsCjd-9ztS4OQto0TYQSruucluDYPToT9mlT7VADOAcQH6s7fOe279NDKpqQ_U0qDbUd4qqcIlsIM_83jVcmuK_4-M6asMRXnnWDbNK1RtPF15SSivzmr-P-7nbAj22vtVV0A8vm_9nwrF69EytIP5GnjEKNc5oDfdl7PADipmtFOZ9SoHJZhgBDVL2pByKTH_lc-DUQp_rfTSFqRZcozgADuXNdd865iLTOHcp9FHgk3IIOIECBIjLlWETGtlVthjg4okJoha0In0a3_44XVLgQffaIHAarTYADj8V0tNUTDdJU0ofu206fR9QyU-TLyUlgsqLTaGUSZyRuV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkLnMe43lSTNkP_73dA8rtMvdO8gHIzg1pa_X4fSBmKKOaO1GK_LoH0w_C9cPet8STYCdmZEQiNpFbRQ4UGJ7vDyCbjLbSrgtP2FB458D4kT3d8Y3tWudjUomxjNQiQsIyasOoVdEWJtAZ-VkR4En83mZ2X4fxHOwIigCH2rZWYy-L7EsA6u0EVrNNeNV-Bxcmugd_H9EhIbqRIZQe5gYEHJzaVWBdlSxuB8QPpjU5wte6kgTdQwc22Y9p9srOyj0x2tRyPZl_z_jUVGmwQPFF_Um5wT4COGc7RtXBOXsgZ6GHDbsGoRsMnlyk9W7xI8M0MOVMpWGIXFgxg0IAGvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njNaRKu4qGCWYo9m8L7aerEhjQYK0w1B-UPF9nAVTJB15WpUmcWoiGoYMws-ejr3aZSji4-uYghVchXbv613-63ldt1GsLTVdr9fMT6fjG3zSKYQHuJhf0gQL9Dl9CTiV5jIctACIs24Chma_6p7JkM0GwNr6l90eEXe5yh9N16jFga9kO28ogxllpo5dcM8VKadS8qxkj2-_eZag6wcIKfw8-BDPdZhUz7z9sWOr7lMzL7DGm6uewz8IwLzT1cLu9ttQcPzGp40z3Hntpv0n6OPN9IW72FAYEIHMgUSN3H-P6rClYIf-nS193GqpvCkpDpfqb_eX59iaf8kDc43fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zgug-IqPaVv7npwwRWeo_juDiTzmZaZH8FQDavY1fyLAg1Y64gk1YgLMUNAJUls0w8vLzPK3bgWGD5IX6L_FjR8pKQ7eYCe3h3ZLAD4YjwswcHqfrfhZQfs1Kg7HqHCKOuBuAvPri7wHTpBUcK-VS6COMYV24QUhp7R_RZjjYluQa2vNcl56WbL5Mux_WWlDBNmHGHzU5DEUkgH8w0rR0mfncI-hAL25ScuGstL4gmqJMBcRNs47JiVlEyo-gKId0lNLJcr0iAoj5RYmmp_F8d0Ln-UaiRN3loZ2xF-3nruEgCiU4lvLLW0F2a0XH6BK4_-KJGGsmE9kID-KOsO7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep_wPTFX6fnEzbUhd0RO0pX2ndvbM4BEKcuAfROLYD2qYAcx5bDxcbJEkALAWt6ZZuaHiUCTYZrUFyo3fq5bWXXLsc2EeExjyqH9DNHzhLSsaEE0cyPiVQBakhrc5zkdjkdWErJV3ERHTsjcF4zmENGIY7rVG8rgLQOVAXd8VRIEhMQkvQusZsp2u89qL2IIzwiBnfFSxkioMTtYfnjdfw8rBEu2vPtwIb8BHAL7Cx5mxCKKO4_GtFlsYRPcHIABwK6HmoikEtm0gRGjfbfDW1rUwZhbqXodNAMTP6Qrxh7jrqdUofdHDYJmI_3YHcHSN0im_OHSGUiRSY7B9SwS6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449253" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRa83Rq_yWCGFQDgBAayUi5ht8ghka2actDVSikU7KXwfaR1jx2-1_CBXS2mFklbX9G3B9ODcrWdAe9To-xgssZe24-OufM5JSvapBRAZIbo8oz4qY4XM3HWfg4dzX1gan0ZWnZX6XvJbgHfgN55dkfmrmVsMrmPqQH5ODnRV0RKUAq7UiBJg09zzDtopJM_ISIrmIrnqYzL0ScBMlw2-GCjjw1RR7WRLE71CpgxjokTGtSkHtQxHFI1afAnoZvs6DIe_4E5NuB5vOrHV99mJrMeF_HyEQa96bTew5QMf0vaKqPElZecuLZqvJMiRfSdVteJEUf2KsvF4IXP9M3-7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از ۶۹ سال؛ وداع آخر در کربلا
🔹
پیکر صدپاره و مطهرش در بین‌الحرمین طواف داده می‌شود؛ گویی ارباب بی‌کفن، خود به استقبالِ این سرباز کهنه‌کار خویش آمده است و ۶۹ سال فراق در چند لحظه طواف ذوب می‌شود و تاریخ به احترام این عروج، کلاه از سر برمی‌دارد.
📎
خاطرات شنیدنی سفر رهبر انقلاب به کربلا در ۶۹ سال پیش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449252" target="_blank">📅 00:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvHUbjTm3KYlCVl2AEOQcecJ23q30yv6s6445OXxaBEvm1O2GQOhaju-XdSN0JYf9trpCwAkRbk5ToF7gho5OnOIu2xYX6R0PsIQJhzLiIWKSkgO3UqE2RwpTCJFM3CAl_OfJgdrjBDv5pLXcRsiEkmSqNXz3fzY0ubHauqJBxLJNjee6RZxSF71MgdnJeyMRvWqrUnh_dU_R36rp398NWztxIUl5JmRKajLFNa67VXQfpq6PjMltPbf5N0CJJAPPPU2pvR43s5VTYY8WQtZ4o4Onl34wz4k-FoYaX4jsQ1dvJEizoAejWRXlfjpJJcu8CdfD0XLG2Ene4V86X0Mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد حضور حدود ۸ میلیون نفر در مراسم تشییع رهبر شهید انقلاب در مشهد
🔹
معاون استانداری خراسان رضوی: تخمین زده می‌شود بین ۷ الی ۸ میلیون نفر در مراسم تشییع پیکر رهبر شهید انقلاب در مشهد شرکت کرده باشند.
🔹
برای تأمین امنیت این مراسم، حدود ۶۰ هزار نفر از ارکان امنیتی و نیروهای مسلح در کشور مستقر شدند که از این میان، ۱۰ هزار نفر مستقیماً در مسیر تشییع و مابقی در گلوگاه‌ها، مسیرهای ورودی و مرزها حضور داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449251" target="_blank">📅 00:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6576fa0761.mp4?token=V0dVe-SPteNxdvzZJ3Om6tpwkfFr7Tlo81pG-g241VmEynmAxkACXlpHV5XOzyY5gMGWdKqq5AjXrmWPjd9EE2poZhkfk8Vt5R0Yy4ZLGSJHVAVdhoeM3F0Ki-7d_zyEtvwTB-B0FkjZBRZl57rTwfrbjeSxsf5e38X24hthEjxVWdbQbjX4Q3KRf6gvkn1x6p5WBmUwo_an26Aai7sDglt1XPkhZUl4ngab1Jyt6lfkSe5zBfAWez0pFtca5_TXxcq4JLx3vTiehP3riWkSnWf_fANEiTF7BY5CrwHkVSRKhfYI1dyIjatSBgaGNGDFxJ-TQFoqxwNcsCDf-oXU4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6576fa0761.mp4?token=V0dVe-SPteNxdvzZJ3Om6tpwkfFr7Tlo81pG-g241VmEynmAxkACXlpHV5XOzyY5gMGWdKqq5AjXrmWPjd9EE2poZhkfk8Vt5R0Yy4ZLGSJHVAVdhoeM3F0Ki-7d_zyEtvwTB-B0FkjZBRZl57rTwfrbjeSxsf5e38X24hthEjxVWdbQbjX4Q3KRf6gvkn1x6p5WBmUwo_an26Aai7sDglt1XPkhZUl4ngab1Jyt6lfkSe5zBfAWez0pFtca5_TXxcq4JLx3vTiehP3riWkSnWf_fANEiTF7BY5CrwHkVSRKhfYI1dyIjatSBgaGNGDFxJ-TQFoqxwNcsCDf-oXU4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توله‌یوزهای هلیا پیش‌از موعد مستقل شده‌اند
🔹
براساس اطلاعات رسیده به فارس، ۲ یوزپلنگ گمشدهٔ «هلیا» همان دو توله‌ای هستند که خرداد امسال در ۲ نوبت توسط دوربین‌های پایش ثبت شده‌اند. ۲ توله‌یوز خانوادهٔ «هلیا» که چندین روز از مادر خود دور مانده بودند، «پیش‌از…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449250" target="_blank">📅 00:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66a3439079.mp4?token=qYmuXfDu88_E8ldQkr5zkPFN50BIY4tqtiuXlz3okbAhju3pmynmACkiEGAMuZ5TV7M9huIRmNUq0YbPwJY_sVxncOhtJAD-_Mmxxbc3LLdOP8d8LiLPlORLRFnOoP1BNLziuZo0t8q0h8O1KLQDVPWHm3lz4CKkOyOUiU1X2L4eOpOvHsWPW55WGk_hv-6AFyiwkaaCmOOt0boND4rTppn-j0KlfVh7mBV1KIk3hUJ0YaLKgvPdeiP1Q-rsymFivIqY_jJd8RNzPIi6K_c119ZZ5jvR9_gSd_nIGtivwX-HPXQ_XyRolFq2z_fnTdPrpaqKbUiRdzNlSqf_0LiJUpHvUFF8CgEU0A9DAU5hJyCyKgZaae4oT95O6x6aIcrpb9Xs6Nwt7mlllf5U7X7lYcdac6YFvPSuErWGdt7EpS0Qd4WdmshVkcNRE4qjlHS5KVDBjVjAxUL-GgDnU4VxhXuxqsAZOQvkDk0nxssA5jcGDql31HCvmS6JLSaHD8XBqowA1VekJMemi5nLrzrZPc4ua1K1Sd_X9vaYNnPigqvbt7_zN_1B2K-JO1J0RV5uL6UF-443oR04-GA2kVgVeQ3AX6zxJ8oTtjFtONQ6zglUJI-7czYEcCil7fGax1f3GKMA9_H2SJynhMw5E1qG2wpt7TSiYVkUv_Ah0Evc_II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66a3439079.mp4?token=qYmuXfDu88_E8ldQkr5zkPFN50BIY4tqtiuXlz3okbAhju3pmynmACkiEGAMuZ5TV7M9huIRmNUq0YbPwJY_sVxncOhtJAD-_Mmxxbc3LLdOP8d8LiLPlORLRFnOoP1BNLziuZo0t8q0h8O1KLQDVPWHm3lz4CKkOyOUiU1X2L4eOpOvHsWPW55WGk_hv-6AFyiwkaaCmOOt0boND4rTppn-j0KlfVh7mBV1KIk3hUJ0YaLKgvPdeiP1Q-rsymFivIqY_jJd8RNzPIi6K_c119ZZ5jvR9_gSd_nIGtivwX-HPXQ_XyRolFq2z_fnTdPrpaqKbUiRdzNlSqf_0LiJUpHvUFF8CgEU0A9DAU5hJyCyKgZaae4oT95O6x6aIcrpb9Xs6Nwt7mlllf5U7X7lYcdac6YFvPSuErWGdt7EpS0Qd4WdmshVkcNRE4qjlHS5KVDBjVjAxUL-GgDnU4VxhXuxqsAZOQvkDk0nxssA5jcGDql31HCvmS6JLSaHD8XBqowA1VekJMemi5nLrzrZPc4ua1K1Sd_X9vaYNnPigqvbt7_zN_1B2K-JO1J0RV5uL6UF-443oR04-GA2kVgVeQ3AX6zxJ8oTtjFtONQ6zglUJI-7czYEcCil7fGax1f3GKMA9_H2SJynhMw5E1qG2wpt7TSiYVkUv_Ah0Evc_II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثم مطیعی به یاد حسینیه امام خمینی خواند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449249" target="_blank">📅 23:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ23wlw9A6csmftqxHl_NVJ0H8N-e4oNmGrwYidak-qTxvxGnTyXrQBVZEPQczOBll0135CyfQ2fXm-sKUdKF_khEwcBaaNk2IFBROxysYfSCtETSaX0FCh4dFKOuNNgw3gkAX03mSuMWT8YJmvP9Ln1Ka3d_LYAT6sSqesxU_NNXv9tIWaCa9Sb8PY20wUSeqrw_nj_zo0hHwOCuJovM1SPLfygN5ekybC-9LRRfTsIVXgUZrRuE-z6J078oo08kHtXLK8o_n-mmZWZzAmvnRlJWmsMbj135eLmS7ynudpc1LEJER7o5OM3zYlhq5m7p9xHsrF3p2Kx07trS5YLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ کشوری رهبری به این لطافت نداشته
🔹
اگر امروز مقام مادری را برتر از هر شغل و منصبی می‌داند، به این دلیل است که رهبر انقلاب تعریف جامع و لطیفی از نقش‌زن در کانون خانواده داشتند؛ به مقوله زن همچون «هوای خانه» نگاه می‌کردند.
🔹
«نمونه ادبیات لطیف و نگاه جامع رهبر شهید نسبت به زن و خانواده را در هیچ کجای دنیا و هیچ رهبری پیدا نمی‌کنیم. ایشان فرمودند زن باید «عفیف، محجبه و درعین‌حال در متن فعالیت‌های اجتماعی» باشد.»
📎
نمونه‌ای از تاثیرات رهبر شهید در زندگی زنان ایرانی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/449248" target="_blank">📅 23:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تروریست عامل شهادت یک پلیس در کرمانشاه دستگیر شد
🔹
رئیس دادگستری آذربایجان غربی: تروریست مسلحی که عامل شهادت سرهنگ محسن چهری از کارکنان فراجا در کرمانشاه بود در سردشت دستگیر شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449247" target="_blank">📅 23:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a29d9d41b.mp4?token=TBID7dFHiZyAnRq4ZdDD_dnj_-6iLovCnNh1D-8d9hTZ35GIt6G37ntGPrZ4RMk6ta15Jsw-62-uQeg2q6yKlZ7qOuFafpkd9zN4LI2JT8pQ6x8Np4zcMJv6vRVQ2Y3sMjY5VE_eyP-XeM7QBliDcauN43wi91tmE06VUnZbzzfIrtBOkqniM4f9EOY8rdAsAklkww38BiTVendUrAJBkUw-XgISWTp31jhJx2og44wqHxfVQvHd3BCb1dj5zz_bN7OBwLe8NdJLF-rYMg_NDNqzaTqkZyOfEX0Vj3Y-ugO3A3nA3ImxqxPHCneeOnjb66oH0rTC5zgVa1Bfab8h3xsy02B7hi-CREbHVWBNMfq48jrA25qrqGybAXT3LUA2aBlVpZHCtvUuxGQPLYDEnU821kcwQW44l1xz0ZEsN5Nq7cIIQxCZ7sh4BLboOwdRSXC0E9B9Cn9GGiYnK6C0AEfc2cMilqUhVzCJCCEEgfPzHWnzWMn2FlXl3zs7f5uQ93ghkFQh5ffUmFqTOeh-QhjCabndywBwRn9pe0IhStt0nq0iTtggGSTg-pXU8-dooarP4hRod58xqYQgCJpz5F36dIYzMC4wkW-L9cOk4urK7krj2IJ_suzktjALbahdYHRdCDUOnldCNawu4PBRsx_LBBeMVFfqS9pgVYXhYcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a29d9d41b.mp4?token=TBID7dFHiZyAnRq4ZdDD_dnj_-6iLovCnNh1D-8d9hTZ35GIt6G37ntGPrZ4RMk6ta15Jsw-62-uQeg2q6yKlZ7qOuFafpkd9zN4LI2JT8pQ6x8Np4zcMJv6vRVQ2Y3sMjY5VE_eyP-XeM7QBliDcauN43wi91tmE06VUnZbzzfIrtBOkqniM4f9EOY8rdAsAklkww38BiTVendUrAJBkUw-XgISWTp31jhJx2og44wqHxfVQvHd3BCb1dj5zz_bN7OBwLe8NdJLF-rYMg_NDNqzaTqkZyOfEX0Vj3Y-ugO3A3nA3ImxqxPHCneeOnjb66oH0rTC5zgVa1Bfab8h3xsy02B7hi-CREbHVWBNMfq48jrA25qrqGybAXT3LUA2aBlVpZHCtvUuxGQPLYDEnU821kcwQW44l1xz0ZEsN5Nq7cIIQxCZ7sh4BLboOwdRSXC0E9B9Cn9GGiYnK6C0AEfc2cMilqUhVzCJCCEEgfPzHWnzWMn2FlXl3zs7f5uQ93ghkFQh5ffUmFqTOeh-QhjCabndywBwRn9pe0IhStt0nq0iTtggGSTg-pXU8-dooarP4hRod58xqYQgCJpz5F36dIYzMC4wkW-L9cOk4urK7krj2IJ_suzktjALbahdYHRdCDUOnldCNawu4PBRsx_LBBeMVFfqS9pgVYXhYcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر شهید در موج ۱۳۳ بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449246" target="_blank">📅 23:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqq06_v2RPaQcdUt89uL9UTOfpKAkfGszSWwDno58DeM2-SpHeLebpVs87QilgFaALl2T_dgA38yH3P2T82CzK4p-ZmJT_MvhfQTAvDg-MZXY4JaRWAtzowvvdj0Iuovt7B-oxfaEj88-fdCA18WAT0YKNKfHb7bHp9WRFx0herWXtpK73wodv-mLwCLMaT1JQc0HAPqJK-wLHv8A7ztTUwXIRDzarhWv9JMZ2gZpbIFihNMOcNqq28_vwnbq4o0e4sMLvttg1qvY3EIexmKE-YKzrt9s__yvt-Jv4VZIuRkbT8HPigBZ4OSCunjc0ynlUAPVomneLY_YL6O2zX_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
این نقطه شروع کار خون توست...
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/449245" target="_blank">📅 23:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449243">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPzSvM-OI1kDjQ724DuuxDyF10yRfV5PauYZTUqdrYN-l1Es1jngt1u_L252q25J0BFAmGXODlxd5_j2bk_VHvru0f1mqnnUobKBCFmsC2MSjKfFEJNnbPISrzU32_XDLeXLEZforzQL7XOl6jSYt7HjtDgKYeIvvH5pieeeKMWYHWe3EspRdZ2Axr2WeR81LsjV54lIf2LcmdnHZKsn-zA3Y6xVMVOT18S4GBNMnJpqeghOCxG5sqcQtQsnqyDhxRl5KUKRRWfiwVdGa2Rp1e1DIowu5O0dXNzMht5TXE99opqRECTep0s0Dth9x81nSkrJ4ChZmTi0rkhqeInFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KegMrw7tvw6F1PcgvB1VqMOJ3TWBINSY7I0NYcGKPcY0hH_tSV8paIwM9eJwiD5FQhPSaPTW482BQvPaHSpA99FvsCmN0npuC6b-6qNjz2PqEyZQXJxrltUw6tHwfagtNlxXqehe1dupaqOwqqYLAiKmJ9K6POFKK7ShcFH8BrLqjlaXhDrVKjRqBij8VRRNnARXDOtT_tGeGLAEiB1IVQm1ERNFez9XmYyol7udkj-rLfdrbm5VEeD6X8Qifcnj0so6ZhFBn6sEgMX7ps_EaPvObfxo0cHscM5S9Wg_48mm7uZLRl0kO5KSjnOz0h7gni2_13sCzLb18BBwWl6JCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم انگلیس و نروژ
⏰
ساعت: ۰۰:۳۰
@Sportfars</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449243" target="_blank">📅 23:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449242">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f727df6f.mp4?token=PJ5RbfKdaZMZLclL-ER2VvviVnGDagmV8F0TwUSPt3FA672Olrt3jEXfdrsPxoqMpM-CJVc0CW0axquUKNT8uqSn4HKPoczZ5SrVSmxvy_ZQZoM8DoFDRC0fDmNuM4uDfd9z-y9BpoOpkzgDGon77jv78qHCF8j8l_ae6CqF6JnWMADVDKIBEr62WeLE8TFG-Rv8G5vVJwbfy4TxvE6A0We4P8IelvCMenHChhya8tRRNfw14ADtAOwWja9nsJ2g8RoSTpdpTylqKRG4vyr4sNJNeLfdBS6m9VHi5cj9b1aD499bvSE4N4_FDV2VkFkCLQriEN3DbthNRYeOaP6QXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f727df6f.mp4?token=PJ5RbfKdaZMZLclL-ER2VvviVnGDagmV8F0TwUSPt3FA672Olrt3jEXfdrsPxoqMpM-CJVc0CW0axquUKNT8uqSn4HKPoczZ5SrVSmxvy_ZQZoM8DoFDRC0fDmNuM4uDfd9z-y9BpoOpkzgDGon77jv78qHCF8j8l_ae6CqF6JnWMADVDKIBEr62WeLE8TFG-Rv8G5vVJwbfy4TxvE6A0We4P8IelvCMenHChhya8tRRNfw14ADtAOwWja9nsJ2g8RoSTpdpTylqKRG4vyr4sNJNeLfdBS6m9VHi5cj9b1aD499bvSE4N4_FDV2VkFkCLQriEN3DbthNRYeOaP6QXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک روس مصدوم شد و به اسنایدر آمریکایی باخت
🔹
در مهم‌ترین مسابقه از مسابقات کشتی آزاد آمریکا (RAF)، در وزن ۹۷ کیلوگرم کایل اسنایدر آمریکایی موفق شد عبدالرشید سعدالله‌یف روس، قهرمان جهان و المپیک را شکست دهد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449242" target="_blank">📅 23:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449241">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98dfa7bc47.mp4?token=foNYoAw_rjt_aOKH93i7UYzCIinSuw8c6kf5Emtim44FoH9l5-aymeERByRjl-ut7NfTgXUo5meBwQXp_ThVBgWmQWhAam_-HRcVSQuuMW4dM5f1BKHPH759ZJBzDLSxBz1LEBVT5qbdTUjvg2dFL_R4G1y0k783d9gPgHOb6Wbfhoxix9KUgejJ4lmpB52di9Yf-8bvo2R7Dn_e03hydD7dDr8p5OiJcfPigxkj88GXvm8q1isAtwqVBabdsmXkzL8H1hcdO_pMjDfceIpAYPpomVd1Tp3z0Y8SKDeo7CqhzA7DdIbskt_etV-ugs-h-MuZOP5iwgLqbKYd1omlyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98dfa7bc47.mp4?token=foNYoAw_rjt_aOKH93i7UYzCIinSuw8c6kf5Emtim44FoH9l5-aymeERByRjl-ut7NfTgXUo5meBwQXp_ThVBgWmQWhAam_-HRcVSQuuMW4dM5f1BKHPH759ZJBzDLSxBz1LEBVT5qbdTUjvg2dFL_R4G1y0k783d9gPgHOb6Wbfhoxix9KUgejJ4lmpB52di9Yf-8bvo2R7Dn_e03hydD7dDr8p5OiJcfPigxkj88GXvm8q1isAtwqVBabdsmXkzL8H1hcdO_pMjDfceIpAYPpomVd1Tp3z0Y8SKDeo7CqhzA7DdIbskt_etV-ugs-h-MuZOP5iwgLqbKYd1omlyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع عزاداران رهبر شهید در میدان بسیج زرند کرمان
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449241" target="_blank">📅 22:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449237">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me-mW0idgd7nz7XTj3DRAZglAJHJf_Hoghg80PycoxSlEN0EwFmM8_YWrhhpTIsMM4A65o0haZi82QyNQVjPLWBbdpWqy3GU1ycG93J58fxnM4ExnOYL0-lCA05h3DWtRBmL_2IDPCkDiEusTmigzuAAUtfNiQgnEdzA96DP996GHq4Gl9wA8rrqWY-NUfhELGwuOuOb2tw6AtpR5BZ92uoKXdlP9YizE56DfWqRKDfnorNoWadWFUogW2GeDl2InTmnsWurA4_AGwrCPt1FefB_rrF7vtPhL3FIyvFS_FVDQxnRQ1T60Sgrhiwet-jHK05OmaKEplfI6pyUYvyE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkMik7IUJHWsjX6xoaQYccHTn1KbCcYpI47klJoJpg_U9X-6ymdEsKkBK7p3dMuFg5ZKygs96-FMJBECddXx2akpQHdu7pawMLyMTCaCc-bMfULmbX411zHWPd4V1rl-1zyk0AUW0WH4l1pibaWnN3zM06rdWQ6mVH3KkkgAc5HWw0GELXUC5xLyG_av1TiPkdyu9j6k--OZ7_teGwJbQ5CJ3RWQ0hheMyIh0zANk03_UVnQ6hO3Nw-04u5kSKMgj3x-yPbVGR9xO5i3NW397O-r4WDBqojBNaNFGZFSmaLhdOAGYEUATzZy4W5mhPfpfG7GiFabxIiwgVEBUwTFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TowKjOlatvCxY8dwINviOXqDLpSJR-bBf-7QpALfvL2PdlDKuQ6Scrba-x82MMCrgYZ8IlfyomJa0dd8pg7AywqOTilQhiwb9PMXiCxRWOtBeSEa2M5B0B6pX3FYm3eM5ONsERkRYvPQlCpayCGihiYfDmUill0iTjGsBgjA1_Oz37FVtJzU7nbjHLn6T_dJ1QS23d1vO4gSaq0sM9ueV4db25-ZCuJ9x-6VlLzMK_0mrTHsQEI_Rx3NTIqh7-0MeAPOeHEGvPa62FKWHtxY64TFcRD-ISkbo9AnRxX81_xJB5aNDktH48iicXe-6Vj_xpWjbWkfS-1HfQLdcZzPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUUwzzt-gU5D3oIdl94IkdWizDV89PYFuHqPZO-l_KGr-DJCE4wpi6RxP9_F3EP6f0ngFJdtWmmcJ9MU_Zr0Ug-wvhJwZXMlcc9pSzUjY0l_shKLgTbfO46EC_CthBYI_UMG3yeGNe7h0ypdxt6_1DrED74NwWVZRAkidaZyON_-pZAwHfVeIuS_hAZ6HNE3HNbCkapN1wzI89nx91BxDEfaK6Q79-GFwcQZEkSi92XbEes-EergWN9XaQodSozzPai8BLSbkjqvJqWdMYEydbxrkv4neeHMkk-CIe7CrPJiiVgUcV2BmJ70B8BqRPmf1Qpu_nSDN2K3_wOxpmxy_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع مردم ایلام با یک مهندس شهید
🔹
مراسم تشییع پیکر شهید محسن نجاتی با حضور گسترده مردم و مسئولان در گلزار شهدای صالح ایلام برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/449237" target="_blank">📅 22:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449236">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت فردا هم ادامه دارد
🔹
سپاه سیدالشهدا(ع) استان تهران: فردا برای دومین روز متوالی، عملیات انهدام مهمات عمل‌نکرده ناشی از تجاوز آمریکایی-صهیونیستی در شهرستان پاکدشت انجام خواهد شد.
🔹
​این عملیات فنی از ساعت ۹ صبح الی ۱۳ ظهر با حضور تیم تخصصی و با امنیت کامل اجرا می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449236" target="_blank">📅 22:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449235">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a06b3177.mp4?token=pAM18ZIoDThoYroMyyJM4pgdFZx2KVusn3AcSL9boGvHKBHTFQrB2_7a4MlSHMbEiMZnPd8HIhZj-GKuFJ9nxNEPxAzMUM6mownpLkcwfjF971a6qxZP6O6SEVOYeyxY6vlvTf6H-_R1wxHoFnodRomC7hQTpmKh4tonNIaRs8n-1BF-g1ZfehzTCdeUca0OZuGmtNOySIc4AsdHp6ofZbZmSUDWLJd54xKqw70tI_9i5q26CTecjAVwMuKuZBqmfB1MQew2DJLEde1cPuliZJia-mdcX_0hrWliwLBh-Vd4Fi0ariwL1Ug8vW0I0N9UNWfIN9jrb8UmORvtf9XECjtYlYtj6x_WOzgs1FYf1nmBHXvem7IgZ0A1KT0U49_39cRMM-MxKmTj-aNRn1WGkdOiFJh6ml_k1dflD_HY6xJVLe8B_oJv1Mg5YuHPIeJZrCBc4Kq-6Kxp0FXVUM5nylWEdkTy58UxP5WDYiD3YQX919Mlx-Fd609OEmLlfWpkgv13sFisZ_bDpJn8Vk5fbHvvGiZ5Iw85PQS8QzUMzayeZJMq4fFnabUURIM9uL1dcr4L79COC9fHdc2BvziojYUOHil4de1vrDkrhsk5y1uzP-jAGOp4BLvf1p4rmLqS4z2CcX2vP0E3anLhWpybbTP5O0KC-eiQx2VgrhpvHBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a06b3177.mp4?token=pAM18ZIoDThoYroMyyJM4pgdFZx2KVusn3AcSL9boGvHKBHTFQrB2_7a4MlSHMbEiMZnPd8HIhZj-GKuFJ9nxNEPxAzMUM6mownpLkcwfjF971a6qxZP6O6SEVOYeyxY6vlvTf6H-_R1wxHoFnodRomC7hQTpmKh4tonNIaRs8n-1BF-g1ZfehzTCdeUca0OZuGmtNOySIc4AsdHp6ofZbZmSUDWLJd54xKqw70tI_9i5q26CTecjAVwMuKuZBqmfB1MQew2DJLEde1cPuliZJia-mdcX_0hrWliwLBh-Vd4Fi0ariwL1Ug8vW0I0N9UNWfIN9jrb8UmORvtf9XECjtYlYtj6x_WOzgs1FYf1nmBHXvem7IgZ0A1KT0U49_39cRMM-MxKmTj-aNRn1WGkdOiFJh6ml_k1dflD_HY6xJVLe8B_oJv1Mg5YuHPIeJZrCBc4Kq-6Kxp0FXVUM5nylWEdkTy58UxP5WDYiD3YQX919Mlx-Fd609OEmLlfWpkgv13sFisZ_bDpJn8Vk5fbHvvGiZ5Iw85PQS8QzUMzayeZJMq4fFnabUURIM9uL1dcr4L79COC9fHdc2BvziojYUOHil4de1vrDkrhsk5y1uzP-jAGOp4BLvf1p4rmLqS4z2CcX2vP0E3anLhWpybbTP5O0KC-eiQx2VgrhpvHBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضرغامی: حتما باید اگر کسی نقدی به مسئولان در جریان مذاکرات دارد باید بیان کند و اصل امربه‌معروف هم دربارۀ اصحاب قدرت است
🔹
البته باید مواظب بود این نقدها به تخریب تبدیل نشود زیرا اختلاف‌افکنی با سخنان رهبر انقلاب مطابقت ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449235" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449234">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXxvox719J_O9bCcUymO9pYYdil9eitb0pJJcbk--oIv9xiFPjOaUw71B93-LRxCD2NKHcNXNlVO3_V-F-JwFjZgDnxSxMIknMbwy54XmzEwYYiYEN_zII6WkPnoBws8FXOMOp4uHPp7Nn9QGvvDVOf2o592uA4lkky1sFrxs9xnIWvOqo6SalUgdoJnKpkBQbALERj4xaKTGoBXRQ9OpKejmGUVxLaUs73VWFnG-7WhpwIo_Sm98TdDp9o2eA8V1c-AdgBgvEzcAxoZXILcY9wuQicfn3_nxTlH5grrPPDH0X192Rz5iNSYUTCPD7e1AibUUUrogc97akbHwc5VVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل قطعی برق در چند نقطۀ کشور چه بود
🔹
هم‌زمان با افزایش قابل‌توجه دمای هوا، چند واحد نیروگاهی کشور به‌دلیل نقص فنی به‌صورت اضطراری از مدار خارج شدند و حدود هزار مگاوات از ظرفیت تولید برق کشور کاهش یافت.
🔹
خرابی ترانس در یکی از واحدهای نیروگاه تبریز و خم‌شدن روتور در یکی از واحدهای نیروگاه قشم از جمله دلایل خروج این واحدها از مدار بوده است.
🔹
رجبی مشهدی، معاون وزارت نیرو با اشاره به افزایش فشار بر شبکۀ برق به‌دلیل گرمای شدید و خروج اضطراری نیروگاه‌ها، از مردم خواست برای حفظ پایداری تأمین برق، در مصرف برق صرفه‌جویی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449234" target="_blank">📅 22:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2b14ee02.mp4?token=bYdKsC6-5flqkIsOTQOUZskYaA7XeowLXqecbxJW2_F_JnHu8q1hawPMzN24gHnlrF10i_MpKn6qSanvygsu1siHnqtW9_Ctr8vxqOp9-h09i0ou5iIfbL4mE37-ibvkiOjQp1dREhLaA124Mpy5KN_TE33CNu1pTGFYTi0Ksl03nk2568c63kHevAU6SrQAmYxlQogNRLGoNQmetMy5G7tuucMPsd_9fuFLr0IkmNsgHN1em25wP0vRaxy41BftPuFyIXFwxG5tIiDQr-LMNdH18_q_Y4UVsBWzbiBgipBBKBwUACUG811lYoGu7QnPpeFSc0oZE0K6Fg9QwT3sow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2b14ee02.mp4?token=bYdKsC6-5flqkIsOTQOUZskYaA7XeowLXqecbxJW2_F_JnHu8q1hawPMzN24gHnlrF10i_MpKn6qSanvygsu1siHnqtW9_Ctr8vxqOp9-h09i0ou5iIfbL4mE37-ibvkiOjQp1dREhLaA124Mpy5KN_TE33CNu1pTGFYTi0Ksl03nk2568c63kHevAU6SrQAmYxlQogNRLGoNQmetMy5G7tuucMPsd_9fuFLr0IkmNsgHN1em25wP0vRaxy41BftPuFyIXFwxG5tIiDQr-LMNdH18_q_Y4UVsBWzbiBgipBBKBwUACUG811lYoGu7QnPpeFSc0oZE0K6Fg9QwT3sow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۳۳ شب پایداری مردم شهرستان کوار استان فارس
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449233" target="_blank">📅 22:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔹
خبرگزاری عمان: عمان و ایران در مسقط گفتگوهایی را درباره تردد دریایی در تنگه هرمز برگزار کردند تا از ایمنی و آزادی این مسیر آبی اطمینان حاصل شود.
🔹
عمان و ایران توافق کردند که گفتگوهای فنی و سیاسی را برای رسیدن به توافقاتی مطابق با قوانین بین‌المللی، ادامه دهند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449232" target="_blank">📅 22:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc69f6bc7.mp4?token=jd-Ojc4VFqVgF1q-CnjdbY_uLqirADgaFwTn-q6R1JFx7KuKtq8cFAPS35hfmVoP5KVSYr_I1eqEorNL2n1KcUPa_2kU-XP_clvaFj1RI2HogSXaqKnqQUEOi-QNY4mn9oNvKxRR0jVrB8LvmGuY8og5sGTGa4zNE8o3YLHz-ouEb3ImjpPwjWKIKs1Y0UXF7MTmLJzkYr5Ro9QTKw8EK5C78k6POUu4YIrmfRGj9hsqUxvG6765iOvsnxEV-ElHqbh5TWfWUDB3kuio37hxK8JjUfx1N8K574-aqvUzc_zswNrxdeuCK1T48zUBHkeuQCF35Xc3w_uPb1Tt2WjXrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc69f6bc7.mp4?token=jd-Ojc4VFqVgF1q-CnjdbY_uLqirADgaFwTn-q6R1JFx7KuKtq8cFAPS35hfmVoP5KVSYr_I1eqEorNL2n1KcUPa_2kU-XP_clvaFj1RI2HogSXaqKnqQUEOi-QNY4mn9oNvKxRR0jVrB8LvmGuY8og5sGTGa4zNE8o3YLHz-ouEb3ImjpPwjWKIKs1Y0UXF7MTmLJzkYr5Ro9QTKw8EK5C78k6POUu4YIrmfRGj9hsqUxvG6765iOvsnxEV-ElHqbh5TWfWUDB3kuio37hxK8JjUfx1N8K574-aqvUzc_zswNrxdeuCK1T48zUBHkeuQCF35Xc3w_uPb1Tt2WjXrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اختلال بانکی کِی تمام می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449231" target="_blank">📅 22:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da132def03.mp4?token=QQ3PNE2jkS754A-lpI1oxyRNSesbcKz76S8iL0rFxwqs8UjtVyeK6Hx_SibyFZWfZ1k7SYNo6z204moseVP1gPwjYtiTpZvxl7AWOh1b9BmdHTXzZKbr2y7UcE5i1jMugTsNuiaqmriQuWB27MUBoMltwmFkPOzMorwOP6nLvDAiSyS22BIxeCk4Q7OR-Q_2JYspggPV_7iS7Mqf1nOoJpOajEtxKOMjbc48p-Py2ElTSVH2yvxZhyjWWYHOjf9dqYhJVERdo0QAVf3BqJPjEbxEllYOAgCxiVV6WYwIWNmGtIVRuQBQnN6TiOmUX6GmBKmWdaqAHVyMfaybhsRtRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da132def03.mp4?token=QQ3PNE2jkS754A-lpI1oxyRNSesbcKz76S8iL0rFxwqs8UjtVyeK6Hx_SibyFZWfZ1k7SYNo6z204moseVP1gPwjYtiTpZvxl7AWOh1b9BmdHTXzZKbr2y7UcE5i1jMugTsNuiaqmriQuWB27MUBoMltwmFkPOzMorwOP6nLvDAiSyS22BIxeCk4Q7OR-Q_2JYspggPV_7iS7Mqf1nOoJpOajEtxKOMjbc48p-Py2ElTSVH2yvxZhyjWWYHOjf9dqYhJVERdo0QAVf3BqJPjEbxEllYOAgCxiVV6WYwIWNmGtIVRuQBQnN6TiOmUX6GmBKmWdaqAHVyMfaybhsRtRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیپم متفاوت است اما رهبرم را با تمام وجود دوست داشتم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449230" target="_blank">📅 22:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640feee9bc.mp4?token=Aw52k8gaNMnl4DN9s-9opypaQEnqExqafgDNouA553aV2FnJKOdAhTfDhFKnc9jga9W-mxz6_DD_ax1qTnTJncEuY03GQFXGyFPi2nzVjm912Fj7pNka65w3KHgF1mLa-MAVhVxOT6Jjzl9TqRebPSm-cr-5WefHA7QZwnVDk19lGWvpKp9GiOmYJYEKFrXLlMNB3YxSf9YA7z1fSNHTOsQxWOzFZQiUKDayOoKY2EhZndwCCaQlyc4pZ2UYItNJD1O4p2zAhIAjntpEb3NVovMxTNEJhc6t0ivkQNMsytRhvzsr0eNK0IT-miu3uzNq61BdUnCDICCn85Rv44pjCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640feee9bc.mp4?token=Aw52k8gaNMnl4DN9s-9opypaQEnqExqafgDNouA553aV2FnJKOdAhTfDhFKnc9jga9W-mxz6_DD_ax1qTnTJncEuY03GQFXGyFPi2nzVjm912Fj7pNka65w3KHgF1mLa-MAVhVxOT6Jjzl9TqRebPSm-cr-5WefHA7QZwnVDk19lGWvpKp9GiOmYJYEKFrXLlMNB3YxSf9YA7z1fSNHTOsQxWOzFZQiUKDayOoKY2EhZndwCCaQlyc4pZ2UYItNJD1O4p2zAhIAjntpEb3NVovMxTNEJhc6t0ivkQNMsytRhvzsr0eNK0IT-miu3uzNq61BdUnCDICCn85Rv44pjCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولاک نوجوان گیلانی با تقلید از مداحی معروف حسین ستوده دربارۀ ایران در برنامه محفل ستاره‌‎ها
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449229" target="_blank">📅 22:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449228">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7uvWf8iQPgsNDzPVdtszfkuPaHiWYCGaPAqe4SsczgR-qfbzlL5ifQ64XGrOfToGIhSBdTWCq884CTRpGu3R6Psk-4ZMAzbopFDLhJxgjsW34mQ76DlFER_lHT1A_1eW33bpATK7xpGvZj9QruK80FVgLZjtjuPDFX4d3g36PzNzLSzedQQ5wqa2ZLNYGj1qnoQXNZFcX8XdKS-tFwVittu31g4Fr8Zi_fjTcmCvEVpzwM71MsIDuMKFaKq_XoFYRVczP-VlFAEfop2jR5CR2if7XgkOVAQtcWQZSOINp4tJmn1nYWM2A9tuFjkRz2tJipX50DwqbOQ1DrWgFaYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویکرد، فرآیند و دستاوردهای نظام شایسته گزینی؛
💥
گزارش جامع «نگاهی به فرآیند انتصابات در هلدینگ تاپیکو» منتشر شد
🔶
گزارش «نگاهی به فرآیند انتصابات در هلدینگ تاپیکو؛ رویکرد، فرآیند و دستاوردهای نظام شایسته‌گزینی» به بررسی طراحی و اجرای نظام جدید انتصابات مدیریتی در هلدینگ سرمایه‌گذاری نفت و گاز و پتروشیمی تأمین(تاپیکو) پرداخته است.
🔶
به گزارش مدیریت روابط عمومی، برند و مسئولیت اجتماعی تاپیکو، این گزارش با هدف ارائه تصویری مستند از حرکت تاپیکو از انتصابات مبتنی بر تصمیمات موردی به سمت یک فرآیند نظام‌مند، شفاف و مبتنی بر شایستگی تدوین شده است.
🔶
هلدینگ تاپیکو به عنوان بزرگترین هلدینگ تخصصی شستا و یکی از بازیگران اصلی اقتصاد انرژی کشور، با مدیریت بیش از ۹۰ شرکت و بهره‌مندی از حدود ۱۶ هزار و ۵۰۰ نیروی انسانی متخصص، در زنجیره‌های مختلف نفت، گاز، پتروشیمی، پالایش، روانکار، لاستیک، قیر و صنایع سلولزی فعالیت دارد. این جایگاه راهبردی، ضرورت استقرار یک نظام حرفه‌ای و شفاف برای انتخاب مدیران را دوچندان کرده است.
🔹
برای دریافت متن کامل گزارش
اینجا
را کلیک کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449228" target="_blank">📅 22:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449227">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sic8sdBv_pjVhmwUiu3ggMxdPK17M-7QNwCV2jpollZrVkmml1kf1ck_LQqJkjde1awn-ljqat58oYGWP3x2sxB7dwTiBmJ6L5Z0pwCtnrn1QFhyT-RVPNsWu4JDHEEuoH4eO-veJiQoZDyTluXnG4-IRdS8znkwk5lQlBxBY5f2FMzQ242fLTvWsaE--ZVQQOoCr1HRF40ql6EM5ox8hPJitkhjD9bOWJXt7kxLKgkSLiMQ0np2Pg8obbso438_W59-9OF9KARDylJdbEuPRmL3hK1NXjdULApLRqLPhIHoLdAU4yaxmYKofxAnHCMOAMIFyU9aG2lid5c1-jJFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#راهنمای_مشتریان
📲
آخرین وضعیت خدمات فعال بانک صادرات ایران
🔹
تلاش‌های شبانه‌روزی برای پایدار سازی سامانه ها و خدمات بانک برای رفع مشکلات اخیر ادامه دارد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/449227" target="_blank">📅 21:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/449226" target="_blank">📅 21:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1e380ff5.mp4?token=UXR6Keo0cziIuUohoeanuYk8-cYlajC1WcKykGtmiM9PpwqqmRPqY6DbIgysh_9yMyT3SPSBYQ_BvX-s98h0w5sUCFgUpKWBIYmKfBRLKsYQS47OL1XWX25NTc-iKDcH_LZC08sWLu8cDQ2vJ5KPGyvE0VJ71YK5Tyi8J2RdLNIoUJ9gAQRDENOiUrqK3uhuTc-F-2N1O6wAinEHvXRxMNadfXxL37J19KygWSY4D7yjz0ReCa6qkBdzKMaq1807VOCaH4iXdi8EP2H54TzX7JUPr-rZcOEQiB-SFH4ws31vl4_iOJ9u49If43ygAIK0nVfc2s-66OgPWysW6wQ71Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1e380ff5.mp4?token=UXR6Keo0cziIuUohoeanuYk8-cYlajC1WcKykGtmiM9PpwqqmRPqY6DbIgysh_9yMyT3SPSBYQ_BvX-s98h0w5sUCFgUpKWBIYmKfBRLKsYQS47OL1XWX25NTc-iKDcH_LZC08sWLu8cDQ2vJ5KPGyvE0VJ71YK5Tyi8J2RdLNIoUJ9gAQRDENOiUrqK3uhuTc-F-2N1O6wAinEHvXRxMNadfXxL37J19KygWSY4D7yjz0ReCa6qkBdzKMaq1807VOCaH4iXdi8EP2H54TzX7JUPr-rZcOEQiB-SFH4ws31vl4_iOJ9u49If43ygAIK0nVfc2s-66OgPWysW6wQ71Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهد سرخ انتقام در تک‌تک خیابان‌های ایران فریاد می‌شود
🔹
شب ۱۳۳ تجمعات مردمی هم فرا رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449225" target="_blank">📅 21:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۰.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/449224" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۹.pdf</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449224" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f1912163.mp4?token=vsPNcw9kbpSbcMQcn5eQoqt9Sd3iNEdIY5jeRqu1cHUy4vBeA0887Kr7gqXvXTysY1gEOuh3S3gZFW3_DdNid3BLEr0ZIHk76VsEHgMQvEI7JIYBVxK29gUi3eN8XVFa4-Ehfvq1VyfoBq8IGtL2pyVzqMUFIZGkvjlUqAYYqwAOUY8hFpItzuKwViQPSuh9m0ZcprAfrKJ76xOJ6EyXI7vo16r7fktZmA6Aq_GvM0XpBWvY8m746IOLGz4WWxBSmF2vXvqxGBHFRxINkCk5JK0FJPz_P8tXNqq4gvX_p79rbmEPOftbDraAaplnlvPXCtSxG7afoyRGyOvaPSf9pQONqh6td4HB0AY6wj1OP4v2C3422qM-G9lLKXc2HK9c2fXeA731hZSYuQOfytnaRfWS_Xck_ZWprWN5TlFF7NDL8nJPVKCZ5HqOv2FNhsjcwx5PWe9cnDCNIw5XN7_kMUxETtaukgf1K8uZq9RgvfyK96lgqCHNbVXdVqB1K9snUzVufiOs3RziOcyd7usm6B_HUyHS8JMQV_KaZLXTwr20mCZ0JT8rP2-p294Yo2MZeBO5fOTq3FVTcV-lbQmRbxA859uRDd1-vvyNVA9ywSKczsNF8pEkv0BfMoKFvI8_tEq67o8j61JYZHlp87vim5OHibcPom-bxdPKxpbjVLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f1912163.mp4?token=vsPNcw9kbpSbcMQcn5eQoqt9Sd3iNEdIY5jeRqu1cHUy4vBeA0887Kr7gqXvXTysY1gEOuh3S3gZFW3_DdNid3BLEr0ZIHk76VsEHgMQvEI7JIYBVxK29gUi3eN8XVFa4-Ehfvq1VyfoBq8IGtL2pyVzqMUFIZGkvjlUqAYYqwAOUY8hFpItzuKwViQPSuh9m0ZcprAfrKJ76xOJ6EyXI7vo16r7fktZmA6Aq_GvM0XpBWvY8m746IOLGz4WWxBSmF2vXvqxGBHFRxINkCk5JK0FJPz_P8tXNqq4gvX_p79rbmEPOftbDraAaplnlvPXCtSxG7afoyRGyOvaPSf9pQONqh6td4HB0AY6wj1OP4v2C3422qM-G9lLKXc2HK9c2fXeA731hZSYuQOfytnaRfWS_Xck_ZWprWN5TlFF7NDL8nJPVKCZ5HqOv2FNhsjcwx5PWe9cnDCNIw5XN7_kMUxETtaukgf1K8uZq9RgvfyK96lgqCHNbVXdVqB1K9snUzVufiOs3RziOcyd7usm6B_HUyHS8JMQV_KaZLXTwr20mCZ0JT8rP2-p294Yo2MZeBO5fOTq3FVTcV-lbQmRbxA859uRDd1-vvyNVA9ywSKczsNF8pEkv0BfMoKFvI8_tEq67o8j61JYZHlp87vim5OHibcPom-bxdPKxpbjVLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: لعنت خدا بر آن منافقانی که به خدا گمان سوء دارند و فکر می‌کنند خدا ملت ایران را در انتقام کمک نخواهد کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/449223" target="_blank">📅 21:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478d72c5e.mp4?token=U_8n4xYTIRQNaP1RYJzlELuW24En-YJrk_pzNI_87cgurvRwfQbKGu-Dd4ixW2qqRxfbRjhxl0D2xDmve1mwp9HdOoB_dA_xdtxw0wYIxKXQtwlXkryzmXJcxAaGXYaVf6-qNk4hdYtH3AiTTiOasGGXC9bI82ZrBkEBm6TbvgZCXTs8FWa8IbEs5ceF4C1aeD_DNBrSTo9AobDYBJ34-lX_Vdcsov66nrMLlIdu_HjfhiD3IqS846Mv7YYrI4mr7FHOJoUm88gSEasbxgFTJ4jr-tRJXTCUVDar1l79XeUf3kt-BpeAfYxd2chcT45RR9akZtrftoG6sFbDr_Z0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478d72c5e.mp4?token=U_8n4xYTIRQNaP1RYJzlELuW24En-YJrk_pzNI_87cgurvRwfQbKGu-Dd4ixW2qqRxfbRjhxl0D2xDmve1mwp9HdOoB_dA_xdtxw0wYIxKXQtwlXkryzmXJcxAaGXYaVf6-qNk4hdYtH3AiTTiOasGGXC9bI82ZrBkEBm6TbvgZCXTs8FWa8IbEs5ceF4C1aeD_DNBrSTo9AobDYBJ34-lX_Vdcsov66nrMLlIdu_HjfhiD3IqS846Mv7YYrI4mr7FHOJoUm88gSEasbxgFTJ4jr-tRJXTCUVDar1l79XeUf3kt-BpeAfYxd2chcT45RR9akZtrftoG6sFbDr_Z0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: عقلانیت به ما می‌گوید باید انتقام گرفت. باید خواب آرام را از دشمنان و به‌ویژه مرتکبین این جنایت گرفت. دشمنان ما هم به‌شدت در دلشان رعب و وحشت جاری شده.   @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449222" target="_blank">📅 21:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449221">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b16e075cca.mp4?token=DnjqGFefxWdyhlq_2jpZdQjM37ZfoVoy0U9JSFgLm6-o3RlrVKfkx_QLx6yCplJlCxTr2-mBgKB1vNGp0g-U6Bf6rZHvRBTv_6xP6Zc8wnmy7TqJEmxy5TCJvileIZYy7ge2o0j0-FJk3e2BVsumFMre8acj7j0G2SDvM6BV4lFcs7OLXBXyQn-OecW7j8gmf4b9tFi50eftDxBpQJ5IA8J5p0BRTfE0D7SjwxfslLhqc5LFt7lnDxso477ql8GqxjLlH1EfWMJPntGtgExtLxgP09CqgQrRPeBwVGkjjbKNb8JKmdBIFsQFSUzTuM9nQw0midXZRE2mB4rpavKqc51vqR4E0usc96nOnYZ-xQPZ-Y_RUnwRixHShn3TlkEyOaGeREHAN74lqlkM3DTkMNlH40cEu_PulfsB-SCby6KGmamQM5aVZMZhyDG88_nMSV-_0frnc137uHmnJKMj_xO3xEbKwTZyv8KOJjuaaAgDZq4J4tiXySinHkLzCumxChGYzk1GCnIQQV6zm7WHYnOXbpAecle7d8pj_8kzhzMo7mmsRWpNY8btPcOwY0ihVKuR371fDs6ngE6fxlv_RcSw7yHc1WMOx07eX8iRGzrl9EzGoMnCnAS-MEOlhnCgMgHDqecIj5SE5yvmom3bhZWP1jKhb5hoY1x_xY2TcVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b16e075cca.mp4?token=DnjqGFefxWdyhlq_2jpZdQjM37ZfoVoy0U9JSFgLm6-o3RlrVKfkx_QLx6yCplJlCxTr2-mBgKB1vNGp0g-U6Bf6rZHvRBTv_6xP6Zc8wnmy7TqJEmxy5TCJvileIZYy7ge2o0j0-FJk3e2BVsumFMre8acj7j0G2SDvM6BV4lFcs7OLXBXyQn-OecW7j8gmf4b9tFi50eftDxBpQJ5IA8J5p0BRTfE0D7SjwxfslLhqc5LFt7lnDxso477ql8GqxjLlH1EfWMJPntGtgExtLxgP09CqgQrRPeBwVGkjjbKNb8JKmdBIFsQFSUzTuM9nQw0midXZRE2mB4rpavKqc51vqR4E0usc96nOnYZ-xQPZ-Y_RUnwRixHShn3TlkEyOaGeREHAN74lqlkM3DTkMNlH40cEu_PulfsB-SCby6KGmamQM5aVZMZhyDG88_nMSV-_0frnc137uHmnJKMj_xO3xEbKwTZyv8KOJjuaaAgDZq4J4tiXySinHkLzCumxChGYzk1GCnIQQV6zm7WHYnOXbpAecle7d8pj_8kzhzMo7mmsRWpNY8btPcOwY0ihVKuR371fDs6ngE6fxlv_RcSw7yHc1WMOx07eX8iRGzrl9EzGoMnCnAS-MEOlhnCgMgHDqecIj5SE5yvmom3bhZWP1jKhb5hoY1x_xY2TcVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: عقلانیت به ما می‌گوید باید انتقام گرفت. باید خواب آرام را از دشمنان و به‌ویژه مرتکبین این جنایت گرفت. دشمنان ما هم به‌شدت در دلشان رعب و وحشت جاری شده.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449221" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449220">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3fcDon9gVv0GuXESvZB_M2Q4bwgYpF5jiwSQs2RvYm2bN0FL9jV6H3UWzBHQx7zKbaWPBYyokDfNr3tzRRYKvLO4QI8v3ABinJoPYvJM44JdEcRr7YyOef68ARCdYpUVZWM7D5QRnGltUYx-c-v1AR_j5rWv5kBgGViG18lej9-IDzCuUtg9e3vCCgFikCx2Ip-ggsSb0W4vcQfSsraJpkm4_7xf9LPrY3Yv_VJHD6J_ACShyHVlwCMwnWomocNFlHzZ6Pjba-wQpYT0Jy6a_NJLlc-ir6IqvE5Mm5qNi_wUVG9fHjyk6xjZnu17MZKgJvgjLPLzx0ch4VSLU03aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نظرسنجی جدید از تجمعات مردمی سراسر کشور
🔸
خون‌خواهی رهبر شهید مهم‌ترین انگیزه حضور مردم در تجمعات است. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/449220" target="_blank">📅 21:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449219">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2de71c563.mp4?token=TZYWpB8kjnXd9LjGb2v6gKBoBLfrqSuJrk-FmcSCf2VGmcgb5NS0Rxs3W6AZIUMw1XiiV4iqclNZ8Sg22aaye5eMA1BPFfmaaZ4_gtNzkGVul9Ty6HFG8MdkjOgD_5meG7fyhSXJWej7CU-TG57OEHoYlstIFzwa2b6YCaLJ-MnJDyGNdvgF3nXzHDCXvMzp6gFNSZoWKMA7hg-xBC1gZuwNfTrQK7kQcGrYNLsxSPTd6VgWjlTM2VeU36zUGk59w3KjX1OTVj29XQaMm2RAeEr23MSrvKJ5paljVaioeMrzpZTTK7egsrNkGI0QUDGE03rbeIzaY55GU9v8J0EUPIVpU3c9mcOUWCBt1SVCmyYupAs63hDYbhSoJ8X16m-W9c_FPtz2dsE9trG6vCPI4xh9606KOWCLjSgd0UpgvbW2dfLsJSqvvRzZZt4veYSehI-dnSbpxOXIpHKDK5QC2Zf9RCRkdBNCZkyhMxRr2DmBDMoAchWOIZ0lfsNdK1CrRToYBMuUe1II-wyznGb6l7CmUbMhnbO6Fw3PWGX5QdWMe9v5l2dreE4i7kqxKNztchu8aqOftDiGv3uRaB4V-jL7nQAXSnEQYV3ohZycDW7N06YuE7NhnbGZ6_LJa_UdCBKSz1QV7k13mQQvruLT3qEnh--IJDx8BiTex7o79zU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2de71c563.mp4?token=TZYWpB8kjnXd9LjGb2v6gKBoBLfrqSuJrk-FmcSCf2VGmcgb5NS0Rxs3W6AZIUMw1XiiV4iqclNZ8Sg22aaye5eMA1BPFfmaaZ4_gtNzkGVul9Ty6HFG8MdkjOgD_5meG7fyhSXJWej7CU-TG57OEHoYlstIFzwa2b6YCaLJ-MnJDyGNdvgF3nXzHDCXvMzp6gFNSZoWKMA7hg-xBC1gZuwNfTrQK7kQcGrYNLsxSPTd6VgWjlTM2VeU36zUGk59w3KjX1OTVj29XQaMm2RAeEr23MSrvKJ5paljVaioeMrzpZTTK7egsrNkGI0QUDGE03rbeIzaY55GU9v8J0EUPIVpU3c9mcOUWCBt1SVCmyYupAs63hDYbhSoJ8X16m-W9c_FPtz2dsE9trG6vCPI4xh9606KOWCLjSgd0UpgvbW2dfLsJSqvvRzZZt4veYSehI-dnSbpxOXIpHKDK5QC2Zf9RCRkdBNCZkyhMxRr2DmBDMoAchWOIZ0lfsNdK1CrRToYBMuUe1II-wyznGb6l7CmUbMhnbO6Fw3PWGX5QdWMe9v5l2dreE4i7kqxKNztchu8aqOftDiGv3uRaB4V-jL7nQAXSnEQYV3ohZycDW7N06YuE7NhnbGZ6_LJa_UdCBKSz1QV7k13mQQvruLT3qEnh--IJDx8BiTex7o79zU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
او سرور مقاومت‌کنندگان جهان بود
🎥
مردم عراق دربارۀ رهبر شهید ایران چه گفتند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449219" target="_blank">📅 21:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlnbirMxSpx9Wa1675ub9OiV-i6yEg4j7cb3jjxSLlvjDWdyrEQmXb2aegJuNCyE5iuGPIQLdMm6MqUJFwLOhfUKJMaeB2uQHS7bfBc-SJ7kyZ-FUPM42YWniZ7_zsd4zrDVN3iCPRHcgHQrJDJPmN6PnP5qtCfPXKf6yqYv_IH9dszq5sd9E-VKtDSc2SJTuKdOGOTqRnOZ8hu2GzuvfybZJjkQTNYBNJonwrc7aHzJesvM4GWYGUC2lX3MCqMgZI87m84cYuqWznsyOfLhRJ-tYAGfJ3W3RGSzN4ERyuPDZ4xLketYIWVUBWOV69y5fvY6wKd_1OUaqaSN5FHZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: اگر موجودیت روسیه به خطر بیفتد از سلاح هسته‌ای استفاده می‌کنیم
🔹
«دیمیتری پسکوف» سخنگوی کرملین، با رد هرگونه احتمال شروع جنگ جهانی سوم از سوی روسیه، تأکید کرد که مسکو به اندازه کافی بزرگ و مسئولیت‌پذیر است تا دست به چنین اقدامی بزند.
🔹
وی با انتقاد شدید از رویکرد نظامی‌گرایانه اروپا، سیاستمداران این قاره را به «شستشوی مغزی» مالیات‌دهندگان خود متهم کرد و گفت که روسیه به عنوان «شر مطلق» معرفی می‌شود.
🔹
پسکوف در عین حال هشدار داد که در صورت تهدید موجودیت دولت روسیه، از سلاح‌های هسته‌ای استفاده خواهد شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449218" target="_blank">📅 21:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449217">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722505521a.mp4?token=Ka_HCYjJJacA1EgnhfLjtP4ZlNKzIikcuIiCgwAozbQPioVCw55f4SZCm9pKtp3RO7u4cRUaVGltXWtz2sn7CM96AckaeGp7eh1HNJXks0--tIukkQYMMtVFHb4euiafW6I9mHChRYgj5--Msng-UrGCYnXQWALPrmSoE4k6_i86XcnmDM4ZFfdTli5H2w0TQBU-9YQ4UZ9bVwZE8H2AJoeF9EeuaoQWLDK0M2MfkUGR-KqHAJ3-JiwvROgS3oJasOYarkhTzPDasfwamG9cL4Uzg2mjYUzbjty35WUjgFC4WjQyBeZts8XGHXIyvX6L35JfkJWWCQFTtCNubws1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722505521a.mp4?token=Ka_HCYjJJacA1EgnhfLjtP4ZlNKzIikcuIiCgwAozbQPioVCw55f4SZCm9pKtp3RO7u4cRUaVGltXWtz2sn7CM96AckaeGp7eh1HNJXks0--tIukkQYMMtVFHb4euiafW6I9mHChRYgj5--Msng-UrGCYnXQWALPrmSoE4k6_i86XcnmDM4ZFfdTli5H2w0TQBU-9YQ4UZ9bVwZE8H2AJoeF9EeuaoQWLDK0M2MfkUGR-KqHAJ3-JiwvROgS3oJasOYarkhTzPDasfwamG9cL4Uzg2mjYUzbjty35WUjgFC4WjQyBeZts8XGHXIyvX6L35JfkJWWCQFTtCNubws1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در جایگاه سوختی در پایتخت اوکراین درپی حملۀ روسیه
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449217" target="_blank">📅 21:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449216">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea5cd6288.mp4?token=nFroUiiv3f9svO4CIqz3JCn2-uLTOQhiN_-M6sqQO8116op4PKF5InRPM5Xdb9ohBN0kPdW8Z0Jt-EHwiwtCx69NvPvLiwFKlskUTYhJxK7V5bdROfxc0A0OV_55vi46S9nLEbgmHRNUIZui15iMkrCLPHV3X2Y7KJ_uSwUYqmvOTPFnmbtekcZiTYzUYDQZTuC7O2ry8ieZMUihaVbY6zU6rD70k5rZe5jjGu5duwoiLWgqZKpeTi5hK1tH8HiGoAU0cYs8q3kQmkC9qy_n6JBPg_dbGWDb7Rn9DV5iSz1QVSoeM0Pkbw-osgwbeJCz-ihoDOFkVqpcaz-cjqwk2r6lXlHNEAMHB-2Cb-_UjVFUTzoa987cY5SRYxf9Kb_DMUUBPymP-DHTJfkKa-gI31aT0ZB5R2PXgwHAPNzBHHzgr33ZZtF525BBurR1zXHhxoxCUe4TW-SThehPaoYMilfav0YGOBOf05DOxm2k5ffq-ZdsWgBW4ZJeRprbaS8DioQ1BZpOWVuMvW80pbCmL-t-aBu4Vd1a7fQ3esC0oges1utDbe6HthasTvn59EkALnDm9PKmL0VT5TXZ8dyT4NFF-iBo7OVubIrJM3kVKZ3fiKmLNvMxT5XxEClR8VTgKAoxb7m2cGvBgsA_DW_JiddmZ7mcNF7nDdxR9YXiL9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea5cd6288.mp4?token=nFroUiiv3f9svO4CIqz3JCn2-uLTOQhiN_-M6sqQO8116op4PKF5InRPM5Xdb9ohBN0kPdW8Z0Jt-EHwiwtCx69NvPvLiwFKlskUTYhJxK7V5bdROfxc0A0OV_55vi46S9nLEbgmHRNUIZui15iMkrCLPHV3X2Y7KJ_uSwUYqmvOTPFnmbtekcZiTYzUYDQZTuC7O2ry8ieZMUihaVbY6zU6rD70k5rZe5jjGu5duwoiLWgqZKpeTi5hK1tH8HiGoAU0cYs8q3kQmkC9qy_n6JBPg_dbGWDb7Rn9DV5iSz1QVSoeM0Pkbw-osgwbeJCz-ihoDOFkVqpcaz-cjqwk2r6lXlHNEAMHB-2Cb-_UjVFUTzoa987cY5SRYxf9Kb_DMUUBPymP-DHTJfkKa-gI31aT0ZB5R2PXgwHAPNzBHHzgr33ZZtF525BBurR1zXHhxoxCUe4TW-SThehPaoYMilfav0YGOBOf05DOxm2k5ffq-ZdsWgBW4ZJeRprbaS8DioQ1BZpOWVuMvW80pbCmL-t-aBu4Vd1a7fQ3esC0oges1utDbe6HthasTvn59EkALnDm9PKmL0VT5TXZ8dyT4NFF-iBo7OVubIrJM3kVKZ3fiKmLNvMxT5XxEClR8VTgKAoxb7m2cGvBgsA_DW_JiddmZ7mcNF7nDdxR9YXiL9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در رواق دارالذکر به آقای شهید ایران چه می‌گویند؟
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/449216" target="_blank">📅 21:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449211">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faIzhQw53v7Ti6WoS5btfADG6x5b6ghrtWiu4IlSiwj1b-OR7NDdiXHfGLFxfWYPoP8t6C0WvC2tcEhvLtJ7O-OWIE1ZJWt984ih-6cqia9w7eooMsUrl7H769k1631N4Iu2dlZPWhhWsS42NoOumpn72oE7Kf4p1meXMp4XHc0ox9Ub8PlG1Q_olQABwqeJiGCwr-isXNz9eSghLut72cEOWQK4vfT562Y6yFd8LmmlUGWhqj-9Hl9qPMGozlxyf8cw2wm5EJjeSbcnOKvKRTcWBq79FymQ0fb1prYMmVA0YL2oNpuqiblr9BdIuoStouf0r47_fuT6b1Tl-Qttig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWUtps7_fucN7t1DPW6Z7nfF-kSCU7DvgHVcqUwc5foBrx_arIEXq6koWPrWixZ2HBpS4IZgBDvfdYZTB3uJwDNV16RfqdH920ofQVXTVNjQWvoV5k3_SdBJ8ZKNQDGmLZ5zXSkbeEOSL-SnHEPyPkaHqBWuKHC2bH_bEg7y9WXLTPdx-oqOsOXcFqy52D6qUHH2egiHAVsi73_-P7dYCs3y5XA13zlXiAZr0kdIR5P4l1AbiCvEiVIKgdF2oNoUbQmNqIn3vOoJWvDlASTV8FHmrZ_PHKEMhYegtoDRDk--IwS4lo3cE3SahcfhwDtBNHIvvAtXxD_DaP_gAWj7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KysGvuKnEZURio-VzbYKhbU9AnOvDLKPP-ZfOUcghwguJkeAJ9LxBMm104Rqht7ENqMFBHisOC6BCr4cIt4opDJbzESklm8Jj-qCfiq5jIATdgejQ_mZbRAAD8DMjvJzPvuixUr5vH-mvsk5DpWJxvgiL8Xp8qBaMGjYWcmVa7-Lg4LCzOA2E2FerKFcXCvBGn9H5Pl1RLeaTRDL9sYuuvfwnsht5an4yLqnyqvUsv0Xi6ihtESYPMZx_UMQGfnXJkecEIgDqxEKeD7q7JFV1go7XymBN_RrNQ5YZ6ptL3sj7lTrU1zGxx4662N_Yma5WOfJPeH_YEfeU-dFGd6zlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRFBGYwdMP2JHHVDyUYUSuhajJxvB0F95KxaUBRUAzSHiT6byFx_6aA-g2ik2caSwKghsrBE62JLo4Lht-qvKGx8K8nkY8HyqBfW-cBUaj0yVWmtqWG-hA2Kz3rJrfQBjrzRgNSwvz74KCeR8u-0QnXTLVf7tVu06_lBJqUJFqTIYNs_zx5yJNfQywZvdZxDzKG_z8ZGUPzW8k-m7ZTYPgdAQvWLI0ua1lVz16poZEzDUuPxq-k-DV5qdXWgBl5nsV7TKpIWR7sDAzofNyg8CTO_v7mpXD-juYocrsdjGQAhPjhOef8zrLBH02G2oN51ey-ENKWbakTvTr6Xj6fycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EACsYT8wGhQJxdyXkuslL_uWf6Nw6wRO70fhDelTlHSz0KiPcUQHirzMyvKnClCdOEBN-bqXKhcx7Nd4UTAVTuierw9wfapZQBepAY26C1AZUyOQGgRXPi_J9PSCQawat5Kf3LWyorAkzqoXRoC9bEtze0pctLOuuD5aFsitZiEuhSWScDUN-iSZJ-4b41xOTxoYYaJAV5mg9AiIULOfHFDqTy_XHzLpCkmBhcSITQWs5WtRnxDLVTL3ToR2s0zQV1VpYPHJy_BXPPsky-cPan0hyE9cBI4SOQfaAAbTy9AT7F6hy-7De2R4gMgt43AtxEbIHcryJ51DRtldGNnXOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع پرشور مردم البرز در بزرگداشت آقای شهید ایران
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449211" target="_blank">📅 21:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449210">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcad9066a.mp4?token=L0Z0_OXbtmAj1cNrhQTeMMR5QmpqWLogYXWVXnDUJwrBL83_ePb6bVYb1tgXiOJ8fFS8NgM_ta57VtFX80UtGRkZIfumdQmOZWReZy6BG84BnduBMj9lJoS_X18Rud4VF071ML6K3T_nuBBt_-qmp0ZCTpRnoREGo-pBjx8VCXx1Of0wSAmhcZP6k0R5l80c1kl20L0fAkJ54YQ1df_5p-7y6b5bCjhCnEygP4m96xkKvl4Ax4dyv6krdQW38vwP4m8cxx-LWiXr6L1OBgkbMsFhY-Vc3Wxif1BFavch-rL9mjX-q-0WUMGerFgCK5wqbr0vukRHvB9DHoBp_qehI5NanKVa5vJ4OQVlEH1_tKZCQc_19eqNQKzsTdDtOWJ07GhvdhztoeMf5FW--mSY_b4lgkN9lwSbrVZEhCaIesCEOkacAcn464kenYPUq44twAxVUF5XwXMuyDUdOBz0Qst19Po2-5WIq7-fL0dAglUBQZ_Tw8Q1aWY86NNZbhbRpXii8lU_MnhVQD_Sd_SXB04x2q1JtTYF5gqwSm8lK3bsCEvBgn9UnkkwtzSLd0cA3XRYej7VSBI56fAB4dhn1ZnbiTBQrib5AWv5i7zuXkdGK96518PNTFhiEs2PUAKAxWns8K-WEoWiaVW9MtfhobUo16F7gRcLRJAY8JCPm5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcad9066a.mp4?token=L0Z0_OXbtmAj1cNrhQTeMMR5QmpqWLogYXWVXnDUJwrBL83_ePb6bVYb1tgXiOJ8fFS8NgM_ta57VtFX80UtGRkZIfumdQmOZWReZy6BG84BnduBMj9lJoS_X18Rud4VF071ML6K3T_nuBBt_-qmp0ZCTpRnoREGo-pBjx8VCXx1Of0wSAmhcZP6k0R5l80c1kl20L0fAkJ54YQ1df_5p-7y6b5bCjhCnEygP4m96xkKvl4Ax4dyv6krdQW38vwP4m8cxx-LWiXr6L1OBgkbMsFhY-Vc3Wxif1BFavch-rL9mjX-q-0WUMGerFgCK5wqbr0vukRHvB9DHoBp_qehI5NanKVa5vJ4OQVlEH1_tKZCQc_19eqNQKzsTdDtOWJ07GhvdhztoeMf5FW--mSY_b4lgkN9lwSbrVZEhCaIesCEOkacAcn464kenYPUq44twAxVUF5XwXMuyDUdOBz0Qst19Po2-5WIq7-fL0dAglUBQZ_Tw8Q1aWY86NNZbhbRpXii8lU_MnhVQD_Sd_SXB04x2q1JtTYF5gqwSm8lK3bsCEvBgn9UnkkwtzSLd0cA3XRYej7VSBI56fAB4dhn1ZnbiTBQrib5AWv5i7zuXkdGK96518PNTFhiEs2PUAKAxWns8K-WEoWiaVW9MtfhobUo16F7gRcLRJAY8JCPm5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب: انتقام خواست ملّت ماست و به‌طور حتمی باید صورت بگیرد
🔹
به پیشوای شهیدمان عرض میکنم: ای قتیل مظلوم! ای مظلوم سرافراز! ای بنده‌ی صالح خدا! حال که با چشمان اشکبار و دلهای شکسته با پیکر شما وداع میکنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449210" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449209">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f5344508.mp4?token=ZS07XjgGmNE0yr_Tlzc5O1qNnIL4l5NSr7DP-AQusdmMkt8MwP4jlmDz-jji9yVOUaUyZBD5cyt4DYmOB8x401EjVFEFosG1JO-2lnHfUZfiMJ7LCnVFNkM77JWAN_R94Z2-dU7tILvAFpio4h4mYxzucyUz1kB8MuR3oEH6rqSM6K2HJLT4RTJZ1i_7HEYu09lVL70BlSYbDghWaSVvIR4YN3Ji8WSFStms3BqZnWDhB4nMq19sD16vZzD-kP2LUqYxMoLy5zJIQwUn7fj4m3bf0cMl6VnW9ostw9ZwG3uSNvys4myAa1MuNEDoOKkPZRwbExhERSHjp7jSPHGxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f5344508.mp4?token=ZS07XjgGmNE0yr_Tlzc5O1qNnIL4l5NSr7DP-AQusdmMkt8MwP4jlmDz-jji9yVOUaUyZBD5cyt4DYmOB8x401EjVFEFosG1JO-2lnHfUZfiMJ7LCnVFNkM77JWAN_R94Z2-dU7tILvAFpio4h4mYxzucyUz1kB8MuR3oEH6rqSM6K2HJLT4RTJZ1i_7HEYu09lVL70BlSYbDghWaSVvIR4YN3Ji8WSFStms3BqZnWDhB4nMq19sD16vZzD-kP2LUqYxMoLy5zJIQwUn7fj4m3bf0cMl6VnW9ostw9ZwG3uSNvys4myAa1MuNEDoOKkPZRwbExhERSHjp7jSPHGxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش
معاون دبیر شورای‌عالی امنیت ملی به تشییع ۴۳ میلیونی رهبر شهید: پس از این تشییع پرشور مسئولیت خونخواهی سنگین‌تر است
🔹
باقری‌کنی: اتفاقی که در نجف و کربلا افتاد بی‌نظیر بود، از این جهت که رهبر جهان اسلام در کشوری دیگر مورد استقبال میلیونی مردم قرار گرفت.
🔹
پیام اصلی پیوند میلیونی مردم عراق و ایران، تأکید بر خونخواهی رهبر شهید جهان اسلام است که این پیام با پرچم‌های سرخ به‌خوبی نشان داده شد.
🔹
مقاومت امروز دیگر صرفاً یک جریان یا حرکت نیست؛ خون رهبر شهید باعث شد نهال مقاومت بارورتر و ریشه‌دارتر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449209" target="_blank">📅 20:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449208">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5074b22b90.mp4?token=gp6GXG-MfBgppW2jNw8pgWfhl4nJIQzuBIA90DEy2gcZzaPZcs51LLAZZv28X4eiN_dtVa9tTizUIYAXatJvYEEZoU0JLPssv7fjY65Hvt-00023L3FRWtwpdEahYeKCWG78L7ZR9CUql6r1zfv_ke7uN_wynK5x3Z8R--Dtga5ycGnQwrZIpqp34miUJgHNjamNDRkDk-jGgI-a2G8S-VwDp7JyMj7vUn1LBLPGrYJOd75ad95t93IDHiP59HZrdY0tfoa2fdDAsCWuib53M1aT_Mj3UjHykyCvbSOd4bxzeIZ_2xa9S7VTuvXIzSOXmQEXpTh7t5vgaMVcW_jZYYneXFBzvuOI6U5_kaQhUfmmMPg4qnaRiQzIxfyAZZm4s4pCeSyYXetkdJnDIAu33O_8YKcTOY8pIIcwy5HsQiiGBDs-FtWoONrt9gO1pki_Raf5J4z7nCA9NYCbKZl9miDRqqfsZ7wJZoU2yd06xbl1GbSFCgn2U8aKRNUTNrwJNQUiTeeso7HUKe8ZIUoSSJJLwPnVKDmlouNyw7ylIDKmxsuLocZwZVxyhI-N3Wi9zNxA5Aus6N3CbuQzaiXH_NRLyfHOZ4lpbidVL7cB7OEHH3xoFUBfAVJfaOT47lsQukQxZVXycdpEsGSZnOsK-a_5p8weUoCygW3jUYNM_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5074b22b90.mp4?token=gp6GXG-MfBgppW2jNw8pgWfhl4nJIQzuBIA90DEy2gcZzaPZcs51LLAZZv28X4eiN_dtVa9tTizUIYAXatJvYEEZoU0JLPssv7fjY65Hvt-00023L3FRWtwpdEahYeKCWG78L7ZR9CUql6r1zfv_ke7uN_wynK5x3Z8R--Dtga5ycGnQwrZIpqp34miUJgHNjamNDRkDk-jGgI-a2G8S-VwDp7JyMj7vUn1LBLPGrYJOd75ad95t93IDHiP59HZrdY0tfoa2fdDAsCWuib53M1aT_Mj3UjHykyCvbSOd4bxzeIZ_2xa9S7VTuvXIzSOXmQEXpTh7t5vgaMVcW_jZYYneXFBzvuOI6U5_kaQhUfmmMPg4qnaRiQzIxfyAZZm4s4pCeSyYXetkdJnDIAu33O_8YKcTOY8pIIcwy5HsQiiGBDs-FtWoONrt9gO1pki_Raf5J4z7nCA9NYCbKZl9miDRqqfsZ7wJZoU2yd06xbl1GbSFCgn2U8aKRNUTNrwJNQUiTeeso7HUKe8ZIUoSSJJLwPnVKDmlouNyw7ylIDKmxsuLocZwZVxyhI-N3Wi9zNxA5Aus6N3CbuQzaiXH_NRLyfHOZ4lpbidVL7cB7OEHH3xoFUBfAVJfaOT47lsQukQxZVXycdpEsGSZnOsK-a_5p8weUoCygW3jUYNM_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عمری «امین» میخواند امین‌الله اینجا؛ این‌بار امین‌الله میخواند «امین» را
🔹
شعرخوانی مهدی رسولی در دومین شب بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان در صحن جامع رضوی @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/449208" target="_blank">📅 20:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449207">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCkPhH8d1DgnWjX-uYP5e4oMojGFv2j49O4dbGow4HRpKa8wU7iydwoamo0W4S2FUVSuVFLd1XbwvdD69WOPOwnS3lTyVldtnEy4y1pO1UfuxFc1U331SnX-ZocOGRWxD86Mp1dlHVU9BY4sXiGsZ475LxrbJ33OrI77W0NMvnQkA8669-99Z_k027O4Jb1TeZN4hM0U0WQfWg6Aymr6e1n6y4lnzdsUe5COGORUPYo8JwCZDSDcbNb4Hv7m2Usr32XsOYXl8NaJQgpsjBvpaRwuaORdw9mPXO1UJjJNwrqf43Y7Qv9XX6J14x537nfrSqYYjSXXYIR-jdoGwvtYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگ-۲۹ ادعای ترامپ را بی‌اعتبار کرد
🔹
پایگاه تخصصی میلیتاری واچ مگزین: حضور جنگنده‌های میگ-۲۹ نیروی هوایی ایران در اسکورت هواپیمای حامل پیکر رهبر عالی ایران از آشکارترین نشانه‌های تداوم آمادگی عملیاتی این جنگنده‌ها پس از ماه‌ها حملات آمریکا به پایگاه‌های هوایی ایران است و ادعای دونالد ترامپ مبنی بر نابودی نیروی هوایی ایران را با چالش جدی روبه‌رو می‌کند.
🔹
به اعتقاد نویسنده این گزارش، توانایی ایران در حفظ ناوگان موجود می‌تواند نشان‌دهنده قابلیت این کشور برای حفظ آمادگی عملیاتی جنگنده‌های نسل جدید نیز باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/449207" target="_blank">📅 20:42 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
