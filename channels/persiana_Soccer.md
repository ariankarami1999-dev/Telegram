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
<img src="https://cdn4.telesco.pe/file/G_wCbs8BWU0C2nl5NuCqMlHG9PdTL_uDYsRduZM8alQ550Xe-kUonwghcU2-eh6UDipHFBZsRDKFXeBk0ye8RkW3ArGnSFQ31GAs8anRvJSxRCUYyQsq8y0a3Pf-v12WxXoxur0yveGZ2xUUe4pXy93JfWm-HhSqlCXdRHC5lxLikLLn8jvxcWcRAKtfHeKdN-U3FG1LhTmR0uDRgZ5kXhb7aaIT03Tg1HtY7bigW8hg5tZ34cJgZaqcSvO3WTIFqKOk62w5ZCtDiKU_a_8w1XGJ90N7TK3XKWZZuhs5sXBJ4L7nS5FK9kbVi6dPcheD_wFk-zHroE1V7ftG8pmN7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 182K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e99804290.mp4?token=T4awkiHBjVC8NnM73lRoh7l7cvNALWjkoRo_NhbB6uK6O8UFk0PfmFM47QBaoQPLNgGkrcsuNLtztOuRcCrVUQgmsBNjCvh06iqhA9DtohZZUrOCtqYeVYYjnk5XoPiyuqNbo57e9qgBKHPk-y2FhCMbRjNXRL2fGL5w4VHa_4jLGO0O80yXSfLU6wlRWpzJyxihssv86D0oHJjY3BZygN_3m_AxQyTKNGSQn_GTQ-gW5xw_YPdtRO8PyucSSW4TLjGg02xcI-CSQfqBwmQiNzSmV2D_IfcSr3NZPfRpdOSrlMoYU27wt6bFFz8X9xG33S6PqhCUoWUJfm2aD-4agQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌تماشایی هریسون رید بازیکن‌فولام به لیورپول به‌ عنوان بهترین گل فصل لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/persiana_Soccer/22428" target="_blank">📅 16:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsNPDERe-6HhVbcImpnQOs86DRNEDnLy4SuB611GEG8j7ibsgyQYHs82tcJpHuuT5mwVEeY0FL4AEt6J_ph93-gH-EjKlxdXswLWdJNUHR-p-z9_IK6kldzTJ30vUQ9cg1uWF9GXJ3IFmJ96NqovIy8KY2glF-kc7LHN6FKxozkE2K_WVbzdxpTla7xxxn-Mwkno2gd1YsQbR_YM7SQR45RflrsgIoW-AMTc0rW1F2IVn46bbNarui6gUDCGzTybBaAeSNd5iv88fylXMAiC4qxKRSrw9RdEzg1_WUN0CydPW7ZgzM-zemwBZ1pMewecQZH-qrrNPzdIHJBlf965Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22427" target="_blank">📅 16:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBrd6wfgM1mT-JfHt986eUr_FekfkunGY1u_F7xMjBR8osUYOWPJDMSfuIx5oWjvY3hvj3Rd5hYlg_g-0GwnbzC8Mhb0smqKnv_9DpM2u6XcdgFh5hd9OzgLiKOvUJ5oQOx-Dd8BEAe_6EiZhb7uru_8Ezh3RfdXiw4oZTJQXRptmdeMiDES_RDguj1-PsLlFRxEQbfch29yhEyQyfzr5krf2nBvIGY13vUFZLiNJF5oj3QbHPcsaQY3zn45dMEkqc2v57bdp5MVdMxM0gcqjryxESajnfmIGountolJchOODcT3ZRVFWeZoEiFhxTIG9poMBCXw6rx8-mew7pEH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه پرتغالی آبولا هم مدعی شده که باشگاه بارسا در حال نهایی کردن عقد قرارداد دو ساله با برنارد سیلوا با دستمزد سالانه 8 میلیون یوروعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22426" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccdf1c58d.mp4?token=b-jxRSpHuXpM_6SOcY4lfN0HSVsirO6s0Laqsze8X9Ml7tizh9SBFMqwdaAY9SFxnR7knmsvSqirLKRKgSqwxVuvIDX_gkT1EeeUIlUT2NY5FHt4FGSyvcYbXBsKdbkCUPSMLDzoDifOPBTh2LFWv6_X6onPOkP7UJvVlqx3dmQR7TYSKQlFCnlNyn8p216ASugdcucF-yqzJhlVjB8dt9QFyLzu6papcTb7_pKGSwXXDSc33mWlMUgDv-XGdc0g7Qqadh-kqquKZO_wNayFp8FPV8WixdWI5fFn756wzSOHrnfbywXwz7d7YqkRVoUVojrQn3IXb7mOMoweHYq82oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌که‌باشگاه ماخاچ قلعه روسیه از عملکرد درخشان محمد جواد حسین نژاد ستاره ایرانی خود منتشر کرد. حسین نژاد تنها یک فصل از قراردادش با این باشگاه روسی باقی مانده. درصورت باز شدن پنجره آبی‌ها مدیران این باشگاه تهرانی برای جذب قطعی این‌فوق ستاره 23 ساله اقدام خواهندکرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22425" target="_blank">📅 15:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHkZE4Vrc6Mf2PYFRK260rshwUXmMHerr67CuDAp9XxmBNxFi1wSj4yXvoZhj7BlMcK_GsQ1yZPjl2P_F9hx97hnRJolGGesvOTOjzd8M4KY4kLEQg4jixCQgRYQjb3k64x9AYwIZOCYoYBqrSuhwFu3kS5laJHQsgLP5gIsGTPIamTqEq4OVBdN9BPqPU-l5WLNyndLgTRjBANryUghScM3wc_JXhI7Q5tbEVKcSJ62ixKjM0czp7tOAhxFtfJFGCXSbPJ5Y4w9lhF6O6z-nV0uPTmI9krirrC9esBczy93rMW1vKMFgh47-hmHHd8SAFMgmU88IjrQk6CSQlwDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22424" target="_blank">📅 14:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA2QeNw6AQYtn59xWNq8LZfiFn2I-osK2tHQRtVacn_vgHrBRO8IH4DshTc2N3DrKMDK83XZW8mkPBkJMiH1gH25sp9HAVhFDJi1Wk8sfPyH4enJOMSlARiRfU4h3sUjxxVjElbObBs1B_Z9y4J9kTgbnOvAceGlT5vzh1qISIEPjCFhZbpK__6BfcWL1joUbzwkshfU0bET9pUmDUW0qmbUfxnKlgK5_UAZtPg_DuFhUhShrHrdY5j5fhKCarPjdk2RDflZO_-vNXlht9bLFJln9nsSZCMgjqufcYhqU1-EF3AAPB_iPZzF3sl0Gl7QJwiCpM9ljzqSwuD62wqrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4m45Yt3X5m91rb3bqMPtd-FgRJjrwmmvppRunJOebxfp_UNyQ3xYV0TBWKtolNwxHtlfdUFvmsmkll00EA9fgPEE7GerBwhS43IVwu68HJSmjoPk9fL0qom0ET3safwaaM8judu67LYnni2RxX6ELaKd1aK3deApB_8T-61R-VGIQU1Vr4pQ54uG1K6okPlswqvR75_EFJq_CIcCF6sR7c0E6csWVWevlxGPjpTaBVrx77cOMO4FR-NBT3fykO6t2V5BD84unfutcFT040lD52KwCkspT_FLZhbk3v1yxtrUZhzQTJtkOFYnuTjhS2BRmhvwATM2jHmeG_cONZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5jpgXcipW6z4Vwg4OAETnl67lundILyPe8hYIcXLj4xOzr6Yj--9avJLLpygv130LfkVej-M3ghLlvZldNSPG1wYHhf_9gu6Su63zIHOS1Qs9kIzyKnSwy7A_5udfme49vEka8tpdBhyvPWWWXCugxeDDrQvgFdWHBN1yvnzrTeeVCFEKUdC2NQ5FrLzZ7JyBlsXT7PGPowTdfhjum8l_JAXchchL0NsEUz0MSNaf2BHOxDcg8dxRs0IpR3vznC6Ur3_xcWyVpF225K8JdIQ1qqqTSUIvl73iBAo75R0CtTYFsGvPdoy3eiYjjvpHj6p1wCcGriGNnEWq2PbRrpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq4b441M34tyELi16tz4F-N3OHz2lzWN-OK3j8ncDJ8TQcA9AzdvkP5ad17YLaxZf7y1KX8EcWswUseL1uqExrWLpSZNfSr5B7SE3E2ItPDK5OtFXpa_KvfkoBWC51lE1e1Brx0lg7VDAf6PRmigpv1um96Sod9JAF_2YJ0evzFHGZu2j5-CzQgErhmqiFf9a8cixPaRUCvnKmDAfUwfnCAJ3Pnkpc-zsuT1I_Rc8R5pgj87uqDUOlVUbpjagr1m7J-yGX0qyGSqNDaKdmLSCHQ_a5ndPTib7DNlLZicy6KUJMjMkyhWRX5ULhgLmd3XykIw41hq-0d-6qquJTCc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uim-hmQB83m5MwaH5enr-yZJVVTh3gmBOfoTUZ_ELE6RcJIE84yFbcwVDj-LKo-fBDSqKEskSiokH2Ed-AqoFO9M3BtrXcDFO7Zt6UNbGO9hnal2EtrnMadc5zUs2W_0Xuc7cTwmTEY6XaZ6uKRSnjymsh24HoKEvksMTEFm9WadL2NEdtNW-EYup4_w88nuMt5LPq_GdrSHQNXx1izO0rlo09L2KyMdb6sMH96_U9mFf3jXLgelIw8g5p8O6X-0bBGDuM1A-ATU5HGgUU2eLVf9D0r4EDEZlgfJmUf18hbCYNcxWaQ0ClVukip-kzBIt-fkXdwLP-rWXpxcxCrgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej9myXIU1TvvAqXoWkr48rV0TAwQ-6FYBXgezSnUZh1W9ULuQoWUIKH-f_SPrqOiEsXxr4985HpxiwW7ocGmq91QPBE2aH6Eh4KEAxiK5eOxejgjQ4SyZkLPtmrhpy1IjbuiMswTGTlk6FQPWeJpZ8pglUPKmplZ-pIMlhpNsKhbcmCADvcSqKadwk6E-te8VcC5e2oWTT7qFo8PS_d4GZ9Ewt71rhDsz-JCYwd5_FWz0gWsq4kbK6vF5ROiSfRDkxwJ9TdM28PSzMBV4Fdz9XNhlRjX-lTje3SOA6SCfbsfhDLQ_HicWdO99VtdliIairROo_NZUJZ_5-We0WX-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djM8NsMnK4eKisCZKTOgSf9J-INEKfyRLkYdMzC4EtIunnHOifZmRjVbKLOBhuj8p6_RC3ZflDvnDFHxvbOtMZtldyp14w3___FxWgRsv72lGhcghTCvBoEMhOZGKERBJ-UgGdzhoUjCzoWdeLXdnTZYw_q3dlTdV7GgwhHxoUKNV6qx1xEg6YSVkrbzgF63mHKhZVHnVPgs9yV8PJV3Qi-EQ1UzRTP32Npy2SBHhaXef3GkaXNyEBY180zgFdeQVB2Bin2583GZrKGsuQijOuxqoWtx6eOeUW4IO4b8b4_ymc_NeL6DXwxpEXhh5vHcGzPszdJjbcBA8_jLkSExKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhVw6WSP_THRF8iiwjGFV_XTo2-T2RZB2tt-Nzytp9o_I8qO8QibLl_10js4SF99K6UyNXVx53midcYO-8EP62OIz8x3qFalxUf9dfBK65xoGPFG2gUW6Fr7Tkp-FawotW_P8HdDxR7FEbQzgTpXmygmSxmy1B5O4JSnM0qQGjwO3qkx2F4MAq9PwWi2p5dd6B9Usm8yn6RgP2R3MIcv2eImQhmDxwR6nv_qBV4kS5ify1Ukcmd2EizSKuDYIctO0V_X9IpUk8qWsW9-RVcYdCCvGLhVxPkU2BKcIgn3qwWpE_gZR2G7ueCzbmVqJwPLyPKgm6JzKG6JFyWrJ6SFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEAhzTdSCwalIpWcUUQ5xrPv0HcbVoemG9sWDZDBNXN27IaITR-5kFGioCt2QntTFqCxnudE6lxbymj0bOEbtznK7sGLJzRwO-QVwLG7Y8X-ghYBhtH9IcxNmArQKBvZwt2Oz2aOO3VohD5Ase0SBMIebzGqqwsFYJnop0vTT0KFZMpuwp5kXPUYS16CvGj5VdJjIB3tkO_0zNbJvUkWtmmTMzANjIw4vRO2k84mqoxgIJpeB6_6kvk8arjl_LPcUS6U5XcadmbJlmFXFwqFVjIPC5T62SGewiphoXuCrT246X-zdx9h3jqqH9_85hEsQiaJ-yjIx6XaE5ZoVhHSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgCDfsZT0Y3dc8T6iaoGeMEWg3QudUuEm4j3affHhSeTOE09OQ75vf1mQGhCIHBpE_x4j4QFpZCDrfBc-yb-u6KWwJhHPxX6vhrKZSFNeH0yDHYHOdaA-BoJgFQE-NpN80H70Uj3XjtQU1hVpQHa_1Vk_z6TdN6OjpTJef27d1SR5I1M1NCox3ebdTkg7WPd1DN5-JR72uLvG-VC-17tUsXcqU28tBzJlBq_955bi54LHwkwlNcJDC01JtFZiw23YenUJwsBw5iU4p62aqWk_5yNBLlZk5skDIAQyqoR6Aa_mA6UmBiuNJn3eXkjYeYw4bMeDYK-9vtVXVki6K6DSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI7rrWcaQCPrbpOcv8uxyvD35a0wgge0srchUkaEBNlzDKJsIgOnjMxMbVGQJkXgMr7uL7V5zj_PtrsbJDE7oUV1eqSKKsmdd6pY99DxkJMdqz6fBs11RtbpNnld9FRdtVZab0J7SRQ1xFF3TBLMwN2G7QuHuzkGXSGf28cq6O47oHcR7ReKZU9lsmsw9noQbXLrqE9He4KGo9o_QhcKlwv-VH70Lrualm3mqnIcnZc-UQGKzwaB2Jl1t2CIY_dCbZiCxfMRm3WSuiQWt9Os6Krfm02ljPK1vb9blzCjf_u9lTVunKHr3AEcGIh2kfozfqf2jAa-NRMC3zHkhDPuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰ هزارتومان بهت میده
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22413" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfkJXdVRy9CW_JMITsWKbCTqtY4gtIrSamvbO99_QoNZhbg5Sr2yoWrDk0yqYWwACujQVPfg_vSjIAXqCmqcpShXp2u-hBimRKOmMZxxZezCE_Q-wjQxtvMrU2mW0WBxM3SiHPbOj_C3Fms95sPpCRqxxgoLTcyXrqUbDBEfjt5DzftYEVIhZtA7pPqcXtRAB85J-zoyfUrYb9dCSPwVr8skxh5aXutb5RIJyOGvoXojU_OY5YCZtr-Nib7khfcBgxeBicMiYyWUDMYlfOiWsPAdUpfVkULcouxVTFyA7MDKQlx_3T8gUOJeP0mxXk0v-NU0s0hzJ5CO_gjYQI1usA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=XFp6X7peeTiSe1i7gSOwDbJJ5pVEB0Uwl41M5XohaW47pYFcmwy1jaav2zsvz9acWFTgkoBvc-IWrBMWLxXP0-vZje4yRs7GBm2gEdsyOlCuaIfSXxGZmx7HwOp8VtuatToNjIf2Mk6Ap5fwpXc6QH6Qp9BsvhrP2TzoFhy9ySv9B5Sw7EcIL01oN8T53mWU_lqI4nW4JEDJY0NzGzwnJJo5PW1F_7sz7bqXj2cf7pxvnC78p4oFysnLNaHc4FgtYz_QrESHDpLqci5j4akfklo0JiXGAZo9XNq9rL7uaHPHqkH0Y_M-SDYh6WHcICrN563jTS-9QKHsKhbFeSBpm1eJ62zQngb1StfZ-51Xl8sIxJxjYdqDwmLw2IDnQB-3HZNZM6FTu70_ElJ_lABwN6hHazePuCiMdsUp5IrSKw_FSNYLNXrCjvDB332WQ9_UAlSsq6ZcOarRQ7W_-ljdhc0lwhc8HFE307aYliS2v_lo4CJIgv2Q0Cp01xLpaItoUGDg8IAYftM0mQ6cGtVXuLlH2RIbLcx9whCzjgftP0dZU0Z2-5pWjw965KWFdKAXCxFbhS-hK5BOyTtFfDnsmmTDx6JXadubJuJ_B2Mc5Q11pZulANN2gNAuEeqApp-MWUjAK2zVUIHQ_4E91q5SV_jWqAxcG-4PZ-MMcWBscZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=XFp6X7peeTiSe1i7gSOwDbJJ5pVEB0Uwl41M5XohaW47pYFcmwy1jaav2zsvz9acWFTgkoBvc-IWrBMWLxXP0-vZje4yRs7GBm2gEdsyOlCuaIfSXxGZmx7HwOp8VtuatToNjIf2Mk6Ap5fwpXc6QH6Qp9BsvhrP2TzoFhy9ySv9B5Sw7EcIL01oN8T53mWU_lqI4nW4JEDJY0NzGzwnJJo5PW1F_7sz7bqXj2cf7pxvnC78p4oFysnLNaHc4FgtYz_QrESHDpLqci5j4akfklo0JiXGAZo9XNq9rL7uaHPHqkH0Y_M-SDYh6WHcICrN563jTS-9QKHsKhbFeSBpm1eJ62zQngb1StfZ-51Xl8sIxJxjYdqDwmLw2IDnQB-3HZNZM6FTu70_ElJ_lABwN6hHazePuCiMdsUp5IrSKw_FSNYLNXrCjvDB332WQ9_UAlSsq6ZcOarRQ7W_-ljdhc0lwhc8HFE307aYliS2v_lo4CJIgv2Q0Cp01xLpaItoUGDg8IAYftM0mQ6cGtVXuLlH2RIbLcx9whCzjgftP0dZU0Z2-5pWjw965KWFdKAXCxFbhS-hK5BOyTtFfDnsmmTDx6JXadubJuJ_B2Mc5Q11pZulANN2gNAuEeqApp-MWUjAK2zVUIHQ_4E91q5SV_jWqAxcG-4PZ-MMcWBscZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=aqLImRWNSvZnqAcWIp3qrb_Fv4JNYTaubxoAUvE_y_wbN-afhYSuXvnuVPTmmHZsZiX5AHsF42i36m15_yMRk3OGULtqMEzU4vE8G_xGf8be-Khnt8lhM6Pb_KB1qhXf0TU6f5fPJURjrbtIGNHpV28UR0zVfcsLI2v7AJAa4Jtduqf5zU-28NNbEXoLNk9FnunIjRN99tCTkz79fYzBXIFK4Rsu9RIFV40xZM_p032wPf9xogjybiAaz2QHUFbShJoP7XctTJcng8w5JcVv-yF_f_fnS4Cr4A8tdRpzqQuQmDPhRng2JaQv04CSdHqRQhVQXwVvUfLbSOg7xsAz1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=aqLImRWNSvZnqAcWIp3qrb_Fv4JNYTaubxoAUvE_y_wbN-afhYSuXvnuVPTmmHZsZiX5AHsF42i36m15_yMRk3OGULtqMEzU4vE8G_xGf8be-Khnt8lhM6Pb_KB1qhXf0TU6f5fPJURjrbtIGNHpV28UR0zVfcsLI2v7AJAa4Jtduqf5zU-28NNbEXoLNk9FnunIjRN99tCTkz79fYzBXIFK4Rsu9RIFV40xZM_p032wPf9xogjybiAaz2QHUFbShJoP7XctTJcng8w5JcVv-yF_f_fnS4Cr4A8tdRpzqQuQmDPhRng2JaQv04CSdHqRQhVQXwVvUfLbSOg7xsAz1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyP72RC_c90Tqm93TJ0pTuMpbpt0gZcI8iACfQJa7UJS8LEoTFES_Qh9eDzly_LYo4oLWTZM0xyVULy5JmXnp7DyPG7Jg44RfpurcQjUkL-2qVfHv7nbpEAOZ3-Ign3xKVGNGjqR0qQa9v28We3m4g1-37lVtw0sHIPNiGZZ4WaY1jong5xRujhgFHx4lRwH-aIy6MsMPrH2zSoD0j_uc_LqzZuBVk2PXozONBivvFzKFY86EnFx5bt7I9Svz5q6eJl_bCooCNncgyY5SymYZQatkvOzFznonaLIkN8kVO8HsCnmEewD0GuXqfCpW-ucKuCaSLpnu1KixEPX41Appg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRPaxrshZG3NsQqqBi6oX_8-Con_8bTkV5Tpo_BawT5opN9xnEEkADPNhtiWF-bO0U_hWApYStgVebi5SMTOsoMDCWTFcw2aP6fUYFSo2Cw1bn-OJ85xuyADgV8tXV4-TGWBy2ihHPFwfEBE9UX1lQmtkFpD-XhImlCODUa3XkdHWF0doU6wdIh-NLRFgXFwrUhTY0w2X2Ck2Yso2DBNyYVd4STUhskdJsDdStOtGPPiYNlBQyiEb5f0CL-6shPdSXQO2IHU6rjKnn-ajSLxwlHTiUn1Kjthf2gn--KRYpp6DcreGvg-1Jngk5eEd28I20DbrxjLBuUqUkaVqb8kqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVOAVIi-fYglomtYk8gH8fW1p5QKFibbQR8BOT7ZXvJ2f2eiefCZsaIWi-tCaSpeJhBHAYawXnfve-1g2SaPtREUFq2wl5I_zKHx43aTMeU3Ew06UT684hBxSGDSk91WE7cqyueKqNmcvaSqqicJG6dPtOb1Al6GvDSoB6xPzh7YISoteoMleU4Fn3NIu2pPapcyI8R5PRWzkzrzK1Jh6ku7uY-sH1tBsoyjyTNd6XOYBB9i-ZU31_hjkwbq3auZFRGspvb3aoY7ROK3PXzizl9Q_EifNIr3u-TY90Pcd1-khKeMq-SDrrkNUmYl3ijlHXaXvzetCdpCuKx45ybfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ2ESnQvbbLZDbezUGSrUHMYAp5zT6I2RtILOIWwQ0FrmB7T-13zLHHMkyMQ5RG_Ub21Z-_p8Ocy_X7uMoAL08TOUQj9xyzDZR7Y5aIs_9TrbPwRggv4CiEa0TVed3246E6_bmyark3sIFctEYkMn1SNevBNlwijOmvWFh0NEghPDE7eYWMH5ZDo45P8DshQOMAzj6yClmaUmYlQgNJisJ-XmHfXN0BxskEba8ahNxiRRLCVQxmGKvJRJJAtKEr4FkFGbce66Ezq0UmsCtaUcmlCNzIGK8h9j3fDHroMOY9QaW4iI04hzTxAgzPt-xSQXfvocGyzEeDX30hzW0CHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmhWNZgQakn3d3644A6suFTPW7OzCgA5eEj0d2GuHugKtBNXB2319aegqaA9wPEq6a-PZ7phGfW-R6BY0bEuHFA-r8PZUyZVoikE6mqUQrSNf5lGVMwDFOopigW47Y6xxgwGX7ywno6g7FzKaCDz-8nedPZ66w2myWkfhxc4oZv8duWLwvayLQecicBR_EgHpFj6bVPmx3zYjp7hrfhGgoE2oUMmMaJRZaQa8XFl_tyAKyuTquazc1bUqXnjudSr0VMEtxnkKLujptTING4ahiNi94rJdsxjLtpV2QK1FKAE5vh5SIsuux0UmdWoH80rrLxcYAwEoSbDuG7rJDhYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKv9loT3sTbSbv0qoGoQiMoGwGZgX7P9iJzmrAHRZF-fMV2BPnUR1gy-auddRCjx7XeUx4-tHZuftCEIn1Yp67CMsA3bOMsAvU7mg2IyjNYlTtAR9z99HbJoF1zBLEUmVnWG51AusBVl-BbNvjReTOe876gh5pfNG-cXKKsyX84ikM5QVgirzREyZZ1DmrGAknKf_6nyI7s8Shi8ZuF0PX5KVI7uDgp0HzO_NWqAF9zplBQfZmHAfpU09TdSV2pLSOeAECFrlIVGiMvbLO1jKdcN0aXxOyhjg4BspxKMeQytmRrDAMeiZYcKTFb8xAUD9OdwIzt9-zlfx29HqdbnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmmkXSpVTQNtIU29tC-p6klsnuVFxKvuNrrCreeFnGN1ipfeurS14pE7zhl1iDbUzb947ZjRWmU37MiOLhwHK4UCWO3Mxnk_fpk1LIHYS8gQdW9AUKA4VIWWCn0gWUNmdRcJB4rBq1_7yoDbYpx3fmbX3jKWOQ4D8223f_XgLdSV4sVeXZtbvP1QR8fBhkhi0XC8jiAnMNEWZtR_uFUqZCh1Cu2ZH5gLPfl64RLqKjDdHnXlnvRu0TatHLRdEhgPBhINgAqJTVwZ4FidykspQ4Fc4j3mqnsKElrJNAF5XOY-c6AZiv3m2r3WKP5aS4y27Pvn7nIFauICxI88eR8x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STNpoQX6BH4KqSoUqQEYUJB-34vd3anQK9d5aCmrd2bQRS4dtJ4maH06htCJYk9_dJ7phaeBLjtyU3mZVxS-fQu9cIARDGVRSnxOMvBFNinW0-WZwfulRw9PKFoNtEx_6jMIuQj5SWV2E1EKPnLNryyTFouSNHEEx_UiIXkP7ApQu77v25xiq6Yv6uFsR5Fg8FNEptewAQ54fttB9fqsN-A-bJqF4C9FsyAQi-qY3HH8N1b-F1dvVVyEUpD3eU6TkPtoD6yYHqxbPcBJumQAnSfPZbrkDT6avkeDCIt26lCB8bIVg3JrE9lxhBkJQZRH6HmPWdn9hneXSVo5D5msGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4S9nKuGN-EspqobeCS094hRq0oin2OzSPxTDLCfLnsXfCnehUs-zGlHO9KRitc-GtxqXrbjgyPCc2vh199vE-88thjEbUIXRC-trLoZCXsvlSAZhHOP8Bvixe-FOSOGGJv1Yh4fl-6lDJeqiYY8ENzHXI2uR13iuQ-NZ4jAqyfNEWxKKu04KJfg3gghH-s75AmXQlqIwnEJK13FgXvFnbUPu7sVYaN2Yu-MUn3NnVjqL_kxI-g1k_JsjpWH8ewxorGdwN66AA8sn60SHK9U8QMuuXeML4gkV07MIVh6-pLe5IXH9OTXngiESDTJ1WGNloO1mkEb4xeOvy2B9nx6fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=jYoI5XUXaS-u6hBLQtBEa7uGl0ytpObonWfxbo9Rus3WlIAnGT8wdqoMi5bcExSiKI_M-ZWHRrv5ZsSlVM0yjWfw-b6gIaidIhRht__-QaxZCTsSNqgPhr_MOuwAq-i4NPWbuyX8dUlCAm7Dr0mWm8MMH91t4EmYx2lp1t0qM_fgBfp5JwbSFiCOH6K-x8VmQB_rOPBlVInVeUiAVnt2GZ7PnbHKrwiMDZPWu-zLEerxLWu4FPE3UXsKppRVkF-22Suh_8yQyFqkG-nIa58AqGdlMIa4JYEU43p6bYd6BCaK9h2c-l5el7tR0_XS74KnkuV2zacniT1aTyt2CymxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=jYoI5XUXaS-u6hBLQtBEa7uGl0ytpObonWfxbo9Rus3WlIAnGT8wdqoMi5bcExSiKI_M-ZWHRrv5ZsSlVM0yjWfw-b6gIaidIhRht__-QaxZCTsSNqgPhr_MOuwAq-i4NPWbuyX8dUlCAm7Dr0mWm8MMH91t4EmYx2lp1t0qM_fgBfp5JwbSFiCOH6K-x8VmQB_rOPBlVInVeUiAVnt2GZ7PnbHKrwiMDZPWu-zLEerxLWu4FPE3UXsKppRVkF-22Suh_8yQyFqkG-nIa58AqGdlMIa4JYEU43p6bYd6BCaK9h2c-l5el7tR0_XS74KnkuV2zacniT1aTyt2CymxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ0mETQ26bb6yTCrKRwnPjZO95fXviQ60rbWPpJplBb8d0P1YWzKw4qpMMMDZKFQBAZyhj8MXTApgMOyW-k2ABnmLz90q3yAFDqQzjGeGGMGjr9KHZZXC3uwOcijEdbq-daheJUylCTgp4ok5j2KS5PhgHNsejdx7sPzSLYRUCIu0HKeR1ngk5_qw6LVflQl0ZhYTCtt0n0WjHZQcjeF-huPO75-Y4V7NTSnN4reJ7oGao1seklEKcRKdtHmpBcn0T0i1QF0ce4C3lLeqQ-SGFExCkRHWbkGmTUt7BlKZsuL7V5C2i6RONooGEFsip4nvkD6Hz6zlzN2dPpboB5HaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=saphz6ukCgiG-tW4goMW3frZG1m9TRu5qsxlDcWl6AG4iUJEpIsAAlK3eDNwWXpjORlhg2Kvf-z3CzNeymViubFtRPstDe1bYc-ugBVcoG7sil2kZYmtyztzYzec5jiwe7ocYaA1j-o4rSf_PspdzwtjDQ_NJXpve9kR5pKjwkIINZ-KVfe8cHFNHy_cyVaWMHlrqGRW7axuqAEcg4ifeckYtHAz0oEzMcxPFLdYQwc44o1693VfStkPRido2KtuHIK-eZFTkgzaxyraRwGBN0nHL28HbH0kYcdOsOOLkq6nTbWB8_IUTONKFstWFP_ssbs1whtdo44LLpVdIdKP3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=saphz6ukCgiG-tW4goMW3frZG1m9TRu5qsxlDcWl6AG4iUJEpIsAAlK3eDNwWXpjORlhg2Kvf-z3CzNeymViubFtRPstDe1bYc-ugBVcoG7sil2kZYmtyztzYzec5jiwe7ocYaA1j-o4rSf_PspdzwtjDQ_NJXpve9kR5pKjwkIINZ-KVfe8cHFNHy_cyVaWMHlrqGRW7axuqAEcg4ifeckYtHAz0oEzMcxPFLdYQwc44o1693VfStkPRido2KtuHIK-eZFTkgzaxyraRwGBN0nHL28HbH0kYcdOsOOLkq6nTbWB8_IUTONKFstWFP_ssbs1whtdo44LLpVdIdKP3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEQG3bcnsGRHLVEZs5HLH7s4-jdrUev4FB5kVoC1mAW5wAbR3I0cg_QP2N2jKk-bHpRYOXIni4BOnKfgMhjDR_HQO9Z92fNfWJq_yuFxsxsptGHqvE5Kr8cGaTeUdlDIKhWqVKcXhOMziaaBsDGFtkPBg993v_4BAo0kxYbrf23YkjXCM7WS3DHJKaiHKs9T-_sJhqiW3W9aEm2aMa30KeGVkHcjxEW4JGGwOvRWi57HLK9swPTA2dtg6dBJ4Yag9N8S-WpYGI80nwzwqc7Rwl-eIuPYeLINCAJY1u7RMeBxxcmBvvkiRBjrU5WXsOoB18-JskR56EKfcWulQoL8kT58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=fY-22HFq6eRNPAfmcKMSJBrMQmIAHC8FzYqrpmtV_S5GrNTyhBVSqSL21-wRB2Jql0JJtUiBuWe9g-eQo8wjN_nshO3ipHj30L9GlY86PEYmkFTpK06QjNYhys8vGSZ9BrNQEDxplIn6yEPKZXka0il-PgE_oQkDS35v0RtDf2HBw4kDKM4HfoOh_iw8fxe2EW82Rn9XmCKLxfNQKwjaglYkXSmFuZcEVTjbMa_EzR6gcv0FegVnM1F9cDK0vqy57zpZczQOpU57xmI_wgU976k9X5GePFpECSuJfLgPZGKc3DdCEOG2PKsX7e_alYq9p9fXCMq49Y5sOuUxsK-vEQG3bcnsGRHLVEZs5HLH7s4-jdrUev4FB5kVoC1mAW5wAbR3I0cg_QP2N2jKk-bHpRYOXIni4BOnKfgMhjDR_HQO9Z92fNfWJq_yuFxsxsptGHqvE5Kr8cGaTeUdlDIKhWqVKcXhOMziaaBsDGFtkPBg993v_4BAo0kxYbrf23YkjXCM7WS3DHJKaiHKs9T-_sJhqiW3W9aEm2aMa30KeGVkHcjxEW4JGGwOvRWi57HLK9swPTA2dtg6dBJ4Yag9N8S-WpYGI80nwzwqc7Rwl-eIuPYeLINCAJY1u7RMeBxxcmBvvkiRBjrU5WXsOoB18-JskR56EKfcWulQoL8kT58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf7jx9nLoDK1zO7wQSAMmFYgzljtNt_uYVnBlG6eI1tSz0LQkMghrFtydwmPUQMU1ggHCecicVV_JTjolZpg0sbr_Cz3em3AcSSBZYRVLr_PVKJmLhEa-LjEuT7JA-BqWnyLfgBjYmRlG-ThyJs1wWlb_wbaxTCUM1ZVUJZQD7W9jn4uIBod59t7wEmf4wcrUH7QN7S-xLih1nn8ArM3Es4r9z6v5cmbPbeXygp6L52aQzFpcp6FfN3jSiFdW0mEkQmj_C-NQxiuQSCsmmZC5WTdWgGndunP4QPaeLyDCp7SCw3TQtI4sBLRLxleUtxCP1lI5fRJkjX0v46a4pui6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5NrpBR3ThfESxcvwvQxi9FUE-EZOPArZsJCivTEaVYowtVb9Kw6JfhKQtTKeC4NVUnI_wEkdT6UkuKJ6q_YNVR_Q-SPt1YjCVB4fwU1RqF1YEGnP5C1j9C5G3canUisFomysOWdMetC6FicofcepBJrwugoWyPd0kPVHRMcN9phhbapEF0Oz190GyCk_uXIRNtHvS9dplDsbA4U2sIcOFZ37BwML9OW3nkM6R8kFd-m1xDxpRIN5E11hjF2ItbwKbEi76PpRRkFnGjvUCin3VKzSUk_gPtPA-BdmLFRiwbtmni3p-PXyL0llSz1uJN3Ap9fpwE-_8k1yg6Cz-kMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVM_yA5AXOiauwtglTmUDw-l1Wv2QytRe0AKXG2sx9D3UVvKqy0aUhharxHk1HjT9CkYHuyvEwHdJXINWb7lHtVz3hNI92GZ8dZDGiTAOhFsBGXMviK_59ZqIx3tTcA_F9EWTcBIFQX0mytdKcA2JqVLIGkFkQyPn_h1klCk54TFpd_3LWVzThwlTIeRhVsTtMqaIhRS9IP_zhrkbz2ZkJ7fGLHAep9Bi6BOiuHweoTAig_akEVR7PSgB7wCt0Bn1pPU1cxAy85wF76-R3y--RGMLRAZxUmM6_BKw3_c6YPTWww1zYXVtZkTSw6wceCktOe8szbap3abwl_gWtY43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3q_oC8xYTAH9TGYWwZoGxJ8CH-OPfEsPZq06joF5CxJICFbAFe5gblg2M4JUXz33RTKQ2hdctDZ84nfSBJPXNsNSEZafORIAeCnt6pC8iRZ-OgQo5K1j5n_UsJzmzV_Dj0GCfPCTg4060QkZaAXy52djKX_LTzeLkfVBk5S-3cFMDAzGz1NII3bI30QJG6Jm2EnzcwAeX-Q26GKEafl8QXvtnmvmCVu_LaK1B7dlXZNAgjq4UmqUEvEmFhByxhU4KjICsvSsWxENG2H9-Zb12ytgl9W3zz_OZHnBOwAuh2JeFVq41qP0BkhLvPQm1cqiHwCB9eI2W3md012SJEsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUzyPXMq7C-2OcQfORU-z23qNAm6pUzc6JQ2CMOypEJta05TchdjhzBiQLPJvtTCWzGGoQ_d4qrdKMUoWHwcAqE-vxKxHRxuUp1qY6NHLrBHcEXg1t3CS70q4V7FoSqZMtwuO8TixUyhZh5wqR3KPDv_77AQr39_x4nO-VnE92466x4nXwjvANM1OIdDjP4-wQCAu91vwYdX0WsdnLQYHC8feDSnkZw5q5V8crFUr90NbayBiZ2p59cOldkfBe4KuG34P3yPlpO4HZwJKIssaxzzp2RrR0EclokvnPEla9IkpF77TtI6RCUl-dlP_7oSnINffOPmYTYeGSb0L1ekGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwRUf050fi2HxfnJongBLmcLeo28lwY9MykM6wiBOZeL5a28ZwRdRpl_F9y9ji5Vd2SRvLahDOI8wpVKkTFCmzoJsyTXqV-7Kl6nxBLNH2Rp7aqgJNDXsD3E3p7rS29Rk8noSfYoEmR7TpKyhjJ7h0Xp8UkYzI3faIMWhxCe9T2Ze97JA35qm59-r8j9jQIOT5jxZBRcWZ19CrBTkck4Vcnf_YnMw0WO2MCZc1UYRWw2TYEAlEotnSX-n-gMy5DwS-VG1v4ri-UaQBoaFI0fmjwTYvZFM2EaA_zQNK9Qfb1-4Gr7560HTroV3FjzBA95RMS4alANDSCzxY3sEs_jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=YmV2Pp8JjJ29lJWAMo6hcchhpO4tJwWwVfLRdpfAEnKppQdL8GgP25kEziRd1dKrYlfQK53Bsfh5L8rwNcABOfG2ZgXCfNXnKORjGL1AX8Q2iasK9Y4fTI_bggG5YIXIj_M67d_NBY3ura66bQcZJ0nsus2N55TrAbNZTC79k_lUYFDNEZkw3odspDjM8mYMMwMliSjSs3eM-tfLF53VILY51eTqI2Sf4ACq_l26VeqLXtl1kU1WJqTv1gbQSzVFNdWJafdegivrC-4AAT7-2Mreef-izCM_lEZodIcPmfyyD1inVr8vZvX_mLK814PtVbcO1m83AHwl6FztTPwlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=YmV2Pp8JjJ29lJWAMo6hcchhpO4tJwWwVfLRdpfAEnKppQdL8GgP25kEziRd1dKrYlfQK53Bsfh5L8rwNcABOfG2ZgXCfNXnKORjGL1AX8Q2iasK9Y4fTI_bggG5YIXIj_M67d_NBY3ura66bQcZJ0nsus2N55TrAbNZTC79k_lUYFDNEZkw3odspDjM8mYMMwMliSjSs3eM-tfLF53VILY51eTqI2Sf4ACq_l26VeqLXtl1kU1WJqTv1gbQSzVFNdWJafdegivrC-4AAT7-2Mreef-izCM_lEZodIcPmfyyD1inVr8vZvX_mLK814PtVbcO1m83AHwl6FztTPwlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=BLxOjELy_y3qn0DeIJGDZOyAJf7Nvos5sZy2oZ7Ed7FilnSAfL7YbADQ98j6qHjxM2J-nN8AAr5lr0h4v1g9oEb3PSL2HML7zNbIGcBD5OhuYirmmFMOsq5fL4UHuoA1y9JBi20PdZHnKGgtEEBoKXqO64eGjmcDLBTujQPYCJwkXkYcCfxpyJNxg4yAUZj1LoeeTsiFukyj3jm_9NJWrFquy7QDdMXZcbhSbeUJP3ZEsOPREZwU8WkDqTEgwCLptFPjtuv0BrJk4LcwnMkG5dwqiqWBzr2tpKT_2VbkqC9BtKnA9pn-netbH36z24jCr2ypdQg30c1NMXaCSQj_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=BLxOjELy_y3qn0DeIJGDZOyAJf7Nvos5sZy2oZ7Ed7FilnSAfL7YbADQ98j6qHjxM2J-nN8AAr5lr0h4v1g9oEb3PSL2HML7zNbIGcBD5OhuYirmmFMOsq5fL4UHuoA1y9JBi20PdZHnKGgtEEBoKXqO64eGjmcDLBTujQPYCJwkXkYcCfxpyJNxg4yAUZj1LoeeTsiFukyj3jm_9NJWrFquy7QDdMXZcbhSbeUJP3ZEsOPREZwU8WkDqTEgwCLptFPjtuv0BrJk4LcwnMkG5dwqiqWBzr2tpKT_2VbkqC9BtKnA9pn-netbH36z24jCr2ypdQg30c1NMXaCSQj_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVlWw2GYWYw7xE3BfcGYWqa33bDteferuYWinWChq7UXWtEWT1OZiq0kAKx0K_jbNk4krcgjbnS7w8MXuRPji9v4PjuKRaJqRKdcn0LXM49MqyfKJg-WRFJb8PiTPmwvj9qYIiLgJzO-H-MXDStPTF7Q3_GhFsz_YoLRJ9uUfiDDAxTfYMwM8dzfaRj5EBfDxsd6jXzFuVfJO_7ujI_orYHEI9PnSqchN9FPqR_8i1syBjxHkoBGwqa8wBBJO8Vaqcsfzhp0Js7mme4RlxP9SnkxLXYy7JHyjnnUsDwhmzw7OhP1LhulR-p5IFB7HfNk3-DF6VcTFVO7SS-IPTFbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUouvOD34kLUBTqCnyg8WoBtQFnT6e6lZktNRycG41fijqfBMnI30HxtGRQOk4KhJyhfyNqvnEWvcXZMZpyBqzAIHIXlR960s4kByI6rVCgXOi4-x1-m_iNa33T1Ron2ecluoxYE1teCDMCvKgZBNAQ35O_nIv2s7wVnJZXIn5VA6pmpNUIDQLlAbRu_loPFKE8eFGu3I7ql7qpUwBwMf_hOjwMNT0sM3bGMGKDFhabIj0OLOLph-KTddXSoOiV3DtWOnhLWDKNck209zvIn-_1gO6HUfp2Q1bEP-eDLhWQuPSaXqWos98-lxFcu2YZ95bpwT09cWNTnPh2fSfKY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDPQhtOWdLEa52oMZIGKEtNcu0uGSMnkbW1qSXR0FfvfaAeooXw6r8SspKSiktAjZFUMcZvx3Gf779s2vIzwrrVnAyoMBFTnASSRCg1xH9qHLj6ZJ7DbGdYrTS4aKLJmeidnsQQGv7nyTZOQ2VmXap2ILm2AkWq3723zeNi9vxghSiD4XeKGqA2LJ4Q_iaJ4aAXzMeATbVzHHooqr8Wothr2y0aM1-lMINOGaiVgs2Mc9NCJv3dtbKK2VednmVYKGotMYS1fgpgij39YmFeHNpcQbXVLKuE7yegPVgEakzgAToMd4fIGMiPUe9_htOGk4aEFSgroiYfGq7iWLawQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtnZGc2IBQTfvpUMlFbsO5A8Vmnk0_sHfZlaeyIwgLc_Oajv8MKz2OwPUzjhpFtaZTGAdUTQaHg0iGHbT8jp_fl4MrD0PXSWTVmxvmB1F_boLwBxtY1drMZVceKSqiJk4buvfrGs1J0DCXcBWolOxOrQuxRo8XYYD7MMKkiGPz7vpl3tpZlukYGaTNEOUuQ9c8poKAapi2VwIerO7GvSyclJuyDks3dEH8AndJpjXhBR_6nVDxUEdwTOFd-fk282V3rAdhvWQ-XmIisR--JVzUL2U2QFLR8oE9PGbedWVThv1lL4tZ49Kzag-w1bWNWscteNLpvbbKSwX0gdfP-Pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9_chjPNIOnJRoMX5tZMDmVF9PNm3f4hbG9JuQST1J4nUVMgaveSxPbqb5S-FJ2RF2I6bwEFn3QQwBjXuzDFBtwtrhmUyhsu3ltQsfmRxlgjn_XxgDEXrTSA92fdgDuhKFB_AqNYcKHBpkW2yV0FMOiTGqShZn0x-3G7GaLxhT4-2obhNaOzGJJUhiLE4ABxHocv7dNAAbhG6rXkgkxnhD-v_mb5th2i1NOIpzyqiBZyCvjwxQFCRfr6rZyoA6GBDsN7obFpLgCQgT6Xpi9oqEOdavTakpMseFXUQMzcvCQ-LiugsicAIj89TV8oiEFJE-KkeYKkITKBnqFS6LLVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=I-aXu69dDPk68IWXUiMyj_QQ-n8Hc5ex2XfJDrhdAay9K-eoaM5k4_sSV_KVz9_Wi3p-0ZNKl5RI5ojTriG8KKJ0BbGoYFOWvFrznSP-UOlMWkYlav0X6N52QHADYRh3dzHnYxsh86C7f2UjFYcPqykdVnm31OBLZ3IR2P5uv0j85qJvfDvYC_u6d559wNXwBQwWGGqvS0oyO-0Fpy4Us298A4I7TwehRwCdsQETLxhiwdKozWn3Zbpx76wNbNNpKotYsC8CLqpm8K29GW0ZwvcR8iGU0dH-gnQFcgweXXF_CTU4Bz4il94_n94dI8oR5RAZTlld8graXYvVPgxB5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=I-aXu69dDPk68IWXUiMyj_QQ-n8Hc5ex2XfJDrhdAay9K-eoaM5k4_sSV_KVz9_Wi3p-0ZNKl5RI5ojTriG8KKJ0BbGoYFOWvFrznSP-UOlMWkYlav0X6N52QHADYRh3dzHnYxsh86C7f2UjFYcPqykdVnm31OBLZ3IR2P5uv0j85qJvfDvYC_u6d559wNXwBQwWGGqvS0oyO-0Fpy4Us298A4I7TwehRwCdsQETLxhiwdKozWn3Zbpx76wNbNNpKotYsC8CLqpm8K29GW0ZwvcR8iGU0dH-gnQFcgweXXF_CTU4Bz4il94_n94dI8oR5RAZTlld8graXYvVPgxB5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D87NnHtBkyFelbE7u6awF6K-NSHYUjEE9OFt4Urip4lz_BqwqCjwfPmrTey_TrmcsnZ-cj__Aq38q1dZfrdyu28Uh8-r3SjxNsPcoje9K8eSKa30oR8x1zRUg159NuafQHfEMP4sbEsZcs_4UzLALVRoQWwjFMIIebkEzdeYNaePmxucuIU2L1j7GEIDkZV6HFiCQk9Uy1_PJ2ICy68hjooo9emzyi1WowUehjK47rYfY-ai5OyHoKghk3ZeuZaPNELUavieDjtA9-bTo-Ka2CRpZdXqN4p80GHVSUJK29-sbN4Nax4E_tMrr6eWB327IeslHwgnCR1Bf8KQRcwmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9d4MexKRQVm6ZRP1l8ze3g7c4CCoWSZ-dgX45MP0QqGYmKyB6ymew_yunlzfu4BZ2o7T-PEfVNQJ-THH_DA0Xo58g_Qe2nYc7O0b1QQG4QUk_1Nus2HYH4Shmb91SaRiKbgz0t6E0yE0ft9qu6HY-sRtMZiiRDNgX9fVLGSohdRXME-Lozf5L_nte5J5TjOR4mFCFl3OJLa9WZH2hqBAqllhuc1eeTXIH5It5T0Kb4-zIrgki4Q96VU3bzVgw37Yu9ylcK1utXDHTSNGuAxyg_JiAXEPk9OwoAMBHdJmWbjIJAxlz05n-ZUc2SFKuTe5m-XmbyFcdAqbv_8hwFWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvIfxr7-oUf9l6nwmykBUuOTwtQv-pTUSQqOpGPMJ4VyU29UzibrSi_aNAMY_lknGRerPjSHSlph8auMi_wdEIN0JOOrpe8u7mYHFCX82_s2YaT9qJ32uqRP98kxGBIybaqBGSz9TN0rPARzdX7ayQGpwSog9mJSkAIulXUarOwh-rOghVjBjbnfXzYECjc6YcQQ-3ts18_jP2fuFOHJUe8-a4It_AFnpOjHqkkP7N6o2bMpn7xqyrmH9b1GFiDZ8NSfVzSX4L8Y_ys_VAeHon2leYS6hc4gKZsUnnf9rMkhtL6pCb5ze5HM67wHph7IhkQ9omZIAsy5smaK2PeWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPdtouQXsTvrOamWDgby6R6WJ-NyDA0uIK5RiV6rDMKDD-8D5_BRSkqRiHsSofNHUFgwTmd31VygDUAoD9LUN5kfPVdM2pcCzfrbm2-ghhTPjhEzuQG6d1O-1nN6AFOKqntlUYU2l-ZNrAreeniJIE14HlNvPtFVZuULlBQCot9db-jdDx6d8nyMP-35gBVt-zzrrZF9ZWy_5iBxHpcd9U2Ma5jgPFOxwY6GI1kIRz-LAj5cgQzVjzdJG5g3KWoh0ZLP15BR_HUd0Mki_CzJSU3pSwTKDarnEVY3ECHYpqB8aZAX1tYGgx5ktqlVZAvqji8UwJj7ypzh2W41PzH68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=m_Ln3T9opBu-_LUuWP8jjb5JV3_w4ZTNR97TQ23IKebVrihEv3YHZze_McWtxbRwn1JxvSiro2Ql9rKfruTXKEsNA9BPv2DtUzhqFgJ7kc8_CJEnGf3yb2B5s8gGD0ajGx0zCr80Bt10_HeXJZRrv16kzXf9bHBKSCL0MQg8I81Vm4PMUYRooVSGshgk6W-QwroYgIhVGspxuMcTm8aZzMpEqJOZa7Etb-ALOKzqlOUOQARDV0HekEDdjM23_sydLOAeO51-jjRDkC1cWGV2hgCIZFXVvulJuMK8uEs1PtWPjqz7sc2KRDHDnpxdtEVAevJAlPvow2OneS8FOYlXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=m_Ln3T9opBu-_LUuWP8jjb5JV3_w4ZTNR97TQ23IKebVrihEv3YHZze_McWtxbRwn1JxvSiro2Ql9rKfruTXKEsNA9BPv2DtUzhqFgJ7kc8_CJEnGf3yb2B5s8gGD0ajGx0zCr80Bt10_HeXJZRrv16kzXf9bHBKSCL0MQg8I81Vm4PMUYRooVSGshgk6W-QwroYgIhVGspxuMcTm8aZzMpEqJOZa7Etb-ALOKzqlOUOQARDV0HekEDdjM23_sydLOAeO51-jjRDkC1cWGV2hgCIZFXVvulJuMK8uEs1PtWPjqz7sc2KRDHDnpxdtEVAevJAlPvow2OneS8FOYlXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti9oCT7pNu-888xSesK2XlcSvrxHPfLh8mnWn6hXB6FSHlMbxTllLo-HunKUPWlz1yLIQ7XqcT_DsdK9tVEVt1oN5MeM0iQA0E8l_nXS9Y23sWQQYDC-O8hCYE7bDziRW4piM_BG15ERxhc0wcOAGX_zzztqHZhGbJDq40SLKkeTWxqqWwPkIb8bV604tzwxCjCKQwPVeFDBS_8JuUXNVyGVmLNAYETTM17xidPvO2nEICUWoutCnJ8R5JYuVoMozbi4vgKzPpSoDGB8jKvQufJsPQRbLIeqk0Kco94GRrP9_UxWUq5Ng_xRaFTDNZcoOYdSSB4nCs5T7gcckWw-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaCAvoLKP5izezm_akgaIwmU2aZxgZWsAEjOBn0moA7fZpBgD_pTDr7HWVra4005i-9tKYS-n6NEGJk1Opsmf4FppOPxlywCF_A9G6BWhnFfG2UAS_N0PTRMaidcDdzvFGxQiy2zkhum6IknUd4oxBXdo5bfrwjiKd4CZrrB0qOioQMLKvQVtIyajDvriDlMew04ugrd8cpvZLbuhFLteJTZYETbZSaJrYZBJO-eGk1jBHP5dBU0aBh86eGGLKxEU5f-9AP2WmDV79y0Recc9735NQXmCyke6nvzwEmUFYTvr--Jk3vHgzCV78IsiFk72uny12m4BA37cy1lU7nurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke5Ufr_5SrkfuWpBa0UzRZud3jOBLtoGi1LSW_WlnnvCUEdLqXZ5VzOHpDrJGAX_vTCrfP22wNrd7E1MNpyi0P6DMijEoJbRIB8VxmEO1B6mEedmV6OW8DQWXv2B5W39G5d2BfZJnIthPmIIsbvMFOABzQTHBE-Ehjfvv__7lDN15KT1WDheO2QCYB0PEMxM-Kx1RYVSRlyu4BCSXzCoiMA5h4OUxL3GSsZozuXbqeuYO8T8eq-YEJWdn7S8jtkqhrQdPm1-6QQlp2eW_T7V49wImXzC-ckn02uh0jFszXudzp-FsQ8dtllzJD9GU8xTNurmjjpnKGzntZrQq3NnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=RG2iemSMv_2JcBOxUbXnQMseIZetLv7MoURpHffSZ6icyBz45iXSFayl0frWGh5PEOnTyDg0nKaIR0_OJ_wxDQ3nho4tFlX_HcAesZvJrLtNB99v_dCGAn8HrK7FqXUtnmu7xQtP_53NWpPCIAHQ8a6svfzEBpmD0cp_wIbL-dq6qXSm8mRev0UsdIv_km6YU6J7BnZaXR_w-76-hZqTpJezhckEUyR3n-7oG99a39J3YXkGot6_6JPRG6zA94TUYcxpB-XE4E_2XxdAFUEM7IzkXFn23YQypXefsa6U-Xq5VfUpGGOZDO0jnJ6LMFRys3bo2LkOLJ5MVkQP4Vl1Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=RG2iemSMv_2JcBOxUbXnQMseIZetLv7MoURpHffSZ6icyBz45iXSFayl0frWGh5PEOnTyDg0nKaIR0_OJ_wxDQ3nho4tFlX_HcAesZvJrLtNB99v_dCGAn8HrK7FqXUtnmu7xQtP_53NWpPCIAHQ8a6svfzEBpmD0cp_wIbL-dq6qXSm8mRev0UsdIv_km6YU6J7BnZaXR_w-76-hZqTpJezhckEUyR3n-7oG99a39J3YXkGot6_6JPRG6zA94TUYcxpB-XE4E_2XxdAFUEM7IzkXFn23YQypXefsa6U-Xq5VfUpGGOZDO0jnJ6LMFRys3bo2LkOLJ5MVkQP4Vl1Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFcJAThzPfiH15Rizx6Dg6uYyBUdXwtF-gqT2BcxPPtmkrgahcp-DDE-A1Rs85CD-gbE2xipve6Ew80GC8lWBdd8AeI7z5B1Mv0WU50j6fWQevt3RSE_i0-28EhbQCfPs-YHF7OPvX0GS3wC6ZPcRzA7tpovUU9FbM-6vTvK3VJjskJZV2ii9-Pr5tCorSWnic76-5vJr2EYfbqJvXqt8OsnTtvp8wCKfrt-0A-lIKAX6bkgkIFodPnRX4MY5tGRQQhXxiNuXCNlEJGRvjHwDQeUl1dGw7vuLMWcafELqqRdftHoeQj8bea0jIiUthoE9omjVYZ4QNjTtQbkCr1dFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ8IpiBguFAyNo2JJV8vlIbcP3BX1nQnfhGU17vbbzJkrMAlzf6HXbbtwse4WRZKhckZbbPpaJIyTfdtxVohSFfsnHKQPeqNbuDoAwtwdoKQvaQlJ7zpgFOGjz_Mbq47PxfstZ3YOigd6VmuXL8TxPjO-cnOFmPp6Z9zfSSpwKdgL5PFPlvSBNt1ENfBDDFeJ_ye44giU5Tm-jDUoYHsnK-uPlu_UxFB0wc1wpF-0by2bXZ7aRkz_DbzmG7p4WSJDZpxI755I_hDBT_kjCy1-PoVl3aPOueDrNxwsOsz8HAb82FbFGKNE_ZzBUG8NRCAFuCxcY-4jioFA25fhTw3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaw6dkoaD7ymgJ5i8_1_sM8PknRWKLsoo7xVmRxajKc0ZuuYeHck7k5cWsV_Ksgv7zqP8G9BN4Tu_dBbKgI4iqXkB4J8L_EEJSKEOOPWzOET71YGAFLkImyyn4desV_-p6HQwZhEBF6jAeq8dUV0izANUVzvOXkxrYRow6WnJqQ5jRIZpq8_upy9f9Hsi1eTVIxr0VACYblbVpTJbaeriA5cBDPTLQCFMFYuXoEA3_99C-eJEFmDvDsTcyASj--jdY7gkvkeeG0vEbBBec-36MDe1XFaJzCKX6MzOmKGz9BdD9CAl8AvquMdcYwpTHYFe8TOSxJUIv8Kc7pZpdel-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPDBvQj2UNHGxJ9Z3VIzSsIUd5lAkX9DXdT9o454liY7RWn2lPVTxkDWnPLl6yDUEqdBUHISkZtnTDYvN0iPiVv-_W7s1uYWf0oDN7XK0rW8sUn7gm3uif_OhxPdp9RZR_BuYJs5JwAfKy_DV0T8wCajxkMVmuw6cMycsi9tGDJr8r6bSsCwIb-0XgdnIt6SO_BpxxofV9eXl9_UZsFy_z6kYoXWEVpRThkXjB2k_DLHZghYWofXBOpQw9kYWqMiMQ2o-FK-1W2vqqTBIFS7edQNovhHWeb76GUhaJbXJKiYT0YiKHCmAFwuUhXUMqYaBVMZErPzKQfnUEVJj9QL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=rjWgeTRNRkRL9mVuF6qesWdb5Ri2K7s1CM9PGU8brt_19lX-40LyVjHXEejBC8xEw0ps15x5-cEE0GLR3EcGCFZip0v-aTXnqZ0u_0ImJrGIevc6GSco_HSLYWuPTxfECl9e5ywQSTDzdM0TTNHs_0ZdNawzhKJHF0Ystvz4O1syiqVkW5Dx0CWD4UKcn42L8b_fhu0cZKj9nKqOl7z7zqKrpekiBAXsPDyFXNTdetVUc6cHsLcOJj_l11dw2LBaUnqK799rGT4scuDW1W__Cuz1bSI3PwZIGb1nvFGQk3SNaWRe63hsfZhsKk2BfGJj87VgtAV8qYQZ82Znnsi_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=rjWgeTRNRkRL9mVuF6qesWdb5Ri2K7s1CM9PGU8brt_19lX-40LyVjHXEejBC8xEw0ps15x5-cEE0GLR3EcGCFZip0v-aTXnqZ0u_0ImJrGIevc6GSco_HSLYWuPTxfECl9e5ywQSTDzdM0TTNHs_0ZdNawzhKJHF0Ystvz4O1syiqVkW5Dx0CWD4UKcn42L8b_fhu0cZKj9nKqOl7z7zqKrpekiBAXsPDyFXNTdetVUc6cHsLcOJj_l11dw2LBaUnqK799rGT4scuDW1W__Cuz1bSI3PwZIGb1nvFGQk3SNaWRe63hsfZhsKk2BfGJj87VgtAV8qYQZ82Znnsi_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2duOXgv4rEedWoKCVaSU3JNnV5-GWF1udDMGgC3JM9EwodpF10JG2EOmtycgoIfp_CPxbL0Ir4hmv1jqPlLTrtudhSGxAtvT_YW-QkNg74RHMt60d9yu3NusBK-B2f3xJiMTOx4rlA5WnSwCxrihpsTZCbog-vYc1ui6h4y-7f97Mu0iqThNDhV2JPQcXi9SBNaLiVqA7X5Az4gezUesauGWl30Dk5z38ykGeu09s5ny8_iqUZzr9Al4og8tJEsdf5s2hFQD98t7L0hdGU3wYynQYZ3SSGPnSO5UNnH_8NO7PsU0aZ3f8hMblFc490ocwTGLnKOHuN3vYx3qPsTvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=auC3P83ih05BX6lY7dUNS4d0bcmFBkcvwk318oQz7oZqQPW7TT0nCddXb0uiSn7PIht45tCgC4c2m-YT71TgSrPqRGJeDVNZfXmWsHf0yb2sX3hkHksIUhrbp3g1eU6jrx3zZ1UvfCmbEhSKzDof3TyHn4P0K7WsHy3sopTBbFe_NwgqbtREFNZnEjiRF7TsgBxQMzq2Ro2Y3Br0NlNoQyeU55eA_-3NfQvGKb4M2CUmH64KekcwA-4QAvI9evMy9jz-EWXwZTFqAr-zwRiAS4kiYiiGjUTj-DtxaUWekKG0S_GRctyJd0IDm_xOdUkCAzo2C7rKYUN4TPD9m_u2Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=auC3P83ih05BX6lY7dUNS4d0bcmFBkcvwk318oQz7oZqQPW7TT0nCddXb0uiSn7PIht45tCgC4c2m-YT71TgSrPqRGJeDVNZfXmWsHf0yb2sX3hkHksIUhrbp3g1eU6jrx3zZ1UvfCmbEhSKzDof3TyHn4P0K7WsHy3sopTBbFe_NwgqbtREFNZnEjiRF7TsgBxQMzq2Ro2Y3Br0NlNoQyeU55eA_-3NfQvGKb4M2CUmH64KekcwA-4QAvI9evMy9jz-EWXwZTFqAr-zwRiAS4kiYiiGjUTj-DtxaUWekKG0S_GRctyJd0IDm_xOdUkCAzo2C7rKYUN4TPD9m_u2Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIh_kS6QlDWIuBAKGKytDW9_BmRh_fZg05aY_qjSpUiIoveaSdkQKtgEmmAAreCegJgoC4kWUHfbElZh_jJwfHbqrU5iKAPTIsHDRKTezD2oArne_0zKH6oqtjx7V46PHtU4jY5qJNu4o3-q0OwiWmLaiONSxXLKjwLOH1BZx7fGv4eFGV0iP5uRJhN3a3FQtKYwW8OuPxgZVtRis1j_3C5jmpPGjQWPQaTIW0GvLKC5u5f77MIeMXNxRbrdy4NlZFqCparQIB8O31mA6olIrgH4xuBm0tjsekl-ogomqktJTYgu4XQuHokhLeMgYA_JNbhG_bJ5kc50VWN6Bq_xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HASl_LtQnRyUL__jgcXbBwgkgsaTjG2MoSnOhA2n1ArDb2iazVx4AT3RuN2RjSzQTj5NapmKR98XE-qE8hpzaHlfl2_3jVDgp4BLYmKvgA7MyN1eN2ELwBEcIdzidRQovciKfz2W2eInhIYxvziX6jgtdqv_phjZhbX93fRVtCNOr7AwCgU-jkI1_qPOGhgVcR3OgAwqRQfsMMv8XqvBzRn9t0omWxiXQzhGYRRk-FBGY6FiRu0ucxK-5l6pGHuNQiIwC60V08Nn_c22DgxnIKn7qz4e632xe-dCrbM7gep75rzfDvqwjptTuOjQT8wSe0DbojSqx_h_0hYg6ZOXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGttK1S_0X3hlX2rGgavCapVSK71BJXyswvda9CHr1vlPeB6zeBb6SqKEmKzVzZbsXxnRcdvVy4KgRDC4U227qQ0uiWca3VWd61L0cPNLH1P3fV_seWf60xmsdEXfa5Ddy1tCG9ZPIfz2bbDLXvE0d5ONBh60zZAUusSCx96biK0wyABzCsFbY1gnwEy4gvTJYJnXrtP2u-U6tNBFBeH8knDVnQZsNbhhRwGJLL4t6rwPf8PIa4QtFbl48HUlkMCOQ28KEFpTSLmDaExPm_rKM5L-a439QKgP9-LZGO7RMx2jFdC2JC9JJP9gnI26JJwRbWT8qZ0KnczXS2xFcEYag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJ8G_iW5fnGzCg7hziL5UCcr2tUMv9qM0revXXRSsMcE9t3J8rwkyUtaEaUde21gwU6mzApQADvItGogvoDbMPtrvhfA8SH53GgIIGlMrZCMu0qpNVTciGv7s04nOofB7ubceCPJ2uiiDh2vytmPzFoTizKZTl8FjSBBCIZJcsxkZDwQR_FrpcDjLEcXNwlPyysjL05xQMGhgSeuvSl0r3Y71jpXYFFYPIwRVrJE3YOiK47ZNrMoSb3TC7BSWU--7PFteQfG3C3iXSHuwY5hrrOfYwT9wLsa7nJ2MRFjkV9JNHCw90qB-aoZ8-6tD81jMqHx5BoAy48vTJSlOT_vRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqiY4-AcU1WPrfGIAdOJ35j7CtBlSX99tRIWq1FXIGJ00dWrUMHn351nv5EIBlStz3zhCsG4AK-TrkWYXojJUFEPG_AxbsslmaAcQPXTC5XYooAeuaHkMy52TCfzYqLf5SCndLWvj-NHFoMFoWsPG0hhGs21nR_qEc86s5YPpOJ0rTxOPSB4TPNcatqrUrK-kM5GDLkxcQ92E7oWPo8AxM6ooVDbNJL4O8iedrtRu_tZWKy5S9MnWKjsLr-MXpUKkK55Owej4LMHDtvmjisDMEZJZlf0XODbGxWm2LnCR6semzMa10Dvu93JyTtO-ZlKlObIYqBSObkdfod4FxcOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=cQ2W4QX1mcRH3xMa3op3rZ7uSwxiqofQk3H7UwBqr9nzDfpEoptfzwg5LEwRaqmErbYaXUtZvpzBqJmmrqXQtEyT1QSN656ogumHC-nJvTnuU7mKAtb75Q9fqWz62wJXIfQ1BOJ_u78sUDoMt5tS91FlMk_gubqMrhJnLa3Ao9vKB6N08cRmKTA2BntZtjNFcA8-irIGyqNbzC-NOCOyJ8tow3Rttj41HjVhUxIQDKO7merB3SEpcMJpXs49p7u3xgDVrSSgSCMrtd9VR3Jhs3ovC8FHC5PkyGGL5OfL6fyFjJ9lQKisIlcz-tLp1uhaOgmmfsMkBxcDtZ-5Pa9Bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=cQ2W4QX1mcRH3xMa3op3rZ7uSwxiqofQk3H7UwBqr9nzDfpEoptfzwg5LEwRaqmErbYaXUtZvpzBqJmmrqXQtEyT1QSN656ogumHC-nJvTnuU7mKAtb75Q9fqWz62wJXIfQ1BOJ_u78sUDoMt5tS91FlMk_gubqMrhJnLa3Ao9vKB6N08cRmKTA2BntZtjNFcA8-irIGyqNbzC-NOCOyJ8tow3Rttj41HjVhUxIQDKO7merB3SEpcMJpXs49p7u3xgDVrSSgSCMrtd9VR3Jhs3ovC8FHC5PkyGGL5OfL6fyFjJ9lQKisIlcz-tLp1uhaOgmmfsMkBxcDtZ-5Pa9Bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIejV0adj-DIqdqzd_YQyfkXZbYpnxw0GYSoJxwXDU_iMOj_7JoCIYcTEA4gek3yUXu21dXxLzB4_bce1VrzfyaZu3ypQ2F7YKS7594Z7khs2qci-_NkPQEEa5w2kagQHbi5LEOALICZv6Isc7IjWL5r24eLTNkRq0_wvwDTBzY8TGvUc6NSv8rx6s6JFMVkusOmxP13gjC-_XTq5u7X2hGlBencumyvRRoqi0D7ARF7pMz7KMfJs2az_SXUrpvFLVpWMwCcuJ_SWTHUUFdsmrlDD72PXm5sONQcMePajkHJODBUQwWmONkVHcB_ICSj7pw0ncU7l7KyTqhDXcWuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkUrhFlTQxtAW_-FSAHoXtnzoxHx_rp211WjQdaqSraSkcgKwe9cyU-Y__VtDZ2bYKlq8GtVUNmhLslifc1jsPsCv_DOA9CjlwiKgLNcaFJr5g1RxzMk1R0dC9JwzkWUHlO4KTPlj9KZufUkyNld18xnUd9PM6AjTHRlqRGXLPrEEo6RrR5H1E78hlEKpNyrntWuddOWXDLx1gtGW4TxNWy-9Px7PS29wH_NsHO7s0pRz8ssNsrE19_nMr92enk6BosXR-d-K5gwsT87flngU_hBdBBjUA7dQZLfUdlf3aJfkHJ7XLwPp0S4e98NakN9UcLvF2HpLo48hB-9zkkY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=rcFoJRGqDLn08hBNUgTPPF18yvQY24yy7h1-5UPSlJgEonyaQElJHgPoP6K8iYds3CsnlqkmumOolMFe2IROjjuU8YoBYJtxbR-2oU4COqB3bySuFukgswoXlFI05lwlNhqE2InmPguCdPSe_QXwvn8bqrCNJKTUPOYNwusnz36oFEaBk6BkTA6fcEL7CdZmdOla3p-_Psx4oDT0z2l98vrcJKROG0immwGjvCx9kanHXio0_FyYt-5p-qcX7slodHkLl1hPEV-Qp92cmMmG4iNOCKunbi8g89_JQJIS1DU1gIlVcLIv6IyzDii_XUmCIkfTzv2chVSg1SNKxyxD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=rcFoJRGqDLn08hBNUgTPPF18yvQY24yy7h1-5UPSlJgEonyaQElJHgPoP6K8iYds3CsnlqkmumOolMFe2IROjjuU8YoBYJtxbR-2oU4COqB3bySuFukgswoXlFI05lwlNhqE2InmPguCdPSe_QXwvn8bqrCNJKTUPOYNwusnz36oFEaBk6BkTA6fcEL7CdZmdOla3p-_Psx4oDT0z2l98vrcJKROG0immwGjvCx9kanHXio0_FyYt-5p-qcX7slodHkLl1hPEV-Qp92cmMmG4iNOCKunbi8g89_JQJIS1DU1gIlVcLIv6IyzDii_XUmCIkfTzv2chVSg1SNKxyxD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4zsJqZKKnwx0uZN6Hc57tRh4B7_n7DEL7KSdf0xiMUqvjWn7tC66p3lMbfIbvnmq4RwJewBt_kjoxWSIQcC1FJJkVvaq9_pN4sGDj99lZrJi4ihF2Uc2b5HV2VMzu26tK2N4Od9_NOKicciY9Hf026OJZUXpF7A1LgK--Jw0XTTj0Z56Fmkaf3NjDD7JgUqCp_7CENfFSymGefYYfMi7QppbgVAFAHukxuiCi7lPFKxfYdpWgkrVjIc1T9FxxN9uH1FhCTuOLyh9335jXvR0g33_JOpvm_2PRs0lHEWsiGGa50o3r9jC0nYbYTjkcdy8QHKubv4p9_n-evArXm4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQzibHy762yxZv8OToBpKSlT_yC0Ix6pN_QHnCwDSaP0prhKlH6pRG1Ts5TtTCiPpGgjPhiDxqwgN56Vwg4tJgsaJooAg7E-Mi6NghmgLQ9FSD8MQfcFV0K8db5mXH6AlsNz7kkaL-YYb1k7aSdi_GMJbdyHNhYJW5GzEE0HOvZZ-oKE4P4XXiEHIRMo2Y1POkae-JtGi1MsLbloqbdd69y53yeUMSFgO3VOtx1eoKC6pviSEPiHOrqRNAQH0tkmuzYEsp8P6pxViU9002Qu7OEpDCWINvCS3_183MO0ty_U4q6mYGIIIt_rJpSQn-gTGGRW_Uh0NqbdFpY8hOeFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq3eTDrDMQVv-nGJ5z3j5q6CmWwI8t9rKOMPA3MyknRk0wbfKPHJYCikYNGbwdoV4bEckinABpuNt1arZ_kQa-ViCvNrNGbGoTi8OQEyc5sfsEVLec1pLNVyPNZ9eZbFWH-ipQIZ5oAKfILsIrXTPcUVQTaTGJIrOPYKqQQvxKbaB3cRCyPlWZcDbMzIcWd479ZBhwir0KE1jqcsYUVME0lICd6vkCOI6YHVfml62zQaTfVVfAYX9UnPDfwCnSawRIB4u3317yuWjnEN8ewWR6ozV6KU7dsCsTg-z8iSuNuCIFCQOYXXb4HSIjSBoSh1bO4IamXEOjsKjHX2AYGrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn-E-3QhO0NlKf-F-GzyWRC3-_Snm5-cbxmQB074fizijrX4i8J5uh0PzoSB3sV9A5A39CUhGwo-rjgTs0p45b1vJw4wmcpwS0GXvkHDCq5bdufKm7hihpfXNK3etBOFtfOHzzT0KDv8FZhMebByXalLiq3HTNOt6Vb7brelC9u6F35N9vSAlFZhZ8e1vSVcVRBSgAQXRwweB5JTO45jKr0TY9w0K2yIW1E9vFy_t-4_PQQZx5cHPeyPYiDcM5o1mKh7pobS5CcojtW-R1gatWIeu0eQ69qoD8AYU-qBTUk7moeOv7jmlw1CFF_xWge1CCMOwi_aQ1E04TfRFJx9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XugTx6o-2lC_LFLCkNrDLH5UggjF3bc5m4Iu6dJV7cMXpXv6OkPHkEOCYjXj35LPbTHWimx9rafBHqH1BigXhd_eqkB3OSf1gygq5GwDeGmhyhM-GZu59_2-cYWYI5OC-Ly8kqb8544UIxt_m_iPZFeARyIqgYbf--UfvG2hkQ1mRkbKu2pHI17Nn1Z0jtp1ni4q92VpQ6WJrdK2hnB8bGwu3bejq6-AN5dO9KeSZ8V_R9x5iLuP00T8bwnSwvpZRwWXSmpGxv0C32GihVYM0QEiYVJWyoY9COkQIPN0nfWOYohrS881qQQVdXJU1IpjXbSSDTdtRDGDYQMc25n_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEkPEh0_c4_IKIs_4vvU1wX6Ffy_SwJRJinkf6khQqE6h0TqxHZbSeNMrBGbFN6PA8iFqCRWucNx4XyiF4WWr1y8VqSEhin26TW2Yl3rO_Xt-Sf0T0gFCHB1_896LEQ7yvb8E22kaC3fBeb1AcrfWbeoygIx04m4cagSTGTGyA5x3-VbvYAxh3htGt0NEa0jzvZ-kGh-7CYK7klIUVW0v_ZRTUe9bXBlKRXCXEWy32JM3-nSuHnTPtcYhvg_98WKGKBhGmH7tch6PlhD9hk-t1s_7qa3j1Ngecz38o034NvtGNUlRg7zcmNBr1LzygWrV7vlM4r9ptJxPMqLU1zNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCFdLZ2IQ6Lni09vl_Af8CB2QzqNBe5W9d51F-ZNcNnHeBoTYgKS-lZVQsLcym7ivMpNXHELvSXRiSj3YVF9QeE6S5nZZRcy2SYTCU2cKLbztnr77N00RDSySpvwNZr7_sW_RpsaLhRN8obZ-BOAKHM_6rYJTdz79mCOzpiwQkytFQx0RdtXwGA743kMzVNto4sragBWXOO83XqYoxC01uZHNtVzWcufwVnLn92lMIxf55rL57WUS3kjT87zETGMgVRX5TiOWSWsoYe9aDCo3fZIQ0QQGEF4uB4RkFVgzqAARGQ0gM02frKtPNRCmLHkOW6LTU8Wb0FQdlQn1hoSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLVjNqVc7DM3Ixc00Fp_mtB20URzbfXxDuz735h9XSwAyuxfnAJCDYoHc-vvboJIxw14noEAM7gn0NdR1prZcVprB3TdAEJU3aecDSEDncTgWJABRlWDsh0lIj3NO2Y1ZcME6xTJIFmr0xZsta7ib4EN1cwOARbRWEh26uoHnjjnr0NhuFsHOWVM_TkH_TLD-RYUxV3EinZNnmMXf5MRGxxQgLMBK72tcs2irOoarFWL_LNws2XS59LtdPWV_xRzwZvkKB7AweDqaGBfOpbXsaKhdM4a_rhrfV-SCXEe5863ShmXWSkjdydwFnVJ0_s2fw67eayUtAwxdfvzemsLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTgQzLMikRu2pgKOPT4pu528f4rRJ27Hn3JdOb20lX2OnotR9tPkGAJeY2U0rNtqut7tkN2LciBRQm8BmmZsuozGLR-yAgdIVdpDzYax_EQtFjGUV3Z_POiJEF8nDvo-L8rDF7pfYDLCmKEpLKA8p0kJo1zfBa9Bm7BGCEMOUXHQ4UzozlV8apngJzXw_ho3CvoJ57EuDQnr9A4yQF7e7A7fWWm0BJEk_F5vsSWpJ2qzpvfP4jUmlZxVW2aaM5FSUM5kXv5FfqqGBYD3IH-ch-ohmMW062N6oNqTj-RgIYNjNUgCn138UrMBA2JiTqIlaM7lUzNEvgjFACYxnhUGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaPYDNMIL0EbK74snfmyBJBFwJtBDnsNHcyeirQd_7WHjeV2eh5lgF2RgcyKvOWS-e7lhi6UE-WKMv5v1BLClVKPEAewecpyVSR9N9eBf5t7A4rj8cEFGbb4m4cBSNUQ8M_FzDRpnXx1gWW0hiFYNQDycg3ILBqOV7UCk0O2T46NqDlN_bYBEvPcDDSS2Mfe4betPd9qCHpGMe34edduz09WEY-4mzDHWo8p4V5nRYgea1du7QPGEZQ4EU2OWm_xeVy6DL2kw2Ig0UQBDebmqFRa3cerSUXp9RO7thWl8fVO8t-P5tjGWgPpzmlZuGnZJz57yNnyEmkIFj-lvqDp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=tS92Ko7arsp-obUpg09GIJXJLe8AmF53lcHtY4P7hei0dH_ZMqm7aaC2xeRDAO5sRRlr713-kZooIlTVi9kQdZiPvZitdg407MqCwG8TGbIoShe9QkEKvPKbU0Gg1i2RGIVijumF8UctZdHKtx8TRUxeJEsTIrO9y9-K0rkiM19iCMab264tHveWZVLXIV0aNNramvlgi_RG84tb_-xe0lMFudfQxK6F5ufqs3geXSjJWCX9Fhs2DC786_Bq0lmV8v3lAKAFO2EvizZq6VtYleRWvxWrSjRz5dQ_xLgrTUHNkREt5AP-Qiw1GtidSTqejuDStT4icdVSLvy8I_c12g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=tS92Ko7arsp-obUpg09GIJXJLe8AmF53lcHtY4P7hei0dH_ZMqm7aaC2xeRDAO5sRRlr713-kZooIlTVi9kQdZiPvZitdg407MqCwG8TGbIoShe9QkEKvPKbU0Gg1i2RGIVijumF8UctZdHKtx8TRUxeJEsTIrO9y9-K0rkiM19iCMab264tHveWZVLXIV0aNNramvlgi_RG84tb_-xe0lMFudfQxK6F5ufqs3geXSjJWCX9Fhs2DC786_Bq0lmV8v3lAKAFO2EvizZq6VtYleRWvxWrSjRz5dQ_xLgrTUHNkREt5AP-Qiw1GtidSTqejuDStT4icdVSLvy8I_c12g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHVaa7YU-74_cM9F0rtpyV_5f_yfFqEcYVk042PJGZyb3ma8eQoa4wLup1jdqYlGVbcZbdIzklyVwLVj55vlmFiY_Vf20oWeYSYp5j1py139O6GqSne_2gnylkTRZCg50CBVjaYqw4aRcpt2RTMyRX8iWGxMmhMKL7b1kPH844FWwBBkeqVdW-7xSCZ7IwkZB8Apl2zecn_qurkt_6132KubMbR9LObDZgfMKVVXNYFcA6tQ9eEYYtAIqxu9_4QF5Cok_H1g9dre0O87aCkVxW1HZSMbC-ovqZpP2huTAa2m9E0lGAgdtw3Pi4BZ14o49E0B3R2V3Q78rDInu_Z-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3XEzg23ohzsQVSnu4G-ywuB0IJcVdu2tX52L80E1ipGSFNN4jGlR7AK7yTdbb59_uS1ASJxr2vt7e3ubwZv9MKqdAqugjiJJ-fQxTmKPKQcqTMZwN4e3RSZxxu2fjgl_ydHAWcSOZKDCRC5iWlOoKVqOxDbUkgKLpuLKGEaOnXUrv-rDpFvVC3tlmMHBjCDCyzP7Fketz_XA2NTXx81QQbI0BS-1kw8AlKVNU5O3dQS07KDz-bIjCLLAdQ9MDfrywQfGOHn0wmbMHIn6ZYZlWlUhtf0wpx2-medZbsj0vDui7-b0CxM4mMiW54CL7g6Dq6TN7gqOfiiEp7VPR9wDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOHOxwLUi9zjXT4aDUOU_bJnBaY5HbgoImyuMuIXrVmaXfMVyge8V6dPuEGO_tN6gA_uf423-pTkOee6LnkdaIe6RrbYSx8hRTbY_hguZJsZBWpiVNc6z0nbMjSZrWHEwEWPwqcp5pm_ez-UphEZdrl36caNyd8nWZ43nB39mmmR3Fint_2grDnUnzo5TkDKVbFmxSH6aT51Caed3cADdy3j8GxAXFpHFMntXYDvoCtQ1Dpf2xq8pZta5GWErmWipdVjBo9VfSiZeR3yKzI7bbrmK9xpfrCgMArVEFpXD2ZRWex5WOqWJLjl80J1zRprdsznclz2rNiyAZ9eT-RTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKZdX-cPFlALGInFxYQUz1gZzB6EonukSPqx9R6SUlmDf-_WynK-HCy0RnTR9bSG7dxNcGbu1KfcJfsHUeOMfoKLj89icwDNqLDhVubeIIhMT0UKaULtEv7s0BIcx4WEZvp8cXyTe6Pph9dw398-OXUgC62W6Fs_jHnvLZJk4zVOgSrEJeZp_HPlWEJHLC5zpuMWErFvRbD-Vi1_570gGnmNTr3Nv741gsBG9P8nsvSIlpltqakJcBmblDYuQMmPxQn-BITfHYyKoy7eUDH7HZUiqkwS90X_Hnpdo5lzyIznHKw9ceIDpNosvYtKn_e9Jspchhl3GQw8rHQXKB352w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvNoQZ8aDZKNu9z5lP8kYX74ftW35JA75N3Tq-ZgSEzq4roWEXfywZ9JTDTdY18j7D_RvQ5hYqI7I2AZaGJJB_nWPWZoidBpjtYX6Ruk-nriYpfWVxv1mBJ1-UGujNe49uTtRPB3yn-v1E5cFiS6kZSUsAryutzLrqa2tmvx3KPW--z3_6n17KIAXH6-ztrWFYaMkFkHQXo8-MsK03_m-LsizFVDUsjYXzRoPsUzLD7FGEEM6h0qsZhwYRhXgaSTmBgnkhwklci_o3torP_rsAzqwFA6gzRCMkJv7Pa63huN89-eDSzoArrZJ5vgYz9zH3h933m_h0euOVf1549i4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz_zUMoYzw3-p4KmsBt-yvQZ32LcB1v4rr2R3OZjI2U9bgoqK8sUMsspiRlOEVdBco1eneUE6AvUZanNBY66mFviJaPMVwaL97AY2CtVXnxhIjfSku3hkSTar12akQpXPdid5bfe9UjcL2iY8is3qYJVK_VvKqZG-BWXn_xR2hxE6HiBbzJtBbAvbvq-6KogvPAkWKp_GEX2PTr1vpFHfS0OCfcZK6bRubJ9SuZOu8ZxvBwl3FpVOLUpculHO0oBsBmZlY_LOJS_7nJ4Eys2X_6dj--o08FzbT9-TehF8lMIf-dfyCX3gS1CcvLbYKjTLXLTT31SBsJqdvWfn-Dl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJRDzTWZWjJsJ6PqkM4GBglUPIrzHtPNuqvATrO96HUWGM-dwVhyLfOyFoYCxlmd5xSnQV_4D4xjOjMEQOeaOSsfRHlDN907AXk_jVScXiZuXX4XWBleBulKrWayo8ZzHH1FJoYtu1EONa_1WGYs6cHTSq6RRj-yl38kRoev3kb6LHnjuWfjTA-0xUt6EjGD4M5PImx2tFx6VF95KxUjE2fk-K-EO_HVapg5MUJbWznOR8y9hav7eizWMRyL8rI7KwjghcWxUy6CNlYdPbFd5UI6BmBmQCAmvb--D-cG7-49bOXRC9u_YUhsTL5_ggs2RgRuQdTzPFrT_M8LRZKiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=udRgOVIhlivIeWkzEMFiflz1XMMzuWWMqN--QMRIuitdA-AY3TOjLL3E9BYINMGi1MwDRvbVcBlT9_jHqH3kAzqrl-8V8ZsieSm68El38B--DNlkFh1e8Xco_RORDY4IaWDfwt_M_rX8lNhY-lSSpBlqitF0Nql0ebtpwZ9VZltf_pbexEavoKa_R6qpMu2mk95FfVrXcvqD2sEnQ2SAF-l_tm7lxAd3kMNMuMF5q1wG9ttXuif0R9fJ0CAUC5yRyAUzzXbSyTk37o86zAt_qdkBtSK6LDq0TY_W-QrHPFLdoZvAHmXh7lcyhuqebzTBvnDSjeFzERt9w_B-Vdy6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=udRgOVIhlivIeWkzEMFiflz1XMMzuWWMqN--QMRIuitdA-AY3TOjLL3E9BYINMGi1MwDRvbVcBlT9_jHqH3kAzqrl-8V8ZsieSm68El38B--DNlkFh1e8Xco_RORDY4IaWDfwt_M_rX8lNhY-lSSpBlqitF0Nql0ebtpwZ9VZltf_pbexEavoKa_R6qpMu2mk95FfVrXcvqD2sEnQ2SAF-l_tm7lxAd3kMNMuMF5q1wG9ttXuif0R9fJ0CAUC5yRyAUzzXbSyTk37o86zAt_qdkBtSK6LDq0TY_W-QrHPFLdoZvAHmXh7lcyhuqebzTBvnDSjeFzERt9w_B-Vdy6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUe6YVIrFYB0CBDeWMoQ8i624O2aNfk_RKqM8hR_D5YnrB0-upl0Nuhd5HrJDNWhurxQgVQgYCcgmYb4sf6V6_OxcVBF2wE2pBdpi7aYgs3wtOZxmUjkOb-NOYzcLsqbR48TyGRo5OdeQc0IhjPvaG9M1LsRKynKjF2RaJ8wxHysWKipewv4W0eFK6GdaZIHxEIL7H5XW4KKNX9I0Go5R9Evy8F_J7juRNWt3TFHfNEdXZotUrVIWD_eNVzM-WbbAHOmoxowkp3uHC-gf95gifXqWYaZPdEAlUEonC3e-1VzZ5g8yJp0HYkCKMREYAct8HdfBrjtdg1f4s3YNaWIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR1X2oBa_rsmOAbakzcib8p7gDQaFJp1jRHF4nYqCmFGsTWmPSY4MpQwyaapdGJK0wC5x1h4FN0KTFAwfpGAwZI2Ln2Omp8UWYMfsMmHcphCsHr3txpChOuX-O7uBIZGdVfSzHHw4qIAYAaW3RiChP_nzuD9aMhe9kBZ1_mYTqnZMZQGHTIUhnCi3W-zpz-7NbIUMYLjShkMqA1fRCUOpXrFPOiYkgO8ZjOZApfbuPmK6jg6DiM_hvDdRd__KVooakNBcjHc1Ihn-lpsJsB0Wr_z-A1oO8R9yjXjWvK2C_t4NRYpOgkTcL7Y-AE_0KkkLRSktwAnRtrr_kksiPtVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=PhUGi5Gk1mtkAsdlat5gjsmIwwDW7O5sQEzCNFJJwcmGjucAAlM7VMoURVZ5r8U02FfR4TCgxX93cNTkuauoip9N2Y1v-7wSqp1hnz1xwL7gSW1rrw0CzONoeqZuDZWQj8HIsEAEtZDnF9vxtpsvPCp1ljVw3viop2o0KhzERB9oU0M1heBWynRAaQneCOOYGWCrdZsHQdkaWGbD1e3wFsLS9S3vJoDtFUuSvGGOZMoqysIRWDx3QiH80YqeSbLqTDADXHXzNLogYl3GNG4hrBgkT9wy5HG-LSFJsTJbvCnR4GpwccPSzvuNAzOLKO31gA7Hubu9mHup46ltqa2Vqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=PhUGi5Gk1mtkAsdlat5gjsmIwwDW7O5sQEzCNFJJwcmGjucAAlM7VMoURVZ5r8U02FfR4TCgxX93cNTkuauoip9N2Y1v-7wSqp1hnz1xwL7gSW1rrw0CzONoeqZuDZWQj8HIsEAEtZDnF9vxtpsvPCp1ljVw3viop2o0KhzERB9oU0M1heBWynRAaQneCOOYGWCrdZsHQdkaWGbD1e3wFsLS9S3vJoDtFUuSvGGOZMoqysIRWDx3QiH80YqeSbLqTDADXHXzNLogYl3GNG4hrBgkT9wy5HG-LSFJsTJbvCnR4GpwccPSzvuNAzOLKO31gA7Hubu9mHup46ltqa2Vqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKprfLJqOvcfK0o1Bb8eCMH86ACCOLnMcp7hPKZGmhNb6-0QTOYDJrIvYuNkVi4GHRFMcLynCsvi6dUpu7Me3jdLEq1J8v1hCfDTdo6H39tqt1jj6z5WnKh6aae9jMzvOaV1p_fT3ScPNTXl3FI7C4ugONbKVm7MsfjKZHm8cDYKWekMkIfBSkWyULvEzBRghqyIItH5jdmnUkJzoPliMpBNRWwikJt7IuvjgMQJ-VBTWqtBsg6lRz6ccLFM9-iQql46svCeWYdE2IQ_jsAw9A3nZCEnay8C_DXvzQ_wqVgWZBg0M8rw7UFgt2HnaT8Ip4P3CpWNmQu8ljsESxo2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_AGTbphnvYagtBUE-mgOTnW5OOqygUM4-BnO8RZT98xq99vxLcGUrTxWfwIZRCloY5BT6mytaQwlGaBjkJfYDR2K4Ow7iCbKm8N7Q31I11_cNGZtDVjnZBlxPZOtK4faGn1JF7jc99PN6GbIxsDQUhG9GL8NEqm6E_epqmaPPDijNZawIQxKEKXtLdRvh96BlxhwwRK_1b3DKhmlh1GhCKVeUz8q16j5IKcJNraPd7oq4xZ2WNf694K39SHseOmLtiazepYy4eFSm5N76J5POl9ay7vdBpN5rYAAkhY8Uit7IttZKpuuvN7uKZB-1ikrGr72HXVU2FNSzQBvMbh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obH2_e6NBKB2XR6TTViUFi11XVnwuu-OrZxxIHj_gto__ihXK7i0V8ElAr3RsYeHurh-loC_MElxU65G6OePC4Jiu_vM4P7C2bvDFm1ZJnsxe_Cs0h6lLbss-hfH_nYQpwC2JJ78i2nR9YanrN9bCmwbCGX65WqCM4ee4ds2BTA270AjoJRS2QbgdD4ulMjrBxPTTXenw-ODA8bx8OPie7-a1c_XzkyPyiMB3OHSnsW-LcswuYaSmdSgCDo00oVTC9NnAWM4LeLOImmcf1pX-t11gNJp12BxjfrvxSMlyIecnXbMSylR-h-vVwgR05UTWdWhqtkfETFK0oeDAUvP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOgMo_nYz75Kv8lpwqYwBeugnESIZrscDnIeq4Wu8Ke0yol2gENFf6drSkqxu3MxEZgRjQN3lsceIbpfuosvW0wjXA7c1-fXAMo5JRnMxSx_55S2FTxVopf9P-vacwQU0YaHkJhH_yMGfBMEykzBBkA2Sl5ZB6O_cNdepWD0SsFjeUZgu2cCIaLOqFw29aD3ZRd7i90ckYUjkeGnsrWZxZa4hi2xyejF0N-LUxGXwLXgKgf7AsYzwjWziUT89CkLdTTu7bwY1k4D7IoKTmwQqp-Z-pBrfn9dKBtO57yJxGOkHNN_60v_gSX4ERhD9dyvPNCcRmi0tS8R5gVeT4jpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=AEb1PIz7g00QDS0KHjZdQWyOsimEBpUiECgeXZr9NWBZ9JhQeEVnYDliDpk_q22taR9Qkyag9TRfOvjt5PiFod6EkKCP9YfGbh9cbHpCPQGRebQrvDQrPANK4LbpxemIlk9bUprBRU0SxyTk3N2p6w2UCS2QqOmsVHhIPo_Lten0odbtmRhZ-RG9KvQKiReI7OI6aP0EKzDNkSGyMERdM-OleQYTj4NnQXaiVDDuEKKSZeur7a3P39e2LmqmVx9aJlH_o0OSayunjzfAPWeQNviBfP8yspHy2wXAu_9NUSvyToxzoYNxPR8vQHS2i03xR7qmZlh8en1y-5U0-a8DfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=AEb1PIz7g00QDS0KHjZdQWyOsimEBpUiECgeXZr9NWBZ9JhQeEVnYDliDpk_q22taR9Qkyag9TRfOvjt5PiFod6EkKCP9YfGbh9cbHpCPQGRebQrvDQrPANK4LbpxemIlk9bUprBRU0SxyTk3N2p6w2UCS2QqOmsVHhIPo_Lten0odbtmRhZ-RG9KvQKiReI7OI6aP0EKzDNkSGyMERdM-OleQYTj4NnQXaiVDDuEKKSZeur7a3P39e2LmqmVx9aJlH_o0OSayunjzfAPWeQNviBfP8yspHy2wXAu_9NUSvyToxzoYNxPR8vQHS2i03xR7qmZlh8en1y-5U0-a8DfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
