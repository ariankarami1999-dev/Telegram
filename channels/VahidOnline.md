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
<img src="https://cdn1.telesco.pe/file/TC2_Jin1ew75BxQZCiH8NQ6dyQ7Ymes-tNdHPCFytEtPmP0dgafpe2UZN2_aRP6_lzPcSxqfUcBdLXMd40yhDRveHlVTcHFGblGcLf3H-iMWVseE_OWlzUEe9hJ6fLuUamQ0gG7u8nOwrgxioTujWQfLryTzgv0gXol0maxAfehieaa6r6EF3s8WHR7hQEmjlD1RdCXKvGpkXOvS4GjHM7vM2sk3g4IdkUbo2YBMHBBArO_12b1yNi7hV-3qJ1ZEYdRGOf9_3CjSwIBatK143j-pIn9NWpvipVTeuvwMpZXOy-br3VzLdDGedQXVBwRAUg_y86HkNi7fzWR56qB3ng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 04:16:56</div>
<hr>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=B2UmCtT9gnAwSF2HqGr4L_429bGN3YyuN4k8R7GTTDTBZEvmrxQbKjlc6vvVvo-eAuxVtWIkVIquecVM8xnsR2trpWEJ8Ftbiseb2yP-pd6X2mRj-f81btiaSyUYgGNLScU_LqdWw6iDm9L9IhLDJ9xucf_ytdFN4YgeNd9nnxewvuOCE_6Otl7QtVtrZ8o_HbyyBYu0tEn7Duo4SOad7Q7R2OmJKV4eqjWFNXeGmbe3n6ZjUAWzz8x4MtzRgUZkSZvkL1701gW2Ozutr8-mwUa06vCV9iIjIqWBz45tzNqLXEzH8zA8LlzCksX8DS2VtVPt6g2OkitJQF_EBizlvho9iuTAVcil4NorfElCTjnVHSnNzRIL38QOwfdMS2HxEI6iq5F7TJlohiBnAHYGdhtYiquPiMm6CtartE_ueWGUOfzI8OvpQCJNJdsFOfnneM15dN6arYmc9iilzZ4A2R-gKTvnfVlaRxJjIRS9n0EyMU1CdBU5VwsRxqPW2Gqx76-OspsAXfngoIvza4rnzzIOLm6NvJeqYNPEVCJwGYH9QL7h1LdMdMGEYCu59QtQCcFIEBydhR7AcLYDn1nNjkn_NIIwdIZ6XrlVdfL3pH-8kzCAmyfy54GHHqvios3C4ukep2JkYiCsCAYMvtJjpThuKBmgtuzCZf5p5XRzrbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=B2UmCtT9gnAwSF2HqGr4L_429bGN3YyuN4k8R7GTTDTBZEvmrxQbKjlc6vvVvo-eAuxVtWIkVIquecVM8xnsR2trpWEJ8Ftbiseb2yP-pd6X2mRj-f81btiaSyUYgGNLScU_LqdWw6iDm9L9IhLDJ9xucf_ytdFN4YgeNd9nnxewvuOCE_6Otl7QtVtrZ8o_HbyyBYu0tEn7Duo4SOad7Q7R2OmJKV4eqjWFNXeGmbe3n6ZjUAWzz8x4MtzRgUZkSZvkL1701gW2Ozutr8-mwUa06vCV9iIjIqWBz45tzNqLXEzH8zA8LlzCksX8DS2VtVPt6g2OkitJQF_EBizlvho9iuTAVcil4NorfElCTjnVHSnNzRIL38QOwfdMS2HxEI6iq5F7TJlohiBnAHYGdhtYiquPiMm6CtartE_ueWGUOfzI8OvpQCJNJdsFOfnneM15dN6arYmc9iilzZ4A2R-gKTvnfVlaRxJjIRS9n0EyMU1CdBU5VwsRxqPW2Gqx76-OspsAXfngoIvza4rnzzIOLm6NvJeqYNPEVCJwGYH9QL7h1LdMdMGEYCu59QtQCcFIEBydhR7AcLYDn1nNjkn_NIIwdIZ6XrlVdfL3pH-8kzCAmyfy54GHHqvios3C4ukep2JkYiCsCAYMvtJjpThuKBmgtuzCZf5p5XRzrbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در جریان دیدار با رهبران و نمایندگان کشورهای عربی خلیج فارس، ترکیه،‌ اردن، سوریه، مصر و لبنان، ترجمه ماشین:
فقط می‌خواهم این را اعلام کنم که استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌های ایران داشتند؛ عمدتاً میانجی‌ها. ببینیم چه پیش می‌آید. آنها مدتی است که میانجی‌گری می‌کنند، اما فکر می‌کنم شتاب زیادی برای رسیدن به توافق وجود دارد. این چیزی است که از همه می‌شنویم.
و سخنرانی مرا هم شنیدید. لازم نیست دوباره مرورش کنم، اما ما ضربه سختی به آنها زدیم. قصد فخرفروشی نداریم، اما اقتصادشان واقعاً در وضعیت بسیار بدی است و امیدوارم کاری بکنند که واقعاً به نفع مردمشان باشد. و فکر می‌کنم واقعاً همین کار را خواهند کرد. واقعاً همین‌طور فکر می‌کنم. گزینه دیگر برای هیچ‌کس قابل قبول نیست.
جرد کوشنر... [بخش نامفهوم] اما استیو و جرد، دو نفر بسیار باهوش هستند و دارند کارشان را انجام می‌دهند و فکر می‌کنم این ماجرا را تمام خواهند کرد. هر دو طرف احترام زیادی برایشان قائل‌اند. ایرانی‌ها برای هر دوی آنها احترام زیادی قائل‌اند و فکر می‌کنم این مهم است. اما فکر می‌کنم کار را به سرانجام می‌رسانیم.
...
می‌دانید، زمانی خواهد رسید که دیگر خیلی دیر خواهد بود و ما دیگر شاید فرصت این را نداشته باشیم که بگذاریم به‌عنوان یک کشور باقی بمانند. من مایلم بقای آنها را ببینم. می‌توانم بگویم افراد دور این میز هم دوست دارند چنین چیزی را ببینند. بعضی‌ها از شنیدن این حرف تعجب می‌کنند، اما آنها چنین چیزی را می‌خواهند.
همان‌طور که می‌دانید، نیروی دریایی آمریکا مین‌های ایرانی را از مسیر کانال‌ها در تنگه هرمز پاک کرده است و اکنون در حال تسهیل ازسرگیری جریان نفت هستیم. اخیراً اعلام کردیم که بیش از یک میلیارد بشکه نفت را از خلیج اسکورت کرده‌ایم. حالا این برای تمیم رقم زیادی نیست، اما برای بیشتر مردم هست. یک میلیارد بشکه؛ این نفت زیادی است، درست است؟ از هر طرف حساب کنید همین است.
اما اخیراً اعلام کردیم که دوباره بیش از یک میلیارد بشکه نفت را فقط در همین مدت اخیر اسکورت کرده‌ایم و هر شب ۲۵ تا ۳۰ کشتی را خارج می‌کنیم؛ گاهی روزها هم، اما بخش زیادی در شب انجام می‌شود.
محاصره قوی‌ترین چیزی است که کسی تاکنون دیده است. اسمش را «دیوار فولادی» گذاشته‌ایم و نیروی دریایی ما شگفت‌انگیز است. ارتش ما شگفت‌انگیز است. واقعاً شگفت‌انگیز است. و حالا نفت بیشتری از تنگه عبور می‌کند، نسبت به هر زمان دیگری، با فاصله زیاد، از آغاز درگیری تاکنون.
و باز هم، بخش بزرگی از کاری که کرده‌ایم، شاید ۹۹ درصدش، برای اطمینان از این بوده که ایران سلاح هسته‌ای نداشته باشد. آن سایت‌ها منفجر شده‌اند. شاید مجبور شویم یک سایت دیگر را هم منفجر کنیم؛ کوه پیک‌اکس. فعلاً فعالیت زیادی آنجا نمی‌بینیم، اما اگر ببینیم، فوراً آن را منفجر خواهیم کرد.
در حالی که همه اینها خبرهای بسیار خوبی است، حملات تروریستی ایران به کشتیرانی تجاری و کشورهای همسایه نشان داده که لازم است زیرساخت انرژی خاورمیانه را از گلوگاه‌های تحت کنترل ایران دور کنیم. به همین دلیل دولت من قویاً از کریدور اقتصادی هند–خاورمیانه–اروپا حمایت می‌کند و همچنین از راه‌های دیگر برای انتقال نفت، چه از طریق خطوط لوله یا هر راه دیگری.
و با همکاری هم، در آستانه غلبه بر چالش‌هایی هستیم که دهه‌ها این منطقه را گرفتار کرده‌اند. این وضعیت دهه‌ها ادامه داشته است.
پس آنها ایران را به مدت ۵۱ سال «قلدر خاورمیانه» می‌نامیدند. من می‌گفتم ۴۷ سال، اما چهار سال است این را می‌گویم، پس عدد واقعی ۵۱ سال است. و واقعاً دیگر قلدر نیستند. می‌توانند مشکل ایجاد کنند، اما دیگر قلدر نیستند. ولی قلدر خاورمیانه بودند و همه بسیار نگران و به نوعی ترسان بودند. شاید هم حق داشتند، اما دیگر نمی‌ترسند.
بنابراین فکر می‌کنیم که وضعیت ایران ممکن است درست بعد از انتخابات میان‌دوره‌ای پایان یابد، شاید هم قبل از آن. نمی‌دانم. هیچ‌وقت نمی‌شود مطمئن بود.
اما آنها درک نمی‌کنند. چیزی که واقعاً درک نمی‌کنند این است که من انتخابات را با اختلاف بسیار زیاد بردم. هر هفت ایالت چرخشی را بردم. در رأی مردمی، با اختلاف میلیون‌ها رأی پیروز شدم. در شهرستان‌ها ۸۶ درصد بردم، چیزی که قبلاً هرگز اتفاق نیفتاده بود. این بالاترین میزان تا آن زمان بود؛ و در کالج انتخاباتی هم با اختلاف زیاد، اختلافی بسیار بزرگ.
و من نامزد نیستم. افراد دیگری نامزد هستند. جمهوری‌خواهان دیگری نامزد هستند. آنها آدم‌های فوق‌العاده‌ای هستند و من کمک می‌کنم انتخاب شوند. اما خودم نامزد نیستم.
و اصلاً به انتخابات فکر نمی‌کنم وقتی که به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم. فقط به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم و تمام. فقط به همین فکر می‌کنم. و هیچ ارتباطی با انتخابات ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgDMZYWSJHFas6GmEm38-qDbR1e9cYY2RRKh76MeaaOwkDJZ2MZPAZenS8UaNOho-abgINB8nxuffSJZd7JsgvJpWiffFeP33nls0eVfs34u2TTlWkAkYQZywxm15Hdt-JOK9HLLwiilGBRc4cOrSxhJOA1tDFcDYwcD7EZVxIYpEhs5iyv9PgWCKCBJIPnXJR_Zo_TGOXaWnU1CX4A-cPunDfDG4NAkalZ6dLZlpHa9I3p4kE_cn0A9HK8_RaZa9mjsApHktleDBvA-UT6U01OxWx5-sunqo8ccwGjkCyy5BGrrNnaY9NzPCjoWauMiBwn9Pq_n5yEnjaPSboFruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=dCKXQZBq2tYJGJgWefVrJe3PkMumkVOgCe4uVOlkUgHprR31A8WB57s-e6tOxy6i9KBzsWB6XMMpHhQNGN_QLodeUjYL5MxUbPLdIz7DMa_TqcI70Uc2N9QXUBCMuaf-3kl7d9aBGA9NeSx0ndJ2YQSF-ASe4YJ3K9tX0OeJYq3HM-6oEnc4Ge0w1-EMk9ozQDWHE_vlN3JmQxJxttyI5UVFe9Ir0LbOeLK1kLhLiF9fydzg2StYM3b-dgK34POdKCVtUTGbyp1OXNwiaGrVpgS44l_tzPxQQosKNqA-r-JpHWdyA8bfrDwez7YUl1DA4_tXZVSBjlA79hq7N30vbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=dCKXQZBq2tYJGJgWefVrJe3PkMumkVOgCe4uVOlkUgHprR31A8WB57s-e6tOxy6i9KBzsWB6XMMpHhQNGN_QLodeUjYL5MxUbPLdIz7DMa_TqcI70Uc2N9QXUBCMuaf-3kl7d9aBGA9NeSx0ndJ2YQSF-ASe4YJ3K9tX0OeJYq3HM-6oEnc4Ge0w1-EMk9ozQDWHE_vlN3JmQxJxttyI5UVFe9Ir0LbOeLK1kLhLiF9fydzg2StYM3b-dgK34POdKCVtUTGbyp1OXNwiaGrVpgS44l_tzPxQQosKNqA-r-JpHWdyA8bfrDwez7YUl1DA4_tXZVSBjlA79hq7N30vbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
در دیدار با ایران، آیا آقای کوشنر و آقای ویتکاف شرکت داشتند؟ درست متوجه شده‌ام؟
ترامپ:
می‌خواستم همین را بگویم؛ آنها دیداری بسیار خوب و بسیار سازنده داشتند و دیدار دیگری هم برای آینده بسیار نزدیک برنامه‌ریزی شده است.
استیو، اگر می‌خواهی... جرد، اگر می‌خواهی چیزی بگویید؛
آنها دیدار بسیار سازنده‌ای داشتند.
حدود یک ساعت پیش.
خیلی خوب پیش رفت. یک ساعت پیش تمام شد. دیداری بود که سه ساعت طول کشید. یک ساعت پیش تمام شد.
دیدار بسیار خوبی بود. یعنی باید بگویم، خیلی خوب بود. اصلاً نمی‌توانم تصور کنم چرا آنها نخواهند به توافق برسند.
یا عظمت است؛ عظمت بالقوه... یا نابودی کامل. دو انتخاب وجود دارد. یعنی، در یک حالت نابودی کامل است و گزینه دیگر، عظمت بالقوه است.
ایران می‌تواند کشور بزرگی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtwDfL0GqYSzhVNYdZW63keJU6AFNJPbWBwtWHWYSbS8M1jzl_wWgEWWqgz__pfxPbHOn__bDkpQG_5feKJXNiykLBMP3h-gmZw2mA6Zc5bqWu5ZtCnnWz8LCHyqACxO1wPEf7VSe-eXRcGUX5dITpev9QD1qjwQBxLv7jyEUQhvngY7GEQ_vuvBc4LiLHR-q4iaS5TSxJDNTpsv32yUNPZZ7CrOoqMeN2DIwySLo_nhaZRi7uCIbiF0LLGTg-RqZthePrREpp6JZ9lGq9s03S9hJ0nUrC-jSIJlIb-SgQKwGkQIWx3UI74jZXHkuLoOk5qZJ7ls9ovul95JMJLsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l1V0XGPDzrxEGPRlWUtfctFCMfdB0awQxCcmltUqdz_QW7tckS2xtjqhQ3gS6aIyGq5j0Dzu3SMOqQi94-cO04b473GX7CHBZDJ8C1Syi_pW9loyKf9iDlmYd9OdlDNUPXbNHzJo8g-gwgd87ZjTCd3wIbpEp1k69QD5L__LUZzOz5W1TSOW1qVnFBB9p-DTOL10o8FELHeqwjdSKpiXRZehngoSwv9LWu1MDAx8fonvd-IkIfd6-vNRpSoO05jptiEkjihBaWqVJospIHaqw6X1VBJvrXWbfNFC80jpEP_V2U2Zu-uK04iYUDvVhC9oxY0o7ULxMjJQKqTpbKyPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNyU3A0aOYKxaSsbFQ0JtHrAcZdAZCrPIhGKZ56F9Lb-7CnZyQ6TAhvvefpZY_Wx_ZF0ZU4m5OprBCgcZtQHOIWdG5oMWYW_Bu5ER8y8wPfHVol8qUvfP7GB9YmjFUYwIewD_9051St3V8pdwdlOYKawgZ3OknZduGdMXZ69WZY6jPbfXXx57R86EjMT3Ig4urt6WByjdLHq4SblrKNTB7eYeMMBEre-Rd2jHiO3ElQPrlgeDTweabmS-z7Xk0DgLK4KMBe4FayZEdPDmAJWBT-k6-C8OcYCS-VarIBuBphb8BHxU33UBlqvyg5FkLYY2qZPZaAvIpjsGPNQCShPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در دیدار با اندی برنهام، نخست‌وزیر بریتانیا، در سازمان ملل در نیویورک گفت تهران و واشینگتن روز سه‌شنبه نیز در حال گفت‌وگو بوده‌اند و افزود: «فکر می‌کنم توافقی حاصل خواهد شد.»
ترامپ گفت: «ما مانع دستیابی آنها به سلاح هسته‌ای شدیم. واقعا جلوی آنها را گرفتیم. آنها سلاح هسته‌ای نخواهند داشت و خواهیم دید چه اتفاقی می‌افتد.»
برنهام نیز گفت در نخستین دیدار خود با ترامپ «ارتباط خوبی» با او برقرار کرده و دو طرف درباره خاورمیانه، جزایر فالکلند و مسائل تجاری گفت‌وگو کرده‌اند.
او خطاب به ترامپ گفت بریتانیا آماده است نقش خود را در خاورمیانه ایفا کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78492" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xg_QrysnZsAa6-lrk_WY2-AE8W6gmPd5mmYY-xSA2Fx4pEbDGgB2pt5I9cmRnetFitXXn-TvSP3Im4Hux93fQ_ST_yfLPTgtqSO1UKE0QPtbcmj9p9crWQK2iDoqoq3jWEYSklrlgJqdOeaobCVwS7kii_v-LhGfWYMIsx4yDwX_JAgmVp8iKE84EY_QtQEXQvZyonWDOIHo5etp8eku7H-E-r-ciUnb4D2fNjDjt8i_QK8O1YcpVEwRwg_qQR_GLUE7OfU0zzPsUeBIhoO-n5Uba64l6uMMZM4fWOdLbWmNUeu60cAfhqOy03ENV6Zn8be0KcroThwDJEJ97TEfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4be0LkMmtIImzoyMRzmEJIoNXBIvoCKPBGOi8PS3-a5irZMEAusqkRUL5hBrKCqimcufj8_Ktie3ekb5TSrypA-YdT0T6aqVKQoI9notEzaiIlRdINs5VbAEgWxqviI5BPbNLODw_y6omaVLTPFe3hhf3WlJGfdKDDhZtrsOm1ZRHQbLSaOs9ll3SeQ5ydF1GTDE1vrl6EWPWJQXOp3Ueya0d8d6Ps8hm3SpKlwVzR8zxzpmSB88G47o7zEwbMWZnlMSn6k-PLpn5UymQlzH-LIPSGoNuW7xjwvkz1nEMNtJsw-zFifSk4T9k-nYv1NpW1gVqHm4NpuI4E5BySDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpy56hglfrIMHQqEmCzS6okysCTZIWcUU5TSnXU70VYaXd1K8wVKDTuIlK8WHTyGSCUTUkza29jWgIq_0-nFnz6tv8MwOwLnDaUE-T63x4mFnC2rs5DIlT1UT0-xrrU6RGGBE7ct_xZHMaTqhPzqZ8vsV2t8KoEZNXNEAR4c3EZUUa_ypiQ6nSRcNgxpp_gSHQtrFvHP8o82X_aFYjmCeUYh5HFnzNXOkFq-dnkRdj_4XadO7FUW927mfxQBwXnGWEdaUlVXwjhdvbxzw30GU-zaIhsTTPc5xaWe1X7xvP53VYitm108A9OlNAPRR_r93NDQm-bl-bqf58iL7J8PRph8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=ohjQ7jhllGMyHFzeG9UULRrT6aa9WzgrJZ_UCRMGFLIVMkK2QEggtkzKyRKcnYZR9c7Nf-tb91fIOU9It5LAMBeOOnqEQmqkS-xxD80aUvPg8szd_NJCn0J0Ivcp6KsMlXB-7P9CqVD5HM9WtbLFuEsUnwfc9EWSNs0ZAY4KxN_aDaHH9ykJb3-LqxnUXvnb8vWomnJ3UXKGT1N2NqhhJ_vYavIP_lypdkDhMDnHE2APpviEQZ1HiyfSbTtp3W84tpYvTFVe1wvkeKO-5ALqSxwtZEnokw9yazDE0KFR28ug51w7OCNurP5JUcgjx0g7mZglhH-0BanbrzLqj6fPpy56hglfrIMHQqEmCzS6okysCTZIWcUU5TSnXU70VYaXd1K8wVKDTuIlK8WHTyGSCUTUkza29jWgIq_0-nFnz6tv8MwOwLnDaUE-T63x4mFnC2rs5DIlT1UT0-xrrU6RGGBE7ct_xZHMaTqhPzqZ8vsV2t8KoEZNXNEAR4c3EZUUa_ypiQ6nSRcNgxpp_gSHQtrFvHP8o82X_aFYjmCeUYh5HFnzNXOkFq-dnkRdj_4XadO7FUW927mfxQBwXnGWEdaUlVXwjhdvbxzw30GU-zaIhsTTPc5xaWe1X7xvP53VYitm108A9OlNAPRR_r93NDQm-bl-bqf58iL7J8PRph8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=ZP_4V6phNoMV72oqHEGAfL9I4hXPwhFOf1IsJ5kxs-Qk6fhDvm2XfFKBu1IW5MyINXUubddeuEu9E3w8tjh7gQ38p1NRKWD1hnJXBE1ya_B5aWaqz73Nr-JdlF9-TIhSnt-eDb0ptiIAoLJXUDORLpOjEBKuKJW-n4udQB4EgEFgfIPYVUAn4sNS37-Hol-8B_pEHneGCtJOncKM19xJB39du2dTTedpEm1sx09mkbaYtHBWqaCwQiuLx-ggfcOBgYjQ5zTygdhD4xJ16xUdkk8FI2YgugV08ddRwhqLpTUyOVgp3tw8gOZPf5hXu9qQPtyFp2oLFrC95tBH6cth6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=ZP_4V6phNoMV72oqHEGAfL9I4hXPwhFOf1IsJ5kxs-Qk6fhDvm2XfFKBu1IW5MyINXUubddeuEu9E3w8tjh7gQ38p1NRKWD1hnJXBE1ya_B5aWaqz73Nr-JdlF9-TIhSnt-eDb0ptiIAoLJXUDORLpOjEBKuKJW-n4udQB4EgEFgfIPYVUAn4sNS37-Hol-8B_pEHneGCtJOncKM19xJB39du2dTTedpEm1sx09mkbaYtHBWqaCwQiuLx-ggfcOBgYjQ5zTygdhD4xJ16xUdkk8FI2YgugV08ddRwhqLpTUyOVgp3tw8gOZPf5hXu9qQPtyFp2oLFrC95tBH6cth6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
ترامپ: ایران در پی ساخت موشکی بود که می‌توانست اروپا را هدف قرار دهد
▪️
رئیس‌جمهور آمریکا در سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران به ساخت ذخایر گسترده موشکی و پهپادی ادامه داده و مدعی شد تهران موشکی ساخته بود که توان هدف قرار دادن اروپا را داشت. او گفت هدف ایران این بود که در پوشش چنین توان موشکی‌ای، به سوی ساخت سلاح هسته‌ای حرکت کند.
▪️
ترامپ همچنین با اشاره به حمله هفتم اکتبر گفت عاملان این حمله از سوی ایران تامین مالی شده بودند و افزود حکومت ایران «چنین خشونتی را جشن گرفت». او سپس حکومت ایران را به کشتار گسترده شهروندان خود متهم کرد و گفت چنین حکومتی نباید امکان فعالیت «در پشت سپر هسته‌ای» را پیدا کند.
@
VahidOnLive
🔻
ترامپ: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند
▪️
︎ دونالد ترامپ در سخنرانی خود در مجمع عمومی سازمان ملل، جمهوری اسلامی ایران را «بزرگ‌ترین حامی تروریسم» خواند و گفت که حکومت ایران سال‌ها در خاورمیانه «مرگ، ویرانی و هرج‌ومرج» گسترش داده است.
▪️
︎ او گفت: «هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند» و افزود پس از آغاز دوره ریاست‌جمهوری‌اش، مذاکراتی را با ایران آغاز کرد و در مقابل پایان برنامه هسته‌ای و حمایت از تروریسم، پیشنهاد همکاری اقتصادی کامل داد، اما به گفته او ایران این پیشنهاد را رد کرد.
▪️
︎ ترامپ همچنین گفت که ارتش آمریکا در عملیات «چکش نیمه‌شب» برنامه هسته‌ای ایران را هدف قرار داد و پس از آن نیز از تهران خواست توافق کند، اما ایران بار دیگر نپذیرفت. او سپس ایران را به ادامه انباشت موشک‌ها و پهپادهایی متهم کرد که به گفته او امنیت نیروهای آمریکایی و دیگر کشورهای منطقه را تهدید می‌کرد.
@
VahidOnLive
🔻
دونالد ترامپ: تصور کنید حکومت پلید ایران پشت سپر هسته‌ای حملات تروریستی انجام دهد
▪️
︎ دونالد ترامپ گفت: «فقط تصور کنید اگر چنین حکومت پلیدی روزی قادر می‌شد در پناه یک سپر هسته‌ای حملات تروریستی گسترده انجام دهد. این واقعیتی بود که باید با آن روبه‌رو می‌شدیم؛ واقعیتی که افراد بسیار زیادی ترجیح دادند آن را نادیده بگیرند.»
▪️
︎ او افزود: «در حالی که دیگران حرف زده‌اند، من عمل کرده‌ام. در حالی که دیگران از صلح سخن گفته‌اند، من آن را برقرار کرده‌ام. در حالی که دیگران تهدیدها را نادیده گرفته‌اند، من با آنها مقابله کرده‌ام.»
▪️
︎ ترامپ گفت: «من از آن برای تبدیل آمریکا به قدرتمندترین کشور جهان استفاده کرده‌ام.»
@
VahidOnLive
🔻
ترامپ: امیدوارم پس از انتخابات با ایران به توافق برسیم
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت که آمریکا باید فشار بر ایران را حفظ کند و افزود نیروی دریایی آمریکا تاکنون بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت کرده است. او گفت اکنون نفت بیشتری نسبت به هر زمان دیگری از آغاز جنگ از این مسیر عبور می‌کند.
▪️
︎ ترامپ سپس گفت که در برابر ایران با یک «تصمیم بزرگ» روبه‌روست: یا توافقی حاصل شود که به گفته او به ایران امکان بازسازی و تبدیل شدن به کشوری «بسیار بزرگ‌تر» را بدهد، یا آمریکا مسیر نظامی را در پیش بگیرد. او در عین حال گفت: «فکر می‌کنم درست بعد از انتخابات به توافق خواهیم رسید، چون منطقی نیست که آنها توافق نکنند.»
@
VahidOnLive
🔻
ترامپ: نیروی دریایی و نیروی هوایی ایران از بین رفته‌اند
@
VahidOnLive
🔻
ترامپ: انتخابات در تصمیم من درباره ایران تاثیری ندارد
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران ممکن است منتظر نتیجه انتخابات میان‌دوره‌ای آمریکا باشد، اما تاکید کرد این انتخابات در تصمیم او درباره ایران «اصلاً وارد محاسباتش نمی‌شود.» او گفت: «تنها چیزی که اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
▪️
︎ ترامپ همچنین گفت برخلاف ادعاهایی که به گفته او مطرح می‌شود، آمریکا با کمبود مهمات روبه‌رو نیست و ذخایر تسلیحاتی این کشور با سرعتی بی‌سابقه در حال افزایش است.
VahidOnLive
🔻
ترامپ: اگر توافق نشود، جمهوری اسلامی ایران را نابود می‌کنم
▪️
︎ دونالد ترامپ در مجمع عمومی سازمان ملل گفت باید تصمیم بزرگی بگیرد که اگر توافقی حاصل نشود جمهوری اسلامی ایران را نابود خواهد کرد. او گفت فکر می‌کند ایران بعد از انتخابات میان دوره‌ای با آمریکا توافق خواهد کرد.
▪️
︎ او بار دیگر گفت جمهوری اسلامی ایران بزرگترین حامی تروریسم در دنیاست اما اکنون دیگر تهدیدی نیست چون آمریکا برنامه هسته‌ایش را نابود کرده است.
▪️
︎ رئیس‌جمهور آمریکا بار دیگر گفت اخیرا ده‌ها هزار معترض اخیرا در ایران کشته شده‌اند.
▪️
︎ او از اروپا انتقاد کرد که متوجه تهدید موشکی ایران نبوده است.
▪️
︎ آقای ترامپ بار دیگر گفت تمام قوای نظامی و اقتصاد ایران نابود شده است.
▪️
︎ او همچنین گفت دولتش در ۱۲ ماه گذشته بیش از هر دوره‌ای در تاریخ آمریکا در زمینه نظامی سرمایه‌گذاری کرده است.
@
VahidOnLive
🔻
ترامپ از همه کشورها خواست ایران را «به‌طور کامل از نظر اقتصادی منزوی کنند»
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل از همه کشورها خواست به آمریکا بپیوندند و «انزوای کامل اقتصادی ایران» را اعمال کنند؛ تا زمانی که به گفته او تهران حملات به کشتی‌های تجاری را متوقف کند، از «جاه‌طلبی‌های هسته‌ای» خود دست بکشد و حمایت از تروریسم را پایان دهد.
▪️
︎ او حکومت ایران را «ضعیف و مستأصل» توصیف کرد و گفت اگر کشورها متحد بمانند، به گفته او «تهدید ۵۱ساله تروریسم ایران» پایان خواهد یافت و قیمت نفت نیز کاهش پیدا خواهد کرد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXoz-I-n6A2Ubnsaz6Z9rj192EFA97KZCoy-EsmXro9cG3ATvKxWAb_q_OFwvbymAZhF-Nf7cs_8eUH_GdUXkIXaPQPG8Ly8vfGtmQqOy0lrfrG8jEyPeb136E1R0qVBGiwi0WAETRDL_PU_Tdv3gP5jJvLOF_8q-7WCUgmgBiVxo8FXuBYALvAsuUKq0YCOy_RlXBXoD_zJQRDmtEsz-OozFMlOAz9Hb5NVcIZ2oECBHNBX0NSECs9pGnhymeyhXUlgxQNEf_mjeCN3K5X8IDyuNX61njtxH_nkciEh3uaYH8Ai-Lju5r5qHraOaT9HGF5qi43Ft--Pmp6uI_PAJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد جمهوری اسلامی گفته است تهران پیشنهاد کرده در صورت کاهش فشار نظامی آمریکا و برداشتن گام‌های اولیه برای پایان محاصره بنادر ایران، تنگه هرمز را ظرف هفت روز بازگشایی کند و به مذاکرات با واشنگتن بازگردد.
خبرگزاری «کیودو» روز سه‌شنبه۳۱شهریور۱۴۰۵ به نقل از این مقام، که نامش اعلام نشده، گزارش داد این پیشنهاد از طریق میانجی‌ها به دولت آمریکا منتقل شده و بخشی از تلاش تازه تهران برای احیای مذاکرات با واشنگتن است.
براساس این پیشنهاد، جمهوری اسلامی خواهان ازسرگیری مذاکرات با هدف رسیدن به توافقی برای «پایان دائمی مخاصمه» میان ایران و آمریکا است.
این مقام گفته است تهران در مرحله نخست انتظار دارد واشنگتن نشانه‌هایی از آمادگی برای بازگشت به مذاکرات نشان دهد و اقداماتی را برای پایان محاصره نظامی بنادر ایران و توقف عملیات نظامی مرتبط با تنگه هرمز آغاز کند.
در صورت برداشته‌شدن این گام‌ها، جمهوری اسلامی آماده است ظرف هفت روز مسیر عبور کشتی‌ها از تنگه هرمز را باز کند و به میز مذاکره بازگردد. این مقام تاکید کرده است آمریکا برای پیشرفت دیپلماسی باید «جدیت و تعهد» خود را نشان دهد.
کیودو نوشته است پیشنهاد تازه تهران به تایید «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، و شورای عالی امنیت ملی رسیده است. مقام ایرانی مشخص نکرده که آیا این پیشنهاد به معنای عقب‌نشینی تهران از بخشی از هفت شرطی است که پیش‌تر برای مذاکره و بازگشایی تنگه هرمز مطرح شده بود یا خیر.
براساس گزارش کیودو، شورای عالی امنیت ملی ۲۵مرداد تصمیم گرفته بود اگر آمریکا ظرف ۴۵ روز محاصره بنادر ایران را پایان ندهد، جمهوری اسلامی گزینه حمله دوباره به نیروهای آمریکایی را برای خود محفوظ نگه دارد. این مهلت اکنون به پایان خود نزدیک می‌شود.
هم‌زمان، یک مقام ارشد ایرانی به «رویترز» گفته است هیات جمهوری اسلامی در مجمع عمومی سازمان ملل در نیویورک اختیار کامل برای احیای گفت‌وگوهای دیپلماتیک با آمریکا دارد و جزییات توافق احتمالی می‌تواند از طریق کشورهای میانجی در نیویورک بررسی شود.
مقام ایرانی احتمال دیدار «مسعود پزشکیان» و «دونالد ترامپ» در حاشیه مجمع عمومی را رد کرده، اما گفته است همچنان «امکان حرکت به‌سوی توافق» وجود دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78486" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct5F-qoUrNHcffE0CCRy3_fBsixXT2I2XKlegD59d-AM3Mg5AoxaF5DCap7-NMnAaHzeAqKLQpYrNWTe6QzBIkw0oVROYPiNDDO5wXbhoOw1J4qsKiJSxdGMah8aM5DJhoniiDR_CZRYeW4NfWFMajdfonQW7iRY0_SrlOcwl_l7lPztFxcKE6kqbmtbWO9Jl46lgJABNbnet-MS1hP2XrGVNqkr2rTYMqShLHKmUPvKMBGJp7ZUXelEWa1pVlLPGhBkAvh_aRvEro31Xo7KyoVr26WLzokgWwdHxqjCVczg5QR5K4dxte1whpFP1LZnNYBJ-rDxnhwW0h7a43Psdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPkXGw8UJ16iG45m1Ir7Gs3zJUCzVint7Q3cNUNV6IO15jQ1tjXvtwNsGWQXD0LHHPUJcSy8R_gEn-bzoOuQCeDxS8dl6EsDWEyuoTV4iOtPU5XhQTVEBx_OaJtpjTLH2N5mNGU0mQ1nr5xb-4cDg9hjxPl-VkUUeTa7r942DdQgPEs3mKBSoNJylwZ2538NQtmvMaczIQJePaz7N1byAzyE-pKEuuskaDGwxIRY2P3BFzhvy0R3V4QPz4riy9WLGczLWvW397TpmYGPyWQxLdGZGtyFgzBLV-N4sI2iRdj8yZfbVNR0n6i737kCEOWd3xHpRkri0w2c-Tatq3mwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران روز سه‌شنبه با نزدیک یک درصد افزایش نسبت به روز گذشته به ۲۳۳ هزار تومان رسید.
بر پایه داده‌های شبکه اطلاع‌رسانی طلا و ارز دلار روز دوشنبه ۲۳۰ هزار و ۸۰۰ تومان بسته شده بود. بهای دلار در ساعات نخست معاملات امروز تا ۲۳۵ هزار تومان نیز بالا رفته بود.
یورو ۲۶۷ هزار و ۴۴۰ تومان، پوند بریتانیا ۳۱۱ هزار و ۴۳۰ تومان و درهم امارات ۶۳ هزار و ۴۷۱ تومان معامله شد.
در بازار سکه، سکه امامی با یک و نیم درصد افزایش به ۲۳۸ میلیون و ۴۸۰ هزار تومان رسید و سکه بهار آزادی با یک و هفت دهم درصد افزایش ۲۳۴ میلیون و ۶۷۰ هزار تومان قیمت خورد.
نیم‌سکه با هشت دهم درصد افزایش ۱۲۱ میلیون و ۴۰۰ هزار تومان معامله شد. ربع‌سکه ۶۳ میلیون و ۸۰۰ هزار تومان و سکه گرمی ۳۳ میلیون و ۲۰۰ هزار تومان بدون تغییر ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6hUw5s2NYVmzZcb1_WSL2E7H7RPjnv6MPIhZkDQs0oSVaKRvoe97p-LX7HY6VkdSOT72_Vlt8U1QKh0b3ZT8Bzo7rzpinX060uaBLxuOYTAau8i6KmdDEQGdS1GiJVWBuMFmAut4xZXNTCu0iV7Kfym3HKZs6lubnaT4vpec-KhCrhQTG33tKUThzR3vfiGlZpmhnPO6ex5M2dx_biGrwRrFtMBL6_RAaXwmhEQeLYo0v5zsg0Kz8K4H3xjEHrp8wpa4XjdP-7IM3ery8x34clYaxZTK4jWq2JZyg6zPgzjrFzZJLe3Ztu1iDL2z8V7s2E_vu9-AfE4EsNZJXbqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهور آمریکا می‌گوید این کشور «بیش از آنچه حتی بتوانیم برای استفاده تصور کنیم مهمات» دارد و به گفته او «اکنون نیز در حال افزایش ذخایر مهمات خود در سطوحی هستیم که تاکنون هرگز شاهد آن نبوده‌ایم.»
دونالد ترامپ روز سه شنبه، ۳۱ شهریور در پیامی در شبکه اجتماعی تروث‌سوشال با رد وجود کمبود مهمات در ارتش آمریکا از کسانی که آنها را «بزدلان و خائنان» نامید نوشت آنها دوست دارند بگویند که ایالات متحده با کمبود مهمات مواجه است. این درست نیست.
نوشته رئیس جمهور آمریکا می‌تواند واکنشی به گزارش رسانه‌های مختلف درباره کمبود مهمات در ارتش آمریکا به‌ویژه پس از جنگ اخیر با ایران باشد. در این گزارش‌ها به‌ویژه از کاهش ذخایر موشک‌های رهگیر سامانه‌های پدافند هوایی خبر داده شده بود.
این در حالی است که شرکت لاکهید مارتین روز ۲۴ شهریور اعلام کرده بود که نخستین محموله از قطعات حیاتی موشک‌های رهگیر «پاتریوت» را از شرکت «جنرال موتورز» دریافت کرده است؛ این تحویل کمتر از یک ماه پس از امضای توافق‌نامه تولید میان دو شرکت صورت می‌گیرد، آن هم در شرایطی که پنتاگون بر تسریع روند تولید تسلیحات تأکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/78483" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw1YyRQmFueDkKZPrghWlBouVxM9rBdWPLVg8WVpI_nfOXmuuDu0IW1lLnmZb6IG8rj4KJUpUW7EkkKdP8zg8N6GpWnT9IRGons1870NLsM85784HzrLeNoTIJttS5mOLe2SVBXzj5w3iqWvsZdhagnX3LnEMzltWi0s9gNYeu8UAwYH8nTOe6p1IimNhQ0A7KWzvwp9ufZ1_B_oTbyb2icRMgOdCijsGs_Cbx-hpNBbOI499-rxeHsLM3ocgm1IiY7Hxcnb960LW0QrkmjIjycEu_q_6njAvEbeUiPGBEmf3H5YXSoXGThBsrf3aoCRA422rhcRNUnljNc5QVQWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو گفت آماده ملاقات با مقام‌های ایران در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک است.
وزیر خارجه آمریکا گفت: «فکر نمی‌کنم در حال حاضر چیزی برنامه‌ریزی شده باشد، اما قطعاً برای چنین دیداری آمادگی داریم، به‌ویژه اگر چشم‌انداز آن نتیجه‌ای مثبت و در نهایت تحقق هدف اصلی باشد.»
آقای روبیو گفت منظور او از چنین چشم اندازی این است که «ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.»
عباس عراقچی، وزیر خارجه ایران از دوشنبه در نیویورک است و مسعود پزشکان هم عازم این شهر شده است تا در مجمع عمومی سخنرانی کند.
دونالد ترامپ دو روز پیش به شبکه فاکس گفته بود که آماده دیدار با مسعود پزشکیان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/78482" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78481">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGrCFapt-t9XBc5OgsnM6t8BovXICGW_wVgGkZ7-8xYcJ31AUieidARf6bi7Ox0vnBGX72qmeRE7gXM_i0TC3stwcC1XPYnMwFJIy6IezSLsV4jXNQa6tlVO9Bz0sd10xYZ87kP2OgCptR-1iCtF7vrQkVQnSZb_ZjqJuGDV0dZ8OqfESdrgqhChQ6HyPGhBWSurXg1C5ATLIu6ERIRLooWM64DvjLdhSKR1meNw6i1gHVAxOZ7ex5SRrmQ95XU6Luz-01avTdK3Ogw33XFFtQckAU1RnV3B440KQvUMEENsOZQ5lqbSUlfw0kxDPwQhNyDiKVNgCMM6cX-_iajFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین روز سه‌شنبه، ۳۱ شهریورماه، رسما اعلام کرد که با تحریم «یک‌جانبه» خطوط هوایی ایران توسط واشینگتن مخالف است.
گوئو جیاکون، سخنگوی وزارت خارجه چین، در نشستی خبری گفت که پکن این گونه تحریم‌های آمریکا را «غیرقانونی» می‌داند و با اعمال آنها مخالف است.
این موضع‌گیری یک روز پس از آن رخ می‌دهد که اسکات بِسِنت، وزیر خزانه‌داری آمریکا، روز دوشنبه گفت که تمام شرکت‌های هواپیمایی ایران از تاریخ ۲۳ سپتامبر (اول مهر) «در سراسر جهان تعطیل خواهند شد».
او در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «وقتی هواپیماهای ایرانی در فرودگاهی فرود می‌آیند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛ در غیر این صورت از سیستم دلاری کنار گذاشته خواهید شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/78481" target="_blank">📅 17:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfCvouuDEoPAmCQkZe6n__Kajk0-_AZyIQJ9ipPtzurh9GUA62UB98giO98uxhi9nRzzPUCEZtO5jb-7ULU31wGk4dFWWYuy0xywSYcr3UGliPknKE1O1NOM0Z2jJ__p50CZtJWsUP1Ry3gt0u1rFlsf8aw_bQlHzrVXviw-aBFCGGI_36xTYXJtjxD9Z1XlEkE8XVZzBS4qX-1Z0-lOiQSY8gfrle27J0JZgv34EmyF_YrKpZ_Xk8b-hBiZ8EzmjOPOKIvsTH5VSmpdvyNq414VOk4Gd2gAkYHQcbuG6o53CJaJSu2DY1nrfdbrNgoyj4QRv_xzAQftV3ytbDR5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت نمونه‌های مثبت کووید-۱۹ در ایران برای پنجمین هفته پیاپی بالا رفت و به ۱۷ درصد رسید.
به گزارش مرکز مدیریت بیماری‌های واگیر وزارت بهداشت درباره هفته منتهی به ۲۷ شهریور، این نسبت در هفته مشابه سال گذشته هشت و نه دهم درصد بود. نسبت نمونه‌های مثبت کرونا هفته پیش از آستانه هشدار بالا گذشته بود.
وزارت بهداشت بر ضرورت تشدید مراقبت از عفونت‌های حاد تنفسی تأکید کرد.
این هشدار در حالی است که نگرانی‌ها از شیوع همزمان کرونا و آنفلوانزا تشدید شده است.
از طرفی واکسن آنفلوانزا با وجود نزدیک شدن فصل سرما هنوز در داروخانه‌های ایران توزیع نشده است. به گزارش روزنامه شرق، سازمان غذا و دارو از تأمین محموله‌هایی از چین، روسیه و برخی کشورهای اروپایی خبر داده، اما داروخانه‌داران می‌گویند خبری از توزیع نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/78480" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAr9y2i0XoZ_z_yUXu9UQMM081-dfSbema_phMfoT9MVBPzfpUgh29z4ibxgAZMKL5VAhCtU8RTl-9_xXkuZmztkf4TqpROmjCDmYxTF40ex3zSF4QxAF52R9Oo2hwp3kqJOV8GMDK8povt97bpa2OA2eMJtk3HAVqrBqfvtZafKFZba3XDNsscP33p5pXp-IY66U0Zq5IfXXLpzviYRhThyqB-bXzJrOkZ2ald3lVMqjQYFhewbASDlXJ9f_qOHKpjXeZCgeYyFKevyMmxbKWXGm7of0mH9gge1xLv6tE4ByhhvN0QsdN08weMWuyDXl7i__0I4MO0Jbyitct0_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر بریتانیا، می‌گوید با ارائه «پشتیبانی دفاعی و سوخت‌رسانی هوایی» به عربستان سعودی در برابر حملات حوثی‌ها موافقت کرده است.
اندی برنام روز دوشنبه ۳۰ شهریور گفت که این اقدام در پی درخواست عربستان سعودی برای دریافت «حمایت نظامی» صورت می‌گیرد.
دولت بریتانیا اعلام کرده است که زمان این طرح «محدود» است و براساس آن قرار است نیروی هوایی سلطنتی بریتانیا به جنگنده‌های نیروی هوایی عربستان در سرنگونی موشک‌ها و پهپادهای حوثی‌ها کمک کند.
برای ارائه این پشتیبانی، بریتانیا طی روزهای آینده یک فروند هواپیمای سوخت‌رسان «وویجر» را به منطقه اعزام خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78479" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOV24W5PYCseX59Pv5tPdQY6rYJjkvPyvvgASUOQTfcITFBOoR0lHkE0iWmXpfOz6168rlVMCIby980DQEbLe8qSX-kCiYPOckNzql6oyYduI3spB-_w5EKbgauAetmVQsIJ9kI4eE8AlOJG2EEknybS2assHhwC3KxYAIP4DK11iPzlvKcZon92OMtAo9MQniU8wCXO7bHPve_OtL2iCaG1OQY59uhhnVUuiwGlNm94zspTDI2ExLP1tOOTFBmc9Q5WTUpuDXNMd9D1Hzhr2jqpUNWUZjhpT1tgKiCAtaHn2ejCiUef3Oxfklz-E0iV7rSQ4CDfprnotgHa-885KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهوری فرانسه، روز دوشنبه، با انتشار تصویری از دیدار خود با دونالد ترامپ در اکس، از توافق پاریس و واشنگتن برای اقدام مشترک در زمینه امنیت انرژی و بحران‌های بین‌المللی خبر داد. مکرون در این پیام نوشت: «به محض ورودم به نیویورک با ترامپ دیدار کردم. ما تصمیم گرفتیم با همکاری یکدیگر برای کاهش تنش‌ها در بازارهای انرژی، از طریق حفاظت از زیرساخت‌های حیاتی در خاورمیانه و تضمین آزادی دریانوردی در تنگه هرمز، اقدام کنیم.»
رئیس‌جمهوری فرانسه همچنین با تاکید بر تحولات جنگ اوکراین افزود: «ما تلاش‌های خود را مشترکا به کار خواهیم گرفت تا توقفی در حملات علیه زیرساخت‌های انرژی و تاسیسات غیرنظامی اوکراین به دست آید. جمعیت غیرنظامی باید محافظت شوند و ما باید هرچه سریع‌تر مذاکراتی جدی درباره شرایط صلح میان روسیه و اوکراین را آغاز کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78478" target="_blank">📅 05:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FugQOR_cRNzDadGTSUtkt8As9EOJ9oKGrxU78Ba8bkmm-QBrTVZFHA3TKapfWguMtLHZdK-KKk4o82zBjhC_jf0lEyTWoXqjgW0yK_7pvn2WJncryKalAbTY51P6PA_yRN1deuF3xatq7KOoS11-u0SJjvv7vhG6ltzC89-vGpdU9COrqV4Kb-llB8sBwgHY-3E2oO6pFdpsalk-02l_J2w8MvKn4p4PA_Q-v10BOoT_-wihqHK_htOqkI8zEeinCgqd_QsH6s7-OjIeo0WwieDQ6jwnrCbAwHiIJg6kVmzxXFK4uyGyTt5KnDCeQDEQjC1FwL97YftkPBfYUAUnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYfZQvIaDTQkLQLxa5WtbEjc1ge0qjLYM5jKR4HL14LmF-01P1Jh1GxMQmwqkH_ZX-YVksuQrUk-oagVcEhvtorUrYz8Qe7HK7J_iH6O3YPHkJQ3jt7SUlB8l8jCro4JE6Tb2LrE-8VRYskdAgXE-5YmxaC8o75EIIeCya5h8z7boYiKAe76otxjC6pvKr6mv2pbisvYOD6aWi3Pacuvoq4qiFGLupyXGqaG_CIOXoGFjRA6g6PrJTYENM9W14GjILc3uGeLBkSc9asnOtcgy8Mm-17DZogOL0ZvRSFlqDOTd4kIvdw-qY9ggBcMs1XbsorFMsTzh42ZHQs3ySJeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=RfPldTgyuo4cdkZySnq4r2-t93IacgJHn72tO_5MBtYTbfEsXfY9Sol6mhxO82ap_LLk97Dprbo1g3m7WZjHqx8HI_Q8E1LjjsrxFeL4rtFm3mBeh3H7cPKKzFOQUoBQQXuEUoLVi2IzLBB4sioCqmLE1B-2JMejlmClE_iJOTdZ69J6xby94FFe9FEWQGrpvoAvXRaM37cCOdFpIBSv0YnCbse4SQONTTOJom0dNGu5pgeBQp1nk9iiNq2KBK4lfRaXWLviGh8IugCU4PgCgaZ7jLCAqBe8JzqTkjYXEYJqEgwvS2VerFYjePvSGdc_UWe4isqcm365dBBfbRNNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=RfPldTgyuo4cdkZySnq4r2-t93IacgJHn72tO_5MBtYTbfEsXfY9Sol6mhxO82ap_LLk97Dprbo1g3m7WZjHqx8HI_Q8E1LjjsrxFeL4rtFm3mBeh3H7cPKKzFOQUoBQQXuEUoLVi2IzLBB4sioCqmLE1B-2JMejlmClE_iJOTdZ69J6xby94FFe9FEWQGrpvoAvXRaM37cCOdFpIBSv0YnCbse4SQONTTOJom0dNGu5pgeBQp1nk9iiNq2KBK4lfRaXWLviGh8IugCU4PgCgaZ7jLCAqBe8JzqTkjYXEYJqEgwvS2VerFYjePvSGdc_UWe4isqcm365dBBfbRNNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q8InXW8ovWyQM2YcIp_lW3u9gBFOKnCoEppqFP3JI0QRHAv6jMcohutgFJiUNi-mg-NKH2FSRVKVmuFISwV00M9XmXKZMKsOPXFciaalu9Fjw8PQM34WFieIoNqeEAFjD6o4HRrc7QfCif9ziN2e3qSx-WZKsPlQpBh28HUs-YHaGx8f3-TIiFpr9gsnzx1TlCiDUmlJrVbTt2ebuKP2s3JB2Jb9T69h9NxyjVuiSqAotG38UTZlqVJIMCdI2luTSRNfFQCRZuE6Oi3jgX78XcjQI6YwSv4NDD77sbwwaiJmEDe3tdeMnutY5O7xzfUj5uCzQSte3DN7X4YIXDRvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q_VjwweNbWLRLaZY57FgDoKpL_augtYMLetgTkLk0ipRDhTQiLypprmlGC-LlfSdNgETvBXfr9H4OZRk4-qpcsCQNa8e0dVGhdL0fZe4zSsoJDn1jrZZGNLxG7I9ZON1-K0-IiRvj6I2gCqt4ToQdZD1oxQDdiDp7SOPgNYXG8wMeMZNj-sTOgRZdxAjOyt4JJRY0CzBwZbCofweJon6gbpm7i58xuMFhQuDYaWM89GvwPVBd5chY-K0nfmPUzOc0YG_Zjsw9xSIu6pOpnI8BwS-mzt3qXFRUH2ZIuT_LqWKZInLeq5U2pK3Zsdd_qdIsTfmvkP3KDrR3n0_MzeOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oPLOh9CxVXHSXubBkpY237oltAHWmc3KYecO5-Eq4A7gaLdyLgVBPtw3FrNmp-ISAT0n_igbzKEd9YNjBztdtql0vTDaUf3M9SVw2J__jpz7qou9tlUyTvF99MN-AcbDm_vzjyKbxZ4X0aC7ZAsC5vwhxB5C0gmBC9f0CkJGrDD6-zrvjLzi7wcpP08vLhvHVso8ZmJd265QoKzaOOvU4ktW1v1TfsEhn8ssG6OgHRphmszksUgeOCwCGccL9L55SoWoEAML6Vov8OCgnaOPCM0jlU5Xey4mGm96Pqgu2G6DFA6bWpnF8yuO_6fKE3KP_sF1taGgqNIU7-IltUNb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ukt5dphlaLhb5VDG82gECgUkz92HkPwxd7ByRg3XlWayMidZgKQ7c6ysyrwK1Lwr7G7iey9Da_l6zX1vmf0rjhgVtZuvgy4x9WA8uHHJReIZwvYSz_6ZpqJpN6I09V3zKmT8voxyEjzXnCeWPA4vFeJNzRErrnFWCnD8J0A_PPSZQm6QgoH4vlhTJRQ-YW_bCGh1-d1651cvB5UkMf3xzwzrNUVjut1jLodNH9JTLk90bdkUuvcYluMet39RFcbDGk9aW_plf-amCCBQVei7C6YplpI_x-x3jN8muG3jQdPs_rGZ6VRVdsp4anmM9Fki_-AfPgU1oRmLYXOjf-R6wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواگردی که توسط ارتش جمهوری اسلامی ایران در نزدیکی تنگه هرمز ساقط شده بود یک موشک فریب آمریکایی ADM-160 بوده است که به اشتباه پهپاد اوربیتر تصور شده بود.
آمریکا با استفاده از موشک MALD به دنبال شناسایی موقعیت سامانه های پدافندی ایرانی است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78471" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R2hFwJPMQ6OMpvCUrUfFuGnWDc9r_LAxY-yJSAPcAFTnrDnnX1kRsfHM_SL6WXSMlz5XUJqiEauLxxS4b8G90ouaonq_MB3KFjLB3MEeaTJQ22k8FoIeNOCRFiME1kW-3TOyQGqR6yz0kjavljBS1a5DtIazGxWqDAziqMLPvCot5-LMkbig9tSs26WFt-4gfTacgVc-HoKgzcAcMr9ML3um_wcn18RT5XVGJI9TId26SUa1hh5_Z1i5N-zYKbbAO_whwMpftMM-451eu2kI1-n4G4ckAn0FLvhmeObAgb7MhP4WY6aEo9tAk8AyZHbnZDMI7ac5UEoXlmB-dkg2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز دوشنبه ۳۰ شهریور، در گفتگو با شبکه خبری «سی‌ان‌بی‌سی» اعلام کرد که فشارها بر جمهوری اسلامی به بالاترین سطح رسیده است و از ۲۳ سپتامبر (اول مهر)، تمامی خطوط هواپیمایی ایران در سراسر جهان متوقف خواهند شد.
بسنت با اشاره به اقدامات جدید وزارت خزانه‌داری از جمله در حوزه‌های هواپیمایی، دریایی، ارزهای دیجیتال و طلا، تصریح کرد که طبق این تصمیم، در صورت نشستن هواپیماهای ایرانی، ارائه سوخت، خدمات فرودگاهی و فروش بلیت به آن‌ها ممنوع خواهد شد و هر نهادی که این مقررات را نقض کند، از سیستم دلاری آمریکا خارج خواهد شد.
او همچنین از برخورد با حامیان مالی و «تسهیل‌گران» منطقه‌ای و بین‌المللی این رژیم خبر داد و افزود که سه بانک از جمله دومین بانک بزرگ مصر (شعبه دبی)، سی‌امین بانک بزرگ ترکیه و دومین بانک بزرگ روسیه به دلیل انتقال میلیاردها دلار به نفع حکومت ایران تحریم شده و فعالیتشان متوقف خواهد شد.
وزیر خزانه‌داری آمریکا تاکید کرد که دولت این کشور با تمام توان در حال بستن منافذ اقتصادی حامی تهران است.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا همچنین گفت مقام‌های چین در گفت‌وگوها درباره کارزار فشار اقتصادی علیه جمهوری اسلامی حضور فعال داشته‌اند.
به گفته او، آمریکا مذاکرات مثبتی با مقام‌های مالی چین درباره رعایت تحریم‌ها علیه جمهوری اسلامی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78470" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-RSIY-00btQLXpCxYel4My281NTDWgm2CYkt7n31dw_Qy3mqb2bb9zmz1IYQ2ANx0bghdsXpgO9uZtmXted7Q70h_S9H-ZOi-9UpuB2uaOB3ZMR8xexPlERvDNoGk2tTg6iZn4S8R6LBUkKn1snvjR7diI-nEXh6sSdr8AUadbvrVZ1Iohabmxb2J_i5Ygrbg3maC-LwKf6F6PZVe24UUt5kwD7UETpQWcHnKO2ey1VrYR7j6oa3jBzJUcqDxbVgLpAMax3IjRQ-0kgwfuGU1nlQEYZeE1BNvq6pskPWPVvsgDRgVeRJTjlmoAXpC64RV3BEesfh0kxRcD7dUMZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه اعلام کرد در واکنش به اقدام حکومت ایران در پلمب یک مرکز آموزش زبان فرانسه که به سفارت این کشور در تهران وابسته بود، سفیر ایران را احضار می‌کند و «اقدامات مقتضی» را انجام خواهد داد.
پاسکال کُنفاورو، سخنگوی وزارت خارجه فرانسه، روز یکشنبه، ۲۹ شهریور، در بیانیه‌ای گفت: «این حمله جدید علیه حضور فرهنگی فرانسه در ایران، پس از تعرض به دو کارمند سفارت فرانسه در ژوئیه گذشته، غیرقابل توجیه و غیرقابل قبول است.»
خبرگزاری نیمه‌رسمی تسنیم روز یکشنبه، ۲۹ شهریور گزارش داد که مقام‌های ایرانی این مرکز آموزش زبان فرانسه را بر اساس دستور قضایی دادستانی تهران تعطیل کرده‌اند.
مقام‌های ایرانی مدعی هستند که این مرکز، با وجود هشدارهای مکرر برای دریافت مجوز، سال‌ها بدون مجوز و تحت پوشش آموزش زبان‌های خارجی فعالیت می‌کرد.
روابط میان دو کشور طی سال‌های گذشته بر سر برنامه هسته‌ای ایران و بازداشت چند شهروند فرانسوی توسط جمهوری اسلامی پرتنش بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78469" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYXt46f8v43WXrWV44jKjQ3GjcbZ68ZB6ufL-SWoc_K_JKIbwxeLIfAvvQ3_nbfvQPG0mNO9Ua_G20lLGjfWzyCOEFXwFlo9Wpr3hYvlBHDfRxMwVA7gXXEcL75cb5PmUc_2RjbFWEp0_Ep0Q5I3ez-Q03pOXgEnGv1oSAj_ciMsRT6VUnjOIZ6rjSyAbPgh81hF0vf5w4z9or28fOrYWlNtvWuk3fh46HRVQ_-JlZlfW0EemizWE7x6qn9SIzHfCHi-REex0y0k2i3adwR_HQsP9ICS8e1diE-4wDJ8-YMAti4UEoyMndrYVUcfOGP7ym9E1zt00KihrZCbSTHwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»، وابسته به سپاه پاسداران، گزارش داده است سفر «محسن نقوی»، وزیر کشور پاکستان، به تهران ارتباطی با انتقال پیام یا میانجی‌گری میان جمهوری اسلامی و آمریکا ندارد؛ روایتی که با گزارش شبکه «الجزیره» درباره هدف این سفر متفاوت است.
تسنیم امروز دوشنبه ۳۰شهریور۱۴۰۵ به نقل از یک منبع مطلع نوشته است که سفر محسن نقوی به ایران در چارچوب همکاری‌های دوجانبه تهران و اسلام‌آباد انجام می‌شود و ارتباطی با مسائل میان جمهوری اسلامی و آمریکا ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78468" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcshpfWkVU4vVhmo3EXP8QNsxnbDCrcDDpKWkWgB-su1dCR7UkALhOxKA0BmPuAPdRkdCOxktcxT9iSaXawQUyX-WhiI3ltWHfje00-8_c0RSAh5mqdssCvi9DsZAG8unEjHDR4iZjt_Bh9Z-37xlCGz-3hCOQagED1bzDnHBI02iYaaX6q9k_QzwqoZuEyR3jyBtW2Cd3Wzwtq91C_Bk7_gou6KxnN0a7eQGHfDvYKnl_sH7k8FeJjVxnOGV0AgZiUIUFvl7rcpiOZhI8XWVgdFxnl8HWCSBAHIdmSp85Wf5pN7jLkE9uAF3kN0Srrda6gXYX7NIkw3XOS7PoA2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌های منتشر شده، امروز دوشنبه ۳۰شهریور۱۴۰۵ یک نفتکش هنگام ورود به تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و دو نفر از خدمه آن زخمی شدند.
«آسوشیتدپرس» به نقل از ارتش بریتانیا گزارش داده که این نفتکش هنگام ورود به تنگه هرمز هدف قرار گرفته و دو خدمه آن جراحات سطحی برداشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78467" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvuaFFM4BeMo5aA7Vyh6WCLUzGSfd8wgaU95Lp4_xq8yzz4APocvuWBrXGeOtXBstA6kYGd9SS2X8fJGlWo9_kiUQs4hqQUDw_WgZ2HtcixGAe_Khn8Ct3B0PFBmNaeMgEgEUg7jgKcivys8Je0TnEhzdSwE9bhQQXJgGYwMndrtI1Nql6usBaw4tHfycDmkONIXMqXVzK-N09pNmn_kYJMgVNEGOnZlxgWs2HOaOvedZusiXjkWjPbRDGAAdSeSU_G4KsFBZmViHMqFs0O1HvjfJ3fqF2qh5FHDhJnDZo8jU8Y9ee12-Up-BjJzWHcfVjBhZDikK7zSjrI0fWVdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_tFBnDOtXasAEOPFkTk0JAjKlZgzhYmdPNc7KtWJuN8j4cq7-Cq8Tv5auAzeoD_gpoVdOSd-Vlw2LGSmQCstK-0nCWdIy_6ETZ-8dK0b_pqHttw6oqdl3vB6O-PPAYVPnFcCDDByX28HqdhsHHLdm9-ypRYdVux5ZZweDs3awv79nho6HqKRnYff4tKmhzPRo7tRUaV6QcvOUrU8cDSldtgWbdc6FaG8QHZ-ErNRaL9ch-b65KRuBw-wQy2pFeqvgjr8n4Y-YFtPb7V8AoVP8riwJXm2aN5z6lSZYzoRX0_Zr7MjeKPzc7BYWQj2Oc3JyIHG0pSS5I27MiTbLbMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-hThjuK3vIjmR47fZumDar8JBru4j4c2HNDXsdlRnDgpeuYRIrkwE8iK8YvbMPXMxaXFMlBH-fcRT4TBj_jfVzDi2NkWgmo1ELF3uIcTTteE8tG1UIMJI-mo9OHqxl3GYYWsh0lYFB_LD503CjGXeFjk1gTa-_bR4wYZQe2raipwQQzw__ajYuDG986t7pMjG7TIUPTMI9aMlxmdcsww1n-QgJ6nESsRM_O4p1Nkb0J0P_wyrddktH735ET-veFx46wX6e1u4MfhlJGpIvxRUFyRG41rOy3DquC77-4h_QQCF3KD1CCDVxik3F0TTtTqDKEp03_2X7oOZbaqz5Lrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCFBtvJqnfyNH5jQmFDBnp_VTC2-MNYNWlBFkLqD32K_WaQ_e0H476PPGBKUPA3PmuSj3A5eEiX__eAJ_vdREDfGmtobrD4AGugWxDe-S7MQeE2EI_64SZn348t_KOPr1X0B4K-ggyQpQsE9OXHTfjwbJ5HWitInMAjbWaOANt57siaKGCV3s_U_nmXglE6EoxoE4fOy3CHGcE2O-E0MwWs6_GIW5MqdmjdQqtreGgwddWrSzEwOfuNrFYMGpqunqBsDkGhs2RXSy2uQCe8syrB7CygyY_fJgbNYUX8RVTUnTgLgND--DavjJ0Qd14gEbEz2CTiPmiWgn8b3A5DgfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
پدر و پسری که قربانی قتل‌های زنجیره‌ای شدند.
🔸
آقای حمید حاجی‌زاده و پسر ۹ ساله‌اش کارون، نیمه شب ۳۱ شهریور ۱۳۷۷ در منزل خود در گلدشت کرمان، به اتفاق با ضربات متعدد چاقو به طرز وحشیانه‌ای به قتل رسیدند. آقای حاجی پور با ۲۷ ضربه چاقو و فرزندش کارون با ۱۰ ضربه چاقو کشته شدند.
🔸
خانواده حاجی‌زاده در تمام این سال‌ها برای روشن شدن حقیقت و پاسخگو کردن عاملان قتل حمید و کارون تلاش کرده‌اند؛ پرونده‌ای که با گذشت نزدیک به سه دهه، همچنان بدون پاسخگویی و اجرای عدالت باقی مانده است.
🔸
سرگذشت کامل حمید حاجی‌زاده و کارون را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-7014/hamid-hajizadeh-pur-hajizadeh
https://www.iranrights.org/fa/memorial/story/-7010/karun-hajizadeh-pur-hajizadeh
@IranRights</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78463" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnILE1hODrq8fnmeZ65VDlA52yaZGpW5t3lhBxjseUSOlpk39lnmtLu_OFWN0wkbcKEEw1LMDyBqFLMTM_NkVpJqXKUNpTpQrhXZewmbPRFbBfhp_X01i6wkq_SU2TQTRrKP3j8yzT7vk5xfQ5Kb0RXj64Ijv4hUFahlYDi-YCxUHP0LLYFKKQnEv17VCLvPO3i9mj92Z7MiXdBXGI1P3mt0vqVG-w9oukgWEPDmZ4ZMpQdUYFNDELL_aQSj8SPsmTdW7-fBc-rH25Myf7ZahMw-5CJzjif_J40prgAYTfeah5J2outGYf5jVBNcFIJ-TnmT38P5qL5Ijfx77Drgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار ایران روز یکشنبه ۲۹ شهریور نرخ رشد اقتصادی سه ماه ابتدایی سال جاری را منفی ۱۰.۱ درصد اعلام کرد.
بر اساس گزارش این مرکز که در خبرگزاری جمهوری اسلامی، ایرنا، بازتاب یافته است، تولید ناخالص داخلی کشور در این سه ماه ۲۱ هزار و ۷۹۵ میلیارد ریال بوده که نسبت به مدت مشابه سال قبل که ۲۴ هزار و ۲۵۵ میلیارد ریال بوده، بیش از ده درصد کمتر شده است.
کاهش قابل توجه رشد اقتصادی ایران در حالی است که نرخ رشد تورم در کشور نیز به شدت افزایش یافته و بر اساس آخرین آمار اعلام‌شده به حدود ۸۰ درصد رسیده است.
از سوی دیگر ارزش پول ملی ایران نیز در شهریور ماه به شکل مداوم کم شد و قیمت دلار آمریکا رکوردهای تازه‌ای را ثبت کرد و از سوی دیگر مقام‌های ارشد دولت نیز از محدودیت شدید در صادرات و واردت و کسری انرژی خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78462" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNBdQeV_807Iw8voeuNWuTlqdTi4xRLN90f22hTPJ9jKGb331AVdehUgCaHGjxoFtmeob8evpx41RlrwCLEtQ8MgMvfdIXmkCdGMwQw7cdUTCzi3KwoZvu04vcFIsakKMnEKADlxdkADkle-O3BDrjpaVXmkhSvuQmpzG-A9pqmgstF6_88JiFWQOWk268O2RRjNGae2oEr4NzLTXDSbmPL9zyWoJe15Dv6jBiqhh_7p6bcxhvki7y3MRvlpyBxZb45vCTq8OLkm94ZQXgE_HNgY0ZA_utjjPgCnKokvnY4xEF10-GQ-C6JFEjtv-Q3VVyCJDucKZwz_zHR4I2JI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید موسی شبیری زنجانی، از مراجع تقلید شیعه، یک‌شنبه ۳۰ شهریور در قم درگذشت. خبرگزاری فارس گزارش داد او از روز جمعه به دلیل خون‌ریزی معده و عارضه ریوی در بیمارستان بستری بود.
شبیری زنجانی متولد ۱۱ اسفند ۱۳۰۶ بود و در سال ۱۳۷۳، پس از درگذشت محمدعلی اراکی، از سوی جامعه مدرسین حوزه علمیه قم به عنوان یکی از هفت مرجع تقلید مورد تایید حکومت معرفی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78461" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=A5yBlbNdDjxDf88O5KJnChcNfD-ArkiX67SqR4_7bg8lvMvEIlp4XLzGxlMjECM2JEAvn9B1RcTOtY6sJKo43UyawLP9-2bbTLvo-5mRIiP31uBmjSpioRGIInY6a_nJrUUIP8jnkrJ4kX7hYAYdoMjG4AoCvVdyC3Vqn8__rB1df8fknxWpJS3jCdCZmCuJUSR7GNNl8dlFPSE717o0ffFdOCCQS7l2j_vH3QT002sXXhal5_MV6FXxDWDHKiARpTIRKYZdozYpEqrKuXHCKgJVGudaGujZKtmazlBOWFQCqHa3TqvuVFpCDSL0DDbVsdXbn1nd1LbVqm-OtQRvpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=A5yBlbNdDjxDf88O5KJnChcNfD-ArkiX67SqR4_7bg8lvMvEIlp4XLzGxlMjECM2JEAvn9B1RcTOtY6sJKo43UyawLP9-2bbTLvo-5mRIiP31uBmjSpioRGIInY6a_nJrUUIP8jnkrJ4kX7hYAYdoMjG4AoCvVdyC3Vqn8__rB1df8fknxWpJS3jCdCZmCuJUSR7GNNl8dlFPSE717o0ffFdOCCQS7l2j_vH3QT002sXXhal5_MV6FXxDWDHKiARpTIRKYZdozYpEqrKuXHCKgJVGudaGujZKtmazlBOWFQCqHa3TqvuVFpCDSL0DDbVsdXbn1nd1LbVqm-OtQRvpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANv00QuX0p45fM-iJzGsOPir-LG9oyRAzDq4TU-aEY5a6n0UnFRCrnDAalt7f6J2gWQOUtUScJ3U4i1rbTX3XWccWqWiiLdAqq7HyVgefVa8zQgamSlC61TYtbAF8koy_LxlkQ43C51HucFJ8fioSci1BmqopjdaLPhP4NVFwxgUu-9f7LeCiUPYDjdWfF8jiSZJtLFvvusnccpvB4taIBLFI1Wp212DDZi7XC7e35GIMCMKRie0bfq4e_v8AobXsubijJs3lUfNdGPWs-z3qwXUtZzy8Ec7CtOo8J3hI9U1JAZvnbXABPWGyaJM_B-GfM9NTJb2F9BVUuw7cKNjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfA7Znca5zKFGbxzG02HfN_jY5YN-E2Blm1wPG_F4__3h3YmgocG-mttv18te5QnxccdRpeN7Ei_f3WW-RghHjzHOSxh0dWT2iXtp9U-lVOGSpTPEErvr1_dDYqCcjpYbkL73WigutPEr5dummnAuXF-VoFjnY37HLK6ytRTYdCJspvJyRWwMamdXrxI88rGpldwiJ4YJUdCMJJEmtDWYoPJe_iHmrvmX89PLujDxax41KPpC0lChatjZs271Gji_dtGXC93qyduQEgP4-HLYq4iSdIi5kJxBnmig9N9l_MsYn4cS-QeKb4JDcg7Bw7C20qc1iyyaPmEP_aM5vSfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJRFLWb5jm_FVap4P__uFqMcKNXPlpPaGNQvKXQTsEPS_p2-96oh6ysCAb1gK2LjcgphaJDNvSWoZNc-tBqAwZyHnP-wukv0_p1Jgl2sS-HH9HrdznZJUPvjQBjNxfOjNQIE6uPTs_aegCNVQzEr-WML4Iexova8lcyId0LJXCFImJIz9EgjIKXYXs_FHRMjJeBx3OuTe3wD7-kjCLbjQrsC1csEy7WvRw9M7CmXQa0Pe-d5saVJY5UiHWZVIAx5g1HYjwCTxHtTLOxnCRIuWLa1fjuaCDF2PqItFgL0D6f9ECBBDPwTk6nNtCsypCFIfXIE31U13cIxVn0ugUy-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoceogVNPHmaoEeW15LnMaxGwLeqxPNlS4wqakx1t42vG_2-JGf-Vpo5fq_l8OaznnnHrMyR3LqIbzbDp4mSLRLzinyPVjxxIq3xQ3evqp7fx6teC92yRYwT6yd7396nG_NELsCq7GsiQi0zlIcxT3hPXaTeDobPXYYdDUuaCWebSB7qryRMqL4l4-graGeWpkEPhTv2YXNAB8GD8866ow4hykISMvlVtXP2ysj1QSFx0pKxS6QvMDaX3COLcQLqM3AqZQ6izA4xGYaEIAVOyth1SIvvvHLwsQtx6FIZK_l9W0PBR4IjCi4zxOXCt8xc-PzCY20eT4OwA0t4vVhZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=Y-oU9wKlttnBCCM5WUk4sDJS6Alu12drHGXQaYGtVotqT-P2p3JoC7oshEz1CDKpGHtRfSQs4f-CvDINNvsIYcQlfdXREgtDGYO7Bml-WUQ5l592P1MtoD1AYQNhAApme2k2RqNNlgYNTiUwFnbRLwz9dR7tiXtLkO9OHxELqBRw6b-m61-tlQhg4wp6yDPIcAj22n__CY_xDl6gcf8rk9aeXcDZH6sjntX3vHQr8gPvsjSlvmGB1SR5TgHBluwFwmHzoHpYuSccMSIxYcMXfcnk6zV74PR_VB7cSBzxiu2PnvK2k2Uu8qCBoGszHoiI06M7l-zOYutU1XapRvtCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=Y-oU9wKlttnBCCM5WUk4sDJS6Alu12drHGXQaYGtVotqT-P2p3JoC7oshEz1CDKpGHtRfSQs4f-CvDINNvsIYcQlfdXREgtDGYO7Bml-WUQ5l592P1MtoD1AYQNhAApme2k2RqNNlgYNTiUwFnbRLwz9dR7tiXtLkO9OHxELqBRw6b-m61-tlQhg4wp6yDPIcAj22n__CY_xDl6gcf8rk9aeXcDZH6sjntX3vHQr8gPvsjSlvmGB1SR5TgHBluwFwmHzoHpYuSccMSIxYcMXfcnk6zV74PR_VB7cSBzxiu2PnvK2k2Uu8qCBoGszHoiI06M7l-zOYutU1XapRvtCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfqb7ZozWEB0SUgjDn697CBnBU6uLryeRCOqbSjfMFqONkeQppoIcuA0iiCxAmgDwfIhO5QjP9bxNLuwzHRb85uQQQnCSNVuLg64s7mzJjheUaNkam11xrVY77ifizaAJ3857EB1pfaDmOjuiIdjPDggj0o7owITeZgAjKiH5D40RPNGs3WEhLFAw-2T2YbhLhkawyxbdn6GBK0b6i0YyKbRnwWSNmyjrrwdRa7bMNs5qt7zGNbo7U-xvYwVvTWTwy78F8SrT9mLjxdZpVYfpSI02teaBPzbumtZoH4QG6mIFK8vWQHZ7JPQNsvBNpUQdMhCMGbX9U2Qiv0-BEuO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WNsZvwfVlisjApFTOgdJSb0i5a3x23PXo3i_lndfurzO9IwPaNq8_6cI22SpcNt9zHp5HJMLqTlYg5JQboRFg76tTtA9jdhd0vLf4CQhDUyxw2-otIaeRsTzt9GJXV-bfxFYgznEa0OLufGu2AnoURDWTj9Um8AVAWVKfzXy0aBG_NaGPHXcsnB5MShEZZyQZEAuQ515a7SDO7riw_iW9-go9_F7de7qx8XJZDENg-5Z9XLn0RDOLOrtIOiEHMC5geo6yniMdco-wKKjEVS8CTn34aZ9rcJ8HIkAtpgyawIjDtoO08zTr45TARyIVpasrHhhNyFoh7YwtxAixWnJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=Mag1AjXtHxqLPVI_G6PM4I6mZ-l6NXDzM-0OAVMDSC-G5dSLWFMU89cBrvMtPMWuPg5HnKag4K6osPI8s1jDQlHrCtnd_0nlxZnEplgsVMLi4zUxSPfLaiBIfcSOeXbdq4XajxdJvHyW-nX1zRM9ulB9WI-U7gkbm_x86yIPSGjAbjExbzdoUkzl7vbOWO-rcvLsPZjW9pdHXQtzYFktqnIlmMyJV6vBiziD1CRAGli6VnFdOkcEs0Ss7Q5xU7WoZwZbOoMnfi1BjQdXOok5P9VTt1aCH1KcAd1O2Srz0gNostIbHvMWBhni3tCw2zckxGxAq8fRA8JtseCgcjscQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=Mag1AjXtHxqLPVI_G6PM4I6mZ-l6NXDzM-0OAVMDSC-G5dSLWFMU89cBrvMtPMWuPg5HnKag4K6osPI8s1jDQlHrCtnd_0nlxZnEplgsVMLi4zUxSPfLaiBIfcSOeXbdq4XajxdJvHyW-nX1zRM9ulB9WI-U7gkbm_x86yIPSGjAbjExbzdoUkzl7vbOWO-rcvLsPZjW9pdHXQtzYFktqnIlmMyJV6vBiziD1CRAGli6VnFdOkcEs0Ss7Q5xU7WoZwZbOoMnfi1BjQdXOok5P9VTt1aCH1KcAd1O2Srz0gNostIbHvMWBhni3tCw2zckxGxAq8fRA8JtseCgcjscQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQIgLS5v1mj9UcKDy6PiH-jE0Pmudm-4WQMZHHtLSLN8T0mHxrKvEBa6E7WG59UIpTjivQlipA2bJjqeXj9LUBX81IDyPyqjpNMH0nkUmAmpndJXEcGVxQ5UG3DG9mwCNjLAyZBc7Q8laH02j7Bfl6LTbhWHnnmUu8O3GfhX3ZTXiDCxR-jf7N9D3IW3HdYMXuYYMb67HyslC1he3oLe7njJ854_GN2c2BsS6lGlm_2FTl4L3Z8WaUvvf94RVVCSbU8yCZtjqfniXsSGEL4FeXS719izOZpar-6Q9_wimXCLoHNJcr0Qa_PrpAKRpSOFnfBMcR53-gY6XPtYM9D__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmmiKDXBm88g9WfILigOGKxZi9YFqZ-tqOtQyiuUbGAvRXQuSqfh2IRTozGsWIvi2oPpDVEaJKJ62SjlHKIpUs9jU7rlNwdYaggH-i_s4tSpPvvtGDOxuJ9GxILR1p85VJHwUpJaBEtfgtowzw4ujuMLFsbNjWXVzzTqQ5HmKJu8-0m3sO7sm1ilJlZ6umZH0GO7SKMLoHRe94lN5bQTb1HzFkUKhyVwUwG1TtkjSQsrihdiv7yLc7tuil7tti4k5ANQTHRaylMB8pA-XPEcK5cJRTRq936GzY9HZGqa2aN0bEcTRavdy6RW9IQ76ULu4m8kzFhTsbsptsSMUYO2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwhqgiG3b-Hceff_heMHfUDaFuXiXKh4ODMbdqQG_iFD3shKZBRi7HDm3Qn511BTCAQgcUaLDu4Mcdnuer_TxG-0JpZfZtjMaEdXZTEG6mH7HEaHZo-m4u9Sb5LS7_5r85eP9_oc_2mrRBbefyvr2t4c2L9efWC8TLRwoHFdLkMtWpykIvRR-XvCo--j0xGtLqX5UMYcFMnn5Wqvs5Dsy68mVFle5B3OZtZBnkp5XYM1SE4kLyWBXG7kxLHMgckgkQCOCVUgVHHyANQjX5bvWJePN8StitJBgmeiQ0Id-75nxX_2tyxSN83ZS_SunHhEgAEdlqUHSizPZim-0ev2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLa2cIhHC_T20_HjaR1wCKQOevC6XZbvtIoxOfX14X6vxy38PzACG8z5xVlbowx4JFkiuVbqSdaRaTKQnRBvvWG4wfMQt3OahKU8CyHRtJoHDlS0aQY4sg5XQvdZGQuESrdwAtECiXdNbdgJM4i1RKra_Xqu3N4yJOcE91xx0Agjzv-G1vU8pfiR7Ti-7kn71tgb9rd6qHD7nuCFkhk6pyJE89oOf0Ee-ca75BxDamToj-pVVRzwPXed18_kb9dhg0P-CzAFMQMER9e1uL3heeGoscsKJ-71g_uoamkDTjd1HwJtnpYoI-Jn2fKBCjpXr595lieAyZxzWZGkrs3WNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhM-8QxsTqMCue0CRRadSwcwXbJZw7qlhNCzawNNK5qUY30Ts2gx200hgN7Iqk4cFrE8mOKtNtc5oFj2XGW1ZhocASsEqvhGMQkhbFYegFJY7e5FyGMrF1XUn4Mc0JCp7e5ZHl8b2hEzsdBSe2pMgVYZVAlb5CU4GFycXA3Ok7uhaJHsGYR8Ge6wB5FODOH2jTJK8bjsDtqLygpj32O0MC_9EVn4spXEWwS5ojDYrqsALS2dBPD1nsPkE2Tzz3EJDO_mQXrwyu27IRmlGtAgE0JoXLl3AaIEyBQVMTWYgfeWnd2I78_8aG089zjsXEtHpE8R0Kea-M2o8ng6UW8xgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=BhLG7605f8qPeDHUoFEPrYwPWfe-JI6M9pJaU6McSwIbUgICKApzkkmY63VwU6dqOcf5nMKjYJhnquMA0IndPkFhJieCqJXQB14Co2sBbmuuWT-OxUwlHnT58blA8mqVew5s87Un3ZekG-9hXBKzz8hXWDjptQbMA-Gb9RcaX1yEdKv5dfnwzK4zOMJfS20PneBFYTQYyBiE5F115Fo4TzZOuELK05xAWwp51Y7iPPDYrBeDZEckMNtGeHco4BJwBFvfE0WX2Ywmv3kvDXnyEPIz5bHT9bedM7ivu9Z0gy9SGxSOnUJdzRbemw021cNUn58NfKwandlS5vyxok_viA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=BhLG7605f8qPeDHUoFEPrYwPWfe-JI6M9pJaU6McSwIbUgICKApzkkmY63VwU6dqOcf5nMKjYJhnquMA0IndPkFhJieCqJXQB14Co2sBbmuuWT-OxUwlHnT58blA8mqVew5s87Un3ZekG-9hXBKzz8hXWDjptQbMA-Gb9RcaX1yEdKv5dfnwzK4zOMJfS20PneBFYTQYyBiE5F115Fo4TzZOuELK05xAWwp51Y7iPPDYrBeDZEckMNtGeHco4BJwBFvfE0WX2Ywmv3kvDXnyEPIz5bHT9bedM7ivu9Z0gy9SGxSOnUJdzRbemw021cNUn58NfKwandlS5vyxok_viA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=iKyvYy_P0r03qlHigXnqRNUuIEllV7zUAwF_SKwzscgqdEPU9faO2EHMdVHwETXQg9i5HIu8kMnNrgf-Gdv8b4yoTe6wXAE7jYvLatYcs8lbzQi_o8jpx2TmUjFLUS5XdNwnUMDZkX2ePkE0Yqxn7ZdEA2GRvSGO5qENAJNiD_kNaicSDn-IRZIooUVqjKh8h4O0v0TDBLRGsny7PgJ8kwetiDwpLJXqrkN3yH4k34aqIIGhQ-qlahC7pfg9FudXRmvaH_3D-0lgPV68JJg1SbEjXbKYuUB7c5ZqW3Vge_fWPpsg2tayVA9NHq0BcahoBdndRjGyBJ6Na4N8Q81Dbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=iKyvYy_P0r03qlHigXnqRNUuIEllV7zUAwF_SKwzscgqdEPU9faO2EHMdVHwETXQg9i5HIu8kMnNrgf-Gdv8b4yoTe6wXAE7jYvLatYcs8lbzQi_o8jpx2TmUjFLUS5XdNwnUMDZkX2ePkE0Yqxn7ZdEA2GRvSGO5qENAJNiD_kNaicSDn-IRZIooUVqjKh8h4O0v0TDBLRGsny7PgJ8kwetiDwpLJXqrkN3yH4k34aqIIGhQ-qlahC7pfg9FudXRmvaH_3D-0lgPV68JJg1SbEjXbKYuUB7c5ZqW3Vge_fWPpsg2tayVA9NHq0BcahoBdndRjGyBJ6Na4N8Q81Dbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jpe_JmHOIF-8-KU1GAf3ovbUsAoGDAdCO-0ejxnwnOsZKt64Oa3a1L0Uc1k7CXHulkGBWtp3EiMYJ5WmUnM67PhC-iJXBDh6A-DK-L1ys7nhCO7XZanX24M6CfOxiVlDPdhNXNJirsSuB0KOS1uMUAnFvhMM0Jsbul4G5xdUPoWq_TGCkuxh-od_UGNHr1pwkRnpgTirkcjV8piSUV7HAyhzD82REl2CGGxeIQ1dtkIF43EfLVvFDQX5jQ-j2G329wPGkcpWtGOGrR8kk7TNxu4ltEEJgfAj61v4BkRqGKf1g1ylJGBIwl7eCV70IWuKRhYCcIL__LdwPb7kTndE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FmAScflVHLKozis967kOBpR0QkkvXBfQgKw29yUTNeLMmrNlb7_aWHiKdu8R9jksv9-0KpqBzd6adOv-jgOHlcKadw9Mwl6prIpfMDkPSz6R2PG8Hr9pXAopijEbJLqAMSUSUL9KshyyMSDyBHHVRhlkviotstwTE4rYNELI3CLr--x3m4DbNsOJ0JCApGNqq4Gkqr7mbhSvbRTcWslJeocxtgp-fdlUarUEQGg48RQOuerLVomv29Oca0oFiWrR1h9Vr6KHK68LBCP30KnRjzBz_Ivo2QY8TNIiypns5Z9oWMrodBi_JuenmAnfN6n1BIEHwkbOnA79OMwX23PjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/awbyjXPjLKlhlFw5xGslXzxb-S8CJj_2b6VUllUdYrclqbjd0dF1G6Gvimq6PKmz5vUFUck7TU5E4adMmjJkSDaKpRhn_kljLFWiKUK8wsJ-2Z19k_MgSWwv2Dr1-IuvfpWZfEmIyTKCyUZJobcsJ4-apqG9uNvvAWg5hZRIGWCwrxIcWk8z0iJwwgg7Eb-5fF-2Bayk2FUQrlFyrTv6prp35FzJeRjZ7ZnXmrcQIaOz4VPnTqys2sUPLaYuCFTtt1LA2OMDt9_UIzVqd_fW58uu_s_3YlF5vb1bT_RXLR6OOMuzf7nMIVLahReMbID6P1daevX8d5cjON0SQDyAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UjTnJyXu47NItqjsyQvtbXnDubzuTeqDKGF2Ad9Y1iHu7Xq_anSmyUfbg3cEZTyMG7FiNmVcEEKMFyfk4uXObIYiKwmUkvJnNYc0R0cbAREvfYeV-t6jFQUmL2V6EXPGaQo5Tan9flJb9PB1KIFJDj90aGgQs852nK4puLv6XkUwnTNkwGciDkbkRtshKlNVaDQxRx2An90sxyw3jlwMzBYMSPP-acEc1SSywvb31smYIbvEB0RcCrzqvO18SXWb-affvTqAmVofzslTUwNLXOMmRviWBvthF8ctJgIqNdNQNCjnTFAi-w96xVZQi64OAo6oK9DEBMRGN1CuimRLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IT2Qg1sL929-Bcy3O42MDhQjsidC2fwCtVBV700NOfSbOrpy7gCz7v9Hi6r_pFPg2YYdHK9sexZgRNYpZeMniyVsedlJb1A09WTJ6kPjHwL0339lD_rV3PzXs8nTSdjfuqVIt83zBOosrNe6uq8kPr5FraDOa9yJKGCxUAPDP9CZ1FJXWNBiTWFm7VtfHrl2WdCBgbdMmRWHK2AEPt2_mBiJHfoCS0zan9rm4Vj0S8TJHu858lPEf0A1AEKXio_eR4R6kjgu6ip2hzbMYfcMdtCgwksEGcZRyiD3rZqqrSDJg8SRcJJxlNtwrnf6G3XUWTNAZRfMoPVsuuXwyYkIpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=tYE4PeP_uAXFrLHTFZYVfFF8sSc_lMUmQnp9ZqEwiFfxIKnTWKSV1uN6vcmcANurxnqWlrh4J7iymsh3EFqoFnPWLIRcDvIHFfoGdpByT1XH6wCfQN3H10JWPA_n4k55wW-m7zQctxBmaRZl0M5PoLQ6zGuz5WFimcTToMJwKw9jpI_-ir1QvxoWSVOXbc8zSYgR73_sJpPqfK8nyLUGClcClO9n3JhFVoCWA_aV2mErgGWispZcJijrc0GX71p914ARN4eRXWxjNkSaRZ2aQso6ewChgkNmZM6eYx4dM1HPB6O6xQQraC7_ISYKVywBYsCR8qUT5rNf5DO7RT3ZTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=tYE4PeP_uAXFrLHTFZYVfFF8sSc_lMUmQnp9ZqEwiFfxIKnTWKSV1uN6vcmcANurxnqWlrh4J7iymsh3EFqoFnPWLIRcDvIHFfoGdpByT1XH6wCfQN3H10JWPA_n4k55wW-m7zQctxBmaRZl0M5PoLQ6zGuz5WFimcTToMJwKw9jpI_-ir1QvxoWSVOXbc8zSYgR73_sJpPqfK8nyLUGClcClO9n3JhFVoCWA_aV2mErgGWispZcJijrc0GX71p914ARN4eRXWxjNkSaRZ2aQso6ewChgkNmZM6eYx4dM1HPB6O6xQQraC7_ISYKVywBYsCR8qUT5rNf5DO7RT3ZTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6LA7QAWr5OT9ymT_xx7WzuGgpl9lJSbZl4rmfaVcBQkiydn3rVP51ctV6wpoT5w6aqpnnW6BSwbWORPDZCjZH5pMyOLBR8Rd2BQ3GralNv4eK3yS51gyCBHGGbOvnOxOUkgHpGWWTtz8evKndsJtD7_x1n4KdD7z6MuDgUO87aOWPlwUihhT9lT140J5QQ9ft0WLxzUptRiUfNcM17RKgNoJe_YLLwUGaDS_Ab9GmcEN567sPwNpunPEkZLdWIelAuLz7xlbl8tm9MUDkWGiicntyNolg-WikEHxMaZl25cMOo63GM4L83FK0wCVfj7akF2CbcMhl6ypALXGnG0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J2tOt0Pmltfnfi20Z-tlbUZakXmUhw_rBAM_YQarFg3CoQk75-lIsEq6uG3bdpglfZQAJEnLSFbMD9zCU--uILJZqtWQEhZI0xz8TN-0Oj7pRYuI2hEVugKSWwxGJKsReJnavVOkKFmmlNsM6wdYeqFcI1l6NKTpWdnRfptHFEcg9CE0BSn0dDDbRxhr-CepGJoSFAoLZht4OpJyEAHgcGxQqKH_6fzB1HDnTKAkhoj_ytr-iE_SrK5CamwM9FQ-8ESdQSz8ibMPBjyYgms31wx8KbzUByUqjRiE1n3AfHaB-7kE_ACj1nSe4YOu-2Jx_QK3hucL_YFytwTbiDshhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLKxEV5lYcQXiVrOAi1Dei7S0qqkOHDQD-wgGy5UNiBOGPbDHcU_3ygojV7HVQlnzkthHCfBngw8B910Omo4n-lDT9M0zGFbcDLj1ieoAZWsBebt2ofoo5Qzo1taR-NPjylmVnUP0JfsdkJLVdA_CWPr1eVsTdwK-rJFw7b8uwQPeG9nzn_iTBxRiaru7BhLaqBAxqGyWGRMseaQ8oSWtFCC6JzRquNQIBg94G05eM9Zs1zHhJSzVMx8LHIBKrfZOkU1JHmD8_pWEXUYcvoLLf6DIwwHttm2v08pQcuODQlnoXC6a1S7NNH0IaT8dtHNr9I864-UNavKfHn5A80Ptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pC_CNNp0_G4jIS1ynjfHPWPO8WWZhdfyy5hTu6Nm8nyH7wc33X_K67crY462Qo6foeWRrgfAcXVWnzZgVDkFuGJ8cU1LanZGU9s6w0Ja3lcma-r1Q42U0rii9gr3xmvm17NGf-ErBX0IWiMHkFR74TDpIuN6BZmEY5RT0Ho65FljzU6qxYxrW_aY63Jo9WNtqIY-9-IkXARc0Co44meGumyZoPbM0Q45Vq_Dl3Z25r0f-Yi3oYwRVqDA6EBLxHbqpwL56Nsqktw57MTIBsE9Uo6PejPOMBv49nhOfo5F30hmlwzjdkyWNDQbLU2cGPmIg87_vbyypk2zDX7ULKn1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=Ql-am75hw_hyCtpVbjCYcVbrFAdhp8n9UQ2zKzRgQUZbVa1R2wacjMs9nG5VK8XICvwrCMNff7sw_ypCbh0sgjMDIg9MhwfIfyAln9qmNacMI9ug8bxGn71XoSXp4-V44XcIDC3eTCUZooxrwJJ0bALM77vTMkdkYRMK-0nSS6_mDvW_x8pEPeuw8zZKOxEy3FForbwj0a7DsIBs8DpePCtUUsrQo1WesVPzAtR_lyymBIIcLE1Vn2mVE-l9nEPUuB-p_h2NEowfG6WSf5BaAFsVrpuHEs58qE_qNMu2JNFvxlj-EApAzDgHwWBZnVh4yBj1K5WnJKXd6WimB1OC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=Ql-am75hw_hyCtpVbjCYcVbrFAdhp8n9UQ2zKzRgQUZbVa1R2wacjMs9nG5VK8XICvwrCMNff7sw_ypCbh0sgjMDIg9MhwfIfyAln9qmNacMI9ug8bxGn71XoSXp4-V44XcIDC3eTCUZooxrwJJ0bALM77vTMkdkYRMK-0nSS6_mDvW_x8pEPeuw8zZKOxEy3FForbwj0a7DsIBs8DpePCtUUsrQo1WesVPzAtR_lyymBIIcLE1Vn2mVE-l9nEPUuB-p_h2NEowfG6WSf5BaAFsVrpuHEs58qE_qNMu2JNFvxlj-EApAzDgHwWBZnVh4yBj1K5WnJKXd6WimB1OC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU0y9_uO2d2CrkSivKdqQr5bxlXjahNOsO5CAzzL59Pt2J5ZnI629vcc1LAcmMUkKgtkpgQrsQcNRwFJHXKVPkxfY2QR-qEWrCKTniIJdt7Bap77m8d-4eE6tNWyEPewQpL-7srhY1Y8YF2XNa_WRNk1OlTUBV7Xn8wOehIP3-FQDD1pMIV8MPsEnnYcrk3npJGFDxoTqIZeXUoePBStDrqfzx0hOh1wJvL4dH0ZbldAihNfLTL6Nc-RPywzpsp8Nd4C1tsXHKeUdkLyi7khSFjsa-WHs41TA-daLTZWpMH5ONym9d9UQZ60SL7LsuEpFHtjlGy2WObzHn1lJ-DkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IN7ZrRzcw39Uyx38glhrsaes4kBQ8cXKQfYzDMnBxBzFljtZuinXh1QhL5Y0JngrRH8ZmUE1P4Wfl5OC00jqCY6hS5h6rgS4wE9UOfQt84hIubqTDQlX0ivlAZqKSc1tdPjU5835zqxcy4NEVo20BQeuLHttijnQvnj2DUf1PtL8pzFP9OIAPzL3c3ANy_ojn78P11yTdG2GWw0JLAf2kgqxHxOCNXtwuiXK7kIfCUEoXZVlX0YP-1SOtRh-hlnGdbBGpjpwTsLH3nh2bRO9AXrRfPHdVhy__oX4cQdFwB2OqqKp0tvh5SYqRJ4pt8fWN0evp6hB7fKQceXlRWx7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78423">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bvMj0ZSmJonnDmrexg1BL5LK_9HuoZGwhWg186he4lq8xYyCM8u6D3t0Uxz2-kj7hSpM2fdP7fxCcPWvX8XhQjru9dsIFZa5ND4ukli-SNBHrmGK7SwOulE-SnB7szAF-OzhwNrhJXF_gbCApnRYda1pw-h6qnbsTyi1WOX0MHsSXM1N21qTMrMHwdC7h8xTXrUewo6XBWgQFVkJCaSdEaCdo92D49D6STYa5HhpyrFgt9BrnlNLcpCEi9XoYaDHulIjPWMEwpwKjN-HwmLYjjVVsh9I8AuS7FMnCxeHIgGtUw3u7H31weFaRUoJ2jxHfSdS-WNPnTPylh0SY6970g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به اکسیوس می‌گوید در جنگ ایران به یک دوراهی بزرگ نزدیک می‌شود
ترجمه ماشین:
رئیس‌جمهور ترامپ روز پنج‌شنبه به اکسیوس گفت که در جنگ ایران به نقطه‌ای حساس نزدیک می‌شود و باید تصمیم بگیرد آیا برای پایان دادن به درگیری، حملات گسترده را از سر بگیرد یا نه.
▪️
«تصمیم بزرگی پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر اتفاقی ممکن است برای من بیفتد.»
چرا مهم است:
اگرچه ترامپ پیش از این نیز تهدیدهای مشابهی مطرح کرده، اظهارات تازه او در آستانه دیداری برنامه‌ریزی‌شده در روز سه‌شنبه با رهبران شش کشور خلیج فارس در حاشیه مجمع عمومی سازمان ملل متحد در نیویورک بیان شده است.
▪️
این دیدار می‌تواند مرحله بعدی جنگ را شکل دهد، از جمله اینکه آیا بار دیگر برای دیپلماسی تلاش شود یا اقدامات نظامی تشدید شود. اگر ترامپ بخواهد عملیات رزمی گسترده را از سر بگیرد، به همراهی متحدان منطقه‌ای خود نیاز خواهد داشت.
▪️
رئیس‌جمهور در روزهای اخیر چند بار گفته است که جنگ به‌زودی پایان خواهد یافت. برخی مقام‌های آمریکایی هشدار می‌دهند که این درگیری به بن‌بستی ناپایدار و «نه جنگ، نه صلح» رسیده است و معتقدند اگر تا آن زمان توافقی حاصل نشود، ترامپ ممکن است پس از انتخابات میان‌دوره‌ای دوباره به عملیات رزمی گسترده روی آورد.
آنچه او می‌گوید:
ترامپ در این مصاحبه روشن کرد که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای درباره گام‌های بعدی جنگ استفاده کند.
▪️
ترامپ گفت: «می‌خواهم بفهمم در چه وضعیتی هستند و اوضاعشان چطور است. ما خیلی از آن‌ها محافظت کرده‌ایم.»
▪️
کشورهای شرکت‌کننده عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان هستند.
▪️
ترامپ از گفتن اینکه تصمیمش درباره مسیر پیش رو را قبل یا بعد از انتخابات میان‌دوره‌ای خواهد گرفت، خودداری کرد.
زمینه خبر:
در اوایل اوت، ترامپ پس از آن از ازسرگیری عملیات رزمی گسترده خودداری کرد که عربستان سعودی و قطر ابراز نگرانی کردند ایران در اقدامی تلافی‌جویانه تأسیسات نفت و گاز عربستان را بمباران کند.
▪️
از آن زمان، ترامپ رویکردی «کم‌سروصدا» در پیش گرفته است: تعلیق مذاکرات با ایران، آغاز کارزار تازه تحریم‌های اقتصادی، ادامه محاصره دریایی بنادر ایران و متمرکز کردن ارتش آمریکا بر بازگشایی تنگه هرمز و افزایش جریان نفت به بازار جهانی انرژی.
▪️
ارتش آمریکا عبور نفتکش‌ها و کشتی‌های حامل گاز از تنگه را به‌طور قابل‌توجهی افزایش داده است. با این حال، ترافیک همچنان پایین‌تر از سطح پیش از جنگ است و قیمت نفت نیز همچنان بالاست.
وضعیت فعلی:
به گفته مقام‌های آمریکایی، ترامپ و پیت هگست، وزیر دفاع، به ارتش دستور داده‌اند سطح نیروهای خود در خاورمیانه را تا پایان سال حفظ کند تا برای احتمال بازگشت به نبرد تمام‌عیار آماده بماند.
▪️
این مقام‌ها می‌گویند ترامپ باید به‌زودی درباره مسیر پیش رو تصمیم بگیرد، بخشی از دلیل آن این است که ارتش آمریکا نمی‌تواند خیلی بیشتر در وضعیت فعلیِ انتظار باقی بماند. یکی از این مقام‌ها گفت: «بالاخره در مقطعی باید تصمیم بگیرید که هدف نهایی چیست.»
▪️
ترامپ به اکسیوس گفت از اینکه محاصره دریایی مانع صادرات نفت ایران شده، بسیار راضی است. او گفت: «از وقتی شروع کردیم، حتی یک کشتی هم به ایران نرفته است. تلاش کردند و ما آن‌ها را منفجر کردیم.»
▪️
رئیس‌جمهور افزود که ایران مستقیماً با آمریکا در تماس است و گفت ایرانی‌ها همچنان خواهان دستیابی به توافق هستند.
تصویر کلی:
کاخ سفید همچنین در حال کار روی یک راهبرد پس از جنگ است که خواستار تلاشی منطقه‌ای برای مهار ایران و هم‌زمان گسترش عادی‌سازی روابط میان اسرائیل و همسایگانش است.
▪️
هرچند این طرح هنوز در مراحل ابتدایی تدوین قرار دارد، هدف آن هدایت رویکرد آمریکا در خاورمیانه پس از پایان جنگ ایران و در دو سال پایانی دوره ریاست‌جمهوری ترامپ است. دو رویداد بزرگ بر این برنامه‌ریزی سایه انداخته‌اند: انتخابات ۲۷ اکتبر در اسرائیل و انتخابات میان‌دوره‌ای آمریکا در نوامبر.
چه چیزی را باید زیر نظر داشت:
وقتی از ترامپ پرسیده شد آیا هفته آینده در نیویورک با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد، گفت: «شاید.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78423" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78422">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i16q8alEjDvvUytUw1Dfv0DYEPwzVNkCQBqF4zbCTKFHO7B6wHxk7g6wamrcRAq-bdea61G-ZrS3934ivi8Ckgx_M9Q1hVO5o3tY2pPf1u6a6gl29rB4Z9O99KStlpxDQoswz_wIWG9WyIIV-HcrzwVdEJ3mNwOlepRGTAk3NR-7Wn1LqpSuZOXH2mxcg-1B_BUxLMPL3bpYXyiD0DfDq9-1mCTBR55jLeiO2jDmFWm9ySk9YyaLmlt42b1KEz07hK5lcGcuGHVDp6zv8x2DsT9Xc1UX-Efn7seY6dFMg90l19N04NWcgO6oPBod7jm26hnF3n6NTf4l--kPYGVKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز پنج‌شنبه ۲۶ شهریور به نقل از مقام‌های آمریکایی گزارش داد نیروهای جمهوری اسلامی در روزهای اخیر دست‌کم دو پهپاد ام‌کیو-۱ آمریکا را سرنگون کردند.
مقام‌های آمریکایی که به شرط فاش نشدن نامشان با سی‌بی‌اس نیوز گفت‌وگو کردند، مشخص نکردند این پهپادها در کدام بخش منطقه سرنگون شدند و از کدام مدل ام‌کیو-۱ بودند.
این پهپادها برای ماموریت‌های اطلاعاتی، شناسایی و نظارتی طراحی شده‌اند و قابلیت حمل موشک‌های هلفایر را نیز دارند. سی‌بی‌اس نیوز نوشت این پهپادها در تنگه هرمز می‌توانند برای نظارت مستمر بر آبراه، رصد فعالیت‌های نظامی جمهوری اسلامی و شناسایی تهدیدها علیه نیروهای آمریکا و کشتیرانی تجاری به کار گرفته شوند.
بر اساس گزارش دفتر بودجه کنگره آمریکا، از آغاز جنگ آمریکا علیه جمهوری اسلامی دست‌کم ۲۴ پهپاد ام‌کیو-۹ ریپر به ارزش تقریبی ۷۲۰ میلیون دلار از دست رفته‌اند. یک پهپاد ام‌کیو-۴سی تریتون به ارزش حدود ۱۵۰ میلیون دلار نیز منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78422" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y1obBVpPWT-omI_x3n5aLKWIfH8JbtpvQBPOqkACTjc1NjiJTORWkjOsCByuwhxxJbEVrQvgisnf7MHbNLqzfrFLLX95Vif6thfb4dQFNw_WbwH8xndLsyTtHP25sTGLLI_1demE-MOcDjVxOWsk0XT7ITx3eNqwzduMfNcCXDvMxtTWgrUQ-vtHWOrsMglTNxCAcwDjAkPDqu5J1bnmL6sRF1---Gk9YfWmwEyzZdhDZLoLg2UWaMQsSekjFldXxlyIJ7DXf3zGMwo7fZd4a3zD1EF6GTO0Ji8N-27W3Jy1t-nTiNn-y3HBWYnxMu1-Iv1bOx9jA5MtnjPhX_3erw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=WIh3vSF2SC_rvb-qjb8dFuDBZwh4CYGNim6rjWlxURC41exvN5ktJ5tKT9NgRZI9xA9gyh-OTzSMf4Ib8cAreSewlG_YyIRAszH7XMhO0txJ65d9eVfXSIoVULWsqkIpyshk4emJ2gmvbRWMQ75X-Ce7IxOqJyk91cusupROjaapq_WpWjlQKxs_7asRANclPcy8pXER5W1hKOhoMn5RZmPPL8yDhP6wDa-DZAoMukOtB-MkENGeD6MwPoXh5Iig3f0yp3aO93Bj7bwBlAsWjk7aT2g193TTSk6NlumB3Fgb1H8mWPnNDvs4R1UYp59xJnjk_gYhKivQxRbpKfhDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ae7c8ac7.mp4?token=WIh3vSF2SC_rvb-qjb8dFuDBZwh4CYGNim6rjWlxURC41exvN5ktJ5tKT9NgRZI9xA9gyh-OTzSMf4Ib8cAreSewlG_YyIRAszH7XMhO0txJ65d9eVfXSIoVULWsqkIpyshk4emJ2gmvbRWMQ75X-Ce7IxOqJyk91cusupROjaapq_WpWjlQKxs_7asRANclPcy8pXER5W1hKOhoMn5RZmPPL8yDhP6wDa-DZAoMukOtB-MkENGeD6MwPoXh5Iig3f0yp3aO93Bj7bwBlAsWjk7aT2g193TTSk6NlumB3Fgb1H8mWPnNDvs4R1UYp59xJnjk_gYhKivQxRbpKfhDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز پنجشنبه ۲۶ شهریورماه در مراسم تقدیر از کارکنان برگزیده شاباک در بیت‌المقدس گفت اسرائیل بخش عمده ماموریت خود در برابر جمهوری اسلامی و گروه‌های متحد آن را انجام داده، اما این ماموریت هنوز به پایان نرسیده است. او گفت توانایی ایران و متحدانش برای آسیب رساندن به اسرائیل به‌شدت کاهش یافته است.
نتانیاهو با اشاره به ادامه عملیات اسرائیل گفت: «هنوز کارهایی برای تکمیل باقی مانده است و ما آن را به پایان خواهیم رساند.» او سپس تاکید کرد که اسرائیل حماس را از بین خواهد برد و در مورد جمهوری اسلامی گفت: «حکومت ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سرنگون خواهد شد.» او همچنین گفت اسرائیل به اقدامات خود علیه حزب‌الله ادامه خواهد داد.
نخست‌وزیر اسرائیل همچنین گفت خواست ایران و گروه‌های متحدش برای نابودی اسرائیل از بین نرفته، اما به گفته او، توانایی آن‌ها برای تحقق این هدف به‌شدت تضعیف شده است. این اظهارات در مراسم تقدیر از کارکنان برگزیده شاباک برای سال ۲۰۲۵ مطرح شد که با حضور اسحاق هرتزوگ، رئیس‌جمهوری اسرائیل، و داوید زینی، رئیس شاباک، برگزار شد.
@
VahidOOnLine
یسرائیل کاتز، وزیر دفاع اسرائیل، در شبکه اجتماعی اکس نوشت کارزار نظامی اسرائیل هنوز پایان نیافته و این کشور «اهداف مهمی» در برابر ایران و جبهه‌های دیگر دارد.
او گفت اسرائیل برای دستیابی به این اهداف «با قدرت نظامی و تدبیر سیاسی» اقدام خواهد کرد.
کاتز روز پنجشنبه ۲۶ شهریورماه با اشاره به غزه گفت سیاستی که همراه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دنبال می‌کند بر سلب توانایی گروه‌های جهادی برای حفظ قلمرو، زیرساخت‌ها، فرماندهان و تجدید قوا متمرکز است. او افزود اسرائیل این رویکرد را در غزه، لبنان و شمال کرانه باختری اجرا کرده است.
وزیر دفاع اسرائیل همچنین گفت این کشور فرماندهان «سپاه فلسطین» در ایران را هدف قرار داده و اجازه نخواهد داد ایران یا هیچ طرف دیگری حماس را دوباره مسلح کند. او تاکید کرد اسرائیل به عملیات خود برای تحقق اهداف امنیتی و جلوگیری از تکرار حمله‌ای مشابه هفتم اکتبر ادامه خواهد داد.
کاتز همچنین رجب طیب اردوغان، رئیس‌جمهوری ترکیه، را خطاب قرار داد و گفت اگر می‌خواهد به همفکرانش در غزه کمک کند، می‌تواند آن‌ها را به آنتالیا دعوت کند، اما «قدم به غزه نخواهد گذاشت».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78420" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzZES2Cf7wLfQkzcRUdMEhIP4e1Fa1rExUM7JkVBhiHpqNqV3TEr8zmBOCZ2x672YPzE0s_Bit44Wt1MDNWdnqpcXpgwbYmLTveeKMidTosH5-QrOs1Qc5ygx64CHhJKW2MqK6CuZ_mbOSm_p3lp11qHeoxCsOKyhElzSjuFKh8lcV1WeKqMuq2N1QFn2nuFsPrWuf74GwPo5mft9vCsQzq8r1z-rrmVCxCfx4xxK0lNFfhYlSWL2uSfB5cv0ffu3MqLuQjleIJb_vbHmwEVx5iWAoNe7UZy-VtQfBQOZXm_GL9vmF27CIuP5dzqO6LNYqDvwjvc3WfaQLr4qdeoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیات حقیقت‌یاب مستقل بین‌المللی سازمان ملل درباره ایران در تازه‌ترین گزارش خود اعلام کرد دلایل معقولی برای این باور وجود دارد که آمریکا در جریان جنگ با جمهوری اسلامی، در دو حمله هوایی به ایران مرتکب «جنایت جنگی» شده است. بر اساس این گزارش، این حملات دست‌کم ۱۷۸ غیرنظامی، از جمله زنان و کودکان، را کشت.
این هیات در گزارشی که به شورای حقوق بشر سازمان ملل ارائه شد، حملات آمریکا و اسرائیل به ایران در ۹ اسفند ۱۴۰۴ را بررسی کرد و به این نتیجه رسید که آمریکا در دو مورد حملاتی بدون تمایز انجام داده که به کشته یا زخمی شدن غیرنظامیان و آسیب به اماکن غیرنظامی منجر شده است.
بر اساس یافته‌های هیات حقیقت‌یاب، در یکی از این موارد، موشک‌های تاماهاوک به دبستان شجره طیبه در میناب اصابت کردند. این هیات اعلام کرد این مدرسه به وضوح قابل شناسایی بوده و در این حمله بیش از ۱۵۰ نفر، از جمله حدود ۱۲۰ کودک، کشته شدند.
در موردی دیگر، آمریکا با استفاده از موشک‌های تهاجمی دقیق، ساچمه‌های تنگستن را بر فراز یک مجموعه ورزشی و منطقه مسکونی در لامرد پراکنده کرد. بر اساس گزارش، این حمله ۲۲ زن و مرد غیرنظامی را کشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78419" target="_blank">📅 21:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw0QeBtnnCsaY3evaa90GqYIzqehJsAjDvwzHg9x4J136g3FL7Z8SE6ZtsRdM2OgATgaOCy9HKj8Xll0_wweey8D4G0Pq0bt2SaA0EAb_Z0VSbf3u88xWO241vPk-HHwt1ssRjpugElw0IxIFsc9-G8vl6P1vaizQN3eb4vlQ7NDdnMPQmz4Mw099pJ2XmM7EQ1dX0xECXGebI1r9G-fpM2uRBU_9RFXATODp4XA867mq6iC-HAjNyrXgB8e_CUF-LK44FvmlPSjdiCHT40JkuiYSOz9-n3wup-w5am37PGHBdvxAobvE2ARgVTfK18rb94ikz6Snab3HfC5q_rgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه و چین روز پنجشنبه، ۲۶ شهریور، در نشست شورای امنیت سازمان ملل متحد، پیش‌نویس قطعنامه پیشنهادی ایالات متحده برای تمدید ماموریت هیات کارشناسان کمیته تحریم‌های ۱۷۳۷ علیه جمهوری اسلامی ایران را وتو کردند.
این نشست با ابتکار فرانسه که در ماه سپتامبر ریاست دوره‌ای شورای امنیت را بر عهده دارد، در چارچوب دستورکار «منع اشاعه» برگزار شد. در جریان رای‌گیری میان ۱۵ عضو شورای امنیت، این قطعنامه ۱۱ رای مثبت کسب کرد، اما با مخالفت صریح (وتو) مسکو و پکن و همچنین رای ممتنع پاکستان و سومالی مواجه شد. برای تصویب یک قطعنامه در این شورا، علاوه بر کسب حداقل ۹ رای موافق، وتو نکردن اعضای دائم الزامی است.
دیپلمات‌ها پیش‌تر از مخالفت قطعی روسیه و چین با این طرح خبر داده بودند. مسکو و پکن معتقدند که با انقضای قطعی قطعنامه ۲۲۳۱ برجام در اکتبر ۲۰۲۵، تمامی سازوکارهای تحریمی پیشین از جمله کمیته ۱۷۳۷ فاقد هرگونه اعتبار و اثر حقوقی هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78418" target="_blank">📅 18:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/caed21affc.mp4?token=AzaVdL9nitK9JHrWuAz9vGH-ZwjLmt8dSPHmGkw91nQ_YnFGefa43nZTnZC0P4Gej_0ArG24OICwpj5XlHzb9v5VjTJLsgVUzQG5NSzfUWvH969OXnB0DoyZKIqD0gv9chdsSGVNdAh66u4_Hvwz0G94oj2CSpxijI6U3Yf7GsqNrrX31ZtWhJbW_JxNozubMXa-TeDUwiC5snDQfpxjIl3u68yPzQ9dDVhd8uyG7UeJAytFzaij97XXBSsdfBU6UkCWMOaufObVkiFncs0yFq-P1oTcQnuW7sjiP-S2wz8OD5C6QCNoe44Ax2GuTx9YVE0poDegEykanUhGBEHDxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/caed21affc.mp4?token=AzaVdL9nitK9JHrWuAz9vGH-ZwjLmt8dSPHmGkw91nQ_YnFGefa43nZTnZC0P4Gej_0ArG24OICwpj5XlHzb9v5VjTJLsgVUzQG5NSzfUWvH969OXnB0DoyZKIqD0gv9chdsSGVNdAh66u4_Hvwz0G94oj2CSpxijI6U3Yf7GsqNrrX31ZtWhJbW_JxNozubMXa-TeDUwiC5snDQfpxjIl3u68yPzQ9dDVhd8uyG7UeJAytFzaij97XXBSsdfBU6UkCWMOaufObVkiFncs0yFq-P1oTcQnuW7sjiP-S2wz8OD5C6QCNoe44Ax2GuTx9YVE0poDegEykanUhGBEHDxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خشونت و آزار جنسی)
ویدیو نشان می‌دهد ماموران فرماندهی انتظامی جمهوری اسلامی ایران یک نوجوان را مورد ضرب و شتم و آزار جنسی قرار داده‌اند.
این ویدیو خشم بسیاری از کاربران را برانگیخته است. برخی  گفته‌اند که «وقتی پلیس مقابل دوربین دست به چنین کارهایی می‌زند، معلوم نیست در بازداشتگاه و پشت درهای بسته چه به سر بازداشت‌شدگان می‌آورد.»
فرمانده انتظامی آذربایجان شرقی گفته که این اتفاق ۱۴ خرداد ۱۴۰۵ در جریان یک نزاع خیابانی در تبریز رخ داده است.
برخی هم با اشاره به انتشار این ویدیو در چهارمین سالگرد کشته شدن مهسا (ژینا) امینی در بازداشت گشت ارشاد، به تداوم خشونت پلیس در سایه نبود قوانین بازدارنده اشاره کرده‌اند.
پس از پربازدید شدن این ویدیو، فرمانده انتظامی استان آذربایجان شرقی گفت که ماموران حاضر در ویدیو «تنبیه انضباطی» شده‌اند.
علی محمدی به خبرگزاری فارس گفت که این افراد «تنبیه و انتظار خدمت» شده‌اند و «اقدامات تنبیهی تکمیلی» در مورد آنها در دست اقدام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78417" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q0aSd8Zvl6A6cPNY22ppl1dw1r2Af3Zxw5qBQ9rlczFj4fqtMopEVwKwrg65ykgXtwbOj7V0C5zgueH8UaBo50kTdtpWz66JrrxXhK0v_mhZB_Bcg1aM8XxohhkYr6oPl-5RjoXMGSwFAt9yDLHQkQ6H1fPwMMQNNbBR6qI2KTjn9WGevh4pm6Z7dxQx42oJSJ29oJ820ncRUocunOQ05SwFSGYKn4a3FwFv-HLv86JL_X_QnBjgE3Y6ELERNUzT-XmOHlawsSGJSv5n-n3FUpEhxBeVpSqbqGPYDljOpk_6lifWZ37wCD1h1nzH73N-FuC4dA_QfrcsIbc9E7DDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، مدعی شده است جمهوری اسلامی مستقیما با دولت او تماس گرفته و «بسیار» خواهان دستیابی به توافق با ایالات متحده است. او همچنین ابراز امیدواری کرده جنگ نزدیک به پایان باشد.
ترامپ بامداد پنج‌شنبه ۲۶ شهریور ۱۴۰۵، پس از ورود به ایالت کارولینای شمالی، در پاسخ به پرسش خبرنگاران درباره مرحله کنونی جنگ گفت: «امیدوارم به پایان جنگ نزدیک شده باشیم.»
او سپس درباره احتمال دستیابی به توافق با جمهوری اسلامی گفت: «آن‌ها می‌خواهند توافق کنند و خواهیم دید چگونه پیش می‌رود.» ترامپ در پاسخ به این پرسش که آیا پیام ایران از طریق میانجی‌ها منتقل شده یا تماس مستقیمی صورت گرفته است، گفت این تماس «مستقیم» بوده، اما درباره زمان، سطح و محتوای آن توضیح بیشتری نداد.
رییس‌جمهوری آمریکا ساعاتی بعد در یک گردهمایی انتخاباتی در شهر گاستونیا در کارولینای شمالی، بار دیگر گفت جنگ با ایران به‌زودی پایان خواهد یافت و «پایان واقعا خوبی» خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78416" target="_blank">📅 03:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHRLD-ZTCUfRy334SbH2-TC58Auh9F6pnjPcfgt0LRAa-DR7FKJvY7r7uIXkSzZTPc4dAiPrxYeZrtMooUXurnvJf_QDnL5FIKpGLm5GHTv8lqkciRHQqlQsl6a4hQmjJASQaZ4xavwxMydFz9PRgWjEXutMBwYwI0v3u06cqe2v-LoKihNVhSaNYNA2hW-jjQQg4V-Zv2ijxqhjCf3gBVAcmqtFeeOKNmNmj8zbaS1RzDWIOaw_gpzj7VLGu5qpCXLQbQCeszeGiZTu_x54Pq-lM1Z5r_Rd7IBdQ-P5UNzcgdMKjJUKPn_Ws0uXtGNRyhJ0ZrisjpzoJxcBZ1r6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت هواپیمایی ماهان چهارشنبه ۲۵ شهریور در اطلاعیه‌ای اعلام کرد پروازهای این شرکت در مسیر تهران-مسقط-تهران از ۲۶ شهریور، برابر با ۱۷ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان دلیل لغو این پروازها را اعلام مراجع هوانوردی عمان عنوان کرد.
این شرکت همچنین در اطلاعیه‌ای جداگانه اعلام کرد بنا بر اعلام مراجع هوانوردی ترکیه، پروازهای ماهان از ایران به مقصد ترکیه، شامل استانبول، آنکارا و بالعکس، از ۳۰ شهریور، برابر با ۲۱ سپتامبر، تا اطلاع ثانوی لغو خواهد شد.
ماهان افزود آخرین پروازهای این شرکت در مسیرهای تهران-استانبول، تهران-آنکارا و بالعکس روز ۲۹ شهریور انجام خواهد شد.
خبرگزاری عصر ایران نیز سه‌شنبه ۲۴ شهریور به نقل از یک منبع آگاه گزارش داده بود دولت گرجستان در پی تحریم‌های جدید آمریکا، پرواز همه شرکت‌های هواپیمایی ایرانی به این کشور را از دوشنبه آینده متوقف می‌کند.
عصر ایران افزود بررسی این رسانه از چند آژانس گردشگری نشان می‌دهد فروش تورهای گرجستان نیز تنها تا یکشنبه ۲۹ شهریور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/78415" target="_blank">📅 17:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjOjSjlqbefUEUI3yuDe6E-s3lNzbakn8I-1R03JbPMj5lMI3Cl1oGSVnBbY3q71bAfUAR9gIF7d7EydvgsSwISAlMvrxWerKKIaSFUvCAX9Xvtana8cHaXGn-vo29sQEUfEGemo0anj_4KS-hCRNUL9Rm-z51_Q4tF9xOWgK6q0G02Tj6M6RhMKYx79Njz5Cl0NMRy3Khcth0TIoWWIgwz79YrJ2WFAn-ADZLCSmIpiCUZFjZ65klKrWnF9jjuCbbVE31_-M7v84i5kIEjnssXMUhJG_3SqOqH3hipV5Le0Gz47QOvwZ8wMPzLaoDfuY2x6ztVIe7y3K-WQaJBuhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل قدیانی، زندانی سیاسی محبوس در زندان اوین، روایت جمهوری اسلامی درباره نقش «تروریست‌های وابسته به بیگانگان» در کشتن معترضان دی‌ماه ۱۴۰۴ را رد کرد و نیروهای حکومتی را مسئول «قتل عام» آن‌ها دانست.
قدیانی در بیانیه‌ای که روز ۲۴ شهریور از بند هفت زندان اوین نوشته، با اشاره به راهپیمایی ۲۲ بهمن و تجمعات حکومتی ماه‌های گذشته پرسیده است اگر عاملان تیراندازی به معترضان، آن‌گونه که حکومت می‌گوید، «تروریست» بوده‌اند، چرا در تجمعات حکومتی که در امنیت برگزار شده‌اند، اثری از آنها نبوده است.
او از رسانه‌ها و نهادهای حقوق بشری خواسته است درباره این تناقض در روایت جمهوری اسلامی پرسشگری کنند و نوشته است: «تروریستی در کار نبوده و نیست و قاتلان [...] همان نیروهای [...] حاکمیت‌اند.»
قدیانی همچنین در این بیانیه علی خامنه‌ای و پسرش مجتبی خامنه‌ای را مسئول این «جنایت سهمگین» دانسته و نیروهای حکومتی را به تیراندازی به معترضان متهم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78414" target="_blank">📅 17:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78413">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNcQUhUIskiQZjvBFUmeRhL3O6x0C3_lr00XCn3bI9irNu8Sz2PJ-foR3XNwe7GbjWAZ6x3HQtPM2miLDGz9DtJz4NEoCVlUWsX9db_WRyWu2vQ4la2YUsIkPjUG1Pzt7B9qZd66KW8wtgbl8hlLvdWQa2c_y20JABn7QcSRzWcjy0q_z9vj-59qZyZjlpTM7IU-d1tQqL5B1j-N99YuVpbbMJlZR4K43Fed2NG5elf3IGPvOEVITVkOTi9AD3zMMgH4ugypIKzrGyg6A2ddv9Sart_S29twnxvpFuDWrnLb0RO6xBIq02Qm4CnRqv9vCZQ0D50vBvmfpllVWtbqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین با صدور بیانیه‌ای اعلام کرد که وانگ ئی، وزیر امور خارجه این کشور، روز چهارشنبه در دیدار با عباس عراقچی در پکن گفت:
چین، ایران و ایالات متحده را تشویق می‌کند تا عقلانیت خود را حفظ کرده، خویشتن‌داری نشان دهند، به یادداشت تفاهم اسلام‌آباد بازگردند و «در گفتگوهای ماهوی درباره مسائل مورد علاقه طرفین مشارکت کنند.
براساس این گزارش، وانگ با بیان اینکه چین «نمی‌خواهد شاهد سرایت بیشتر تنش‌های منطقه‌ای به یمن و دریای سرخ باشد» افزود: «ما از همه طرف‌ها می‌خواهیم اقدامات موثری برای بازگشایی هرچه سریع‌تر تنگه هرمز انجام دهند.»
وانگ همچنین گفت که سیاست چین در قبال ایران همواره ثابت و پایدار بوده و چین مایل است ارتباطات و هماهنگی‌های خود را با تهران تقویت کند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، چهارشنبه، ۲۵ شهریور در سفر به پکن با وانگ یی، وزیر خارجه چین، دیدار کرد و بر گسترش روابط تهران و پکن در چارچوب مشارکت جامع راهبردی تاکید کرد.
عراقچی شرایط کنونی منطقه را ناشی از حملات نظامی آمریکا و اسرائیل به ایران دانست و از مواضع چین در محکوم کردن اقدامات این دو کشور قدردانی کرد.
او گفت: «جمهوری اسلامی ضمن آمادگی کامل برای دفاع مقتدرانه از حاکمیت ملی و تمامیت سرزمینی و صیانت از امنیت و منافع ملی ایران در مقابل متجاوزان، از راه‌حل‌های دیپلماتیک که حقوق ملت ایران را تامین کند، استقبال می‌کند.»
عراقچی همچنین گفت شرایط منطقه پس از جنگ ایران تغییر کرده است و در نظم جدید منطقه‌ای که با گفت‌وگو و همکاری کشورهای منطقه همراه خواهد بود، جایی برای حضور و دخالت نیروهای خارجی وجود ندارد.
او با اشاره به آنچه نقض مکرر تعهدات از سوی آمریکا خواند، گفت جمهوری اسلامی خواهان بازگشت آرامش به منطقه و روابط دوستانه با همسایگان است و در همین راستا گفت‌وگو با کشورهای منطقه را آغاز کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78413" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ePgS96xMcJRR_r-DP9Xa41H9rR8mhb1L7UbuS5_jotMV5VhzEI0baBxSJG3Y7iBn4bbbvWyqphaumTa4MvKylXvdxXZLCbJMMrasMInanFYJJsRHYZuEs6MK-Z0APf_6KQDr6Sidn4NIJsXkt6ur5mgbQcysbN7GJJFzRfKU9RYousNWEYXyp9BoJVmGIeSujUBYovWP_J05WaXmBO0pTYO6Xwz4y0LUaPaX8UjDwAQyh5j8RSB1c9pYjzziy_9FesuuVIrhdbs8mleux-n6eE8-A0icY1_1NIlP8jfoTSIZK2OuKmSrUyC2XFLNXev1oWYLojXDV0QKLYSEh3xI0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز چهارشنبه ۲۵ شهریورماه به نقل از پنج منبع آگاه گزارش کرد که مقام‌های ایالات متحده آخر هفته گذشته (روزهای شنبه یا یکشنبه) با نمایندگان شورشیان حوثی مورد حمایت جمهوری اسلامی ایران، دیدار کرده‌اند.
براساس این گزارش سه تن از این منابع که خواستند نامشان فاش نشود گفتند این دیدار که رسانه‌ای نشده بود، در سفارت آمریکا در مسقط برگزار شد. دو منبع دیگر نیز اشاره کردند که دولت عمان، به عنوان میانجی باسابقه منطقه‌ای، به برگزاری این نشست کمک کرده است.
دونالد ترامپ در سال ۲۰۲۵ و پس از بازگشت به قدرت حوثی‌ها را در فهرست «سازمان‌های تروریستی خارجی» قرار داد و هرگونه حمایت از این گروه را جرم‌انگاری کرد.
ترامپ روز شنبه گفت حوثی‌ها با دولت او تماس تلفنی داشته و از ایالات متحده خواسته‌اند از جنگ یمن دور بماند. جی‌دی ونس، معاون رئیس‌جمهوری هم روز دوشنبه بدون ارائه جزئیات تاکید کرد که ایالات متحده در تماس مستقیم با این گروه است.
دو منبع آگاه اعلام کردند در این نشست که به گفته یکی از آن‌ها روز یکشنبه برگزار شد، حوثی‌ها به مقام‌های آمریکایی گفته‌اند قصد حمله به شناورهای آمریکایی را ندارند و به آتش‌بس سال ۲۰۲۵ با آمریکا متعهد هستند.
یکی از این منابع که یک یمنی است، گفت این گروه همچنین اعلام کرده‌اند که به کشتی‌های اسرائیلی یا هرگونه کشتی تجاری دیگر، به‌جز کشتی‌های متعلق به عربستان سعودی، حمله نخواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78412" target="_blank">📅 17:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78411">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoR6EyugLUbv5tji3nimtNQRioNGeLcdQrBBLLYtmfc5qboc6VHsmD2koUS57I1paFDyTbryIUM_7GhUvfAE_1yQb4wMBwUBcc5J3jdjZoyrovJg2lXAkRKVfvv4UhdHyV_0a1DATi0kISZxTzIql42oER4yGeDWd-PUAzDNplPAxukxmBp6nFtrRq23oPpWJjdiX_WX7su93RlO57-Cq52VmxWY9AUcFIlctZEkW5tPO0Q5XBte2jQPGbGyQdc8RyuQ9HpIGdgVWUEZTmg6yHtf-JH1ni4fAedy4zIu5Tih118watK0rWLWmQBd938lBi4NwBQO9WG7ptCnUyJ-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«جی‌دی ونس‌»، معاون رییس‌جمهوری آمریکا، گفته است جنگ با جمهوری اسلامی طی «یکی دو ماه آینده» وارد مرحله‌ای کاملا متفاوت خواهد شد و واشنگتن در مرحله بعدی باید مانع بازسازی توانایی‌های هسته‌ای و نظامی حکومت ایران شود.
ونس همچنین با پیش‌بینی «دونالد ترامپ» همراه شده است که جنگ پس از انتخابات میان‌دوره‌ای آمریکا پایان خواهد یافت؛ هرچند توضیح نداده منظور از «مرحله متفاوت» تشدید عملیات نظامی، کاهش درگیری‌ها یا آغاز روندی دیپلماتیک است.
معاون رییس‌جمهوری آمریکا در گفت‌وگو با نیویورک‌پست که روز سه‌شنبه ۲۴ شهریور ۱۴۰۵ منتشر شد، گفت: «نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم رییس‌جمهوری درست می‌گوید که این مسئله طی یکی دو ماه آینده وارد مرحله‌ای کاملا متفاوت خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78411" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T37H6HIZ_89h_3upX8pFyCbAy__IRUnRyZrZr8jkmNqwLBxOHHzk5FIAe8lokafwBoptdAImU9D5D2vr07IfRe_oY2i7wJlqmzTi8pWgJ-vC2PRhsIgzG_GEBZhXW5AQuL6TLtA4nfmlz6bfTrjYAO3cQhKhNdIW0EkeVToZ2zchjsT98QO4nBIhit6E3oP14tS73qzc_duBwudRG14viR9rt9JDrwzQgrCsUhFA580EdrmT-H0IWAiNluUAdpZPsWrq5jhli5YoxjNfEi5-vniALC6CvgMhnUmbqhBrY67SE4McZ31vAwo4cxRcMRof4zsREczQgpnUQx2ib6nDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین قشقایی، همسرش سارا شمسایی و ابوالفضل قشقایی، برادر حسین، از معترضان دی‌ماه، پنجشنبه ۱۹ شهریور بازداشت شدند.
حسین قشقایی و سارا شمسایی در لاهیجان به دست نیروهای وزارت اطلاعات بازداشت و به اراک منتقل شده‌اند.
محل دقیق نگهداری آنها مشخص نیست و احتمال می‌رود در بازداشتگاه اداره اطلاعات اراک باشند.
ابوالفضل قشقایی نیز همان روز در زرندیه ساوه بازداشت و به اراک منتقل شد. به گفته یک منبع مطلع، ماموران هنگام بازداشت با خشونت وارد منزل شدند و گوشی‌های تلفن، تبلت و لپ‌تاپ اعضای خانواده را با خود بردند.
حسین قشقایی با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «اغوا و تحریک به جهت برهم زدن امنیت کشور به جنگ و کشتار»، «نشر اکاذیب در فضای مجازی» و «اجتماع و تبانی علیه امنیت ملی» روبه‌رو است.
درباره اتهام ابوالفضل تاکنون اطلاعاتی به خانواده اعلام نشده و پرونده این سه نفر هنوز به شعبه‌ای ارجاع نشده است.
از دی‌ماه، سیم‌کارت‌های حسین و سارا و حساب بانکی حسین نیز مسدود شده بود. آنها ماه گذشته به دادسرای عمومی و انقلاب زرندیه احضار شده بودند، اما در مهلت پنج‌روزه تعیین‌شده حاضر نشدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78410" target="_blank">📅 17:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=hveiLtKiklIiiBoBY0ZfSJCywtmhchwoaiTcVceDtWbEO7fylleeLEC4GtAayzNQJ5ADBy1fAOi5m3BjsyF3T4Vu2Wdu9uzPiegwE0TAopGIKMJnKjIbxc_Sj0j3glvsKyo82bNqBy-5BDND0UY1zjaOmeAM-FYusUF1zhu9UvbtUI2PlHaGKrEIyrNzfMmYpEWvR0QW9hlsYJaNVX4PntPuSy6p2xRE3pjH5NRNBm8BiZpqvtEuhO49R6U62Rz2AfYFhlr0eosdPdEoR3GG9mRkHqZaoLeHDm888zlh4JWD8yXTCWvocWEwtn5XYcUHeQiBvv27SFwePdam7IXrwo22ZlXJi2ejhz13T95RnqvVxrfr9hhXYuhv6QHrZhbL6YcyCZzZqgQgIbHJ3zvb5embOeXLdnuo4Zjw0Qi_DIQEcySFlrtHaM2v2lKlQRIsWkTVYg7DXHg0NkPtG-BE78puHt5DMToLBX1CFe_-gR1-7ohU1WQqkQRzM_RWcYsab1LbAylE7zce28ezN8JhGO_sk25PSBtqEH1iXfg0kr67ujnljz3rMiAsoXeXDOLJsHlVwaFDbhXOymEpSfwRYKPz0YrgvnjWlVbjh-c4owNXjBpPvQr214xEKPLJ3vlFQGn8bBBU49to3sb0n2ACfuZMDBSXCVhTjnfZDKWt8Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fe85f5293.mp4?token=hveiLtKiklIiiBoBY0ZfSJCywtmhchwoaiTcVceDtWbEO7fylleeLEC4GtAayzNQJ5ADBy1fAOi5m3BjsyF3T4Vu2Wdu9uzPiegwE0TAopGIKMJnKjIbxc_Sj0j3glvsKyo82bNqBy-5BDND0UY1zjaOmeAM-FYusUF1zhu9UvbtUI2PlHaGKrEIyrNzfMmYpEWvR0QW9hlsYJaNVX4PntPuSy6p2xRE3pjH5NRNBm8BiZpqvtEuhO49R6U62Rz2AfYFhlr0eosdPdEoR3GG9mRkHqZaoLeHDm888zlh4JWD8yXTCWvocWEwtn5XYcUHeQiBvv27SFwePdam7IXrwo22ZlXJi2ejhz13T95RnqvVxrfr9hhXYuhv6QHrZhbL6YcyCZzZqgQgIbHJ3zvb5embOeXLdnuo4Zjw0Qi_DIQEcySFlrtHaM2v2lKlQRIsWkTVYg7DXHg0NkPtG-BE78puHt5DMToLBX1CFe_-gR1-7ohU1WQqkQRzM_RWcYsab1LbAylE7zce28ezN8JhGO_sk25PSBtqEH1iXfg0kr67ujnljz3rMiAsoXeXDOLJsHlVwaFDbhXOymEpSfwRYKPz0YrgvnjWlVbjh-c4owNXjBpPvQr214xEKPLJ3vlFQGn8bBBU49to3sb0n2ACfuZMDBSXCVhTjnfZDKWt8Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فراخوان ائتلاف نیروهای سیاسی کردستان ایران، همزمان با چهارمین سالگرد قتل حکومتی مهسا ژینا امینی و آغاز جنبش «زن، زندگی، آزادی»، کسبه و بازاریان شماری از شهرهای کردنشین اعتصاب کردند و مغازه‌های خود را بسته نگه داشتند.
از صبح تا ظهر چهارشنبه ۲۵ شهریور، اعتصاب و بسته بودن مغازه‌ها و بازار در دست‌کم ۲۰ شهر، از جمله ارومیه، اشنویه، بانه، بوکان، بیجار، پاوه، پیرانشهر، ثلاث باباجانی، جوانرود، دیواندره، روانسر، سقز، سنندج، قروه، کامیاران، کرمانشاه، کرند، مریوان، مهاباد و میاندوآب گزارش شده است.
@
VahidOOnLine
وب‌سایت‌ها و منابع خبری مختلف که اخبار کردستان را منتشر می‌کنند، از جمله هانا، کردپا، کولبرنیوز، زاگرس ۲۴ و شبکه حقوق بشر کردستان نیز گزارش‌ها و تصاویری از تعطیلی مغازه‌ها در شهرهای مختلف کردنشین منتشر کردند.
در همین حال تصاویر و گزارش‌های مختلفی از برقراری فضای امنیتی شدید و استقرار نیروهای نظامی و انتظامی با سلاح‌های سنگین در شهرهای مختلف کردنشین منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78405" target="_blank">📅 17:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jiBod9bSVo66fOnobjZQ1QTAyAOqJxR1hdsbGlzGR_iv97YPer96Cpord0rLjyGiIead4qiEXbKgQm3Q2wzoKnYJTrmpq_WTyNW43CWSLxYcOBmyP2Ajpnt1rK7S-ehyIgz9TqLf0KWNUvqwK3Nw8xRZoJAaQaC2T5BtG9QaE0CikOCVH-XjRgY0qbBGGNgyF_qxuyZGa4eUmL5KowRRv4nlihpGIrhos4O5NMOvqIQJ3TxMvGyPoEfiiK5yCxkHt_PLXzapL-8dDyRatiwwbeDKY3OmwrM27Co7OxzfOb1U4eSu7TsvX344kHObZj_WOPxQkq02rJwYSCvLM37wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kmVUAmcdaHODJLcJud4QGyIzkbK_oNwxdyLZBcY75VycrKd45qTLFe4pWJaD8mW4CtmQ8HfckB7iE2eX_boCWky6UnQy5PiHRuTWmIU5-C-hk8FvnraHJ_6xg957US2NMw6B6fixiPhiMuyIpo6d6PE2o7JtFaqZixvWGR0q5PgsIqbcuAkA4e6Da1fctq4hzWZ_e1lkAtn7aaBWP7Eqc42THFYhSzV0BI04Sz2-ACRbv9Dmll6I7jENGbrrnBnw5N4c9Yaf5gsdmn83I4fzeQICy9Q-vLx5x7XrbRsRVaMSq5K0qo9qknh5ROtABgZUD-IfkqeqNJUfxXuDvJtCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YIW2AOa9Bw5CPUtnegb0koHy_tX0qySMQCzjTIrY6jRdOpqHBMZ88TBV0P9X6CLlrYZf6Z9oFQ2Ne8jQcO-soxDieO-SBtsQfMjCkXELZat1KoGcSGwE3TSFOuPtejjJ1uoqCju8zeQGfY90Osa4EjfiopZoQ_BfsiixJzKI-jzp4FeOWW7TZHxkzMuYUDSZBxNlR0n28tNSi-ALoYA-U23XXgYi0u9II_YA-XRQhngbq8x3u0cxmS9q2xlB333CBbfmBGgGo9yeUqmPVHcdII0VEpdLYLPxYfiMY4FEyyneDQCuAeFiBbAx3QGMXgmYLzsbK-IHBvAE1qHI1CRIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v8wscxY4WJC6YJdA_SekOUJBAa2Rf6S7FeqU7Uq7-E1pUpWA_QdJws_QtoDwC18JavavCMFqeGPUB8LjsTT0XqdijHD9h89C3-mxKnBSxA-EvkyZxG2q6OA9FNq7-ujEI3_eyz6vr50P4pfRuqzAQjDSuT1G4t_w5zT0HudXMr_plCRWOI4tToqAEUgeLh8g8G5VDzNIAo2nbWTBwM4OpUxMcY8-y--BVxnp_69eWgC8RApN4H1ryUkfm2IONHq3ZzrMMFbYj4-6_TJYzbjrt93W78NgeoUErnjmXqAkq-DWz6lfL7UuSIo9BJ5fTtThLK68jxbLrA3vod_UebVmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pKaPq-Cwk19O5wKNGDrq592sOqJsSMiUYFX0j3FXmMEgG_Bpli6zXbojHIUBAEr92Cs2cvzDEK-PoO_cvHzFTVWJ162XuE5HOJc_FmIs3oIAE3RnjimdGtWnqso0pnBpFq5vHgI0JZRxPb1CBogXLCJkDX3utVz28aM-RNEsy8wg_PBc4-oLiNEhEbQdXc4EV8onurkE2yoFLAycoIUX_pxMItkgCH3HazIDMFE17hGJt80bAbytJ8Js0WoHjnwvkZiCFg0DvWZrHiF8dEiQh6XmSgBVfBAsvY6k-pNI1AB57IA_4MeUFbd2CjBcHAqu0CxhG31YfhEoQp1lCQg3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNk6yZhKVE4UJ4TGDSNE9m93-Ev6zPY5ed899tPAD5DQrVCYzAXmqNNivl5B2WNJf9HB2hbSMXoht7YVMoRc20HCPMOpFdYLH3tVr7L3xAaR_DDDF8dsMq9wiYfcS4J77IglsOHFSdi5kShK82zdPsTFbE--JxaK9A1r-8TIIiYXMItJJuZQQq0fej8beJMvJVSA4JWTEyuHIFa_C1xYN6Q7-DLzTxoQxfa_NpRE1Y4TGYebbCMUTpTvkCM1N-OgdXzjGcOQKIA2njPuaUJWk_BYeYtodDon-jvEatJCxSs8rvMXu3PMzWyS8c0P1djfIOq5Cp7ZznzSxR6FaLrF8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌بی‌اس‌نیوز گزارش داد تصاویر جدیدی که به‌طور اختصاصی به دست آورده، برای نخستین بار گستردگی خسارت حملات موشکی و پهپادی جمهوری اسلامی به چند موضع نظامی آمریکا در خاورمیانه را نشان می‌دهد.
این تصاویر را نظامیان آمریکایی در اختیار سی‌بی‌اس‌نیوز قرار داده‌اند. یکی از آنها گفت خسارت گسترده به پایگاه‌های آمریکا به اطلاع مردم این کشور نرسیده است.
در تصویری از پایگاه هوایی شاهزاده سلطان در عربستان سعودی، یک هواپیمای چهارموتوره بویینگ ای-۳ سنتری دیده می‌شود که موشک به بخش عقبی آن اصابت کرده و دم هواپیما از بدنه سوخته جدا شده است.
تصاویر دیگری از این پایگاه، ساختمان‌ها و آسایشگاه‌هایی را نشان می‌دهند که بخش‌های داخلی آنها تخریب شده است.
سی‌بی‌اس‌نیوز همچنین از ثبت خسارت‌های مشابه در کمپ بوهرینگ در کویت خبر داد؛ پایگاهی که محل استقرار و آماده‌سازی نیروهای زمینی، خودروهای زرهی و شماری از هواپیماهای ارتش آمریکاست.
پنتاگون به درخواست سی‌بی‌اس‌نیوز برای اظهارنظر درباره این گزارش پاسخ نداد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78399" target="_blank">📅 04:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78398">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJGU-EZmNrPBN9Jz_FN8bhP-7lqwagJQZtcD3uAEUvc_quudTsbMuokSfTWv0W3qSNVjNd0Ors69_RmIZPwksOGcNQpYEnlTbluqGfG8vpx0dEUlRLmGO5O7-RtqXZefPYm0wi5w08MBRQ7jHJ3x8u0dwodQ5Y8R3Mtceg3ZA0B4X_Du5OZrjiEFGJ2yh7h9c4I7IyfOuufkhAJUZspWjLGPhL-Pdp7w10N4qOwamKWDz5qC-TIyLpcfXiT2Szyu8Bl_Mko9nJuIudbMdo5lOKyR_iVr9TIMJ09iPY0KhX8WhBxYu4NCk8iBAa5WTiAfXom9kpcUtVKtH8Ho_ArQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی در یمن اعلام کرد پدافند هوایی این ائتلاف یک فروند پهپاد پرتاب‌شده از سوی حوثی‌ها را که قصد ورود به حریم هوایی مکه را داشت، رهگیری و منهدم کرده است.
به گزارش خبرگزاری رویترز، ترکی المالکی، سخنگوی ائتلاف، در بیانیه‌ای گفت این دومین تلاش حوثی‌ها برای هدف قرار دادن مکه بوده است.
به گفته ائتلاف، پیش از این نیز حدود ۹ سال قبل یک فروند موشک بالستیک به سوی مکه شلیک شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78398" target="_blank">📅 03:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jPDLHk5DXbErIZGnQIltBT8-KZXl4phT4Ddk1LwEkUIIxuKK02g56F6_UOHCWugLMuGSIk1dEH7aJcw9k1dEnJfFX7kQbQ2dlGRs58lgbsSbH_9ExQHTy1FMPZ0746z74BxRjWq2ZDT7mc-e_p_CG_9A_iw8xWmBEe4tWesKl00siv7U9UTTJjhoBOOsGNkPkJSUvQzPvLprPSWbSw7Dp8bQqTFkY6eA-8Fs0omEW56eIc_ytuw8lyeKWsrzV2GezoVZe0fopo_WdNGG49jC_leiI0tajMMa_gM3eEgfGoHlCIjM2UIZxLY-p5utSQwvwYbXvS51TTo1Cn2od425WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو مقام اسرائیلی گزارش داد فرماندهان ارشد نظامی آمریکا، اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر هفته گذشته در نشستی محرمانه در آلمان درباره جنگ با جمهوری اسلامی و تنش‌های منطقه گفت‌وگو کردند.
اکسیوس گزارش داد نشست محرمانه فرماندهان نظامی در آلمان به ابتکار برد کوپر، فرمانده سنتکام، برگزار شد.
به گزارش اکسیوس، برد کوپر در نشست محرمانه آلمان، فرماندهان نظامی اسرائیل و کشورهای عربی را در جریان برنامه آمریکا برای افزایش تردد کشتی‌ها در تنگه هرمز قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78397" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78396">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=nYsoshWRSTyu_-b6_8rB18LyXu7IzYLFFpD41WMLqII1_d8OG6j3CIPR0vPDpVRY2ZUH68iltCni2QUMJkMKUWvysMtvMINivOET5E37TqIA9CtKPT3zQLLrDNacm1WaV1E_z83iJndCNpP75yVvq8efhkGtdP-_WjQM53tWu4t8P3I1nTlJqTN5NP9iu3Upi4h19-QryXApWgNLFclO3qcOXullhB-AIKZESTUPXEhvHAMbD9a-NlIQTm5fGsOZN4zukH8D3X6C6SIIS7iEXFpMsKNgfvPlWwfA_uTmadsO-yb2xmbyORwIOkh1t93ZWi4IVivMYJuU5Rxbb04AXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86139d3a31.mp4?token=nYsoshWRSTyu_-b6_8rB18LyXu7IzYLFFpD41WMLqII1_d8OG6j3CIPR0vPDpVRY2ZUH68iltCni2QUMJkMKUWvysMtvMINivOET5E37TqIA9CtKPT3zQLLrDNacm1WaV1E_z83iJndCNpP75yVvq8efhkGtdP-_WjQM53tWu4t8P3I1nTlJqTN5NP9iu3Upi4h19-QryXApWgNLFclO3qcOXullhB-AIKZESTUPXEhvHAMbD9a-NlIQTm5fGsOZN4zukH8D3X6C6SIIS7iEXFpMsKNgfvPlWwfA_uTmadsO-yb2xmbyORwIOkh1t93ZWi4IVivMYJuU5Rxbb04AXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده در جلسه سالانه درباره وضعیت اقتصادی آمریکا و سیستم مالی بین‌المللی با دفاع از سیاست‌های دولت دونالد ترامپ در قبال ایران، گفت رئیس‌جمهوری آمریکا اقدامی را انجام داده که به گفته او، رؤسای‌جمهور پیشین آمریکا سال‌ها از انجام آن خودداری کرده بودند.
اسکات بسنت با اشاره به جمهوری اسلامی گفت: رژیمی که خود را وقف شعار "مرگ بر آمریکا" کرده و به‌دنبال دستیابی به سلاح هسته‌ای برای تحقق همین هدف است، اکنون با سیاستی متفاوت از سوی آمریکا روبه‌رو شده است.
او افزود: تحت رهبری رئیس‌جمهور ترامپ، آمریکا دیگر صرفا در حال مدیریت تهدید ایران نیست؛ ما در حال پایان دادن به آن هستیم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78396" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78395">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VltfPcjFeuSCimdbs2oCaPOb90rQa7y9m8vOemJgkXkcmJ2zpalPHTHixWdvCIvWlGa_kKUKgsRXuIdAF6vZFqDHAEAZONkdsnCnycrRYvE3iBmUucI6Q5F9j4KYX-eKshTkNv2XgHXkxiDjH6o2OYbWWA3yt9b1jcSd2E22c5wLeck8hD3wrMiAf0TeXVbn2LqUNWedH0N_FwhKin0TQy3UMNMKs9gzHDGqK_T5ehXRRc31jH_4ipL_J0GZo11GVJ0lhVF8HMXCBzUAyWmu3AUsnCDeucmdSoHZ2hspq_8IgU2cDrZOykfZsZrD3tUx7-bbPQvh7HKq52PrYMZkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره خبری که تسنیم با شرح
حمله به قایق‌های صیادی
منتشر کرده بود:
وبسایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده روز دوشنبه ۲۳ شهریور ۱۴۰۵، دو قایق کوچک ایرانی را پس از تلاش نیروهای سپاه پاسداران برای تصرف یک پهپاد نیروی دریایی آمریکا در تنگه هرمز منهدم کرده است.
به گزارش اکسیوس، نیروهای سپاه با استفاده از این قایق‌ها تلاش کردند یک شناور بدون‌سرنشین آمریکایی را که برای گشت‌زنی در تنگه هرمز مورد استفاده قرار می‌گیرد، تصرف کنند.
پس از شناسایی این تلاش، یک پهپاد آمریکایی دو موشک به سمت قایق‌ها شلیک کرد که به انهدام آنها و کشته‌شدن بیشتر سرنشینان منجر شد.
تیم هاوکینز، سخنگوی سنتکام، تلاش نیروهای ایرانی برای تصرف شناور آمریکایی را تایید کرد و گفت این قایق‌ها «تلاش کردند یک شناور سطحی بدون‌سرنشین آمریکا را تصرف کنند، اما پس از واکنش قاطع نیروهای سنتکام موفق نشدند». او تأکید کرد این شناور همچنان تحت کنترل عملیاتی ارتش آمریکا قرار دارد.
این در حالی است که رسانه‌های ایران حمله به دو قایق را به شکل حمله پهپادی به «قایق‌های صیادی» گزارش کرده‌اند.
به نوشته اکسیوس، این دو قایق در نزدیکی بندر کرگان و جزیره لارک در استان هرمزگان هدف قرار گرفتند و احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، حمله را به ارتش آمریکا نسبت داده و از مفقود شدن شماری از صیادان و آغاز عملیات جست‌وجو و نجات خبر داده است.
این حادثه در شرایطی رخ داده که ارتش آمریکا تلاش می‌کند با افزایش تردد کشتی‌های تجاری در تنگه هرمز، عبور و مرور دریایی در این مسیر را به وضعیت عادی نزدیک کند.
یک مقام آمریکایی به اکسیوس گفت ارتش آمریکا و کشورهای عربی خلیج فارس در ماه‌های اخیر تردد نفتکش‌ها از تنگه را در طول روز نیز آغاز کرده‌اند، در حالی که پیش‌تر این عبورها عمدتا شبانه انجام می‌شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78395" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78394">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=OWVpnB5Wq5JyCk7_FpPVybz0g5cFe1ATE7otqlX4x7Ca9ZjUUw-MHySsO4Ji_9Wt9iDW1ezGsUm7b2lA--8weD8GgQkP9s-ZumvZN-OY-Mu2PYXfaBy4U5dJn0ZphIlQoR_j4jgoXpv993sg8i8FzYW7yqWWZ09Kh3uyBnykunH_CW3ODoWm2blm3ULQpqZp2z9GBMU757-tCxI858eEAgOUpXxhJNpHa9mFuBCpAeKT3Eq9-4UNI38SG66QsSSA1wqnKSkerPyzfFRIK7Gqb1rx-6w2CHgKzCJgsm0jxKVH-GMsUZig1iMRZY1agd8LHDOvpPshVTglY3_m0VT-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d82b868f8b.mp4?token=OWVpnB5Wq5JyCk7_FpPVybz0g5cFe1ATE7otqlX4x7Ca9ZjUUw-MHySsO4Ji_9Wt9iDW1ezGsUm7b2lA--8weD8GgQkP9s-ZumvZN-OY-Mu2PYXfaBy4U5dJn0ZphIlQoR_j4jgoXpv993sg8i8FzYW7yqWWZ09Kh3uyBnykunH_CW3ODoWm2blm3ULQpqZp2z9GBMU757-tCxI858eEAgOUpXxhJNpHa9mFuBCpAeKT3Eq9-4UNI38SG66QsSSA1wqnKSkerPyzfFRIK7Gqb1rx-6w2CHgKzCJgsm0jxKVH-GMsUZig1iMRZY1agd8LHDOvpPshVTglY3_m0VT-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیوی منتشرشده در خبرگزاری رکنا، لحظات پراضطراب داخل هواپیمای بوئینگ ۷۳۷ شرکت سپهران را نشان می‌دهد که دوشنبه ۲۳ شهریور پس از برخاستن از فرودگاه مشهد به مقصد کرمانشاه، با ترکیدگی لاستیک مواجه شد و با گزارش آسیب به موتور، مجبور شد به فرودگاه مشهد بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78394" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78393">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nKFs-oV529Gn15hHRUWxfrUmsO-_cz-0ezjS_qVGMVvj2MJ9P_dU6kLco8F6ZWmzubdQu6_LnxHKEp4pFbeyOy6kK84tywzd3dgU_hFapt3stZJETb9YHdTyxfdnFUVbGqENaVH1CfSmM7_ufnxy74ysryV7v26WKUiIT9mUIOthTfRAcBCJfu4CGfBi0s6t7eG77WUPs0MBqwZfUwcOfY7cyBgVzwUB-bpar5kOznTIpSO3NT31j2eh2-pA-uzjXtYt1XmlVAYK_RCqdKtPaMCN0CeIiSmmcNyhltRM72aKENEQaYptYcbgPmLV1Cfvqb0jsXoTUMIhncoYVn7ImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل دادگستری روز سه‌شنبه ۲۴ شهریورماه با انتشار پیامی در اکس، از تشکیل پرونده کیفری برای رضا درمیشیان، کارگردان سینما و تئاتر ایران خبر داد.
به گفته رئیسیان، سپاه با شکایت از رضا درمیشیان  به اتهام تبلیغ علیه نظام پرونده قضایی تشکیل داده رسیدگی به شکایت از او در شعبه هفتم دادگاه انقلاب تهران در جریان  است.»
رئیسیان با اعلام این خبر گفت در دادسرا برای رضا درمیشیان قرار جلب صادر شده و سپاه پاسداران به عنوان شاکی، تقاضای توقیف اموال او را کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78393" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMCpuZ_RKZTx6tNI0HIGOKosGBtd13FSEdhOMgkpJBQbqayAKcmykLfvlWKu55KFQtgLXDQ1avEvlTWPI04J8eAD8UxXmJlRqNY4SSIcxXVglbXrCxgT-bFo2FmG6vpG0ppcuwqSBsqeTFutU2LQ-p0lcOPeK9VXnEuxq6dlA72vKPSqU70Sxfvh7dLrU4bTEsmKmCoaUY9JNSUe2YqOFR8W1co2uGrbQx42LIvM-nSWOGMJ8zEoc7njbmipSu4vP3KIZMKYWuk60v33ZX0gAFyhN50NFKZrCXz60zYr_dsOuozZUs01PoWihKefyuqnI8Uexnw574tyT4_UNcxRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استودیوی «کارگاه» با انتشار عکسی از آزادی «آریا کسایی»، طراح گرافیک و یکی از بنیان‌گذاران این استودیو، پس از نزدیک به دوماه بازداشت خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78392" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78391">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fOpgmt8eIScCovDx7iAx8t4HHG4BTGAfkarhvQBp5O4-lYtbEyo8ysnvR6mVjXx5IIqYM_qv5FLFpvY9a3_wLvBaBR-_K_7JVQyUaW3O-O7rCkSplTbPOblhTkHid0oGEe3vNgYkzkG2qgQf3bvH6NXjVpVmiRojzOym6A4f-qLaw-cb36H2lmVubY-nb8YZDAHIk61Cmukv3vl-S7wFOr7G66wM0WpEoPcupsGjt2XopwHOwt75pz9L6hpI2QYi3c_gAdz8LOtuYDDxPbK0Pkb71A7oyrXYrg99r3zvX7qS8MT-6myUlP2gmL5cARQ-TROFp5UFCe_nAfE5fQPW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس تهران می‌گوید فردی را بازداشت کرده است که شامگاه دوشنبه ۲۳ شهریور به سمت «جمعیت حاضر» در میدان پونک تهران سه کوکتل مولوتوف پرتاب کرده بود.
میدان پونک از جمله میدان‌های تهران است که از زمان آغاز جنگ ۴۰ روزه تجمعات شبانهٔ حکومتی در آن برگزار می‌شود.
بر اساس بیانیه‌ای که فرماندهی نیروی انتظامی تهران منتشر کرده، «این فرد حوالی ساعت ۲۱:۳۰ از بالای ساختمانی به سمت جمعیت سه کوکتل مولوتوف پرتاب کرده و پس از آن گریخته است».
در این بیانیه ادعا شده که این فرد «قصد خروج غیرقانونی از مرزهای غربی کشور داشته اما ماموران با شلیک گلوله از ناحیه پای راست او را دستگیر و به بیمارستان منتقل کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78391" target="_blank">📅 15:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdKoNJ4ukWJr_GrW29kdaQ3jOsW8_Hv4_pPVcuqgmKlRH9-XoZdMFltZcmbJ0E-F6VeeMwAFAkAjNIoqQZv2tF8QfThz7hbwmSgiXZULW_aMSn9P4S9Mlq_ZJqMMUVE73wdeyP04QTnt6CqhIorA7HT_Pu8VtcxtDbQ4M7Bpf7Y-Q4Ngot9zQMFr33NMcaO9ulZCZF9IAIdzBg9DYsXnQv4xznz28f9mykdtOIs919aCnzReRxVGdfbFXuieK11D-B3g4EhhE-KUfRTFgRVXNMaQsEK1mPsy-LlX98VNIgKGsn8GEIYgjZCEOGnbajhKbKUojrxdaymyL4WT6u9Wqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش رسمی آمریکا از هزینه‌ها و خسارت‌های جنگ با ایران منتشر شد
یک گزارش رسمی نهادهای نظارتی دولت آمریکا می‌گوید جنگ با ایران به «کمبودهای راهبردی» در ذخایر برخی تسلیحات پیشرفتهٔ ایالات متحده منجر شده است.
نخستین گزارش رسمی نهادهای بازرسی دولت آمریکا دربارهٔ عملیات «خشم حماسی» که روز دوشنبه ۲۳ شهریور به‌طور عمومی منتشر شد، می‌گوید مصرف گستردهٔ تسلیحات در جنگ با ایران «به کمبودهای راهبردی در موجودی‌ها منجر شده و گلوگاه‌های پایهٔ صنعتی برای تأمین مجدد مهمات را آشکار کرده است».
بر اساس این ارزیابی، پنتاگون برای مقابله با این مشکل در تلاش است روند خرید تسلیحات و زمان تولید را کاهش دهد و ذخایر مواد و قطعات حیاتی و برخی مهمات را افزایش دهد تا در شرایط اضطراری امکان افزایش سریع تولید وجود داشته باشد.
این گزارش همچنین نشان می‌دهد آمریکا تا ۲۹ ژوئن (۸ تیر) حدود ۳۳ میلیارد و ۴۰۰ میلیون دلار برای جنگ هزینه کرده است. نزدیک به دو سوم این مبلغ مربوط به مهمات مصرف‌شده بوده و ۳ میلیارد و ۷۰۰ میلیون دلار به تجهیزات از دست‌رفته اختصاص داشته است. بر اساس این گزارش، ۷ میلیارد و ۴۰۰ میلیون دلار دیگر نیز در ردیف سایر هزینه‌ها قرار گرفته است.
پیت هگست، وزیر دفاع آمریکا، اواخر ژوئیه (اوایل مرداد) هزینهٔ جنگ تا آن زمان را ۳۷ میلیارد و ۵۰۰ میلیون دلار اعلام کرده بود. شبکهٔ ان‌بی‌سی نیوز نیز پیشتر به نقل از مقام‌ها و افراد مطلع از برآوردهای داخلی گزارش داده بود که با احتساب هزینه‌های گسترده‌تر، رقم واقعی جنگ می‌تواند به ۸۰ تا ۱۰۰ میلیارد دلار رسیده باشد.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه و همزمان با انتشار گزارش ارزیابی «عملیات خشم حماسی»، در شبکهٔ اجتماعی تروث سوشال نوشت آمریکا اکنون بیش از هر زمان دیگری در تاریخ خود تسلیحات پیشرفته تولید می‌کند و این تجهیزات به‌طور روزانه در اختیار نیروهای آمریکایی در خاورمیانه و دیگر مناطق قرار می‌گیرند
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78390" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78389">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ttej4ZsjUnkUId5KjAdIcd8pCTCt2R0UvMDImHj4c-ti_zxTr94IN0QFVQuIRu5ic8Zxn6K-k0jf-UPULQT-ktS0Do9GM5IwPtvG2z2mybi-GF0tZDCBerTAwG4euxKnT5HqnVl7KfabBW-efO6sNmTseG-gNHb1oqtKRagUvmLs7O4tOJqGYM4nvPlKk73ypR_rsxM-Rvps2vshpv9RtEzYsJwv2HwL17GPb5y6v6W1RmonCFR6Yen0oHyqUJF6U8ki9A_UBDONwI-b9iA86YUc60LvWKcKgxipBc8Y10UUDKIgjiEvAp_XVQE3Dx9TDLwM9pdul518p1eqbuFRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پروژه امنیتی با نام «علاج» با انتشار اطلاعات شخصی شماری از ایرانیان خارج از کشور، از شهروندان خواسته است افراد بیشتری را شناسایی و به این سامانه گزارش کنند. صداوسیمای جمهوری اسلامی نیز به تبلیغ این پروژه پرداخته؛ پروژه‌ای که مشخص نیست چه نهاد امنیتی یا حکومتی آن را اداره می‌کند و اطلاعات هویتی منتشرشده در آن از چه طریقی به دست آمده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78389" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KT9z7ySvi4xedjhTSXs1HjWP0ngDmUU3czsiAY4VwjIGQuTAWQkGD8dF4qzFuifM79hAUJS8QABRMo50l0q_i9JsF1Sh79Wd_OyzwnoZJrqvp-AzJ1HQB3qQkEn8_wM64enwHKcbmN8H_Z9wEIYKfRCZ2g0Oe8cWRWdhJV2-ar5AxP9xxW8z3qTObp5k6_LNvGMzplOBMKQ3ExHkm0ASqlCYkYXEQEj17Co4kWU-Q9EDxMWb4St-Zisx1nI6hHj7wMxW6V3RIi0ztm5eMWWGbVNJzOeDchG3gRrTfUmadIwnjGjKJBAaEO_VbCwvk4RcLsjcD6uLL4iPT6NcvVJ3aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mkwaxU4qVgqdDIgypGXCNJ_jNe-lDJ3QtEgngFgKuHT1X15pwLJXRGQLHDo6MkYlgW33gdCXPx8QnZb1bNnTVHq-i81hycBFSwhJC-qww4SqYJsciJhd-VJSiJjdPycdkQ3w1a_uU0f0_D9mLxZrNVmC147tRYwGQ7nguVWY7dNAimMMDEPzHtaBuQkLxev3NEvdov5n8rzSKrmsCd_mWOmTUKTcn87sXGXeaYYqLy_eeg1K12UMZ7SqGQgwy5hZ7VSU4vvxDpO_UDTKyyw79FGbVQFYI29k2cNpVdmWvoyB0OdOvkCxuRgf4AiMrMSR8SOlPsTVgDaT4htucQLOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sGprd2TZJN3dNqSbD_ElQ5gkP9peP6tfEGz-CRabQNgBcmIP7J2gOeS9KU70n9KSd04LRhKkzdmaZmBA7fYw6hSpasUY2hOKh_mJQ06InLnymWSKMuvlFnqoNEdZaxUP_cYOQZqiRKDYrRQCz9TihLW9yNA_00XePfF3Ar7YR_rLtjIr2LFj_BUldeuHx7OqELYXJeiyrCp82pCo5tQJDVFWx2l1jA5BHvAQjRd7wTphSsMEjqMOpax7qqYTEWwvDqlrHGa29cWM7_p7nnhzROIZqk0UdEmpsILy7RFUre0UayztJKweeOp47VaKS0LMKHSkB2iCQKf4hokaEULoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/psBh42cRxhUmjmmz4msHIsvqR5wkuNdpH20RgG1YHkXJbNFVSiY5hqaFteWRKEqrjGcPpZGybP7VTZ-SIt-NF529dK4Qxopt4cRc8K7l9_BQWGqe6uEwfXH4cIgZtQX992bnZjkEOwePFqZoXHSxJE2io65pgPPq4VPBFQVBukgtC9Dwz-muzDf0P4l6D1ryP3PiOVW2IlKb-uFox1ZGoiuh-jqG_ZKiVcX8gSNEty8zkVL7NMTn6cE22O75XmaNC0H-gtIOIeQmbjI74Gc1RAOEUvfJA1o6ZpCoxmpCTeMxYCXhEN6fTtV5mflo0qge8iR4C1b1zgVoHnqZ6KTrNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4SE3kuNQ9JCQ_7ji3_oKvq1kfSla7YRkLI208839wDNVByheRmZV5wKScWQ7tYaEeHk1R8Zrl-zcw3qAGYjEriKfGlnikLuVzfKyYIIZCgB4nNT9wQGiFuEfoatSqOVUPNeEA5CtgBXFhnLhk99OUORMBMFyBgpREBFjC7G__nMXZ1rWVkDSTds71BaFUgyY9fpA0B91UAgJKatxxVoJWK3o4Q22qfppaR3GNLOSgeu2cmL1XyaiV2ZLJ3ixeRWWcsDqd4n4PrYSmXKjZ3fp4jwunlZbgB27BRKrtoA5yce0hZfuYDFmmAYAbYtzFzrlL72h-YgNt35MFsKxfu96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UDKR1CQGCiJW6woXXu7Zh7oJzDUm6xJSTOZHe2ZEpIN92sBvhftc5O5rkgFilIQM1BMcSNriXoYrzq8TR_2VqxdQ8pPQN7Yqfl6h2hCCeuFRVF-kSK_HN6IAwL2Ktk0WYUEm_qgIb9947TOgMXJvNeF7GhkQVLUJcrNuL-2eNbFyqv268Yc8CJwBtBZ6jIHEmN8eGgK7ITCRZvMtdBr5egRAaZMjmFFCdhAxj_prV9f4z3T2_pPDLZJfn2VtVcSWS8jAoLtlt7zuKmijr69MTkcPQVUGVMwd9qIWBfQRc3BazQJGSyCLswaEC_ZaZQr4Q_BlSEGHVSOLj2MRmrQXdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«پویش جان‌فدا»، کارزاری وابسته به نهادهای تبلیغاتی سپاه پاسداران، ارسال پیامک برای ثبت‌نام شهروندان در دوره‌های «آموزش نظامی و امدادی» و سازماندهی آن‌ها در قالب «گردان‌های مردمی» را آغاز کرده است.
در پیامکی که برای شماری از شهروندان ارسال شده از مخاطبان خواسته شده از ساعت ۱۷ سه‌شنبه ۲۴شهریور برای شرکت در «دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جان‌فدا» ثبت‌نام کنند.
پویش «جان‌فدا» از ۸فروردین۱۴۰۵ با محوریت «قرارگاه فرهنگی و اجتماعی قرب بقیه‌الله»، از نهادهای وابسته به سپاه پاسداران، راه‌اندازی شد. سامانه‌های اینترنتی، پیامکی، تلفنی و ثبت‌نام حضوری برای جذب افراد بالای ۱۲ سال در این پویش در نظر گرفته شده بود.
@
VahidHeadline
دیروز کلی پیام دریافت کرده بودم از شهروندانی که می‌گفتند در این پویش ثبت‌نام نکرده‌اند ولی اون پیامک براشون ارسال شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78383" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGnqXp2sajknQyp_hVQoY3QgrqspKwbQBLkGqnOVCDGvMySk5bbx7VT60bDUbIggojF1SkDtiYkO76w_U4-rRrsLLPZ8WjBI4aGJs3VbYuIr6OfqSd5N2ObdJV2uvkBQVEQC22nblYNCnHVGLjKhWQzBYvNjStcUBGvVhT1DNCl2Uu0hCB9J0zTmyq9ig-lFij0t7HeJQWvEppz-qIhQ-BYvdSH7lQRmgwfAwicX-3c-862_-AfOf9cdKBaBmnGoBQClm7E73SW8i5oVWe07QPY55-V0drWbyEZenokeziVtwAtjrM8Y5fcOlIyw-LDlPs1TuGa_gBcIJp4lIkri8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دادگاه فدرال آمریکا روز دوشنبه، ۲۳ شهریورماه، به عدم اجرای دستور دولت دونالد ترامپ برای محدود کردن مدت اقامت دانشجویان و خبرنگاران خارجی در ایالات متحده حکم داد.
‌این دستور که به گفته قاضی دادگاه به دلیل «استدلال‌های بسیار ضعیف» دولت صادر شده، قرار بود روز سه‌شنبه به دست وزارت امنیت داخلی آمریکا اجرا شود.
‌بر اساس قانونی که دولت ترامپ سعی دارد به اجرا بگذارد، روادید دانشجویان خارجی و روادید افرادی که با برنامه‌های فرهنگی در آمریکا اقامت می‌گیرند، به چهار سال محدود می‌شود.
‌این قانون همچنین می‌گوید که روادید خبرنگاران نیز نباید از ۲۴۰ روز فراتر رود.
‌هر سه گروه، بر اساس قانونی که اکنون دادگاه جلو اجرای آن را گرفته، برای اقامت بیشتر باید بار دیگر اقدام کرده و روادید خود را تمدید کنند.
‌به گفته قاضی دادگاه فدرال، اجرای قانون جدید تعداد دانشجویان خارجی و روزنامه‌نگاران و خبرنگاران در ایالات متحده را به شکل قابل توجهی «محدود خواهد کرد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78382" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptwPQ9XbBfoQ6JX5MjlimzET6au1JvVbuG0HEItw8gvrxpO-n1Nv89YDFFGUl0RIstM9F4zPrOPzr1iB41qLyIc4wkZbuUtqjCfNEa4SEl0nPOv3qbBDeHN0WabfN9PqHNPhBBgTCB-h7e3dZMyrtzkHnFDGkZCjjHsTBkesJOyEI3X30xAaap9j4msLXA9v1KyHnx1g-fSUGJZASunGGVZH-XK7UEv_pkq1CfDvokX_KNw0EvE_we8BF36Vq-hw887c_kjREc-8YKkIsh9P5aNYP0pu3fPrbYLV27fTBAl-gmw4mkoEzkT-o1zjx0wj3NflYf1xB7Ex5pQLARTA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه اتریش اعلام کرد برای سفر محمد اسلامی، رئیس سازمان انرژی اتمی جمهوری اسلامی، درخواست معافیت از ممنوعیت سفر سازمان ملل داده بود، اما درخواست رد شد.
بنابر اعلام این وزارتخانه، رئیس شورای امنیت سازمان ملل به وین اطلاع داد که درخواست به دلیل نبود اجماع رد شده است.
وزارت امور خارجه اتریش افزود با توجه به تعهدات بین‌المللی این کشور، ورود اسلامی امکان‌پذیر نیست.
اسلامی در راه وین برای شرکت در کنفرانس عمومی سالانه آژانس بین‌المللی انرژی اتمی بود که اجازه حضور پیدا نکرد. او از سال ۲۰۲۱ در همه کنفرانس‌های عمومی آژانس شرکت کرده بود.
ممنوعیت سفر از سازوکار «اسنپ‌بک» ناشی می‌شود که تحریم‌های سازمان ملل علیه جمهوری اسلامی را بازگرداند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78381" target="_blank">📅 15:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a9cjvp1lbAfgUtI-a8R-xhRUmW_kVLFX4XaCG-vh3G4VPxkuCFALnxrtD0zys8NwV0F8blhUchNdtfEITQrwEO4WKfs3qhUVgrgmR-cvsVRHQZAyFIwwGCDlauOj3KM2hAe7c3NJquBGBrs20HJJI0US4E0wyF885veaBg7rheTP2BxFJ7def_utPaVXRy-5wrHtUMr0ZMWJfGefMG0GAafUrtZ-wHWaMaI45-PhsZGydcPjDL3GkwYX2_Gui203QOf1uiQTEah2Yl2YLEqR-joCM9h05jXdkifAJysQYSZ8vCcfQoQF7Jw84HtTfPt-f_F2_C-5Z1damZk4sJzQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش الغایا پس از حمله در سواحل عمان و آتش‌سوزی در موتورخانه، به یکی از بنادر این کشور یدک‌کشی می‌شود.
بر پایه گزارش رویترز به نقل از مقام‌های عمانی، ۲۳ خدمه از شناور تخلیه شده‌اند و دو نفر همچنان مفقودند.
روایت‌ها درباره علت حادثه متناقض است.
سپاه پاسداران اعلام کرد الغایا با پرچم پاناما هنگام عبور از «منطقه ممنوعه» جنوب تنگه هرمز با مین دریایی برخورد کرده است.
فرماندهی مرکزی آمریکا ادعا را نادرست خواند و گفت شناور «ماه گذشته با موشک ایرانی زده شد و از کار افتاد».
سازمان بین‌المللی دریانوردی گزارش داده بود الغایا روز شنبه آسیب دید، بدون آنکه علت را مشخص کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/78380" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYdA6dOqQqC_3dXMwW7upfSMlck9Myj9crvoFtnusScZAdYTtU0VsDL1ZIyOX8E5hoSBLEMo8-Rn3y5SbV2TC_W9QBr9TMC0Bfapd3bZIPaOnuKn3Ga0c5FAiiPGarISuuMlCGg9Sly18ryhaIoxWb5bL0OcwIFghndUjoL0MefbJyc0NHoKuSzCBnc20hwhKneNDpFNYvTm4-NmknsBEovPpUAzqwaxv6-H-1iDoZqxqI6KMu_yDBlFrwAseP8qbvwEXYz07MYw1Dd9Z4zmzKoBbpvlu2smm2HLcDBuFVlDpuvauiP4qdldfimztlFiwUFZw7GqOgnrpMmIIZzsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست‌کم ۱۰۰ معترض در ۱۳ استان ایران در خطر اعدام هستند
سازمان "حقوق بشر ایران" اعلام کرد دست‌کم ۱۰۰ نفر از بازداشت‌شدگان اعتراضات دی‌ماه در ۱۳ استان ایران با حکم اعدام روبه‌رو هستند؛ بیشترین شمار این افراد با ۴۶ نفر مربوط به استان اصفهان است.
بر اساس فهرست منتشرشده، پس از اصفهان، ۲۲ نفر در استان‌های تهران و البرز قرار دارند.
همچنین ۱۰ نفر در فارس، هفت نفر در خراسان رضوی، پنج نفر در مرکزی، سه نفر در یزد و دو نفر در سمنان در این فهرست ثبت شده‌اند. در استان‌های خراسان شمالی، گیلان، اردبیل، ایلام و قزوین نیز هر کدام یک نفر با حکم اعدام روبه‌رو است.
این سازمان می‌گوید فهرست منتشرشده تنها شامل معترضانی است که دست‌کم در مرحله بدوی حکم اعدام دریافت کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78379" target="_blank">📅 15:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rIweNt0DMJ28sQGBNhuMQP5PE2-uKuPS-AmUDcsgkx7Jw6vUlFdUmUivezZaGHd_fgA4NIojjgbkKQ0lwbCMTPxISdl0OHYXLS4gJoTS18Lxlvf4PetfUAfO73HpMxjYpw6QtRR-DUrD1aWv8dvRZT4C_Roz2PLY-qEuhzZkEK8PFt_UzG3XBCEHudV26-VW08y8ybVUForC5vkdfLDk4F-xuGujZEYIP9Ty7tQ3bgjfRgozg1nz9deW36Nq1aNcnjLZeCFlmhytQDQhbEw5C6nhH6NGewkcDHEbaHp1oAPs-xlcQXM7-uLjLeMNposlcKHsqyEy64EJNLRD0pQenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، شامگاه دوشنبه ۲۳ شهریور ۱۴۰۵، از حمله پهپادی به دو «قایق صیادی» در حوالی بندر کرگان در آب‌های خلیج فارس خبر داد.
بر اساس این گزارش، در پی این حمله که تسنیم آن را به «آمریکا» نسبت داده، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند.
عملیات جست‌وجو و امداد رسانی برای یافتن مفقود شدگان آغاز شده و نیروهای امدادی و دستگاه‌های مسوول در محدوده حادثه در حال جست‌وجو و نجات هستند.
تسنیم نوشته است جزییات بیشتر درباره این حادثه و وضعیت صیادان پس از دریافت گزارش‌های رسمی اعلام خواهد شد.
@
VahidHeadline
آپدیت:
اکسیوس: آمریکا دو قایق سپاه پاسداران را منهدم کرد
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78378" target="_blank">📅 03:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lYuL-J_RAF_phcCfh7ZfIT-sF3EHEIKdMfZudky9HMZieEBkZhVZNXTUMvGDQx7nzYV08t-0cFzyi6uphXeNwi9pbfKtNi-ktGnkLu59v2QQcRaoCdKTXYN2WgSOxDW24TvyzxagLY_DMFhWJIT_MK_PQLFC45VRYmdn_32Z7g6pzKyWQp2mZopwj06G7TxT4Vx8PO1PYUc11hnsUbbFw_Cq-wUDEz0KMyOVF8RYBuVSYXMK-U3YfCiUr61r5tOFd5Pbg8O9fWO8Ow1NEO61ESEtUNwwcp1u7b4pvVKZctw7C1b9J_QTMwzfZ5-CW7VP9u-2EmTBXrAo1Zh1pI3B_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی نیروی دریایی سپاه می‌گوید یک ابرنفتکش که به گفتهٔ آن قصد عبور از «منطقهٔ ممنوعه در جنوب تنگهٔ هرمز» را داشت، «بر اثر برخورد با مین دریایی منفجر شد».
خبرگزاری‌های ایران شامگاه دوشنبه ۲۳ شهریور با انتشار بیانیه سپاه، نام این ابرنفتکش را «اِل گایا» به شماره دریانوردی «۹۳۲۵۳۳۶» اعلام کرده و افزودند که «تلاش برای مهار آتش بی‌نتیجه بوده و کل نفتکش در شعله‌های آتش گرفتار شده است».
فرماندهی مرکزی آمریکا (سنتکام) این ادعا را «نادرست» خوانده و گفته که نفتکش «اِل‌ گایا» که با پرچم پاناما حرکت می‌کرد، ماه گذشته هدف موشک ایران قرار گرفت و از کار افتاد.
@
VahidHeadline
پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است یک نفتکش با پرچم پاناما اخیراً در تنگه هرمز با یک مین دریایی برخورد کرده است. این ادعا کذب است.
✅
واقعیت: نفتکش «El Gaia» با پرچم پاناما ماه گذشته هدف یک موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، ایران بار دیگر این نفتکش را در حالی که در آب‌های ساحلی عمان قرار داشت، با یک پهپاد هدف قرار داد. این نفتکش در حال حاضر توسط یکی از شرکای منطقه‌ای یدک‌کش می‌شود.
ادعای کذب سپاه پاسداران نمونه دیگری از دروغ‌ها و تلاش‌های آن برای ارعاب است؛ آن هم در حالی که می‌کوشد مانع تردد کشتی‌های تجاری در تنگه شود
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78377" target="_blank">📅 23:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KoxfmJXskzynmalW6Mv3-lnsqU81fDAMmSexr9Jmmiv60s6FuO94acJueZjJtKdikvagDOSTCPwQ27PlfG0cT_O7yNZIH-25vulZLNsGt5MCQkrdBvOoifpjtiM5BQKJjhMTvC7KEQXWY2HQmI0VQ0SzKmLyp_j60H0PCuq-9zYj4vqPeblecEHFKtcmOs16kWUMQhHvB3orhT625l_9FzjT8tn1lnqnV0fD1goiEWa4GuFJosZulelTK9XthPcXtRe6DoE2OfYsF2NUjJX49-urU7MhD5vPkOlV7LIIh_9glJNpwAqAgrT3GSirR75-Wvye23e3KYLsV_l2ih3CwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Es_6qWdQ5HlFQCNirPb2VFwp9kFjSjOA1O9S-ixH4YPjv1Po8L3sYMYRuHmpC0RNM4A5Z16qXdQYFp7mloc1Q3pz52cUL5WJRKPvx5TTkbNxJn4yXMJ5rMfGpw-zNfsNGGWgR_qKGOFY_w-18MnCGrtWDKW-uRxdWMzItY92aO1jlDfsBLJ6LE1Ge5PZLxzcOJIO7N02q24eiKF3iVlkg-SOo7b_OW94yhFrdxBsWmRSS1HnLUPbtzeKIJMd0Q-8mURD72OOKQdFsIbvONqdTznuqvrFBHfdsUmqkM3rs0BPCYihDf-7NqYDsPV94SETeYhQ4XgFnl7dNuyc5aL38g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پیامی در شبکه اجتماعی تروث سوشال تاکید کرد که افزایش قیمت‌ها در سراسر آمریکا ناشی از سیاست‌های جو بایدن و دولت او بوده است.
او نوشت که حتی بهای نفت نیز در دوران بایدن بالاتر از سطح کنونی بوده و دولت او مانع از دستیابی جمهوری اسلامی ایران به سلاح هسته‌ای نیز شده است.
ترامپ با اشاره به اینکه قیمت سایر کالاها به شدت در حال کاهش است، افزود که بهای نفت نیز به محض پایان یافتن درگیری نظامی با ایران—که به گفته وی زمان زیادی تا آن باقی نمانده است—مانند یک سنگ سقوط خواهد کرد.
در دوران ریاست‌جمهوری بایدن، به‌دنبال وقوع جنگ روسیه و اوکراین و بحران‌های بازار انرژی، قیمت نفت در بهار ۲۰۲۲ به بالاترین سطح خود رسید؛ به طوری که قیمت نفت برنت تا حدود ۱۲۷ دلار برای هر بشکه افزایش یافت.
@
VahidOOnLine
رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال از کشورهای جهان خواست پس از پایان درگیری‌ها، هزینه‌های ایالات متحده را برای حمایت از کشتی‌ها و کمک به عبور محموله‌های نفتی از تنگه هرمز بازگردانند.
ترامپ با اشاره به اینکه نفت در حال عبور از این آبراه است، تاکید کرد کشورهایی که هیچ کمکی به آمریکا نکرده‌اند، باید خسارات و هزینه‌های این اقدامات را جبران کنند؛ زیرا واشنگتن این ماموریت را بیشتر به نفع دیگران انجام می‌دهد تا خودش.
پیش‌تر کریس رایت، وزیر انرژی آمریکا، اعلام کرده بود میانگین تعداد محموله‌های نفتی که با حمایت نیروی دریایی این کشور از تنگه هرمز عبور می‌کنند، رو به افزایش است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78375" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nF-pyCuimvx-JPubJHMgmsd8rWRuytGW3-mJORHMlTRTX1kgONMixUwvGcSUbz9CXvqEpMHB7tmVh2S3SRWdEiN-Y_XP0tyfXxKuZY8o1zP8IjXK6KvrJ2_0_3121rXqPDoH7hst40pe0vSNLHsMmzLtVmC7csFUejSOwha90u-gjXs1iWz4k1QNAvJKSUB3r3fgajLHaftYA8Dr_yG5emxfJJwsj9xApNaE4cEPt5p-os16u4AV9TQfuX1WvYKa6WafFsfen_HU1xhl3hC-nDKMa2c8-GyYNTdWj_bXXVdGV2c80ERmIFaZ44wXfc-AoRmSqwI9caX2FH_kVk1hOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایرانِ شکست‌خورده می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
من تصمیم خواهم گرفت که آیا ایالات متحده آمریکا وارد مذاکره بشود یا نه — ایده‌ای که نسبت به آن آمادگی داریم. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
ترامپ نوشت: کشور در حال ورشکسته‌شدن ایران می‌خواهد سریع و به‌شدت به توافق برسد. من تعیین خواهم کرد که آیا ایالات متحده آمریکا وارد این داستان خواهد شد یا نه؛ چیزی که ما نسبت به آن نگاه باز داریم.
پس از انتشار این پست قیمت نفت اندکی کاهش یافت.
اظهارنظر اخیر رئیس‌جمهور ایالات متحده در حالی است که ایران گفته برنامه‌ای برای مذاکره با آمریکا ندارد و شروط متعددی را برای توافق با واشینگتن اعلام کرده است.
در همین حال، اسکات بسنت، وزیر خزانه‌داری آمریکا در راستای برنامه فشار اقتصادی بر ایران موسوم به «عملیات طرد اقتصادی» از همه افشاگران خواست تا چنانچه اطلاعاتی درباره «تسهیل‌گران تروریسم ایران» دارند در اختیار وزارتخانه تحت امرش قرار دهند.
او با انتشار پیامی در شبکهٔ اجتماعی ایکس خطاب به کسانی که در سراسر دنیا اطلاعاتی درباره شریان‌های حیاتی اقتصاد ایران دارند، نوشت: «این شانس شماست. اگر اطلاعات قابل پیگیری برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت جایزه باشید، صرف‌نظر از این‌که کجا زندگی می‌کنید یا چه کسی فیش حقوقی شما را امضا می‌کند. اگر چیزی دیدید، بگویید».
او همچنین بار دیگر تاکید کرد که وزارت خزانه‌داری آمریکا عملیات طرد اقتصادی را «برای قطع تمام شریان‌های مالی رژیم ایران و حامیانش» آغاز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78374" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=vC-OydH-laQROFkZu6joTiQBAF7Hmr8yf1z6GD_UaHHcR0nK4aIJYayWro3wvlUeeDcg3MSUH4yO6hh9N3GPPxPUv5tKWmjQO_yOj5_TTzYtB4PuL8mlACOtgXJvUOmiVijaQYLlw8laBvMI_YWHkaGsz9om9kSB76KzSda_nf5ngKPVBJnskG1hadmSn81_FTNU5c1N3SeIvklFhpf6vGKzcTjJ_KMdWSE562yQNKIQIg0zCRwUV1CQWXocXK0q85-Nb65pS9m_OuvjssuVW3lnu-5yBbMrQT4PZMFyhpiVvFCWoVOJWlnX51f-L0U94wEyVas9d1vRKztjMWVeng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/078a1aea27.mp4?token=vC-OydH-laQROFkZu6joTiQBAF7Hmr8yf1z6GD_UaHHcR0nK4aIJYayWro3wvlUeeDcg3MSUH4yO6hh9N3GPPxPUv5tKWmjQO_yOj5_TTzYtB4PuL8mlACOtgXJvUOmiVijaQYLlw8laBvMI_YWHkaGsz9om9kSB76KzSda_nf5ngKPVBJnskG1hadmSn81_FTNU5c1N3SeIvklFhpf6vGKzcTjJ_KMdWSE562yQNKIQIg0zCRwUV1CQWXocXK0q85-Nb65pS9m_OuvjssuVW3lnu-5yBbMrQT4PZMFyhpiVvFCWoVOJWlnX51f-L0U94wEyVas9d1vRKztjMWVeng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رشت، حامیان حکومت شبانه به آشکده سحرخیزان حمله کردند.
در ویدیویی که آشکده سحرخیزان منتشر کرده بود، عبارت "آش برای افراد با حجاب رایگان است"، به دیوار نصب شده بود و در چرخش دوربین، چندین مرد محجبه در صف ایستادند.
همین بهانه‌ای شد برای یورش و تخریب مغازه.
این اتفاق یکشنبه، ۲۲ شهریور ۴۰۵ رخ داد.
دادستان بلافاصله علیه آن اعلام جرم کرد و مدیر رستوران بازداشت و خود رستوران پلمب شد. ولی انگار این واکنش از نظر لباس شخصی‌ها کافی نبود و دیشب ریختن رستوران رو تخریب کردند.
via
pkhwshhal
,
yaghma_fashkham
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78372" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشگاه تهران - دانشجو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2iCtn2TQlrExDYPbJ4oaoE6TBgChIfW2Y3Z2EDxuVcGfA4sbNQdvSJ9VYOcMJGemoOU8QnewTSLeuaDa4uX1vIn6zmeE2FguFUDhbwYKwCsJ6xONv9ckJYjL2R_p-8-Vj-K-YD_jxR0QHixvXj2vEWQ5y8rAex2NRa7H0mltLtHBp1HDoCTF1gD8dmdL98YHnK9l81gYJSFsaxWbYaBtgW8-ccudjJpB-m08aDVH79aDmlm8__Y4fFMRumPMhDh9JVv6_BWv5tjPHDppQ2jv6dEAaeNfNr1f8-R_T0qnXejnQHbOgR1ZuBYkGPHvVenDaV5bfjU-DO1Nf7AGaZWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اتهام «بغی» برای محمدپارسا گلچین، دانشجوی دانشگاه تهران و دارندهٔ مدال طلای المپیاد!
بنابر گزارش‌های رسیده به تهران-دانشجو،
#محمدپارسا_گلچین
، دانشجوی ورودی ۱۴۰۳ کارشناسی ادبیات دانشگاه تهران و دارندهٔ مدال طلای المپیاد ادبی، به «عضویت در گروه
باغی
» متهم شده است.
همچنین، «اجتماع و تبانی علیه امنیت داخلی» و «اقدام تبلیغی بر خلاف امنیت ملی» دیگر اتهاماتی‌ست که به این دانشجوی نخبه وارد گشته است. او در جهت دفاع برابر عناوین مذکور، به شعبهٔ ۲۶۸ بازپرسی دادسرای عمومی و انقلاب مشهد احضار شده است.
محمدپارسا گلچین، شنبه ۲۲ فروردین ۱۴۰۵ به همراه جمعی ۱۸ نفره از دانشجویان در جریان یک بازدید دوستانه، توسط مامورین مسلح و به‌طرز خشونت‌آمیزی بازداشت شده بود
. پرونده سایر بازداشت‌شدگان نیز در جریان است و در انتظار دریافت حکم و احضاریه هستند. درصورت دریافت اطلاعات تکمیلی، گزارش پرونده‌های سایر دانشجویان متعاقبا در تهران-دانشجو منتشر خواهد شد.
#سرکوب
#بازداشت
#دانشجوی_زندانی
دانشگاه تهران-دانشجو
اینستاگرام
🆔
@Daneshjo_UT</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78371" target="_blank">📅 17:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=GH50nRjVW47Wb87LLs80-zZ-NU0pcClM5NPHTCB7kWyyD4bCnCcnfds947Bgkt3U1pqVdKDk9kNsXJ7dyjEf5uPAidYkvX0GZm5t_vdQUsvVRM1DfF2ZXj24VM7ZBPLHV-Ho5-7moLDUphRd4iiAGJdiD6ziaRcUMIGK6IJelSBDId8BixbIIte8YsxiJVcvWIDM7aSy2JXupuDTJ8cUUVkrPrToQo_c8lG2OLkCPhXAedzwTropMGfXjEY2lWXsp6VHqwH5fugvQCsrTQlu_jT-kDJCM-Z1AKSlmWAb5vWzhJq0Ji_3uqie9UZdi2F6hFEMaonIANk41_taqdAlxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d288c0bbe.mp4?token=GH50nRjVW47Wb87LLs80-zZ-NU0pcClM5NPHTCB7kWyyD4bCnCcnfds947Bgkt3U1pqVdKDk9kNsXJ7dyjEf5uPAidYkvX0GZm5t_vdQUsvVRM1DfF2ZXj24VM7ZBPLHV-Ho5-7moLDUphRd4iiAGJdiD6ziaRcUMIGK6IJelSBDId8BixbIIte8YsxiJVcvWIDM7aSy2JXupuDTJ8cUUVkrPrToQo_c8lG2OLkCPhXAedzwTropMGfXjEY2lWXsp6VHqwH5fugvQCsrTQlu_jT-kDJCM-Z1AKSlmWAb5vWzhJq0Ji_3uqie9UZdi2F6hFEMaonIANk41_taqdAlxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
پیش‌تر نیز در سال ۱۴۰۱ نواب ابراهیمی، آشپز، در پی انتشار دستور پخت کتلت در اینستاگرام خود همزمان با سالگرد کشته شدن قاسم سلیمانی، بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78370" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nAmDQk1lp61yFWGJAu6LV4mqk_Dj4aLI93ZbomBXZJYhZ9tBMiSp-kgbmQIbOurUVtEdQCfkLhSR2iov0YnqxZHifxVXOIE1RCouFi-mF5-f5Gh08HAAeAs0-F78ZHNirMu1_5AmR3dr949W6tZ-Owv3ObBGdiJBp0N2qEyH3gYHCwGoC-gB78iNKtDoYAJAGVcEztEt7_Wop2PuGlBBSGpM6fFBSp0COLKjhQ_lWJmV4P94078NneB1swUeE2wZfIC2De6asi8fhs9oQ9vTRelGroC-FZJ2GvfzvGwoh1uFqNAt2ZsWJ0BbS5JtlatP_5e-wckmGfJJgUXHukz_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MuPsNh_jg2YR8hq5NeetUBn6bBRt9TGeTraSL6FTXY2pkqHpiZuCvSJEboibGffyinYGHCnjcL7Hw3JuHEXkPCPR8AG9c1lbJdx7xZ-I6E9ae4yXLI3kkJieShmS8bRlXGitGNOR9fSY8QuYk2Ri7SbfmvO-BfB5UuEEApMphFRn4tG9CsfzUgLnaV2j4usZBkSjpF4p0L_Soou_-8jcFVnipDnV1p_OWOzW5nBwgJhOMXJgdOt19GeFVgFSlGigGUqUtAM-298oQ1PjI5khsJ8I022enFHSVJb93G1i73YWvOkAJ155aj0jUvyoMtXS5O9QSCRBUUxUOm35Rt9UCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«یحیی سریع»، سخنگوی نظامی حوثی‌های مورد حمایت جمهوری اسلامی، از انجام عملیاتی گسترده با ده‌ها پهپاد و موشک بالستیک علیه اهداف نظامی در منطقه خمیس مشیط عربستان سعودی خبر داد.
سریع گفت پایگاه هوایی «ملک خالد» در این منطقه هدف حمله قرار گرفته و آشیانه‌های جنگنده‌ها، رادارها، باندهای پرواز و انبارهای مهمات از جمله اهداف حوثی‌ها بوده‌اند.
سخنگوی نظامی حوثی‌ها این عملیات را پاسخی به حملات هوایی عربستان سعودی به یمن دانست.
@
VahidHeadline
«محمد بن سلمان»، ولیعهد عربستان سعودی، امروز دوشنبه ۲۳شهریور۱۴۰۵ در جده با دریاسالار «برد کوپر»، فرمانده فرماندهی مرکزی آمریکا، سنتکام، دیدار و درباره تحولات اخیر منطقه گفت‌وگو کرد.
خبرگزاری «رویترز» به نقل از رسانه‌های دولتی عربستان سعودی گزارش داد این دیدار در شرایطی انجام شده که درگیری میان عربستان و حوثی‌های مورد حمایت جمهوری اسلامی در یمن شدت گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78368" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bk0UjtlSFHKuAn1VQ8e-dpWm0d7FAadBHcLEzQXBQ0n-OvO7YsHeG24T2uOcI7jq6mMjQ_D6cOd9qLKy5sGOLYEB1FcHdPqkHmqdPzouKNuwB-pgB0Xx9z8rvYZGzW8FxWCUVrqwq9IOQHEIQp4F2RXfKIjGZ3suvckUFARf_-JBijyX1A_yfpZWPGFbuXayIB9WX5lxqfB7XTioSXRFGveHlhuY_5iWc2n2PQJLiHVaFarSePMO3_oM8TA1uTryJaPnpKlkXihh5feisF9r_NUpW7zBJmhNQH5iWQjMH7qLEMDr-tE3val3ZTtg-Fi9-EgoBv-ZH3-SPFwKaMP4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین امروز دوشنبه ۲۳شهریور۱۴۰۵ گزارش‌ها درباره کمک نهادهای چینی به جمهوری اسلامی برای هدف قرار دادن یک پایگاه نظامی آمریکا در اردن را تکذیب کرد.
خبرگزاری رویترز به نقل از وزارت امور خارجه چین گزارش داد پکن «قاطعانه با این اتهامات بی‌اساس مخالف است».
این واکنش پس از آن مطرح شد که روزنامه «وال‌استریت جورنال» به نقل از مقام‌های آمریکایی که نام‌شان فاش نشده است، گزارش داد جمهوری اسلامی پیش از حمله موشکی ۱۷شهریور به پایگاه «موفق‌السلطی» در اردن، تصاویر ماهواره‌ای این پایگاه را از نهادهایی در چین دریافت کرده بود.
در حمله موشکی جمهوری اسلامی به این پایگاه نظامی آمریکا، سه نظامی آمریکایی کشته شدند.
براساس گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی نام نهادهای چینی را که گفته می‌شود تصاویر ماهواره‌ای پایگاه را در اختیار جمهوری اسلامی قرار داده‌اند، اعلام نکرده‌اند. این مقام‌ها همچنین دولت چین را به مشارکت یا دخالت مستقیم در این اقدام متهم نکرده‌اند.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، نیز روز یکشنبه ۲۲شهریور۱۴۰۵ به گزارش‌ها درباره دسترسی جمهوری اسلامی به تصاویر ماهواره‌ای یک پایگاه نظامی آمریکا در اردن از طریق نهادهای چینی واکنش نشان داد.
ترامپ گزارش مربوط به دستیابی جمهوری اسلامی به این تصاویر، پیش از حمله‌ای را که به کشته شدن سه نظامی آمریکایی منجر شد، «کم‌اهمیت» دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/78367" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D5Br2EKKgVEhME3BGaVGC_a0eC2qKJRbeg3opSitC4T6QadVIsHr5OYKF03IOVaoGJXbI9omZ57YPAPkzhi2WvHDiRqi2IL02VFnoeJ-w9F-NcNW1Oh5DBck4CXpNjHya3BXhM40nurDk_R2UX6zB_YvzzvDaPJFHbNLHNoZD0GzNe4XoMeF6lePXTLN8nRsLH7wIgCKZgKsSugWHt5C6OXxfgQAFHFQwFyn1hng6UXUHtaWeGPHGegct1ujYMKq_yd5Wz28AiRn0eJDt6QuDLDuu5aCe9eGQur9sXK-bK-duwh6861UVTaswSgroTrol_RgWLctm4X1NJiWmXQoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j-I2FFx3HnJS99MC9f9LuuogPKYX4NhcO188egcvhi-hkpplXZ01s99pV0c-gVRQC3ogbBSZ3F1gyH3qSdCPXhiUt-UNCUAAHr9NZXDhDVD7dCRQWcYLZZazfeuyjhx_NBMehhjAi_4vs72ZOBtUXLH39s2eVSi9MBtm0AiJAz3x-BOOh2JcXdfdHfb9S0uYcaCURUytP2cljy76eG7QxfUqescjvy4Buk49xoFVtmjBEcxdjDhGItixTJDinS0uivWMRrNHVqHwne8qSoWV4TTIrcLT5m7AnGTUooRQEZV0j2rb4PRi2E9AQVYfOeMAZEOCdQa8UTNwtcAsezcpMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه و پس از اعلام خبر صادر نشدن ویزا برای محمد اسلامی، رئیس سازمان انرژی اتمی ایران برای شرکت در نشست مجمع عمومی آژانس بین‌المللی انرژی هسته‌ای در وین، از احضار کاردار اتریش در تهران خبر داد.
بقایی با اعلام این خبر گفت می‌دانیم که این تصمیم تحت فشار آمریکا گرفته شده است اما این واقعیت، چیزی از مسئولیت اتریش کم نمی‌کند.
@
VahidOOnLine
پیش‌تر:
به گفته یک مقام آگاه که با اسوشیتدپرس گفتگو کرده، محمد اسلامی، رییس سازمان انرژی اتمی ایران، برای نخستین بار در چند سال گذشته احتمالا در نشست سالانه کشورهای عضو نهاد ناظر هسته‌ای سازمان ملل متحد در وین شرکت نخواهد کرد، زیرا از سفرهای بین‌المللی منع شده است.
این مقام گفت اتریش از کمیته تحریم‌های سازمان ملل خواسته بود برای اسلامی معافیت از ممنوعیت سفر صادر شود، اما این درخواست پذیرفته نشد.
این مقام که اجازه اظهارنظر درباره این موضوع حساس را نداشت، به شرط ناشناس ماندن صحبت کرد.
اتریش به عنوان میزبان سازمان ملل متحد در وین می‌تواند برای مقام‌های تحریم‌شده درخواست معافیت از ممنوعیت سفر کند تا آنها بتوانند در نشست‌های بین‌المللی سازمان ملل حضور یابند.
به نوشته این خبرگزاری آمریکایی، حضور نیافتن اسلامی در کنفرانس آژانس بین‌المللی انرژی اتمی نشانه دیگری از وخیم‌تر شدن سریع روابط ایران و کشورهای غربی است.
از زمانی که اسرائیل و آمریکا در جریان جنگ ۱۲روزه به تاسیسات هسته‌ای ایران حمله کردند، جمهوری اسلامی اجازه دسترسی بازرسان آژانس به تاسیسات هسته‌ای آسیب‌دیده در این حملات را نداده است؛ این در حالی است که تهران بر اساس تعهدات خود در چارچوب پیمان منع گسترش سلاح‌های هسته‌ای، از نظر حقوقی موظف به همکاری با آژانس است.
آژانس همچنین نتوانسته است وضعیت ذخایر اورانیوم ایران با غنای نزدیک به سطح مورد نیاز برای ساخت سلاح هسته‌ای را راستی‌آزمایی کند.
تحریم‌های سازمان ملل که دوباره برقرار شدند، شامل ممنوعیت سفر، تحریم تسلیحاتی متعارف، محدودیت‌های مربوط به توسعه موشک‌های بالستیک، مسدود کردن دارایی‌ها و ممنوعیت تولید فناوری‌های مرتبط با برنامه هسته‌ای است.
با وجود اظهارات این مقام درباره احتمال عدم حضور اسلامی در کنفرانس، خبرگزاری دولتی ایرنا روز شنبه گزارش داد که اسلامی تهران را به مقصد وین ترک کرده است تا در کنفرانس آژانس شرکت کند و با نمایندگان کشورهای مختلف دیدار داشته باشد.
مقام‌های ارشد کشورهای عضو آژانس بین‌المللی انرژی اتمی قرار است از دوشنبه تا جمعه در مقر این نهاد در وین گرد هم بیایند.
آنها درباره بودجه آژانس تصمیم‌گیری و آن را تصویب خواهند کرد و درباره دیگر مسائل سیاست‌گذاری، از جمله پادمان‌های هسته‌ای در خاورمیانه، گفت‌وگو خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78365" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78364">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvRZlqktAchNzEj0a07UvBAUpMnbx162jtYm-6l9f7UZokRkeWUXwrLLyqNcHieUPKFwk7qntnAEpAmfDzyD2I1aWBd9cV-FEYRdriFekF8lOBHMJGv-_Ov2Bu9YCutiF5EPuh4AtbgTS-n19AZXncxuKy_pAhImUB3ur5evgOSCGHVJSwMHFiD1ygOkCe1d2JpMPI6K-qy39eifLksGLopcMdKTVQpnWMyWrBtZ9V9SODqO3TEKhf5QsG5YPxPCZh5czsScTWuDKnvn2CQVAl2aOUoMK4XgvXZgJWAYSumHRWTgi_GlWBmL1YTubORm6aFf22yFaq5ytmAmHY-0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آستانه چهارمین سالگرد قتل حکومتی مهسا ژینا امینی از اصفهان، رشت، فومن، مشهد و نیشابور ‌خبر از تشدید فشار برای تحمیل حجاب اجباری و حضور دوباره گشت ارشاد، حجاب‌بان‌ها و نیروهای لباس‌شخصی در خیابان‌ها می‌دهند.
یک شهروند گفت در میدان علیخانی اصفهان ون گشت ارشاد مستقر شده‌ است و ماموران «بدون تذکر قبلی»، زنانی را که حجاب اجباری ندارند بازداشت می‌کنند و با خود می‌برند.
شهروند دیگری فضای اصفهان را «به شدت امنیتی» توصیف کرد و گفت نیروهای گشت ارشاد در مناطقی چون جلفا، مرداویج، چهارباغ و میدان نقش جهان مستقر شده‌اند و با زنان بدون شال و روسری، برخورد می‌کنند.
یکی دیگر نوشت: «در اصفهان دیگر ون گشت ارشاد نیست، اتوبوس است. با اتوبوس دختران را جمع می‌کنند و می‌برند.
...
در مشهد نیز شامگاه ۲۲ شهریور، نیروهای مسلح وارد پارک ملت شدند و به زنان تذکر حجاب دادند.
شماری از شهروندان از رشت گزارش دادند برخوردهای قهری درباره حجاب اجباری در این شهر شدت گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78364" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=blDweZyhPSKLtWV85y1LYIVh1wFuQrwE11-m8UEJcOhEfKpEePy9X9fmmdK0VJpILELhluPDwcqeND-9jhUjzL6LohUZg--F04Zaxq6liLAmlTxjZ54-feX6PPs5dQn8drZljbQSB2m8fGEvhBsBzd-6UzKI_GBUaKB3il45-ZCdKU3FqzGScnArbMPW_9mO0ydO7HwEZAHrExLowhTK3F8a_SlOHvY1XRpRO-6cXa30Q-HQl0QMex3CHuVAs6LWNrpbFzuPvJySwTMadQASAfX6Zq4JbMgTM3pRGqH3XUjABFlNJwyT0B10v6O7nPMvzaIjxTtQMF05N10XEbOLyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bc68687ab7.mp4?token=blDweZyhPSKLtWV85y1LYIVh1wFuQrwE11-m8UEJcOhEfKpEePy9X9fmmdK0VJpILELhluPDwcqeND-9jhUjzL6LohUZg--F04Zaxq6liLAmlTxjZ54-feX6PPs5dQn8drZljbQSB2m8fGEvhBsBzd-6UzKI_GBUaKB3il45-ZCdKU3FqzGScnArbMPW_9mO0ydO7HwEZAHrExLowhTK3F8a_SlOHvY1XRpRO-6cXa30Q-HQl0QMex3CHuVAs6LWNrpbFzuPvJySwTMadQASAfX6Zq4JbMgTM3pRGqH3XUjABFlNJwyT0B10v6O7nPMvzaIjxTtQMF05N10XEbOLyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ویدیوی نجات خلبان آمریکایی در ایران
۲- یک نفر از ۷ نفر سوت موشک که داره به سمتشون میاد رو می فهمه.
سعی می کنه به نفراتش خبر بده اما نمی دونه کدوم طرف بدوئه. در نهایت یک انفجار هر ۷ نفر رو می بلعه.
A_z_im
سی‌بی‌اس پس از پنج ماه با یکی از دو افسر ارتش آمریکا گفتگو کرده است که در نیمه فروردین‌ماه هواپیمایشان در اطراف اصفهان سرنگون شد.
این افسر که براوو معرفی شده، لحظه برخورد موشک دوش‌پرتاب با جنگنده اف-۱۵ آنها را مانند برخورد یک قطار باری توصیف کرد و گفت به همراه خلبان که در این گزارش «آلفا» معرفی شده، تلاش کردند هواپیما را نجات دهند اما خیلی زود دریافتند که امکان نجات هواپیما نیست و باید خروج اضطراری انجام دهند.
پس از خروج اضطراری (ایجکت)، آلفا و براوو در حالی روی زمین در بیابان ناهموار در ایران فرود آمدند که حدود هشت کیلومتر از یکدیگر فاصله داشتند و هرکدام تنها بودند.
آلفا سالم فرود آمد، اما براوو خوش‌شانس بود که زنده ماند.
براوو گفت: چتر نجاتم در حمله اولیه آسیب دیده بود. یک لحظه به بالا نگاه کردم و دیدم چتری وجود ندارد؛ ترسناک‌ترین چیزی بود که در تمام عمرم دیده بودم. همان‌جا مکث کردم و دعا کردم: «خداوندا، اراده تو انجام شود. اما اگر قرار است از این ماجرا جان سالم به در ببرم، به کمک نیاز دارم.»
او در پاسخ به این پرسش که «فکر می‌کنید هنگام برخورد با زمین با چه سرعتی حرکت می‌کردید؟» گفت: براساس توضیحاتی که دادم و جراحاتی که داشتم، متخصصان معتقدند با سرعتی بین ۱۱۳ تا ۱۶۱ کیلومتر در ساعت با زمین برخورد کردم.
او افزود: یک معجزه در روزگار مدرن بود. باور دارم این اتفاق گواهی بر لطف خداوند در زندگی من است که باعث شد از آن لحظه عبور کنم؛ به‌گونه‌ای که هرچند دچار جراحت شدم، اما آسیب‌های فاجعه‌باری که می‌توانست توانایی‌ام برای زنده‌ماندن را از بین ببرد، متحمل نشدم.
این سقوط باعث شکستگی کمر براوو شد. او همچنین دست و شانه‌اش شکست، مچ پایش پیچ خورد و سر و صورتش بر اثر بریدگی و خراش خون‌آلود شد.
براوو گفت، مجروح بودم، اما همه ما آموزش دیده‌ایم که با شرایطی که با آن مواجه می‌شویم سازگار شویم و بر آنها غلبه کنیم. با وجود جراحات، تا جایی که می‌توانستم سریع از محل فرودم دور شدم.
براوو به سی‌بی‌اس گفت امن‌ترین جایی که می‌توانست به آن برود، ارتفاعات بود.
بنابراین با وجود شکستگی استخوان‌هایش تصمیم گرفت از مسیر کوه بالا برود و خود را به خط‌الرسی در ارتفاع حدود ۲۱۰۰ متر، برساند.
@
VahidOOnLine
چیزی که می‌بینم رسانه‌ها و کاربران فارسی‌زبان دقت نمی‌کنن اینه که این مصاحبه نمی‌گه که افسر آمریکایی با دست و پای شکسته کوه ۷ هزار پایی رو بالا رفته؛ بلکه می‌گه خودش رو به ارتفاع ۷ هزارپایی رسونده. بین این دو تا خیلی فرق هست.
در نظر داشته باشید که خود اصفهان بین ۱۶۰۰ تا ۲۰۰۰ متر از سطح دریا فاصله داره. یعنی ممکنه ایشون فقط با صد متر صعود خودش رو به ارتفاع ۷ هزار پایی برسونه.
Ardeshir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/78362" target="_blank">📅 08:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ypp12ZDpE_bKMayPKrjFXqHJ8EokomJdF1AiHrerZLPFiU-Sd2L-AaOls4nrr5WOYvwHJZSIrDQ-c31Ch_b8VSuk7p0e1v-0_6G_eH2FCzip80wlzSlkXoYololbU1g0O0S9PHNlyUVeV0CO_uIerPnpt2tynaqTWC3JfSI5xNe_jpZ0zhLXXKdpkFt1cRVqMWiqm7Xu3zlatcOnjPKObwQ91hvpHp8sJlSzlY2uh6p-INGDJ58pJdtcsxYnzT_q39IeUgVMB32QkpyAhJ_-XM5IVswplhdVZLUNcaJca22dbDtza2O5qXVgw5FqXN-cvMDJabJ7GoBRlFsBHSY7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه عمان از تعویق‌ نشست ایران و کشورهای حوزه خلیج فارس و منطقه خبر داد؛ نشستی که قرار بود روز دوشنبه ۲۳ شهریور در شهر صلاله عمان با محوریت وضعیت تنگه هرمز برگزار شود.
بدر بوسعیدی، وزیر خارجه عمان، روز یکشنبه ۲۲ شهریور در شبکه ایکس نوشت که این نشست «به منظور دستیابی به اجماع» به تعویق افتاده است.
او تاکید کرد عمان همچنان به تقویت گفت‌وگوهایی که به «ثبات و همکاری پایدار در منطقه» کمک کند، متعهد است.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، پیشتر گفته بود که روز دوشنبه در نشست هشت‌جانبه وزرای خارجه کشورهای ساحلی خلیج فارس و دریای عمان در صلاله شرکت خواهد کرد.
قرار بود در این نشست درباره طرح ایران و عمان برای ایجاد سازوکاری جهت تردد امن کشتی‌ها در تنگه هرمز گفت‌وگو شود.
تعویق این نشست در حالی اعلام شده است که آمریکا پیشتر تاکید کرده بود در مذاکرات مربوط به تنگه هرمز مشارکت نخواهد کرد و هرگونه مذاکره مستقیم با جمهوری اسلامی را بر پرونده هسته‌ای متمرکز می‌کند.
مقام‌های آمریکایی به کشورهای منطقه گفته‌اند واشنگتن درباره وضعیت تنگه هرمز مذاکره نخواهد کرد و موضوع اصلی مذاکرات احتمالی با تهران باید برنامه هسته‌ای جمهوری اسلامی باشد.
مارکو روبیو، وزیر خارجه آمریکا، نیز پیشتر گفته بود تنگه هرمز نباید تحت کنترل جمهوری اسلامی باشد و آمریکا برای تضمین امنیت کشتیرانی در این مسیر اقدام خواهد کرد.
در مقابل، جمهوری اسلامی و عمان تلاش کرده‌اند کشورهای منطقه را در گفت‌وگو درباره سازوکار تردد کشتی‌ها در تنگه هرمز وارد کنند.
قرار بود نتایج رایزنی‌های تهران و مسقط درباره مسیرهای امن کشتیرانی در این نشست به کشورهای منطقه ارایه شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78361" target="_blank">📅 22:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78360">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN-NxHssxiR7aWcpASbYLMY3DaV61C1Uils11fBgAIwbwaxPufdkoz0_ypnibqFczeTfSXk0HHCJMcuY3ugHsP46VhBDr7mcD6yHtDraRuJY20z9vtjzNFhJj-TPu74ui2eL_vKBdQaL62NPGHVE4IZooWN-EcdmyDNhyVw3MVGtkN_lODOTV-DSMJkxdNBXz2BQu9UWYYiv1buPZF-F8PmCD8FFMYKjo84IggkPc_2LA5mUXvw1fUf8K8LXbi5xRRvGAX1gChlrhYhczxLz-0Jiv6V9zAdmqKH-0mSyJLK7wDMmLntYMZoP73TpnVzbKLcqnXhjMlhpaCobPHM2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز روز یکشنبه ۲۲ شهریور ماه در گزارشی به نقل از چند مقام ایرانی نوشت، مسعود پزشکیان، پس از حمله نیروهای سپاه پاسداران به سه کشتی تجاری در تنگه هرمز در اوایل تیرماه گذشته، به‌شدت خشمگین شده و این اقدام را «بی‌پروایانه و غیرمسئولانه» خوانده است.
این حمله‌ها که منجر به آتش‌سوزی یک نفت‌کش حامل گاز مایع قطر و آسیب به شناورهای دیگر شد، درست زمانی رخ داد که ایران به توافقی با ایالات متحده برای پایان دادن به درگیری‌ها نزدیک شده بود.
بر اساس این گزارش که فرناز فصیحی به نقل از مقامات ایرانی نوشته است، پزشکیان پس از آگاهی از این ماجرا با احمد وحیدی، فرمانده کل سپاه پاسداران، تماس گرفته و با لحنی تند خواستار پاسخگویی شده است. با این حال، وحیدی ضمن سلب مسئولیت و ابراز بی‌اطلاعی، به رئیس‌جمهوری اعلام کرده که نه مجوزی برای این اقدام صادر کرده و نه شورای عالی امنیت ملی از این عملیات مطلع بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78360" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/930e263d13.mp4?token=gSwycltKLx1HWEejMSJI0Cbhvr7xkqwVvLwq08dSLnnKrhxP4HPTp0_3_0Zrrg1E2i15AwuA3tE3em2cG6EjVEXIRz0t8pqIVaTnVk0C9ElQ-bGMFpaYsKd2wLFNOfCnJyJn53NFizQUY-yAb7aF4-c_TKS9V4k_esjjS11faUJYCau6Z0uz_Gu5Nu2Oow7LxMOh82PmsOuSBWxnqepHgfsQ-0ah0Ge20myx1sHnSC8oetpu95JQW9ems4dWt_HcXO6L1NGK6WKem4wxpLfdMhiWjrJ5oJOOs9udWngc5PPsWCSzcyiznIkl80B9IHUTQEfjzYSPbVPsfwVvPmBZNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/930e263d13.mp4?token=gSwycltKLx1HWEejMSJI0Cbhvr7xkqwVvLwq08dSLnnKrhxP4HPTp0_3_0Zrrg1E2i15AwuA3tE3em2cG6EjVEXIRz0t8pqIVaTnVk0C9ElQ-bGMFpaYsKd2wLFNOfCnJyJn53NFizQUY-yAb7aF4-c_TKS9V4k_esjjS11faUJYCau6Z0uz_Gu5Nu2Oow7LxMOh82PmsOuSBWxnqepHgfsQ-0ah0Ge20myx1sHnSC8oetpu95JQW9ems4dWt_HcXO6L1NGK6WKem4wxpLfdMhiWjrJ5oJOOs9udWngc5PPsWCSzcyiznIkl80B9IHUTQEfjzYSPbVPsfwVvPmBZNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش، پس از اعلام نرخ سوم بنزین در ایران، تصاویری واقعی در شبکه‌های اجتماعی منتشر شده بود درباره اینکه بعضی از تلمبه‌ها در جایگاه‌های سوخت (پمپ بنزین) امکان نمایش همه ارقام بنزین ۱۰ هزارتومنی رو ندارند و مجبور شدند در ادامه نمایشگر یک صفر بچسبونند روی بدنه تلمبه.
حالا محمدباقر قالیباف، رئیس "مجلس شورای اسلامی" در «ایران»، اون انیمیشن رو پست کرده.
ولی درباره قیمت سوخت در یک کشور دیگه:
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78358" target="_blank">📅 21:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g34mC_l0HCiwJgJ-OQOkIFfPOiIrbS3ebRdsTBttNivOtuk8twhYoIwSw0GW54OZmJSwHg4PvrfKt_iCPOxpE339PR_eA1VXk2INE70-bFxEmoOxexIsGLDkvCMxtSuB1-lnAyXbiX40T2vCF2ejBpIkbY_fExKzQ5aiCcemBs3bdpPQkY8b6h6L_iCHsqIure6GKLm1Mn-4aZdcZ5rqfBwWB3WIf7uwsbmU6ASs1D-9hmsxbWgJnjWro_wEBVJrYDh6HQifNajd7VYZy7Ih62vE-uaKlDDOGV6xXUFI3NaYjdgbetuX_t05WutlLARGCwMGF5oF9c4wMncRGripvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین رسولی‌نسب، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در شاندیز، به اتهام «محاربه» از سوی دادگاه انقلاب مشهد به اعدام محکوم شده است. او در حال حاضر در زندان وکیل‌آباد مشهد نگهداری می‌شود.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، روز یکشنبه ۲۲ شهریور ۱۴۰۵، گزارش داد حسین رسولی‌نسب به «محاربه از طریق مشارکت در تخریب اموال عمومی» و «اجتماع و تبانی علیه امنیت کشور» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78357" target="_blank">📅 18:43 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
