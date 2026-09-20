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
<img src="https://cdn4.telesco.pe/file/Y7D2ejLthuKI1pzf7zAF_ZigvW-aP1oJ1dzAokgC3rPJETKgUXye2xkS5LcrdKRCVbSO2sThBmQyWfh2ggbzJ5YC9AbzT5zC2ipG_UStu6sHd7XZhiDqUSLxLswyxEp38uatHwzHhwEhnXH6vbT-gD96CmQmxzFRlQOleFkJ9JHs9wGVkJBCn5fhQdgvzuXOdheAypPJv06hsqc-rXlfJo0yi-NVWzJNoDD6CeqtSAI4MKZb2VDl-FYpqRRqzDNsw_KUN_dk0vL6QrQE09lCU_tKDwx-DenuqkaBQ1ppBa05DfkduxbiEI6ne-D0PqHOu7xHcEvirJEqf68dCizUjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-463228">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVv8gAVgDVSxdkcgbiY0JrR7AxVIzVXrrjtkSP5NXuTarIYbVBZDrPnYVu7IPFJppKTpU5FG2G30RQg1wmCz2RBNUmHvmklZcyLyaoqT8BOG2jDZeWhJenTIEB8yYCfA9dBvL8oJkvdGajPTe-ohhurAQHgq0vQ8eVBe2m7rQRDekHlE9lrb2iaMUJZ53Ztmv80_ua_9YK0O_zwNPWH07GDqc1wcmcYaeFEwVrz2g7aBkqh3s6uu3crYjiNU-No5HV9h7lOmMF72IGKBHj-ZljVNnQF83Tanop4cdwriHUVh72KZclFf4Kq_OReupY3DMU8tpHyz4c7JBUBoc4LgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ اربیل عراق خبر می‌دهند؛ علت این انفجار هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 25 · <a href="https://t.me/farsna/463228" target="_blank">📅 17:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463227">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75282217c2.mp4?token=hy5NqAbB8VWaQz7EO_1tiKBLLE0fw4crtVHAjE371HGgjjC306zgT2b0OAyJeQKBj7gZK26B2FttcHt7CLlzjiCl4ITABd3P_-0tRPaFc8vvztMGD1ltlDF9w8RldxRw82yGmOsGauTalkJ9V2KfBncFzHpA3AuWn2TKJddD32vxUkfXvwx9IfkOA1auVFWnAyxyfYYqTsJ_QKMROIX0vjPsDB584KTGnYjlXVQMAJNr2ytOFLQU7FnDRs8RLX3risX2X0SFaKY4s4c7xn4nwwA0V7qv-T3-FjbUkUpJh3rF1NZ-rWfCw7Uw3v993acgo05DMYzxJGQkxOPAkwhnSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75282217c2.mp4?token=hy5NqAbB8VWaQz7EO_1tiKBLLE0fw4crtVHAjE371HGgjjC306zgT2b0OAyJeQKBj7gZK26B2FttcHt7CLlzjiCl4ITABd3P_-0tRPaFc8vvztMGD1ltlDF9w8RldxRw82yGmOsGauTalkJ9V2KfBncFzHpA3AuWn2TKJddD32vxUkfXvwx9IfkOA1auVFWnAyxyfYYqTsJ_QKMROIX0vjPsDB584KTGnYjlXVQMAJNr2ytOFLQU7FnDRs8RLX3risX2X0SFaKY4s4c7xn4nwwA0V7qv-T3-FjbUkUpJh3rF1NZ-rWfCw7Uw3v993acgo05DMYzxJGQkxOPAkwhnSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌های جدیدی از رواق کشوردوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/farsna/463227" target="_blank">📅 17:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463226">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ اربیل عراق خبر می‌دهند؛ علت این انفجار هنوز مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/463226" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463225">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601da1c19b.mp4?token=R2-Vbdv4H5trCXQi8cd4fcU3xtSvSX-K8Wl3Sw7wpqKQPEKusCH6_J4E17dTE8frxVVKVE3H6lsZOZT3JmKtTX2w02-gHTArBVCJmBcmP3c1C8vCivZYfvBiKmXwLge6xVH8Y-j34NUYFPzNHY1pRWWs4MapUfFAEKK9Q3zkLa4OjHKefxIB-43bdK49FwGbflG0LOzQGj8JRfGArfBeaGLOJ5u8gBYF1SgqLh6GD0NWrMy53G8pdIYq4o3IEbMDktuyL4Y4bDsXH0xmTgXtWRsqfG8Us5koo9db2apkhR2BdXfWWFl_X49-l4goIryGO0VxBqesPvuQD7aRYB2rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601da1c19b.mp4?token=R2-Vbdv4H5trCXQi8cd4fcU3xtSvSX-K8Wl3Sw7wpqKQPEKusCH6_J4E17dTE8frxVVKVE3H6lsZOZT3JmKtTX2w02-gHTArBVCJmBcmP3c1C8vCivZYfvBiKmXwLge6xVH8Y-j34NUYFPzNHY1pRWWs4MapUfFAEKK9Q3zkLa4OjHKefxIB-43bdK49FwGbflG0LOzQGj8JRfGArfBeaGLOJ5u8gBYF1SgqLh6GD0NWrMy53G8pdIYq4o3IEbMDktuyL4Y4bDsXH0xmTgXtWRsqfG8Us5koo9db2apkhR2BdXfWWFl_X49-l4goIryGO0VxBqesPvuQD7aRYB2rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ پیش‌بینی‌ناپذیر برای آمریکایی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/463225" target="_blank">📅 17:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463224">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq_GXdIdjB4Jjz4Xb2yatEz1d0E52AFjKG5-mRRgR3jygCqTjBrqSJVSmxZhh1TdNOt0OlxyqWo7LkyYf3RVtoFn3qLy2MxNoYJsh6-y3xOBlxvvPMGFYxhsvW0VnjwgCgIm8qzyVEvspBBTjrgrSFp3GkcXkfVm8gsjqCmA4eZ6zUH2VY9Ud0-1_bTc_gFVfCGWWtdNq5Xf0IYGB7MNGfCUYFohy64pdchLITIgUph5ai6I2LDoYrmOZd_k_VAFRc9NrOLDODYKd4Y4giAusXiKedYl4zxen74Qs1tDUrauv0dAVHTEUDf3TKZTUA6gBKVzC6TwvChvF-Otu8KAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای مامور نفتی آمریکا در ایران به ونزوئلا باز شد
🔹
با قراردادی که میان دولت ونزوئلا و شرکت توتال امضا شده، قرار است که پروژه‌های انرژی این کشور به این شرکت فرانسوی بازگردانده شود.
🔹
توتال همان شرکتی‌ست که با خروج آمریکا از برجام، بدون هیچ تلاشی ایران را برای همیشه ترک کرد؛ شرکتی که آمریکایی‌ها در موردش گفته‌ بودند، «به توتال ماموریتی دادیم که 16 سال به خوبی انجام داد.»
🔹
سال‌ها پیش رئیس‌جمهور سابق ونزوئلا ،هوگو چاوز در مصاحبه‌ای گفته بود: «آمریکا نفت ونزوئلا را می‌خواهد، تاریخ این را ثابت می‌کند.»
🔹
در زمان او قانونی تصویب شد که منابع نفتی ونزوئلا در مالکیت دولت می‌ماند و شرکت‌های خارجی نمی‌توانستند به‌تنهایی مالک یک میدان نفتی باشند و در زمان مادورو هم ادامه یافت اما این قانون یک ماه بعد از ربایش مادورو تغییر داده شد.
🔹
حالا بلومبرگ می‌گوید که طرح ترامپ برای کنترل اکثریت بخش بزرگی از ثروت نفتی ونزوئلا منتقدانی دارد که می‌گویند ونزوئلا به یک «مستعمره منابع» مدرن، مانند «جمهوری‌های موز» تبدیل می‌شود.
🔸
جمهورهای موز، کشورهایی از آمریکای مرکزی و کارائیب در اواخر قرن نوزدهم و اوایل قرن بیستم بودند که شرکت‌های آمریکایی تولید و صادرات موز، تنها محصول مهم اقتصادشان را در دست گرفته بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/463224" target="_blank">📅 17:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463223">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۱۰۰ هزار واحد مسکونی در صف وام ۸۵۰ میلیونی
🔹
مدیرکل پایش طرح‌های مسکن وزارت راه‌وشهرسازی: درخواست تسهیلات متمم ۸۵۰ میلیون تومانی برای بیش از ۱۰۰ هزار واحد در سامانه ثبت و متقاضیان به بانک معرفی شده‌اند.
🔹
حدود ۱۶۵۰۰  واحد نیز به دفترخانه معرفی شده‌اند و در فرایند پرداخت تسهیلات قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/463223" target="_blank">📅 17:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463222">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPLbl35WbJdZuML3fsH4WjdiHSsVupm9SrFz8zwv1kvCfBBVwfHzjgFYchuJAilyWKTJlkFVOX4e2Y4GDyfP4Mgfmk_MxIjDHlw1q0JGRIBbdC_YhAcsssCaOCy93HR9GtR6IgUngpKq9ZuTIqNaDactttlD7XXgNHaaoRsY6VqNzW3aQ1RBSQSp1OrwufrCUoFbc3HfsS5SBSWvM6TKK2pTuX8-tHzl9n7r69vxIDnRz0mBxK4sU4TCh8uTPgQVf4tS2J20KPGqAoNwVT52p_-T6d2WMH4-mSCCFeQ_X7V_LIqxlJ8IQnAVPFMRkEgensv3o4XrhDbOYvmIgOI8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری غیرعلنی عربستان با چین برای دورزدن دلار
🔹
عربستان اعلام کرده از پروژهٔ «ام‌بریج» چین، سامانهٔ پرداخت مبتنی‌بر بلاک‌چین برای کاهش وابستگی به دلار و شبکه‌هایی مانند سوئیفت، خارج شده است.
🔹
بانک مرکزی عربستان می‌گوید عضویت این کشور در ام‌بریج صرفاً برای انجام تحقیقات دربارهٔ ارزهای دیجیتال بوده و پس‌از پایان این مرحله، مشارکت آن به‌پایان رسیده است.
🔹
با این حال، فایننشال‌تایمز به‌نقل از یک منبع آگاه گزارش داده که ریاض با وجود خروج رسمی، همچنان به‌صورت محتاطانه و غیرعلنی با این پروژه همکاری دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/463222" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463221">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=qEGZVWsurcr43Df3gDd8ue8q8oAHPoL-7G005C28mGDOj6X9Dufi-hZUjTTM7n0ChKwv0iG7YbtQQ6B_fJGgQhssVKbXcJZziavzfkaOEza-stuUUzyxuhvEsRijUQCe6WikwU43I-iQUCbTQq6U_aQ6WL7cNygiW0iCTY8BiVQ9eVxjQdrqvjG_G2GYd9qiwezo3C3q8JI3Wji4zRg3w3dJQtxCDNhOrCMO3_1_GSz-3Nzvrt7w_Wp6id4OrP5Dk922sYYsVqHjLjwBRsJwpCzhPxy3NX240yAEegOgIebu-Ov5Fd_iidWsuzRbDFrXklzzyDkwR-oYWshKYVeVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=qEGZVWsurcr43Df3gDd8ue8q8oAHPoL-7G005C28mGDOj6X9Dufi-hZUjTTM7n0ChKwv0iG7YbtQQ6B_fJGgQhssVKbXcJZziavzfkaOEza-stuUUzyxuhvEsRijUQCe6WikwU43I-iQUCbTQq6U_aQ6WL7cNygiW0iCTY8BiVQ9eVxjQdrqvjG_G2GYd9qiwezo3C3q8JI3Wji4zRg3w3dJQtxCDNhOrCMO3_1_GSz-3Nzvrt7w_Wp6id4OrP5Dk922sYYsVqHjLjwBRsJwpCzhPxy3NX240yAEegOgIebu-Ov5Fd_iidWsuzRbDFrXklzzyDkwR-oYWshKYVeVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نویسندۀ آمریکایی: ما از منطقۀ غرب آسیا بیرون رانده شده‌ایم؛ به این معنا که پایگاه‌های ما دیگر کارایی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/463221" target="_blank">📅 17:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463220">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94640bf397.mp4?token=j-L1BO_0niodcqc6x5d6LB597G6rYkwtkeA3Eo_ajric30Su4gSaKQwU_VCvIbHLUPiy8G0ercyN8czGNFlP0Ybaf4GctvSLFkrXgGvCEwWhNfjcD18-8Uea6Utn_wDoj81KB5fDTVMhQx_W9ltLq9kden9kWFX0rb9HntXpFXDxxQ3IUEP8v74f6SaRuTZDjaggTtVntEB7oO8M_gHz-vBHG-ECjbbznwodBKULZxBfMJLJaUpE5Gw-DhjGpzLr6houA_AkgOgOVDczc68dawpkmVOW7VfsqRwUsiMKfyJ-Ge12iJfCjz2_SbHS0JmwTnCRl8jExY8iIBvcXezNlIqh-uRB9ZPhFCre69hxuAmIotRK5teNH34de6P-SOcSa8raQWhKO5q1xUUcEOCHQo9rwdqAkSAEv3pvPdGUdLASgDTzNM5hTweg6M2iXhb2et6lvnkQefUvP3I_bZex3rVihd4cH7qhiVb7asNWIM-bwPHyDpCDETavlkTqghyn5V5hdRLLxXzNuBOfgOOjG6yj99dUtV9-FhtwFIOGnw9-j2i_JtJSeCxk4bvSP1YQiVYBEEtZqjzyxogY1GPnFffHlpl6pVQ9rAICQg0e3S9S2XBOTUyBJAjRqP6M6K3dHBDpgjbvqwDvLndigtMmn0hZwuVkxky1t2hIFe_0-nY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94640bf397.mp4?token=j-L1BO_0niodcqc6x5d6LB597G6rYkwtkeA3Eo_ajric30Su4gSaKQwU_VCvIbHLUPiy8G0ercyN8czGNFlP0Ybaf4GctvSLFkrXgGvCEwWhNfjcD18-8Uea6Utn_wDoj81KB5fDTVMhQx_W9ltLq9kden9kWFX0rb9HntXpFXDxxQ3IUEP8v74f6SaRuTZDjaggTtVntEB7oO8M_gHz-vBHG-ECjbbznwodBKULZxBfMJLJaUpE5Gw-DhjGpzLr6houA_AkgOgOVDczc68dawpkmVOW7VfsqRwUsiMKfyJ-Ge12iJfCjz2_SbHS0JmwTnCRl8jExY8iIBvcXezNlIqh-uRB9ZPhFCre69hxuAmIotRK5teNH34de6P-SOcSa8raQWhKO5q1xUUcEOCHQo9rwdqAkSAEv3pvPdGUdLASgDTzNM5hTweg6M2iXhb2et6lvnkQefUvP3I_bZex3rVihd4cH7qhiVb7asNWIM-bwPHyDpCDETavlkTqghyn5V5hdRLLxXzNuBOfgOOjG6yj99dUtV9-FhtwFIOGnw9-j2i_JtJSeCxk4bvSP1YQiVYBEEtZqjzyxogY1GPnFffHlpl6pVQ9rAICQg0e3S9S2XBOTUyBJAjRqP6M6K3dHBDpgjbvqwDvLndigtMmn0hZwuVkxky1t2hIFe_0-nY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/463220" target="_blank">📅 16:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463219">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhLsaxweToInBiYsdyuCbKaIVAe4RBOUkEzNDe6RpQhBUqzQIS4mCI1Go6M6o7Dfv6in3Ol8jdGCbkiMIn1AfVuhqduCWhxv_4iNEDs2ckZGe0QsuZX589e2amhuSyKnGeEQ9WLaKydmru4zGiecCl3ncIb98qdVI6B3Eb1CvqxkqWabF2SJzlWbcj6AoyLT0Uf_ugEtbf6uZ3He0YhckGpCHOQJ51a4AfthD4tHZUUSNnshVkiA2w0mjNzNJ7lxnxmZSgIXCuptZHb-WIVtsuLoOMtktLrfLzQMkdAmFQ2bdR2LqwD5Q7Ojz14zuQ4g4sVwkjcmkSoed4GfFQhaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۵۲ سلاح غیرمجاز در خوزستان
🔹
فرمانده انتظامی خوزستان: در راستای طرحی ۲ روزه، ۱۵۲ سلاح غیرمجاز و ۲ هزار و ۹۱۶ فشنگ کشف و ۸۹ نفر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/463219" target="_blank">📅 16:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463218">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5Cc1mNWMwPm9InnHKto2zUMpN-huFRha6870Yuqo-e-EE9JjW9KlHYpG2rWanE4uDljPfkXr_vFKaV6zR_b9vfdayz8lzujjcTvO-S-haVC0txUyqeOPKzozcjb9sz51sl19CTxSe6bSTZ266VXM0eQdmWrRWh7G4b0UfXPe9OOeahVFe3L6gCZ3x76F87do2xVYbsrOz0OLJovERLDu-H0RRYdBS_hWr8_yEiNRyy9-YJ2CacA33szC1PJXJc92N0_smc8Clh8-uYBoUhhNRFi5_BpE1HLoxhWVL0fpb6JwNsrDPl_w9v9zvzE5xUv8-LTRXkCcTqSiDCeSUyzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند برای سربازی به فجر سپاسی می‌رود
🔹
مدیرعامل باشگاه فجرسپاسی: ستاد کل نیروهای مسلح اعلام کرده بیرانوند باید به باشگاه فجرسپاسی بیاید. هرچند با توجه به بسته شدن پنجره نقل و انتقالات تا نیم فصل نمی‌توانیم از این دروازه‌بان استفاده کنیم.
🔹
نمی‌دانم اعزام…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/463218" target="_blank">📅 16:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463216">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تأمین‌اجتماعی: بازنشستگان نگران پیامک اشتباهی واریز حقوق نباشند
🔹
سازمان تأمین‌اجتماعی: پیامک اشتباه واریز حقوق شهریور برخی بازنشستگان و مستمری‌بگیران، ناشی از اختلال در شبکه بانکی بوده و حقوق کامل افراد امروز به‌صورت خودکار اصلاح و واریز می‌شود.
🔹
برخی بازنشستگان صبح امروز پیامک واریز حقوق شهریور را با مبلغی معادل معوقه یک‌ماهه مابه‌التفاوت افزایش حقوق دریافت کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/463216" target="_blank">📅 16:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463215">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9XfP5xRqmOWHR9C6e8jeMKnw_FpBhRsFKXxLJIEYznenSlIR8AXY4xF4lnNops5rzES90KyxgL2Esu3RYRP6RE25eUhY2_9ejcPPib7skTYzu16VyVOmlzoc5idB4IzM1doEOADnawkiYl7k5HO1MD5_F-cYa90CqpsKxcz8Kpy1wlidUJfW_ORCZ0nCYii3sT0B_BJBMCUlxqeV9Ey9dKX5xTTs9YEoBIhJn74lQPl_v9P5UUiKAkM3WCeEb8LeGm5y37VEM-WNhH9XCeqWr_JWvW_SZ-YTv09VKdDV691zk9MgLfsusFFoNqW0EHKyrEAY7HdpoefFq4f7G2cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پویش ملی «برای پدر، به عشق پسر»
🔹
مسجد مقدس جمکران از مردم دعوت می‌کند به‌مناسبت میلاد امام حسن عسکری(ع) و به عشق امام زمان(عج)، با انجام یک کار خیر برای همسایه، فرهنگ همسایه‌داری اسلامی و ساخت جامعهٔ آرمانی را ترویج کنند.
🔹
با ارسال عدد ١۴ به سامانه پیامکی…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/463215" target="_blank">📅 16:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463214">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMDbGNiDmx9dU1PskewIt1mdcu1IDkFSN_SP5OOvJTGb1DD1XMymyrtnCDlsEHKikVVhUZOBdwyRwJc9Wjyew10kXZ66nSJgwpDnUOrIGsTMIR-wwIKTO9Ts5GSx_dxg-SuDy3PIIBtvIuXPoGWMC7reWbAWpPKbf_Bq3YH_M2Gw7hDL95l5b6rnTHaGF3dk03yEeLpwy0ch5XEE_-lyfK9GfESPUlBCdxyROCLybT7NNaAJBCzQjGn8HhAnOVxfVe7dvfjBORnYqbgHpYgtq9mERcwMXgmbdwv_t3_3T76z2R8hocWxyOryUwKYzDGp-81Nf1C00n1o-Xzno1INcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور یگان‌های واکنش سریع ارتش در مرزها
🔹
فرمانده نیروی زمینی ارتش: بخش عمدۀ یگان‌ها در مرزهای شمال‌غرب، غرب، جنوب‌غرب، شرق، شمال‌شرق و جنوب‌شرق کشور و به‌ویژه در سواحل مکران مستقر هستند.
🔹
یگان‌های مختلف نیروی زمینی، از جمله یگان‌های نیروی مخصوص، واکنش سریع، ویژه، مکانیزه و توپخانه در مناطق مرزی حضور دارند و از پشتیبانی‌های لازم نیز برخوردار هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/463214" target="_blank">📅 16:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463213">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0157fdfc1.mp4?token=NLGp0pZ7J7KiC7MtNnDxRZaM1r8OYkoi0l-TcO88lRXkQHxMhr9RkEf0TXW8YRnxz4j7Y26QAJAMEItk9O2_POzPtHcwquApb1ia-RdFp8aqRM6LWX3C99IqYWXH4pbDsvUNFD_wlN6b_9PfB5sAK1t1MKc50z2xXFo1qUbqN96ivDhDczVYAS8nN6tSMjLqtEVMnuR46Ie54EXg8GmZFs9Art6mo0H35U3Wsyt2uLhTtOk4YOTQ1SzlfyiHY8SJ2pYc9WzG58dpggq2gyvIbmIqOOWR-FUL6k_XeJgoMOiRSLuY9NNW5fqj_ugyt9w6IPv62NnTmS-eU5pNEGODQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0157fdfc1.mp4?token=NLGp0pZ7J7KiC7MtNnDxRZaM1r8OYkoi0l-TcO88lRXkQHxMhr9RkEf0TXW8YRnxz4j7Y26QAJAMEItk9O2_POzPtHcwquApb1ia-RdFp8aqRM6LWX3C99IqYWXH4pbDsvUNFD_wlN6b_9PfB5sAK1t1MKc50z2xXFo1qUbqN96ivDhDczVYAS8nN6tSMjLqtEVMnuR46Ie54EXg8GmZFs9Art6mo0H35U3Wsyt2uLhTtOk4YOTQ1SzlfyiHY8SJ2pYc9WzG58dpggq2gyvIbmIqOOWR-FUL6k_XeJgoMOiRSLuY9NNW5fqj_ugyt9w6IPv62NnTmS-eU5pNEGODQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دولت پول دارد زیاد هم دارد
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/463213" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463212">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe605c9d8.mp4?token=szXJsUAurIdIXCnWx8SxAQiyQFSnSYXL4YdVOI7L4ZyOmg7gsDOJ-8DKzE94mhN34500CeeovxoL7SS-SFXTAkPzjnD2OFMuF4gUB4StK5S4FrOUU5mMW-erOz8FrbVmWwHTW9FdmiAQg6ozUhampsJs93PQSQdO3_5hKR8f2wLvPqo6kZQCAI05qMU20tozUXdAduq6S41J7oQB6B1D-l7-jBMrJwOddm5nOxY-odQoNOT2YzHnhp3yRiwiyvfTxvFS_wLL3CVL7jk2nYaU6CXJO8xvpDSU80OxxRnTEZUznhgv9kW0x38RsK7FBX6_s0-UsbG1NG5unrCzMBTjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe605c9d8.mp4?token=szXJsUAurIdIXCnWx8SxAQiyQFSnSYXL4YdVOI7L4ZyOmg7gsDOJ-8DKzE94mhN34500CeeovxoL7SS-SFXTAkPzjnD2OFMuF4gUB4StK5S4FrOUU5mMW-erOz8FrbVmWwHTW9FdmiAQg6ozUhampsJs93PQSQdO3_5hKR8f2wLvPqo6kZQCAI05qMU20tozUXdAduq6S41J7oQB6B1D-l7-jBMrJwOddm5nOxY-odQoNOT2YzHnhp3yRiwiyvfTxvFS_wLL3CVL7jk2nYaU6CXJO8xvpDSU80OxxRnTEZUznhgv9kW0x38RsK7FBX6_s0-UsbG1NG5unrCzMBTjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری ۴ اراذل در نسیم‌شهرِ تهران که مناز‌ل را تخریب می‌کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/463212" target="_blank">📅 16:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463211">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1901b4bda3.mp4?token=vlE55Kck5O4VZRHqyskrO9HgaO3MeaKdkGM0BspBd-jzdPTrtw_JdwrEwZmIJjVtql6Fs7d0HmUz5wLBohsWRgZI4BY1-SKDqu9A11Zz67BE9Uguow5plX61W9mZfHJWEb-f5zZTwh6E2Z7h1f2FADTM3GeR_60Ok4pCycxVLRxgz4oJ11hUGSGHsB5_23iPNHgztYT9k3K6LKyeEd4wvpq34eqq8AdIOBattO0vpiZBsJBzCBsVnWJyI9ukTbDZ8lTiqpo6UknTd1e4uRxjQ3Y2GeeSV2fMKQ2gXqQ47RuGqIcsHUE9xIeTbUgTqGkLv7SRZ6gKGVXz33j84w4r66lx1DFzRAEbDc_tObxVsKR9ALR3EZMk6sGEXng3g3_Cq7VwR5AuXD2LscQgakgs_-PifbT8McSl0qSicHdut4_6-5h8fSevWOgqOrJKrlahf9r4Ru-EU4HLbVIv1HmqLklF98MBIrjrzqu-n7VJQrHc8-BlqL57Jy8WhRCgCkcxgdHvySnKwzMlGBDCgYZEe_s_uayXhRS4qZrtaRHzPzXd0drvhtr6ux76I7FOC_E2vsb-ySRFVvYvQ9aNTomaaMNAYP86h5HWrLZfVNx2ujMsmMt_3h1BOIjDvaPPnCVWAbgieXMeFqKWPI0q62Iyqxws0F6A5E9qzZvwlM0LHN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1901b4bda3.mp4?token=vlE55Kck5O4VZRHqyskrO9HgaO3MeaKdkGM0BspBd-jzdPTrtw_JdwrEwZmIJjVtql6Fs7d0HmUz5wLBohsWRgZI4BY1-SKDqu9A11Zz67BE9Uguow5plX61W9mZfHJWEb-f5zZTwh6E2Z7h1f2FADTM3GeR_60Ok4pCycxVLRxgz4oJ11hUGSGHsB5_23iPNHgztYT9k3K6LKyeEd4wvpq34eqq8AdIOBattO0vpiZBsJBzCBsVnWJyI9ukTbDZ8lTiqpo6UknTd1e4uRxjQ3Y2GeeSV2fMKQ2gXqQ47RuGqIcsHUE9xIeTbUgTqGkLv7SRZ6gKGVXz33j84w4r66lx1DFzRAEbDc_tObxVsKR9ALR3EZMk6sGEXng3g3_Cq7VwR5AuXD2LscQgakgs_-PifbT8McSl0qSicHdut4_6-5h8fSevWOgqOrJKrlahf9r4Ru-EU4HLbVIv1HmqLklF98MBIrjrzqu-n7VJQrHc8-BlqL57Jy8WhRCgCkcxgdHvySnKwzMlGBDCgYZEe_s_uayXhRS4qZrtaRHzPzXd0drvhtr6ux76I7FOC_E2vsb-ySRFVvYvQ9aNTomaaMNAYP86h5HWrLZfVNx2ujMsmMt_3h1BOIjDvaPPnCVWAbgieXMeFqKWPI0q62Iyqxws0F6A5E9qzZvwlM0LHN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اورژانس فقط برای روزهای آرام نیست
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/463211" target="_blank">📅 15:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463210">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_rZEOC0hncuwCoXik8Igy8lKxRhatuoTNkX81PwRJbxIM0_3xNXkesFjmB1ozzssiNr6R0lIhTj_S6EhZPwp8oGgLK-lCTLeFbrJoR9oKY0UuuwzwEyL7QnSGBhdZ0k8Ewh5i592u6ZeJa2n-nemd6W6EevkTNRP7gfKqNVhm4Z0hOADNnxKbGvbw-XCBbNz2EUg3c24B9FcpreFcU9NiLeaf7fk8E__31NI7QvPN9sw7K78IvrVSLXZarkRjuhh8mK2XErs92sZGtWVPRJsOtlZ1c1NnOkGdEM-6V_5Vd6y6DIfDWNLTqFmWcm1UllZ20qY7HNUAYDsmh6FOZROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به نیویورک می‌رود
🔹
رئیس‌جمهور در روزهای آتی به‌منظور شرکت در مجمع عمومی سازمان ملل عازم آمریکا می‌شود.
🔹
رئیس‌جمهور ضمن سخنرانی در مجمع ‌عمومی و اعلام مواضع کشورمان در خصوص مسائل جهانی و خصوصاً جنگ آمریکا و اسرائیل علیه ایران، با سران برخی کشورها دیدار و رایزنی خواهد داشت.
🔹
آمریکا برای هیچ‌کدام از تیم رسانه‌ای و روابط‌عمومی رئیس‌جمهور ویزا صادر نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/463210" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463209">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0tA1p2h8qLQWbLENmfHMsW3pqyEvyUtJI3Duqp8C-zNl11qfInRAmL2ay6rKUN4wM2g4IY5hPA-NsXur6ZZFWOJXi2uUAGu12p_eTwKyowVx0IURhTjRg8cIeG6ZAFaOwlsdbIFv9xfmpy6OHvp6J-l1lX4ju2P9D0akGJWC1BGBmU5YTtCix22pPJP_Vv2YDI5WFSSjyo68KKyO37LJUjMpLGa81Ytx9jcEBwsnKcPHlxxrHGN6jduMKBlls7GRL4-uhuQpYwWjOyITWq1x4QXWfNkbkwo5loAjeJczv4UO1Mu66Qcl337bfncJdnctREpoScOgPOycUZCq8LF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  یمن: تأسیسات حساس ریاض و ینبع را هدف قرار دادیم
🔹
نیروهای مسلح یمن: ۲ عملیات نظامی موفق را با موشک‌های بالستیک، کروز و پهپاد اجرا کردیم: ۱. هدف‌گیری سایت‌های حساس در ریاض ۲. هدف‌گیری تأسیسات آرامکو در ینبع
🔹
هردو عملیات با موفقیت کامل انجام شد و آتش‌سوزی‌های…</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/463209" target="_blank">📅 15:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463208">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ورود ۲ دیپلمات فرانسوی به ایران ممنوع شد
🔹
وزارت امورخارجه: با توجه به فعالیت‌های خلاف حقوق بین‌الملل ازسوی ۲ مامور شاغل در سفارت فرانسه در تهران، وزارت خارجه این ۲ مأمور را به‌عنوان عنصر نامطلوب می‌شناسد و ورود آن‌ها به ایران ممنوع خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/463208" target="_blank">📅 15:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463207">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVTB1Oabe1iE-r3k9rfTxr87szUcVUbBtrUnryyxl4ph1iVsJXqkVkpLsg7jys6DG_6x-w8IJuOXlhBAtTk2Q-7pJcRRxoDgm9gMkMzyWgkbsl5gKVPQSOQUR07tidXPfUewKnI1h1nuSYO5khHZZA4XGGLTr8A33KKDhFFUh4ZwkNgc6Z0bsxtz-rUoetj44Vmm82WUJJbVpER6u5Rm9aRN0uUmdsahWXByoA0qxXS422HcPlqEtwh07nEAqrWUAfdfYnNCjBca7a73pgaJM_1f-99GUqbAp8U0_sY_jFydZ9xXsUQu98WaLljB9W5-uU-QBfbY7_gWXDXJirVOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ راهکار مجاهد برای تبدیل ظرفیت «جانفدا» به نیرویی برای حل مسائل کشور
🔹
مهدی مجاهد، معاون پیگیری‌های ویژه دفتر رئیس‌جمهور شهید: حضور مردم در تجمعات شبانه و همراهی با پویش‌هایی مانند «جانفدا»، نشان‌دهنده یک سرمایه اجتماعی ارزشمند و آمادگی ملت برای فداکاری و مشارکت است.
🔹
این ظرفیت اگر به‌درستی سازمان‌دهی و هدایت شود، می‌تواند از یک موج احساسی به یک نهاد پایدار مردمی برای حل مسئله تبدیل شود.
🔹
محله‌محور کردن، ساماندهی داوطلبان تخصصی، پیوند با تولید و اشتغال، استفاده از ظرفیت مردم در بحران‌ها و ایجاد سازوکار شفاف برای ارائه بازخورد پنج راهکاری است که این ظرفیت را ظرفیتی برای حل مشکلات کشور تبدیل می‌کند.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/463207" target="_blank">📅 15:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ecc4eefc.mp4?token=O7coSU4ODaMtBPR7uyfvZiIOUAnX_wK8m5ZtyyxXcQqn7OpUoqDfbG-Acu4gO25RVyN7F9jfY5S4o3Zb0y7iRT02l5UM_K7ysgVHCxQQZOcfuFoARZMzTKuzJC8JLWURTa_Pf_9H8L9rFrkNjovdC_CWpoxOEvMEnPDwt1grqykyGTnlDdkPuYPzhuTlDkfqZagPSkVbf3Y9QlGiyIP4jiUDY2vfUk7v74YPRxrLW0Fhrg2P4VDOZMGqIVViqAvbVLFdRxQLgSWPnNPkrIHdHYfjXzxGXJxzdokTmeketmQspQzW4Dmyi9646Kt6o6U17hAy06fS5iQ-EYi4sF08GHXUE-_jwNJBYtpE8z0xe8HIcF14KeoNQfQuBCDHODQJel_AtEz1LJxoZDlfocmnH49rq7EvRrkF3vtlM30ivWcjcre5luH1iTHiU2dCLu5-S4pSQr27FtCt9nn3u2vRZkdWl1TWnLlR476DLSs-hr7S0r6UaOsiN7403QPHO_S0FvFTn6DWnstmoaulxINuz1etl8UjAXCQ1jTplvT-6LY1yPK8MCac9-xwjFQ5DmaDk9XAs1gP-4v9mpTWdtOjhIeI_UGbkJoBglQdHqIIAoR667x-aRBRwsNVD7z16QEf6yRdVWNVqfHA7cj1TpDipX0Qwq3SmYLuZ3kqF039ROU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ecc4eefc.mp4?token=O7coSU4ODaMtBPR7uyfvZiIOUAnX_wK8m5ZtyyxXcQqn7OpUoqDfbG-Acu4gO25RVyN7F9jfY5S4o3Zb0y7iRT02l5UM_K7ysgVHCxQQZOcfuFoARZMzTKuzJC8JLWURTa_Pf_9H8L9rFrkNjovdC_CWpoxOEvMEnPDwt1grqykyGTnlDdkPuYPzhuTlDkfqZagPSkVbf3Y9QlGiyIP4jiUDY2vfUk7v74YPRxrLW0Fhrg2P4VDOZMGqIVViqAvbVLFdRxQLgSWPnNPkrIHdHYfjXzxGXJxzdokTmeketmQspQzW4Dmyi9646Kt6o6U17hAy06fS5iQ-EYi4sF08GHXUE-_jwNJBYtpE8z0xe8HIcF14KeoNQfQuBCDHODQJel_AtEz1LJxoZDlfocmnH49rq7EvRrkF3vtlM30ivWcjcre5luH1iTHiU2dCLu5-S4pSQr27FtCt9nn3u2vRZkdWl1TWnLlR476DLSs-hr7S0r6UaOsiN7403QPHO_S0FvFTn6DWnstmoaulxINuz1etl8UjAXCQ1jTplvT-6LY1yPK8MCac9-xwjFQ5DmaDk9XAs1gP-4v9mpTWdtOjhIeI_UGbkJoBglQdHqIIAoR667x-aRBRwsNVD7z16QEf6yRdVWNVqfHA7cj1TpDipX0Qwq3SmYLuZ3kqF039ROU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این مردم ایستادگی و اتحاد را در دل خیابان برای جهان معنا کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/463196" target="_blank">📅 15:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fcd4f50e6.mp4?token=YYwjhOJ_n-H7ssNA6xniFuBhjy7UQSI2ywqlDIr1I2s8x2AsNyGWgUquIzUOz6QVqi6ylrEqcv1F8VXWXsjbTeniW5X2Pbme0Cg0EMDJyjY1wNrsdqEg-OQSnbQx1pCkFLnQ_eBZ2rkmGqlMt1YPq2RsfOT1yH60rGsAJpaI8L-gAkrCfLUTHHU79-H7rxERlR8DhmcQ7Fs57fo3-Ic0D1FvmB7YHHqkzAsJWMsfbc5CQstvt5HW3R6V--lGMwT4kbZwmHOwQHkhHZbMZ5UcBUoORJxyZjEF_bWq5JOZHF00u6MvLOEB1DI4RNyNO6S0NZEjJGeMcVFL48hPMehS6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fcd4f50e6.mp4?token=YYwjhOJ_n-H7ssNA6xniFuBhjy7UQSI2ywqlDIr1I2s8x2AsNyGWgUquIzUOz6QVqi6ylrEqcv1F8VXWXsjbTeniW5X2Pbme0Cg0EMDJyjY1wNrsdqEg-OQSnbQx1pCkFLnQ_eBZ2rkmGqlMt1YPq2RsfOT1yH60rGsAJpaI8L-gAkrCfLUTHHU79-H7rxERlR8DhmcQ7Fs57fo3-Ic0D1FvmB7YHHqkzAsJWMsfbc5CQstvt5HW3R6V--lGMwT4kbZwmHOwQHkhHZbMZ5UcBUoORJxyZjEF_bWq5JOZHF00u6MvLOEB1DI4RNyNO6S0NZEjJGeMcVFL48hPMehS6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون آموزش متوسطهٔ وزارت آموزش‌وپرورش: معلمان در دههٔ اول مهر می‌توانند برای شرکت در کلاس‌های هوش مصنوعی ثبت‌نام کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/463195" target="_blank">📅 14:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzgSvS1qnq6RRpCqhwxz9yLZ1_KB3iiOPtzphVIdMPBdq6MHxfd8_i2VZ-uZwj5i6Y_PhChLZCeDJH9P-uU8qxxm-gY5vN0uB1HRUSXm8RySuvrooXmVjf7EDEliPDKMyqa58yCEJLBZxE-ZRAfXizIyJ-tAM_dcSy0MrCphjCQ_D_1DJXnygKx33hX3lqsqAB_PGjizgb4ydRntC4-5cSX8vDvXog5tbbfkOsDFXXfxHu9JmthgB2ZwLaD-WKYBlpghXZcvq7D3_ArdwM34lDh_mT8qTy4WGKzEdghOVmkFe52oQoBxvySOjnrNcuWb_H_nq4Vy-3i71sG2Ni1H3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان ایرانی اف‌۱۴: خلبان آمریکایی یا سرعت را نمی‌فهمد یا ارتفاع را
🔹
در گزارش شبکه آمریکایی «سی‌بی‌اس» از سرنگونی یک جنگنده F-15 توسط ایران، فردی که خلبان جنگنده معرفی شده، مدعی شده پس از اصابت موشک ایرانی به جنگنده و همچنین آسیب‌دیدن چتر نجاتش، درحالی‌که با سرعتی بین ۷۰ تا ۱۰۰ مایل بر ساعت (حدود ۱۱۰ تا ۱۶۰ کیلومتر بر ساعت) سقوط می‌کرد، با وجود شکستگی کمر، دست و شانه و آسیب‌دیدگی پا، از سقوط جان سالم به در برده و سپس خود را به ارتفاع حدود ۷ هزار پا (معادل حدود ۲۱۳۴ متر) رسانده است.
🔸
در مورد این ادعا امیر سرتیپ دوم حسین خلیلی، خلبان پیشکسوت جنگنده‌های اف‌ـ۵ و اف‌ـ۱۴ نیروی هوایی ارتش می‌گوید: «خلبان آمریکایی گفته با سرعت ۱۶۰ کیلومتر بر ساعت بر ساعت، به زمین برخورد کرده. سؤال این است که سقوط از چه ارتفاعی اتفاق افتاده، وضعیت چتر چگونه بوده و برخورد با زمین چگونه رخ داده است؟
🔸
به تعبیر من، گوینده یا معنای سرعت ۱۶۰ کیلومتر بر ساعت را نمی‌داند یا معنای صعود به ارتفاع ۷ هزار پا را.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463194" target="_blank">📅 14:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e2ca13cb.mp4?token=XI_lgoJxiRFfcxV5qn_KMYO96znPTUekG7aV3xDcuRWU41kX7Ua2thxkKtZ2My4DYju3xqYpy2N5gl4oSjTatVgt9HEIxKSZalgE8JPsmFifTmtLB0gtDGJz7vWH1eYbqEsLAPJoy4n3xprHX0d9D51ZHQJuYwVVhgd34kiJYmLNQCz04lBYSyznmtq-laGEBSBk1nsXGsIEPlIL2riv-5_EKJcWck1La96BqqlFb1DNEnoMVJXFoHVnGgny0oXbHPeqKdNDGQJ8K6WXaHskXk-TaMou1P_EA3JM0OER7mB2udwgruaH4lxqalZacJawpFH3Oby7NNWULMZGwmrGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e2ca13cb.mp4?token=XI_lgoJxiRFfcxV5qn_KMYO96znPTUekG7aV3xDcuRWU41kX7Ua2thxkKtZ2My4DYju3xqYpy2N5gl4oSjTatVgt9HEIxKSZalgE8JPsmFifTmtLB0gtDGJz7vWH1eYbqEsLAPJoy4n3xprHX0d9D51ZHQJuYwVVhgd34kiJYmLNQCz04lBYSyznmtq-laGEBSBk1nsXGsIEPlIL2riv-5_EKJcWck1La96BqqlFb1DNEnoMVJXFoHVnGgny0oXbHPeqKdNDGQJ8K6WXaHskXk-TaMou1P_EA3JM0OER7mB2udwgruaH4lxqalZacJawpFH3Oby7NNWULMZGwmrGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت بنزین و گازوئیل در اروپا و آمریکا همچنان رکورد می‌زند
🔹
به‌گفتهٔ کارشناسان تبعات منفی جنگی که ترامپ به‌راه انداخته، بر اقتصاد جهان ادامه‌دار خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/463193" target="_blank">📅 14:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=Ulxja3F5v3h1gxVNYhgXYU7ntvq7L-Zb1gT7TPjzSs6uSmBIWhfzi4JJ62paHoSH0KeXCA7lWCatkCPGNsQ9wAgtl4fvsqIW0hTtfIAqk0spd3XGRdkYKl3VOr5zPmzF94u7HCP8nHhabdGyWATqmOI4rOTy2yn3oSucvIaNWld49Dkjn7cSaEzGZm10eO1x4CeMc0wWJPBXp21jcLoCPy0DkhQrfP0-BvSfh914wTxp41P42kuJC894YHrYPSWPpWUNRwJh157pHkyQuluzrg3XGbKcQhTpfTp84kwtOkUEbwB-wdUmxdLfx5DdpqpIQIB7aqGrnshqFbrroVrkRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=Ulxja3F5v3h1gxVNYhgXYU7ntvq7L-Zb1gT7TPjzSs6uSmBIWhfzi4JJ62paHoSH0KeXCA7lWCatkCPGNsQ9wAgtl4fvsqIW0hTtfIAqk0spd3XGRdkYKl3VOr5zPmzF94u7HCP8nHhabdGyWATqmOI4rOTy2yn3oSucvIaNWld49Dkjn7cSaEzGZm10eO1x4CeMc0wWJPBXp21jcLoCPy0DkhQrfP0-BvSfh914wTxp41P42kuJC894YHrYPSWPpWUNRwJh157pHkyQuluzrg3XGbKcQhTpfTp84kwtOkUEbwB-wdUmxdLfx5DdpqpIQIB7aqGrnshqFbrroVrkRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چین ۹ ماهواره را با یک موشک به فضا پرتاب کرد
🔹
طبق گزارش رسانه‌های دولتی چین، این کشور ۹ ماهواره را با موفقیت با استفاده از موشک «لیجیان-۱» به فضا پرتاب کرد.
🔹
خبرگزاری دولتی شینهوای چین گزارش کرد که این ماهواره‌ها عمدتاً برای پایش محیط فضایی، پیشگیری و کاهش خسارات ناشی از بلایای طبیعی و انجام آزمایش‌های علمی مورد استفاده قرار خواهند گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/463192" target="_blank">📅 14:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0401ffdc.mp4?token=mbj9T2Wuyul4Tn7YXy4_TikTOysDqkiQaxL4VopV0o-hxaCxACTuhInGpJAYmj4lb5azc_OZaxu2ME8CFQeGHE4I6-33YKriMB14MpNfgjJuUMEwpuSdTwn_AqP4FZmuq23C0YeF7bB5Mz5WGJHV5O3CVKG5IWOBJxUM2TQ3UYITq9a7f7FqwV8XcMTfFts_0ReN24ZBoT0SnPeILjILfxzmNTUBajxBw1_mbCThXsIVHCyv6sNKfPNUwbT_yYhN8GK9nnDFums4AH22HBQQvxgUqjj-XWtFi7fC9ih8ZqtNu9LqEELUXssRSMcbpr66VzObR11X3NjxDICfYCbRLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0401ffdc.mp4?token=mbj9T2Wuyul4Tn7YXy4_TikTOysDqkiQaxL4VopV0o-hxaCxACTuhInGpJAYmj4lb5azc_OZaxu2ME8CFQeGHE4I6-33YKriMB14MpNfgjJuUMEwpuSdTwn_AqP4FZmuq23C0YeF7bB5Mz5WGJHV5O3CVKG5IWOBJxUM2TQ3UYITq9a7f7FqwV8XcMTfFts_0ReN24ZBoT0SnPeILjILfxzmNTUBajxBw1_mbCThXsIVHCyv6sNKfPNUwbT_yYhN8GK9nnDFums4AH22HBQQvxgUqjj-XWtFi7fC9ih8ZqtNu9LqEELUXssRSMcbpr66VzObR11X3NjxDICfYCbRLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت ۱۰ داروی بیماران خاص تحت پوشش بیمه که از نیمهٔ شهریور صفر شده بود
@Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/463191" target="_blank">📅 14:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463188">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
هشدار قرارگاه خاتم‌الانبیا به آمریکا و کشورهای منطقه: اگر خطا کنید هدف حملات دردناک قرار خواهید گرفت
🔹
براساس اطلاعات دریافتی، آمریکای جنایتکار درپی پوشش شکست‌ها و دست‌یابی به دستاوردهای کاذب در جنگی که با اتکا به دروغ و صحنه‌سازی صهیونیست‌ها آغاز و با فریب و حیله استمرار یافته است، بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
🔹
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
🔹
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.
@Fasrna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463188" target="_blank">📅 14:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463187">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qg-Ss3QUqDl3kdIGsc-IQRcsZdEyHpeMGTaiYm6K1DPyqAsmp7D9Pj7X9_xSSWyx_hQYPrpJD8P91URR1SECE-T9zqvRYP0KfeyAnqHcEypH4vjAY_JLaZp0q3KZXeMfl6OF9oS2ValRKM7ds-CwKYTnDmQ_sEQaw08vt6vdRqbAKcZ1wJOu11vruf3vaERadxyUnoILEdxCYwD0uaW5EundGY_FNMEHLK0Nwqe5UDnvD7H8KS0flkXamjaRs3fVCMf9hk4PCrWMTt64XXzF_BXK2fYGTv_9R8z-0gCkkJ7uqg79NuiICyoIeoH6kr28_RMrym60xSKRLIF8xHGgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهاد مجیدی، گزینۀ غیرمنتظره مالک نساجی برای نیمکت
🔹
پس از جدایی مجتبی حسینی از نساجی، گمانه‌زنی‌ها درباره گزینه‌های جانشینی او آغاز شده , در این میان از سعید دقیقی و محمد ربیعی به‌عنوان گزینه‌های اصلی هدایت نساجی نام‌برده می‌شود.
🔹
شنیده‌ها اما حاکی از آن…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463187" target="_blank">📅 13:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463186">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh0J4gJFP0D7X1encWaLOgiWpsPFvnXPK3LApreheuN-o8NVLKy42EUVHSxO191J_K1apwq98pKDe_1W5PgsEsQde4J12xS2FSmKsbtGjJWbjNcqihvawYi_SThTjqBKjzf6oj5mX_ywjT9lPFLWJ3GKXibwGbP2b7hB4b2MQk_fCGzHg1iECDTnTeC0MKiRlM0RxDw0Xi1D4kqCK5thpDA2LlZS7y6yo7z1tUM-b9QlmPSWxPM4Q2MgUAbd9R7fP1Tr_8SB_Vpi9tp12N7W9enugq6kAGyhJzmdHVEZ_4bqdVYV9j_ISi92wHvEUtbRuzt8xFvyXlgx1LEqx_hAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار شریف: سرنوشت صدام در انتظار ترامپ و نتانیاهو است
🔹
مشاور فرمانده کل سپاه: دشمن پس از شکست در نبردهای میدانی، مجدداً به اهرم‌های تکراری تحریم و فشارهای اقتصادی روی آورده است؛ مسائلی که ملت ما در طول ۴۷ سال گذشته با آن‌ها زیسته، آن‌ها را مهار کرده و از آن‌ها عبور کرده است.
🔹
اکنون بحران قیمت حامل‌های انرژی در آمریکا و اروپا به‌دنبال این جنگ، غربی‌ها را وادار به پذیرش شکست در مقابل مقاومت ایران خواهد کرد.
🔹
به برکت مقاومت و شجاعت مردم و اطاعت از رهبری، همان سرنوشتی که برای صدام و رژیم بعث رقم خورد، در انتظار ترامپ، نتانیاهو و همۀ حامیان آن‌ها خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/463186" target="_blank">📅 13:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463185">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwJkcoTMUxzENTA7kPJWGtJs5t_LHdXHFWefdsvc0pgCTR3_eXC0SmSpvAASssfPIdGMQIaT9Kyqei8cJd5E1Kgoxjt3NyOmFXz_fN6uWTal2ufn374XoqRcvNtCPZ_LqkOHOJKFwXywQ4c2QfWAqBtRTvBoykY2igIkkCvnKpzyZgNRtlbjr1BilHCj3p4h86U0TM5ps9sYLIe3rU4XhQTY4JqaSR6W4xTviuQahBVZfM9JxK3Jxk2f4GtstKTEKQgt2xPOoTOjp-6GvvNbRE0G-NBNmpBLzAgpmZocG0zlee7mY4H0lnau_udQLu7FzOY6mYGrqUEVmPm8mjAKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بازسازی لگوییِ پیروزی‌های یمن، از المخا تا باب‌المندب  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/463185" target="_blank">📅 13:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463184">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWV3-ybEv7qv_A9TKvaCIvyRTZd_yptEIkEiiGVM0b6WIVSV58G5v_sQ4vLr_fZJeuXZFSJzir3EyNydCrNJkb8Fl68_U-TszOo-ZCRTHvPUuJCa2n8kzuHYpRe0wx98ITxc14keBxiDDn5NU6ZTrTgebNXKbQrdM9r8ok28VIAHc0Z5sEYVYlasCJHR6LFD1KweU_Y8XoIij7PeTEoP3X1-YmCGMV923Lku8vmoTARiyw9eZ53gRsDr18ain0vbA8XTe0hcv0GJDKWP_bqFPkxLffDnQMFo2JhnQCzEYSMn3fc3sQetSaXan0nDyMNDYQs-UvK_Kv73aZHr1bJdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد دولت از شرکت‌های دولتی تقریبا هیچ بود
🔹
طبق اطلاعات رسیده به فارس با وجود برنامهٔ دولت برای واگذاری صدها بنگاه، درآمد حاصل از فروش شرکت‌های دولتی در ۵ ماههٔ ابتدایی امسال تنها ۳ درصد رقم مصوب، یعنی ۱.۵ همت، بوده است.
🔸
این درحالی است که کل درآمد پیش‌بینی‌شدهٔ امسال از واگذاری شرکت‌های دولتی ۵۰ همت بود.
🔹
بررسی دیوان محاسبات نشان می‌دهد ۱۳۴ شرکت که ۴۰ درصد شر‌کت‌های دولتی را تشکیل می‌دهند، در مجموع ۴۷۲ همت زیان دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/463184" target="_blank">📅 13:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463183">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2KvlfNdLwKRMLTxDtt_z5JN_oKWR0_dnyxMVODHmNGCDqd7F7JB0383kFa4aG1td7jGPy7PjqAyhDw6_Fn-UTxkLri-NDWRA_Q127ENBiF3VeC88Eq_1Tr7BolK77nhPbeElvFIwwS31dJ337KPXF5y4zTdEhj97somtpGWAXoskMkhNUmDMBKVBqlNw6XKNczHVYG7ZV5aTMXQNolg7vyXvcccvArVeua-TG7kmqLju4L-uFgOpOGIcRlmfUgPo21-wvtYhakAy9KGfF_jh35ZeQf4EYAVkY9h8GsDyZ9AkxyZEe9g5LvNVz37TjlHRtHJ1VZ8smJt0mPyFEyzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام ۳ کانون عملیاتی وابسته به گروهک‌های تروریستی
🔹
وزارت اطلاعات:
با مجاهدت‌های خاموش سربازان گمنام امام زمان(عج) و با بهره‌گیری از گزارش‌های مردمی، عوامل سه کانون عملیاتی وابسته به گروهک‌های تروریستی مزدور دشمن آمریکایی صهیونیستی که قصد عملیات ترور و تخریب زیرساخت‌های اقتصادی را داشتند در ۳ استان کشور به هلاکت رسیده یا بازداشت شدند.
خلاصۀ موارد اشاره شده به شرح ذیل است:
🔸
۱. هلاکت عامل عملیاتی گروهک تروریستی تجزیه‌طلب که مترصد ترور یکی از فرماندهان حافظ امنیت در شهرستان پیرانشهر بود.
🔹
طی اقدام پیش‌دستانه سربازان گمنام امام زمان (عج) در اداره‌کل اطلاعات استان آذربایجان‌غربی، یکی از عوامل عملیاتی گروهک تروریستی تجزیه‌طلب که قصد ترور یکی از فرماندهان حافظ امنیت در پیرانشهر را داشت، در کمین سربازان گمنام امام زمان(عج) گرفتار و در درگیری با نیروهای حافظ امنیت ث، پیش از انجام ماموریت شیطانی خود به هلاکت رسید.
🔸
۲. به‌دنبال رصدهای به عمل آمده توسط اداره‌کل اطلاعات استان البرز، یک مزدور وابسته به دشمن آمریکایی-صهیونیستی به نام «امیرعلی_ ن» که در راستای اجرای دستورات سرپل گروهک سلطنت‌طلب وابسته به سرویس جاسوسی رژیم صهیونیستی، قصد انجام اقدامات خرابکارانه داشت، با الطاف الهی و مجاهدت‌های سربازان گمنام امام زمان(عج) در آن اداره‌کل، دستگیر و از اقدامات خرابکارانه او پیشگیری به عمل آمد.
🔹
این متهم با هدایت و آموزش‌های مختلف گروهک سلطنت‌طلب، مشخصات برخی افراد هدف گروهک و مختصات برخی از اماکن نظامی سپاه و بسیج را برای دشمن ارسال نموده بود.
🔹
تخریب پایگاه بسیج در منطقه، ربایش و اقدام ایذائی نسبت به  افراد، آتش زدن خودرو و.... از  اقدامات برنامه‌ریزی شده توسط گروهک تروریستی برای این مزدور بود که به لطف الهی پیش از اقدام، پیش گیری به عمل آمد.
🔸
۳. در ادامه سلسله عملیاتهای پیش دستانه‌ی سربازان گمنام امام زمان (عج) دراداره کل اطلاعات کرمان، یک هسته سازمان یافته و مترصد گروهک‌های تروریستی وابسته به سرویس های جاسوسی دشمن آمریکایی-صهیونی شناسایی و اعضای آن پیش از هرگونه اقدام ایذایی، بازداشت شدند.
🔹
این هسته دو نفرۀ تروریستی از سوی سرپل گروهک ماموریت داشتند یکی از تاسیسات زیربنایی و مهم شهرستان بم را منفجر نمایند.
🔹
همچنین از سوی گروهک به اعضای این تیم ماموریت داده شده بود که برای دیگر اقدامات مسلحانه و تروریستی، این هسته دو نفره‌ی تروریستی از سوی سرپل گروهک ماموریت داشتند یکی از تاسیسات زیربنایی و مهم شهرستان بم را منفجر نمایند.
🔹
همچنین از سوی گروهک به اعضای این تیم ماموریت داده شده بود که برای دیگر اقدامات مسلحانه و تروریستی، کسب آمادگی نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/463183" target="_blank">📅 13:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463182">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464f9314.mp4?token=WTpS-7Cs-Di6NNrDBbOWtwlt9i9b0bVAXyfLtEGwqXyqph8CAPAo_IdVP9JjN_NBaN--x5qOvWKd2meyK6JEcByDyTdmUq2A5AIPHEAZ7WsEcx55tlIGyd_qoo23ZDY93QdcBuyER3WPdunIMmKrw4BSBXu_3Kwr_TLcJXWEjDron6NbpPbr5Ot-2HEr-xD4tV4Ega_HhzH5_h-oWkDymvJkv90AEPgvKfE0XoNLPh10a8yfulwVUybAtCf6lfjoD2_TtkxLXvYg9WdKsUigM-5cmBZQ0nE6QltSkxPX3gMM3jSI74yz8d911sMJj7MQx23ksWYUU7LVb5HotnLf_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464f9314.mp4?token=WTpS-7Cs-Di6NNrDBbOWtwlt9i9b0bVAXyfLtEGwqXyqph8CAPAo_IdVP9JjN_NBaN--x5qOvWKd2meyK6JEcByDyTdmUq2A5AIPHEAZ7WsEcx55tlIGyd_qoo23ZDY93QdcBuyER3WPdunIMmKrw4BSBXu_3Kwr_TLcJXWEjDron6NbpPbr5Ot-2HEr-xD4tV4Ega_HhzH5_h-oWkDymvJkv90AEPgvKfE0XoNLPh10a8yfulwVUybAtCf6lfjoD2_TtkxLXvYg9WdKsUigM-5cmBZQ0nE6QltSkxPX3gMM3jSI74yz8d911sMJj7MQx23ksWYUU7LVb5HotnLf_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/463182" target="_blank">📅 13:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463181">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133a7497ee.mp4?token=WB4oQsXD54UzNRF3qr-yjJpzuxW5CT6gz-ke8sZn1nBKekgdAg7i6inEjzTOaQ1dMP2w5eglaFpyO2QasjHBK-dC6tj7YvFu16ve8h3mxv_taS2DWxxTg-pyUojrXDPK12nRg5UsVUCjMAVToUlAe7Vl_1uZfPPDms-siCpfFWHHB8QyGcEC8ERqRco8d-hJ-JfN29TgzTyCM8yAGbUMVJqL71GCAwN8gZKUfT0vDMd5s4QdAT0u3xOGtuhOe2N3Ll2ecdKXfjcae_QbXSyapOIVYIRO4X5EF9GdFaxMYySOAjvhTWbSNtgW8O2OFPShCmJvbusD_EoSvLZ5KPMg46n9evwA9WFt2W7SCCi73KSMqKw3ACDull7agOGl9N_4QEhm6UpaszDycXl2GNvtwBiblRSNPvbQ3KifumZjQndPlfpiYMAWO38zDSjcXO3WJdvOu4ZyUnMbZGpCOd5OLH7CWUi4iNp6nfGtv_dXLQ0IecdiyvX4dmYF5POzor4cUuc_vpz5f00Ql6otQFZdZd2vYGNSeOZWZTJ2UKn9V3sAt8Ry_CI-YCgLrjNpCMq5SyxcJaAHWLzvR_OaJcLMY3HwIdRJ7LaHFF92B2cfSCu2mXH7dfhMbQpvyZjb9GjvQAy99BakA4jp-N2ejCo_Y-LrI2OeHUryk1z7Xc-c3Fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133a7497ee.mp4?token=WB4oQsXD54UzNRF3qr-yjJpzuxW5CT6gz-ke8sZn1nBKekgdAg7i6inEjzTOaQ1dMP2w5eglaFpyO2QasjHBK-dC6tj7YvFu16ve8h3mxv_taS2DWxxTg-pyUojrXDPK12nRg5UsVUCjMAVToUlAe7Vl_1uZfPPDms-siCpfFWHHB8QyGcEC8ERqRco8d-hJ-JfN29TgzTyCM8yAGbUMVJqL71GCAwN8gZKUfT0vDMd5s4QdAT0u3xOGtuhOe2N3Ll2ecdKXfjcae_QbXSyapOIVYIRO4X5EF9GdFaxMYySOAjvhTWbSNtgW8O2OFPShCmJvbusD_EoSvLZ5KPMg46n9evwA9WFt2W7SCCi73KSMqKw3ACDull7agOGl9N_4QEhm6UpaszDycXl2GNvtwBiblRSNPvbQ3KifumZjQndPlfpiYMAWO38zDSjcXO3WJdvOu4ZyUnMbZGpCOd5OLH7CWUi4iNp6nfGtv_dXLQ0IecdiyvX4dmYF5POzor4cUuc_vpz5f00Ql6otQFZdZd2vYGNSeOZWZTJ2UKn9V3sAt8Ry_CI-YCgLrjNpCMq5SyxcJaAHWLzvR_OaJcLMY3HwIdRJ7LaHFF92B2cfSCu2mXH7dfhMbQpvyZjb9GjvQAy99BakA4jp-N2ejCo_Y-LrI2OeHUryk1z7Xc-c3Fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/463181" target="_blank">📅 13:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463180">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBX3-fiotyLq3rtAOtOeR5fSagifBiYk_QleoXIwtGss0YZ1TFxDOQO1sdhoUYHdBKWI8CYcczeU8OjIDZZmXY4dNi-2AV3uNxw-W48A9J9SWkxatPIDHfOyXF9PGb7ZjglUeSup-uuDb3Rm0E7UstvslkK066n0hA0N1qzmjXr6R1AlvEfim6hUZ3j4EhTyw8-8Lz19VhBtf7Tbgdt-9Te3bG6QwNNyp93uh1PPqCnp6VxMslu0pqc0MxPVTjtlHC8Ih3th9ziere48-LKGCuOv80jmk3ZdYZ8t3EYYlbyPqxfQHTU7Xs_AyNNMT3V92glq0x26LyMJnZYy-nfdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از ۷.۳ میلیون هم پایین‌تر رفت
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۵۷ هزار واحدی به ۷ میلیون و ۲۹۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463180" target="_blank">📅 12:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463179">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477de95318.mp4?token=f_EKZ5xQoTS4cjvbkrd1GgF_5DloaNIAb3xpa0SJ933vkpumzfddckKH-EbJiCZsaMPkgAdjn-t0kFc0LTJFs-C82BDCmHybdYBwi1ixg5wqcS8Jy-ky8K0YD3d2lFFJhuIQthgxvfuJ7cCSgjhavJ8F11gQASIo16D1bSSuh81Dxpwccj9Jt-P8f4hAXF6XIQT_ZZ731IuTxbpq6qO_PrF_Zp7ZHtbdHwGpQxTLqtqFNZ1aAxQuSE928wUWJPYD-HTvADF6-AoQJ4GNOKffKqADS417Crkpb5kmFBNAhEusbYf34geCl-bvWej6pFemJZcY81Ns3FJAtQW_w83IFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477de95318.mp4?token=f_EKZ5xQoTS4cjvbkrd1GgF_5DloaNIAb3xpa0SJ933vkpumzfddckKH-EbJiCZsaMPkgAdjn-t0kFc0LTJFs-C82BDCmHybdYBwi1ixg5wqcS8Jy-ky8K0YD3d2lFFJhuIQthgxvfuJ7cCSgjhavJ8F11gQASIo16D1bSSuh81Dxpwccj9Jt-P8f4hAXF6XIQT_ZZ731IuTxbpq6qO_PrF_Zp7ZHtbdHwGpQxTLqtqFNZ1aAxQuSE928wUWJPYD-HTvADF6-AoQJ4GNOKffKqADS417Crkpb5kmFBNAhEusbYf34geCl-bvWej6pFemJZcY81Ns3FJAtQW_w83IFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ سوژه تمسخر نخست‌وزیر کانادا شد
🔹
در بحبوحهٔ تنش‌های تجاری آمریکا و کانادا، نخست‌وزیر کانادا با تقلید حرکات دست ترامپ، حضار را به خنده انداخت.
🔹
کارنی که پیش‌تر بارها هدف طعنه‌های رئیس‌جمهور آمریکا قرار گرفته و ترامپ از کانادا به‌عنوان «پنجاه‌ویکمین ایالت آمریکا» یاد کرده، به‌تازگی همزمان با تشدید تنش‌ها با واشنگتن، بر تقویت روابط کانادا با اروپا تأکید کرد و پنجشنبه در سخنانی در پارلمان اروپا از پیشنهاد اتحادیه اروپا برای پیوستن اُتاوا به‌عنوان عضو وابسته استقبال کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463179" target="_blank">📅 12:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463178">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هلاکت یک صهیونیست در تیراندازی در کرانه باختری
🔹
در پی عملیات تیراندازی در نزدیکی نابلس در کرانهٔ باختری، چندین صهیونیست مجروح شدند و اخباری از هلاکت یک شهرک‌نشین صهیونیست هم گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/463178" target="_blank">📅 12:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463177">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ممنوعیت استفاده از سهمیۀ ۲۰ روزه تردد رایگان در هفتۀ اول مهر
🔹
شهرداری تهران: استفاده از سهمیه ۲۰ روزه تردد رایگان در محدودۀ کاهش آلودگی هوا از ۱ تا ۸ مهر ممنوع است.
🔹
تردد ناوگان پخش مواد غذایی، دارویی و حمل اسباب منزل از ساعت ۶ تا ۱۰ صبح از ابتدای مهر ممنوع است.
🔹
همچنین در هفتۀ اول مهر هرگونه عملیات عمرانی در سطح شهر که باعث اشغال سطح سواره‌رو می‌شود، لغو خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463177" target="_blank">📅 12:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463176">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph3Z7DhtaJWt1Jp3QgiCoYzdJurMOdJ6ATSE1yHjuiN6_DBmQX7vxBJQWGXaEaOyQY82Yhr4OjsXuU5FiOnPWfjMRcTq7PPf7Wbk-dtdAqvMPlrNAZ2qQx63xca24Rc29A3kPETwCdc047zT0DDVb7FxOMq7QGAe9XW8gA5IB7H0Qj51beLQGgKdtjt-T_neiV1QdPNShgtqZClyxdF4QdiyEbNOG6IWSJ1s99HV_6MmiCADanffYr8fCHwOytr3aVry72i2CEG09E4csNgVOWJBUFsmLwh8yhkAWBhTwvbVvomVw1CDc-8-Pe-F1XVtKdgAUEHpRrlDUvn8sm9dXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای رئیس کمیسیون قضائی مجمع تشخیص ماند
🔹
در جلسۀ کمیسیون حقوقی و قضایی مجمع تشخیص مصلحت نظام، حجت‌الاسلام محسنی‌اژه‌ای برای پنجمین سال پیاپی به ریاست این کمیسیون انتخاب شد. کدخدایی هم نایب‌رئیس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463176" target="_blank">📅 12:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463175">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b1d8a308.mp4?token=SGxRh6DRuqP89aSqEydFBsw2RGEADStOjdRUWqJRoRFkHcATHj__S2CzcZLO6Sksy4bISa6fak0VweqIM43PzWaGrPK8KTbrqfPDwFhUo7ItvhqqofxyQIVd47pcbSl30e3LjklHrEhb6G-yVYU0IGB-Y6Rl_2krEqxzfIh5wBqOOnE39sR4ZhPQDfhbXdOcJr2M7z5oBYU3BTJC3vM_s-Tk5O2a02GnUbtoJIzkBevQ8DLPBPvQs5LSGGsufEVrFrDANx4wPMjeQgQCi0MWAilRJMzsmBMzrfq3kb-lHVw9RsXHZGu8I9K0d1Ek96cNqjijSOLphvCF7423nvoPdixeCFNev84TxlS0CFu0VNn2aONH103C9SwOUS3uBxbBwhIxneyHPvTEn1kMIOisa3KuYOx1ngqgtmzfo9CYELDuqC9JIwxU2_E164WmJIcONui2mKN26z9-vsP2b1sk0D3VmZFjbOLbf07ewjAgmEqzDE-qTkXD9HOAI7RAA6_r7SHvB5tnzP5_HnXuThHo370oCtQxhM2imyfjPr_9NtwwpuVJRNmj4qlHFCcWdlvag00RzHmYNQG7htWP0rkXmw48VUSPpAjTNRFFfhmtwQZjgcWElqhYck9Z1xXtOjcuzTLKYJG0ptEKOugmCdQNTSX9nYgoATTwsvmS4W7XK4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b1d8a308.mp4?token=SGxRh6DRuqP89aSqEydFBsw2RGEADStOjdRUWqJRoRFkHcATHj__S2CzcZLO6Sksy4bISa6fak0VweqIM43PzWaGrPK8KTbrqfPDwFhUo7ItvhqqofxyQIVd47pcbSl30e3LjklHrEhb6G-yVYU0IGB-Y6Rl_2krEqxzfIh5wBqOOnE39sR4ZhPQDfhbXdOcJr2M7z5oBYU3BTJC3vM_s-Tk5O2a02GnUbtoJIzkBevQ8DLPBPvQs5LSGGsufEVrFrDANx4wPMjeQgQCi0MWAilRJMzsmBMzrfq3kb-lHVw9RsXHZGu8I9K0d1Ek96cNqjijSOLphvCF7423nvoPdixeCFNev84TxlS0CFu0VNn2aONH103C9SwOUS3uBxbBwhIxneyHPvTEn1kMIOisa3KuYOx1ngqgtmzfo9CYELDuqC9JIwxU2_E164WmJIcONui2mKN26z9-vsP2b1sk0D3VmZFjbOLbf07ewjAgmEqzDE-qTkXD9HOAI7RAA6_r7SHvB5tnzP5_HnXuThHo370oCtQxhM2imyfjPr_9NtwwpuVJRNmj4qlHFCcWdlvag00RzHmYNQG7htWP0rkXmw48VUSPpAjTNRFFfhmtwQZjgcWElqhYck9Z1xXtOjcuzTLKYJG0ptEKOugmCdQNTSX9nYgoATTwsvmS4W7XK4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند نکته از زندگی امام حسن عسکری(ع)
🎙
حجت‌الاسلام دارستانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/463175" target="_blank">📅 12:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463174">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46656a27f.mp4?token=EV1480Tf6A-0Am2vNjQ3n6BwuyAkI9at1kxst8723pE0g5Uzk1UfhdNwb1jH-edgpQ7bAgAmeptUv2lQbW-p32ket1YXMFgplFgkKSzq3CVsPaf-zkPDihVR8sgNivKXBVEWu6XpFKIf1578DLTP8lNmah3Isfzy69y2oPXWkp_o-ygkSvgBzqrTJbkZactbfDhsoPYsi8IR7FsJU3n_KFSLZ0DdiT-hVoHROoNeSTjHkuN6Q_fFP0yGLcoaR9-haOcRnEcrRaScM3bJ97FsEWP9MzwQl6626lbz_KQzGHnScyW3m73yz3fDS54b8ZSGpXZ1fVNL4_OzN47oBoSOPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46656a27f.mp4?token=EV1480Tf6A-0Am2vNjQ3n6BwuyAkI9at1kxst8723pE0g5Uzk1UfhdNwb1jH-edgpQ7bAgAmeptUv2lQbW-p32ket1YXMFgplFgkKSzq3CVsPaf-zkPDihVR8sgNivKXBVEWu6XpFKIf1578DLTP8lNmah3Isfzy69y2oPXWkp_o-ygkSvgBzqrTJbkZactbfDhsoPYsi8IR7FsJU3n_KFSLZ0DdiT-hVoHROoNeSTjHkuN6Q_fFP0yGLcoaR9-haOcRnEcrRaScM3bJ97FsEWP9MzwQl6626lbz_KQzGHnScyW3m73yz3fDS54b8ZSGpXZ1fVNL4_OzN47oBoSOPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرماندار مریوان: یک محمولهٔ سلاح قاچاق در مرز باشماق کشف شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/463174" target="_blank">📅 11:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463173">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYrlN-I6ZpvWWxxS84zeL5eNSQ73A5YukMsNMMq1qN0nGlMYieUHYK5SKY31m9uj7oxS2Z7CQBEjU_4v3rEdJ56Mhhcd-tulnOFOzIhtv-BU9jrBEdXEEsKF5yNE1X0Xjakriwy0mmCTizqqaLDaLZTO0lkdND2e2Xp8QFfmOD72GEr3Scz_aME9uOKmDtwI3Lwi-Cwi-vjigEgkGzJ8xK8P-t4ZbVQF73DYq7MUZiuMKR1hv5tcoBrgReNqGFYTMe4AzTqh1Lopo4lE7dOORK_JIMfQT0Yh3mD_6U2-eqBn4leUAgpHCdGO01tJPQdJtBMVNAw6cTo4dyGz-zt27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک مزرعهٔ ماینر در البرز
🔹
شرکت برق البرز: در یک مزرعهٔ استخراج رمزارز که در پوشش صنعت فعالیت می‌کرد، ۳۶۲ ماینر کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463173" target="_blank">📅 11:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463172">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1113bc549.mp4?token=nAXdvCD5BGEZI4YlRibK6V1Xk0Weq6w2XVIiov6Cgg-M0S2kbWhyeim9GmFGTG-daqxUjGTM0VKD_CzILj2iKHDwzFYpqtUFUsIE2s7QWzStmNM8Y1bjMGWxIfRy3iFlwaPZ3nxIlyN3hbmVLyCtMjHlOj7MJN23huObY0bpY_tGIKNrs3i6ZSTkisjw7NpjcmgVxe3bbw2_xAR4PDxRmZx4r1WO503sb28vODbTdlVhPkapUk98hI4jtST6WXkIoy4M6_lxWPK4XgyRmrlwzxekksz11TtLq7IdvxqK40Iuo9nPzVpbeosPl0cCDMUr5fJH5ErHR6E4fsrHFDKFwKMcGUM8cDBrAecNUQ66YHeUFJ5faGC2J5dqllP0ciCgconeQbnFBvvTcQ6KVHcV29Ncsw4BqRE6-FveE3nD135CKpEWm3iKYP-Gnxw0l69qbZk-pIP6mbCDwFYf8MLQBKg-wLM-iTmOl1w0AzXr4ILTChuYY7UlprCqCiS9GoqTc4uscFCS1CdK2edC_V2mmnfH90S8ulYpBJ_iAcwP7-xpnSqN_lPVoll8gVm_y4bOE0-HAatQQxfgiKkLzA9xueskkJVjGRK_eJ-PH0nctIrbJQQP2ajXqlqCw2NcX4vyAaTEsP7nklpkkvJ41NHHazRf03qzBRDLQxuY24_Llic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1113bc549.mp4?token=nAXdvCD5BGEZI4YlRibK6V1Xk0Weq6w2XVIiov6Cgg-M0S2kbWhyeim9GmFGTG-daqxUjGTM0VKD_CzILj2iKHDwzFYpqtUFUsIE2s7QWzStmNM8Y1bjMGWxIfRy3iFlwaPZ3nxIlyN3hbmVLyCtMjHlOj7MJN23huObY0bpY_tGIKNrs3i6ZSTkisjw7NpjcmgVxe3bbw2_xAR4PDxRmZx4r1WO503sb28vODbTdlVhPkapUk98hI4jtST6WXkIoy4M6_lxWPK4XgyRmrlwzxekksz11TtLq7IdvxqK40Iuo9nPzVpbeosPl0cCDMUr5fJH5ErHR6E4fsrHFDKFwKMcGUM8cDBrAecNUQ66YHeUFJ5faGC2J5dqllP0ciCgconeQbnFBvvTcQ6KVHcV29Ncsw4BqRE6-FveE3nD135CKpEWm3iKYP-Gnxw0l69qbZk-pIP6mbCDwFYf8MLQBKg-wLM-iTmOl1w0AzXr4ILTChuYY7UlprCqCiS9GoqTc4uscFCS1CdK2edC_V2mmnfH90S8ulYpBJ_iAcwP7-xpnSqN_lPVoll8gVm_y4bOE0-HAatQQxfgiKkLzA9xueskkJVjGRK_eJ-PH0nctIrbJQQP2ajXqlqCw2NcX4vyAaTEsP7nklpkkvJ41NHHazRf03qzBRDLQxuY24_Llic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازسازی لگوییِ پیروزی‌های یمن، از المخا تا باب‌المندب
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/463172" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463171">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlaFnictlJwL0UQXtqGv56orTMJp18OmoKGXPKxm0ylFDbog0W4V0-zmdeezGRZzkwwnKT9JWEa8H5vpwl210oL3qOAxYSz17r8VFze3kKBUr9r4m1cKKi5MWN4k6QTqfJVChWF8sCtch4DWA5Eom7_9QqhbJs5NllFCF3mOBZz_pBEKBvCYr8Nh7RUXqcbyZPSbPOxVH3ljF2AhphHy72Hir8ogj9TtUBa5CFWuP3cJRnGHQ6MtQg1G3kVAfhGhqKOyCmgEIEmHhcJCQO2Z78zte6mZOFKPp3Wa8MdNs9emSgoe41ro-qEJ6e4p7uKrJ3U0FeyUwLD71GPB-B8zcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انتقاد دربارۀ عملکرد دولت در تئوری ساده است
🔹
ارائۀ پیشنهاد و انتقاد درباره عملکرد دولت در تئوری ساده است، اما در میدان عمل، به‌ویژه در شرایط خطیر کنونی، با پیچیدگی‌های فراوانی همراه است.
🔹
دعوت از همه برای مشارکت در حل مسائل کشور، یک باور و رویکرد…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463171" target="_blank">📅 10:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463170">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byjdOSd2TGH8-tAoFIH19FMk5WbSPgnQezsH585IiIpHdQnB0_oj6cvP9yjz-BPC6lPWaGPjCDZL6WOLlizRkQX5vWnhh5MH2wsxm8Bp73ZuUQ_hycvRwsiAvKLzDu2L3N3ktbAHmZSNh9hfOje9UiuclXs2DaLnmfCD3EYOYWBVHBcERPVtppLIoNOg-PTGI7xyHnr7EbNsYtV9koPg42qj6VZpj6ULBKMxhafgdq6BsXE-zJ3L6k4ss-xp9CPQS3-j6PwUYcU0i9MkiYIuJUO92h7Afvip8sWhuIrQCPO4aJMFa3wEcCeSLNKrH4DR_JTVM51LzamojdxW_0r8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انتقاد دربارۀ عملکرد دولت در تئوری ساده است
🔹
ارائۀ پیشنهاد و انتقاد درباره عملکرد دولت در تئوری ساده است، اما در میدان عمل، به‌ویژه در شرایط خطیر کنونی، با پیچیدگی‌های فراوانی همراه است.
🔹
دعوت از همه برای مشارکت در حل مسائل کشور، یک باور و رویکرد جدی در دولت است و صرفاً به ارائه پیشنهاد و راهکار محدود نمی‌شود؛ بلکه مشارکت باید به مرحله عمل، اجرا و پاسخگویی منتهی شود.
🔹
امروز دولت با وجود بدهی‌ها و مشکلات به‌جامانده از گذشته، محدودیت‌های موجود در صادرات نفت و هزینه‌های ناشی از جنگ، ضمن پرداخت تعهدات و مدیریت هزینه‌ها، روند توسعه کشور را نیز متوقف نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463170" target="_blank">📅 10:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463169">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378421841a.mp4?token=orXjZENbQzfjNVfwaQr0RKfTISL3JRItNWInGf3h3lb_hVozeZ-u2Svgnz-iU0dQyia-GGnADlF_EEF2jX44HfZIVQ-ost2SIGhsFDDjQQ8bYyJzUKGTNAcTf_awB1opMhV_RI1r19D5jQKU4hWAdvcuJIiN9fS2K-4YIvv-sNF5fNDbnSe_8U2o4iN6ePJiZWQczkGlgQAmHCiuchf87JuJ8peNdcacq1cyxOUvlM2y2j1srZyHObrxMnGmkGU7xIILmyqkXEMHo3vh3OGru86TlwOW9Xb6zK-zD5_j8XUhXl_dMouDGD7yJWSjIHaCxWGxztM3wOxJnQVVDhVyNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378421841a.mp4?token=orXjZENbQzfjNVfwaQr0RKfTISL3JRItNWInGf3h3lb_hVozeZ-u2Svgnz-iU0dQyia-GGnADlF_EEF2jX44HfZIVQ-ost2SIGhsFDDjQQ8bYyJzUKGTNAcTf_awB1opMhV_RI1r19D5jQKU4hWAdvcuJIiN9fS2K-4YIvv-sNF5fNDbnSe_8U2o4iN6ePJiZWQczkGlgQAmHCiuchf87JuJ8peNdcacq1cyxOUvlM2y2j1srZyHObrxMnGmkGU7xIILmyqkXEMHo3vh3OGru86TlwOW9Xb6zK-zD5_j8XUhXl_dMouDGD7yJWSjIHaCxWGxztM3wOxJnQVVDhVyNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ اوکراین به پالایشگاه نفت روسیه
🔹
صبح امروز پالایشگاه نفت مسکو در منطقۀ کاپوتنیا در پایتخت روسیه پس از حملۀ گستردۀ پهپادهای اوکراینی دچار آتش‌سوزی شد.
🔹
پیش‌تر ترامپ گفته بود از زلنسکی خواسته به پالایشگاه‌های روسیه حمله نکند، زیرا این اقدام عامل افزایش…</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/463169" target="_blank">📅 10:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463168">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLM45JB3RfAGOY2qojE3hxNXpY_vXGcbOtsKlxcZJr_qeoM1qg5HTi436n07IbC7n3L9cJni25FXdvuNcJpU83R4Z9KRDQhqflzf8oynWdncHR3ygQH6eJtLraFggFaNZDkbn2Lc6QGXJwEhtqmMurNl_2fYJVfTbA-Er5KQlJnUarIFKMsn-FWwFOw2p4aHV17-nwb0xzdCdqi4VbULDNH0KX96kJw3FZtdHMENl47ewpVIHPzf_ocuYobDq-b5l8iaLyXjz0NAU-NgFeC4Um2c1FLCQH27CbVJ2utdp5svpST-50TuYk9NHuYIasidsiXzpU6Flz91v3Vfw1bLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ حال عمومی آیت‌الله شبیری‌زنجانی مساعد است
🔹
براساس پیگیری‌های خبرنگار فارس از یکی از مسئولان دفتر آیت‌الله سیدموسی شبیری زنجانی، هم‌اکنون حال عمومی ایشان مساعد گزارش شده است.   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/463168" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463167">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npvK5VcVA-ehNejHUlA9X6flvg3QSco1MhEJbIHCjkNJhGmmPy9fLBxaLYWUBhh6aPwB0073Wjum1p6ct27yWEFgcKJoNtOVGRU3qZhzmPHSeV7Pd-QnSw81Auq-q5GAMQgJy5jpVDUMZQKa9jCXTOE6xhF3fkMRXSBe5PFULLvCz9fMfUo9ZuXxJ5pkqBKaejKU0SL82g9U2J2_ouzfY5pg4oL2wLFZC6B7qUPkUjI4-7yuiXi8CAYOfBA9m16lfStldMkhg88HboIMo9YQ99yaLwVmLfQmQ_4ZTbAhFyTJgeZZZlUPN5kxGld-jB5VVWeZX3t7CrxR8-9vDvCJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«شفرونی» بعداز ۸ روز رفع توقیف شد
🔹
برنامه «شفرونی» که ۲۱ شهریور با دستور قضایی از ادامهٔ انتشار در فیلیمو بازمانده بود، پس‌از چند روز به جدول پخش فیلیمو بازگشت.
🔹
«شفرونی» پس‌از پخش ۳ قسمت از فصل جدید، در پی اعلام جرم ساترا و ورود دستگاه قضایی متوقف شده بود.
🔹
حالا قسمت شب خوزستان این برنامه در دسترس قرار گرفته است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/463167" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463166">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a76ce8106.mp4?token=CUS47fw1Z6ADV0tG-zSLoJFgQzLqfAy693GLGf6v3Mn3Rn2hCRQKL5ZI3kaJLtrLpPs_bXwZ_UyWUwLzKTjiFGI7dMJxz5NJ_q64ZU3ZCAGLgSQjOUwTtf8XDAvpI3a_jMB61lkCywAkHP400Ld31rD48KAERK811oQ-JjYk-AlzT23MTLvFT7JunA29lP3N-fv6stmdL-LuqDik_ztYngftX550yJRJgK55eVfv6-A9Aj76peUPXF196EXW0TTVPOcuO7NcZBAaJaGyBp3-myej7nFr4Lw-g-4iK3lJ_LHd76gAtoExd6QZqrCpvdN6DfXB8jyULXtaGkTOqkrTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a76ce8106.mp4?token=CUS47fw1Z6ADV0tG-zSLoJFgQzLqfAy693GLGf6v3Mn3Rn2hCRQKL5ZI3kaJLtrLpPs_bXwZ_UyWUwLzKTjiFGI7dMJxz5NJ_q64ZU3ZCAGLgSQjOUwTtf8XDAvpI3a_jMB61lkCywAkHP400Ld31rD48KAERK811oQ-JjYk-AlzT23MTLvFT7JunA29lP3N-fv6stmdL-LuqDik_ztYngftX550yJRJgK55eVfv6-A9Aj76peUPXF196EXW0TTVPOcuO7NcZBAaJaGyBp3-myej7nFr4Lw-g-4iK3lJ_LHd76gAtoExd6QZqrCpvdN6DfXB8jyULXtaGkTOqkrTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کرنر خطرناک برای ایران که گل نشد
⚽️
ایران ۰ - ۰ چین @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/463166" target="_blank">📅 10:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463165">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy8YaUs82CsQyRb5U3qcPcWkGxJD5abq4ocTsyAc3pdNevwo8GySInF7H0B2jyIJEw-z1F3OEegphRsps1g9h9ziTl6M4MArmswWQZsCNdu6ihBDG8UyYGKppmoPBA1QQdfDYhrBIfxgQqfJLhQE2bsN9JXR0FPD8BjKFSVhAuMVV3vqQwLCMfdlh3bkpSQpRe1_omK-QgC_2H-39cyAjmTp6LYnFepFPqq033xClNIJuFUA0UgJFtZKvBHWSsl7HxEajNljx0DgUKixBzyu0FV9OzLeDZyUnQni1BlDJVBY0LaCKPwavlj1VpSLPV5ThRABrutGtiSX21dCySEr9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیرعامل سازمان مهندسی و عمران شهرداری تهران: بزرگراه یادگار امام به بزرگراه ساوه متصل خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/463165" target="_blank">📅 10:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463164">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXvGLwZ3Imf1UIjYIo42XFY-tXiXhgEdhvu20PPrHbYzc-IdIZzL3m9paxdEDsS3tUd8Vge1I768NlVoPF2JRZAQRAm49nnp_4k5EoxjxewLuUon4ppVI2Aa68a78YEll4QWU-LpRB3vMMd3rNQzKxioO4J8BvjzmNpGB0utcCo432bXS2uvbKraoa7rSs6l6JtJro_MFasq17_xQfYYoEsPChbBcaz4N5Q39XgwhXAR2Ayw0jla4Z6K3yndE9xOWo4PHkmBsgAbocc0DZaEzbvgQmESehWqvQ36suavCAgKvSQxnRca8j9cFLbnGmNQQYX8fBZgzmWYY_c70DCOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های حوالهٔ ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۶۶٬۶۰۷ تومان
🔹
یورو: ۱۹۱٬۳۶۸ تومان
🔹
درهم: ۴۵٬۳۶۶ تومان
🔹
یوآن: ۲۴٬۸۶۰ تومان
🔹
روبل: ۱٬۹۷۸ تومان
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/463164" target="_blank">📅 10:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463163">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فرمانداری دزفول: صدای انفجار شنیده‌شدهٔ دقایقی قبل در برخی نقاط شهرستان، مربوط به امحای مهمات بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/463163" target="_blank">📅 10:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463162">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b183bb2e0.mp4?token=cfvppSxfLUlpEmd3pxjAmJSTBn0TR986g2YCXf2nCvM3D1uZYsJqCumMLR5qye28ct_P7yZc2xHIhO9wnOD5VKTLszI1TXd0jFcTyWWj0p7FSJquCXf1ibeNY5yKWi85fgAnjDN4eF2sWaSe9bNqU0rROcJPJbl8UOEY8RjCGpFdB9nksqcE3vJ9iN0xocNNUoOphYhC_yq4F1D8bDqqW7eVrwgfHkQcgev7Hx2gsu-pnEjJRPyWKCEYnagvVj1lWdDPc70pRv8-V6enyv39lk305xrbJSWWWLhhuxQaZagwlMY-Q-M-PGRiyp7QyzgxIXFF22NgoS35AGUdHmYXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b183bb2e0.mp4?token=cfvppSxfLUlpEmd3pxjAmJSTBn0TR986g2YCXf2nCvM3D1uZYsJqCumMLR5qye28ct_P7yZc2xHIhO9wnOD5VKTLszI1TXd0jFcTyWWj0p7FSJquCXf1ibeNY5yKWi85fgAnjDN4eF2sWaSe9bNqU0rROcJPJbl8UOEY8RjCGpFdB9nksqcE3vJ9iN0xocNNUoOphYhC_yq4F1D8bDqqW7eVrwgfHkQcgev7Hx2gsu-pnEjJRPyWKCEYnagvVj1lWdDPc70pRv8-V6enyv39lk305xrbJSWWWLhhuxQaZagwlMY-Q-M-PGRiyp7QyzgxIXFF22NgoS35AGUdHmYXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصدومیت عباس کهریزی که منجر به تعویض او شد
⚽️
ایران ۰ - ۰ چین @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463162" target="_blank">📅 09:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463161">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c466f62b4f.mp4?token=jfZk7kaZfZCMxiuvJjdpYnbG6RRgWdvoD5cZyC8d3KWMWhWhLmRjoXnyrvYUoInjM49Qlyc_7h22NmAY4DHdkZYH7fjFzEzrLfG11jRpKWsZOeC0VVwszbor4CW5CsStH3k_fCgxvH-9XeWlL2_aBdxkysdHg5aK-jllL6uw_RagvadC4WTOYW-yDpVwev9vnQWTPmylpcL-g8E-kKnoSSIeiDpfQvk59Ye9pz2GbqK1jMtxXd2cMsPCSKpABoMEweRqEzwrpnDT6Ip1qKYdeASw5k1SfeCL0IJnAy6KSulT8G852eEqJ_NfaF37XjUPP9c5Zz4kW8hx4ekW7aTIEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c466f62b4f.mp4?token=jfZk7kaZfZCMxiuvJjdpYnbG6RRgWdvoD5cZyC8d3KWMWhWhLmRjoXnyrvYUoInjM49Qlyc_7h22NmAY4DHdkZYH7fjFzEzrLfG11jRpKWsZOeC0VVwszbor4CW5CsStH3k_fCgxvH-9XeWlL2_aBdxkysdHg5aK-jllL6uw_RagvadC4WTOYW-yDpVwev9vnQWTPmylpcL-g8E-kKnoSSIeiDpfQvk59Ye9pz2GbqK1jMtxXd2cMsPCSKpABoMEweRqEzwrpnDT6Ip1qKYdeASw5k1SfeCL0IJnAy6KSulT8G852eEqJ_NfaF37XjUPP9c5Zz4kW8hx4ekW7aTIEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: تا محقق نشدن شروط ایران، تنگۀ هرمز باز نخواهد شد
🔹
امروز در صحنۀ‌ دیپلماسی  مواضع ما کاملاً روشن، عقلانی و غیرقابل‌معامله است.
🔹
انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده و دشمن به‌خوبی می‌داند که مسیر فریب…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/463161" target="_blank">📅 09:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463160">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpOVcmAdr44boHxwkRK4A5dliVQp3qKurNb3b9Z7hkbY2pSVyCWijjF1zR_v_00PnlJj0gXf2fGvzCu4svPFWABQqmiDIyEoiDp1MUJrLDaeTMDuOdjSPNxKny6kiOlfS9a2vLy6XUkijaAEXVrThO3m9zE3GL3sMjoFVggYdOUf1JdT_LB9rR-LNd3gdOfHcU19JffhFbAov29L2sVa02Q4J_Ddu4X-2k8mOFAgdeb7mdxzOmty0ANr5_WtJZDualqNvGhC5ErUTBMSh7bN8cyaZIkioOvBYoo67Eg9MCSXkCq19AMojrQRN3sJ7vpEVY5B66EHUdEK-XnLpskMZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مرز جوی روی نقشهٔ هواشناسی ایران قرار گرفت
🔹
براساس نقشه‌ای هواشناسی، مهم‌ترین سیگنال جوی ایران همچنان در نوار شمالی، سواحل خزر، ارتفاعات البرز و بخش‌هایی از شمال‌غرب دیده می‌شود و احتمال رگبارهای پراکنده وجود دارد.
🔹
در شمال‌غرب به‌ویژه ارتفاعات آذربایجان‌های شرقی و غربی و اردبیل، ناپایداری‌های محلی می‌تواند باعث رشد ابرهای همرفتی، رگبارهای کوتاه‌مدت و رعدوبرق شود.
🔹
در گیلان، مازندران، گلستان و ارتفاعات البرز نیز رطوبت دریای خزر می‌تواند باعث افزایش ابر و بارش‌های محلی شود؛ این بارش‌ها لزوماً گسترده نیستند و می‌توانند نقطه‌ای باشند.
🔹
در مقابل مرکز، جنوب و جنوب‌غرب همچنان تحت تأثیر پایداری و گرمای هوا قرار دارند و احتمال بارش گسترده پایین است؛ در مناطق خشک و بیابانی نیز افزایش سرعت باد می‌تواند باعث گردوخاک شود.
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/463160" target="_blank">📅 09:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463159">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN55KYK2S4NHWag0tKNjI2XSm7P9qFVxShSXwNaHTnE3uy14Myp7Vs-qEFUNHLFtuGOm944csTgvW0djZ-PW48DTcC5DNVx30nyFxm4c_KBdQY-5xGfOm1kvp-TSksG5U4I1I7enDosqM0Ef5X6yLh9WJwg-jmQc3e2yROeXqbLSLIAO6ElA_2hepicjlXurfCpSZBBVCaBg4fpof0IX7fmA9-Ejz4oXyt0tN5OgVm6pyYrsYC-IO8EHDBiGr9eGF4KhuxcPp8HygW3hqltulo6e_bLQKAjsn0cPJuD6aDn7Hbo6Mug6LFyx93_m8U1dX70V_9kOAHLmZI-lYDkkRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر توله‌یوز تلف‌شده در میاندشت مربوط به گذشته است
🔹
حفاظت محیط‌زیست خراسان‌شمالی: تصویر منتشرشده از لاشهٔ یک توله‌یوزپلنگ آسیایی در بخش شمالی پناهگاه حیات‌وحش میاندشت، مربوط به حدود ۵ ماه قبل است.
🔹
لاشهٔ این توله‌یوز در تاریخ ۲۲ فروردین امسال مشاهده شد و با توجه به فساد پیشرفتهٔ لاشه، علت دقیق تلف‌شدن آن مشخص نشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/463159" target="_blank">📅 09:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463158">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm5VidMmw62rIdXP9N-w5uOceUEvW_tsXNbb7cxTEdY2uJDr_nQWQvy1s3MZgM3KL0J-snA6j778lL3vKQ3mSqJ0HbWRZa9-Njm8qwQyl5pYZvSg_wLZxC4cW0WK1BZgMtayhxDKYlH71NnpHe5csFvG6qDHUyLqO_iRMS2THLkqgnPIYT1zp71JsYwuA_GQpvirEZEcevMZwhLv2TB0vFV6BTfLchwIqcA1uIqsFoktMPbElP9f40VShJwttFSpWNgQKYchc5rtPx52DAvvmrJpwAD_Q5zKsmP0VfCEPpQGvKohC99AJKSCMsByBmFRudTltK5PdT6Zf_cOSoG1fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/463158" target="_blank">📅 09:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463157">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c7dd06c5.mp4?token=p1VmB5FQQtwnONLNIeNtHg8T169Y6ibM0Q_wuq-OxJXkL5latuh9eZwFRUqSpMZmh6Fqg56cvWpnc0bSbXmdIVE05uutqx0PyafA8C7vc0hJOIvrUy_3XaLUiOAt5TZyfSwHKEyJSgPr8V6dHew4LpYuDDsJODVkTPVFISrPqpMgjwhn3lcIb0kJ7YFLPBK4jpPkDEdpbhX_FdTfewU5qDJWxQTZFOre1_KmfIfsT0eCdUZFK-cluzxScF5bwxCmEhfujX564o8IRwxX-sOxSNyNTQYHMeZrWxo8Bk33K72dI46lxyGqd0-g-lKvjIQ8z-8toigjTmzUPnfePne46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c7dd06c5.mp4?token=p1VmB5FQQtwnONLNIeNtHg8T169Y6ibM0Q_wuq-OxJXkL5latuh9eZwFRUqSpMZmh6Fqg56cvWpnc0bSbXmdIVE05uutqx0PyafA8C7vc0hJOIvrUy_3XaLUiOAt5TZyfSwHKEyJSgPr8V6dHew4LpYuDDsJODVkTPVFISrPqpMgjwhn3lcIb0kJ7YFLPBK4jpPkDEdpbhX_FdTfewU5qDJWxQTZFOre1_KmfIfsT0eCdUZFK-cluzxScF5bwxCmEhfujX564o8IRwxX-sOxSNyNTQYHMeZrWxo8Bk33K72dI46lxyGqd0-g-lKvjIQ8z-8toigjTmzUPnfePne46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: متاسفانه در فضای نخبگانی ‌و سیاسی ‌کشور، دو خطای راهبردی وجود دارد که هردو واقعیت را ساده‌انگاری می‌کنند
🔹
مردم عزیز! در هفت ماه گذشته نشان داده‌ایم که در برابر تجاوزگری دست‌بسته نیستیم. منطق ما در مواجهه با دشمن،  پیشروی هوشمندانه و تحمیل اراده‌…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/463157" target="_blank">📅 09:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463156">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a03c66c9f.mp4?token=bJucAn4hTJPw_V-D4xIYbFYPQiWJTRle1TfMOMEF7Ck1HEBDPsf3Mgwq3yhMaady7JlTOZJ9kub_pgawgWeBQ9PepgrR_OzBYlUjuqlOjsbZ7HhWKHC5lZ32i_dwunQBlvKlYTPRwK5nDxysItDVawgXMpWmy9HQBaVdxNY2TeYVCJWKtun_qeM1EX64U_h89py22SkzA83ioF8dM3tqo74mwYImpxvVhiwnDT4DTodZPK0DiwUt6XgFcp9fbQHqhNGDj7DAn651m9gc0wrCIR-o2mzbnZlbqwRcq5JzbiiA43WNiqLllisuaO0TSKA9mAJ7c_zdsa6ZIhrWM5qqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a03c66c9f.mp4?token=bJucAn4hTJPw_V-D4xIYbFYPQiWJTRle1TfMOMEF7Ck1HEBDPsf3Mgwq3yhMaady7JlTOZJ9kub_pgawgWeBQ9PepgrR_OzBYlUjuqlOjsbZ7HhWKHC5lZ32i_dwunQBlvKlYTPRwK5nDxysItDVawgXMpWmy9HQBaVdxNY2TeYVCJWKtun_qeM1EX64U_h89py22SkzA83ioF8dM3tqo74mwYImpxvVhiwnDT4DTodZPK0DiwUt6XgFcp9fbQHqhNGDj7DAn651m9gc0wrCIR-o2mzbnZlbqwRcq5JzbiiA43WNiqLllisuaO0TSKA9mAJ7c_zdsa6ZIhrWM5qqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رئیس‌مجلس: مسیر آینده نه با التماس، بلکه با عقلانیت، شجاعت و مبارزه رقم خواهد خورد
🔹
امروز نظم کهنۀ‌ آمریکایی در غرب آسیا فروریخته و این کشورهای اسلامی منطقه هستند که باید نظم جدیدی را پیاده کنند.
🔹
ما با تکیه بر اراده‌ تاریخی ملت، تدبیر فرماندهان شجاع…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/463156" target="_blank">📅 09:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463155">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04a8dd1313.mp4?token=Id8QsqlKMwNXSx64Xf65sHiRdGtlpxpbow-BPaJYq9W4aaN4P_fFjLTaVcwdZXOJO0kbswdReyUJ9HO-ODPJyI0YksNfTBKkFDU5Se8ktSilcS-yUIo5vATrKCkXmYYJNgUSLZXubbwrmz1c3AZ2zrY5tceogRpp5WHxfwr-v4NpjfaVzdJXDmAI1jjdVki6fANQc4_NGzZStT229ZiCKfYVq5QmUHIWMGoBhdv2VmL4ij61HGW01ZxCQMmxR51lnHmGU5OUYVP8zcrZECoMbdqH1pR_-gGAdp1uoMLsqtPpnIo1BGCRTBLcC47mzQEXhr1Y73hCgGZ54oM0InSWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04a8dd1313.mp4?token=Id8QsqlKMwNXSx64Xf65sHiRdGtlpxpbow-BPaJYq9W4aaN4P_fFjLTaVcwdZXOJO0kbswdReyUJ9HO-ODPJyI0YksNfTBKkFDU5Se8ktSilcS-yUIo5vATrKCkXmYYJNgUSLZXubbwrmz1c3AZ2zrY5tceogRpp5WHxfwr-v4NpjfaVzdJXDmAI1jjdVki6fANQc4_NGzZStT229ZiCKfYVq5QmUHIWMGoBhdv2VmL4ij61HGW01ZxCQMmxR51lnHmGU5OUYVP8zcrZECoMbdqH1pR_-gGAdp1uoMLsqtPpnIo1BGCRTBLcC47mzQEXhr1Y73hCgGZ54oM0InSWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: تا محقق نشدن شروط ایران، تنگۀ هرمز باز نخواهد شد
🔹
امروز در صحنۀ‌ دیپلماسی  مواضع ما کاملاً روشن، عقلانی و غیرقابل‌معامله است.
🔹
انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده و دشمن به‌خوبی می‌داند که مسیر فریب…</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/463155" target="_blank">📅 09:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463154">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okHFlMGqlPOh5fOCf2bTNE_bdXq8vracHgI7ql53EED5oGqQUJQKbM5ew0uuNEmmo6N0d8rb2TCHJUDumgU3I_m37_TbzP9c8s76owFiE46LiGKfZ1L_GGfj1ArFQ_NVZeLdYMun6IYV5Kq3bNbxH99_BbpDHIZaPLJggklOI9Vd1CwgCAKmEF9ZOt-WRTnYTstRn4lFuGCRzg33uh6E4Y0UOSZv6ovH3pC1xStq5x4INxJ4UpHICHJl56l-28GkfDG5M0gPBBOW8yZyWHrRipm3ou7Ucmf8GEQQL-gNN8RYSBohvDZqvFQCMm6Cspv7E_J9h2brofNgAGvtkob12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: مقاومت مردم با شکل دادن به نظم جدیدی در منطقه و جهان، باعث گشایش هایی در حوزه‌های‌ اقتصادی‌ و استراتژیک خواهدشد
🔹
رئیس مجلس در نطق پیش از دستور صحن علنی: در آستانه‌ سالروز آغاز جنگ تحمیلی اول  علیه ملت مقاوم ایران در ۳۱ شهریور ماه ۱۳۵۹ و هفته‌ دفاع…</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/463154" target="_blank">📅 09:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463153">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcf81759e2.mp4?token=tjZc5LuK9Eq8qIEU4DtyiUVgpltHQqAL7A4BFRNhm830vI5M-v1HUCSuTwG0Z5wggFWkElcgeFO5sqQePGRrBg4QXBcWB7BBPyRLsOUgTXxge4OPx6SHxGgsptKuMe8RmmNMF00t81-hzFDsODAs6jXNC4pKTEc5YrrWAARu9556M4XmtVDGpJJveB6s6XEVIut-lN0zpAWBxH6fjXCT_g8Yhl9UZEciALg_0WI8uEOh9IZvUAoHDPY_6Jnm-atJznK4VPbfgvk3JroEU_JO3s4nmVQj3yBrJaArQ-gifvWWSpe0PagAQr09J1hq4qyfu7yceHKiZqUTdBlieV7mvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcf81759e2.mp4?token=tjZc5LuK9Eq8qIEU4DtyiUVgpltHQqAL7A4BFRNhm830vI5M-v1HUCSuTwG0Z5wggFWkElcgeFO5sqQePGRrBg4QXBcWB7BBPyRLsOUgTXxge4OPx6SHxGgsptKuMe8RmmNMF00t81-hzFDsODAs6jXNC4pKTEc5YrrWAARu9556M4XmtVDGpJJveB6s6XEVIut-lN0zpAWBxH6fjXCT_g8Yhl9UZEciALg_0WI8uEOh9IZvUAoHDPY_6Jnm-atJznK4VPbfgvk3JroEU_JO3s4nmVQj3yBrJaArQ-gifvWWSpe0PagAQr09J1hq4qyfu7yceHKiZqUTdBlieV7mvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: مقاومت مردم با شکل دادن به نظم جدیدی در منطقه و جهان، باعث گشایش هایی در حوزه‌های‌ اقتصادی‌ و استراتژیک خواهدشد
🔹
رئیس مجلس در نطق پیش از دستور صحن علنی: در آستانه‌ سالروز آغاز جنگ تحمیلی اول  علیه ملت مقاوم ایران در ۳۱ شهریور ماه ۱۳۵۹ و هفته‌ دفاع مقدس هستیم. هفته‌ دفاع مقدس، صرفاً بازخوانی یک خاطره‌ تاریخی نیست؛ بلکه یک تجربه‌ زیسته و آزموده شده برای حراست از استقلال ‌و عزت ملی در برابر هجمه‌ دشمن است.
🔹
اگر دیروز، جبهه‌ نبرد در مرزهای جغرافیایی خلاصه میشد، امروز دفاع، شکلی سیال‌تر وعمیق‌تر یافته است. ۳۱ شهریور ۵۹،  آغاز یک تهاجم ناجوانمردانه به ایران عزیز ما بود که تازه از استبداد رژیم منحوس پهلوی رهایی یافته بود. اما جنگ تحمیلی اول نه تنها ما را زمین‌گیر نکرد بلکه مقاومت و ایستادگی مردم در هشت سال دفاع مقدس  موتور خودباوری و استقلال بنیادین مان را  در ۴۰ سال گذشته روشن کرد و کشور را به اهداف عالی انقلاب نزدیک‌تر نمود.
🔹
امروز، در حال تکرار همان تجربه‌ تاریخی هستیم؛ با این تفاوت که این بار، مقاومت مردم ایران، نه تنها ضامن امنیت ایران است، بلکه با شکل دادن به نظم جدیدی در منطقه و جهان، باعث گشایش هایی در حوزه‌های‌ اقتصادی‌ و استراتژیک خواهدشد. این ایستادگی با ارزش و تاریخی مردم،  همانطورکه در دهه‌ ۶۰ ایران مقتدر امروز را ساخت، امروز نیز ایران را به سطح جدیدی از اقتدارو شکوفایی خواهد رساند.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/463153" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463152">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO72gRQBO-z1bgVzp6e4HQ2NxcbTR8SufVGNoeMKu5Y5JKkP3coQ62am9FvpThBh-_pjWliEq7s48i87KG3Y2Ru9dsEmUXF8GBE_d8q8JSyvOKAMO8ScWaLRv4jUbVS_GdC_jIjH_HK1ffjXObmGF5uKnkYhZTsSmfRgjMrXfmeZBuR5Xxri6IbdME750L0iLHfwQSx7aCWj8029S0qC1cR4hFwLFGtDdeAPkWnWCf_7e-dDa40samMlCgioe8whTfHZmvt0oN0__GUkV8r-thMWR47iqRuEo1qL8MP1hnHFZ_Xs7257sqpVKxXWrnjL-ip0s4XRe1yq1bn1Ryyapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار و فرناز درپی مقصرنمایی ایران
🔹
یاشار سلطانی در میانه کلیپ افشاگرانه‌اش درباره تراستی‌ها، بدون اشاره به نقض‌های پیشین آمریکا، جریان سیاسی پایداری را عامل برهم‌خوردن تفاهم معرفی می‌کند.
🔹
این همان روایتی است که پیش‌تر نیز در گزارش فرناز فصیحی در نیویورک‌تایمز مطرح شده بود؛ روایتی که می‌گوید اقدام یک گروه خودسر در ایران، فرصت دیپلماسی موجود در تفاهم بین ایران و آمریکا را از بین برد.
اما واقعیت پنهان چیست؟
🔹
مهم‌ترین بند تفاهم، پذیرش ترتیبات ایرانی در ادارهٔ تنگه بود. یعنی ایران در ازای پذیرش برخی تعهدات، حق مدیریت و ترتیبات خاص خود را در مهم‌ترین گذرگاه نفتی جهان تثبیت کرده بود.
🔹
آمریکا از روز اول اراده کرد این بند را نقض کند و مثل نقض سایر بندها، آن را عادی‌سازی کند. آزادنکردن دارایی‌ها و برقرار‌نکردن آتش‌بس در سایر جبهه‌ها، نمونه‌های روشن این نقض‌هاست.
🔹
منطقا ایران باید در دفاع از دست‌آوردهایش در تفاهم‌نامه، خودش را جدی نشان می‌داد و در دوران گذار روی حقوقش می‌ایستاد تا بتواند در توافق نهایی حق خود را تثبیت کند.
🔹
بازکردن کریدور جنوبی در تنگه، نقض اساسی تفاهم توسط آمریکا بود. اقدامی که اگر بی‌پاسخ می‌ماند، عملاً بند اصلی تفاهم را بی‌اثر می‌کرد.
🔹
بعد از چند روز هشدار، اقدام به موقع و زدن شناورها و بی‌تفاوت نماندن نسبت به نقض حقوق ایران در تفاهم‌نامه، توسط مجموعه تصمیم‌گیران کشور قابل دفاع بود.
🔹
روایت وارونهٔ قصه که ایران را مسئول به‌هم‌خوردن تفاهم معرفی می‌کند، ساختهٔ اکانت‌های اسرائیلی و سلطنت‌طلب و رسانه‌های آمریکایی است.
چرا این روایت مهم است؟
🔸
اگر این خوانش درست باشد، آنچه در تنگهٔ هرمز رخ داد، واکنشی به نقض آشکار تفاهم از سوی آمریکا بود.
🔸
در این چارچوب، کسی که اول تفاهم را شکست، واشنگتن بود؛ نه ایران اما روایت رقیب، با جابه‌جاکردن نقش قربانی و مقصر، می‌خواهد هزینهٔ سیاسی این تصمیم را به یک جریان داخلی منتقل کند.
🔸
روایت «خودسرها تفاهم را شکستند» در ظاهر ساده و جذاب است اما وقتی در کنار نقض‌های زنجیره‌ای آمریکا قرار می‌گیرد، فرو می‌ریزد.
🖼
سوال مهم اما این است که چرا باید انتظار داشت ایران در برابر نقض بند اصلی تفاهم، تماشاگر بماند؟ و چرا حالا، به جای محکوم‌کردن نقض‌کننده اولیه، انگشت اتهام به سمت داخل نشانه گرفته می‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/463152" target="_blank">📅 09:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463151">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آغاز عملیات ۱۰ روزهٔ خنثی‌سازی مهمات در خارگ
🔹
بخشدار ویژهٔ جزیره خارگ: عملیات خنثی‌سازی مهمات عمل‌نکرده از امروز به‌مدت ۱۰ روز در جزیره انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/463151" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463150">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7457ce6ff.mp4?token=WXl99iUH47w6WUGDNGdKrH7lfvYuWWHkXb_mJV2LUC-CSqAHoHkl9GHGFzAP44zb6UG27uW5mZTyAlyVT6XEC7qZbocSZve5eTp5X5dfutHpvSrLUPWF1hC8aXxJAfUyE4Ki4egE8Ey0aXik9_9i5x147x4LAcgt1d1csr0RSUSnRrwuBb8a4MrsUWu0lq2-AVKAV6Z4a5FpWw04mrmorEz6VwzGd5k7Fk8e4wlNJ8aF899jHFfQqH4rjfbk-RrFnYmLcRtFYG2eTCDRFjOOa0WtcBZwNarbpkLtQtZ98A0HHIY5gN1ojK5EuhMfjqLt89QrQX-aJMxcFnGVfZTY2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7457ce6ff.mp4?token=WXl99iUH47w6WUGDNGdKrH7lfvYuWWHkXb_mJV2LUC-CSqAHoHkl9GHGFzAP44zb6UG27uW5mZTyAlyVT6XEC7qZbocSZve5eTp5X5dfutHpvSrLUPWF1hC8aXxJAfUyE4Ki4egE8Ey0aXik9_9i5x147x4LAcgt1d1csr0RSUSnRrwuBb8a4MrsUWu0lq2-AVKAV6Z4a5FpWw04mrmorEz6VwzGd5k7Fk8e4wlNJ8aF899jHFfQqH4rjfbk-RrFnYmLcRtFYG2eTCDRFjOOa0WtcBZwNarbpkLtQtZ98A0HHIY5gN1ojK5EuhMfjqLt89QrQX-aJMxcFnGVfZTY2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رختکن امیدهای ایران پیش از دیدار مقابل چین @Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/463150" target="_blank">📅 09:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463149">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXtV19c-YCddZFpTcpAluiHZbSph34zVIxaEXHU4xXyNBdwicJD04vXwr4i-wMk_0z2iBdtebjUqC096dYV-AkJZXCfDZvQdw582tXbO7G5JWqFjarGuLQjpQsuCdIPl_DK71kUfM0szlfBSYyPyjMNHl4azKJelQVTy8kYhcr2sNjUYSRLmBifW3IlmtUctpiFxGZllUzLrs0IuNZtGDnkviIIh1qHE0x--0AIkdUuFQSaH-K_43UayY_vFXM_TMJlhqhHjI3Bnr1uvf-eTNTCyQzjFBAPLiGzADG5uEMQWYwCUqc1TkwpbQklGeZ-XqS-QKXD122CkP09RPl-xoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصراف رقیب گروسی از دبیرکلی سازمان ملل
🔹
«میشله باشله» اولین زن رئیس‌جمهور در شیلی و کمیسیر سابق حقوق بشر سازمان ملل، انصراف خود از انتخابات دبیرکلی سازمان ملل را اعلام کرد.
🔹
نخستین رئیس‌جمهور زن در شیلی، با انتشار یک ویدئویی گفت: «شاید برخی بر این باور باشند که زمان برای نامزدی‌ای با ویژگی‌هایی که من نمایندگی می‌کردم، مناسب نبود. با این حال، از پذیرفتن این چالش بزرگ پشیمان نیستم.»
🔹
با انصراف او، حالا هفت نامزد (چهار زن و سه مرد) برای دبیرکلی سازمان ملل باقی مانده است. رافائل گروسی مدیرکل آژانس بین‌المللی انرژی اتمی یکی از این نامزدها است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463149" target="_blank">📅 08:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca3c3932e.mp4?token=QsJWoNUtQHaxc8iFxNlt-TpO_ES_P1RXeWzcXJCEu8q39aHapJDQtL58N_z7qF3-qRnIUayHlr5Yr37Ytv9zodmSmv21V-_CVG70hJdA8edf3-5bzzse6b9bm9Pqgva0pPW4ZpoMtCf_AJlBV1n1ZSAwUkHdcV59Fnnt8o3DXHv91vCludVQjl8U2xcgzpGs2BLm6Iincgk6H7t6ftKK548z3iO2kSs06KC-eCekg3rH_janF7qPYiO14sZ8ZDT-7Lq2jqkoJCwfhmmCF0z6XyURRnRMyjhBAsu4p2Tz3VL5jrbQQ8vbsJ-MqHDUk96IzcgA5oRi_IVi0ubDPP4gZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca3c3932e.mp4?token=QsJWoNUtQHaxc8iFxNlt-TpO_ES_P1RXeWzcXJCEu8q39aHapJDQtL58N_z7qF3-qRnIUayHlr5Yr37Ytv9zodmSmv21V-_CVG70hJdA8edf3-5bzzse6b9bm9Pqgva0pPW4ZpoMtCf_AJlBV1n1ZSAwUkHdcV59Fnnt8o3DXHv91vCludVQjl8U2xcgzpGs2BLm6Iincgk6H7t6ftKK548z3iO2kSs06KC-eCekg3rH_janF7qPYiO14sZ8ZDT-7Lq2jqkoJCwfhmmCF0z6XyURRnRMyjhBAsu4p2Tz3VL5jrbQQ8vbsJ-MqHDUk96IzcgA5oRi_IVi0ubDPP4gZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب تیم ملی امید ایران مقابل چین در بازی‌های آسیایی ناگویا
🔹
تیم ملی امید از ساعت ۸:۳۰ امروز مقابل چین دومین بازی دور گروهی بازی‌های آسیایی ناگویا را برگزار می‌کند.
🔹
این مسابقه با ترکیب محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی،…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463148" target="_blank">📅 08:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توقیف سواری بنز با سرعت ۲۱۰ کیلومتر در آزادراه کاشان-اصفهان
🔹
رئیس پلیس‌راه استان اصفهان: مأموران پلیس راه کاشان-اصفهان حین کنترل تردد خودروها، یک دستگاه سواری بنز را که با سرعت ۲۱۰ کیلومتر بر ساعت درحال حرکت بود، شناسایی و توقیف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463147" target="_blank">📅 08:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترکیب تیم ملی امید ایران مقابل چین در بازی‌های آسیایی ناگویا
🔹
تیم ملی امید از ساعت ۸:۳۰ امروز مقابل چین دومین بازی دور گروهی بازی‌های آسیایی ناگویا را برگزار می‌کند.
🔹
این مسابقه با ترکیب محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی آغاز خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463146" target="_blank">📅 07:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdKWJ23r0MoDaA8R04QzSeyKEnqwXYhEV6QzRkT28KeLSCk9Sb612YKT5pfjLDfOdr1RDEfa2jgxryMe_qef8HgbNH3fAuY8muvJ4lMQdk_aRBAvPviq5G-Qxf9oqRt6QEuxoObko43PTJytXXIkmagq-wphkY9lTQsxDLMKFllrCMuX4Z_7wvvBIb8iZukZqnjios4h4FSu07KzZUcNaOe3JmCuTG9-gkV5dvg29AQWp6qjh_lJBmkJZ0O43NLRUrxxrkMLK15u78n3zGXdcUN3LO1XTT0zuHBza9gJAmwH1Lo8tk_tMO0Up4q1iYNrNzn7K7dYfRcEJ9xtiWoXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدال برنز بازی‌های آسیایی از دست صادقی پرید
🔹
فاطمه صادقی، نمایندۀ ایران در کاتای انفرادی بانوان، در دیدار رده‌بندی بازی‌های آسیایی ۲۰۲۶ با نتیجه ۴ بر یک مغلوب چین‌هوی شوان از چین تایپه شد و از کسب مدال برنز بازماند.
🔹
صادقی پیش از این تایلند را ۵ بر صفر شکست داده و مقابل هنگ‌کنگ با همین نتیجه شکست خورده بود.
@Sportfars</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463145" target="_blank">📅 07:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooq3Dw8Szi8nUvsCwwKAlQMNZduAiBioFjevmf77zYOmXvH7ef3nqxmnv15Ps2vBUkTBrKx9WQeRGXBzzxuQ_7qcKGJxnPcJvVzCZrq3Qcmv-9BJv6nBOGMQkt3FevjWkgZ_LV-azix_7t3ym6GObRwN3qiJPhP76UA84viG6HNheilqrlaUFtZGVyqHZ9NyeyFPZZf9RKFAZ1rBv32EL1PygdWH0L6PG0dSbyK_jxp6S9x2II_vZYSA4N0Sh92Gl0GD0njgHaZW1GQQlo8aHWfkpKUWA3_gA4ym-5Yriw0WLWa7IiANEhrChfac_pS-uGDWBvDA_--feyMFWOKKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اوکراین به پالایشگاه نفت روسیه
🔹
صبح امروز پالایشگاه نفت مسکو در منطقۀ کاپوتنیا در پایتخت روسیه پس از حملۀ گستردۀ پهپادهای اوکراینی دچار آتش‌سوزی شد.
🔹
پیش‌تر ترامپ گفته بود از زلنسکی خواسته به پالایشگاه‌های روسیه حمله نکند، زیرا این اقدام عامل افزایش قیمت گازوئیل در آمریکا است، نه بستن تنگۀ هرمز.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463144" target="_blank">📅 07:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هوای قابل‌قبول پایتخت در دومین روز هفته
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین کیفیت هوای پایتخت با عدد ۸۲ در شرایط «قابل قبول» است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463143" target="_blank">📅 07:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463136">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAtok_MLW8fBzHivNsS_8-yIcw2kiWSRp2jePwCi3JkLF0ksClROUKUOCZCcoQsSRD7QG0WYUoTPU2vxg4fozRafokOSe3Nm1fZFap3grEZAbDHUiaPo3RM6Ut70yG8sw3lvDScqznr97riNSMQ5vGVX0RgtQDZwnMhHmbVFGhxAczI7FB5nfYvZ8mSjIPo0uy_nQdNlwAhm7FlZfvWPUqt4tYQvRnk73EUcBXjTLpoMcS8o2WHfGarIGZqaGiMOr3JhNQgP7nyRl-gBrWctE6GI0wRhKCn5kLmY_XV3LEme4mh3XOLlYIn3F5ZgCzmpW8zzZ1x_wsOkPp4cGOyBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0ZQbM4p5gfoynKUGaxJAmbl1lGbuvWx217DbSetiF4j8AM85oLQtz4bq58L2VPwQgc5FBY_VXLwIqdMGPHJAGEbt_b4z2VXpHtVNW2B9Vv5sbuemuoe3g5pTXaSLLxKS-4rF351hvI4nmdHas_ABVDe7ADT9Z-ZCNyL-vPOaLNAP2OD-ie0DSOMpcpWyX9OwXgO7i91u69AZZ4E1z8i9NDCtGvDW8FaxMYR-BtC4_pJhoFg7rVyFQQx1kSE5Jhpr_ymo-0JBYYw9eaAV9ZCVp27nVYOWX-svJz5rll7bgTvPcoNwJRT5VF8UXhvqBVCeHQvo-MW5UfcfMUk1rJqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3dq1kVecNCpdFrTRm3VJ4ZzjMrKvp3XEny7K5iDnlU2KYFe3Ivx8MLHf3cwCbcVjUUFrPL7SUKz_-GDKVSKJHMJkLSfIw3zvOXx0OnhrEd7YDDBIcVJxp58bao-UeciNbsWLsxKAJytugpX_JXjdGDVt6V1r2wDJ1QUELG3Ld6h9uX1EkyEejvKoZDPSkej7zZIic4C5AUzkqfSdm0AIye2f7vTiGGnybHlO5P51A1uHpUDOrelSfJRHYxw1hG6ZJc2iaCx_trch-20dtew9BgVVQbvpKcFj_ce4lPfMdTM4JbyebLpYgN-T_bY9aSngSA55ElebuYX8NpdlkdUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbF-Gq-PoYlWTewBSCKgl_8AZCtcsrzDyPTLB5y8mAtfNHCarZLnqOFFRwj1z1e8nCG0zYJkrif_ButuQcyvaaGxFagFsNF4wfE9KKO2hLqvCp4pFPdCHe7IGggrqRK7sk-by73mVt4GtUyJ0uugndrPl_DGEf19tiOGCpsTi_Y6663j_d10oKPzyiuA3bi8zATJEyIOVdD6-CxqdIAItHLkwpJGgWfDFCv-Sw_TwUxv8KKgrADrlYw_wcgYPZysJeiqYf_y9oqKcohoxG6_Kea2VZtYjObEtRfAtq2czg-qrPMkNis-dWnj8MZqyMyczGPNk4LBbcEzwm20Yrgt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CF4Y8xkDmQhZKdG2ivt4Qb9HY9VnMZqLt0WyMBkOxAUNov7Ke-8b_tuL8Dn5v14WDpegN5WAHFNJBa0X4-16iERlJBnXoR1nq7NAa_dFvuHGXUmc1HZYthY8a0WkStvMdW4bGBDCylVoqGgzSj2taWiRTq8ehS4vhPYmkiwWJrB2AnaZcvIlaRxizz9wqUdPmxg8TgmrAptBwhzL2fA4KSgN1d3gYE3dij9D3ijpinTXZDGLyga26GjsWT143dVV1ho5TdxT1tpfs8FebWFKaHQmRaPiqbMWhJ0L83X10Q2NhpT_bR3_jWy-5WO867-99A03qQMpsrW3V2Ko_D8cLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSR2Fi4CA6Sw4-XB8UltUN-rygD1plAZxgISVv_mZgGB9bijP66w8IXAUaMgSJqGJ7jFJ06L3_4kidglNgzM1VzFjpVZeDVXuAm5fOsZNcOUyt5UqOyt_wHWvOTDy_J8nIbgzW_cDyQJt8FJEhR-ID_N1YN3ybihGvYZ3DNIJJCWEQUptG2rs3t-ZcZ3flpn3VW-FM-pC2JbCWQX4s6gKN9029cahZnGY-ufg0ThqttNEHqEQEt9atQA7gQJnp44LAI7spgP6zrRDZ3p9psqdS8yCLoF4gchSjImNLDLy316VGBbeWEhqNCaMx1HYnDkmregfhvkRRYlcbTCS0C3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iso7Wgfx_DLIGSxuRA8wjNSiAZ3mHuOLeOGbyUWeo2Vvci9yT5jScEA9YnHLbN1zdAJ_I5IWHfxlOzzeKGRRo9mkto6cxPXPvi1M4cNgHIG4ySchbfb6lp7pkGNFvvirxA6lHhNVLMwXXwqqK1CSX4odSVZ2veVNo8QEjJogBxGzdXuBCvq9bUUIsOf8If58a-gV1gUqnciX32H2pa08iiMW670y6fC_oiOdz5Nwt0ANVQ-U7H-76A_on-49apWJ-GrweHMYoC44f_PnFGe7S_2ZatQE1D8N2vGNtW4OhitPqLJJizWIBzSk63SrrevRwg7c0cOshGhcBDNJC9IGNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رسم کهن بولاوگیری در دل کوهستان‌های کردستان
عکس:
بختیار صمدی
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/463136" target="_blank">📅 06:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463135">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBMoRJYkbcqdD0-WXr-p_ZhRKfpKzA6tCgug5sqvtZH3m5O6LjOjzL_8rkYwyuv1ErZUUL0NXBWNnxj7ZAXUnPbPfvIs0U1vXqw5do1rKZk4EmVrMhD-3TMC6oL1LG94fsom7LQvZFE9oDR-l27W9m9XKvjm76PPV8WBuSJcq-j8zCqysosng3iD4DMs5vJUlf_9etADrRMMu9Xe6Nfxv4YgI9WU_X5afFXxeu-cbfJN7U3duqzmG__7qKKiC5dgOJ_xcSxm_uPOir4FWJP-AiJiuK91GJeRG_Lh2FOROIX4gxERfuUniPrQOHn78SuoUEai9uvb0nLX54xplFuG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا دربارۀ تشدید جنگ در عربستان هشدار امنیتی صادر کرد
🔹
سفارت آمریکا در عربستان سعودی با صدور هشدار امنیتی، به اتباع این کشور درباره احتمال تشدید ناگهانی تنش‌ها در غرب آسیا هشدار داد و از آنها خواست اقدامات احتیاطی لازم را در نظر بگیرند
🔹
وزارت خارجۀ آمریکا…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/463135" target="_blank">📅 05:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463134">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uES8MLnh3-R7ynn6gZHKJ9pOWrJbO2SdrQuun5Ze82WhQ98_iJoFBd2s2Oi7A-AZ8-bv4TigeABvF7YKS8Ug-QEpKPGq_kMFHyRqjlJynBoBUWPtz12OCcmUg20b_vW2ZEhZ4mFZfLmWFNk5V52-ljAD12-P8NGUTtidlhkmXhdvgrYwDhmJPThYwkkROIXD5ewhlVzk5YPGIrJcLtcJFQWKvMtTmoYpo5901kMvBkWt-X7ntCQxLVVpVrXj29a6SBj6oA74ZftDhULkhvJF4RhpFnmzRCErgF1UstGT6CrBlbVDoAbx94Gb41dKFj5PROE4exUmBDDJcdTrk8bPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت عربستان پشت سد باب‌المندب
🔹
شرکت رصد کشتیرانی کپلر اعلام کرد تنها پنج کشتی حامل کالاهای سعودی طی هفت روز گذشته از دریای سرخ و از طریق تنگۀ باب‌المندب عبور کرده‌اند؛ رقمی که کمتر از یک‌سوم میانگین تردد هفتگی کشتی‌های سعودی از این مسیر است.
🔹
کپلر همچنین اعلام کرد انتقال نفت از باب‌المندب نیز کاهش یافته است. از ۱۱ سپتامبر تاکنون روزانه حدود ۳.۴ میلیون بشکه نفت از این تنگه عبور کرده که در مقایسه با میانگین ۴.۴ میلیون بشکه‌ای از ابتدای سال، کاهش قابل توجهی را نشان می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463134" target="_blank">📅 04:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463133">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKt4F0CgP6RExIXjhxDVq1mxL5x0h2y7R4Gv9NKqHJKkJ9pwYOXghLuL38yLqprWSJc99MT_tM1ibpn4JM0lsVlWbWei05s4-aU0B6M7d-LgOowGk2o7lI_PI9bP11s0KPAep_B3LBhFSXupyeaJFF_YqRsH-pek0mmOi0OtQAYz2ubhAGGrC62wt2IVMNFJRyB6ytgz1Wy1qv5qV4kbPmedeb2t5WabUDPtFlXjc-Gr_wsdzX6nQSmD69QVBDY2rjI8bqIr1g9vfRZ13Xxy_tMloyb3GwA7VGSCR7LgJLerRRPHYuB6A5H20b-2RHxvudunP90jT4RQeQw0sIPKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از استقرار نخستین جت‌آمبولانس کشور در اصفهان، تا رسیدن برق به عشایر چهارمحال‌وبختیاری؛ ۹ خبر خوب از ایران   ارسال رایگان کیف و نوشت‌افزار از سراسر ایران به دانش‌آموزان سیستان‌وبلوچستان، با پویش «مهر را پست می‌کنیم»
🔸
همزمان با آغاز سال تحصیلی جدید، شرکت ملی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/463133" target="_blank">📅 04:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463132">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac9d2c105.mp4?token=oOnh4o7BHJQRJ8b7AshTyZNS3SP3meB783kn-V_wl5QT4JBVGmg9D9lVlDPhO5bx0OaRTBCyaEDhLoGvFiIYNd0NX3dWe1faktyIDMTM8E-sohbLWER9O4h69a6ee1rvlfW3WWRXOTZ8X0IVqZPWyda5YbzAk1dLHZloOLYWS-R7n5BKEERCELbQXetrNTJchMAGDvp2e5wrMEBY2jizLGqAKv7Pocui9VKuDfRsj1VeHm2wH7t3pcDNuBkslDmJgiGT0qkT72jH9PapQ3TWxL9GvFdvIjRLW9mYNidBrqLZ3VZ-eAWJwYQ_CVKUOfMyW5zinnh0qB-iOchSH1QmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac9d2c105.mp4?token=oOnh4o7BHJQRJ8b7AshTyZNS3SP3meB783kn-V_wl5QT4JBVGmg9D9lVlDPhO5bx0OaRTBCyaEDhLoGvFiIYNd0NX3dWe1faktyIDMTM8E-sohbLWER9O4h69a6ee1rvlfW3WWRXOTZ8X0IVqZPWyda5YbzAk1dLHZloOLYWS-R7n5BKEERCELbQXetrNTJchMAGDvp2e5wrMEBY2jizLGqAKv7Pocui9VKuDfRsj1VeHm2wH7t3pcDNuBkslDmJgiGT0qkT72jH9PapQ3TWxL9GvFdvIjRLW9mYNidBrqLZ3VZ-eAWJwYQ_CVKUOfMyW5zinnh0qB-iOchSH1QmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکار امام رضا(ع) برای غم و غصه و نگرانی
🎙
حجت‌الاسلام پناهیان
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463132" target="_blank">📅 02:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wx66leFTdNeZ4YnmyBmsbc3kz0Mlu0Um7BPHrircDbQ-xoCMewUEvRYxeJLSeTkGoAB3B2cX0U526LzluNUfgRcavUybN1HCVYD4tPu_n8Q3nRiYd5lNvbmT5CEJMJEohsRNzK4S6Hc9FccZb2f-jNLErj9iPqwKHKx2YtWJgiLBSsiLjXMckA9Xe7_zoGBL21Ey81aANpDafsRmGKexuAirikP2EG8EDubOiwrx-X6KzAP85mXyHGKUarViRnNGu_wajK89Odo0qmg-O1a6e9EOntpR6VRMg3tjkVpSVDPfe3JjgjOmt7-046nzibMseYUIJdaA-EG1y1rBYSNs2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا دربارۀ تشدید جنگ در عربستان هشدار امنیتی صادر کرد
🔹
سفارت آمریکا در عربستان سعودی با صدور هشدار امنیتی، به اتباع این کشور درباره احتمال تشدید ناگهانی تنش‌ها در غرب آسیا هشدار داد و از آنها خواست اقدامات احتیاطی لازم را در نظر بگیرند
🔹
وزارت خارجۀ آمریکا نیز در هشدار جداگانه‌ای اعلام کرد احتمال تشدید درگیری میان عربستان سعودی و نیروهای یمنی وجود دارد. این وزارتخانه از اتباع آمریکایی حاضر در غرب آسیا خواست احتیاط کنند و به اتباع آمریکایی خارج از منطقه نیز توصیه کرد در تصمیم خود برای سفر به غرب آسیا یا عبور از این منطقه به‌طور جدی تجدیدنظر کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463131" target="_blank">📅 02:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g835LZt5YPHDbnU8K6HucqAy39Bl2wTpOhxsEMPQQwtpPFViyiC-fTcZSA2lHpOJeoaUiwHERPZSJ5RYlQN22JVtQQATzJwuNtD30jkXxn8AdIw3L6sIYJpqgvICQFtoObvRos0Oml2NJZnfjFCFjyVNiba_8LyKIdAXhsgkz8PDH484fzcep8vPdc1ywOrk0d3TXv9fkG_zmX6kiU0DiI1HWRrAg2uQdmrIQKs3n4mvyUIgeHk2KLtyQUdQhU_VRyLQ9A92m7gw3VVlrQWOKfomYLpv6LhHS4dyLXufylKRtRc5iH58OQdBR6rwO_rDlihGaBQMgNEZP3Hm92C79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvqNuOqGn0bLpjQSBEDoA2_yIBhwVs6Z_YYUkO65zXEwlMScR0f2ONJLyCuGnD0ijF52moK3cqgvj9GiPEXWdoZnY8iMjBp8MFiR0EbyMVUbIHFZJAvxiM4Ju92N20dUj_iywNN_MeZBt1gXeownz2T11_wpGluqH0i5PnnwlXKRL7YsTkbs1s_8Vc6cmSL8nN2jWBnwzDZFcf9r8xjqAH_XH8uLTYfXU_7U4vKncCsLOEkNJMVgtGQUwGnQtkJhgNG6Gp_MmxbJ4nktkQNqI1U5LdI2fYue0GxpzqYKyicP0mjrgRsrw8uG2jqcUeVJxjQACYiMqcuvKNOEf8atPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTkwDxvRMePGDoGNIbZXgE8KrEe4MoboUr-NgsQ1kthwqGTy2B0CsKYyYP5_iLoUkvTsbe5Q2XEWc6ipvllgrwoCk01_hoItuClv0ZT8cQtYrbeQ18qQ-2carwCw15VkdHJs5wFAMoE9vhwKXS8LfBckqCRpVn1oK8p3UAq4JFkw7T4B2k4RYWcxZUT8NPsDPwLlkZ2UnfIY1JHoSeW4-K6NUNoHiZJnNmVXdXn3Z9IA-dpzg3CKF_ClrbqWyhTwUTXff7aqhDQixxdmKj7QksGnpg7JQVnjkWSHO5mKi28JlVx3j1PGlaofTY27Q5QwpQ1btceD8aZoTHyOf4CX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tam7BunL2PWEhXXSoP7J3nl4pzBNlN9CIeC29btYugK-NYK03kN8cbfYCLLWFMAznp4xWa4POmeKIFKCLgJDZIyOxoFIX1q4caNyXLuCUTDltu11Avl03a-A6wih2FBp5JuBlgpsVCxRvryPcCGwtjBHeM9u7W9Wm0aZvhF5vvZ8PYhhl4gZi0kNEJaR6zE2cNwZPDrfet5IdMIpfu4oBg0iRktbY6XpTMmU6bqGFKMjZnrSrGeu2rvr03sW0Tg68ZZD_JC-4xaU7YPIrv42fKWKicyvr_HpfYrY_Q3bhGvxJd1bTqlhkXUnnomSRFNNJP_lVxwrqO5LlRrjoNKk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxevuGu5OLe8dedZBX-ITYfcGu90MDMqy5W2xzX_jMy8CRnVnDABP_X7cWS0DKh3LM9-eVVZVzHMiUf9BVkNzXjYqarqOGuvI9LbjrZpBLsse9W3I9I-dB5u8k6gLjFVVZkjbYw2vlX2nLnslqoTPKSB96E0ng0ACpV4OTfN6WYY9hel4fla-9B5j3ucV-lwyhuPAH6DC3crsn4ElxMIxI-Wgvt1_rT-ETgBSgy9HqtlPtTtTYp76T0dp_mXEK8zE-GrSCuJOgL1LReU2mJdokbPA4KM46lxzBa2MHeUTHBYzB5zH_yXpHstcYazYM7oQxRWku-c4D4dcXcY0GBUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4PGvaREIzFQ68VsziRdQMDK3qbOW4zmBUeEciovzkA2ewuaQapoL3ACk-tBNDDy-6UqTfNrEMfCEZZ1NHQvFn_cy6sUhMWWTgQS_tqRLbK7sn5ej35DSn66sZsJais5j2ynYAg9ETrIfmfHi95izq9WDTb4xSF-ybAJzCNjyNEa08lWKcNp8mO2jlo6JNL_5WPLnsIZJ1L3dVkFoJa0ETma37W74If-6m6aqC_7W845wPy4AJfhNPNvdGeBPX-Vc4Jpb2_TOty7OZ9Tu7uqgLF4KxKJJLQvhIOp1AiklxPXl6GXMFPnS4sNeYlq0_f7KeL3-MCmrmM6FFX0pWLNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6CCK2HGN3hg2swTjpgbUeH1iedr_GNhl761yB0NoIxvFM9xCshNZFtTWIl9s07FbuEJUv4Ys_st0Ae98W5Yq0DIfnr2hqVG18bkP41ElGvh2AaKWMESWDMoz9HChGW3zmWQ_f0BegZDHX2FAZqK1KPjxUxTyec8b17jz-o2-ze_IUZhqkM0JvcQzGPWaQ84B4nrV6EUeZs0vwE7MhNPQjcsVB-wZ4F9bXR5smGGNv_ePaR-F703gBLtNJ1L6Rl0l6DC-ejPTnm7r21HJQSzqkkvVYyRCpYrJPjdoF8HNHGQkzOawub8yNCAr8fIVSWhZWgz4-irIvcl9Ihp1hr48Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن تولد برای طلبۀ شهید جنگ رمضان
🔹
حجت‌الاسلام اکبر قربانی‌زاده در اولین روزهای جنگ رمضان در هوانیروز کرمان به شهادت رسید.
عکس:
مهدی امین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463124" target="_blank">📅 02:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463123" target="_blank">📅 02:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انصارالله یمن: نفت عربستان منشأ تروریسم است
🔹
حزام الاسد، عضو دفتر سیاسی انصارالله: نفت سعودی منشأ تروریسم، تامین‌کنندۀ مالی رژیم صهیونیستی و علت بی‌ثباتی در منطقه است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463122" target="_blank">📅 01:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انصارالله یمن: نفت عربستان منشأ تروریسم است
🔹
حزام الاسد، عضو دفتر سیاسی انصارالله: نفت سعودی منشأ تروریسم، تامین‌کنندۀ مالی رژیم صهیونیستی و علت بی‌ثباتی در منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/463121" target="_blank">📅 01:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">منابع عربی از توقف پروازها در فرودگاه بین‌المللی طائف عربستان سعودی، در پی حملات یمن خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463120" target="_blank">📅 01:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هشدار یمن: تنش‌زایی عربستان را با حملات کوبنده‌تر پاسخ می‌دهیم
🔹
سخنگوی دولت یمن: زیاده‌روی ریاض در ارتکاب جنایات بیشتر علیه مردم یمن، صورت‌حساب میان عربستان و یمنی‌ها را سنگین‌تر خواهد کرد و سعودی بهای هرگونه تشدید تنش را خواهد پرداخت.
🔹
یمن برای جلوگیری…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/463119" target="_blank">📅 01:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هشدار یمن: تنش‌زایی عربستان را با حملات کوبنده‌تر پاسخ می‌دهیم
🔹
سخنگوی دولت یمن: زیاده‌روی ریاض در ارتکاب جنایات بیشتر علیه مردم یمن، صورت‌حساب میان عربستان و یمنی‌ها را سنگین‌تر خواهد کرد و سعودی بهای هرگونه تشدید تنش را خواهد پرداخت.
🔹
یمن برای جلوگیری از تنش‌زایی‌های عربستان، در وارد کردن سخت‌ترین ضربات به این دشمن متجاوز هیچ تردیدی نخواهد کرد.
🔹
عربستان باید به اتهام‌زنی، بمباران، ارتکاب جنایت محاصرۀ ۱۲ سالۀ مردم یمن پایان دهد و اگر چنین نکند، بهای آن را خواهد پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463118" target="_blank">📅 01:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">منابع عربی از توقف پروازها در فرودگاه بین‌المللی طائف عربستان سعودی، در پی حملات یمن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463117" target="_blank">📅 01:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbrjG6RvHI9h-6V-vrnwt7zBlac1yXNLm-5igIjIbweVNurp5o0bQ65vZ0s5i-stfpytxq6egoz86lVg2lIxpsQ8kQJX6PdA6YKOULBDpcOg4uWXsX77ErDk4XwSAlMqj3KWAhSOjsyhaa_VLO0yU-kioFTIWhyS2F3ZaC3Ly4-5P1Vk8uz3_B-s18LdFgkaxGEpcZ4IXM6J2-QLl9D7QaaK6ekHiu0CvbiF2JAbv1KK1Azxtzs8wEmYQ1_BaQaoLoRrATGgL-RKWv9Yp3yevIBr9aT63ExHli_Nf6HsRuvuBFRA1P__3_s9KfCrGEpEppUdA8U9oaD-EKiWQUQKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت عظیمی که می‌تواند گره‌گشای مشکلات کشور باشد
🔹
رزمایش بزرگ «جان‌فدای ایران» با حضور گستردۀ مردم در تهران برگزار شد؛ رویدادی که حدود نیم‌میلیون نفر برای شرکت در ثبت‌نام کرده بودند.
🔹
کارشناسان معتقدند نقطۀ مهم این پویش، تبدیل «اعلام آمادگی» به «کنش اجتماعی» است. امید چوپانکاره کارشناس مسائل سیاسی پیشنهاد می‌کند این ظرفیت در حوزه‌هایی مانند امدادونجات، مدیریت بحران، کمک به خانواده‌های آسیب‌پذیر، محیط‌زیست و مقابله با اخبار جعلی سازماندهی شود.
🔹
عادل پیغامی بر شکل‌گیری «هویت جمعی» و ضرورت سازماندهی افراد در عرصه‌های مختلف تأکید دارد؛ از نگاه او، ظرفیت «جان‌فدا» می‌تواند فراتر از یک چارچوب صرفاً نظامی، در حوزه‌های اجتماعی، اقتصادی، خانوادگی و رسانه‌ای نیز فعال شود.
🔹
مهدی تقوی، جامعه‌شناس و استاد دانشگاه نیز معتقد است ظرفیت «جان‌فدا» در صورت سازماندهی می‌تواند به تقویت سرمایه اجتماعی و حل مسائل کشور کمک کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463116" target="_blank">📅 01:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463109">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Es42G4FGI8hKz1-KlIH7JkB4_whltIfoGBx6XUkPCxIEHk4dLd3G9-qVlq87YmmaTSC9WCaxWZPWmpH2tK4SZPaB3HH_xCYTop5DPtQCEW8anxdE49-EVuwBrNrYolfHrqon1mz455AQb9XslWtXF9MsTPNk9RZTeVDTCyO9xLAGzUgvIN81YVeXD2kC7Si6x1BH3pjNWK1ZrP-owROrVsSx1I0cK5xngepKWe0sHycbsKt0hZUd0Tq2voh2oqPIsHTpUVd_si5SVL8S32LhHqeG1KnsERSSG8FUIvFGdASeFEgeyfex9fssVID1TxMoMXzLIEM29qINgQUKVbBG7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2njmdvpujmldh52sLCXHkPW4nKsBQIEj7z1l5t1LsokzIu3YoLCxxoZsVtCozQCPPVu7YKNCvyZcBhc0RiGRYShD686QjXHBZM5Ho1jyyZjX-aNvU231zpHG7XvpySxstW8y2UeKecgOJbMw3tqu8ZhMNy5ZxDsoAYbFsHBQodYhBgdv38OtANAhCE0TYVBxrQYfB4xV2hnUJEO6G1wBw8aYWSQm5BNv3TIpaWs8L68X8PHReAutciMCe3Ukjsq4Y9cxfBSMX-RK2uzxE2Aw6WSR6_zUpGCh8AEuDJ8X6k9oAVQm8_qDnkkh-7xMdz8qAasOJvXxlcTdpDvkG9IGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8WX1NoTpAc-ohkqEjtVp2BYluGFqdp9nQRR4PteMZRb9UKI13tr-eQZUM3VL5dOitcMHozI_7Bodo-Na67tHJZ6eIy7kS9m22YrJZOu6hAoiVXq39lYPm4Fqm9DKd-4EmzA765yzrbqcPl2V3uKbB1p7qK36iHrvrAHNlKqshk1Jp7tjxeyAnmQfiHlOxk2z8sFBbfRYCXV6uV9TzA5FAlsPNTu3LYsgM9bEw6BUQBGwZHBGZQt-rJGYDE3YDAxQF7IpoIyV4054wBPHQV6b9bghMXhKRY7OVUsKkYoTPjZboxrCdxZtueq8llQx1Ikmrf77haeqOaN0dxRO8yAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOgdWveDNNIGS6POhTTHR6bcEQlufGUeLoLVhimfN4k7FnC5Os2gnR8EEH5NKz1xoW2WVsAKLX5JyxLRkqhzw2SQBRXM2WPoPkbeSTJTlOB25jl1g_P5qwUIURaBMaZ5mghQgC2CnnmRcRAbdzNbSGfkdju2D28zhehiCIKsIYnhRAL7Exq0JG2sM0kwvoK8RvOIsSkws5TtH-VADUkoJGFGBpCOjryfaQc_ph3ykPpbuSEPFFEhQ0_6NalJLi7FQOAwnx2p7ZN49R9uotxIJdjQOAcB7chRhb8_bhGBHscwgzVkUp-y3VBiWFGoqQJCfOLPD9X67fOmflrB5yA9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWKulD224uuSoKEfc915jUz-UV-YrdxXn821cmnoNfdgLj-0UcGaS03Nkq_YRZtvRDMyDYj6gNSzG232lLPXGrqsOp9oiStEYFQOROp29VPi2G374OQlmETFpk1GagCIUR1EdeRigYzk7TzIkNpESTRksBAVdUv3m0e5ZrIwzwnvhCTeQU6iErO5uXbYH2ii2cDy3bZ_qBOU6FBmqK75LW8RoTh9ZcBkoTciubv7QC3oxIE2JbLsQlcdS5MIgG1z9S_p65AAlAOTJyYrmHFgpBoK_5EyaPd5iggLUy6xi1XbxFOLIDDk-g_db-ECEhZwiP5t0sSX_kD6cpvdv3D-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfSBCxkdyONBo2kG-HjImTypYYTN8pp4kSGjE0p8XsvMRzLE_M1bx9bbzqWShiYgI4ygDj6kGqTDG6gCxf2yKXuvtGd-De4szQGhu10dSKXnkiWamDKVFKhM9jMYVIlSd4OdFql69LPnT0mFdoARMVhh6pJh-GCT_QUrDA-cc7sO7u4LC2PgDkQrHD6_hv9m60Cybg7ybNPs2QGKdqUTMiBscKOoOjfBMWlzoQuKmhh9UBwxUy5yCZJW6w-CZgW8MAbcVf2FKxWisJwweo2UFr_M8_Qzn0DIRjyGVaRqV4veB7cixzM4CM3rAF4wbQyFVkuiBdCNz_KIg0gB0qn1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMXFF3dP35etziQc5ieaycpK4IrrfDoUXf-MdxDUGR0ZKdcCK_PQ4xrWrQD7tXPexSwezVZR6p9E4FYv2SfZJwEOoyGGBND1XJcw4HeXJgWrvmGdGsRSqJMLDQg5B5zeFRa63gVxcmRx_dgjrz8DTTtmoY_0I-d5SDzsxeMqMS_BIyIchIUeNAo-Myx0KtnMmqS3k-8QggDW1yoAjTP8KUmjbUaQ87coPUNGnm-K3MCiD066SnyACFcuSfEBrJ2D7iLHULE2D-rMrElftY9e_dpexkMkNFN5j_pNyr08j_wmSUU5ohcRjW0jqVTyI1dL5z90nmch4AxJB5jRYfaFfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
چند دقیقه‌ با قهرمانان سرآشپز  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463109" target="_blank">📅 01:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463108">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny9HsoEmp4UNvtrQfeAEYWEQUOo-MNs13Dt2_W4h62feDiX8mHo5ExrRSBU0rcf5MCHQpPDrtybSXvrJ-a_LzzJZcFvcJF4e-ZSMRdZLc-nxxYpAQGrqqoL3uTXhEUFJJCerUXJ3ukbne_M4HCcuk2J8l1ugyawaJD55ZV-wExWwSlx5mwVBo_udD9mye0NPPkPijWxHQRiErnVtXto7cJnACRJ5Zx5ten1KumJpvEO7KZ2SLXyQVIPK5WqYjjfEllHgEa-BsGxir5CBCMYe_RPv15riybw6XEkqZBcVCFjoCHhhVPR1ezmjiRFPPC-Y-1WUQG_4L6KjDYN-r6GHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واژگونی اتوبوس بم-مشهد با ۴۷ مصدوم
🔹
هلال‌احمر استان کرمان: ساعت ٢٠:۴١ شنبه، یک دستگاه اتوبوس با مبدأ بم و مقصد مشهد در کیلومتر ٢٠ محور راور-دیگ رستم واژگون شد.
🔹
این حادثه ۴۷ مصدوم داشت، که تعدادی توسط عوامل امدادی به‌صورت سرپایی درمان، و تعدادی نیز به مراکز درمانی منتقل شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463108" target="_blank">📅 00:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463107">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqX39xbHSvg7fZcydO4w3nJZiI72W-0eX3NWz9MDNrBM0bS6DriJxKtV_ZM0MHzni0n5bWTWre74UG-uCe8uVBKmUOClaq3B7LTu_78vQknsDF6DVgjwvaJv0hva2K0noSa7elBVAp23L6KH6Vxy8zkrn9AIiS_KqPdIOPEbsAkBCks3z9Kty-dJnlCkotmF9QeQolOyNeLMDesObB9klDTDob-Ez7spBfmDSFWK4SDWpwSvWTHXThwE5M-sPvD7PpfXWhOedaAXgYybY7ZuewAPQQSedVxH131yMOe918yxW5Mn4Lrm8CKe2YoU8IZ49beE2kGNGe3nsbZOlXQiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال لغو یک بازی استقلال در لیگ برتر
🔹
استقلال ۵ آبان‌ماه باید در دبی به مصاف شباب الاهلی امارات بروند. تنها سه روز بعد دیدار هفته یازدهم لیگ برتر مقابل شمس‌آذر برای استقلالی‌ها برنامه‌ریزی شده و ۴ روز بعدازاین بازی یعنی ۱۲ آبان، شاگردان بختیاری‌زاده در بصره برابر الشمال قطر قرار خواهند گرفت. این یعنی استقلال باید در عرض یک هفته در ۳ کشور مختلف به میدان برود.
⏺
با چنین شرایطی استقلالی‌ها قطعاً درخواست خود را برای تعویق دیدار مقابل شمس‌آذر ارائه خواهند داد و ازآنجایی‌که این مسابقه بین دو بازی سرنوشت‌ساز آسیایی قرار گرفته که یکی از آنها برابر نماینده قطر (رقیب مستقیم ایران در کسب سه سهمیه مستقیم آسیا برای فصل ۲۰۲۹-۲۰۲۸) است، انتظار می‌رود این درخواست به‌احتمال زیاد مورد تأیید سازمان لیگ قرار بگیرد. به‌خصوص که استقلال قبل از بازی شباب الاهلی هم باید در یزد به مصاف چادرملو برود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/463107" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463106">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیشروی میدانی یمنی‌ها همزمان با حملات در ریاض
🔹
همزمان با تشدید عملیات‌های تنبیهی یمن علیه عربستان سعودی، نیروهای ارتش و انصارالله نیز در استان تعز عملیات پیشروی خود را آغاز کردند و مواضع جدیدی را به کنترل درآوردند.
🔹
همچنین یمنی‌ها طی ۲ روز گذشته با پیشروی در محور باب‌المندب، مواضع جدیدی را به کنترل خود درآوردند و بخش‌هایی از رشته‌کوه‌های حائل میان تعز و لحج، از جمله کوه راهبردی نمان، را تحت کنترل گرفتند.
🔹
در تعز نیز نیروهای یمنی در مسیر کوه حبشی و مناطق پیرامون آن پیشروی کردند و بر مواضع جدیدی مسلط شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463106" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463105">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">حکایتی، قولی، غزلی</div>
  <div class="tg-doc-extra">قسمت ۲۲</div>
