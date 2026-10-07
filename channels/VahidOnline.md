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
<img src="https://cdn1.telesco.pe/file/AT90TxkK8JDdRPBzDWjrWV0jagwBNxFRA74JnY1TV4jEDdLOUetURKANCuwaw5Skt9ioA2wi1U_4CAFscmaCN7O-NJufw70fuWItxZodYnudOrVLIw5M_OPd1ZoXBt87xaacrGMHKz9bPKyXT7vAzM0RClcnTpZJ3cSekPwEO1ojsUtiyyw-s-Eygh-GPZfv9kkBH9Ai5VERZw93La1U3eESSXwdCzVM-8PK98cKDmFaEjeAWHJ3kLqglGIKe7KwSiejOrOOQ12gT1PinlAnNOj8pk_1ytha3QN0abp1I-lyVKejYwoo9oBcxDaxFdMFpoTWxbDkNsDG9EUUzK8uPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی می‌گن. اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جوری که می‌خواستم به خودم نشون داده بشن می‌گذارم.ممنون از حمایت‌های ماهانهvhdo.nl/patreonیا گاهانهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 06:03:32</div>
<hr>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM0hkxXKRqIXKClUAucJ1ak83kj1Yorn3Krl4AdS4ubCSrqfaBLbc7x8gnnp1gPDUvnFA7RjGZnVx-7NCp4Ob91OVi0raye0ZGQSPCB2yiEm8RbiTJhKCb4RcS0h0J_llNpRohDvpil_L2emZ5uxtkJvAcowFd7bxSW6PxyoMQODkDbkVBwXPxKrHb-bMzPry_OXUNi9mcIlSUvLd8ejVgNLaR570GydA7t_xhaDbYBnew1qIPrcmNAgbOhC-ROnou1GeV6PrLwpHDlGU7MvaPMyHcpfNFfX_ugHQYSLEn9t7byHTG8WuumnGKiJpJ9frJRFQ57vfBPRlGcjY06_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در مصاحبه با خبرگزاری رویترز گفت: «ایران برای تحقق خواسته‌های آمریکا و پایان دادن به جنگ هفت‌ماهه دو کشور باید به‌طور معناداری ظرفیت غنی‌سازی هسته‌ای خود را کاهش دهد، نه این‌که صرفا وعده کاهش آن در آینده را بدهد.»
ونس خطاب به مقام‌های جمهوری اسلامی گفت: «اگر سلاح هسته‌ای نمی‌خواهید، پس چرا به سوخت غنی‌شده ۶۰ درصدی نیاز دارید؟ و اگر می‌خواهید تعهد خود را به عدم تولید سلاح هسته‌ای نشان دهید، سوخت با غنای بالا تولید نکنید. این یک مسئله آستانه‌ای بسیار ساده است.»
او اشاره کرد آمریکا همچنان برای دستیابی به توافق آمادگی دارد، «اما خواستار امتیازات هسته‌ای مشخص از سوی ایران خواهد بود.»
ونس افزود: «قرار نیست ما کلمات را با عمل معاوضه کنیم.»
به گفته او، «یکی از عوامل پیچیده‌کننده اوضاع این است که واشینگتن نمی‌داند چه کسی در تهران تصمیم‌گیری می‌کند.»
ونس گفت آمریکا با مسعود پزشکیان و عباس عراقچی در حال مذاکره است، اما مشخص نیست آنها در ساختار قدرت ایران تا چه اندازه اختیار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/VahidOnline/78644" target="_blank">📅 02:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=cYrBlT3sEnXRzWi3Wz75UvcgkTrqx8dsGKH17RSIAP4rHKmZ84u-kmMQPmWaazXHDaCUP2at_M9R_8V8mdKcHkPaaakun_cVvFTDW7TLjkjk8g_9mSWWE0X6FQfTBz_j2c4icpkieu4F0wEPYjqBkD2ddtzXRy1pDuSa6HsPvWscf6F2byz_IgEquEXaJUFWg2qVubIZfele5mNRbm9XCLv2kOiyegnRRk-mNVYHIPyTYg-jzP97xiRTr_8MGBfoqC-7jTFEANvRUficMxxlL5S7fvPKlsHwgE-oOIuBvStcQ_ycwarefEOorjghUGWmChPlcGqWDgtq96ufpUVvKyIeyKUezwLoK1wcqdrBUZQx0qfIVjkqY1mwZPKoUz-aA3TU9U-qWV5v2no6ScnVDSxfTL4jiG3KIYXBWC8qywkl4XOyyveXPV_L6g-d1Bm6l1KNlDEXmuRvkr5FxiCdPBNERWUjarHCC2Jz3rtLQFN6ULLJpXm-IfVIdzwlhZ4FDbR1MuQvGx6DXja7AassQz1A8qhO8hK68c2vu_g5C1fF4ijdHmfr3H2VoNpQ-pjbVoNMMnHuyd09_xIcAyeLNFngs1PY9lzS85f5_djBsta43iKtiIEw6-hTNNkCOsQXDlja0LFalBvfnnOBiVx2_QyqvpTT9Mnrf_4nhTmRrRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=cYrBlT3sEnXRzWi3Wz75UvcgkTrqx8dsGKH17RSIAP4rHKmZ84u-kmMQPmWaazXHDaCUP2at_M9R_8V8mdKcHkPaaakun_cVvFTDW7TLjkjk8g_9mSWWE0X6FQfTBz_j2c4icpkieu4F0wEPYjqBkD2ddtzXRy1pDuSa6HsPvWscf6F2byz_IgEquEXaJUFWg2qVubIZfele5mNRbm9XCLv2kOiyegnRRk-mNVYHIPyTYg-jzP97xiRTr_8MGBfoqC-7jTFEANvRUficMxxlL5S7fvPKlsHwgE-oOIuBvStcQ_ycwarefEOorjghUGWmChPlcGqWDgtq96ufpUVvKyIeyKUezwLoK1wcqdrBUZQx0qfIVjkqY1mwZPKoUz-aA3TU9U-qWV5v2no6ScnVDSxfTL4jiG3KIYXBWC8qywkl4XOyyveXPV_L6g-d1Bm6l1KNlDEXmuRvkr5FxiCdPBNERWUjarHCC2Jz3rtLQFN6ULLJpXm-IfVIdzwlhZ4FDbR1MuQvGx6DXja7AassQz1A8qhO8hK68c2vu_g5C1fF4ijdHmfr3H2VoNpQ-pjbVoNMMnHuyd09_xIcAyeLNFngs1PY9lzS85f5_djBsta43iKtiIEw6-hTNNkCOsQXDlja0LFalBvfnnOBiVx2_QyqvpTT9Mnrf_4nhTmRrRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ، به تشخیص و ترجمه ماشین:
ما در جمهوری اسلامی ایران خیلی خوب پیش می‌رویم؛ خیلی خوب. آن‌ها دیگر نیروی نظامی ندارند؛ نابود شده. همه‌چیزشان نابود شده و آن‌ها همان طرف شرور بودند؛ قلدر خاورمیانه بودند و دیگر چندان قلدر نیستند. اما هنوز باید کار را تمام کنیم و فقط مسئله این است که به کدام روش. می‌خواهیم این کار را به روش خوب انجام بدهیم یا به روش نه‌چندان خوب؟ خیلی زود خواهید فهمید.
وقتی به «دیوار فولادی» نگاه می‌کنم، همان کاری که ما انجام داده‌ایم و آن‌ها اسمش را محاصره گذاشته‌اند؛ من اسمش را «دیوار فولادی» می‌گذارم. حتی یک کشتی هم نتوانسته به ایران برسد. تنها کشتی‌هایی که عبور می‌کنند همان‌هایی هستند که ما اجازه عبورشان را می‌دهیم و این تأثیر بسیار بزرگی داشته است.
برای همین کشورشان از نظر مالی شکست خورده است. یک کشور شکست‌خورده‌اند؛ همه دارند کنار می‌کشند، همه دارند می‌روند. به نیروهای نظامی‌شان حقوق نمی‌دهند، به پلیس‌شان حقوق نمی‌دهند، به هیچ‌کس پول نمی‌دهند؛ اوضاعشان به‌هم‌ریخته است. اما هنوز باید کار را تمام کنیم.
نیروی دریایی ما پیشتاز است تا تضمین کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. و این همان چیزی است که همیشه گفته‌ایم: هرگز اتفاق نخواهد افتاد. هرگز اتفاق نخواهد افتاد. این دیگر یک امر انجام‌شده است.
ملوانان و هوانوردان دریایی بزرگ ما قهرمانانه جنگیده‌اند تا ارتش آن‌ها را نابود کنند. آن‌ها دیگر نیروی هوایی ندارند. نیروی هوایی‌شان از بین رفته است. نیروی دریایی‌شان از بین رفته است. آن‌ها ۱۵۹ کشتی دارند؛ همه‌شان همین حالا در اعماق دریا هستند، کف دریا افتاده‌اند. رادارشان از بین رفته است. تمام تجهیزات ضدهوایی‌شان از بین رفته است. ظرفیت تولید موشک و پهپاد آن‌ها به‌شدت کاهش یافته است. به‌زودی آن هم از بین می‌رود. دقیقاً می‌دانیم بقیه‌اش کجاست.
اقتصادشان ویران شده است. تورمی دارند که هیچ کشور دیگری در جهان ندارد. و آن مردی که چند روز پیش رفت، گفت: «من می‌روم چون کشورمان تمام شده.» این را گفت. نمی‌دانم. من هیچ‌چیز را قطعی فرض نمی‌کنم، اما اوضاعشان خوب نیست.
و به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها تن از رهبران تروریست ایران از صحنه روزگار محو شده‌اند و مستقیم به دروازه‌های جهنم فرستاده شده‌اند. همان‌طور که می‌دانید، رهبرانشان رفته‌اند. گروه دوم رهبرانشان هم رفته‌اند. و بزرگ‌ترین مشکل من این است که هیچ‌کس نمی‌داند واقعاً چه کسی کشور را اداره می‌کند. هیچ‌کس نمی‌داند؛ شاید هم این چیز خوبی باشد. اما خامنه‌ای را یادتان هست؛ همه‌شان رفته‌اند و حالا ما اینجاییم.
ما داریم کارهایی انجام می‌دهیم که هیچ‌کس قبلاً انجام نداده است. مثلاً تکلیف این کشور باید خیلی وقت پیش روشن می‌شد. حالا ۵۱ سال است. قلدر خاورمیانه. این کار باید خیلی پیش به دست رؤسای جمهور یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم. همیشه ما هستیم. کشورهای دیگر باید خیلی وقت پیش این کار را می‌کردند، چون با گذشت زمان فقط بدتر شد.
اما ما کار را انجام دادیم و راستش مدام از رهبران جهان تماس دارم که خیلی از من تشکر می‌کنند. می‌گویم: «خب، کی می‌خواهید هزینه‌اش را بدهید؟» می‌گویند: «آقا، بابت این کار خوبی که کردید ممنونیم.» و من به آن‌ها می‌گویم: «عالی است. می‌خواهید چند کشتی بفرستید؟» می‌گویند: «آقا، ترجیح می‌دهم درگیر نشوم.» آن‌ها هیچ کشتی‌ای ندارند.
واقعاً داریم بار تمام دنیا را به دوش می‌کشیم. روی دوش ماست. و به یک معنا دوست داریم این کار را انجام بدهیم، چون خودمان قوی‌تر شده‌ایم و دیگران ضعیف‌تر شده‌اند. آن‌ها فقط ضعیف و ناکارآمد شده‌اند و ما کارهایی انجام می‌دهیم که هیچ‌کس دیگر، هیچ کشوری، هرگز نمی‌توانست انجام دهد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/78643" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141ace0942.mp4?token=JqVW5CU-R8iRJ8J6Hxk-EBayZiPQK2bt0YxUYJ2XHkXWpKZvqZlTX8w-Sa4aneLpGmefGv9YNn3FSIXLAAoHely3cS4cOovefvlYeluCBdcRpZj4t5dMJAAc60LESBVhRqZ6GyLPQd6A4mJM7PwVw4MAHem1T9tAyTu9lcp0eXAHeYOK9gY8_fZ-5TxfBlqfeJNKnwvLNl1kubh7oOv1oCDqHpOvx1ZAZj8siYdv99Su62esAL5fait3ODNSJ5ZUfOiLMGw-dDc-Z1sdDPDW7phsv2irCUXfrDFzODBALUj_cy4cuaqmSalR7wWQG3GMMixucymwmHyDBiVM8c0l6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141ace0942.mp4?token=JqVW5CU-R8iRJ8J6Hxk-EBayZiPQK2bt0YxUYJ2XHkXWpKZvqZlTX8w-Sa4aneLpGmefGv9YNn3FSIXLAAoHely3cS4cOovefvlYeluCBdcRpZj4t5dMJAAc60LESBVhRqZ6GyLPQd6A4mJM7PwVw4MAHem1T9tAyTu9lcp0eXAHeYOK9gY8_fZ-5TxfBlqfeJNKnwvLNl1kubh7oOv1oCDqHpOvx1ZAZj8siYdv99Su62esAL5fait3ODNSJ5ZUfOiLMGw-dDc-Z1sdDPDW7phsv2irCUXfrDFzODBALUj_cy4cuaqmSalR7wWQG3GMMixucymwmHyDBiVM8c0l6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ یک کارمند ۲۸ ساله موسسه تحقیقات ضدطاعون در سیبری پس از ابتلا به بیماری که گمان می‌رود طاعون ریوی بوده باشد، موجب نگرانی‌هایی شده است.
بر اساس این گزارش‌ها، داریا شیپیلووای ۲۸ ساله در ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) به بیمارستانی در شهر شلخوف در منطقه ایرکوتسک منتقل شد و دو روز بعد درگذشت.
ده‌ها نفر که با این زن در تماس بوده‌اند قرنطینه شده و تحت نظر پزشکان قرار گرفته‌اند، اما مقام‌های روسیه می‌گویند تاکنون هیچ مدرکی پیدا نشده که نشان دهد مرگ او با عوامل بیماری‌زایی که در محل کارش با آنها سروکار داشته، مرتبط بوده است.
مقام‌های روسیه می‌گویند وضعیت تحت کنترل است و تاکنون مورد جدیدی از بیماری‌های عفونی مرتبط با این حادثه گزارش نشده است. با این حال، گزارش‌های تاییدنشده درباره احتمال ابتلای این زن به طاعون ریوی در شبکه‌های اجتماعی منتشر شده است.
مارکو روبیو، وزیر خارجه آمریکا، گفته است واشنگتن این موضوع را از نزدیک زیر نظر دارد اما در حال حاضر دلیلی برای نگرانی نمی‌بیند. دونالد ترامپ، رئیس‌جمهور آمریکا هم اعلام کرده که آماده کمک به روسیه است.
@
VahidHeadline
, @
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78641" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jqp4DC7jdcipoCp-RVu_Bm6wx7PRiRK2_fwLQRkIXD6Z7yRji8Iaeg2aD0lVh47aTAW8ZE357n8quLIJQMGALqYWD3xcwNqOpvXIHXYeLS7DYfHoR-zxkktqecoi6dyt_p-9UuA7-AaehfOO_YVZ4O5uv8RvbtbAJ27rxOxC26cX9rYolMn2fXw1k5rAcr2seV8JI3jlq3mGXtZpjQlI0ProBNM-YKL3QGkI-zxjIiRc8LM5V0J9oyjCE_OboFy3lUnyXxumzBVCOuZYt1qL62UD5wsWVQJgdKtrbARDTTNV0aGtRPtW0agcIf9YI5o4ffGtsXxQ7Ek27MhpBMGOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران گزارش‌های نادرستی را منتشر کرده‌اند مبنی بر اینکه یک بالگرد MH-60R نیروی دریایی آمریکا، پس از اعلام وضعیت اضطراری در شب گذشته، در دریای سرخ سقوط کرده است.
✅
واقعیت: گزارش‌ها درباره سقوط یک بالگرد نیروی دریایی آمریکا در دریای سرخ صحت ندارند. همه هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه در امنیت هستند و وضعیت همه آن‌ها مشخص است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78640" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIDEGOvKtqnDNH3YlCnJVVD6_KdWnr7IYb_DIrz5kdlA51Tg6CBenBW6UsAfWXJaMVxtWWumLPssRsblBL0_hsuRWWx_2BKcLNlrCNAsVSZGzk3u-gNXanoq7Rb6HOlK3dnPlXS8Cf2B3yUmXTwsFXsorcFfpd652sDIxz_3N71jcpWSe1qGVkLhBHRot18vy_egukgKljywWydJoczONHit5dv36ZQ0neLT0_XUoLYPc2FE5RcxE6jyAnSfvCgN95jHfGteaMt6DdoChBkNCGgtIZPP7sngqaGKz5e5RHnZjMh3WV-ZISWnsbI4nTMqDfPD6sl2E4zsW5zVOvSe0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا بعدازظهر سه‌شنبه ۱۴ مهر اعلام کرد گزارشی با تاخیر درباره حادثه‌ای در تنگه هرمز در ۱۳ مهر دریافت کرده است.
بر اساس گزارش یک «منبع تاییدشده»، یک نفتکش هنگام خروج از تنگه هرمز هدف حمله قرار گرفت.
در این اطلاعیه به هویت نفتکش، عامل حمله یا میزان خسارت احتمالی اشاره‌ای نشده و سازمان عملیات تجارت دریایی بریتانیا اعلام کرده است مقام‌ها در حال بررسی این حادثه‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78639" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdgP4LcNlNhkuB4Z01r88YqROgkoIeRCaFkqIooaU_tr9eQ4juE6z5GVVy_sShzrvJP_hQfWbAKYQBiQ4ZZXcd4eaVbswEHlgpIh6GOoB2OAQNQk_eYv5USNz8LtepDObmVOailgqZsPL5AtrOqL5nrlV4IWL1PiO06WWgTWEBy5azQ5XyXnGXZijlSQNAluoyUn1B3Oenv_pcRxflTqe-xgIj9CUbxK_Wb_cTnWfIdUHpiuDA9LH0fO7102A8tRjgWYAbmzoO_UP999RVoPJ5rXlP6grCtJYKXbdxOwgQMX_QLvVDmSROEKucJPxoB_PDZX4hluEy0cxasg5ZdBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز سه‌شنبه ۱۴ مهرماه اعلام کرد شامگاه دوشنبه، فرودگاه بین‌المللی ملک عبدالله بن عبدالعزیز در جازان و فرودگاه بین‌المللی نجران هدف حمله قرار گرفتند.
براساس این بیانیه، این حملات منجر به جراحت جزئی سه نفر و بروز خسارات مادی به فرودگاه‌ها شد.
شورشیان حوثی مورد حمایت جمهوری اسلامی دوشنبه از حمله به فرودگاه‌های عربستان سعودی خبر داده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/78638" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7wrk_mx4Cb9pHBTab4ncdSsmsxprAZ18JdHVVnlfLt6fOcDDPCwsNsLVWH-vYpEUF1uVTzZmBLwiDa-7O2EE5GtpdVo6VtmvcmCN0Cef-fBuKgkmbyHC_xpxMCvY2afLtBQJhnaPhejibkPazovNgBhO4FBsu6YczsX4qVOWY8PZyAvSbDyI0s-CXc-D90oNSMvx5DPCQC6dUueRuLZdmwRFvBEOhBs-7bbNbfP_sN53wF5_G0lRMEs0Mk1INYha0GtL3Fulg7gKm988Vgtjq-Fw7G14h23RMHqD_0a69wwuMMAS1OJYCX0mdW5snzSDdKD6P6r1Fy35n-IkYHf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشور قاره آمریکا در بیانیه‌ای که روز دوشنبه، ۱۳ مهرماه، منتشر شد «اقدامات تروریستی» جمهوری اسلامی و نیروهای نیابتی‌اش در نیمکره غربی را محکوم کردند.
در این بیانیه به «تلاش‌های خصمانه ایران و نیروهای نیابتی‌اش از جمله نقشه‌های مرگبار، تأمین غیرقانونی پول، مداخله سیاسی و فعالیت برای نفوذ خارجی» اشاره شده است.
این بیانیه اشاره می‌کند که هدف از این گونه اقدامات «تقویت شبکه‌های تروریستی، تضعیف فرایندهای قانونی یا دولتی و ضربه زدن به امنیت منطقه‌ای» است.
ایالات متحده، آرژانتین، کانادا، کلمبیا،‌ کستاریکا، جمهوری دومینیکن، گویان، پاراگوئه،‌ پرو، و ترینیداد و توباگو امضاکنندگان این بیانیه هستند.
این بیانیه پس از آن منتشر می‌شود که آمریکا و پاراگوئه در ماه سپتامبر گذشته به طور مشترک «نشست مقابله با تروریسم فراملی» را با هدف همکاری در نیمکره غربی علیه «فعالیت تروریستی» تهران برگزار کردند.
سال گذشته اکوادور که متحد آمریکا است سپاه پاسداران، حماس و حزب‌الله را سازمان‌های تروریستی اعلام کرد و آرژانتین نیز در بهمن‌ماه ۱۴۰۴ نیروی قدس سپاه پاسداران را در فهرست تروریستی قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78637" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MFz6FG7KsKLUKZ0-b05GYQBkuFI5zaESJlPAf6bTy7Ybrd4_M5EBGNQ7I4fntjiSJ54Gb2n3mm2YanrFPH6JEqH_QAXHcusek_PMN1lc4Ifq1x3Wlmiv8B-TyIklKCtZ6ojUXyutxPgm83ynrztqOLkeGopE_1DYg_C8ts896LVNUif9IT7PoPiI-gem5xE9jdV1dAZLjS5lCO5lwdkAkVzw6Oh15uMpUSD7uDQRCqCEM5ZCtjWioRcVZJGFFy0o6Ck9crG5fxm3JRX3JSZB34Z-bnRLxM0xrYZ37DSis-3jgd1qFhEVRt3cz1JGpOZZKglnDApm0aPMqzYULqgNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی عباسیان، ۳۸ ساله و ساکن شیروان، از سوی دادگاه انقلاب بجنورد به اعدام محکوم شده است.
یک منبع مطلع به ایران‌اینترنشنال گفت حکم اعدام عباسیان یکشنبه ۱۳ مهر در زندان شیروان به او ابلاغ شد.
هادی عباسیان در جریان اعتراضات دی ماه با انتشار ویدیوهایی از مردم خواسته بود در اعتراضات شرکت کنند.
تاکنون اتهام دقیق منجر به صدور حکم اعدام و مستندات دادگاه علیه عباسیان مشخص نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78636" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RySUCfoHgJYes75P63Z8JyUFdlCB-ST4oT3IhMaxGihaTRWUh9xUUAcXH0kkr_BzzvwbCoyi2mgaAGDx_-Br-KAt3-J2t-rXK-H1rt68aNQuMV-Bj9DW6ntcf8-QgWRIN4VaDAHx_KLjsfFLCbjUZmtdq0a2Z1rd7gzg-kYhsR7E2s-wT_bSsh7w-xLf40RRHvRFNCS0Ox3HmRD4CN1mETBFsNWo2C-dSNC-KAoA8xH_fLpqBNytX-baYedmx2ZbK9emved27bmZYY277T37LsjJpm9UVxWRC8G8dvFMkvDlKoy4ZWvqjvrPndmlR7oiC6MtGD6aR7R3H0DqFSvsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر ایران از اجرای مخفیانه حکم اعدام «تورات محمدی»، شهروند ۴۲ ساله افغانستان، در زندان مرکزی کرج خبر داده است. او با اتهام «جاسوسی» به اعدام محکوم شده بود، اما مشخص نیست دستگاه قضایی جمهوری اسلامی او را به جاسوسی برای کدام کشور یا نهاد متهم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/78635" target="_blank">📅 16:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NzD--be0wa3gLPObf_lsS0HMafVFTZ3PlBX54bmM3tQczKfs2-BXK-6szYHLMDCxP09G6jg4VltXtzX4zbsPBsjLIgW6LwzBlyTYZ3iw7pwRuSf179I_po7KoqIYedRPJ25yCxZIt1eP2VSJnVEtZCvLCXodXN3lLdGx4Mr6v21heA1tDX9ru1E3YNMsz73RuEAHAtV9JLKqLFis94s1qH18pVml1uowek1nji8Xrefg--WBhMEeyk18JT9dhzK8ePviYHyY738xvvb6OOw5wRczYqNkhGXtc_fXYDcnWB9zS_F2_Nqb6w8B7YmmgdQe-XWaqOAWwnCncUyxHdndZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SGddvF0Kux4-P3FD6vHb2mwvP3z3kkmfCOQEmkz752Rwyto6MjXNWWK7hGqCMk51X9R-XQO8laCdswndLHQjNEloAT79KXD9XgUrwSjenFEspi4VqZQ1trnQWimQmVDscLbOoO6C_Np4WJShcxIAKWZHp2xxgms70lDmdKo8UefBgzCQkNbMXATH1dSCxw8DBRjQHLJbtx3CXMimnrp7IGK4mQok5p2fopaG_V2LN4f55uikhQ3jbt_kT4A9gVZOVCPRA6PdHoiOeyr4fEiUghaDwSAty0sFMIvEYdAWN1_XEgLO6dSqXHPvNSFKEwVMKp_zbiQXVfaU71M99Hqnmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده در پی دریافت اطلاعاتی درباره احتمال حمله پهپادی جمهوری اسلامی، ۱۲ فروند بمب‌افکن بی‌۱ را از پایگاه هوایی فرفورد، متعلق به نیروی هوایی سلطنتی بریتانیا، خارج کرد.
وال‌استریت ژورنال علت خروج این بمب‌افکن‌ها را «نگرانی‌های امنیتی درباره طرح‌های احتمالی حمله به پایگاه» عنوان کرده بود.
دونالد ترامپ، رییس‌جمهوری آمریکا، دوشنبه تایید کرد بمب‌افکن‌ها به دلیل تهدید امنیتی جمهوری اسلامی از این پایگاه خارج شدند.
این در حالی است که مارکو روبیو، وزیر خارجه آمریکا، ساعاتی پیش‌تر این انتقال را بخشی از جابه‌جایی‌های معمول نیروی هوایی توصیف کرده و گفته بود ارتباط مستقیمی با تهدید ایران نداشته است.
@
VahidOOnLine
روزنامه نیویورک تایمز در گزارشی اختصاصی به نقل از مقام‌های آمریکایی و بریتانیایی نوشته است که آمریکا پس از دریافت اطلاعات جدید درباره احتمال حمله پهپادی که گفته می‌شود سپاه پاسداران آن را طراحی کرده بود، به‌طور ناگهانی هر ۱۲ فروند بمب‌افکن بی-۱ نیروی هوایی آمریکا را از پایگاه هوایی «آرای‌اف فیرفورد» در جنوب انگلیس خارج کرد.
نیویورک تایمز به نقل از این مقام ها که درخواست کرده اند ناشناس باقی بمانند نوشته:‌ «حمله احتمالی بخشی از یک طرح پیچیده و چندمرحله‌ای ایران برای هدف قرار دادن هواپیماهای آمریکایی و کشتن شماری از چندصد نیروی آمریکایی مستقر در این پایگاه بوده است. به گفته آنها، تمام بمب‌افکن‌های آمریکایی در آخر هفته از پایگاه خارج شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78633" target="_blank">📅 08:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LAdoF5P8wh9vfKWrVrxuavesg2jP4C8aDhhaBCIqHSwGxG0BcuZElomOHeyd_clvzvQFTKJ-4U6nGWmvoNuDGly5m1HBzeGALVimzlrmvq-apgok498-fY-LbZe85baG-8YgGY9mq2MOX0hxuKVAZabgv5W8kggaXUmg1U8ChwPcXgIh3DTf8-lqUOa5KRGa5m854DY7mQzlUMNXjiF6gClMj1kIPOLbhRdchvXuGrDExwMjbyjbJub6RnvQHGjkyUVzaHZhfJolM9oy5_NXbwzGCfPLA_AmPoahUKoH3oQwkXiSaTSwxA_T4BM8EeIYj5KGt_7mbJTq2fGVyjZgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TH9kKUjznn4EJEnJwh8Va3Na6y0FPS2X9xsO7UWSWMX0SJIV6KN-QoUn152-dfVZWxr34shnf3zEYVoRTcefJOgBekwPgEggvbXOFp0SOI4GR4ihCkM2-QImqQOvTRaxb-RQQnGfsu3WEH2R3qI4Rh_GdOaX-ZPF4ceXRx33GxVuh63AjWdGEpPsjgOhJdbKcnL6Chjwuu_RJdVNbKp59xb40FQOhISKp0k8-MPJBM_yzxKskPZXl1hAKysGAv64jYz10A2RrwHVQZLn8gcwk1XEDHvuUe3eC74w4EZIyT9B1_wlDjBIyDgf8kGOzWaPpvvbdN-uR27HDpnazpV80A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به سوال خبرنگاران درباره حادثه امنیتی در نزدیکی پایگاه هوایی فرفورد بریتانیا اعلام کرد که ایران با این پرونده مرتبط است.
ترامپ درباره دلیل خروج هواپیماهای این کشور از پایگاه فرفورد گفت: «ما با یک تهدید مواجه بودیم و اگر قرار باشد ما را تهدید کنند، هواپیماها را جابه‌جا می‌کنیم. این اقدام تا حدی مشکل را برطرف می‌کند.»
رییس‌جمهوری آمریکا تاکید کرد: «ما افرادی را که این تهدید را طراحی کرده‌اند می‌شناسیم و آنها خودشان را با دردسر بزرگی روبه‌رو کرده‌اند.»
@
VahidOOnLine
ترامپ روز دوشنبه ۱۳ مهر در کاخ سفید و در پاسخ به این پرسش که آیا احتمال می‌دهد ایران پهپادهای رزمی را به بریتانیا منتقل کرده باشد، گفت: «نمی‌توانم این را به شما بگویم، اما اگر چنین کرده باشند، بهای سنگینی خواهند پرداخت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78631" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=s2I3IYD30HzYkx0hnMy4DAVFyoJXUPSs7MBtm-sHl1IGPKhyqYBYlmphwOa5rYiCmub7wy24oV_7bfXmls6N4pHVhugFrssVIxxoMnEHUx_lqMzR5h10Gf5tfb7IuCLb1hpfsq2szo4j79VlMFtTHCk51e_mfU73xt7ZQxjIPzvPObyCwQgFxC7UX3bVEoxt9uVvRUhqcjOGTE74bbjowzfyt83UbYjHTaYvukh40Oxq0A7xh_f696u__64tEu5EJGI3u96npmJOexWZDpWHaO4dlO6ILeXxctqQHxKSN7vTtuNI4Vs2Cc_KeYKVGvPnYAz_koBCKSFXjYAdkQqUCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=s2I3IYD30HzYkx0hnMy4DAVFyoJXUPSs7MBtm-sHl1IGPKhyqYBYlmphwOa5rYiCmub7wy24oV_7bfXmls6N4pHVhugFrssVIxxoMnEHUx_lqMzR5h10Gf5tfb7IuCLb1hpfsq2szo4j79VlMFtTHCk51e_mfU73xt7ZQxjIPzvPObyCwQgFxC7UX3bVEoxt9uVvRUhqcjOGTE74bbjowzfyt83UbYjHTaYvukh40Oxq0A7xh_f696u__64tEu5EJGI3u96npmJOexWZDpWHaO4dlO6ILeXxctqQHxKSN7vTtuNI4Vs2Cc_KeYKVGvPnYAz_koBCKSFXjYAdkQqUCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ترک کاخ سفید، در پاسخ به سوال خبرنگار فاکس‌نیوز گفت: «شخصا باور دارم که ایران مسئول حمله تروریستی فلای‌دبی بوده است».
این اظهارات در حالی مطرح شد که جی‌دی ونس، معاون رئیس‌جمهوری آمریکا در همین روز به خبرنگاران گفت که هنوز مدرک مستدلی بر دخالت جمهوری اسلامی ایران در این حمله دریافت نکرده است.
در پرواز دبی به تل‌آویو که روز چهارشنبه انجام شد، کمک‌خلبان با حمله به خلبان اصلی تلاش کرد که هواپیما را با تمام سرنشینان که اکثریت آن‌ها اسرائیلی بودند، ساقط کند. این اقدام با واکنش به‌موقع خلبان و مسافران، خنثی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78629" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElXVHyTk4hlCObFNc7IHr1IWrrWocayL03mS1F5S2CME7eOtzhebdqCKtCCDTvFw6-00tj8gt_FFhFiRJ4fsqRLoh5FaXVoz8v90VVCJ0RhDZV9TyWFVZNxB9h7wS7V76r0nm8_JnF66FDB_pVRUX8pD-lpeVuYhiPQbweOKMMPpQfrr6HH97eOuVthW1YHg9DSUIRhIWUEkKcLk3DwhHHkSNGXhlIA_I9iM5oQXIINpuK3Wg07X_UQ9w6IfVw3gyMD75QvlR6Q5b-aumdzujYTSoTR-u-ki5yQJ9G9tmdNMNbTP2SD5KH8b9Dh6HNGVHFztiZxz2c4jJ6ToO8h0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید آنچه باعث افزایش قیمت گازوئیل شده دیگر ربطی به تنگهٔ هرمز ندارد، چرا که به گفتهٔ او، اکنون مقادیر بی‌سابقه‌ای نفت تقریباً به‌صورت روزانه از این آبراه خارج می‌شود.
دونالد ترامپ روز دوشنبه ۱۳ مهر با انتشار پیامی در شبکه اجتماعی خود، تروث‌سوشال، افزایش قیمت گازوئیل را به «پالایشگاه‌ها» مرتبط دانست و نوشت: «پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما که در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط "دمکرات‌های احمق" تعطیل می‌شوند».
اشاره رئیس‌جمهور آمریکا به گزارش‌هایی است که در روزهای اخیر از افزایش میزان خروج نفت از تنگهٔ هرمز منتشر شده است.
شرکت کپلر، ناظر بر کشتیرانی جهانی، روز ۱۳ مهر گفت که داده‌هایش نشان می‌دهد صادرات نفت خاورمیانه، بدون احتساب ایران، طی هفته گذشته، با وجود حملات به کشتی‌ها در تنگهٔ هرمز، از سطح پیش از جنگ فراتر رفته است.
با وجود افزایش میزان خروج نفت از تنگهٔ هرمز، قیمت جهانی نفت در محدوده ۱۰۰ دلار در هر بشکه باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78628" target="_blank">📅 21:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد روز دوشنبه ۱۳ مهر یک پ نفتکش در حال گذر از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.
بر اساس این گزارش، این حمله موجب بروز آتش‌سوزی در موتورخانه کشتی شده که خدمه در حال اطفای آن بوده‌اند. با این حال، سازمان تجارت دریایی بریتانیا تایید کرد که تا کنون هیچ‌گونه تلفات جانی یا خسارت زیست‌محیطی گزارش نشده است. تحقیقات در این زمینه ادامه دارد و به سایر شناورهای عبوری توصیه شده است با احتیاط کامل در منطقه تردد کنند.
@
VahidOOnLine
پیش‌تر:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز دوشنبه ۱۳ مهر، با انتشار اطلاعیه‌های رسمی، وقوع سه حادثه امنیتی جداگانه را در آب‌های تنگه هرمز و در تاریخ‌های ۱۱ و ۱۲ مهر تایید کرد. پیشتر خبرگزاریهای فارس از هدف قرار گرفتن یک نفتکش در روز شنبه خبر داده بود و روز یکشنبه نیز ایرنا از شنیده شدن صدای انفجار در حوالی جزیره قشم خبر داده و احتمال هدف قرار دادن «شناورهای متخلف» را مطرح کرده بود.
بر اساس هشدارهای رسمی UKMTO، روز شنبه یک نفتکش حامل نفت خام حین تردد در تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است. روز یکشنبه نیز دو شناور شامل یک نفتکش حمل گاز مایع (LPG) و یک نفتکش دیگر حامل نفت خام که از سمت خلیج فارس وارد شده و در حال گذر از تنگه هرمز بودند، توسط پرتابه‌های ناشناس مورد اصابت قرار گرفتند.
سازمان UKMTO ضمن آغاز تحقیقات رسمی درباره این حملات، به تمامی شناورهای تجاری و نفتکش‌ها توصیه کرده است با احتیاط کامل از این منطقه راهبردی عبور کرده و هرگونه فعالیت مشکوک را فورا گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78626" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XeB7cBMrCn23E_xRvvcyV0CYTi8DrDKLKvgISw4xBMV-pNWfXKH82tpusGg5w76p5NV_3eCg6h6quty20cfR5nsncA_hMWFcG6F572GpBrNxCQLw2OQFgAIJxy5qThwaBC7BDmiLs-jYrRN2-3eNZGzQaBl1NsQZHTenCIjhTiKT1sJuNvY6ExS2kZUTqBrBqgiL0UuaKhUln5rGrfTMnsw5ree4-UUNTQIVjMhCq9z_oTvKqaROzxbJ58q7c3nnjbDHkZAXBbxOaKLB2LVtI0POV-UAxWEHZ5Y0H6OeMzQD3PgZ9GPCkJhd3WpWRiDZAgqHyauDHnZ7cpLAqnDg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا رئیسی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴ را اعدام کرد
- علیرضا رئیسی سحرگاه روز دوشنبه ۱۳ مهرماه همراه با علیرضا سپاهی، از دیگر بازداشت‌شدگان اعتراضاتدی ۱۴۰۴، در زندان دستگرد اصفهان اعدام شد.
- روز گذشته برخی منابع خبری از فراخوانده شدن خانواده علیرضا رئیسی به زندان دستگرد اصفهان خبر داده و گفته بودند این زندانی سیاسی برای اجرای حکم اعدام به سلول انفرادی منتقل شده است.
- علیرضا رئیسی فرزند دختر عموی جاویدنام رامین رئیسی از کشته‌شدگان اعتراضات دی۴۰۴ است. رامین رئیسی ۱۹ دی‌ماه با شلیک مأموران حکومتی در جریان سرکوب اعتراضات کشته شد. پیکر وی را ۲۸ دی‌ماه به خانواده تحویل دادند که در «باغ رضوان» اصفهان به خاک سپرده شد.
- علیرضا رئیسی روز پس از خاکسپاری رامین رئیسی بازداشت شد. خانواده علیرضا تا ۲۰ روز پس از بازداشت فرزندشان هیچ خبری از او نداشتند. او طی آن سه هفته زیر شدیدترین شکنجه‌ها و فشارها برای اعتراف اجباری علیه خود قرار داشته و حتی تهدید به تزریق آمپول هوا شده بود.
- علیرضا رئیسی و علیرضا سپاهی از متهمان پرونده «میدان علیخانی» اصفهان هستند که به اعتراضات شامگاه ۱۸ دی مرتبط است و نهادهای امنیتی مدعی کشته شدن چهار بسیجی و مأمور یگان ویژه در جریان این اعتراضات شدند.
- در پرونده «میدان علیخانی» ۱۲ شهروند به اعدام محکوم شدند. با اعدام علیرضا رئیسی و علیرضا سپاهی، شمار اعدام‌شدگان متهمان پرونده «میدان علیخانی» به هفت تن رسیده است.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78625" target="_blank">📅 16:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3-IswMDWVVI5KaxQkB2JgeIz0hznoCafwQsqJAWoB0WxUDtBwOlBR80oeGl4qcSA3SS3zQyg7-9x3A1EOfvM4rAf5DYiK_0QuU6dS7LjqUKgrgCG31m-N3W736ZsIPJGaHyBBNmPeAGIvYAiUdrSn7efDqRR-gxxOOTsnCuJ9woJYuNeXfSphDk948V2jgcn4FqTDG_ohBCvOapFmkyJf807YuV0SVnTgnn4mZDbJMizDwgNU-KrPhL-c3c_Yrwa9aeUZ3w26TSVHENSlmJ_feC731OiU5dI39VxgMh9aXC2ZG5S_pTXjSRLOpZ8H60N4jnbDXo00H0iWawLlJ7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا سپاهی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴  را اعدام کرد
- خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام علیرضا سپاهی بادجانی، معروف به علیرضا سپاهی، در سحرگاه روز دوشنبه ۱۳ مهرماه ۱۴۰۵ در زندان دستگرد اصفهان خبر داد.
- وکیل علیرضا سپاهی روز گذشته با اعلام خبر فراخوانده شدن خانواده علیرضا سپاهی برای ملاقات با او و انتقال این زندانی به سلول انفرادی، از خطر اجرای حکم اعدام وی خبر داده بود.
- علیرضا سپاهی پیش از اعدام و به صورت تلفنی با نامزدش عقد کرد. مهشاد کشانی، دانشجوی ۲۲ ساله ساکن اصفهان، نیز در اعتراضات دی۴۰۴ بازداشت و به پنج سال حبس تعزیری محکوم شده و در زندان زنان دولت آباد اصفهان محبوس است.
- علیرضا سپاهی قرار بود سحرگاه سه‌شنبه ششم امرداد ۱۴۰۵ به همراه ابوالفضل سپاهی بادجانی -پسرعمویش- و امیرحسین صفری حسین‌آبادی در ملک شهر اصفهان و در ملاء عام اعدام شود اما پیش از اجرای حکم به علت استرس دچار سکته قلبی شد و اجرای حکم اعدام او عقب افتاد.
+- علیرضا سپاهی چهارمین شهروند بازداشت‌شده در اعتراضات دی۴۰۴ است که طی هفته گذشته و پس از صدور بیانیه ۴۶ کشور در محکومیت اعدام‌ها در ایران، احکام اعدام آنها اجرا شده است. سیاوش جمشیدی خیرآبادی شنبه ۱۱ مهرماه در شهرکرد و علی همتی سیستانی و مجید نیک‌اندیش روز چهارشنبه هشتم مهرماه در مشهد اعدام شدند.
- پرونده معروف به پرونده «میدان علیخانی» به اعتراضات شامگاه ۱۸ دی ۱۴۰۴ مرتبط است که در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان رخ داد. نهادهای امنیتی جمهوری اسلامی مدعی شدند در جریان این اعتراضات چهار نیروی بسیج و یگان ویژه کشته شدند.
- با اعدام علیرضا سپاهی، شش متهم پرونده «میدان علیخانی» اعدام شدند. عرفان اسفندیاری و گل‌محمد محمدی ۲۸ تیرماه در زندان اعدام شدند. ابوالفضل سپاهی و امیرحسین صفری در تاریخ ششم امرداد در «میدان علیخانی» در ملاء عام به دار آویخته شدند و قائم حسینی نیز ۲۹ امرداد در زندان مرکزی اصفهان (دستگرد) اعدام شد.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78624" target="_blank">📅 16:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fgrKzBYJSWeCH0odpSDfwfW-JYm751wKuGqXA31p4pF27Qw6rcGyEk0j_LKuI_CZ65OYt-o3gUtoFdxPK9RpaVJFXiq24o8ccOu7MqXcESTJirFDO5CE-X10IF2bNO-mhsezbto8K1M8eyivTykJnGx1oUh8u5GaN2E4JA2NKZ_R1KQN_jWBcEfrBG9Y9q44BiIqVQh0xMG0HrBDMtMmSpeTEzu2ikpceG6Wutlgc_WykfVzXeNgZOU4mfwTZgz8rxyfFGJFu7E9MppjVKRnglVCiFqiNrP_P9gVtiI-a5_Vm6Yc8VA3udPM-CMbIgNYZi5-A8LvkBNvkz-zLKjdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت ایران در پی افشا شدن توقف کامل بارگیری نفت خام کناره‌گیری کرد
معاون ارتباطات و اطلاع رسانی دفتر رئیس‌جمهور ایران روز یکشنبه ۱۲ مهر اعلام کرد که استعفای محسن پاک‌نژاد، وزیر نفت، مورد پذیرش مسعود پزشکیان قرار گرفت.
مهدی طباطبایی در شبکه ایکس نوشت که حمید بورد به به عنوان سرپرست وزارت نفت منصوب شده است. بورد به عنوان معاون وزیر و مدیرعامل شرکت ملی نفت ایران فعالیت می‌کرد.
کناره‌گیری پاک‌نژاد از وزارت نفت در حالی رخ داده که محاصره دریایی ایالات متحده علیه ایران که از ۲۳ تیر ماه دور دوم آن آغاز شده است، صادرات نفت ایران را به‌شدت کاهش داده است.
وزیر خزانه‌داری آمریکا روز نهم مهر اعلام کرد: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت هفته گذشته در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرد برآورد دولت آمریکا این است که حدود ۱۵ میلیون بشکه نفت ایران همچنان در مسیر تحویل، عمدتاً به چین، قرار دارد و پس از تحویل این محموله‌ها تهران «چیزی برای تجارت در برابر هیچ چیز دیگری» نخواهد داشت.
محسن پاک‌نژاد ساعتی پیش از استعفا، بر اساس ویدئویی که رسانه‌های ایران منتشر کردند، گفت درآمد ناشی از نفت فروخته شده «وصول» می‌شود و این روند ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgNGqaxclrPTh42J3vCObfZ1qTqo5UI-WYGO2EWKjmApJb7y67HK2WKoorYRccwYvV5pagiOGhoS8H6fosicmzvpbSoovSLlygnSCp3X4xJhwCYSfvz3ifKr4VEivBPQUKiNiwb5tK-Kr6yjaJMyRqEy-9adGnYP5jNoTrCp3M9xV2GuQhjyc6_y1elRqeLpAcS_JMFjm_oHE6BH2F2wNcEKeEw8Md-H2K9fCGsj-mj8iNMyr6M2YHZ0-Y-Kg25GD2Xx7CePZ9W9YAtoPX5vITfxAw-_LkKGTcB-1KBm7W1JZct2N1MkkTal7LvEzqqQ6_JF7mgMNv9lmIVPH1wT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg0ncK_WYOSZhy5rwjpKsjY7xPIaCapdp4Ngj2XYZV8Yn2WD-1snFJtvQhCo8Cicv2aW47IBwjgx6A2nmcu4Fo8PGvDldS5CggJzzgxRYMeSR0_53fNRONzbZSE2qcg3gZMDSwYvgJaswpJo3ovkH2gJtiDSLOeJ6NRYReZk5j7rCETFBQn2wXg46ZP8tIjAjyCJYk6tu47NTmkcdnFBku8s7syfYUPtSMNo9ZVDlrqNCAKB9_3aPFm0bMQBSdi1BOX2DD5TTiUCGfoFs01ACTzs3UYXGpQbLwVGE6fc0ZNLgQyy6iYVFwHTjHOrm-ekYM9fIFV9ygvESW2t71EXLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTLmtkygKnZb3q_TU4TyttGRxnONstWyo1Q4tRMOvEquhVM8holtOnIYdhoKOHKUj6KkWZ3wum2Ws4c3dXblyz5gy2QVJ14ntxsWyGXLqh66Q8hdZcUed6Rs-gV0A6o6R1gb3mF4-x8zOANVA0VLrn39owYhzKlyXMR1d4SNOgzJvC4wkJbJ4D8F2IS4HYzsDGw7hrjTDqt4xYzimjOh0K904mA6EH2crxHlQwrM9Gp11ymXrm-zf0i_VCBAskANWfTmDbgPoE_9ORX8ocD5x_jr7GtEpf_OUF7oganqUIQwOUiPhJNwaWpE44T9JIDWhEttGBReyNrMssLzLbCkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=Uvc0Wjx5IWirBJUwD0vVhGK5-qO2gEuEA19ViXBdmUF00oMOzGjqUXZ0InLQKTQ_ysuIChEXdP1oKAaGEjUCqNE9yq-R5Mxz_B-V86MkjGDOmAUyUufLOKC_D13hlmN560BnkegXeUGloRMzPV_ph9TqfFyzErrbEB9-FmFZ81Z3duxB5wcAkxuetw9YgZgkDijnIIsgZOI-EBNVWLlMbF_dToxSu6KgjfgZySlTBZGgQDCPESYQn9Hq0Sih8_lkCEKGMtJMkaD2p0WheygPYgS3YjoHzqsBGw_jniO6qk_S1xPEqF8yKUN6S46B0YzdTGh-uT4NfoViBACS8qdkBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=Uvc0Wjx5IWirBJUwD0vVhGK5-qO2gEuEA19ViXBdmUF00oMOzGjqUXZ0InLQKTQ_ysuIChEXdP1oKAaGEjUCqNE9yq-R5Mxz_B-V86MkjGDOmAUyUufLOKC_D13hlmN560BnkegXeUGloRMzPV_ph9TqfFyzErrbEB9-FmFZ81Z3duxB5wcAkxuetw9YgZgkDijnIIsgZOI-EBNVWLlMbF_dToxSu6KgjfgZySlTBZGgQDCPESYQn9Hq0Sih8_lkCEKGMtJMkaD2p0WheygPYgS3YjoHzqsBGw_jniO6qk_S1xPEqF8yKUN6S46B0YzdTGh-uT4NfoViBACS8qdkBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز شنبه، با اشاره به تحولات جاری میان تهران و واشنگتن به خبرنگاران اعلام کرد که به‌زودی درباره ایران تصمیم‌گیری خواهد کرد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه «ایران درهم کوبیده شده است» گفت: «تصمیمی است که درباره ایران خواهم گرفت. تنها مسئله این است که یا از راه آسان خواهد بود یا از راه سخت. ما این موضوع را یا از راه آسان حل می‌کنیم یا از راه سخت.» او در ادامه افزود: «ضمنا همان‌طور که می‌دانید، ایران عملا از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.»
@
VahidOOnLine
پیت هگست، وزیر دفاع آمریکا، روز شنبه، ۱۱ مهرماه، از پاسخ به سوال‌ها درباره اعزام ناو جدید خودداری، اما تأکید کرد که رئیس جمهور آمریکا «مصمم است» از دستیابی حکومت ایران به سلاح هسته‌ای جلوگیری کند.
هگست که روز شنبه با خبرنگاران سخن می‌گفت از پاسخ صریح به این پرسش که آیا جنگ با ایران تا پایان سال جاری میلادی، سه ماه دیگر، به سرانجام خواهد رسید خودداری کرد و تصمیم در این باره را با دونالد ترامپ دانست.
روز شنبه، چند رسانهٔ خبری آمریکا گزارش دادند که پنتاگون در حال اعزام ناوگروه ناو هواپیمابر «تئودور روزولت» و یک گروه آبی‌ـ‌خاکی تفنگداران دریایی به خاورمیانه است؛ اقدامی که در صورت اجرا شمار ناوهای هواپیمابر آمریکا در منطقه را به سه فروند می‌رساند.
وال‌استریت جورنال به نقل از مقام‌های آمریکایی بدون ذکر نام آنها نوشت این اعزام، همراه با گروه آبی‌ـ‌خاکی «ماکین آیلند»، بین ۹ تا ۱۰ هزار نیروی نظامی دیگر به منطقه می‌افزاید. به نوشته این روزنامه، «تئودور روزولت» به ناوهای هواپیمابر «جرج اچ. دبلیو. بوش» و «جرج واشینگتن» خواهد پیوست که در منطقه حضور دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGbSS4N5Qpolpmd5ziFlhapPM16ZGZZV5gkWMtuK3Xljvn8_GQ6Npu3AFTbjxxENM6YL94XRTPXa-yKSohFK473ivrlL67fO56G4tvfv7nRIEdckd3zf3Zq6_rMJVV9l3wx7zprzbLeGYA4gVdA8vt7ek3lGbQMBZchlppRcOrnzPlqMfyYjXdien77vxuHWI4e5j5buRloLfTqP9UKG-FtIg1S5f3wZ3xlSBFiRV5iECpzxLkg7Jk-9Ou0IsfhgGbHdoTkPpybcLdHr7KYkArgp3RPy53ohSNx7wwRks7J1dvHnALBMrBW9Qj8nJwPtflsGsc5ru47ST-UnIcl7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HapyLZzcQVbNIviy6e9xBSLbkDWD7ZFi6J4FiIX1xRqGrO36KjtvAB_Y-lM903opJjfqWttBK-VRr_bNUvHru2dgOAcpkAMxaq1N-kNvSBc0eV71aBY1-D-GCJN-4Gi_yJkE8-cUbFL8hEXgb9ZJkA0tj0hRIB5csXBB3IkgfVF3zjzzaL8yNsYpnrhsCDtv1dIkhKO0SfaLnTAIPDDTfCc--4ub_QG7y7lMFZFdV8l5NF2s8kW0b5XaFSPtMnmZW9-zFX0sGh1P-4BfyvpUOH6Ht1zUoXkO0vv2SZU5CdRnCh7Qlzo43M-JptiA6gqqC3dtVVpAt8C4XSsEuB2EiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dGFvBhbkZd4fWF6YwP-LsmT_czbRX8waxMKF6LVuscYsRgJUbEvAINdFwA07NTWtMXF33Jj2p-B1ie3oftyMqBejyu801F50AXFi4HdHJrEuaY-vqXW7qh5_icAG-2UmwjJ38gDnpgffx-hupBpCIWnDoUmPVE87P7e8-bCHGWBGMkzo-q9aXh0cAhQD-eGf1id3pwUYW7U1uKt5d9Fv5feVFT3xyLAeO9XDX_ySJvBEOqP_6KYh2-9p2teahYettXAokuqTc-R3NpCm3dkFk6y_MPUFT2fuEQ5DF-ZACtXCX_oMclkuYTp_SkP0erVypW_w0PRTBGgH668U0ilAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7iICYnnvWp26WdDzV3opKNWHrFdUEgdcBp16w1rwxj341HxMbXgGQHy-NUWaSuoTljQ0FpdQ-XEeEKL9LDX-V01_ab0noY7On0YjCYGaJ4UaFiNdOfQ1JaYxVSYWCQWMloJrEHri0BMmE9uRA9M5GYTsBgaON7gfbkkitERf38oLhi35KMHo3vMTiJrhED4vapJxnTpD46IWw8FOzh74j35YsDh88nFpNZP6umbgdHokPQOMHjIs8kNqqKsaNugnCvzjc7idel05J6wZbvgZs3HfQvComDGMsuPpbsHKNti0gNP6Dgy2hwP-0qJzHRlRuCSt6tCzFY84ObMPwpbhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/agLAqsI5_k0pfrgZGzKTDJsbv7H8EtQBEnshXDeAgylhSDmOTC0vpX_GvMOjrt6aEtEY_FYrNH4lDJTLrbbz6fMwoiI6o1nA4BcLPF5y5Uy18mTDmnHY4-vvjFf03wRPwN0olnoz_q76Nc1E-fSO74Q86eYCIg7NAfPNkvemTNyJrOSnv2mD2bozwM1_KrnKYvJpRPOl2MGfhkyfheXaRD15BoaTegKs9VlVXccmGro6TZ3Qv19hu4LCte3Sf9yKodpj9pt4lUotjUfIurTCMxsQG5mwl4dPI61glmo7MD5bN2PLFeWFa1PMXZXjV1JIkLf306Hbkuong6DVVBWd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX5i7hhNxQFo7E5CxkswIGHIYh_2dZdnVCOR-PCLGv0C0Jrxd-YHUQEGrp86cAOPMu8wV9F5BMWgkgjskP5d47786fBH9Rc2WiqoJqE3AJR8uc3hz4_bd8HYAzHIeHs2v80AOtBY8CKhrzTk16m4jbJry0hhYMtG-xQjDXuPKDYLdWawUDyMw_Y2KfGHvQIcE799WUn8199k7RGTx7Fdd9poIWzbM5EQvSNZT2u6JD2SVSDjOPlnGih0SIMjJqfAw5Njb3QabuRlRfzGCTAj0T-zvP2kzpY-HT5aDKL_QJCuNRr43yygu4Z5JNrRV0AiuzmbXjzlFWa__xG0T1eUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PCE3xWM2Asl8TXH2sl3GYZVesFtG4fLB3deYnz2bq_0z0EdvnGsXTdsjM94ZXjuJH8FbvcjcA3DanvmjgMtgoszUBjwoNkC0M4xTMjYIo9MyW4MzcS9QtMhWv4siDU8jRAZ7nv46HNAhRDyjJPLyD29DNNnvkzERJnf8znTObl3yBzb_pFSjV4M_w8uJVy-aoshLYGyEymjB2KE-cRM686xgM6MtJKRme1OxK1_yMBzB6zoo93hC3pB47tPz8hLldkuz_rcEmhT4PqUXnhlGytwgWjkdQx62AGljyDil0jbtQalpbxeXy32EGQjsGNzlUmrcgmm0PlGvnBsPRuHUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOf-0h7PV9XlthNwTD2Qfnt_j_3ncMZ1fMU7dWckECOW939ak-FmK_k1jZkj8MTnR9CfnoVQPPX1hI9_giJz8GlvH_vN-XXNBPTmSII9ma9vY85RAwnUQ3-xwrH3T8MAsdaTh38a9jUc543AtqouaiYbfAuP0XT1gwf-PuixVtpNDZu_N8bYnfWsLNoZwlgLVqL3kb0yiZdi1Wf28-MeIBrr8kBdcmS4i_BYviMCZnXY5Hi71Vh4cxnZ1bz0HmFY2t9xanbcfR-8nIv7MnsAp-9v0IvKavNFJr_5cTNbnHrnydgfXh_DJ6FFbrcXv9lyxv47KaEwTmlA-56EWe-ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqft2HfIPTaH1rn3KaMp1OZvRGKSP7Awu92jFg1hIfK2nTJNJp7GDpbt8J0a7Rutb7xtCUyLMcVW7qTFFTmaiCWK4UD-0RhlArr4yv0FbzRCl6QjBouqO79PHRFrj9gBS9pWfujK_8P_-CTiOPWgnbJx187u7yq5tyNmNP35gGomUK7JxO_bGnYejYtraIPSHVmV-q8KUQuS5Y5OefSxTaR57QozjdTC-Z9FsWFybDm1Uo5bhTerBDyb-IuUr_AXmsIpeTp-PsnDlx0ClwVKWXsauIEORJ30uo1iTvNnnRI363AFhgVW6_ehlv-V1dgKhkaMulREy-6XQHkN5LcH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at6QyfH-BuFD5-dil1CtCwA8EuhLPzLAz5uqeUHO7QaZuQpNpk-xh5LF3OW_t4i_PxY-k67sLt5eyhBOM2ljtTdORsUB0wKO5q9gQaLDDmtS27hVU3-IjtGRgw5MvSFwWuI5CAl1IcC5FvRR1olVoBWWqvfT4SrTfHuuZi6Y8Ul2LCqvw07mJ6qck_srhA8ceZxbrwchKdrMX01TUufS2E5HjthyuYpE123ssOTXm5lqLsC_uuC1GX1fVnpU2UdEXusgX89qpnLr4P8Lk6rqdaihUU79iFA-vjJmlzTIO_VtLb9D6VAydGnVip98nq0LWJhIYfDBnuFMai9wS05jJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkA_fao41VwgonJLhpMDqpl6Ctf3lHRlvBmkPzHvNASgl0IKG3-jCq5hFSv8iQe51j8de6krOFKkrZKrIdUzGv9WnvT8_4vOavLj1jg248Q3GMvm5JmQX8q1gob7WIUmojBGH1KaiwZU9rIBkthEg_x3cXUOQFUsYAWiHEF1HNS0mqEufQOXAI-OVkJuEQImu3UrCXOs08wjbeRD2n4jOSNHJg3-1YQKxoIvAu2KC-UJlXldCcFlJLkCN6WvQi61-ShyYBOeke4HP0bbkaQsavloB015iAJgvbAIgsSM4XkpnvwDpGvwBnuYY7T7EU6HY7z6Ga6s8HWS601bozYkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/raqORj6cMGiX1WZgp0IFihYVaWBdmSyjXcfvPNb7XWdssDTei44Z-Y-ndnpQAlYTJszzB9VD89hsmG74PLnNo3fOqbJ--Yd_lcm6uJ2rf3oDhKRWNwSwFbLy4W1zT20XpJYcmbOZcBqZUNMb8kLO5ZFJTdH6hK03ZbbuqusJaQFxEosXKYn6yIBsS_QnBsy1VdZr_8zB18cGy4P2g3_nkec4YphbLmKAQF54iAs7e7PkwyOVtapvRXivr9iFhoE2oYemA06pNHf7Qto_yit7nLfYcD47ic8wH0_JNKJiXGp4zL_cV1ziWw-dNEkhIP94PaFlT4Hm39EEvpk17JV96Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMqabFSjHBs-exnZ17W89acYKRz5Pexkpx0lAnwR0_6FCUKpm2EXJkz1--lsPMDEVCWjmAg7RoIQ7zUV2K9gMLGQiUvc-RPosE4ooPW2pNxtfvbfbyCpsqJ_k55jR8-zb6aq09I-e67SHnrJrULTEcdBfnoGS4NEvIo0AR9uJbxzvSR1IwyoVI37G9mUMO03Yc3yytXKlihE3qyRAB2DvTVNOK-MsvN1uZWV51Coy2YIPicCM-bg1PG4ijTqnkAdIL-vGGIHxYVb7jxbj_2W4VrpMaeu7pKPl1yCw5MRySOoF6w6JZ9E3JBplx9ZOUWpFvyZgR4dgt3J7ll1xB6amg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcxeZ8F_oSzxU0tHiJTm9LR6Lf0kyjIKGpu9YXg69W0RdROiMfIXzx--cK5XqOWAyKIVmxveHixYphVLbCCBaUY3-_zIPa6qC_H1xA6YyB8mPXhXSdQXmj-DQ8zP6fookk3ZOXdJXQ7EvqVl37_KvYZK4PzuslAbhU19hoA1dXjxjZwvR6Jea1BxXjZRZaQClXycGTiSNsQGct31PZZPtOwh-shXiNoSRdlRlJ-IZD3VzHdeX-MpwfLFB2kjcFerORimCe-uP79G_gs-Ao9dtXZGstRRJhhlJCkVtlIIgCRWb627yGFAukTQansJpZRnR9Gyy9mMVlvRaLcHNcPjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHwLz_pZwygG558dDEzXzymGTC__wfQZgHJRMoT6GeFDPuN7iE1tuKcQGkYT-wMhO8olsdbu0h_DvVkONFfxDuYaDNLabgZI3E4N0hDIRXk66a7MjQMct5w32pp-F_7rt_JwEVDOc38MNgHhOKbJDDxOOOPLF7PYK6v-pjwRmSrgnOJ06mjEmL6ZFzgXC58ykUSlNDzUqS5nZPU-xw2lfnJ94frW59TOYtYTaGtE7b8TvY8NLSVq0n7Q6qe1VqEvV8GSJSh8xzggtdVyU8ZvUyUoqJHCiftLgEhrLoyebU5ujW7Wp6P06msqSZh9eW0F1unxSaVJod2hFsCZMg4WvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=A7rAS2TZswuWhOCyi1b_F3z0Kkq1AEF1Po-hGiKuzkzd4mZO0kVb5GlSaVzveuCQ0d5ApECZjMe54T5ibVEVtLA53fddO1Cf_LGXKvsf25-87ifxiZVN1N2sGqq1GlXLhQSM4ly1ikD2If3cubyGMo6SKUEcbWaAsdxb1Bz147dm2rUnG2rSpYLUcSoWRk7Ch2Pzls-70wCXis8QJH1w8ZSN_56DAe0qKiWN8hLn5MqV5DakVn_-B-wsyVjVibpWJPDvUI7cmzH_0u3rSTk5M3n0klBKYOHQQglZMsDMe0CffCM53Nf8gLCMfSCPdMZvmWpuNZOSzUfrAvkEOWkzmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=A7rAS2TZswuWhOCyi1b_F3z0Kkq1AEF1Po-hGiKuzkzd4mZO0kVb5GlSaVzveuCQ0d5ApECZjMe54T5ibVEVtLA53fddO1Cf_LGXKvsf25-87ifxiZVN1N2sGqq1GlXLhQSM4ly1ikD2If3cubyGMo6SKUEcbWaAsdxb1Bz147dm2rUnG2rSpYLUcSoWRk7Ch2Pzls-70wCXis8QJH1w8ZSN_56DAe0qKiWN8hLn5MqV5DakVn_-B-wsyVjVibpWJPDvUI7cmzH_0u3rSTk5M3n0klBKYOHQQglZMsDMe0CffCM53Nf8gLCMfSCPdMZvmWpuNZOSzUfrAvkEOWkzmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jZXxG-7EmLmLwS0S-wHRpI2elEfD_PDScGe0nm57Jkyffcfnjcl2_cbxNLLElsQh5MBTGHoP2Xgmq0Gp457iGHfTkGAlJP1i7cFu1vSOUwXYev5gKuTfz6-AYAwdQ0kif0tNuv52W17vBMCi-b_jQvFNNz0qRYhQrk4F813fd67Nw-c9Cevw3gzBR2vWMLHOCa_DqQNhyn0rBUL2UB28WMkt_ijDKA4FPXhvgsLnK5TNY6_lqFK-CfFC4Y29ReikGMcZjFkB8Y52BeT3NK58s42_UM9P-bejQJ9G5XUlFE6LN-Uuhpq1-u8YU04Dz8xn02YaviOzY997LUgWS1ti_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SiGbHfKrxVyuTwbf0LE_2BIvTH2jacyC4EA8hxR6xWq1pX7_jvSbWBDng0g1SBALuvuwElVIgflY2SX9HoxW4byTkStpsJXTvB7J8t2nHM4icSII-4SxW2xZKbjBdYmWtNK-YFA4ca0xgTOWAzA9xi33zL09D-G51tOhX0G43gViIhkahWKN4fmxJvBoGBA-i-PvSfQA-vJl_XsvdLvjz5tu-DcSMz9I1qDSjXyM7zuR6p5k13jo8JtK__PlE5--plf5qQ1O3FYx3REpspeRKeGSSHtMgTscf_tBEZ4PbMFIALBeapDm9e6ZFoaTZ4zG66F5GLGbCv9569WWWdAjGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=q8deQIosRGgZ0RiN2lBlOgnx8Auaohf44fyXfk1WFgwVxTMIEG5OYU7Krzl4xvf-5EcLXozW3sBcx6AVAmoyIBqsy1Rvlaw4Cr5gHOudjZGg76ThwNbkWICrvP6iGNAT0VamtCXau9_eix73UM3LNW6dpUSBF078V_VbxCO2xZKV9azFvVna48bqdwOiBJnSeVv1Ge7XPlmmJmhYYsE_TFeo1A0iyoy_PmzernLOHMr0Tr9tsU093o7ESgklkgSNecdVpcOGOyps5HcTzzF18GDjKAvtFFdSdWazUqF_pvsVqYiLhtNuLhpuKBDwe9O4ivieU7-PqsTuDmzRXMuayQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=q8deQIosRGgZ0RiN2lBlOgnx8Auaohf44fyXfk1WFgwVxTMIEG5OYU7Krzl4xvf-5EcLXozW3sBcx6AVAmoyIBqsy1Rvlaw4Cr5gHOudjZGg76ThwNbkWICrvP6iGNAT0VamtCXau9_eix73UM3LNW6dpUSBF078V_VbxCO2xZKV9azFvVna48bqdwOiBJnSeVv1Ge7XPlmmJmhYYsE_TFeo1A0iyoy_PmzernLOHMr0Tr9tsU093o7ESgklkgSNecdVpcOGOyps5HcTzzF18GDjKAvtFFdSdWazUqF_pvsVqYiLhtNuLhpuKBDwe9O4ivieU7-PqsTuDmzRXMuayQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EABeYwhHZ2yaWpay8D72T__KasYwgrr_hHsSpxy0I4HjirC1MdoEeATZmnoDQF0pG6RNVOuV8RcvZghM5mNPcZ3vnVfsSVLubHyXNa6vbkkMIShwHGSutZwWZdlTe-VzjlQURGCicfnXHb7oNvSTygKxrw9076RuYU5IEomNQnHbBa5LJV4EGC2qJwskNwCVbFPE1pnPT_qAtM0ucjqiZKxzJBdOKsIR5-ix0zRhjR609vQhm24Y8SdnoXW4Muwbw3fmoHgYIk59v06PdDdmFVAzgl52a07fs7KUZ5GweQMb400wEA2krZYQzdQx_TytmcM4nytl02lTjkqRgXtjnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usIOe4K2w0WeacteVhlREvvrmYCyCwTKeCfWld_pZgowz0xwoEu2tycLR_L8ejN_wqibhva31_94IBE3rKNAVw18Jegr5SqH4alpelN653BIniufb-RsX2_Mt3OESIO1kaUj0uHIyaV2MOYa0RKomFVLjARmc1ZfLFClQZpGb5PTMwJ1TnMTXxZGLn7daAcVZIJKZS3qTzoVDvW-FJ5HXhUvfgFBjQdIAC70zwYVHKJ0BgvqtQHw-FTfS4hz3UWzkBZZMS08V5PdbhBjg4Y77wggdV06y2W28Dxt8TICOAAiEwN-W6iNhsxKH-b2MQWvFGzYUiAwKWmUqQmE6yVRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkpODPjdWpQ0L3eAgoCyUmdCDHjOisJmhedezOX3W-GjVU2G5itrU8QsjcgDzJZ7kEIJaq3tT4nsPGIKbbfAjXFOtQkgPeodfqpyiG0eZ40sE8iQOsmMA4kC8lRI8p2q7uTN__A6uLTVEb5fj2RAWyf8nnzCjsO3MJEuAHQYSvXKp9tTGyp8GRt08hT8X84V10x-8-Rty4jO-q9wvoGgxCONE7TlkstIRgTarmsKAOkZBotXh0SV9KoaCmXdySIfRo0yqKhoK5FkReYmI610eBUFIQfawnnqqnzViCMMWHKq99hz0588_sh0vOOiBOEhRY2VAGyl1h_DCF2Ue1RHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRRARxfdYb0rLQtb4NRQ2MILwU029NOK4JfRE637AhW1Om-GIS3rKAw_cbYclq14NkhcM6LlauJrBKFp-5rO4bTAf8ydkEtOSFwQB5fA7VM-m7CkHIlEGqDJONhVxER2pzwk321zaAJl4a7u--G_vj5HQjQuX1ZHnXNihnbQ0hx0HHl7LnP65qZQIBRiRZtVamBXUyaNFHPZCHzAayD-ecMGeXQwU_JwFmFxGjJlZTHNSZngTqLGHMKcwBn9jvneMWtVvLf7EDm0op4icPirQ4XCh027ZeUL2QeM_gWDouHcbDXWNBTPB562nzaB9bKAhgjdMcdODgk_gJVU80V0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d07vRRyjq5lC5lNBSfj_UDqwWa4mGfqi4KOMvrxXGC117NWKQuNbGu9Nagmgf0dbFEzi3O4y3hME622-57cH4oVvn68Y8al-dvRm32dRRX5Gys40N-rKYRhuFueuj_B4egrftR6a8aFtUITfa7TCeIiH7pamwiBkgEDxqTdOUTZTsGTFh8e0QiEJCD4ZP6IinM4w94pfE5G_0BGmzk_2O_Cih51Zltt0RvoAbaQusD9Fi3GPra2kQltXDlTAeJy9JzjSyYBK7Q0oB38p1xpH8EhH0aKxe5PCEXbhNw0AI6AE-f8hRAh98gwwkt4jFCKvhw1aN-5thLGSEGKZzOVWYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X9RQYx3SQy8FcfoxiAET8NDe5RpeTKnP74Ue5tDqUix28ILn7SkXjdweNKAWWw6oEtKQ4Uw7TUIc6O8fgAe-xqr0eAn4jrjmqqB3E6j0oJlWu3GUfFO64l2j2TQIhA8nKuV3uTv9fiPJ5tUlXMM-ROhDtIWFDIoKO5Zitygpts6VlHLDBNujmTecF0p5oOQ_dRHtIn4paqPhoWhtou48qLo9vbB9b00Y0e-fhZQPGOJXQHCkYEIUMU2nphkNZiWrMyk-KOZZSveAvuL-BHuhEK-4meEdlShEJdVa0USCfU-8jrQiT8yRaKkTIAcNUkd_U8kEI6XB5hvr2gpw880diQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lND0dYO3doxoA43tGPwpZsCtpHiYZtWIKSQ73kSoxudi73wbODqLoo7hw-z8t8WjrsLhdLTSjOfS4jxKTCd2mSXDtjiiDmYUopwieLADi_CJZ-FmpBR5RqGqUHELVDNU4ZcBKv1ZkeraR6Qi3X-7J7Rv7L9CDEPMc9mmzzul3swALbh9LnDChVqp5V3Xj1-k3TZqdlPgBe0rQCq_bvJanwb0iam4w_cLo0KUG4NKDF0JzPklDWZ8_FcUXYBuko9gsphVDiwakYCqrR7xahvobxMFWnoCJDRpVGG85Fq21c_ni8rBtVCVq2IeM7eUhvKWO2AW0lOWGIiwarDg6m-_ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBqoRTDuBi8-9hYpVuRDRPC5u_1L2yJurOu53y9O_bwkcZ3zCHI4UBx5ru4-i4nClZyB1C7FV9aERdhapNc5S5quie5RqUxheMloaqfrFP62vXnlX5dY4QJDaK8mmJF-DIobA6yfV0XAhX-TVY2H6sF4tR03w_XPddYktWE_tSKmli2643Z0R6q0QwiRz47hrtfJBqGQzuZfIIpBSkHLybaPL2oCGwYrIwzGL6AX9QQQYvrSsVD45PblYm69NU8552ePnA7TMxQF4cR3xjxtNNuRYpIpab-GU9cvSAwMp9K2B0qSFKI1FK-y46nSoCOwvrRZwl1AEF7z3B3XVLO6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hcbS1N5t6PEcTOxsCB9aegQ-S5WScXiN9KSefbY6H6zyxJComNA0hBUeXHBlkFQ2e0_4sRPmDn9b0mVXGOrBCPWfid5NNH0bTmi7VsK566cDn29YFqkCjfJva_u-YJnhxh3frVWSOZIJzJrjGheeAWExPZat7_Rd5akttWX9gSCehk-Mt9MVblOOOyl-4xW_OS69abTzWp31USdDUV7ahKNlw0Frxp6MWAhiJWdkIVCIeuC_6q1B99e6o8coLoNY2qi6qvdbSrY0_U5lZ1jHIFFbdQ9gOBRwWOQ3ziGqe-eIcpwYkZ1kq7QmMS9pN-Gzk6NqAdoHppex7M6sVXwpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-4WQ_TXhgWDDoSPf3NeWVo23kQrpt7JAECST6q_AlRlUxkQrtH0MLzDasQhoMOVmcEXa-ZspInj_bx7xwcxq1v9y3AzBWcl4EteKLPPw3uF8Du8c4brSmssZowOc2hNjlm4sTBL8zbtH5uU9FMh08gi_p1PRhcbnVAUAvz567NQgQsiNay1pPv14B-WbBPdS_ihyjKYvx1dasa320xL9SVRbjVWpFRbsfbf0ZBUP2F2sFZXwdiP6mFjgIX5XxiiqD_NBQVVuk0DVqY8PCdj4LNboutHwyrUpM9ibWvh0025qXqCe2tS-DuQ_FexrV-3Bv9A9uVgoEFx8XUDf16Fsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YX5IvGTQ8Jp2LzKoj7cNLz6uo3TgW2JFGcnXeW9P2b0GWrtr85dN6P6A-_ujfePzmI6c6J1seVIVtq72RAWgqwvDYkfKRlD48WwW0iOJKbynXXOu5-g5ZAesjtlcINnuoU9PlQdDVZO0khdfn5cXHXJ89toyCl1TZ62qdIcwnOOi-Qh6oo_uEV7frXJKMzbFha_JwwgvkEnijSZ8khw-xoQRihXfWYSa4dgpzJXHpJvutsYYQcZCcXZyjhvd23ifpCNMjwuCNe6JbdJgO2uWMJYZ5xLCiCZjWwm1jxtSARjSWImSMaIN_ZDwJHyD2IEiummrCujrq1exdSUg3iFkFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpsAVoF6-BRk6EBM1SNCr5B7W-76NSfd-EhScmQlRXsOBTw4nOBVe2ltICxBP9q5dsXEgVynzzYJDl5LKkNxQeNDX3CnTgQ7ClZRtjCJdegLLao4r5r9aKumNZbMw_Xm8YIYVVoF_ApBQkD4tbJq0RAsYG3MN6LJFCva1KahEptkmtqtuMUZxbvYnlEMue2j1EyOWDdfJtcAvCeQWeD3tU6PUYm_vNpLLcKI4AR8BiXr16TDSnwzbasRDqyjULJ6l1Wb6feeBxsdp8XAvZ-avrhOSUulQrPC9up7xI5IRkxSqQdCuE68hTQQC-tDHKMSAvqBDdARxbmi96qVnwNPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dKbR7rvNagbmpSTXnTjubyiHFrVyfWkOLfNYyw1pfPNa5YR4adql0yf5A1tJ8LChKnMzZAbXMTdxSiFEFvDIxpC1zRP2LV6tnrN38tIXf0zFQ61hbi7X0BEsQPYvsg5O0mTNUSjx1JGZZg4-enV_OzQxyv2NE0trpLn6AVy6Sci8VZfDKUrWxN5OQtTHBagUznqYUIDThsFaX-XgaV-vWMSExPeI0qZru4560RGV_8ykMd6eoxn6-I0S7G_XbNGOEWHlnc4dgHMfcF5acD3hU_4jW5nOj6-7T5Nl_0wQgGL1hK9SHGlzLMBhPWZkyB7jMocSs9F77SpM2lpLwMbvrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=jJ1HqNTB-axkbwy_0sFWl7mMe0LIBNOca3_djP-utZzh7va3yoTYuxqgbbELyA8QlECwd3rZpY_Dok8w3H4EHbXW1M4wF9FZ5NU-pfGiQwr68G-WtYLsEJa_WIAmheJZrgXsEp_-MOHo6hygF-DJZYDh2iNQUrqNqz-6jGttc3JtqKMQ3qggFAtI3u7-awRueu0NGHIeYbMinlmm7rp0FxMFnbm_jdGhrcyvyV4DSD2WMJUvvLgW3X9SapStc6MzmZ7BOPmglrs7eHMhfiSb1OEsNbc-uoZL0dAgXtbOYH2h9YpUrxoVMQ7s7I5mjlKOYmcaiaiTAEozWt_wgYErRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=jJ1HqNTB-axkbwy_0sFWl7mMe0LIBNOca3_djP-utZzh7va3yoTYuxqgbbELyA8QlECwd3rZpY_Dok8w3H4EHbXW1M4wF9FZ5NU-pfGiQwr68G-WtYLsEJa_WIAmheJZrgXsEp_-MOHo6hygF-DJZYDh2iNQUrqNqz-6jGttc3JtqKMQ3qggFAtI3u7-awRueu0NGHIeYbMinlmm7rp0FxMFnbm_jdGhrcyvyV4DSD2WMJUvvLgW3X9SapStc6MzmZ7BOPmglrs7eHMhfiSb1OEsNbc-uoZL0dAgXtbOYH2h9YpUrxoVMQ7s7I5mjlKOYmcaiaiTAEozWt_wgYErRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVfOlff0zDPHM5yzKi3lTmA1C3s6AKQCavi27KJHESqqFlsSr_i4gnFb9BK6BK5eN228Q1Ho_v5Rw4AL-AeCTeCTF1yfv3GZFf2MPZRy3OK6GC892gpDczPZsKlmM2R4p7sR9eDW8AZAno8VqQ8x-It5gZVVX9a1WdYm-IJ3Nj4HNFfX8jNgMThlS-q-W3tUlyASFDpL4OCOOD-vWmSjtJHmajXmhjwCpIzadECjJ9ca1OMShAP7xWwAfrOZoiY0tzS2f7DCzpfMM5q0vUi96UgAH2vK_xxIj7WWVbR5KHUtTDh9uCrJtNqRZwMaEJqh8vJeVVRDi1yy-mWALHlSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyQvNOMd_pNGcpRXFuLFZ2tcm4bNJgkAkkxkQzQIXA2d6Yn7O1KfgSnMfFvsbekpsGLXadZK430KstpNJNl0CknEKge09DOtgy4MgjEx4jkwdIOXfBRdSDlYHcE01J0dy8-kGjiLsll5pz1Dv9Rv4Z42cFjwme4OCJJ_D5VnwtBS0UODuOkldpev-mRUSOpiJBBp3f6fzL4UtGL6biai8Cg3z2cUvGNYXT5HpM9Y9Uo7qyS1K3hnGHQgos2fLBoXGnrQw-xmFZpMT2tci9Zee9FqQwn6Gteg3IeLyvf5S9nrU8h7przrFDI-9daAs3XCdmCV6rJX45VF_4meCj8yMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه، چهارشنبه هشتم مهر گزارش داد صرافی‌های رمزارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کرده‌اند.
بر اساس این گزارش، این محدودیت از امروز ساعت ۲۱ تا یکشنبه ۱۲ مهرماه اعمال می‌شود و سقف خرید روزانه برای هر کاربر دو هزار تتر تعیین شده است.
این اقدام در پی افزایش پرشتاب قیمت ارزهای خارجی و سقوط ارزش ریال انجام شده است.
عصر چهارشنبه قیمت دلار در بازار آزاد ایران از ۲۵۵ هزار تومان عبور کرد و هر تتر نیز حدود ۲۵۵ هزار تومان معامله شد.
پیش از این بانک مرکزی جمهوری اسلامی نیز اعلام کرده بود اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIokPrH3TT9i26O5aAX1lXWLKGZv8mGMX3pHMQzYhcCNMk4NqtvMcP_IT8NyI5Y39KfWDSYQlDSHXu-1CGqFhjJEr60SnxtCrdh7qGPPCG2Q68xfbEw6bejy5M9mQ15wesdlUl3pGAkUfbQ7gAYT0dVSVEm2ttbFHwJDwDK-NfDlbynEYf34Sgbto1Qp5OCif99Sgap6v5EEPFxPiH9Wuoa9lKOuSxgHO0oD_LmIr-XqAdjEfo0qXcXCJCWh1AaGWQQl5fsbo38yckDbY86XBqtMTGaZh9QdlU7r6bx2acxKKvUZ0wNmHe6LQlvyE5GC3YUC7-L0WwVIZsA9d6xQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYTVrTgqy5UZcc51GRiqh4nFcO2kXRgf7nimb8A4n1cZ2I5zzxXJnna27yqGgA7xDvxu0_MDT6Ab4hC1WkPaz2jOA93NUcuwt6dzxmTFG8naG3HwbuKeL7oq9sdpE0oR01IdcNejh2GUgeq8DRaK5IknSxdSVSZvjwlXw-SHS_CkK4_4XeC5NEENMQLa-ND9tpx-GP7atnccXbBO3kx1I8T_n6wkW5xfJbTsRrKoS2cCLB4ufIqdLgchojY1GszytcKDTLdRhF5a9Z_Km_7wx6KDCay3XprBMOkpj-Rg0klLZxYtjm3AzQynXsix98C6SXjtotA3k9-W4CvbmWmZmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=GRDx-ktTBzL8HMdFetqa4fQKArDZgkeOb9iydoaDABKuEvLjROyF-9chdNZWzbB_v6qvdf7Q699l_KdFK7mC2bqNSQkKvcLOpFmREU-haEi3-nxGCS1Oe6vaftSkaSEnjGCP_eCtTMQ3Io4iL5WrHADEqHCHsFUdYZkCFFi9HpXodKwqv9SyLAwwb8UDK3xrDlVwv8ZaZ3E8yviVfLMo67f9KVmQto_1RoJX0Homy7GDuPqXdlsEw9pgcXyJAUSFIVGBsXM9VTcwSq0eZNAmZsyJxuPdA4-XnZR91_p1vponL6rdZ8WeyQLiMuChA_UtbC8LeUugamIAfEMVFiuRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=GRDx-ktTBzL8HMdFetqa4fQKArDZgkeOb9iydoaDABKuEvLjROyF-9chdNZWzbB_v6qvdf7Q699l_KdFK7mC2bqNSQkKvcLOpFmREU-haEi3-nxGCS1Oe6vaftSkaSEnjGCP_eCtTMQ3Io4iL5WrHADEqHCHsFUdYZkCFFi9HpXodKwqv9SyLAwwb8UDK3xrDlVwv8ZaZ3E8yviVfLMo67f9KVmQto_1RoJX0Homy7GDuPqXdlsEw9pgcXyJAUSFIVGBsXM9VTcwSq0eZNAmZsyJxuPdA4-XnZR91_p1vponL6rdZ8WeyQLiMuChA_UtbC8LeUugamIAfEMVFiuRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فرود اضطراری یک هواپیمای خطوط هوایی «فلای دوبی» از مبدأ دوبی به مقصد تل‌آویو در عربستان سعودی، نخست‌وزیر اسرائیل گفت کمک‌خلبان این هواپیما پس از حمله با چاقو به خلبان دیگر، ظاهراً تلاش کرده بود هواپیما را با سرنشینانش سرنگون کند.
بنیامین نتانیاهو، در پیامی ویدیویی که روز چهارشنبه هشتم مهر منتشر شد، گفت: «در جریان پرواز، هنگامی که هواپیما به کشور نزدیک می‌شد، یکی از خلبانان به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با همه سرنشینانش سرنگون کند.»
او مسافران هواپیما را «قهرمان» خواند و گفت آنها با اقدامات خود «از وقوع یک فاجعه بزرگ جلوگیری کردند».
نتانیاهو همچنین گفت عربستان سعودی کمک‌خلبان این پرواز را که به ادعای او به خلبان دیگر حمله کرده و تلاش کرده بود هواپیما را سرنگون کند، بازداشت کرده است.
او افزود: «خلبانی که دست به حمله زده بود بازداشت شده و اکنون از سوی مقام‌های سعودی تحت بازجویی قرار دارد.»
نتانیاهو همچنین دستور آماده‌سازی برای مقابله با تهدیدهای احتمالی بیشتر را صادر کرد.
یسرائیل کاتز، وزیر دفاع اسرائیل، نیز روز چهارشنبه این حادثه را «تلاش برای یک حملۀ تروریستی» خواند.
او در بیانیه‌ای گفت: «حادثه جدی در پرواز فلای‌دبی یک تلاش برای حملۀ تروریستی جهادی بود که تنها به لطف شجاعت چند مسافر اسرائیلی خنثی شد؛ آنها وارد کابین خلبان شدند، تروریست را مهار کردند و با دستان خود کنترل هواپیما را به یک خدمه پروازی دیگر که در آنجا حضور داشت، بازگرداندند.»
رسانه‌های اسرائیلی روز چهارشنبه از احتمال ربوده شدن این هواپیما خبر دادند اما بعداً گزارش دادند که «بروز درگیری فیزیکی بین خلبانان» در هواپیما باعث تغییر مسیر و فرود اضطراری آن شد.
بر اساس این گزارش‌ها، این هواپیما از نوع بوئینگ ۷۳۷-مکس کد اضطراری مربوط به ربوده شدن را ارسال کرده و پس از آن ارتباطش با اسرائیل قطع شده بود.
به دنبال این اتفاق جنگنده‌های اسرائیلی به پرواز درآمدند و فعالیت فرودگاه بن‌گوریون نیز متوقف شد.
ویدیوهای منتشرشده در شبکه‌های اجتماعی که رویترز محل ضبط آنها را پرواز FZ1073 تأیید کرده، مسافران را در حال رسیدگی به دو مرد مجروح در کف هواپیما نشان می‌دهد که دست‌کم یکی از آنها لباس خلبانی بر تن دارد.
در یکی از ویدیوها، یک مسافر اسرائیلی درخواست کمک می‌کند و می‌گوید مسافران «تروریست‌ها را مهار کرده‌اند». با این حال، مقام‌های فرودگاه تبوک و این مسافر هویت فرد یا افراد مهاجم را مشخص نکرده‌اند و جزئیات دقیق چگونگی درگیری هنوز روشن نیست.
بر اساس اطلاعات وب‌سایت فلایت‌رادار۲۴، این پرواز ابتدا یک پیام اضطراری عمومی ارسال کرد و سپس پیام اضطراری دیگری فرستاد که احتمال «مداخله غیرقانونی» را نشان می‌داد. هواپیما پیش از نخستین هشدار اضطراری، در کمتر از ۳۰ ثانیه نزدیک به ۱۴ هزار پا کاهش ارتفاع داشته است.
به گزارش این وب‌سایت، هواپیمای بوئینگ ۷۳۷ که رسانه‌های اسرائیلی اعلام کردند حدود ۱۵۰ مسافر اسرائیلی را در خود جای داده بود، بار دیگر پیام اضطراری اولیه را مخابره کرد و سپس در فرودگاه تبوک در شمال‌غرب عربستان سعودی به زمین نشست.
از سوی دیگر، شرکت هواپیمایی فلای‌دبی، مستقر در امارات متحده عربی، اعلام کرد علت درگیری‌ای که «در کابین خلبان پرواز FZ1073» رخ داده، همچنان مشخص نیست و موضوع تحت بررسی رسمی قرار دارد.
سخنگوی فلای‌دبی در بیانیه‌ای گفت: «در این مرحله، دلایل و انگیزه‌های اصلی این رویداد مشخص نیست و همچنان در چارچوب یک تحقیقات رسمی در حال بررسی است. از همه طرف‌ها می‌خواهیم تا زمانی که مقام‌های مسئول در حال جمع‌آوری اطلاعات و روشن کردن ابعاد ماجرا هستند، از گمانه‌زنی زودهنگام خودداری کنند.»
خبرگزاری رویترز به نقل از مقام‌های اسرائیلی اعلام کرد کمک‌خلبانی که این حادثه را رقم زده است، شهروند عمانی است. دولت عمان هنوز درباره این موضوع اظهارنظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMtUDg131sfCfLA9QzKEOsf2eGG2HrLvcnq_5elId5zw8YCTdlmK0K-W5IpCQnAR94iik_bP6w0_UqOKJPU7JFl9WVrmXrQl7wTM3KRoZCuDARtW_qMJH0AvlK6y9GcPfmVFwnuJVCf2wTWt75k5vhisgU5TnYflhJyzBXQ-WfzGks810-LlI17xE8EpkYxzDoVKv8hdmt5GidCmA7Htug654mbP1_BaY394ZFsNHNGnNxGqFAJli28WzDY-Y9RViQymGq7RYzi0rMe2Q9C4DL_-UdYxOyEQvWTo8KUnI3g7BROS5hgT9cozCV7dLfEAwPGTqeVmZOTQ61GONWs27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEUSKBjU6cyza0dEF0x5NPflibkIYW9_U_7V7bnXrzKuj_H_93TXr5Ap79mDMa1TsJXbYmK5a-H4n18bjSvNNMZQNzs5PSqNb_aF83bC_aKlHpFS7GMLPl5ULP1-xO7QnXVKNxGjuz--0EdvtpFUsZ1_dpknOdUSu9DFxmKjr2ESQK5tNRxIB64e8caq5W4dE4BgB2cQci12OREo1PtmP_AgJmswZ99VR0l0klyjV0od6dEZRG25_R6h_m_r7PVI-Kv6XQSAMG_K-APtokO4ITOdySZ0R_xXAdaj0GQfaPrY-6W9NpGgbRaV1D-R6ETC4UQWV4Q70VDkIxJxGQpiqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nE7AnppjwM9lXrVj-hWhY9bqWrp2s388wz8_3cXpIQcOduK7MvTtWPn7EPG1XpQfDusctkNXmFbL3IdDNIx-keT0tgsRyn9vZ9aJTT3g80RPuAAimBNPXIFy0z-g60xBVe9juEsiKICG3auqCHJ1laLRNkJ28bYgeS48y-WEVbONJ6Bzb5tgLzJEOPcMoijyLH2aRpqQIw5fo4mcEL_Qe_cSoMw6cXGtRG9pGzrTPJ-J58VlYDOA5VP8IdhS3VfXQNj2k0oRqxoiUAy2Vd0u_xDWf81g6c63hOtYcvtlaVKXPtkT9kO6mne2p1QDG7pLrhf-bc53kb6NJVoBayGuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdGrgXxUOIZofK9YjMg-kqgY-bpy49u1JoOtOlal5_QIBgw86c6Hy_q9oZcdr2PC_W2pEaaZkVudB9Uzr5AUEYyZ7mBrFyxGzPlQCwZqFt8d_FFBgdLM_iOefxGFFDl9iPZPlBSMGn4DGjkzkx5WDMxnkC-c74grhWujNsiWY8OQgeqHXoXgauZWhujfdwG0XoeoEGsUdVb_bND-w021jGRpF9MeyU9PQ52ovP5zzrQY7PCMi3iAiwyX4Z9F_lQqjNlp8HLV_UOMQiDs9TwOOs4L8G-BUtSuxhOwBkIxEQvuyoTO7hQ2KMHs8JOIOijHLpVQ6snVVEjFBrOphPz2eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
«برای کمک به پدر مجروحش رفت که  هدف گلوله قرار گرفت»
🔸
هفت روز طول کشید تا خانواده محمد عباس‌زاده بتوانند پیکر تنها فرزندشان را تحویل بگیرند. در این مدت، بارها به مراجع قضایی و نظامی مراجعه کردند، اما پاسخ روشنی دریافت نکردند و تنها به آنها گفته می‌شد منتظر پیامک بمانند.
🔸
فشارها پس از آن نیز ادامه یافت. برخی از بستگان احضار شدند، از اعضای خانواده تعهد کتبی گرفته شد و مقام‌های امنیتی برای نحوه برگزاری مراسم و حتی روایت چگونگی کشته‌شدن محمد برای آنها محدودیت تعیین کردند.
🔸
خانواده با وجود این فشارها، پیکر محمد را در زادگاهش اهواز به خاک سپرد؛ در حالی که پدر مجروحش هنوز در بیمارستان بستری بود و نتوانست در مراسم خاکسپاری تنها فرزندش حضور داشته باشد.
🔸
سرگذشت کامل محمد عباس‌زاده را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-9241/mohammad-abbaszadeh
@IranRights</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrr4cv2EqsaKYyJaMQNC0wWQKp1T0yxapv5bMhKiJUkVuPI7-KAsoJpTMabxrt1n7dbzbXN2fkYt2AeF4pybaWVQhJ2bUmLTPa7f34LYeP1KDOlsenpFbTIDUfD5-Ih9iDP3f1PtIk9Dry6gftKj0PsDdH1tM_yXNk10TydBUwyo9q1xDtUOnidNcDlybDq8AROugpZnGwTPjJ-pN76wfhrNXEghfbAx7JcYK6isGiLK2DNbZ4oNFYmLmxCbx9_fpLfzYge7KpLC7j1M4-HVu1u_tIALkxoduUsY7L8WypghzCJmlwKsmQ07Ee8uCIMMX9DYvVtoDhHoS2c7RAFQfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mjUSAoPgmj5IsUPrFcvrfXthPheUEWr6gCMQNdR9S1d3VxZjvA4r5nv5RMucQ_jf0TdpTgsyuFsDhmwHLd4bTAAoG3gQCuJL6tAcxwHTg7bu7P4jsw2F73Gja2qvbm00VS2en7NJveLZUKRdYefaT6XfGsHo3uiz1_2HBEa52P7O0UgKjcNCJcfQGgzyF9ToQmhcTE5hhE0WzwrO4SGQ-2a_joctQ_GzEMf7CtLuq2IMG1JUQKmmUhEuLUl9bMxyPDEpYmFx83ftIXvrv4XKt1xN-OtOFd8KUo66wK9GyPolyrHyn0fKiVUG865RqCqW9IDW_SeGuKVMCHEm3uA_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UCghl-hAqcv3ACBV6Gzt1vYzZDVL31gOjjSWfXrmPkAzGNQxtheYdNRkp0d1Xdr8Yff7KJwpFIbOQR-vyTI5985oIlya49NsGHruU1L7RQMPEpyY9CunWYDmxQ216CoaJHmg3NOdZm3wos-PBV78bzRn46Y4ngyzpyr01HjEyBtx4IR5-uCZKPNo1QB2IPGtjw2gukOdGGePmqzrTQrnpV2T7qfPnM0mdIbNHEIupLyjzX9onrtO3rM3J5IoCw3DCxoIlAP3jX2kCFOO-QJUCytDtWeU5hi2LAw87ESDHfxaJCmfNIOHC1EzD6m0dZ4ieQ22uzoAMf5OlW470ajjjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن رضایی، دبیر "شورای عالی امنیت ملی"، در دیدار با شاهین مصطفی‌اف، معاون نخست‌وزیر جمهوری آذربایجان، با تکرار مواضع دیگر مقام‌های جمهوری اسلامی گفت: «ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.»
او افزود: «شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصره هوایی روی آورده است.»
رضایی ادامه داد: «آمریکا آینده‌ای در منطقه ندارد و ایران با قدرت در مقابل آن ایستاده است.»
@
VahidOOnLine
ساعاتی پیش از این عباس عراقچی در آستانه بازگشت از نیویورک به تهران گفته بود که ماموریتش در این سفر این بود که شروط ایران از جمله درباره بازگشایی تنگه هرمز را به اطلاع ایالات متحده برساند.
وزیر خارجه در جمهوری اسلامی گفته بود که «ایران در این خصوص طرح دارد، شروطش، کاملا عادلانه و منطقی است و اگر آمریکایی‌ها ادعا دارند که دنبال توافق هستند یا دنبال یک راه حل مسالمت‌آمیز هستند، ما این راه حل را معرفی کردیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f601498008.mp4?token=bqd6kl0NYAEYpvWKu0vB8lU1cHZNjlCKhMOQmW6LdJ_T98cbAKsMQ88jRyeo9VCpirKdYRmn9SW3aOSDSQgTyRbByqOH60FaZkRUMZ555djoE_r3GuN4C6M_453WlQiJywA1UZfZz58PUabEIIsQ8-ih6o9rVh_wiSTMOT7mZLPnCUtWAGd4F9gjSzkgrBFfkbmFj9FbOCoXdwv3miPicLov16oUTdxz8Gr853EAmiDBoYoryLnsdzidhw2nl_RMgtKPdp9frr7ya7gIU7mry2ihS6wvnhGE6QjUGV6QxXjKQsjeMTKrsxftespMoPiyqT7UFwFEBmJhSPCoeMeAdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f601498008.mp4?token=bqd6kl0NYAEYpvWKu0vB8lU1cHZNjlCKhMOQmW6LdJ_T98cbAKsMQ88jRyeo9VCpirKdYRmn9SW3aOSDSQgTyRbByqOH60FaZkRUMZ555djoE_r3GuN4C6M_453WlQiJywA1UZfZz58PUabEIIsQ8-ih6o9rVh_wiSTMOT7mZLPnCUtWAGd4F9gjSzkgrBFfkbmFj9FbOCoXdwv3miPicLov16oUTdxz8Gr853EAmiDBoYoryLnsdzidhw2nl_RMgtKPdp9frr7ya7gIU7mry2ihS6wvnhGE6QjUGV6QxXjKQsjeMTKrsxftespMoPiyqT7UFwFEBmJhSPCoeMeAdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
و ایران سلاح هسته‌ای نخواهد داشت. آنها به‌شدت در حال شکست خوردن هستند؛ خیلی بد، خیلی بد. این وضعیت خیلی زود تمام خواهد شد؛ خیلی، خیلی زود. آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت هم به‌شدت پایین خواهد آمد، درست مثل قبل.
من مجبور شدم آن سفر کوتاه را به جمهوری اسلامی ایران انجام بدهم؛ سفر بسیار خوبی بود.
فکر می‌کنم در سال‌های آینده درباره این موضوع کتاب خواهند نوشت و تاریخ کشورمان را خواهند نوشت و خواهند گفت که این یکی از مهم‌ترین کارهایی بود که انجام دادیم. در واقع، این یکی از مهم‌ترین کارهایی است که در دوره دولت من انجام داده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sf3uyU048yxkZ6JjuSZwMKlUlZZmxt50a6fLzKVMe0Yo0B5iPmddjK8IznvPdolnnXNIaHdFIt11jiCUTjXiqxCftH504MU7atj2JVUAaEZ8WnMY_k3o7OEJ7lPkj1KL-RRmpyDm4_FGU5kfnK-H3tX353Ie2Y2p3yCMF2k7VVWcC7eVZ7z5EZ7G6H4d7hoXAiUQBK4pmGYakMHRdZZGynbuvHL6PaOZ5lLOTCEZYaDEVqg4H_PejTXe1DdWzSH0lsKVWz-b8739kahQQBonW0pZec3wu_ffF66kOQVaK45CcF2-mrbRztGg4jj7DSM48Bllpvt538DJ804cyOdG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران با نقض تفاهم‌نامه اسلام‌آباد مرتکب اشتباه شد
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در مصاحبه با وینسنت کُگلیانیز، پادکست‌ساز و روزنامه‌نگار محافظه‌کار آمریکایی، مقام‌های جمهوری اسلامی را مسئول فروپاشی تفاهم‌نامه اسلام‌آباد معرفی کرد و گفت آن‌ها با هدف قرار دادن کشتی‌های تجاری در آب‌های منطقه مرتکب اشتباه شدند.
ونس افزود: «فکر می‌کنم ایرانی‌ها متوجه شده‌اند که اشتباه کردند. آن‌ها با ما توافقی امضا کردند، آتش‌بس برقرار شد، قیمت انرژی کاهش یافت و این امکان وجود داشت که اگر ایرانی‌ها به تعهدات خود عمل می‌کردند، از بهبود روابط با آمریکا منافع زیادی به دست آورند.»
او همچنین به ابهام‌ها درباره وضعیت مجتبی خامنه‌ای، رهبر جمهوری اسلامی، اشاره کرد و گفت واشینگتن با قطعیت نمی‌داند که او زنده است یا نه، اما شواهد موجود نشان می‌دهد که همچنان در قید حیات است.
ونس ادامه داد: «ما فکر می‌کنیم او زنده است. البته با قطعیت نمی‌دانیم. من هرگز او را ندیده‌ام. اخیرا هم تصویری از او در مقابل دوربین ندیده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWv1m1g8R27E2Mi5LzPI3A9pdFFXCBJqpUwlQKp1Zr4SWMsZwwPVBW20NMCJ9Q25OhUSbp8z14ForMeTwHbI8iks3lkc8Cc-89iCkc-ArgXJ2J5mYJL_WzCBU4uot6ZUs1U70CoMvPKT-Q6o67vXve8BMIucyfYyMADX2wKniY5AvNJux6DMW0vOstTnxxnQU1-IgFB0yJcw-V_92vPspKPTGbIleY0MRh68Zz5nFDg1ssD2U8FYmyZURHnyeVCkD2bNXppyU6il5BwkIGUYYuaH-E9eaQflpXtDfpbzenxPqLaZdaHjjkbvbcCbTiXYABdMQP2bCXyXH-vXY704mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYrMeDdMmCHhPFUJDhadecMuL0rIF7u9iIWmtzs8UwbInhiozvYIVzCi7OWUor235ZkeKo_w73QYJ514gMC2SP-yvXZoZ2T5Km_ffbT8-GI4t0s87eca6sf9uY_vMWBcD-GckkNodOw6PHSB0w3Lgze7h17QrHzO-1ThPISETkoL_lfeMj65AEdKoOeAO-rqMhgF_A6qjXFv1-WtTdg6c_8fV0ouaojnAJ4SDwQDlQLdhSVq8ynzHhqCFBUNHkEixxcD2Ay0aZCp3vEBmUDSASAJgLS0EnJ7Hz-ZV8yIcdg92nX6NdpbY1w3rsbwNR21ewWKsJOhFauvFRp34J-2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k1Ef9zbpOmtkSbHES9NNx4CSziCGJ41_LrLgMfVTqP2Xrb2i40gYWAYiKarMoXngyFkdqYtu6geYCczRhQMZIChi6NwvLWQ67ru8Trj7z8GieZNa8kOoYMfkAqBYi4ZiPORIDR21gVdCXordI9vPAShtEmx3bOMyRD6_wPOsAsUDdNdKqEZFPBSfg8rZLFEzit_6edkp8zHL8Szc9n4vhPhLL8kpS3HK23zu7P5MZ9Kc6fRmsK-gFT3k4Pwrrkj_K3j3xSzBQW8NwFapF4uySUdW0VOuk6yO4doBT7ciil4LAPxiX97BVU1GnA3V53qz1kiylbV8rUDnKTq3POryKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u89pCLG6VnLgXbpY8voOOCu6gw0-9AjaESz_gwZNjJVBhxP8nDHuAFkbpW7T5OdAvHFzr4ot72mp1pyLCG7IK7aGQ0ZhUslT5xs9KdC9Ub-UGEs396Z8f0xPplqmTDBAaoZGYDOwqvTo4fqWe2y0XRafH2fe4_so1n_Za3zo5a6DaNI78nooCn0qN6Hkl-z0QRwOH4bEUh5z-O3DMoaSjkNlCFsK-WOin9y8F9rFE9nQ_FmNyGIlRMgL0Sb-2i6ygdOaQ4FBcp3sEzJ6qUZnTK-PkCKbnY2i80FwU16P0Z9ZvluC_iIfRrSLDo4S0KixGLOFp-9JQ5HaIUuh0LcMGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی روز سه‌شنبه ۷ مهر متن نامه‌ای خطاب به مردم آمریکا، دانشمندان، دانشجویان و اصحاب رسانه این کشور منتشر کرد.
در بخشی از این نامه که به زبان انگلیسی نوشته شده، آمده است: «حساب خودتان را از اشغالگران فلسطین که خواه‌ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.»
سپاه که در دوره اول ریاست جمهوری ترامپ در فهرست سازمان‌های تروریستی آمریکا قرار گرفت، در این نامه از آمریکایی‌ها خواسته است «در برابر سیاست‌های دولت خود موضع بگیرند» و «امور خود را به جای اراذل به اندیشمندان بسپارند.»
@
VahidOOnLine
حسین محبی، سخنگوی سپاه پاسداران، در نشستی خبری با خبرنگاران خارجی درباره نامه سپاه پاسداران به مردم آمریکا گفت در این نامه درباره «میزان محبوبیت» سپاه پاسداران در ایران و خدماتی که به گفته او به مردم ایران و منطقه ارائه کرده، توضیح داده شده است.
محبی گفت: در نامه خود حقایق ژئوپولیتیکی را برای مردم آمریکا روشن کردیم.» او افزود: «از مردم آمریکا خواسته‌ایم که نامه ما را حداقل یک بار مطالعه کنند.
سخنگوی سپاه پاسداران گفت: هیات حاکمه آمریکا به مردم خودشان دروغ‌های بسیاری می‌گویند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u8MiDD_fzWpLIPLb3x82VLcOzHCUZ4bHbKVNfCkeZ3AStAst6vif2RL7j4OX4UW2EVoDOqCs9fj1i_vj9Tl1dvUP9uov_1Fo6YGjiYzNOWPxLPftdISlzCHpA6Xu95uas-mENxnugRTVswt0YG-ziYT156fmP7cLS6DDQqFaud8vz3DjMsfvVxTUqS0WoGlpFsVU2TvEYUkpr2Vtw6TdZR8iIqD_KfGI5B0xd7tUeamGvRbDYezpUNkTxetYhR9SWEcSKdBb-IQ3j9PPBjjB8CmspVkMrBN1_N2RakgwLd4Ney3L-JOh8bXnnALnAV4WH9R6k4zFRkIkfL6quD-9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Iqf2oYiYDVRCSx1pKzpOajRV-8DlJ9D58g-19Jojk8AvyxMYx1-b8yTc62g8KPNK37PABpfHQqYc2WQXXaeMeMSl97kSrdGBvbMQvQQBiZULfYgzJTqQYSG5mlMpetL0pWfki-O6PipTgP6FSLKLnVVVLcJ_CIFHASHFVyYhLtLlQwTipkwqgyj3T2RGAfw6Y0RaWDHKsrqJnyG9RwzH0S2D17C8RlvoYAnZ0S9ryW4OcnymNaktiWTa1tx8kscoJx_79IhWJHsmwbl7MV8tu2gY8btx-EMnHWUUkXiCh7uoJYfOJrOBwoqeog-gAUzyoOubdn7W6r0Gmjxq2RjBPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سه‌شنبه هفتم مهر در جلسه علنی وبیناری مجلس، آمریکا و کشورهای منطقه را به حمله به زیرساخت‌ها و نفتکش‌ها تهدید کرد.
این در حالی است که روز سه‌شنبه جمهوری اسلامی در انتظار پاسخ رسمی آمریکا به پیشنهادات تهران است که دونالد ترامپ قبلاً گفته آنها را رد کرده است.
قالیباف گفت: «در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.»
رئیس مجلس شورای اسلامی در عین حال مواضع دونالد ترامپ علیه جمهوری اسلامی در جریان مجمع عمومی سازمان ملل را «سبک‌سرانه» خواند و به او گفت: «بچرخ تا بچرخیم.»
روزنامه خراسان، نزدیک به محمدباقر قالیباف، هم نوشت: «اگر مذاکرات به دلیل اختلافات هسته‌ای به نتیجه نرسد، جمهوری اسلامی فرصت استفاده از نقشه دومش را خواهد داشت تا به انجام حملات پیش‌دستانه روی بیاورد و یک دوره جنگ پرفشار را قبل از پایان انتخابات میاندوره‌ای به ترامپ تحمیل کند.»
شماری از نمایندگان مجلس شورای اسلامی نیز دیگر کشورهای منطقه را به حملات جمهوری اسلامی تهدید کرده‌اند.
از جمله علیرضا سلیمی، عضو هیئت‌ رئیسه مجلس، در گفت‌وگو با خبرگزاری خانه ملت گفت: «باید پذیرفت که امنیت در منطقه یا برای همه خواهد بود یا برای هیچ‌کس».
او افزود که جمهوری اسلامی در برابر هرگونه اقدام تخریبی در منطقه «تماشاچی نخواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=qo2N3jbG1OMOueyHjxa05L5AMq8UFdOtw2s73P4W4PY5kwywEgJQbsAfY-inj39gAyrzmzzAubFEiTbe9Z6mXm7PlAQiIF1gbSD0E9YX22Bsgd9-fjV9f59pEBRdHgtKIwDZINvhwUdBk3ERZ72MHyR8p9xM2owgw1iXtmXjPP-_SKXqrlqWXcEuA7JoSnDLO_L_2qlRYPLku6eO6l1ae_LUFOfrm5h_xZw2mLqzizTiXCpeTQJoqW6JHvNqlqEV8_IrY41ljNAsLgsaiprg8DMgfffj1CimrNo9lgV5J-L20Tj_CrF1Z-AR2oO5Olt6QEMZYH2my9nD8nMTUj6VQgjZqBHF2llaObOdQLw9hd1L03e-9eHYLqryjRKBAWk5NSilOV7pzotwNtpM-FveyMP3HB0WEP1bPDwzr__K4U-jWnRHJDcD1gUTJ97CAIUBD9Aal_jN67aOOF5irZZgm5cwWcYO8NzIDueq24u3mfJJOZ7o5cX6TJR5pl8eajRIlcTVCEU_5ds4ct0bo1mEPk8lzPyliWAgEYDiDACPiyuGjAT2PVl6Umwqu0AxClb4zaYc51rq4vRdZRt8rjrAuRgP0z6_1uNjHFhFFPnk4hTi7JG72nfRpJ-spXZdZHy9xDbSDV4pjzYZeKpZ5bmcwA1OzHcZN_k26M_8yR22VPE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=qo2N3jbG1OMOueyHjxa05L5AMq8UFdOtw2s73P4W4PY5kwywEgJQbsAfY-inj39gAyrzmzzAubFEiTbe9Z6mXm7PlAQiIF1gbSD0E9YX22Bsgd9-fjV9f59pEBRdHgtKIwDZINvhwUdBk3ERZ72MHyR8p9xM2owgw1iXtmXjPP-_SKXqrlqWXcEuA7JoSnDLO_L_2qlRYPLku6eO6l1ae_LUFOfrm5h_xZw2mLqzizTiXCpeTQJoqW6JHvNqlqEV8_IrY41ljNAsLgsaiprg8DMgfffj1CimrNo9lgV5J-L20Tj_CrF1Z-AR2oO5Olt6QEMZYH2my9nD8nMTUj6VQgjZqBHF2llaObOdQLw9hd1L03e-9eHYLqryjRKBAWk5NSilOV7pzotwNtpM-FveyMP3HB0WEP1bPDwzr__K4U-jWnRHJDcD1gUTJ97CAIUBD9Aal_jN67aOOF5irZZgm5cwWcYO8NzIDueq24u3mfJJOZ7o5cX6TJR5pl8eajRIlcTVCEU_5ds4ct0bo1mEPk8lzPyliWAgEYDiDACPiyuGjAT2PVl6Umwqu0AxClb4zaYc51rq4vRdZRt8rjrAuRgP0z6_1uNjHFhFFPnk4hTi7JG72nfRpJ-spXZdZHy9xDbSDV4pjzYZeKpZ5bmcwA1OzHcZN_k26M_8yR22VPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pJvoj2ulFOtwLIdl2Jt0SBgLQP2udF_EBAP1_wfNJxcnr0PCUA0rwo9AnNM-8EMR_dTmrIdCB0jWC7meC2QvVdAakc37Vqe8zaf1edCrA6Bwf1DUogeKPwuol9-KFG5gxPC849LKyYk4uMHSq2U33ENEiWaXnKDDCwO65_lCdrDaN-DHuFEGGxw1Z5LwDT_jeAe8apjXalDWKphFhMEO44gZOueHoU8HJhYgBdxhFMqSnEvFx_qcXNC9wqUTjFEoQInOfYjn6XQ-hW8lw0CyRxeA9TfUa4VtldbaKAn_VH4Bk8j5OTGgpaEW7BNDtlKupD7pLr_cZrlMHmdu9El2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qAcKqkrG0mjx0m8gXo7EB5deqK7Bg104tWO7UHb_tKHpCRczFE-LBC3n6M5JU8P0c9j73deY4DSXXHo99kB3i26q9kwL_Wy0xEKKK5gkqQzbvF34nigVZgaB-MQ1AkhtjaXWRHFCvGCn5QatvzvLY6fwqbSw3ORbcDKZIhBFb1W7k-BkSQeMCGt4XfiL5lHtY3JqX5BDRQk5MqXGbJNZU1jOz5ZnqO2fxqRLCsc3ErmtjuU_ADUwhYXJNZABFIQl3B7KSpwPWLRNQcd6FMvjK2uIS33TjE1bplRNgezcHMQNnA_r-mvxsHyBDxc2vKaVjBNNDZheIXN21sACJMMeuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، روز سه‌شنبه هفتم مهر در گفتگو با شبکه فاکس‌نیوز گفت رژیم ایران پولی را که به دستش می‌رسد خرج مردم نمی‌کند، بلکه آن را صرف ساخت تسلیحات و صدور انقلاب می‌کند.
او با اشاره به عملکرد تهران طی سه دهه گذشته افزود: «مسئله صرفا تحمیل هزینه‌های اقتصادی بر این رژیم نیست. پای هر دلاری که ایران در اختیار دارد در میان است. آنچه آن‌ها در ۳۰ سال گذشته انجام داده‌اند این است که هر زمان پولی به دستشان رسیده، چه در چارچوب رفع تحریم‌ها در دوره اوباما و چه از مسیر فروش نفت و گاز، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم ایران خرج نکرده‌اند.»
روبیو در ادامه گفت: «آن‌ها این پول را تنها برای دو هدف استفاده می‌کنند: ساخت تسلیحات برای خودشان و صدور انقلاب. آن‌ها این منابع مالی را برای تامین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق به کار می‌گیرند. آن‌ها این پول را برای حمایت مالی از تروریسم و طرح‌های ترور در سراسر جهان خرج می‌کنند و بنابراین هر پنی که به دستشان می‌رسد، پولی است که برای مقاصد این فعالیت‌های مخرب استفاده می‌شود.»
@
VahidOOnLine
مارکو روبیو، در گفتگو با شبکه «فاکس نیوز» با تاکید بر اینکه نباید ایران را با حکومت فعلی آن یکی دانست، گفت: «مردم اغلب این اشتباه را می‌کنند که ایران را معادل یک کشور عادی می‌دانند. بله، ایران یک کشور است، اما مشکل ما کشور ایران نیست؛ مشکل، انقلاب و سیستمی است که بر آن کشور حکومت می‌کند.»
او با اشاره به مقامات جمهوری اسلامی که با پوشش‌های دیپلماتیک در رسانه‌ها ظاهر می‌شوند، افزود: «کسانی که در ایران تصمیم‌گیرنده هستند، روحانیون تندرویی با دیدگاه‌های آخرالزمانی‌اند که باور دارند رسالت دینی‌شان رقم زدن روزهای پایانی جهان است.»
روبیو همچنین هشدار داد که دستیابی چنین رژیمی به سلاح هسته‌ای، یک خطر غیرقابل‌قبول برای جهان خواهد بود، چرا که از آن برای باج‌گیری و کشتار استفاده خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iuWlktllwUgkmbM9GYefyJYuvnZ43B8_iI6N0wTFXT_VLpk0IMjUn5MICXFdQcnP8_aC9o3XueLWTy--YFWFFTfu_C1Yp2yllOelFBGzCm__SoR3MZcsj0jkrtebeAFUGpaWAIstx-UmmqBGT1XLudtt0XKjOrOsQ48r5KFcGlWC_0QgQCNY5Jgq6pGd0CfSUjFAmWopCEf61ZSDm1t7ofMkvkQ1imyfmzlTLcZmr1rp5hVIyGl2nDqpxk9v93znrWwzMNGFWkwseGnzEvidL1o32wKEEvMfBacFmrhgy-MQfrkxjguGnc3lXJJPG1k1w7daIjD7fY92HRqLoxZA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=C-wZtYrSxUIf1l_CVo-oW95-rrzo2D_MEI2XeMOsQkzTVw5OTM8Lz9GaM_t04s94vkKpnIR8CEm-TBBBX2N0pzXY8iQzB_ClNgW_MmRH2oGnZFhIdXEMJRCPOW7KMnNTyc_RAhIWX-Ia9_4O1VhM20dD5UDrb5aLI94JV-b6TCKsuqS9LUMeRjfGkvp2v9Ya4nVf-cY_OPxpF56XEPUdJBVMzyjoodhcSMXwI-_VCubqXSJktXJfUZ6-qleHcjtTdKVOQ_jRDseZ1CbkXgoLfDHcD9IGhF892zYeQaiOQ1HZVgdxQ9zN3SXkm-5Zg1lLpvIW6MkFYlc3iKxXgh251Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=C-wZtYrSxUIf1l_CVo-oW95-rrzo2D_MEI2XeMOsQkzTVw5OTM8Lz9GaM_t04s94vkKpnIR8CEm-TBBBX2N0pzXY8iQzB_ClNgW_MmRH2oGnZFhIdXEMJRCPOW7KMnNTyc_RAhIWX-Ia9_4O1VhM20dD5UDrb5aLI94JV-b6TCKsuqS9LUMeRjfGkvp2v9Ya4nVf-cY_OPxpF56XEPUdJBVMzyjoodhcSMXwI-_VCubqXSJktXJfUZ6-qleHcjtTdKVOQ_jRDseZ1CbkXgoLfDHcD9IGhF892zYeQaiOQ1HZVgdxQ9zN3SXkm-5Zg1lLpvIW6MkFYlc3iKxXgh251Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز دوشنبه ۶ مهر ۱۴۰۵، در کاخ سفید گفت آمریکا «خیلی زود» در جنگ با جمهوری اسلامی پیروز خواهد شد و پس از پایان جنگ، قیمت بنزین به‌شدت کاهش خواهد یافت.
ترامپ گفت: «این جنگ تمام خواهد شد و ما در این جنگ پیروز می‌شویم و قیمت بنزین با سرعت زیادی پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست چنین کاری را انجام دهد.»
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت آمریکا مانع دستیابی تهران به سلاح هسته‌ای شده است و افزود جمهوری اسلامی این موضوع را می‌داند و حاضر است به آن اذعان کند.
@
VahidHeadline
متن زیرنویس، ترجمه ماشین:
ایران هرگز سلاح هسته‌ای نخواهد داشت. ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام می‌شود و قیمت بنزین به‌شدت پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست این کار را انجام دهد. هیچ‌کس دیگری.
اگر دموکرات‌ها سر کار بیایند، مرز فوراً باز خواهد شد و میلیون‌ها نفر درست مثل قبل سرازیر خواهند شد. این وحشتناک‌ترین چیزی است که در عمرم دیده‌ام.
بله، آنها حاضر نبودند جلوی ایران را بگیرند که سلاح هسته‌ای داشته باشد. گفتند: «بگذارید یک نفر دیگر این کار را بکند.» البته این را درباره خیلی‌های دیگر هم می‌توانم بگویم. ما جلوی دستیابی آنها به سلاح هسته‌ای را گرفته‌ایم. آنها هرگز سلاح هسته‌ای نداشته‌اند و این را می‌فهمند و حاضرند آن را بگویند.
وقتی جنگ تمام شود، دو اتفاق خواهد افتاد. اتفاق اول در واقع همین حالا هم افتاده است: ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع بسیار بزرگی است، چون اگر می‌خواهید آشوب و فاجعه ببینید، بگذارید آنها یک شهر را با سلاح هسته‌ای نابود کنند.
فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. نباید بگذاریم با سلاح هسته‌ای به ما حمله کنند. برای همه آن آدم‌های احمقی که فکر می‌کنند اشکالی ندارد، من با آنها سروکار دارم و آنها دیوانه‌اند. هیچ تردیدی در این نیست. آنها آدم‌های بسیار دیوانه‌ای هستند. همیشه این را به خودشان می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.» اما آنها نمی‌توانند سلاح هسته‌ای داشته باشند و ندارند.
پس این موضوع بسیار بسیار مهم است که ما در چنین وضعیتی قرار داریم. این کاری است که سال‌ها پیش باید توسط رؤسای جمهور مختلف یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم، اما ما با فاصله قدرتمندترین کشور جهان هستیم. بهترین تجهیزات نظامی جهان را داریم.
و ضمناً، اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات نظامی تولید می‌کنیم. چاره‌ای جز این نداریم. شرکت‌های بزرگ دفاعی در حال گسترش فعالیتشان هستند. مثلاً لاکهید پنج تا می‌سازد. ریتیان هم تعداد زیادی می‌سازد. همه‌شان دارند مقدار زیادی تولید می‌کنند. اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات در راه داریم و به‌زودی واقعاً تولیدشان شروع می‌شود، چون این کارخانه‌ها قرار است شروع به کار کنند.
قیمت بنزین خیلی پایین خواهد آمد و همین حالا هم، می‌دانید، اگر نگاه کنید، فکر می‌کنم پیتر، این صددرصد است.
پس ما ارتش ایران را از بین بردیم. تقریباً هرچه داشتند را از بین بردیم و هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ما بدترین تورم تاریخ را داشتیم. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که در دوره بایدن شما برای بنزین خیلی بیشتر پول می‌دادید.
بیایید درباره همه این چیزها، می‌دانید، همه‌چیز صحبت نکنیم. در دوره بایدن، شما خیلی بیشتر برای بنزین پول می‌دادید تا الان.
و کاری که من کردم این بود که وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاق‌ها برای جهان، برای ما و برای بقیه جهان باشد. اسرائیل الان نابود شده بود. دیگر اسرائیلی وجود نداشت. دیگر خاورمیانه‌ای وجود نداشت. و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا می‌آمدند. و من جلویش را گرفتم.
و این آقا داشت ۱۸ میلیارد دلار در آیووا سرمایه‌گذاری می‌کرد. او می‌گفت: «من می‌خواهم از آمریکا صرف‌نظر کنم. قرار نیست ۱۸ میلیارد دلار خرج کنم»، چون ما یک دیوانه و یک کشور دیوانه داشتیم که با سلاح‌های هسته‌ای این طرف و آن طرف می‌گشتند، چون قدرت بسیار زیاد است.
اما هیچ‌کس درباره‌اش حرف نمی‌زند؛ هیچ‌کس درباره همه آن کارهای باورنکردنی حرف نمی‌زند.
باز هم، خیلی از شما... نمی‌خواهم بپرسم، چون می‌گویید: «اوه، ما قرار نیست این را گزارش کنیم. ما رسانه اخبار جعلی هستیم. اجازه نداریم گزارشش کنیم.»
همه شما حساب 401(k) دارید. لازم نیست چیز دیگری درباره شما بدانم. حساب 401(k) شما در مدت کوتاهی دو برابر شده است. دو برابر شده. ثروت شما دو برابر چیزی است که مدت کوتاهی پیش بود؛ تک‌تک شما، و این به خاطر من است.
خوش بگذرد، همه. خیلی ممنون.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">"ترامپ در ازای امتیازهای مشخص هسته‌ای، به ایران پیشنهاد گشایش اقتصادی می‌دهد"
اکسیوس، ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، آماده است در ازای برداشتن گام‌های مشخص از سوی ایران در ارتباط با برنامه هسته‌ای، به ایران تخفیف تحریمی بدهد و دارایی‌های مسدودشده ایران را آزاد کند؛ مقام‌های آمریکایی این موضوع را اعلام کرده‌اند.
🔻
چرا مهم است:
پیام آمریکا به ایران در حالی مطرح می‌شود که میانجی‌های قطری و پاکستانی این هفته بار دیگر تلاش می‌کنند میان دو کشور در حال جنگ به توافقی دست پیدا کنند.
▪️
در حال حاضر، دو طرف بر سر مسائل کلیدی فاصله زیادی با یکدیگر دارند. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار آن است که ایران با امتیازدهی در زمینه هسته‌ای موافقت کند.
▪️
با این حال، این پیشنهاد پس از آنکه ترامپ آخرین پیشنهاد ایران را رد کرد، روزنه‌ای از امید برای دستیابی به یک گشایش دیپلماتیک ایجاد می‌کند.
🔻
تحولات اصلی:
میانجی‌ها امروز در نیویورک با عباس عراقچی، وزیر امور خارجه ایران، دیدار می‌کنند تا درباره پیشنهادی از سوی قطر گفت‌وگو کنند که طرف‌ها طی چند روز گذشته مشغول مذاکره درباره آن بوده‌اند.
▪️
انتظار می‌رود میانجی‌های قطری اواخر روز دوشنبه یا روز سه‌شنبه با مقام‌های دولت ترامپ دیدار کنند تا برای دستیابی به یک گشایش تلاش کنند.
▪️
یک مقام آمریکایی مطلع از مذاکرات غیرمستقیم، این گفت‌وگوها را «مثبت و سازنده» توصیف کرد و گفت ایران «نشان داده است که در مسائل هسته‌ای انعطاف‌پذیر است.»
▪️
اما این مقام همچنین گفت هنوز اختلاف‌هایی وجود دارد و تأکید کرد «تا زمانی که به مسائل هسته‌ای پرداخته نشود»، توافقی در کار نخواهد بود.
▪️
این مقام گفت: «طرف‌ها همچنان درباره زمان‌بندی تعهدات و اینکه چه کسی باید ابتدا کدام گام را بردارد، اختلاف دارند.»
🔻
آنچه می‌گویند:
این مقام گفت: «تردد در تنگه هرمز همچنان در حال افزایش است و محاصره و تحریم‌ها همچنان موقعیت ایران را تضعیف می‌کنند. موضع آمریکا هر روز قوی‌تر می‌شود و رئیس‌جمهور ترامپ همچنان صبور است و کاملاً به هدف خود مبنی بر اینکه ایران هرگز به سلاح هسته‌ای دست پیدا نکند، متعهد است.»
▪️
این مقام افزود که کاخ سفید نسبت به وعده‌های ایران بدبین است و ایرانی‌ها را متهم کرد که با شلیک به کشتی‌های تجاری در تنگه هرمز در ماه ژوئیه، آخرین تفاهم‌نامه را نقض کرده‌اند.
▪️
این مقام گفت: «آمریکا این بار به تضمین‌هایی نیاز دارد که نشان دهد ایران جدی است و صرفاً تلاش نمی‌کند از شرایط دشواری که در آن گرفتار شده، خارج شود.»
axios
🔄
آپدیت:
ترامپ تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=Tz4U6NGuXhkzyNxFnsd2PxdKsb2ZQpYGKxJCHgV4F3FvyRr_SvtFWtpr5eRE2NisSIdHVvpU_c5AWpQhX-4qbFdwPEPxYgEUwwRNZmEgPvopxtgdB4LGIEffgStIRQ-ysyWVMaTFbs-1ozPJPYZ85NWieDWzb0rXhOJ8W2rGK3bSFSdaXNN_gkzBhAbfbinEcDpryDZVVguj1PtoAQoO8KThZvAN2WUTMBI0iARMe2PcoZeMIS8ZvjzZZhgx-UInSVYjirW3EcIlQfH2XahbtuNEMAo2iOlP8HT7s_a65HvqF418VN13NcL8DGiLuHoAgIk0ZfBiyFm5EISN0jChdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=Tz4U6NGuXhkzyNxFnsd2PxdKsb2ZQpYGKxJCHgV4F3FvyRr_SvtFWtpr5eRE2NisSIdHVvpU_c5AWpQhX-4qbFdwPEPxYgEUwwRNZmEgPvopxtgdB4LGIEffgStIRQ-ysyWVMaTFbs-1ozPJPYZ85NWieDWzb0rXhOJ8W2rGK3bSFSdaXNN_gkzBhAbfbinEcDpryDZVVguj1PtoAQoO8KThZvAN2WUTMBI0iARMe2PcoZeMIS8ZvjzZZhgx-UInSVYjirW3EcIlQfH2XahbtuNEMAo2iOlP8HT7s_a65HvqF418VN13NcL8DGiLuHoAgIk0ZfBiyFm5EISN0jChdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePlV2IlNwzuhz57cNteharF1XqVJFtOq8SfTarc9f9bnvjXi4GgiM0B--sAfegvNIKXnOSUiz64I4vFDZaZaUTNmGGnUsV1ioLzqM8ZcLVn4Eq6RkNp-jmqsxrsNYuoSifOhFmYJf5XUMZGbn8A0q0li4n0OuLUb7bmYuG5_QtkBwF9FpwYh3--LnWjKM1QYLtPj1HZiYNNcJ-2R2Vbmm158IC36fJb6Wxa0VYFwzN5UhAk8F7p54Yil4dZ3VCgFKD9gMCppO4CZYEZs1A4TyZeyTKI8mjmsr4IvQ13Sghx0hy8gr10r5FbVGLGX6cQHiBmFopoJZDLpMN8fDMp1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CFgAOLdOiF1Mec6-HJ1BGAFykp-9xNrwBYaYsJcyuZpWaS3B4rMJJm40gvnDmgZzzOZshosAvZe33fKw3lECoGHBHMZ0sD3L07H_p5NGor1GmixJnziv7glo6UiOYKpiAQInHAJ9plNxq70KWY9z-oo91ZzOKobnT7jlkbn703gNLfERKy27r4dR-UN7Z1W_M851McUqm0VuiB6yaCo0J5t6Boaeq5BuCzLt7-rwBOk9KBskmLUTIkonsdKvUWlLUj6bEBKCQ__dZVlGFeBYBsSLDSFIWBQYbzzRxCThY5NUYgTPWhlwN1oK0zCc9UwS0CPGF8pvmnxhbTdLeY3X8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارز در بازار آزاد ایران روز دوشنبه ششم مهرماه تنها در چند ساعت بیش از ۶ هزار تومان افزایش یافت و دلار از ۲۳۶هزار تومان به ۲۴۲ هزار و ۵۰۰ تومان رسید.
سقوط آزاد ارزش پول ملی ایران، همزمان با تشدید تنش میان تهران و واشنگتن و در حالی که تحریم‌های همه‌جانبه و بی‌سابقه آمریکا علیه جمهوری اسلامی ایران ادامه دارد، وارد مرحله جدیدی شده است.
سایت‌ها و کانال‌های اعلام قیمت ارزهای خارجی گزارش می‌کنند که روز دوشنبه، یورو به مرز ۲۷۶ هزار تومان رسید و پوند بریتانیا هم رکورد ۳۱۸ هزار و ۶۰۰ تومان را شکست.
@
VahidOOnLine
قیمت دلار در بازار آزاد ایران ظهر امروز دوشنبه ۶مهر۱۴۰۵ از مرز ۲۴۳ هزار تومان عبور کرد و رکورد تازه‌ای بر جای گذاشت.
اما خبرگزاری «فارس»، وابسته به سپاه پاسداران، افزایش نرخ ارز را به اظهارات وزیر خزانه‌داری آمریکا، کانال‌های تلگرامی و فعالیت دلالان نسبت داده است.
دلار صبح دوشنبه از مرز ۲۴۰ هزار تومان گذشته و تا ۲۴۰ هزار و ۵۰۰ تومان افزایش یافته بود، اما تنها چند ساعت بعد قیمت آن از ۲۴۳ هزار تومان نیز فراتر رفت.
@
VahidHeadline
به نوشته هم‌میهن، قیمت سکه معروف به امامی نیز روز دوشنبه در کانال ۲۴۳ میلیون تومان قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpUDq0iQauSIkFG8DQ5jeTlsfvBiiG6wi4jkhKUFuEersAokqtzbsUku3itevJ5EZx7KDu_Wea_h0DgsPlK3J309xSBnwlBV72oVEbDFciiZXwBAdfuWHzGSZmAvUHpcMTbzshjbtbhGc692ws8Tnf3XtcPN03u8SWcnSdbtE9cEuwqvB-Wwa56fxcnMXg2lJXD-yRBo2hvv-FUCCxhw0NpK5bCXzXDuviRVIDHtCG_9Sna6TTbBFKXcLGNd6M7VTdd2MDKl7sNKDYVL-U_pMxbK_NgahfwcruPUMNXRPj3Nkf628NOzResodZ3sAG1f3h_DB4uD-FvxJbTFn-AUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=fQEMXBJe2ls6oeMtP8mkig-62dltfRGLovs2bTrZb4_8V8P_C5UprDpPTjdt963WnSjwy6RLLwXcFe2zkXlXCRZfg9rwFU8N76Wr3ZA32Nn5f8Vw-BYEi0SA3qH_WbRhHgQ_5s4k4f0UlCkNGHf0Z2eaolIR0j-70MqSER72kzMdORmCdIbS_8zyaFDx6JQZUxjuJZqWpegDwobXfUSj_AgD-2zVjhhFy2jovAUKqyZrKHMSwlwrwGUo1sishjcdse6SKd7eRMi6V4zp9AC_Mdc478NC7C47wPRgA3rrx1PCMf4ULLu1702eiMNmNoaMRD2WIUpHcK24lhR79egBhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=fQEMXBJe2ls6oeMtP8mkig-62dltfRGLovs2bTrZb4_8V8P_C5UprDpPTjdt963WnSjwy6RLLwXcFe2zkXlXCRZfg9rwFU8N76Wr3ZA32Nn5f8Vw-BYEi0SA3qH_WbRhHgQ_5s4k4f0UlCkNGHf0Z2eaolIR0j-70MqSER72kzMdORmCdIbS_8zyaFDx6JQZUxjuJZqWpegDwobXfUSj_AgD-2zVjhhFy2jovAUKqyZrKHMSwlwrwGUo1sishjcdse6SKd7eRMi6V4zp9AC_Mdc478NC7C47wPRgA3rrx1PCMf4ULLu1702eiMNmNoaMRD2WIUpHcK24lhR79egBhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"از او بگو به دنیا.. از او که قصه ای داشت
او جشنِ زندگی بود.. سروی که قد برافراشت
از اُجرتِ گلوله .. از شر که می‌هراسد
از مادری که او را از خال می‌شناسد
از او بگو به دنیا.. ای شاهدِ غروبان!
این رقصِ بی‌سران است، این داغِ پایکوبان..
یاد آر اگر رگت را با مرگ می‌خراشی
تو بازمانده‌ای تا او را گواه باشی!
دیدی که بر مزارش، رقصِ پدر کدام است؟
این هلهله عزا نیست.. آئینِ انتقام است
از او بگو به دنیا.. از نغمه‌ای که سر داد
از او که نیمه جان بود در کیسه‌های اجساد…
از او بگو به دنیاااا"
monaborzouei
Lyrics: Mona Borzouei
Music & Arrangement: Reza Sadeghi
Producer & Concept: Sia Davarnia
Executive Producers: Mahshid Hamedi Boromand & Farshid Rafe Rafahi
Director: Carlito Brigante
Video Producer & Director of Photography: Avid Eghbali
Ebihamedi
📱
youtube
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PlfZajUfAyQRzlfaQq94vXPBlb0oKgT3lVVqkLqxYNsigr4Ei23z9HgE6nh2EmjAb_U0ibA47c0ZAkQgugoagQ_FaUVPRN6JOxryhL5IwfT5i4afN8FgdBk4FLoNmk0jtOe3ZL3-NIS6OkJ0-Rtg0FJ_XI5qWZMAJDmk-nGFWWtDpyy7l1nZq38PWxWr_gO4mxpICypdssNhIf_6lye2jbI3Q3OZXQIskuaatFilWmv-yysI0j197VxrlWxubRyB2A-7vU0E8IYysa-pQDWmzECoeXGodqcWj-F9vhc-xhF0lxPBnXB0lB5mDLNlKBsa1CW_ft8_rXmZSk-ojJB7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز یکشنبه پنجم مهر ماه و یک روز پس از آنکه اعلام کرد پیشنهاد ایران برای پایان دادن به جنگ را رد کرده است، در گفتگویی تلفنی با آکسیوس گفت انتظار دارد مذاکره‌کنندگان آمریکایی این هفته مذاکرات بیشتری با ایران داشته باشند.
ترامپ گفت: «انتظار دارم این هفته مذاکرات بیشتری با ایران داشته باشیم. آنها می‌خواهند به توافق برسند، اما این توافقی نیست که من بخواهم به آن برسم. این همان چیزی است که شاید یک سال پیش با آن موافقت می‌کردیم. آنها بیش از حد روی مواضع خود پافشاری کردند.»
به گزارش آکسیوس دو منبع منطقه‌ای نیز اظهارات ترامپ درباره برگزاری مذاکرات بیشتر در این هفته را تایید کردند و گفتند انتظار دارند دور دیگری از گفتگوهای غیرمستقیم میان آمریکا و ایران از روز دوشنبه برگزار شود.
با این حال، آکسیوس گزارش داد مشخص نیست اختلافات میان دو طرف بر سر مسائل اصلی قابل حل باشد. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار تعهد ایران به امتیازهایی در پرونده هسته‌ای است.
@
VahidOOnLine
پیش‌‌تر:
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه پنجم مهر در حاشیه حضو در مسابقات گلف جام رؤسای جمهوری در شیکاگو، از رکوردشکنی انتقال نفت از تنگه هرمز خبر داد و تاکید کرد به محض «تسلیم ایران» و پایان جنگ، قیمت نفت به‌شدت کاهش خواهد یافت.
ترامپ با اعلام آنکه شنبه شب «مقدار بی‌سابقه‌ای» نفت از تنگه هرمز منتقل شده، افزود این میزان حتی از مقدار نفت منتقل‌شده پیش از آغاز جنگ نیز بیشتر بوده است. او همچنین گفت قیمت نفت اکنون از دوران دولت جو بایدن پایین‌تر است.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WncgEekVC8x3wRqeBfRF9stLhwfp8FCJPS1eDu9E1Rhd7LVytqX5SsJi6h44tup_as31P7PYJCi0sFgu73xHiCBVcoTB4OoYlngO-ONBQVAK69AfhQIsa6gii5KMvwDHGzXO14YGjbLl-RFOTWgKAeYK3INwno03aL0_7vJK1ZC7gkpFpS0yGQC1eiraN80oHD4YFcvbUICxmRfHFaIvFzLzA7ZAqBmoJo4e_-dwDg6OS6C681DKzHs5FDGulLmyM46gqK_qpl0ZmNHEucg0FfHetVArrm7A0nQdyBca_NcbDW-B3ngyuBU4CndV8t2elHENJUyveMobrw7dXCpjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O2GVYKwujh3twy5ttelgjXQZIj0EAdzmOxp5LnL0Hga-MljQKYpg6lsVBMQjpe_lbgLgqr2h3gK3Wiay5oVFY-JL3e5ckq0s86EbBwUD9VEopvBKkq167usYhhlo806Vucnu7-qtS6FUVoWKDQvfz4yMJHULQYctpE81DEoWQGuJpVdY1zjl5Z-_mpO7QSAwwOgGtYp4bw3V50HxvRLlSuq1dpcQwpJyJAC_SSaHgntQtZT42oo-QzLtJwnCBlWDpengq1RuJb8_bxKwVhRfGFldfU2OXHEKTiwLRumi4caiNts67Map95OJbPJe8un1aQ5KxmZxUnY2rYHsEZLGww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، می‌گوید با وجود اعلام علنی دونالد ترامپ درباره رد پیشنهاد هفت‌روزه تهران، هنوز پاسخ رسمی واشنگتن از طریق میانجی‌ها به جمهوری اسلامی منتقل نشده است.
او با اشاره به اظهارات متفاوت دونالد ترامپ در روزهای گذشته افزود: «متاسفانه از رییس‌جمهوری آمریکا حرف‌های ضدونقیض زیاد شنیده می‌شود.» عراقچی گفت تهران منتظر خواهد ماند تا واسطه‌ها «نظر قطعی» واشنگتن را اعلام کنند و سپس درباره گام‌های بعدی تصمیم خواهد گرفت.
@
VahidHeadline
عراقچی روز یکشنبه ۵مهر ۱۴۰۵، در گفت‌وگو با برنامه «میت دِ پرس» شبکه ان‌بی‌سی نیوز، در پاسخ به گزارشی درباره احتمال ازسرگیری حملات آمریکا پس از انتخابات میان‌دوره‌ای این کشور گفت: «ما کاملا برای ازسرگیری جنگ آماده‌ایم. در برابر هرگونه تجاوز جدید ایستادگی می‌کنیم، حتی اگر به جنگ آخرالزمانی منجر شود.»
او در عین حال افزود: «هم‌زمان آماده دیپلماسی هستیم. انتخاب با رییس‌جمهور ترامپ است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=WykgVFeaiQcFcFnSt8XgiGx204zBchrBzBxq-fL4p1pubxRYkdQxZ6MWkRP9IfCG160gKkvmYDrnv-nCgUGGspTKFTcI-pWkf40wC41WIK5WRc6S3VfOSyHa081yKQT9_UR4hYp9qdbi1bmulR4tpIZFY9YE31XkOjuSstN7jaIuE_KFAZ-MUmd4fIlhkCbNjv58T2MyffeNyQZnOH6tsNnDy3kbdX_8peZD-iur6f2r-hwUH_d-dWWaHAJFbfel2l2SHl5UoeKRvrHOC_arg4K1enm03YqWkAWj6Ff8dzSE_MOkdovrYhv-KHZ50fec6FkmtMvhXxKPRBKergS-kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=WykgVFeaiQcFcFnSt8XgiGx204zBchrBzBxq-fL4p1pubxRYkdQxZ6MWkRP9IfCG160gKkvmYDrnv-nCgUGGspTKFTcI-pWkf40wC41WIK5WRc6S3VfOSyHa081yKQT9_UR4hYp9qdbi1bmulR4tpIZFY9YE31XkOjuSstN7jaIuE_KFAZ-MUmd4fIlhkCbNjv58T2MyffeNyQZnOH6tsNnDy3kbdX_8peZD-iur6f2r-hwUH_d-dWWaHAJFbfel2l2SHl5UoeKRvrHOC_arg4K1enm03YqWkAWj6Ff8dzSE_MOkdovrYhv-KHZ50fec6FkmtMvhXxKPRBKergS-kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: دومین زیردریایی بدون‌سرنشین آمریکا را در تنگه هرمز به غنیمت گرفتیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی روز یکشنبه پنجم مهرماه با انتشار بیانیه‌ای مدعی شد که یک زیردریایی هدایت‌پذیر از راه دور بدون‌سرنشین (زهپاد) آمریکایی را در تنگه هرمز شناسایی و به غنیمت گرفته است.
در بیانیه سپاه آمده است که نیروهای نیروی دریایی این نهاد در یک «اقدام هماهنگ و پیچیده» و با استفاده از اشراف اطلاعاتی و جنگ الکترونیک، این وسیله زیرسطحی را که  «برای جاسوسی در تنگه هرمز» فعالیت می‌کرد، به دام انداخته‌اند.
سپاه این زیردریایی را REMUS 600 معرفی کرده و گفته است که آن را به غنیمت گرفته و اکنون در اختیار متخصصان نیروی دریایی سپاه قرار دارد تا اطلاعات آن بازیابی و بررسی شود.
رسانه‌های وابسته به جمهوری اسلامی نیز هم‌زمان ویدیویی از این وسیله زیرسطحی منتشر کرده‌اند و آن را به‌عنوان «دومین» زهپاد یا زیردریایی بدون‌سرنشین آمریکایی که در جریان درگیری‌های اخیر در تنگه هرمز به دست ایران افتاده است، معرفی کرده‌اند.
براساس گزارش رسانه‌های دولتی ایران، این زیردریایی یک وسیله نقلیه زیرسطحی خودران (UUV/AUV) است و برخلاف یک زیردریایی سرنشین‌دار، خدمه‌ای داخل آن حضور ندارند.
این خانواده از سامانه‌ها برای ماموریت‌هایی از جمله شناسایی و مقابله با مین‌های دریایی، نقشه‌برداری از بستر دریا، شناسایی و پایش زیرسطحی و جمع‌آوری اطلاعات دریایی استفاده می‌شود.
ادعای امروز سپاه در حالی مطرح می‌شود که پیش از این، در ۱۷ شهریورماه نیروی دریایی سپاه از توقیف یک وسیله زیرسطحی آمریکایی دیگر در نزدیکی ورودی تنگه هرمز خبر داده بود.
سنتکام در آن زمان اعلام کرد که آن زیردریایی به‌دلیل نقص فنی متوقف شده و «حاوی اطلاعات حساسی» نبوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e1TzCFThLjewhA_uckc3G1URIzGmgvbOGyXEE0ZUQFFz5vT0yj3thVwm8cfs09h9XW_BiSqi-sGo2c-Mrz55AAaz45H2cVRf9JKvJQkNmoBzL7qjgdVZlH_h0bYl6OuMs0xNN-ccNY42Mdf8cYoZD5QOumUao__gBl73rctCL0lqK_8I3WFaia3FHPsjHe4GvoJfUtWQ58FkK-Dawck4fNZ4ZMaG6pRlsEI_PRJGx0H81GzfeSB2zQktoN2IeqzZQejRB4IUn9GRROcrkn4aydF-7OHe5tjddoEePEXGusDgnRsRtQo2w9hG9cbG1Ui5SzY4G-UM4TorrlUbDx859A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hElI3sWFH8zBbDvLI9v6YVOlirgAgQfo15xMrB3srrZ_Xr1nw4dCvRMGofSziFZKm0dObqEFVVYw8-dOH0ziW67x1yl6N1Ry_ZBLnT1fNGnTD66OeZUuDPx2TnT0030dcONZfZ1dpr_6BqlTfOBucbodnN8xks5i6tpBvFlMaz211RSG_PhX-c_CDtO_09vgUEurRWhvt0CoIx6g2SL8a34GtetcXO5gut1elAAXCMI5U9xOcx4GvNAWpibzWoRMxGVfTQQMmA-gl5HmAmIJfmIO8d-I_Tl5w6OMiy_24Wi-LFjrJodR320xlL5OCmxOdPeuvHEqMQbn8XuBj-6gDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OQWvcQoySd3zOwMUGqiPCE-Yt3RPG20ratNETuz9foUM_UyeAkZl2g4j9hunf3XGNZ9tYxhxq2LMV8TboA8IkPpQTYMU_9TCiBg6Tn2S4jEXluJWvjzH9pQVlLUEyjUECun34Z2wBcNXf47ww-wtcClLolwkj6dcpUXc6NxUQl3d4LzHOZFJMTCaFrUKhj2Zsdwkjkl11txPTyr0NM8ukt0Z57FGPX2D60JcZvatMJjEKdSwPRzVTrmTGsBP2ohILP2-k9Ho625fvinF95xCAMufliYwI-U4oOsGAXaLYZt2RVFJb5Bkrs4YQuZneASMu4lnyR3sZIusZers7MOiCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمید رسایی در پرونده شکایت محمدباقر قالیباف به ۱۰ ماه حبس محکوم شد.
این نماینده مجلس شورای اسلامی گفته است که برای اجرای حکم خود را معرفی می‌کند.
دادگاه به استناد ماده ۶۹۸ قانون مجازات اسلامی، حمید رسایی را به «اعاده حیثیت و رفع اثر از ادعای نادرست از طریق انتشار تکذیبیه در صفحه اول نشریه ۹ دی» و ۱۰ ماه حبس تعزیری محکوم کرده است.
گفته شده است با توجه به اینکه این جرم قبل از دوره نمایندگی رخ داده، حمید رسایی مشمول مصونیت پارلمانی نیست و دادگاه او را برای اجرای احکام احضار کرده است.
@
VahidHeadline
عباس عبدی، روزنامه نگار و فعال سیاسی، به دلیل انتشار یادداشتی در روزنامه اعتماد به یک سال حبس تعزیری محکوم شد.
روزنامه اعتماد هم در این پرونده به دو ماه توقف فعالیت و انتشار محکوم شده است.
آقای عبدی در بخشی از این یادداشت که ۱۶ اردیبهشت ماه در روزنامه اعتماد چاپ شده بود نسبت به انتشار «اخبار جعلی» از سوی برخی از نمایندگان تندرو هشدار داده و گفته بود: «این افراد تحت نام نمایندگی هر چه بخواهند می‌گویند و کسی هم در مقام اصلاح آن‌ها برنمی‌آید.»
در پی انتشار این یادداشت، دادستانی تهران او و روزنامه اعتماد را به چند اتهام‌، از جمله «ایجاد دوقطبی کاذب و اختلاف میان اقشار جامعه» و «نشر اکاذیب و مطالب خلاف واقع» تحت پیگرد قرار داد.
@
VahidHeadline
صادق زیباکلام نیز در پی مصاحبه‌ای با خبرگزاری آنا به یک سال حبس تعزیری و از باب مجازات تکمیلی به منع هرگونه فعالیت رسانه‌ای، مصاحبه، یادداشت‌نویسی و انجام مصاحبه به مدت دو سال محکوم شده است.
@
VahidHeadline
حکم یک سال حبس در پرونده حشمت‌الله فلاحت‌پیشه نیز در دادگاه تجدیدنظر تأیید شده،‌ اما به مدت پنج سال به حال تعلیق درآمده است.
سیامک رحمانی، روزنامه‌نگار، نیز پس از تفهیم اتهام و صدور کیفرخواست با اتهام «فعالیت تبلیغی علیه نظام» به پرداخت جزای نقدی درجه شش به میزان ۸۰ میلیون تومان محکوم شده که این رأی قابل تجدیدنظر خواهی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAq4hmU4Gm2yE3qS1uvbADiRtQ8JQQXBXF0Osp21F0yD-z5DIWXfTnN7S79So_jDiVP1qc3Fl4J6tT2_-F0qmyws9er_PypPK3nEZerZzUiiocL9CuL9Y3ZDGx8M_m1N9XGr7YOpyPxmpdzmazpktEx4m4p2ZABZmt7EmJHPRzHwX-nzRYSen8SnXrDjzBvzZ0TSLWMhRKYpdEnJQBZNS8n5rPWQftPOdYtWtNOKUMDHwyMiiLHH9MKqIS7PEtVQpVvazvulzvrugxVLIWtaunUDtJMAxGAo4m4aS63ZJE9bJxFNhgaAFbt28bE20jEZl0JyGdtdgZ6kf6IFCweEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVkXCsIvSJyOV9ttzkv4_hccxiYQa2KNp70BHvw-0Yod1k69WuWEUd-zIsgdT4XPxRvn6dXlVfTy_q_G_5VBxAA4MCx-PwO5znDO7U6er_kOgP_lmA0D90v2ZgHGmXsEs74DaUAdQv8UJJ8rHCqqhcXPm70VkivSAoWucSpVj6FAPf0Y9yIfMmHtkaVrdCk6DvfURj7SorkWSjaY1lqEC43O0a1W1zo8o2CLr9V4JofSQH3N3HS7_lh5OLRlfzKakzk2zg25h2PSct1seMAjAI6zZUCHmR2V6_R4jV-NntWhjwhBYqSHvLkeNJzeHPqXoPkndJrh-3wDqY0rsiDTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت آکسیوس، روز ۴ مهر ۱۴۰۵، به نقل از یک منبع آگاه گزارش داد مذاکره‌کنندگان آمریکایی در جریان مذاکرات غیرمستقیم با عباس عراقچی، وزیر خارجه جمهوری اسلامی، به او اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند برای بازگشایی این آبراه شرط تعیین کند.
عراقچی در این مذاکرات شروط تهران برای بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای را به طرف آمریکایی ارایه کرده بود.
بر اساس پیشنهاد جمهوری اسلامی، تهران حاضر بود تنگه هرمز را بازگشایی و مذاکرات هسته‌ای را ظرف یک هفته از سر بگیرد، به شرط آنکه آمریکا محاصره دریایی بنادر ایران را لغو، تحریم‌های فروش نفت را رفع و آتش‌بس در سراسر منطقه را دوباره برقرار کند.
بر اساس گزارش آکسیوس، مذاکره‌کنندگان آمریکایی روز سه‌شنبه در جریان این گفت‌وگوها به طرف ایرانی اعلام کردند که جمهوری اسلامی کنترل تنگه هرمز را در اختیار ندارد و در نتیجه نمی‌تواند درباره بازگشایی آن شرط تعیین کند.
در حال حاضر ده‌ها نفتکش روزانه تحت حفاظت آمریکا از تنگه هرمز عبور می‌کنند و میلیون‌ها بشکه نفت را به بازارهای جهانی منتقل می‌کنند. با این حال، حجم انتقال نفت همچنان به‌مراتب کمتر از سطح پیش از جنگ است.
مسوولان آمریکایی می‌گویند طی ۷۲ ساعت گذشته حدود ۶۰ میلیون بشکه نفت از طریق تنگه هرمز منتقل شده است.
در همین حال، قطر و دیگر میانجی‌های منطقه‌ای برای ازسرگیری مذاکرات میان تهران و واشینگتن تلاش می‌کنند، اما اختلاف دو طرف بر سر موضوعات اصلی همچنان گسترده است.
جمهوری اسلامی خواهان تمرکز مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا است، در حالی که دولت ترامپ بر دریافت امتیازهای هسته‌ای از تهران تاکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=NyUJMU1TrIKRaT28cc8adMNocBrcjEbGB1VArpNetqRUl2LmgDbfdiV6i2D9O_cf0aL2CtUjsX8R38bg86srZIoidugoGYbiV6tIdlYCc2LQD_hBglRb4TX4gmNjNWDnT7GoeSztUshW361X3F-V7RHZeVo3VGziLNYejYq2xA2Uwk58tT2a_buEjnLZbxYxx4pb2P1ladxFRNYfZ4h3-tYXHu3OMZSeVN2RuKmiU9FwihCZV9VrHeKPwh3Zb8z1pG2rEcCfMQTgcSL1FhRObczQ9ngasKn1Hje9Z5PVQHq1M3Ls5Nxn9LNX3lm0dF_A22H6IZSFxmpE5_IABpOMgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=NyUJMU1TrIKRaT28cc8adMNocBrcjEbGB1VArpNetqRUl2LmgDbfdiV6i2D9O_cf0aL2CtUjsX8R38bg86srZIoidugoGYbiV6tIdlYCc2LQD_hBglRb4TX4gmNjNWDnT7GoeSztUshW361X3F-V7RHZeVo3VGziLNYejYq2xA2Uwk58tT2a_buEjnLZbxYxx4pb2P1ladxFRNYfZ4h3-tYXHu3OMZSeVN2RuKmiU9FwihCZV9VrHeKPwh3Zb8z1pG2rEcCfMQTgcSL1FhRObczQ9ngasKn1Hje9Z5PVQHq1M3Ls5Nxn9LNX3lm0dF_A22H6IZSFxmpE5_IABpOMgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه چهارم مهر تأیید کرد که پیشنهاد جمهوری اسلامی ایران برای بازگشایی فوری تنگه هرمز را رد کرده است.
ترامپ پیش از ترک کاخ سفید در گفت‌وگو با خبرنگاران گفت: «من پیشنهاد آنها را رد کرده‌ام. آنها می‌خواهند توافقی انجام دهند که بر اساس آن تنگه را فوراً باز کنند، چون به‌شدت در حال شکست خوردن هستند.»
او افزود: «ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم و مقادیر عظیمی نفت از تنگه هرمز خارج می‌شود. دیشب ۲۹ کشتی از تنگه عبور کردند. آنها می‌خواهند توافق کنند و من هم با توافق مشکلی ندارم، اما آن توافق قابل قبول نخواهد بود.»
@
VahidHeadline
او بار دیگر گفت جمهوری اسلامی خواستار بازگشایی فوری تنگه هرمز است و افزود: «آنها هیچ پولی به دستشان نمی‌رسد، چون پولشان را از تنگه هرمز به دست می‌آورند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R15BXSKu56jJHxTHLoRkyXUinUFPOJlNju1-CY2dmWvpbMSCLDtbFL8FuqFoLBmn9ZKhANjI1M0YOzJHiSrAd6p_bafdzSKsT77E63pJfrGqIvAm97InkVuRtDCnkuJNvnvAWSJnhKuTRaVcI4vD3JPn0y0FGwA2F7AVgxCbG2W5QW8QrEzOs4ur9GuKUQmiy--bT8PnfvKN_hKYwHfR46d0ft88NZD8Skym-i4IDQemHSONbLGLHnecLIGjp87UOajL5wr3FTPsO8FySqetY5dpsxDaEWI5ZOmC_HKpnWUH_5NZxTd45IdF8Tjx6CFEhzcbLXVHB-C-jjnLG9IVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=vgubFFL2iRtjANlauYZXD_ruqWJ4tNxSCnjtxiZ-mPF3DHROd1VjCMqBqra-eLaw3k8YB6BrIxq9cPPl4V78EcHtdgaIuwGn_ZVMc2otwXsKl8aHBnAwXhaDvoAhfXNzZ7J4Dc3PmxgBa1nxVNrJ9ty9hfqwVe1bafixBY4cs4eVVCy7xEmihwOCFkVg4QJHDnS9lWP9RvvKfFGA-RdrdqK6LcpOEk3FxOQxZHiasswMfYQgAzVccjf383dtoVLJ2sgXQK_5UxJsD7udCnJ8uY1-B05ESfquPI5MR5SLBo79DualhnXPMF-lbz7EnNVAQ_e-Q-yarTjzTtEZz_LiKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=vgubFFL2iRtjANlauYZXD_ruqWJ4tNxSCnjtxiZ-mPF3DHROd1VjCMqBqra-eLaw3k8YB6BrIxq9cPPl4V78EcHtdgaIuwGn_ZVMc2otwXsKl8aHBnAwXhaDvoAhfXNzZ7J4Dc3PmxgBa1nxVNrJ9ty9hfqwVe1bafixBY4cs4eVVCy7xEmihwOCFkVg4QJHDnS9lWP9RvvKfFGA-RdrdqK6LcpOEk3FxOQxZHiasswMfYQgAzVccjf383dtoVLJ2sgXQK_5UxJsD7udCnJ8uY1-B05ESfquPI5MR5SLBo79DualhnXPMF-lbz7EnNVAQ_e-Q-yarTjzTtEZz_LiKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkznyCTyI0lPkCd0azkYa7h-UETDBrKuicH68FZrxB9HOyxVTlF7DR4OzPtUzpYFPiCa8KOWRpleqlTm3wzSn8Q-o7EA--V5SYx2inX7f4SsYBlMZN1HEnZiB-S81yUFJJCp6YENfHnM844Zy3svU_lGm6k8c0as3yaH4c5IxqYy8eOrXXQL4gw1Az_HVECgWbztbBxb54jO5I3MZM0QauicWc6RmZzyys9GWsFMdW-Gxkt8j99nqB9tWJ3AyTxvLfU-lxZwc3SzdSwJJU_sHwiYVYYVaXjx97o46_ta63VpdU3HDjVnJhq57KMYbPDLQXAJdpGFN9sD4gQh8MnsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdkdWFsQDZ-bCs0TTv__7nmK79r2E7u23J5ZApo70NaOKxwaOxmP3clR15wneCppiE180xnWafXRASRi2bOJMgwHwPhOzKMSoMovmxRll0bRn2EqpTDkjFYkukrqNjxWn-_pxWX4E5C8C5cRZxHL9pHXtMJp0iqJg-4xRTusJVsytT_vkAnw7IWPpn16Msx4ScC038T5DKER9AHOw-s0G4Ke9yvd6StXtEfp5GwZif7BZA8aXcfuYlntvpIP3w2XmbEGPZXs9BNZvgN_98cQP8r1KqQcZPOLAZaF49GOpsmztHK6wuPS8e56FtxEHTGLsGdRnXehJxe_UF-uq5CTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d7s9Gpq6ELlafB1pNa1OmwhdU9TM07FVMelGH8K8Rqrb7I3ppLDkKi6LFUHpPvecOMadmpEr-if6wQwU8qecIXQi6dLFeKOvasAnnaVgSgjClsCpfa-ZcwIobejUydsplb4x8saVTSycTyjPBVCPWdue2-d_-L04WP6jdoMCCpmDBelziFjjEnvW3vHSQPZzcmFzF7TChjWMr5M4AAB1VQOfmwCAojUv4diFPSVI752SUHHn_kk45f1WBDPN1EHKz4wqKqnKhGa74j5-cQ3xjXYDNc9kS_DA-DMJX2Gtrw-gZ6wh9_ECEDrSkE-eG_n0ZHwpeHiTbdahod9qcGxd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=dBB32Q57y_s-rkz0ABNRZzBgp1zmujFqwxQzHagElUhLuiXtMK5Arz6C-IM8MWtSJi0m80ZwTgYaHHCjjLt-5CTnmBcQfOOWBnrMmBtzo4YoOM7tFczh-K0hRLhf7Z7AEbaQHd_DHsNWY4XE0uPm0n1uqba2myIwaKUNsXkHJSjn1q4SsijGo1N8-gDparvn6c492KsC8dHDqO3q20yDuGxEUAmNtM6B0jooAM794HdFdbhHRTGmmOOLnd-LLrFx4F4VhtSKxw_Wa1dO7yYmSn3N9Fh-CqBV9phZM6lF6tw54IYgMtb89vFBfmaOqeNLXA2Di_CMH3IAy62ux7Dkjg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=dBB32Q57y_s-rkz0ABNRZzBgp1zmujFqwxQzHagElUhLuiXtMK5Arz6C-IM8MWtSJi0m80ZwTgYaHHCjjLt-5CTnmBcQfOOWBnrMmBtzo4YoOM7tFczh-K0hRLhf7Z7AEbaQHd_DHsNWY4XE0uPm0n1uqba2myIwaKUNsXkHJSjn1q4SsijGo1N8-gDparvn6c492KsC8dHDqO3q20yDuGxEUAmNtM6B0jooAM794HdFdbhHRTGmmOOLnd-LLrFx4F4VhtSKxw_Wa1dO7yYmSn3N9Fh-CqBV9phZM6lF6tw54IYgMtb89vFBfmaOqeNLXA2Di_CMH3IAy62ux7Dkjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در  دو واقعه جداگانه دست‌کم ۲۰ نفر کشته شدند:
یک دستگاه اتوبوس مسافربری بامداد شنبه ۴ مهرماه در آزادراه همدان ـ ساوه واژگون شد و بر اساس گزارش مقام‌های امدادی، ۱۱ نفر از سرنشینان جان باختند و ۲۴ نفر دیگر مصدوم شدند.
@
VahidOOnLine
برخورد یک اتوبوس مسافربری با تریلی حامل میلگرد در محور بیرجند ـ قاین در استان خراسان جنوبی ۹ کشته و پنج مصدوم بر جا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhhU_G3eLQ_qHDxETSWUm3czPmw3sGop-PDgZlxyuQ5iimaR2sD7F51Ci9q5g6BXw-zqkomwEIXD6EvVwjJO1uUIfLPtcPz1fzFCsyGKZeR32KOFE81D8WQztHTqf8ywxPk16bq6fa_e5nnp3rz77e64wAEz437b5-zdhYGeJk8c96DRl_PcIarKwJ116AgzqAMy3C9Gb9pLvQAJqx-utMxaA8QlsDMpngfhWL108jBE0GdI0A6DAjg7d-KCGRt6DJ6AvwQnjYBHSEoirFaL8M39s_d5KPfIiNxpl9z9RD61mQebpWednRUFxYctLTdXU-LtmtZZK506fXPGMTy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه تجدیدنظر استان قم حکم ۷۴ ضربه شلاق پرستو احمدی و هشت نفر دیگر از نوازندگان و عوامل «کنسرت کاروانسرا» را بدون تغییر تأیید کرد.
ابوذر زمان، وکیل دادگستری، روز جمعه در شبکه اجتماعی ایکس نوشت بر اساس رأی شعبه ۱۶ دادگاه تجدیدنظر قم، پرستو احمدی، چهار نوازنده و چهار نفر دیگر علاوه بر ۷۴ ضربه شلاق به دو سال ممنوعیت از فعالیت در امور سمعی و بصری و ممنوعیت از خروج از کشور محکوم شده‌اند.
دادگاه کیفری استان قم پیشتر این ۹ نفر را به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» محکوم کرده بود.
پرستو احمدی در آذر ۱۴۰۳ ویدیوی «کنسرت کاروانسرا» را که بدون حجاب اجباری و با همراهی احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا اجرا شده بود، در یوتیوب منتشر کرد.
قوه قضائیه پس از انتشار این اجرا علیه عوامل آن اعلام جرم کرد و احمدی و دو نوازنده همراه او نیز برای مدتی بازداشت شدند.
در رأی بدوی، دادگاه پوشش پرستو احمدی و همچنین تولید، تصویربرداری و انتشار عمومی این اجرا در فضای مجازی را از مبانی صدور حکم عنوان کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E17qbthkDxXubTHgeECAXom1qtSYWtocFreB4D9urfoJdQ_cVgiIkM5m54vAuUV5h3KZTJwulNQDaPj2F8TENDmf8wv8pr_RriOsGW9dABP22-lLxqCKMQtXs8HYFNBnwglJyjORDh4HlklHIYJeZxGxvy2ySEqLS314Kw5qQvQ9Jge5vEIDM7SOxKLjB009QJtE7xTrGUwFYuweJVgr-_SwiBfBRiuNN-4xmDcRPE-T8EFGcXrltcvCeaBcGoXwj4Fe_ffxbQov1b1E0t5od17NZWh_3q2-IDKb1ABEcDc5kkJWTayIAEye82uIOt3ePmRexCMVbS5XB5kMASgrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc1s3rdSFzns79nHA2q9n5uvWg1fdQQiZQ782baOdjKrcEYH0CWVs_DGB2aF8t9vAbdJf41iGHIT0CPE4EOb7WqPu8RvRWTVCUqfWjlNlySNGM2IcrCZehJ7Ravw9hvPlACQEt0DFZ34k9Ie-gu9QzqIJNQp79mNeqNHRGx5sHkjI4dDEYiPksEGSVH7ikpaSyA_QdJtAbfGSFwFQzk_3K7x1IVdujEYwDO0KF_cBhHtrRd0jPo2iS10LCT38TXL1pU5jYloOBPa7ZNE_mAYX3cBYiGu907AKRENhmoqRO4mpEQh4JeyZOafWAszxQa1TygOwRMutnd3MlSuk4FNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ew7xBq4cD40lcz6m5LJ7cq4cVIPMt4c0r6vPphoGTAyedkfD0eZAUD_Zb3O3pMeey9PevDSkIi-iIAMvsnYldIJIY8KaS3TtRIicZmV8uFeQjceBfd0FZ8TsQfrWxZiRPmiGVCRDbt15gVDoO6dhDUES3LxjrVdYplZQDF9s-heCeQkBILJOvO_JUy1BSQqJVDqDNh2l61BfYYf4galaBqBa5NBwgsgtvWAnBO3xyA2TqPSDuN0RCK1DAJRqyeB0OrtlbmFjWXjovDPCQyuLn8NNVUF8IfGswR3YMnslr79xDPwgS720VRN1Js_eOozI7Su0BpJT6NbyqhQTti_Sxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCr5HVal7mq2aZzz422f84sgVrZEMbSxr3wxdw6eIBCkoNmz8R4dLmA3OjM5hNh9btBKKU4nObRmTvg0KDU9QWvERNTWY-o69EZg54sXiaoEHZIxmqPv-BWZwttU7UYzMSNMYBAY5LpN2InkML9Mw0M-dn5q7kkksnTeT3yn2IO3Vc5s-XWtfeKpBE-XTSJCdjcQgO6zxRyg756nsFS2to1Ebz33uiJ8XTu3lvbPGi4iFj_ow1Zccc2iOAsJafvAU5aR88zfpIytn2nvhnNUFg98fdSTttVdBPmiPC9xYOFLC1nIroh_vF9MVEKHoPebPJr3h4zCedAvLib2FA1ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc1NYFQqbh220aRCW8ANHGnduhcgLiXIx3JCd_A5USzXJyOUUjDPj5Kbn6B9cyxHjZyV8OOaIe3e6TnDBEXVj9lI2cGmgEtEPfZLgfRuGxIX5egfJDRs6JnPr6Xk0srOxAldY_myc1e2zuUa42uZ8aeFQVX_G5FK0E3FgVnOFwYPcUVRRMQqcv4HBqa08uWGgqi1grcSbBDnX8QFs8u6rRrsAjcHIzIQtI_R0XWJxuqyOol0uOPv0PbU_pbtjubMeewPGnLvr_RPo5WwxcXdUeoxKO_WVqcLlZ52R2VsgHsCk4hmYHRYFczMYaZpYsMfU7p8DSoQMkK4oWhwNthEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axh39XBhUbfmtL_VW1resF1W0heuPekM0NlxcGr1vyTayfMqc1ysQrCqypw6sEnvSBZWz8BA1xGBKUI7AOod35k1FrtGKbJrF7KqaKglEwBiNQzVW75ikscXliGIMdBjHMCnp2uBVq1ikVUDk2V9TUgZtU7CuRqa7fsuluL4lvfwOv1Yf-NrUvNJ55S13G3rfur5uOb6U0mRNb2TxHiQpZDLKzfp9iIdMkMbun2F_xj7dGLbwYUZr0-eg73BRQW692_Gmz4rykXp1fQMWdaHhy1HzFhsF6MuiS5B-YZ00Le8U41tqt0jTTSQuCASu449oR4TLFzII2NpBKF5r0qpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyATVFVVKNZXl_a5-T9o7DftvxYB14bN6XS4MEdoVvPNRXpFF6VUHYPR6YgGO1eDvs9KnnHqrKs8UVoPhn5DmQ66C2X-dx7G3eqcpKpOXAuW9qcPqXXXdvQQKqRvwewsBC396TzpFQYR47qtFd0MtPufV3gGdIjLCjOu-aAgQ5Rg7n4KFmkJHuuV5kO-weNMiiylqkH62EbGNVs3Y__Favl19WWIts4I58l8NXWThkgS1adTloPKEE3UJ6zgbe1-QCXQHnET0IUc0KwzEbGMsmKhVqSJtpWwoIWm5LcbjVS-xpTVA4E2oCDo7etdzAfHfgWyWhJsOYVQXGg70jaZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQDcBVkP7afH_qO0m-eOrNwfLZXN_Y4fTQ_-8-0sNnslS_hLtkAVeuSM3f_LmP0YBjYTv15vRan2L0UUtc1J5OfrDF5bbcPspTCwLXsiyiRHz2kF81up1BzpxlECJcFCriv704l6g2pIurchhHG0qjp6hM4BcgDAjQUfd6ojELomldzlg6eH1UNUAWjm1r1TGsVMrs_Q5WgJtW502EfWxnHG_KdMS_v7NSFmcRYPRj8E-e9-wsnYcNUQ0sgaUc-uYrjbKebNZ6ZkRxcoiTeUG-dvhmTF6PZuYbfdB3zeGspc8NsPTdZWuv-E8yaRN-Mzk4a0bGSkrycyCzY-gXK4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMpAcaAhlj5intkCho55WJ0Gxte0Cf6dc6QA3cC9ZmkCmXF9CrgQC3-ApctFGr5jqMlcoJJvO0CTfHn9xgvBJfGYCWqFusImk2U1PQKSgM5iBJkECkB6IN0kZaftuQcHgrPGrNHJNc4T1IBHBJPp7cMgM-bb8fHrMghFTPLdeSHXHWXlJwhARx-3G6jwZ7O34be790f0qxdrkeTK2UCSVDvKy8TOc_cn2esw6i_wyITGWidEsZ2RQ0VtEEq-lUO2SYsIitYXRtZjYuHSmJErezR7Lc9nT9kGSXxsg1tJfKbdEELoYHQMkQatr4AQtSCfof8fyKA2atYsl8KAoVi5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=BjQ0jXYUAVcYlL19jiZI72q54QWpTx0sj9n6e3F9B-qhJn7C4-9r1WSXR3Kq-mUQhfMZH60YpKj8WfOZMd4Hproes9UGFVm347b7TBC9nvUVOHpa7fk8_iYDZXK-i41vReT62jSaBDA5iL7tGkFKPDDCQCJyPFnUwnAEkweFvBErtvF0P9wPLUElAYIGbi-oN98es_6lYOuwO8X7UTzVgs-4ih_QE1gM3Tnz5CkXOidzxRFAhy_aQXFZF6bszAELsCbqN2AXUngk-Cnq19gC0gs7z945v-TSINJnjFX3985bgdrp19_qBHvHMxrza9qrEnXMLVelsc78ULLG0V6SoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=BjQ0jXYUAVcYlL19jiZI72q54QWpTx0sj9n6e3F9B-qhJn7C4-9r1WSXR3Kq-mUQhfMZH60YpKj8WfOZMd4Hproes9UGFVm347b7TBC9nvUVOHpa7fk8_iYDZXK-i41vReT62jSaBDA5iL7tGkFKPDDCQCJyPFnUwnAEkweFvBErtvF0P9wPLUElAYIGbi-oN98es_6lYOuwO8X7UTzVgs-4ih_QE1gM3Tnz5CkXOidzxRFAhy_aQXFZF6bszAELsCbqN2AXUngk-Cnq19gC0gs7z945v-TSINJnjFX3985bgdrp19_qBHvHMxrza9qrEnXMLVelsc78ULLG0V6SoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPuQ6mCdbYeV2HGSUWLHgH4CfE61FWLmSD0tPJXXLMcoum9biJyhZOnXv-9ZhYWtuGcApJHOOPJ0scuSxiIzWy6n9e-lcdoH89nWpPy6oTCA1ozQFMvbTYHXXU-M-_lLLNq1kvHRx6-wtXtR9zrwOnvYPgdWV34CwJYSBPnMJpkBkQyNSBSePltTuFa1usN5fcefGI7FFE2f6YF3e7h7WsNvN2tK4EjrZyNj1pEVEIKygJynFiinYqxdS1YBxddJ8iHzM6--IBDjrwJMGTElZkgVguHyGkxLDaDLPsiYu5jkck-ZYQZFHg2OaAIUqCe3ffj-cMmFCVhv2qKWwSj1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مسعود پزشکیان در مصاحبه با فاکس‌نیوز، از آمادگی جمهوری اسلامی برای توافق و کاهش غلظت اورانیوم غنی‌شده خبر داد، اما درباره محل نگهداری ذخایر هسته‌ای و تضمین تبعیت سپاه از توافق، پاسخ روشنی نداد.
مجری این شبکه همچنین با اشاره به کشته‌شدن معترضان و حملات نظامی برخلاف وعده‌های رییس‌ دولت جمهوری اسلامی، پرسید: «چه کسی در ایران حکومت را در کنترل دارد؟»
پزشکیان در این گفت‌وگو تاکید کرد جمهوری اسلامی خواهان جنگ نیست و مدعی شد جنگ به ایران تحمیل شده است. او گفت تهران آماده دستیابی به توافقی در چارچوب حقوق بین‌الملل است، اما فشار برای وادار کردن جمهوری اسلامی به تسلیم را نخواهد پذیرفت.
او با اشاره به توافق و تفاهم‌نامه‌ای که به گفته‌اش پیش‌تر با طرف آمریکایی امضا شده بود، از تمایل به ادامه همان مسیر سخن گفت و آمریکا و اسرائیل را مسئول حملات و کشته‌شدن رهبر پیشین جمهوری اسلامی، فرماندهان، دانشمندان و مقام‌های دولتی دانست.
بخش مهمی از مصاحبه به میزان اختیار پزشکیان بر نیروهای نظامی اختصاص یافت. مجری با کنار هم گذاشتن وعده خودداری از اعمال زور علیه معترضان، عذرخواهی از کشورهای همسایه بابت حملات و اقدام فرماندهان علیه کشتی‌ها بدون اطلاع «رییس‌جمهوری»، پرسید چرا تعهدهای او چند بار نقض شده است.
پزشکیان ابتدا به آمار کشته‌شدگان اعتراضات پرداخت. هنگامی که مجری دوباره پرسید چه کسی تضمین می‌کند سپاه از توافقی که او امضا می‌کند پیروی کند، گفت قرار بوده گروه‌هایی برای هماهنگی، رفع سوءتفاهم و ایجاد کانال ارتباطی تشکیل شوند، اما فرصت راه‌اندازی آن‌ها فراهم نشده است. او همچنین نیروهای آمریکایی را به شلیک خودسرانه در منطقه متهم کرد.
مجری در ادامه پرسید: «چرا رییس‌جمهوری ترامپ باید با شما مذاکره کند و نه با فرمانده سپاه، ژنرال وحیدی؟» پزشکیان در پاسخ، از بی‌اعتمادی عمیق میان تهران و واشینگتن و خروج ترامپ از برجام سخن گفت، اما توضیح مشخصی درباره حدود اختیار خود در برابر فرمانده سپاه ارائه نکرد.
مجری با اشاره به آمار نهادهای حقوق بشری و گزارش مجله تایم، پزشکیان را به چالش کشید و پرسید: «شما جراح قلب هستید. چند نفر از ایرانیان در ایران توسط نیروهای امنیتی کشته شدند؟»
پزشکیان بار دیگر آمار رسمی منتشر شده توسط حکومت را تنها آمار واقعی اعلام کرد. او گزارش‌های خارج از کشور را مغایر اطلاعات حکومت دانست و خواستار ارائه مدارک هویتی قربانیان شد. در عین حال، از ضعف مدیریت رویدادها ابراز تاسف کرد و گفت استفاده از سلاح در تظاهرات خیابانی پذیرفتنی نیست.
ادامه گزارش :
pezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ویدیوی کامل با ترجمه ماشین
بخش‌هایی در خبرها:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «می‌خواهم با دقت به سخنانم گوش کنید. روزی، و شاید آن روز چندان دور نباشد، مردم ایران آزاد خواهند شد.»
او افزود: «حکومت آدم‌کش آنها به‌دلیل دروغ‌هایش، فسادش و بی‌رحمی‌اش سرنگون خواهد شد. این حکومت شرور سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو در بخش پایانی سخنرانی خود در مجمع عمومی سازمان ملل متحد، بار دیگر به خروج نمایندگان کشورها از سالن و حضور معترضان در مقابل ساختمان سازمان ملل واکنش نشان داد. او با یادآوری سرکوب اعتراضات در ایران، خطاب به این افراد گفت: «زمانی که رژیم ایران هزاران نفر از مردم خودش را کشت، شما کجا بودید؟ شما درباره مردم ایران هیچ چیزی نگفتید.»
نتانیاهو در ادامه تاکید کرد: «اما باوجود سکوت و ریاکاری شما، نیروی مردم ایران چیره خواهد شد. فقط مساله زمان است. یک روزی که شاید خیلی دیر نباشد، مردم ایران آزاد و پیروز خواهند شد و این رژیم پلید سرنگون خواهد شد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «مستبدان تهران؛ می‌دانید از چه چیزی بیشتر از همه می‌ترسند؟ از مردم خودشان؛ مردم شجاع ایران که برای مدتی طولانی، فداکاری‌های بسیاری کرده‌اند.»
نتانیاهو افزود: «از معترضان بیرون و نمایندگان ریاکاری که این سالن را ترک کردند می‌پرسم: کجا بودید وقتی مستبدان ایران ده‌ها هزار غیرنظامی بی‌سلاح ایرانی را کشتند و مجروح کردند؟ وقتی هزاران نفر از مردم خودشان را کشتند و مجروح کردند، کجا بودید؟
آیا تجمع‌های گسترده برگزار کردید؟ اعتصاب غذا کردید؟ آیا مقابل نمایندگی ایران در سازمان ملل اعتراض کردید؟ آیا در دفاع از مسیحیانی که در ایران و سراسر خاورمیانه تحت آزار قرار دارند، سخنی گفتید؟ نه. چنین کاری نکردید، زیرا شما معترضان قلابی حقوق بشر هستید.»
@
VahidOOnLine
ده‌ها نماینده حاضر در مجمع عمومی سازمان ملل متحد روز پنج‌شنبه ۲۴ سپتامبر، همزمان با آغاز سخنرانی بنیامین نتانیاهو، نخست‌وزیر اسرائیل، سالن را ترک کردند.
نتانیاهو در واکنش، نمایندگانی را که سالن را ترک کردند «بزدلان بی‌اخلاق» خواند و از دیگر افرادی که قصد خروج داشتند خواست پیش از آغاز سخنرانی او سالن را ترک کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «قطر میزبان عاملان کشتار هفتم اکتبر حماس است. اکنون تازه‌ترین کشوری که به عامل گسترش گسترده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است.»
او افزود: «اردوغان یک مستبد است. او نیز میزبان رهبران تروریستی حماس است. او هزاران غیرنظامی کرد را کشته، نسل‌کشی ارامنه را انکار می‌کند و روزنامه‌نگاران و رهبران مخالف را زندانی می‌کند. در واقع، فکر می‌کنم در این زمینه رکورددار جهان است و البته رقابت سختی هم وجود دارد. اما فکر می‌کنم او نفر اول است.»
نتانیاهو گفت: «او به‌طور غیرقانونی قبرس شمالی، بخشی از کشوری عضو اتحادیه اروپا، را اشغال کرده و به‌طور مرتب علیه یونان، عضو ناتو، دست به اقدام می‌زند. اکنون می‌خواهد سوریه را تصرف کند.»
او افزود: «البته این تعجب‌آور نیست، زیرا تقریبا هر روز خواستار نابودی اسرائیل می‌شود. او می‌گوید قرار است حاکم اورشلیم شود. نه آقا، نخواهید شد. این کشور ما، شهر ما و پایتخت ابدی ما است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