</div>
<a href="https://t.me/farsna/463105" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۲۱ – حکایتی، قولی، غزلی</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463105" target="_blank">📅 00:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463104">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7V6zK14mFjiabaoOrK29xTDNh-CXXokXatoc-AXrTmwGR2b92hQHvRQiP0N23_AD7cRzm54OOyAXoWTggbNyZ_SKFcTk2SsoBxJ4coItDGQ5xs1Ps8XPpeMjfG60di67RoEDdJ-W0KUyYspU6IjggC1rKCibdevJbEE4_qcv_wznwnGVNtYCRlWEO6Jb5J77Ig6FZXMOxKnTN2Fu5K-ld1wP80DoWo-6pojyAmp1wzm21AUsmpm0GYFVjfWBWNTxZlhcdeU61YtA-0yqmvfFyk4Pv-BF_2msPe1g_HenOlS-t982owDd5yX3zRHCrJgrlvLro0RsQ-9UmtQ5ho9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی اسرائیل به جنوب لبنان
🔹
جنگنده‌های رژیم صهیونیستی در چندین نوبت دو شهرک کفرتبنیت و النبطه الفوقا در جنوب لبنان را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/463104" target="_blank">📅 00:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463103">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGeGmPpKmBRHvPlRfdXTvF2Jc7v-YQ1OO1rAlr2E-A1nrisO1ByDWXsKt3PuoInHv7qIllEnguC2kcSwU0UEqhfEiMJmQITZ-RadXIDKQnnG7zndPfs8oJNMaW5m5WgiEox3NpAVafNZLMLAk8TdG1ag9QQ-kx50aKcDIGYS14RfxYaZuCm9nr4h9J-GOpYmZO7iis6aL0-Xb7GAtbYhTMTiJM1KTUqzjcbiIZeZH-5PhWD5mg3r4-WZNZ4bcbTCqd_kgQc1pA8f5eOGEfjrpTQ7KxS97cO3AWbZAYgxz-wKQwxxWGNOUabhqBPm5aMyS-yCcETbPwkoDPsMISg2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتدال در عبودیت
🔹
روزی امیرالمؤمنین علی(ع) برای احوال‌پرسی و عیادت به خانه یکی از یاران خود به نام «علاء بن زیاد» رفت. وقتی علی(ع) خانه بسیار بزرگ و مجلل علاء را دید، به او فرمود: «با داشتن چنین خانه بزرگی در این دنیا چه می‌کنی، درحالی‌که در آخرت به آن نیازمندتری؟ البته اگر در این خانه بزرگ از میهمانان پذیرایی کنی، صله رحم به‌جا آوری و حقوق واجب الهی را بپردازی، همین خانه بزرگ برای تو وسیله‌ای برای رسیدن به آخرت خواهد بود.»
🔹
در این هنگام، علاء فرصت را غنیمت شمرد و از برادرش «عاصم بن زیاد» شکایت کرد و گفت: «ای امیرالمؤمنین، از برادرم عاصم به شما شکایت می‌کنم! او عبایی کهنه پوشیده، تارک دنیا شده، خانواده و زندگی را رها کرده و فقط به عبادت می‌پردازد.»
🔹
علی(ع) دستور داد عاصم را حاضر کنند. وقتی عاصم آمد، علی(ع) با لحنی تند و عتاب‌آمیز به او فرمود: «ای دشمن‌ جان خویش! شیطان تو را گمراه ساخته است. آیا به خانواده و فرزندانت رحم نمی‌کنی؟ آیا گمان می‌کنی خداوند نعمت‌های پاکیزه‌اش را بر تو حلال کرده، اما خوش ندارد که از آن‌ها استفاده کنی؟ تو در پیشگاه خدا کوچک‌تر از آن هستی که این‌گونه با تو رفتار کند!»
🔹
عاصم که غافلگیر شده بود، پرسید: «ای امیرالمؤمنین، پس چرا خودت جامه‌های خشن می‌پوشی و غذای ناگوار و ساده می‌خوری؟ من هم به تو اقتدا کرده‌ام!»
🔹
علی(ع) پاسخ داد: « من مانند تو نیستم. خداوند بر پیشوایان دادگر واجب کرده که زندگی خود را با ضعیف‌ترین و فقیرترین مردم اندازه‌گیری کنند تا فقر و تنگدستی، مستمندان را از پا درنیاورد و رنجور نسازد.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463103" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463102">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زخمی‌شدن چوپانی که حاضر نشد به خرس شلیک کند
🔹
مدیر حفاظت محیط‌زیست کهگیلویه‌وبویراحمد:حملۀ خرس به چوپان ۵۵ ساله در محدوده تنگ سردو روستای قلعه بنی چرام، منجر به مصدومیت او از ناحیۀ پای راست شد.
🔹
چوپان طبیعت‌دوست با وجود داشتن اسلحۀ مجاز به خرسی که به او حمله کرده بود شلیک نکرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463102" target="_blank">📅 00:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463101">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa14e10ebf.mp4?token=fOegApDcpH9PHOCruzQn88h006-0NwtF0vG6LGwqRYMxEAxdodevB6zd2G2e5BimH2J9yu3ilXMbYoRJVBBMiWZ2Tei043wteqfq1i9UkHYSjEjWliT-YssgeaBZ4n6ctPAQDL8Wp3GHR42827HCKxOEz57oVTtZRa-TId46iB0H97HsaZjLTQu5mP1Ikr2DjslzN-skqABE4kSuyugRgyKOpq1haP_FqGVC12V4DvjCpN03MR2RnbRZL_Jww7FpGYzFPKlrdLl73j4beZyf3hlXJ_4wBXmTwlihs65oDVwJ_WY58lrWcD54JDbvMg-7XLiFfnbCvZzNlI7cN1stSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa14e10ebf.mp4?token=fOegApDcpH9PHOCruzQn88h006-0NwtF0vG6LGwqRYMxEAxdodevB6zd2G2e5BimH2J9yu3ilXMbYoRJVBBMiWZ2Tei043wteqfq1i9UkHYSjEjWliT-YssgeaBZ4n6ctPAQDL8Wp3GHR42827HCKxOEz57oVTtZRa-TId46iB0H97HsaZjLTQu5mP1Ikr2DjslzN-skqABE4kSuyugRgyKOpq1haP_FqGVC12V4DvjCpN03MR2RnbRZL_Jww7FpGYzFPKlrdLl73j4beZyf3hlXJ_4wBXmTwlihs65oDVwJ_WY58lrWcD54JDbvMg-7XLiFfnbCvZzNlI7cN1stSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین گِرهی که از همسایه‌تون باز کردید چی بوده؟
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463101" target="_blank">📅 23:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463100">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ba59290f.mp4?token=or2v1pGfoBuXXb4lb9oWdeEUO2fk1B_crv0dV7diLyjnkV2n9r7H6dN0NIJtmXN659RvJLtiC645wDUT8OWrqnMJtD0qw-lVwO6QA3c2ym3CE757pL24Nm-vS4Wqr0Mr_mfEaz4iiGWSwzeDAEkuIT1NibCwb2uwhWVaWspUcyXuMaZXwfGsxDf1y5K0r8cqdi9FZLIJ3Rh6KjKVMDHl46HZOzYTo6CoO0_oBp0ZcU4cIDRljgdu7RqNWdDakPKgA9w7zYFONDurEvgbr4BHbg1IbKBgFFqXARM78gdL-q4TDh1yrV8cIQPfNjTTYEWeiBele_jbC1xiQ4NxBiehMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ba59290f.mp4?token=or2v1pGfoBuXXb4lb9oWdeEUO2fk1B_crv0dV7diLyjnkV2n9r7H6dN0NIJtmXN659RvJLtiC645wDUT8OWrqnMJtD0qw-lVwO6QA3c2ym3CE757pL24Nm-vS4Wqr0Mr_mfEaz4iiGWSwzeDAEkuIT1NibCwb2uwhWVaWspUcyXuMaZXwfGsxDf1y5K0r8cqdi9FZLIJ3Rh6KjKVMDHl46HZOzYTo6CoO0_oBp0ZcU4cIDRljgdu7RqNWdDakPKgA9w7zYFONDurEvgbr4BHbg1IbKBgFFqXARM78gdL-q4TDh1yrV8cIQPfNjTTYEWeiBele_jbC1xiQ4NxBiehMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند دقیقه‌ با قهرمانان سرآشپز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463100" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LO0seEJWVVwrEz6MDNvpudRvzxcaIDdf_l_cOsYNkeRWOrFebKkkcdVD6H1K_J4bh0xuHuFSphJwxo8pCOuMG_zvJPgz5IvizkimZsQ1oHRNgtQ8ToUU-s7TvPdlKZwJdp4Vg4d3WvWduKuXFI5Akue5f71H1Tnz2vl1ncXDLraWVjwrQ1A8xYJO0kL1lA3KUBPIBVJ_YVys8mfBKx3n6xUMCkca-g_JjYJWGOg52Zw8YcmwXGargZuWZhYqw07xarA7qJwHX08JUAKTkxVEI5cyBcv4NkPhlo7fywKfxuZ_ZPf4V5IOYkr1r9DdE78NWTxHo8ivqneHWyTEZFRThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQ8Mdcw1kI0AzhKIZcv9rRuoZ41fNAlPUmUkTbGqijTsmGE7lVRVRS0TYTtYR42Ri5NsmCf6x0VQ_NHrP7DkoKnsokHBJPp3-eiFMA7gCmBe_4O9EblNYnNmpDsaKvspYUrAJ6jyRq0Ymn806kBaYv80mIOrdYYVqS-kbYzADgiRZzqNCW22M49gvQOJJCTFLICGPQTJB85itGe9xjG_byHtjMkDwMqIQo7dM5QvTNKAKIwU-l94BZ-GnruYXRgEZ4JOCUZLkOgoczFMOAwKq-S8FjL27MrT37uXNtlOzy_JVN6Ssg5GuSL_4lFNzN9SCaPdDHpIqdu3tyT0DTLyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh27f7mBOy6mISZgNibN1xFjKVIbbOAoOF_fFDJq9liv42JkiQFEydHfBEbR5-d4N-d4epmI4csunwikUVxoisBUfjFxHuVAJRT8BzUouMra5R7zooAK0JmiB9wVTmLSOhYaR8NF_zKkjxjwTzBrJMwcLtOBDtuRiCx99OrzlgVNCWvJZA7_OikBw86093-BNFPmcb9Y89C58mMfBvr7hN3CjRSThI09nzviry2RnDLIOCp54RvkpoEmNSDgDR9kbedB0won-knAmrKiveh5iz22ofEw-Z4wA3mbTfC2CaPhp4etYVG0p4ALZh1Mo3eZPHhqTQeezlIzodNCVQ55qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZCwbuKKm--T0C-4Fy2RiZ1OOwVuB1-v2PvE9FtVqhoZRFOgsGKEsMBPXf7p2Lh0WfLRu8FWw6RZg8z7_wE5uy9oOtfpo8l5M1voQhJewX2zIS7VvDHYYWw71HVv6bTvZ4i1MSMrF3Sc9IJ_tSvgIKaLFkL5KVaw0G6yF78bcAIiVDBMV5y8IcnzorPWS-MCoIfZ6eQkrDa_BzSHeQonJpGf5fyAAM8TxucaT3yD8lamU5EZRTxM7N3TArbHETGxSYW7hYWQuTbF84-B9yAGmjlbODw24HwYAqhyklyk-8Xr8Uw-MXuTqZNl3Gup26fmn0jzKlMqNebrjFJF_aUY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZormU34TPPiwvvLqyfH5Xoe4SiRDaR0p6EB9a1l_PkdPRHspeRnJsjMwbpX1W0SJihXXkwSv_8rddCKqzrGVnKfn9oMROGHR2sHr9XGSHa4VfcC3Ho53B6SRMv6nZXe293WVB8Y7zn-bAQb5CdwD_tRRp5zXeYgtzGFobMTav2YFwWFCkauZWDcIlUXNeXP4bFxa-9gFfrdHTlTudPykpwUsWVunaODUMmcvh9OZZ983hRltBQdJnBibB0HiYct7OxRdhu4QJHdRu3KkLiCFibLUqiEgQNS5xlw87-HzYS7SSHUqB7oeiy6Q75HN21PlJueMCccfOo4wqQ2_rDQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEmLIw21pnWLyg2AKEvqdxFh4pCBaeZ0iguPVWpkJqdwoFMjWmbWCRd32lMU_wpNBADxnYSETtkitFB8O6iuUJ_V-ESYhQEv9ZD-qVy11w4XZV4q-88O0SqCLcyXzC5R23MFNzzZCDN2ljbcSJCE39tNIYUckSBC49gGxWLU4VcRn0LiOq5SzCtvagZg9ERiIpWqeu_Uft0dAUwMY4zx38sQqeI7UL0RGTpD_qQE7eBoNXlJo7t6y2DYmYMeQqvkOeRtHBUVGCeb7ClNNt4B7Nxx09_kxxFw4qkq5tuXUuhBdhBv0ARGUXm6vx4tCscEHH4dxba0rNFdJOMP9854qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbU8sqOjJg85YAWBEBJwLH-lnWB-R_4LZfQ1i1yKzyuJq6ctUw5uH4GCUQsZj35Oydt8d0FPrWs8lVOOS2aCv98Vlu1CcgwujsUgCEithE0gCMOyZ5S3FKQm6s-vth8PcTU5a2O6qh6i_gUScdQpSjczXGB56VXMldLMWUGN-QLOCwS4OgVZ7EnHVhOv5fRQU-CMafG4IKYMXHly6ySlQ7sH-1WNvPmye-aYeuzjY_d_KC2mHXUHIeLzX_rnZLHC6rhiAbuE8TtX9qchpkhzDFs_mFXR0jKlvFzFclROoTeEHcFtTmKo1Cn2PwIG011H4MBzbi65yHVVjLEbgcrXcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت‌های لیگ کشوری تکواندو نوجوانان در البرز
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463093" target="_blank">📅 23:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au8YxMcoICku4h8ZCqSlk1gyySXqUoL23-2N8VUJLuPJ-xJ6n2gENTfyoWPhSbCcyFg2N3X7K_HPZs0h1eJ0NBF9tbYHHRJ0HTdICpwFtttjbIyTClhOc1NVCEMlUTmamLbCQDS4BkzTFnonD02Y8HtHcaFnYeYvwvnGmXxuM5GsyXobTVsdrGFpSzd__QdNCy1emFX7q_mijxTSKkGW0s82CT1iKszDi-jZiKP4fILGKC0qH6P7ORyc9f36sYYbLqOWBEA1_UfaDwaEFO5VyKfw5YvVlHyCXs5y8G4p2Io9Y8kEd5cLTZeyGYnwtON-dUIc22op-XGqv6cdT-Kjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق مکه؛ ائتلافی برای نجنگیدن
🔹
عربستان سعودی، پاکستان و ترکیه امروز جمعه ۱۶ مرداد در مکه سندی امضا کردند که از آن با عنوان «توافقنامه دفاع مشترک مکه» یاد می‌شود. مهم‌ترین بند این سند، بر اساس بیانیه مشترک سه کشور، «اصل دفاع جمعی» است؛ به این معنا که هرگونه…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463092" target="_blank">📅 23:04 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
