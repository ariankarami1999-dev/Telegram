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
<img src="https://cdn1.telesco.pe/file/mmh9kuUAFwKoTgYbu2H_7LhccO-XxV2OUn_Cy2mEvfAWnx5-MJ0wak-wMRQ3xK8by5iqMLQ-y4V3KGh4hFOf6lBvg2NlloJtJLYSwPx5eXIIhXZ6oWZHVshwnvcAkIQ-WtEqsdzzoJmtU2tCVDwGzWjKRqrfBaPg41iZ7oXDES8Gv4vj-dNa-jqB8ZfC02-d65lFK637DSCtTwOdxwtnRbbiVQCuEtXQPLMZVjYSdqy3AR8dfUqV-GkxAD-UydJfHtOS_R3a0Kqbw3bpAmBRiDoMBFEFup9dsFtBcLDXDB1SksllsgYtkHCY6UkUv3ZOVq0I_Stpdh4m4tKPFNoUGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 18:30:12</div>
<hr>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmSQ_HC9y4TQD2ukSQIiTF80MyWHtysHNDLIWfTM_qnJqehjKukIiJBpZDExIPA8yXgCiV8FOe75bewQemmVFn7qJnHH21TZ9UepUTrrSfnvxOfNsHHVM3gB8sKPufvECKmqqWwR2SXQu0tA-UJEg1ZQiVZwpTqFGOUNruT6hycT1t4stZFbdxAWEQHYnlj0L5OYS65ukYQ54mdhhCI59M_uRo0LteSoW8v56dCJHZlYgY3cIGfsmtsdEPkJYhbxdrBiNLmSUCXqTiDBm5lu6FGA_ueFkdctN3yBQLW7vfpIU7SZw6yrhJtg0jGrZkF-J8H72J8OztGr2lu_uwlorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DD5HNhtOXihGqElCfmMn6POiKqfRGxc1WBBmmX4EkkJBoPyO9NBft33DnfaS0WccNdD7DzfqFNniyx0MDNv77-r9AjSRZUfDKzVXkod21HfQm2jBouCXmLlC_TfMZ1Bh_60D-xF9K_KYVXv4WL9pxdC6sRIcGHLV9ERPTnr73lYFRhcEaPddXct4rCSKEMxM1NJ2C6f1g6zkNMWEr7gn-c8EjpWyKOwkQWXOiwwjnzlfHS8bdz5jww0jksqbDK15rPoOHZtyozFfTawvNq2xmhGtxQOBX-jAeWeDPfr4oqvTyU9vKoWmdqnomYRsunVFZTSbLekrgLycSAcgY2hBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QzEaRuKia2x0yCO00kgo7boy6b2HJfV5lhviCT_S752M0cuXAhzVFy3UfvGcOCkkxUtRRkxok_K33xW9dGgv4EOOxlJRXYxhfvR9V1c9sNQEu0aJIZPqfHBqiKQqvXSrrqyCO8ylPxHd7T7pZProvP60mbeBaMRE6BuGsb5RtQrtNCMxGD8nHRsTxji3s-KZkvE0VINMqWHbibSu1QYChn0llNK7GIriWV7QcS_0iJfQsz9PriDFbE4ffN57n7kEJXtRSMEol56-u_ZvSVSvDSr_k-PKCUatQq8b72rHJ92gJMo_wDIjOwERZnEKJib2d9pOEy1wd-5hVP9UIXORwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d5-Oogo-fj4O8hBQ1u921uKvBxfSuX_qZ72yGN90R1vI-UTpgdw8FD_7Ats32StBNiroHCEb_5-1uVJQzM23-duFI8Arq5yBpZ_ymT2EKzHuRUv2mBxSxBQE07NhhUY5cq57xfwNFZSPG8v3IKDp9H1j7yOtm9wJs2MVwSZvn5PdxYGz09L3OHe3Gi2KVNh5xxsbQJFcyOCE4UTgoJm_6PV6X-xqYbHr9C6n4iS2Q0CqhyBIF98bn-cDXpXfb28IqNM3uqZ80qRVDVKxPdWWgwgVl6e-JeueJ0T_11gaC6yeugYf-OGwxBivNXQ8Eo5mqRZAIecgja0mZ927j97a2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=CZLOIgfOBZ-qplxAqbc8z_9wYdHAxF-jYRNhHUG9JTG9X6M_Pf8zuRaq5y3IjkmR83EG5RxLr2R4bPsCZRXMtGd2xti37UCMbuv_Z-24PGU4tllv1OcfWpTPVChMDHuYRYRcak0DBXwXg8kg-7rErxqwLjwJIAKZedC7Mi9FrDcZyv8nuEi3aYITuGB1t5Vv8hoUzzRXKnmrwQTocdn6qmtX-lmwUKwvQYT3D-oPGx3JA6b_Oi11NSVG6ThLsOlD4-0XXUBA59GxmdIjjvvgNH__r9j7xtp7tAkH6SyskztLF3C2NRefhy0TA_uZludg7J6ZdADA7sDdJaw--BMQhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=CZLOIgfOBZ-qplxAqbc8z_9wYdHAxF-jYRNhHUG9JTG9X6M_Pf8zuRaq5y3IjkmR83EG5RxLr2R4bPsCZRXMtGd2xti37UCMbuv_Z-24PGU4tllv1OcfWpTPVChMDHuYRYRcak0DBXwXg8kg-7rErxqwLjwJIAKZedC7Mi9FrDcZyv8nuEi3aYITuGB1t5Vv8hoUzzRXKnmrwQTocdn6qmtX-lmwUKwvQYT3D-oPGx3JA6b_Oi11NSVG6ThLsOlD4-0XXUBA59GxmdIjjvvgNH__r9j7xtp7tAkH6SyskztLF3C2NRefhy0TA_uZludg7J6ZdADA7sDdJaw--BMQhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز جمعه ۲۵ اردیبهشت در مسیر بازگشت از چین در پاسخ به خبرنگاران، درباره آخرین پیشنهاد ایران در مذاکرات هسته‌ای گفت که آن را «از همان جمله اول» رد کرده است.
او با بیان اینکه محتوای ابتدایی این پیشنهاد «غیرقابل قبول» بوده، افزود: «حتی ادامه آن را هم نخواندم.» ترامپ تأکید کرد که صرف تعیین بازه زمانی مانند ۲۰ سال کافی نیست و آنچه اهمیت دارد، ارائه تضمین‌های واقعی و قابل اجرا از سوی ایران است.
رئیس‌جمهوری آمریکا همچنین تصریح کرد که، هرگونه توافق باید شامل انتقال کامل مواد و سوخت هسته‌ای از ایران باشد و افزود که توافقی مبتنی بر «حرف‌های توخالی» قابل پذیرش نخواهد بود.
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره پیشنهاد اخیر جمهوری اسلامی گفت این پیشنهاد را بررسی کرده، اما به گفته او، اگر از جمله نخست یک متن خوشش نیاید، بقیه آن را کنار می‌گذارد.
ترامپ در پاسخ به این پرسش که جمله نخست چه بوده است، آن را «غیرقابل قبول» توصیف کرد و گفت مسئله اصلی از نگاه او این است که ایران نباید «هیچ شکل» از برنامه هسته‌ای داشته باشد.
در ادامه، خبرنگار از ترامپ پرسید آیا دوره ۲۰ ساله برای او کافی نیست. ترامپ پاسخ داد که «۲۰ سال کافی است»، اما به گفته او، سطح تضمین‌هایی که جمهوری اسلامی ارائه می‌دهد اهمیت دارد.
ترامپ گفت که اگر قرار است توافقی ۲۰ ساله مطرح باشد، باید «۲۰ سال واقعی» باشد و نباید به گفته او، توافقی مبهم یا ظاهری باشد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز جمعه ۲۵ اردیبهشت و در زمان بازگشت از چین به آمریکا در هواپیمای ایرفورس وان به خبرنگاران گفت با وجود آنکه نیروهای مسلح ایران در جنگ نابود شده‌اند، ممکن است نیاز به «یک پاکسازی کوچک» وجود داشته باشد.
ترامپ ساعاتی پیش در گفتگویی با فاکس‌نیوز هم گفته بود که نیروهای مسلح جمهوری اسلامی در چهار هفته گذشته، تلاش کرده‌اند تا تعدادی از پرتابگرهای موشکی را از زیر خاک بیرون بکشند و جای بعضی تجهیزات را عوض کنند، با این حال «آمریکا قادر است در دو روز همه این‌ها را نابود کند.»
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره اینکه آیا شی جین‌پینگ، رئیس‌جمهوری چین، تعهدی قاطع برای فشار بر جمهوری اسلامی به منظور بازگشایی تنگه هرمز داده است، گفت از کسی «درخواست لطف» نمی‌کند.
ترامپ گفت: «من درخواست هیچ لطفی نمی‌کنم، چون وقتی درخواست لطف می‌کنید، باید در مقابل لطفی انجام دهید.» او افزود که آمریکا به چنین کمکی نیاز ندارد.
رئیس‌جمهوری آمریکا در ادامه گفت نیروهای مسلح طرف مقابل «اساسا از بین رفته‌اند» و ممکن است به گفته او «کمی کار پاکسازی» لازم باشد. او همچنین به آتش‌بس اشاره کرد و گفت این آتش‌بس به درخواست کشورهای دیگر انجام شد.
ترامپ گفت شخصا چندان موافق آتش‌بس نبوده، اما آن را به عنوان لطفی به پاکستان پذیرفته است. او از مقام‌های پاکستانی، از جمله نخست‌وزیر و فیلدمارشال این کشور، با تعبیر «افرادی فوق‌العاده» یاد کرد.
@
VahidOOnLine
دونالد ترامپ گفت آمریکا ممکن است در مقطعی برای حذف آنچه «گرد و غبار هسته‌ای» نامید وارد ایران شود. ترامپ در مسیر بازگشت به آمریکا و در هواپیمای ریاست‌جمهوری، ایر فورس وان، به خبرنگاران گفت: «در زمان مناسب، یا وارد می‌شویم یا آن را به دست می‌آوریم. فکر می‌کنم احتمالا آن را به دست می‌آوریم، اما اگر به دست نیاوریم، وارد خواهیم شد.»
او افزود: «فکر می‌کنم آنها کاملا شکست خواهند خورد و ما هیچ خطری نخواهیم داشت. ما تجهیزات لازم برای خارج کردن آن را داریم، هیچ‌کس دیگر ندارد؛ شاید چین چنین تجهیزاتی داشته باشد.»
ترامپ پیش‌تر نیز در ماه مارس در کاخ سفید درباره ذخایر اورانیوم غنی‌شده جمهوری اسلامی هشدار مشابهی داده و گفته بود: «یا آن را از آنها پس می‌گیریم یا آن را برمی‌داریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED-cAblv5b59zhD71wWdTNKSYFj9tJ_YG6LOr4hHm77ZyMET8urJipAme77oBBQoLdaJH-BVdwW8dDLSAlkHl4IB-e2FLZuv8mU_Ow_i1J_2jOkOAmMp6LbupYp__Bw_z5SJ-SWsGnRN3dg0l4ICXStnQXJSiGo74Kc87GevTvcSyRM9VVIbD9Q-OBXNjM0di1w5Ro-OpMMMyO0_1ALY3ewl64wq8fyAku7UPxp3C4vUrOHdAmn0n2665KUQBuW46avY3MHZbR5ENIB2RLaKuUvQqkwGimQLN8vvxNaqFved9BcNu8NPt8qyCjeazaIjkUlyRtv-PMzxY1z-3hlamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Km9FZedA1YxWD3oU_JcoJEs_AbChs2q45MUuB3C-_nDnfVyntrhT02bTxSfTZh_d-poGmy31mbw3T2RvvxVhLgSQSmL7Z1hppke4RpiJRVc8rNMJhwoLvx4r6nJF--Q5SV7lwenVa-YHKz5cRrG13myWxRBVjCJhCzAMGAM2oDbRr2o4hqKDBBTnJtItqEl2_LwmaAVsb-dq3_dgsUI_MNiVQGFhjrhxgdX9BrBRX95bcwctNVbCMkB335PfSca-cLKUWKuv8HQpsS2o3rbNZ6hlr5SsoRTkKeZuND6sT4ox-HH4pBByJZK1ADfJkP_jge0aOoGsHDN6EbyxACQJIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GLxtBS4aHnKG385SLIziDy9YoznGiMQgZurjkBwXhkGIb5-92NKAaggFRdTA_iLsW3VyfXbOYys3Popvi77vKVWGm0kKw_NHZWJ2Dxs5n5OBggDRiztdRqsGzjfz1icKuwZRSMMHCp0IMfChtO-lRif_NPiIioFR-4olo8qtUrPoLchUSwgboKKFAj9BYtq9Xy6bgqbDdr0LwET9dBu_-vHWmj6-_1R-LBbgMq4ojSsps0FPo9DQ18MUz4LOlvZnmsdtW0AM4aGwS0ajNu379ycpGrhSeEy_RGn93-uQA34UKwYdrHUqovMSMaDeoR5kQo0_TuLDHXyfSBftev_eFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SjZ96RlAB8F0CmtujUaOZGSov8Lakpx_ZKruHsO7euWvQ0N5nIeoBWENgyxZkcl-bMe8I4ubzcSirsK-28-HsrxRaL_KLueHUwuRWldJfVR4kb5unI6OEKtBO0xuWdKD3uRD3A5aFPHnY3U5R01zJ0dcHb2TAiYA1a2Pi-Nphw1A3QRpNzvd263Clz4frRebndvsPK5QxRnLprqZDsgeNuY7N59X8xKSam4bhH62Tmewy5jRTpji2mZJX9BWnU3Vciwn0rirSX95JLai4Z1KkFfsBbiEVfQPPVovala0qpjbEzOp2gwutkF3eof_4G09sMqFieFTMMlvQ40Hd-iHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oRnSff_9Z9xQX2_abK6MZC10EjK_2kg7AGudiccmYJT5skYhK2j1KZNAVPlr4KHNkwSW1jlvwUz0zHHYnkXkW7oqnSkRp8bC_N4GSYhQX42WOgMuzNsrI5j1ES78_WYpdQgQYOtPNUC9X44a-7IfrXk5IbqpPVgVcYI1ghQjXNIkvvB8qvukw5cXnntkBRIIz4vZqp--ip5ufnc7obZnoX9y-ZjsYpqep-VghJhwzcKBziuWqZFjC1-9gTmSH5vomqAxP75i-AwNBtdutSU5QCn-RZHPk6bkcfozZ4GC734N6INmihmx5OD6TVkuzH5cD1FX9BpcSH6pUoW51cfXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U_SQNILbcsQFmbplqumjzHJ24ZGKh3kZZm0pwNxO7yZXvGRC0PNkBufMEU9b1nfr1U3WuyA_yg4KoFFu9bMy69olDfrosAcc369JJ9ThdTQIFeoJhlLnhjbEDFeKhyYLwdhCggIW5sGtdPbEx6r84zBisMT4ZHdh_SkvtsqAnK5ACzMGcy-oxR30Y5qGeODwrxZ3D1Jk1xtys2zaEeHEvDiABnts13QtAY_CNz6cePfNO8p9tOmx6NpGjZpBkYWlgEy1DNWrOZA07ia4VpvdtlH5D5NNGo-ZVeINqF-H0oIaeuYgxynB7dhpULF-hTGAqiYKNsnpFSHYSIb4rcR2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HRJHBF8y4gIRYFroA_F7MpjRS_02SPtuIDSLxmaxBmnGJ27DwRqzcG6DBpLASAamd0NjQ54a3W2wPxKdjK2uTkPoJps07m1NtchTFpBPDF-eUz1tzVPlMPN7JqPzG1-slbxmvmhiUz7nHF7WBSLS6_BYRbNR2Q-y06wlWuB4qiAepYI36wxOvUO3LtLEAKUY3VXfHHCwpSyIJbvfFgGte9GonhOnBC9pO_ZlkymVPFgdFDai0Pyb6BWa1krVwaZ8Lm4XiSWGELcwO-InkkKEXyne_KbmRHRLTB4lNORduYLoY9zVzR2mZ49Qb8XK3Er7uL_XFYMPjDx-tr6iFyj68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cFg8LhlrttW8RdE67ypB98ZuPNdAv3AdxmW4VcyZRXRsLlPYnuTg-PO9K94IRljvEJCYQvgNTp208wHS0j3IjMBV6cGUKGjXJm9luJPfJbUgCM9880Nq4tq24fySs5LLF4MNHe97cCwXqpC-h7bJCWw_RoqkZT9qk3n28QP3Hd9-GWXbrj-piLmfIWd5ntWWPgMplarh7u6wm8Rov8yVXLOF1qd6My_XqihGl3R9Vq_nUpU4pVo4kgTWQr3WJZkPWdS9TVmK2SZGuwxgPFeywH7-z9Okqc1a1U2i0W-7dGGTPR2bWwd5aGIu8wPM4pgcC0eZzgXvjmlIAiFMWnmAEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در مصاحبه‌ای که با فاکس نیوز انجام داد گفت او درباره ایران با چین صحبت کرده است.
ترامپ افزود فکر نمی‌کند که چین هم خواهان این باشد که جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند.
او گفت جمهوری اسلامی می‌تواند یا «توافق کند و یا «نابود» شود. رئیس جمهوری آمریکا گفت نمی‌خواهد چنین کاری کند اما آمریکا قوی‌ترین ارتش جهان را دارد.
ترامپ گفت ما در جمهوری اسلامی با «رده سوم» رهبرانش طرف هستیم. او گفت رده اول و دوم رهبری نابود شدند و فکر می‌کند رده سوم از رده اول و دوم «که دیگر با ما نیستند» «منطقی‌تر» و از لحاظی «باهوش‌تر» هستند.
او این تغییر را به‌نوعی با یک «تغییر رژیم» مقایسه کرد.
ترامپ با اشاره به اینکه جمهوری اسلامی «پنج روز» زمان صرف کرد تا به پیشنهاد آمریکا که «یک ساعت» هم زمان نمی‌برد پاسخ دهد، افزود جمهوری اسلامی در داخل خود «آشوب فراوان» دارد و «چیزی به جز آشوب» ندارند.
ترامپ در مورد حمایت چین از جمهوری اسلامی گفت که رئيس جمهوری چین، شی جین‌پینگ قویا گفت که به جمهوری اسلامی سلاح نخواهد داد.
...
او افزود «امیدوارم» جمهوری اسلامی این مصاحبه را ببیند چرا که آمریکا می‌تواند به سرعت همه تسلیحاتی که آن‌ها در طول آتش‌بس ممکن است به آن‌ها دست یافته باشند به سرعت نابود ‌کند. ترامپ گفت «ما دقیقا می‌دانیم چه کاری می‌کنند...و هر کاری که در چهار هفته گذشته انجام داده‌اند ما آن‌ها را در یک روز از بین می‌بریم.»
رئیس جمهوری آمریکا گفت جنگ را می‌توانست «چند هفته بیشتر» ادامه دهد و ماجرا تمام می‌شد اما به درخواست چند کشور آن را متوقف کرد. ترامپ گفت جمهوری اسلامی دو گزینه دارد: «یا توافق کند و یا نابود شود.»
ترامپ همچنین درباره خارج کردن اورانیوم غنی‌شده از ایران گفت این کار را بیشتر برای «روابط عمومی» انجام خواهد داد و او احساس بهتری خواهد داشت که آن مواد از ایران خارج شود.
رئیس جمهوری آمریکا افزود «به‌دست آوردنش پروژه بزرگی است، واقعاً پروژه بزرگی است.»
او گفت: «اوایل به انجام این کار فکر می‌کردیم، اما زمان می‌برد؛ حدود یک هفته و نیم طول می‌کشید، و این مدت زیادی است که در قلمرو دشمن باشید.»
دونالد ترامپ توضیح داد که «باید این حجم عظیم گرانیت را جابه‌جا کنید. می‌دانید، آنجا گرانیت است. گرانیت سخت‌ترین سنگ است. واقعاً شگفت‌انگیز است، چون بمب‌هایی که استفاده کردیم فوق‌العاده قدرتمند بودند. و یادتان نرود که علاوه بر آن، با موشک‌های تاماهاوک هم آنجا را زدیم.»
او گفت فکر نمی‌کند خارج کردن آن مواد از ایران «لازم باشد، مگر از نظر روابط عمومی. به نظرم برای رسانه‌های جعلی مهم است که ما آن را به‌دست بیاوریم. من همان کسی بودم که گفتم آن را به‌دست خواهیم آورد، و به‌دستش هم می‌آوریم. حواسمان به آن هست.»
ترامپ اشاره کرد که با «نیروی فضایی» آمریکا که ابتکار او بود همه تحرکات در اطراف سایت‌های هسته‌ای در ایران زیر نظر آمریکا است.
او گفت «من ترجیح می‌دهم آن را به‌دست بیاوریم، اما مراقبش هستیم. دقیقاً می‌دانیم آنجا چه اتفاقی می‌افتد. چند روز پیش مردی تلاش کرد وارد آن گذرگاه شود. دیدیم دری کاملاً متلاشی شده بود. و ما از همه‌چیز خبر داریم. اگر هرگز حرکتی انجام دهند، و این را هم به آن‌ها گفته‌ام، اگر نیرویی بفرستند و ببینم کسی تلاش می‌کند، تنها کاری که می‌کنیم این است که با چند بمب دیگر آنجا را می‌زنیم و کار تمام می‌شود. آن‌ها چنین کاری نخواهند کرد.»
ترامپ گفت: «به آن‌ها گفتم ما در آن محل، در آن سه سایت، ۲۴ ساعته ۹ دوربین داریم. دقیقاً می‌دانیم چه می‌گذرد. هیچ‌کس حتی به آن نزدیک هم نشده است. در ابتدا بررسی کردند و گفتند هیچ راهی وجود ندارد که کسی بتواند به آن غبار هسته‌ای برسد. اما با این حال، من ترجیح می‌دهم آن را داشته باشیم. ترجیح می‌دهم به‌دستش بیاوریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aLPBrhPsHRf7tmnJqo2pJ_GUYDElB9T_sENaSh_K4Al9IF06PV_-jDCWtbQO5boGr6W6vqyuMavTLMejFDioIwTXYnb9FqV9Z4mLOVkulYqe26aLqYD98OH0X2nqA-jcw9TfuTtijeV-iJ12XsfvKGxSkp1TpG0R7aLuqqAqnedPgaiQFN-TBUeOImlUWELX9LCZNQLyrR3sXwNQwI27deIlpCGE0b71htmu-bor0TvXH7QN7Bp7v5-Lhf26UIJKncKkUnIuhNr_1KQsQfC9WgJgnM1m0qnqz67PhIzkXCKjcEQMhMcjqoE9HPL97qbLCM_I20C2ZDe2vb1UMyup6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SITPFakuq-8KNY-QWVN5rvrUcKv4UKPZEUInikdfOgjCZs1PPqfS9TqWfMZWGfclgtltXqp2QSlwQWm1dSJF001h6N49ZBzX6iAG5jSCL92wBJf1YDaRhAFzJx957SAfj-kULD9pSPt5MCcLCPUKWXO1Q5QSUo_0jbzmX4RUXbGw8GSUq8FRATkG4pcrkzKGXYyX3RKMU_Trc3yVw3XpIcn8q4EjX-MUWddYisPS5UWNltgN_WqGSzpQHeLxL_0bvdfxYtctwV-fbFzaSQJBWoHn7xBqzDRTDMJnz09pVrCmY80Y9K8CZcgI6Nstl82MboOOvUDE5vZLhT0hipiW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyRMGx0H20hLaxzdYKMs4EyqF9I7efim8vZaYmGvuU4NEPYrePaQXvfY-WJ83Wa_YH2zR12Ar_9lGZi1GKD_b18o-k1pFND6H5FzLG5x3CeIQf2Vc0BohvsHQnbTYe8M7-yGVXHN9CY2Bo9llNY4kiAf7jcvFs5qQ5tqq_nuaIJzZwhaYLo04wrbk-7e6n8V7lpWumTdbXPKI-Iq_-mXdoJalsYS3TdfcyBFm82ILInPtV6IMor0e6Ddqk2eBUmFZ71sX7qY6gwj5SI3ZiE1ub0OOd0cWuEucLlfRgz74jPO2xX9e9aolKF9ubptwRWqdTHyvTg2JLOxymmTnysXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، اعلام کرد که صنایع موشکی، پهپادی و دریایی ایران «۹۰ درصد تضعیف شده‌اند.»
او در یک جلسه استماع در سنای آمریکا گفت: «تهدید ایران به‌طور قابل‌توجهی تضعیف شده و این کشور دیگر مانند گذشته، در هیچ حوزه‌ای، قادر به تهدید شرکای منطقه‌ای یا ایالات متحده نیست. آنها به‌شدت تضعیف شده‌اند.»
کوپر اشاره کرد که نیروهای نیابتی مسلح ایران در ۳۰ ماه پیش از جنگ اخیر، بیش از ۳۵۰ حمله علیه نیروها و دیپلمات‌های آمریکایی انجام داده بودند؛ به‌طور میانگین هر سه روز یک حمله، که در نتیجه آن چهار سرباز آمریکایی کشته شدند.
برد کوپر با دفاع از جنگ اخیر  تأکید کرد: «امروز حماس، حزب‌الله و حوثی‌ها همگی از تأمین تسلیحات و حمایت ایران قطع شده‌اند. این نتیجه از پیش تضمین‌شده نبود.»
او همچنین گفت نیروهای آمریکایی دیگر برای سرنگون کردن پهپادهای ایرانی از مهمات پیشرفته و گران‌قیمت استفاده نمی‌کنند.
ذخایر سامانه‌های دفاعی پرهزینه برای مقابله با پهپادهای ایرانی در طول جنگ خبرساز شده بود، اما فرمانده سنتکام اعلام کرد ارتش آمریکا اکنون از مهمات ارزان‌تر استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlSN1GLClTczQ129KCbfizdg4JN_N_94GEbBf7weSSABv8p4E0hKyUIrtVr79oFoFkZ56550OUkJZnUrmgdduM3ijLWHa0SUQLNfe3T7hC3YADNbPFzh-iUbXt0hS6c-aCvheVZ7YfVfvNb93Zbe_v4n1jJ0oPTGTrZe061v0qx6usPqZ40djKjWgLGNVLb3zkO62IJ_4K5VnZaEMjEudF-xrkXywg8rjxy4m2nA0likrwr7IXYhFEnejI4aS1iMqIR7EwZG8Divw0pLl2oEYSOjtjUpfL-9jXsxGUOPV5kREL31ZyPlfPlpF8A_03UxFri0beHUWJFY2cDTr2a-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0UD6cVDZaPYdikjXKwZdwD3szb4hZbBTOq_lbtEq1O1cj0g2fcfInVB29seF-xIA6zDPm0_7_i-gBVuaH9QAmzpcWcjpU4MZh7S1FzzxLzXnEHvMYy8pdvwIBKEHRZOqyuZaMSpS8Fmleg5b0h7BLNEk3jPi3W8NBBS6kEL_KOOctCgixH3LfLzW_Nvrzx0wOzj62hKC73rSOvDUi8Ua87tWGWo_tN3tlPadGCLSpC2ngX_vHPJhFVoq5LG80Vro9nraGf6FZFBn7R2UZcejFjavGE35879bgB4E2g6iFMXRu5Njx9uGZ8DljKvf2SyOqzG6xH_8ZkYKBJVYnrO1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 199K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDibiMLSAkD_Yai3GILaI6BUs_hjob6mcuMbmHgykNOsXuDoxTfZBrONDSxsMOdN8Gmd1pk0FsYogd-01pSKvMUmA7zsLX1peE5dL5oini3cWf7_Z-EzajgXS0gKpwV4DE6GTjO1XGmWDRnzoOe4AcNf9yzsBmS1gPh4bSytQWYiNDBwnDSkBiCayjiQfVHnV7hXrm-EdcbUuyOn9duGCNKbBHyjN2bca1P3x_BYEB4_Ms9J-M1nUQrAzfVI8mqhQMdXB2IT-DnwE0ZMqTHPfPLLHcesosv_Vsk_ft8mAfP6Zhgx6nazYqN_SBUxof3QztuKWBniXAiET71QfFu2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2cahrKjDuYvfq-8AiZX6Gsmk_eRm1Q5Ukh0Sm23_U6Nr0_PC1pK_-rtR-rKrtAZiCT6Nmy3PLd16WUJ5dH8LxR-1aw7pX-RrFl6uUEWOtEnubMtnAR1t_5aKqUF1hMnxRn7kgze_nl7BJNIl8SupIkuLun1gHT5crdgou88xodc0zE06qZSabCfX6bnSWT4X26z_bqDcX2wM_FIUbgMOA4_-Q1lASWUdFa0SDhYQ8TMwhqczfdiVkybVuUg0UoMexANc_mcVJdmrstKoZY4NhrLClXX9axtCIvS1hWBL70LRUHKe6M-ODHdHFFMJK8adF6g7FMz_47n3l_q_REtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwh5eegNHnAo00d5wolDVg7YtK420hansbwvgkKVIyWTAvh3sL_nbZGBE5ewuv6ovf3K01fjtgdkUxjJAw_j-5yJf9Q7JzX5MhVGLiekpbBcCtN_vb2YlSiVjJNFH-3BcZlBKT2O5AK65v13dM8pQDE0zEZ1ia__lMUxb31iFClWRhf6SIt4iwDOD4IHsRQLbKKyVj3tzvrozK09ZVynQ0HEYA4zhxiJCcpZQ6igxPuQPCMKHxfyhIfx-7dRlFdWwl9VWQbUVWd1aJKuExmMi0ufmcqYmLZBtln-Phn_W2Ijy9UVozCtWrD5hKgg7x7DsbJUhrEg27HAN5f_Xh-qDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران می‌گویند وزیر خارجه جمهوری اسلامی در نشست بریکس در دهلی‌نو، امارات متحده عربی را به «دخالت مستقیم» در عملیات نظامی علیه کشورش متهم کرد.
این تنش یک روز پس از آن رخ داد که امارات ادعای بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مبنی بر سفر به این کشور حاشیه خلیج فارس در جریان جنگ ایران را رد کرد.
خبرگزاری مهر به نقل از عراقچی نوشت: «من به خاطر حفظ وحدت، در سخنرانی‌ام در بریکس نامی از امارات نبردم. اما حقیقت این است که امارات مستقیماً در تجاوز علیه کشور من دخیل بود. وقتی حملات آغاز شد، آن‌ها حتی آن را محکوم هم نکردند.»
رسانه‌های ایرانی مشخص نکردند که نماینده امارات چه اظهاراتی در این نشست مطرح کرده بود.
بر اساس این گزارش‌ها، عراقچی همچنین گفت که «نه پایگاه‌های آمریکا و نه اتحاد با اسرائیل برای امارات امنیت به همراه نیاورده و این کشور باید در سیاست خود نسبت به ایران تجدیدنظر کند».
عراقچی پیش‌ از این نیز گفته بود: «کسانی که با اسرائیل برای ایجاد تفرقه همکاری می‌کنند، پاسخگو خواهند شد.»
رسانه‌های ایرانی همچنین درباره اینکه آیا شرکت‌کنندگان نشست وزیران خارجه بریکس در هند خواهند توانست بیانیه نهایی مشترکی صادر کنند یا نه، ابراز تردید کرده‌اند؛ زیرا اختلافات میان ایران و امارات ادامه دارد.
در همین رابطه از کاظم غریب‌آبادی، معاون وزیر خارجه ایران، نقل شده که به دلیل حضور امارات در این نشست، «مشکلات و رایزنی‌هایی» وجود داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlHgrBB6ATkjaNqvhsnHHuAjEUqfJkw0fJCNx0nVCf-Ma-wLSpLnlWJA8VCvesB3pFJjpMAseFogpRS8OLSci3LsNUyC_6LGLAXZtKDRBBqGipjlG2mqd_XVu-hwv7cnvXCRoJrkhrZapSepSadVO6YDxkc33vkzPdpCXeSvfTSc9p53WdusQZFvzfBewwgJ8ryO_zHe4laHtJqoVxUsIJSovOB3Z7sC28Kr6l8WPGPN8Bfkq8goO1PlmtHu5ifeWwElht5y9s2fRcGkxNz5pyM9Nwx9ozGrP22dfEC-ZCFi_7MmHceaP9n0N1bL6gs3_CbSSJPMoiqQRohqL-ZGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz-u2QFBsl2ciMKWq8lVSu3igkUNR_BTjtS18zt_8LbKwJc0wN0TnXdV6iO8Agi01l4LJhrJp3Kitd8i3vdSIy_m41nEnlm2YqwE7WyLATaCptTOC5QHepjUBU02Ex55VuSrcQMFRGyBHeiaTGD4N3E1WSrzoEQ_qrgcA9Pwxc1scv6WgnE56VbeNgk0nEENJN2vzRWr-X4aA3oQt0Au3v-Pztx5C30o10ZId3Xoj1XG9t1Fv7SamjbzcMKVXp93cSqEj_g4JfSWL49Y8EDkeqQF33_ai5-HH7G6DndlTUvXcQs5YT0VXPDoWnbBN9-RjMc4mIx8m0-eJwTaEQS3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا روز پنجشنبه ۲۴ اردیبهشت اعلام کرد پس از وقوع حادثه‌ای دریایی در شمال شرقی امارات متحده عربی، «افراد غیرمجاز» کنترل یک کشتی در لنگرگاه را به دست گرفته‌اند و این کشتی اکنون به سوی آب‌های سرزمینی ایران در حرکت است.
این نهاد گفت گزارشی دربارهٔ حادثه دریایی در ۳۸ مایل دریایی (حدود ۷۰ کیلومتری) شمال شرقی بندر فجیره امارات متحده عربی دریافت کرده و پس از آن، کشتی به تصرف درآمده و مسیر آن به سوی آب‌های سرزمینی ایران تغییر داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/VahidOnline/75461" target="_blank">📅 18:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frZ9VdvfSE3c6-w3JhRU7LdBtpKqVpJm9ov6z34YHvUulOV5G1CYDDWGzk8CRjlxsZfo6Z7YDJCbl-Hme0UAAuLomSPaTpu4Ij0mpdzcR15d7BsLY9J2OV5tVJreXmhkUuWFUXAhKtVehscfwCtczTiPEyXNii6RFLhFLZij11IH4rRWQt2x3xZWycLa3ByFMNrbX5Zdhu2l6qg6cA2rKItDVUXPbnXeiAK0usA_MjftWGlNwTOlgDk-o0YySJ_ZNIrcr8Td2FWEwhYKCwZ6b-kAPVBVGu4kmujpOW-S6XYC2ZVqK8LtIOCbIvbDu8u2ZOPPNV4Dd5ZDmFubyuC4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید اعلام کرد که دونالد ترامپ و شی جین‌پینگ، در پکن توافق کردند که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
آمریکا این گفت‌وگوی دو ساعته را «خوب» توصیف کرده و می‌گوید که دو رهبر در حال تلاش برای تقویت همکاری‌های اقتصادی هستند.
در بیانیه کاخ سفید، رئیس‌جمهور شی همچنین «علاقه‌مندی خود را» برای خرید بیشتر نفت آمریکا ابراز کرد تا وابستگی چین به تنگه هرمز را کاهش دهد.
همچنین گفته شد که مدیران برخی از بزرگ‌ترین شرکت‌های آمریکایی هم در بخشی از این دیدار حضور داشتند.
آن‌ها همچنین درباره اهمیت پایان دادن به ورود مواد اولیه برای ساخت ماده مخدر فنتانیل به آمریکا هم صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/75460" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEy71zCbfO8b3TKeVKOgLaUuhzQzQijuK0PirBsLZdqbI6J3yuGdDHIaDw6-tuq3y4PkykGor-jAxljGHOSmGHzUaXM5i6KzW_qw_rb451CAIAKwn1A-evgPZ2TMC0xshj_LPLihlebOq9q_i3-ZnJlPLAbF5fEXbcJomuBC9HyzmFJFvtixmY4w-fKI5iXV_4X39eYJRWt47W8wpPUEWnWm4qFiNr1mOxsAnt9H9dXOZSFAmBeY84ED0V6gUbqK74Sbhs_ik4bZvkH4t6f1F7c4FICd_ySF6EyJHG24IOOwnEBcMHsdxP1dwas-QjHSHG62fwQTbVDiw4TznDkpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید به نفع چین است که حکومت ایران را برای باز کردن تنگه هرمز تحت فشار بگذارد.
براساس گزارشی که فاکس‌نیوز از اظهارات روبیو در راه سفر به چین پخش کرد، او گفت: «ما این استدلال را با چینی‌ها مطرح کرده‌ایم و امیدوارم قانع‌کننده باشد. آن‌ها اواخر این هفته در سازمان ملل فرصت خواهند داشت دربارهٔ این موضوع اقدامی انجام دهند؛ زمانی که قطعنامه‌ای برای محکوم کردن اقدامات ایران در ارتباط با تنگه‌ها مطرح می‌شود.»
روبیو گفت حکومت ایران در حال ایجاد ظرفیتی بوده که بتواند با «انبوهی از موشک‌ها و پهپادها» سامانه‌های دفاعی کشورهای منطقه را از کار بیندازد و هرگونه حملهٔ احتمالی به برنامه هسته‌ای خود را با تهدید به وارد کردن خسارت گسترده به کشورهای خلیج فارس پاسخ دهد.
مارکو روبیو همچنین با اشاره به بحران تنگه هرمز، گفت این وضعیت بیش از هر کشور دیگری به زیان چین است و پکن باید ایران را برای عقب‌نشینی از اقداماتش تحت فشار بگذارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/VahidOnline/75459" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E5XNsW6v_MbJtrXLTuKXOjDPC5-iFyTA30s_SVh7n07d5p-KIrNI6qA5csB35nTfS-HkdjrYnC940tf6BpQ2VB1leqw7Gi1-7GCkhq9-5TSRWfhky-PH4kjYE5wumyTQASK0WfBMA4B1lcjmYj7y5O7dn7FKNMGd4gVJopNdNwmGUIHK8PFM43g-vKFFV0BDqwajI7ssdiiHQewLnGky0tkAq_6ZFNl8yxlm4E1y6QfA_SMOU7yhQnkTakq33Qi6lO9Y_li8kM26m5-W0tlg0QFGhXHZHQeq-q7TmO_R7v1jdhOe8qfOVgYcET3q73XyE-6YBPjAeP0B4nlZqj_1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CMvB5Y4xhbL2fL2K_cZSmsMlS_yOML1HXVxln5VjllldA1SuTVB2uRI0vA3Y7djSWF9r9DilDA6vTXdO3FqxVLYASD5LtgGz3kK8P9vijH7zDh337Y6DAr6H3TywBl1FcNr-j9LZz6cim9N4akdyRNdFjfyCOi7rTuRGE4owOgOOrmnFnSZrNBbBvbXDC83pzwDa0CbWwW81dYUj7rh7f94E70gvRHt8dO7n27hvqHBSB_767BOLqdD0A4lpOvENBdIOoy86rE2Dgq4HpFfVa4w08RN6I5SkEH-r2UGo5G1S5_VQNJj8xZWFGbVfpJA69sEOACKzL2t4MKLYLH1rsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد بین‌المللی پایش اینترنت، نوشت که پس از بیش از ۱۸۰۰ ساعت قطعی اینترنت در ایران، نظامی طبقاتی توسط جمهوری اسلامی برای دسترسی ایجاد شده است.
😋
💩
همزمان مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر مسعود پزشکیان، ادعا کرده است که اگر همه‌پرسی برگزار شود، مردم در شرایط جنگی، امنیت را به سهولت دسترسی به اینترنت ترجیح خواهند داد.
@
VahidHeadline
روزنامه اعتماد گزارش داد که نخستین نشست «ستاد ویژه ساماندهی و راهبری فضای مجازی» هفته آینده به ریاست محمدرضا عارف برگزار خواهد شد.
هدف اصلی این ستاد، فراهم کردن زمینه‌های لازم برای رفع محدودیت‌های فضای مجازی است تا حداکثر تا میانه خردادماه، امکان اتصال مجدد شهروندان به اینترنت بین‌المللی فراهم شود.
عارف در این مسیر قصد دارد از ظرفیت نخبگان و اساتید برجسته ارتباطات نظیر هادی خانیکی و علی ربیعی [
🤨
] استفاده کرده و میان نهادهای حاکمیتی برای بازگشت سرویس‌دهی هم‌افزایی ایجاد کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/VahidOnline/75457" target="_blank">📅 18:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3kG5hi4Nd86NWg_koiarv1hgyU7EEms0__tINti9js7Ot1-3zVsN5byAOHldj0jcLLJ-yIOVsRQNOmpJr9mnbLG9Ha_qoiyx0Y3gzXkFgvJNH2DkfQF5og0LG2yICy21mGxGBN-4q1GIoeEp5IRgzEI8kjvdmW592Aq0R8Ouy9oo2CrjHfXu-6MTmIUUuksloWp6DaxEojsJ-r3WGGdzgnVy_N-bMvPgWZ50FoeWafLsT72ukAxpCJacs1TV1CgYp7DX1s12sLehZkYLyiw02MPCv46b-JQiuZtmVTieQs1IymX3vGq8Q4BVnGeesRHBMd8aEbVz5h49NQa9AIogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی شفاخواه، فعال حوزه آموزش و حمایت از کودکان کار و ساکنان مناطق محروم، توسط نیروهای وزارت اطلاعات جمهوری اسلامی بازداشت شد.
این فعال حوزه کودکان عصر سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، ماموران وزارت اطلاعات بازداشت و به مکان نامعلومی منتقل شد. همچنین تمامی وسایل الکترونیکی و ارتباطی او و همسرش نیز توقیف شده است.
@
VahidHeadline
هنوز از دلایل بازداشت، اتهامات انتسابی و محل دقیق نگهداری شفاخواه هیچ اطلاع دقیقی در دسترس نیست و پیگیری‌های خانواده او برای کسب اطلاع از وضعیت سلامت او بی‌نتیجه مانده است.
مهدی شفاخواه طی سال‌های اخیر به صورت داوطلبانه در مناطق محروم و حاشیه‌نشین فعالیت داشته و از طریق آموزش ورزش و مهارت‌های اجتماعی به کودکان کار و نوجوانان آسیب‌پذیر، در راستای کاهش آسیب‌های اجتماعی از جمله اعتیاد و بزهکاری تلاش می‌کرد.
او برادر رضا شفاخواه، وکیل دادگستری و فعال حقوق کودکان و زندانیان سیاسی، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75456" target="_blank">📅 18:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=BT7uJLXbmZdKhAQpH5LpZsNe7BvuR2k2mfa2xQLgx0gOPGRgvRGv95hGUBarH4m7wcw1mOok-Lnh03fIVy5OIrZOXNtuj2HBiHBLVKEh2-9mlYflTJfmvjPkKzJjypE7ErfY1bDGDDT1G0pNCIA90vSuyUhCMivI_D-1xd64Q0tzMhhUWpoFRnb-vTytERZaaWMi0xkzQWbc4uLRFUUISc3f4UG12gVypdCXH8C9jpRIpcy1LXpQf1W2gcGh7YuPVEv_-Z-GT8ydynwN_CSxxSGz_tJ-1KCS07eglO0bQDd5hO0SzJwRms6D9Uk3Iite67qWNk-Rtf5-wGkE1Sd1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=BT7uJLXbmZdKhAQpH5LpZsNe7BvuR2k2mfa2xQLgx0gOPGRgvRGv95hGUBarH4m7wcw1mOok-Lnh03fIVy5OIrZOXNtuj2HBiHBLVKEh2-9mlYflTJfmvjPkKzJjypE7ErfY1bDGDDT1G0pNCIA90vSuyUhCMivI_D-1xd64Q0tzMhhUWpoFRnb-vTytERZaaWMi0xkzQWbc4uLRFUUISc3f4UG12gVypdCXH8C9jpRIpcy1LXpQf1W2gcGh7YuPVEv_-Z-GT8ydynwN_CSxxSGz_tJ-1KCS07eglO0bQDd5hO0SzJwRms6D9Uk3Iite67qWNk-Rtf5-wGkE1Sd1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر پرچم حزب‌الله را در ویدیوی مربوط به بدرقه فوتبالیست‌ها سانسور کرد.
FattahiFarzad
دیده شدن پرچم حزب‌الله تو اینستاگرام مساوی با پاک شدن ویدئوست و ممکنه حتی اکانتشون هم بن بشه.
Sam1Kia
اعضای تیم فوتبال چهارشنبه‌شب ۲۳ اردیبهشت‌ماه در میدان انقلاب تهران برای حضور در جام جهانی ۲۰۲۶ بدرقه شدند؛ رقابت‌هایی که خرداد و تیر ۱۴۰۵ به میزبانی مشترک آمریکا، مکزیک و کانادا برگزار خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75455" target="_blank">📅 07:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i0tiZIXyO1t1zpWaWpLjbqED3ExUUrYLnRBlOR-ynriTOkQPqIHGORmHE6uNdNl-w6cdlq5HoFS9LFdEVGb_u2SmO8uyJa7LMlCyIyvTJtQYGu4q58jgS44PZKeotlK8At_6jzqjQGoh1PEmR78PrIrYK76xPg5Q4VP_ZFcSHyeoowG1gfGCI3gOaaZxzKzdH6kuyj__0EdpXRJy56U9LpHWh3EOf45ve2ssaqfOpmnwSF_InofRXZcF4eiA1-7SW2k89ffSOT3chvO2DvKuYdgas9PAiItuMKdjPxm_K4mhJnocX8kPwst3aHaNxfLnaKQ2H1z636JDPObEIMfwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERt79bIRJZ3bcpXxPQScAAr19YAmWzXTWFcdYOfifZ73-PJSNXUh2FiQmbcN3CVDNhRUEwQEQYYtoxX0U9Z_zCJaImf57DE7TtOFMAjxqPE1R5lOV2gaYqO1Hs8bbFJgIqITtr2jacx1vSjpJcvnv9EysrJ2gm_Fp7X7XvBKfNB60IkeMqx-9fKIgYNLu_wSeRVJ2dHRZfaTjJhF401Enw7kvAbX0nm7Vq3Rs2sgN0QztVVl_YWdo3PuWKGZpoDDEBWenES48les32iOGnPTJrkgFmTodBD8ei920KcPAWn2PFEawd40kTtEElQLGqrhXZHbXjrkp2KPTB5nyM1GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSknCtWcL1MJzLuK78MN4eJ6sAkhpSrNCaxM60bqMfveYsc4ROtjQkZUS2xhuC-BFY0CI4U25ft7PS_N5Hle41NuMioMKlBVR9PY6RdAA6ZyWZZh6f042mrj0HXMEIHd9_c0fEjjmLGojra23mJYdVRmE0_lnFwlzctQ1CkQLXU5MZ7c5QHMF74-x7NXrEjFDQPxVHUcP4zxrXyUR96sZl6ZlXqRQKflcyzmKJK0iDtD75ohTvC4kVQV-oYp_5wO7VsJXyKEvTynf0oOttdi2NG_8O7lqU94aGX1v8xmqQmTyr1FKDt4dBEaqs8gMSc67H0_0Ono2U66vzeD6_AD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MpbIpxdt87qWeY2hCeKGskM4Ny0qKQN9vpMCh7HYrm8ZdTJtHcWShr_o-xxJ36lk5i3e33c35Ackytz2jYxs__bPifd_t7j4VL7IVNvJsMI4RBEuV0aPP5TD_RpgqFXRi_C9EechKHCmyvf-Kwsb9_jDDopmrUzr3hoVLfPC27T_Nsv0jjKXlrG7YTpybrFW01bipnek_jTE2BIX32NIY4BPZb7CVTOxZn9N3iN6mNa3AAIb83Th5EhdQCXnXFwFQBI2GJcjY1mQMQhcpLbsBM-M5JT6b4tvAqEU-nubSUkrpV6xDFIyRGcl-vuL378iPGYDCc7CtIhtMIqX2-JGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل روز چهارشنبه اعلام کرد که بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با ایران، به‌طور «محرمانه» به امارات متحده عربی سفر کرده بود.
در این بیانیه آمده که نتانیاهو با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
دفتر نخست‌وزیر اسرائیل گفت: «این سفر به یک پیشرفت تاریخی در روابط میان اسرائیل و امارات متحده عربی منجر شد.»
پیش‌تر مقام‌های ارشد آمریکایی تأیید کردند که اسرائیل در جریان جنگ با ایران، یک سامانه پدافندی «گنبد آهنین» به همراه نیروهایی برای بهره‌برداری از آن به امارات اعزام کرده است.
همچنین به گفته مقام‌های عرب و یک منبع آگاه که با روزنامه وال‌استریت جورنال گفت‌وگو کردند، دیوید بارنئا، رئیس موساد، دست‌کم دو بار در طول جنگ با ایران به امارات سفر کرد تا دربارهٔ هماهنگی‌های مربوط به این درگیری رایزنی کند.
@
VahidHeadline
آپدیت:
امارات تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE1YPdn9r9H-3sfNldi3R4j1Rxdl1VLCOWpg3MKK4NikYwhlN5_BstADR_daP7awVzwaEEnQvAZynf3fEy5_DWjjsy9uEOor_XKBD11zrS_ySUulrPKMe0q52hqBUCAKRPlQcWQhjq3TnhQwUyZhJAuycO4VSnbo3EIAbz3k4aOVx6hVCSjH12nZLcPEh6lIMiUpkRQxrnGHLty_CaQ5eSTvgK8kP8hDBGtoM5c-b11cTY1P6UaVVdFR7b9TM2AEffTanNGCytGbz2okiPs1ozmxpg6YFswv1KPLzZIBknJUC0zYnkrZAAP8lLdnHuNumt5lQFBmddzFyp3aBz_DWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده روز چهارشنبه ۲۳ اردیبهشت با تاکید بر ادامه محاصره دریایی بنادر ایران اعلام کرد که از زمان آغاز این عملیات، به ۱۵ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده شده است.
سنتکام در پیامی در شبکه ایکس نوشت که نیروهای آمریکایی طی چهار هفته گذشته ۶۷ کشتی تجاری را وادار به تغییر مسیر کرده و چهار شناور را نیز برای اجرای محاصره «از کار انداخته‌اند».
این فرماندهی همچنین اعلام کرد اوایل هفته جاری، دو کشتی تجاری دیگر پس از تماس رادیویی و شلیک تیر هشدار از سوی نیروهای آمریکایی مسیر خود را تغییر داده و از ادامه حرکت به سمت بنادر ایران منصرف شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75449" target="_blank">📅 19:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=vnbphcRcviCEguYSTBoAyEhWZL95glk3VSdNWWmwrZI9FP_GsmPDGP6dXPvVo2S4QousKVNsCYTZKu_bRx20r_IQPwBJAxoNX4eGw3TKxKesw3lu1nmGFqPfCv8ML7XfPmswkbReWqRGutrlOd8AH-I6VZJwqhXlWxFvemjUdSqx66L5kTze1HbP7DiAAzI6HsBRqQy7Q7CAq5stlMVwlDL9oX1kKu0njf7SOn9OQbe_Lfx_tFTMfi0MoMcCOtc1SGZvqDOMjfyBIyQfS_AxjVRI2tzZHkbp6TeI0WY6ZOrYwLchKx85Ij9OzuYulKOimYDaPD9ADx4-vIHsz_YIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=vnbphcRcviCEguYSTBoAyEhWZL95glk3VSdNWWmwrZI9FP_GsmPDGP6dXPvVo2S4QousKVNsCYTZKu_bRx20r_IQPwBJAxoNX4eGw3TKxKesw3lu1nmGFqPfCv8ML7XfPmswkbReWqRGutrlOd8AH-I6VZJwqhXlWxFvemjUdSqx66L5kTze1HbP7DiAAzI6HsBRqQy7Q7CAq5stlMVwlDL9oX1kKu0njf7SOn9OQbe_Lfx_tFTMfi0MoMcCOtc1SGZvqDOMjfyBIyQfS_AxjVRI2tzZHkbp6TeI0WY6ZOrYwLchKx85Ij9OzuYulKOimYDaPD9ADx4-vIHsz_YIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ‌های ملی‌پوشان فوتبال در صداوسیما درباره میزان تحصیلات دانشگاهی‌شان جنجالی شد.
در این گفتگو، یکی از ملی‌پوشان در پاسخ به سوال مجری که پرسیده بود «در کدام دانشگاه درس می‌خوانی؟» گفت: «نمی‌دانم، الان حضور ذهن ندارم».
در دوره قبلی جام جهانی نیز انتشار ویدیویی از دروازه‌بان تیم ملی فوتبال ایران که گفته بود «من دکترا دارم»، بحث‌برانگیز شده بود؛ دکترایی که بعدها مشخص شد به‌صورت غیرحضوری در رشته تربیت بدنی دانشگاه پیام نور اخذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75448" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqmnYNJ-l5Bsj3b5keNXRWOZR9CyqoKUuz9AqbE8XRjl2sDttN-x7pBQMArhp80SNRppk__iE2ZU5YucqkpAHOBQblmNCrLgVpJVWKCzjqaSy6pGKC-HSah0JwZ9swqwLuO5i9P6vT0Gd6oMsptwQUgf7cQujg8BvznlwuB0jAcKUXfu0xWGK6oIgY7riBkKIS7B8JgNPqOHQMy0MgtF0fL8ePJE1vS8U8h_7w6P3izuScE-3BO3YxniUYWoXce4p7dMnuhx5klkpXhWupP4n1n5bJAdd4LEvHBhT_0uJf4fMNY47jUWCP9DN-eCuIZBR9dVZWuvoiUrQNK7dI5mRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از دو مقام غربی و دو مقام ایرانی گزارش داد عربستان سعودی در جریان جنگ خاورمیانه، در پاسخ به حملاتی که در خاک این کشور انجام شده بود، چندین حمله اعلام‌نشده در ایران انجام داده است.
به گفته دو مقام غربی، این حملات توسط نیروی هوایی عربستان سعودی و در اواخر ماه مارس انجام شده‌اند. یکی از این مقامات گفت این حملات «اقداماتی تلافی‌جویانه در پاسخ به حملاتی بود که عربستان سعودی هدف آن قرار گرفته بود»
رویترز با اشاره به گزارش‌های پیشین درباره حملات امارات متحده عربی به ایران نوشت اقدامات عربستان سعودی و امارات متحده نشان می‌دهد کشورهای عربی خلیج فارس که هدف حملات جمهوری اسلامی قرار گرفته‌اند، به‌تدریج وارد فاز پاسخ‌گویی مستقیم شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75447" target="_blank">📅 18:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3LGrKlMFumtEzz2y4KLHbXyrGg631saWaLThK2xXk6NJrSu-iXUu7FBksLhB-_CLSc_3BiKxy8jhOsIQVhz66zZLwzebF9GmZp6Wr84xM1N8uOj3ASeshd8KxAUZxKDFT7f4WDVNNVBNHzhSKD09WXBnhWlt79e1Hd6G9kemQLOYinatURGVyDwj4G2125EPb5mc2JxHyZVPmMBOTTdY5m4cj8Z2oM1AxWoLhk36_nWblKf1hiIcXfShMIO_XRwnJWFtAynw8iGEu1nJgMBFJoLVunuTTImZA5sDcHzcD0i0Y1v4VmzqHGylRLkPEIb51NyGmHU_YgK_bsi8Lanbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کمیسیون مستقل اسرائیلی جزئیات تکان‌دهنده‌ای از خشونت جنسی «سیستماتیک و گسترده» توسط حماس و سایر گروه‌های مسلح فلسطینی در جریان حملات ۷ اکتبر ۲۰۲۳ و علیه گروگان‌ها منتشر کرده است.
گزارش ۳۰۰ صفحه‌ای این کمیسیون نتیجه‌گیری می‌کند که تجاوز و شکنجه جنسی «با هدف به حداکثر رساندن درد و رنج» انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75446" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fQ8aTCJ4WOSUVD4si7dQsx2UxK-0y7Mq9Us-LECzFlincHd6X7yMz1sRbVbg_8VNJ5roXseOsByAjwaAFe3epizbICUx_Wx5t5tdOXj_znGFSwhqkdjLsy8ApPr_NU-xiAIbsb2bAssXNlUcetD7aDHneny7Vf2MijqqPFb6A-yO2Oip8Ltq3yajEkBVFgXzT-Gpk5l4ot6-aigCCP0fdNysCKD_x4SNg75xVMXrbdinKyc2Wy6tBiKi_iCkNVMVRQ6uxkdZeJ8ro3KMVmBbz2YtElO1dwQ6Hx-z-tBT-Yn-iMQNndkBEIqAaq4D16JRNLYTI4vEyMR6ZHO1CB6qaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، محمدرضا عارف، معاون اول خود، را به ریاست «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» منصوب کرد.
در حکم آقای پزشکیان بر «حکمرانی یکپارچه» در فضای مجازی، پایان دادن به «چندصدایی» و جلوگیری از «موازی‌کاری» میان نهادهای مسئول تأکید شده است.
این انتصاب در حالی انجام می‌شود که امروز هفتاد و پنجمین روز اختلال و محدودیت گسترده اینترنت در ایران است.
حکومت ایران از ۹ اسفند (۲۸ فوریه) و همزمان با حملات اسرائیل و آمریکا، دسترسی به اینترنت بین‌الملل را قطع کرد و تماس‌ تلفنی با خارج از ایران هم با اختلال جدی رو‌به‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75445" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PRzAfvnHpO6-tDx2IFkySTy_RDDkD2ugiew1L7rdpPIk8ibyo57r0idbtvlLYaZhNmM1uDixEaZYG50gEXgFqc9DzVcuEzfDhBi3-To3ZqOxRm9w2qHct_Ua4nHvA81a6eK9XrE3PtnzgPbW4_Wo-COeCu7BqQpXlZ4WpYZaNeGAcHAMPetbA_1EZnBg84w7-op2FW0nNwmPnm9KhmNonaOQYeaHXtjtMo5t7BKHM4mbWWRrRP4sjejH-xb2OSQrdOfWmMbO6Jy6MJtgv44PSjCLtBd4V4zLSjfVqvg2sBkR_LrC2ZJXhI5xreFkzvwTCFkusoGjZNmWqZlvWz4HOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با اشاره به زمین‌لرزه به بزرگی ۷.۱ در قرن نوزدهم در گسل شرق تهران گفت: «وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی دارد. وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل را تخلیه می‌کند، ولی این لرزه‌ها می‌توانند نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر باشند که مقدمه رویداد بزرگتری است.
به عبارت دیگر، لرزه‌های خرد و متوسط، هرچند تا حدی تنش را کاهش می‌دهند، اما نمی‌توانند به طور قطع احتمال وقوع یک زلزله بزرگ را منتفی کنند. در برخی موارد، چنین توالی‌هایی می‌توانند پیش‌لرزه (foreshock) باشند.»
@
VahidOOnLine
امروز پیام‌هایی از پس‌لرزه یا پیش‌لرزه ساعت ۱۲:۳۳ دریافت کرده بودم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75444" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjimAY4H5cTlfHE6mDK0Jq08ID3HV7AAMbem2sqT_KlPmelNugH6CHzfvyXeQi1YQ6EvMMytwzwOvrXUHjqBuOIqVUxWPQDMAnI-WEL0DShb1heIkGVapoBZ1YRekkZWoUvarRKcON-O3fma2YGQ10Jz8PQteXZTbAGp04GNYHcvIAlatrUbFh8LazFa0mXDhm9mbZDDPGDBI0TjEEf7_BEYvAhYvKU6enS5HvLjdypEsmSst-Uw5vU1G-WqqxdUtGnnuj59GQIu4LVA_W3taQ7xRhs81y_qMVrQNjk3Df9wubWnT4y2--RnPsXSs2dQjGrr7ME06gbr2dZDp53hAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان شیرخانی، شهروند ۳۵ ساله اهل شهرستان ملکان در استان آذربایجان شرقی، بامداد روز سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، با شلیک مستقیم نیروهای بسیج در ایست بازرسی شهرستان بناب جان خود را از دست داد.
بر اساس گزارش رسیده به ایران‌وایر، نیروهای مستقر در ایست بازرسی بسیج شهرستان بناب، خودروی این شهروند را به بهانه «عدم توجه به دستور ایست» هدف تیراندازی مستقیم قرار داده‌اند.
یک منبع مطلع در این‌باره به ایران‌وایر گفت که نیروهای بسیج بدون رعایت قانون به‌کارگیری سلاح و بدون شلیک تیر هوایی، مستقیما به سمت اتاق خودرو تیراندازی کرده‌اند. به گفته این منبع، چهار گلوله به احسان شیرخانی اصابت کرده و او در دم جان باخته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75443" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iEnAV-7RiY0-BeJcjg7VpnSQ8FemSGLIdMO3soKuuVOYo9RCQf3tcRD7lhiyWsvgx0EiJ2uwq_7rzpW9UmXyjMDW729Y170nOkgNFH6qyuKNwCQgW94CU3801Tz5YGSoYCD_jqqamCjpuj90NXEu8-dB9Ak899JiQEDRBNAMC7ydDk3GOG3VK2dBBQnKqbmB6buWls3wSWXZl8npI9AVI3q8poBCipTCbinux6IAF4Sof0lTUuR7ua0_UWtco5UhUqKje96GghGjncOdTWzdWkf5EEYMravviKVnpNkAOPetFIet_qaRyjghz_jQLpLJpeXkqnxj5q1pMLIEIMLKpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TzEjTqfhskS6oYLOwDMvTfjz_dYspITMqSOfkzHAClms2vQLNyb-zomFTUw8FdRUdTPYr3VyI3wGs165aRx9SFhtjODGqiJuZlBXdmCz-_xfKza4Hv_eUxVl6P4oLoauLaF3eDosOnpH0LOxHKijtSrJ60b0fr6VuqBVluBpeK6WusR_WFVwwxxgBQqJ4KlAk48aiIpJrHVfs4y_l99L-9Tnuqhg_gyC-kF3HDdZbuRz6nEhsK2aFCGsbP435GDzhU34gbUIlAhfFTyYkTc7QoG7b_dZfZ4OXI-WLRSeTI209_ZkXL1g0-kWwtOi3W2Dnva2CoszrsPMmgj1AgIdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p4G5JOCdI47AYt0GkeRUrGVQBuKlnldH-fKTdSTYlcROhXQDS2DM8seP7f0IF8fgsUqvDa0HEVswPy1IBxq4JVLhaVAwpf4ofWhVoCwqPDWWTNeZEqRuaeR00O0s_G9VkBGG5KUGiYsgAiATYpX7UbRsrL4oYJLw2L5DTahsOPGWeBrhScsjhQuRl2ZajCLAekdWFflA_CInYrVj0pqHQ5RYSLZjzJ26vv8SiHtflE0wMreQrtxuAitUOo3sbYqSGhoSQvpWPMUL-m-VP-MCcHPcGAoXAWDi6ykxAdmwj-vA1zz1T3hK4oIpAKk3tiTUF4B0cjnYcoyNbWnqob850A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i-afVAt8Hfg5rYibFuuBnTkUTsA1SNZR8Yxr2xnUHm8_P9F-PfANzG7xcSwHvilwnWZs5aIEo3ksjIob74PhPX1sUNnnRGd8_21Kwtbksm9K1duENunX01MhvVRNp3jHcR79Gv7EdlBuW7zS4O7pIIoGOvQS92mxt9Devw9D6aWL9XECa2Dx3IH_bT93nEafQfOHBrvQsuOVhr74R1xaY1fdiDoWl-88iNsiejV3fK7jhohYeqoBTAz3qtIPHBhAoLWQ8oyQxW0cX7aF3oc4h0QVDH4ZeRI-l3RamYuyjq4pxBBYFCzVK3ayj46hj-iWvCTfjXk4tj5zv7rZIlj-7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErqrJLmVmMJSnRNKiwErTStl7Oi1Ej_c42CJUm-XCSv_chVXkDro75L0LknIp9E4UgyDjTEcKNE1TyitEY9w1SRjRBOxj6uhms4d0HuBonlpMP1iEFuik2TECyp2thIOgiN9FqGJhvqrGDAytx5vvgsysI4ImtxZciZzvOWLJQ5TGiaQalq87HDz4jsR00NddaaIsN5_bhF8dIjZoJmFkggVedTB_M42vhFr0SSY3UEkYB5ED54-goBXd3oc-nOkTPCNF-mv57GIW8IYvGwMdGkjVfwuP6_HbfgdN-bg0JvP3uCh64YcPa8nLw_yIbFR8BTR8TGkVhavpirNOoJfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K60_VW7fxP11XcVgzEIveYU4doB6udC7NbWztiwrqRuAq95U3N1sRpVQGyD0lJUb5duYLefTd9WPYHmPc5f4NPHNGToOFXVMwvM44bL0bZAv8IAjAW2RGmjro1sIZXt97QkiEE2pd-mHtkHFWb2dRKqD7gNmfJ_6nucXXNbfT__T_8--cym4v0OC6RoZQP3hD-wgL4D3uhBnJMnCngyiuA91Sjr7_ZtXKA37Ysm4RlWI49iJ_pv5Fr8Fbl_JnyPNa83tfjml4tI9vQJbsH2Z9QWkbh_9U63WCnHB-4xSGsNconXSsrQHKijj06pQ7QniYmh-mPdha8IK6211OZw3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZ6U8_T-Kwl588VCMfk_vspnBsV0VjUf0tFoUPcxvBNz1Mv40r9bClr_ZDx38BCAuBgX1qbWgERLYxQyRjTrXByJHFAHZadbUZNnJ1Wxw9L73q00UBmBJXVPlEfMoL0f8FDdqgR6L70L3tFo8RCcoOPSe4rE4M-sIy5gc_6n-3sCcAXJzVd4bNu_C_Luk5BoUwZvdi8_mBRFrvx3DMGbzWzMTGNJ5EhfHgU1RP6NRDcczJWFXx5Rimzgb2gF061TLjmzXAsKYlp_hH6jI1xXajZsbJ8pqqkxL3KWNEuQ9edr0gtRozq8_j9dHhosSj4BPNIhDsDq6BnXNOANiHiQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=Qs6Diy_gfPqP8LXR98Kawepz9ihZDZ79vhutyG17d8RhyOKL6hc6fbojkYg0KDTKXOe2o7ZQ3oN3c8eomaTNcSLd-4Yoky-OWjMyfnJC53E84m1lTuZtJ5uIr3XUTZ5F_DVurTqg3I36x9Pok9dE7IjdB-ZKl1dBINEu2Q1jYLKWQOGPVd1GKZr-eTOwVs8BWD-3usSvMcm7OX81B30Qq2gIWIfbedRp6JZVLAY3FlZ7qNPlFMldqll4ohuMIodmSpz1H9eDzxAg_FEQOMuczvpDLDN2qfybrsV7wWeeauWL1ztlkS5NA2AHcFvvrJx-O8WsqnuMjNeg97TsCeEYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=Qs6Diy_gfPqP8LXR98Kawepz9ihZDZ79vhutyG17d8RhyOKL6hc6fbojkYg0KDTKXOe2o7ZQ3oN3c8eomaTNcSLd-4Yoky-OWjMyfnJC53E84m1lTuZtJ5uIr3XUTZ5F_DVurTqg3I36x9Pok9dE7IjdB-ZKl1dBINEu2Q1jYLKWQOGPVd1GKZr-eTOwVs8BWD-3usSvMcm7OX81B30Qq2gIWIfbedRp6JZVLAY3FlZ7qNPlFMldqll4ohuMIodmSpz1H9eDzxAg_FEQOMuczvpDLDN2qfybrsV7wWeeauWL1ztlkS5NA2AHcFvvrJx-O8WsqnuMjNeg97TsCeEYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCkBl_BQjQ4wwOUyKB6pbg1UoeiDoEZ6SrUoiDuD7ENr-tNj_2OPHdT137vvqpv6BoFdEGvIHN7CIm2stYEznyFvRO_JIiWLSfIFZjnFA5AOR2N6ghl0BiHkjtdOriJXC5bDzxQMwvqXpz5q2ChaoAioje556geaAJW5U1yUeVICoPn9hBxUJ-oEdvhijh5R-bwkkBxg2S8xRe5OFTFlO6rUYLVtWUGcBXCF4JxjjsStiRDRFkYkzMjos_C_WvzNmIKUe_qe5j7ETjX8_xn30NKkwbb4-bo9VKrn1WUgOQPZeLwswJ_7jGKbBiOb2xVlJzGGWabKSeue_tVBSGUgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8SpPRjvdui1I4vs7hlOBK2UP5zpCAOfjKxPHahfuUvfv94O6qPCZRYNsH2r8LC4i87nFKCb74wdKZP0usULM72EcPOnmgGWnTt5GreVjwtjmCJ6_sF8rlMDE_KJy39kVOwXw4cUMlxMbA3ES4DarQHi8pEHKhaPRSugoKLEFFGdwnbqrQXB_6sGy8dxEVxNtsXj7WhNzlf9W-UqqBFJVuJJpMiGEey8nUr7TNg6IOzUV4juhgAk8l5zPbCT9V0wwU5heJitvNNfuv1yzM5U0_QEMmLDh6-VXyctNA-v6q6-GkQGkZweZs7cF7ttPKB6A1IwwPjeK3u3eXNt2xnUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V4BU5EoTYUD3lV9Ii38yUBwgnZ5IJpNSmHls_TqVUSyFrg8jzp2R8-eMaREe_9CUf2C3kgKa_jwPvxhsw8-EIy-s0MvxhIPgd-0Wwm_wTwkJDVcsKHesl6pUXlOD7-AIirxRUGpRZo39y1jCj0hr3Sco5QnmR2u9pCjvNFWSLxQgwShP6V7nPxwqng6j7L417D3Ycrjd31XgswdFJ09RLw6iv2ufWSEOvNQb3Jy1iEOD9aLyP48zYAL3W6IUCI82_ljTug3i3-WgBzw02I215xaB3gQ3m9f--F_h2MTBY2A2_LgmJJH0zeqORYXNhKORlI6dU2Hrtocz7rYIAxi-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=sdeTxtyi3ecERXO2HlAJa8fQ_9TZZ2QYzjTfsJwxOC-WJ2AJ2nOfixX44gcxZUOLH2cx56JqzJfg21qs3-WOk8kfBnz9u-4_3r9ztMdfJaYF0E3IqMricOFnKnGyMuZjdOjxRsNtxfQBWJxSVNOLLWM3uYNbugrVh3wiCq3XLwqBKCx8MynmCAgLaL3p6xHeC2YCjKWojsaOJL_P2-zgq0b0iyEu5B5gVp7eOC8FN2mddSS-PPlxC5Is-5xCshYz9EmzS9b2gWy13tBv6ca4pXCqOwm79iJRE8zjDhmdH1T7MInK7B_TUB70SLB0bUAGJsn_2fC-eEdD8r7ExQ-PHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=sdeTxtyi3ecERXO2HlAJa8fQ_9TZZ2QYzjTfsJwxOC-WJ2AJ2nOfixX44gcxZUOLH2cx56JqzJfg21qs3-WOk8kfBnz9u-4_3r9ztMdfJaYF0E3IqMricOFnKnGyMuZjdOjxRsNtxfQBWJxSVNOLLWM3uYNbugrVh3wiCq3XLwqBKCx8MynmCAgLaL3p6xHeC2YCjKWojsaOJL_P2-zgq0b0iyEu5B5gVp7eOC8FN2mddSS-PPlxC5Is-5xCshYz9EmzS9b2gWy13tBv6ca4pXCqOwm79iJRE8zjDhmdH1T7MInK7B_TUB70SLB0bUAGJsn_2fC-eEdD8r7ExQ-PHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XHILg89zKZD4jtp7s9U4e7Szhxp7A_1IPC0UvOTfvqCquUpuT_iCUowuCcGED_2G-lQbVNM0JHy15wjtjeQAUBw3D7AmOyVS_gmxaBGc3s7mDLhuRMXzMVIc_pgFci2pjoMmhNBO0IthHgnLa7F-TSU2KW2lpbWsxd1hlSVoOMfLuZSo0AifwIHe3LuSHVSbeXzBhkHlxTpszVMRIzIMCM9QYL5H9mfh-FFQH-ua1qp3tphqijD_aHVaf4JogcOBMyW4ynEFk9s3_LZ5AeKnDsJ9TAC0pmGKKEz_YKhjUcVh2h2Vua0EoZobi4IEktrDdmu9ejSPZ1G_vjXon3r6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHTJFfgQmf4UTmOVw6_tEkqQ3xBOn1eEZxlCTYeegwEp6V9CMTbQr6bP7YfO1RZIkfblz7ZrbBCdRhdLgR0O9O8HzqQp2TTzm9zYvvbQTwFyqOKOVSNe1BsTyff4A0S0jiPklasHC2YXXHv59he9t-f8XiuYyf1w7tAM3swAUqILz2PiYdkcift5EFC4el1S5MxZXkOgA_B1AWMHn-DtA6EZr-yHTDikT8twzRpn6u5_lCZ64Mi0hETnIxmTcDz2FsUaXuXaXGNUSUu_8keU6DwEERL1p_SCabed12L11gkf6rhes0JrrTu9nZGdWv6KW5PekTutI32StUuBvIBmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrTc-b_NIvqs29TQtFC-lh2pR-UsLJBbD5IF5JbJAjeb5SBe-DRP84OYztn7gvdMUSe8dJDy5ok1FeeRmhonltNMxRkCsByux2YJeCRS4ITjJeO4hAN3hW6z8c8e4kyC1tmM9iV5tK_aqC35ghAKMmAnQkEISWvg-taPaoTcinkajKoHA9QjPTPHKIOb4mbkm8VYm3aRvUKO1YD9xSHCKH2Cgn25KIg5diadwqVDaEj6QB5FlwZdpoN_eHpMV4g9E4UOVHNAuQ7uuCNYvvRtxAUy97x24IeC-vfzgOmCuS0FW31RqV7UxIlv7dSA3k3NgFbIZWE6qsOLaLb4Wqxitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pphTXFy6zUDD1WSbgIK_h84zaXKgNQHIJ5vifjA9tTFX2sa_EEEkH73fsQYDGnSzd0VSz_tzJENFQEXfWjv9MjvrI29C-b82HtGHJW3AmQ0aL_w4NVD-sBRLwRdXQJkNELq3Z-6A4DP5dE-M2Kjpjc_uKx3Ur52Ft9ABNx8Nxw54yaLHHqA4XWG5UOj8G8cUTCvKnPTAzh9T5PvWLd4CxMz1vSATkZTF4QrADC98xAI93R6XpyyONbEj84ZSlSQ9v0Xv6BZTW3sjYcDsEsWY25cDFb8X9bc2WFkasyRv4-M6lEdj97GWBD1QQl-pz4-h3QI_IOcOoh3QjlCuR3AUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7xYTKZ3GJRSxMaoQNR7lfxHZWr1yJ3StpEgOrPFXgRHGnjrj3JMAxwKuVm8E3ccTzhIH0ddaexXzjkurYuo89xZsRYObhHJQriNX7WawDRvqK0qsgs6tagJyPR2_PCytVgvNrdUh8NNdbaR6_dw-HUr8OkJe_pgJmOs7QYotTfWl4OPo9v_dTcqzVDrkN3dTn5pncdY1GnEvX1yWLXEaVQVfLTM0izThjQe89sbw_-W35rr6LtBFM4E77Yhx8RGiulQUmfoWev-86S_xP2M7U1rccfxxqhpuxkvj6MJXsOF7ToyzDwx0_ZPTLZw8V_HiRFlRa1LTpRAKO2Cj4xcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TrIyOf8NMQc7lCbKyblfEp6yyfQq6PebdaXxMQvDeFQ4qqlD2R6i3ZMRGMmKdbiwekdqp5qau2ISO-bUKXigocqptmBRkSuDrII0dlErB6gHV2C69FAERmJHJfUINjZ7jxHx4fxj_TtwqlzLy3s_lLhLzM8hMhXIMPtUXcsqZZS3boMxCoy-DiOo8BCv4oIS3qakiKjDP3jaM8GcazJAfY4E0rxXB85JhN56DJiWqE9hmGAmr5Dj6PAZgEX51H8lkpuMO2UOhvtaieSFfZ3Stqdgm72cN8S7IBxqkyDsDbXx3ScNoU9JopDNNfd8lvtWZwj071psgjcBH6Lm2xxz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jFESL0dRhWcNsy1KKOZet1K22rTKUPRY-af2yOUN_PL2Wlq8nOkl9qnpR7f7MXYz-epuhwfUuDb4YHGGyVYLnhJkCuBWQ_K9AIGeB5XGQi8KmGCqMaG24B5uNeGf66LbEzvaTeD5GAOe4J2lK8QriX_F-BgR0NY4g0kLtgw3zI7EVmdIKqZDr7xIjNByizY7shHEXqqbWjTRegpXC0eXeprn3DuVdC4_UoDZ70xLBNfaXHg39jc9_7ynkV-dE1FL8aLIIznwwHBgqTTAnuFcxAYChbioymfdmSxFDjDLyya7_Ja4RT5XKufkZ-1cSsiegtsccCq7GJLOszPr1PAyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hy9OoCzn0HoRV-s2lENlH8LJMB6lilMdL3yMPCkssXQ_pECFbcH1M127apmVc4MkSGyhWjalj8MpFwom9-RcjnYEx13lyC5IFtNW77vtMaFlViKe0w3CUqZMRQPic6A2DJWwCsBQkjSb3qAavHCMhIVhVPC0RSzmaMB54GyQ0DPc3iU20Ym02g8eO_y7iJPHo34q2xGWQmvEMNVghuDH1-MBaNeXuDeIfyyDdlLZvzOHEbDIrw96jLlJ-U7PWMEGM0GpqgX0wie5fYXd1Bca70JHDZvMqeSwd9J707lsSnUehErXafi9jLSwOoMy18BVxR6foxCQqwKwI5MVOZ8rdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WA7uunh2HDeCCGWSEyZkqwRRuzz9ZBmCXmjN5SZlCBj9gdi7nzMs6-bTSUIgs07a2J5OztL1CFP98-ZlR9ETc00SWSrgrxinDu6LtOWqobaoZZm-N6oQejopqd854mH8C3mSW5GSFj7gHLhulmGxjl3wpdJEiDc5Ny4COUZFKn3Q5biOOD2Ts_fzEwzX3hvXjZeRKqyRTDj4N9GiyrdrfTuXpSlqHTHnoMuJAWfAZVrIpE19k9FFCth_P1pJt3q_UQ09svqjRPs_5hzZFesSqvvNU8j4C7q0ggmCEKgm0qZ7OZH7cnxD5oggS76wPc5drgazRB3QyP1hF0U06AaJsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pe8nXS4UVTWzfLO0f8MOUV0bQlYOQoGMvkq7Kdny_YT-Mfv64lm6orZIoLJoVrb2gJH6VbeVjLOluMFFW-JE-RRxP3We7tvTE2JE-m6uIxYC7eo_8_N2hceLUDS0VktcjSysKs_yo5YbKYYofEnzAjfMrANKvjbCT6oqUg5i_ycPoLwuo0Mx64bbe5X-kTOcJE96W3bNCrfgImE3qSpfeHWWTS9xZ51sfsAuVUyzIR4Y8Wrx6u4JJSpU24Ccdi1_wcorJlmEyK_XKweWUAtL9J0fIITRy__t0D7ehWXQ_fhP0INcUT1jbXckqvbN8lxp_HcoLzS0JaQ-j3oNOFhoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/csJluhftypobItKAnjyrJShx5b7VkjkVDwrhvMgCH-dYs3VbboEiXXjIeqghosPXae1Sc3YO-EEyBm71kXbH3d8WtAssNl9GzLP-ylsRRIarECc_VuR1sTuDGfq0yXBv1duCz9fbVNvsf0J7_67nnSMxpwl6f0CAAKE2U9KtqhpVS8YbWN92texypLhq1zS98pYQIAmIXuvDFb_hxKV1CrKlygKsYDafpiYSLGmEobRWCiXYY75w1OUcl0Hp8URCAOoWgu1ORfCGXqBGG1LjnBWuk4eSdqmCC3z-y2hsVyUBQPB8yosRpXzsbWDnqPXhj5KDw9DYHzjVIn_9kf05cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n624GICiAheixhqseONGPy5KXyFtNTaAgnQaFNPMGgtwjOUEVJMs9BEXLsftwi2HjnJYHkCxSeHZ6NWIur4fSUSX5g_BEC6tytgQvhTfT02_o9MFTZVvllvw9xoygQlRpXS9sTyfaYXnyKw_GyKPDOhrtbYjY0aZaV1fW_U60SO5cAkXMDHVZ1VV4UkBz5pcBlZN3NSySRNDX10naAT9cFCxo_uhpURUqARLTIZNYzLye35J7DjmX5B4sHaRrNdbqX0246Pqzgx73ntikV8EBww1rNLdHI4TEaGSsoBb5TP6U-YrV56HAs4kKMbj3MVdzp58xHOhq8sFMbzcVZfacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tijbw-izszJQpb1dxHY4M3Mc3BejtA-QZsISQz74NVuhkFvZ4plhoRLst9Ppl0J9irvQ6-Y4MTeFXQoE5nm2hBdye58zqcNOPafrF4o5Uu-L5madngaLKWEdobajYic6WWlOn-CTRToN9Hg7nMLU4S3uGZJlvSwu8h4pUN4ZI-75U1l0mbfaBFEUlVk_SZ1sdDh5apDRJLdByp1U-oDAannVf1rSHNf8CJTTBPEjPhTNBKMA45pqo5I4kkj9o5zeupBBupX310udD4e9Yeee0oLjP-qfYwC9lyC8cGnsqETjYrcMFAwgZR_T41ohklJucNj29peqmDDKkTabgZXqPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=AitmAsR_lTZ99SVq1hXQ06JzIUdzw3IguhnbvTJFvPQp4HxY2PlplBIo8Ua3y20ngXxYwkKpA91c2-nbzY7PQ274vhQi-LgFeD5zHXskQMgJaqH2X_nWkcF57s3W3hktS7MU16y-crpQH1WCXLxOmPLdrmoNv71_DsVGk1X5OHBXbqJgn7pXnrYooJ8nn95BX8h4DbS1eKfWVe9x53tRkE8CSz_MltDojWBQRfxYxMrCEjG-wDx8qigZfvZVZWs18eEg5ZlC_jSdQBZt9QwN4WuRpT6j7LHht4wGcg_WC0tUmSDU9XkbHRo33x3rPqVYo9SejBFTlxSKvmWct4rHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=AitmAsR_lTZ99SVq1hXQ06JzIUdzw3IguhnbvTJFvPQp4HxY2PlplBIo8Ua3y20ngXxYwkKpA91c2-nbzY7PQ274vhQi-LgFeD5zHXskQMgJaqH2X_nWkcF57s3W3hktS7MU16y-crpQH1WCXLxOmPLdrmoNv71_DsVGk1X5OHBXbqJgn7pXnrYooJ8nn95BX8h4DbS1eKfWVe9x53tRkE8CSz_MltDojWBQRfxYxMrCEjG-wDx8qigZfvZVZWs18eEg5ZlC_jSdQBZt9QwN4WuRpT6j7LHht4wGcg_WC0tUmSDU9XkbHRo33x3rPqVYo9SejBFTlxSKvmWct4rHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت گفت پاسخ تهران به طرح پیشنهادی صلح آمریکا احمقانه بوده است و او از ادامه جنگ و فشار بر ایران خسته نمی‌شود.
ترامپ در یک برنامه عمومی در کاخ سفید و در پاسخ به پرسش‌های خبرنگاران درباره طولانی شدن مسدودیت تنگه هرمز گفت: «احمق‌ها نمی‌خواستند قبول کنند. فکر می‌کردند من خسته می‌شوم یا حوصله‌ام سر می‌رود یا تحت فشار قرار می‌گیرم اما هیچ فشاری وجود ندارد.  ما به یک پیروزی کامل خواهیم رسید.»
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت، در پاسخ به پرسش خبرنگاران درباره آنچه او تغییر رژیم در ایران خوانده بود گفت: «در ایران میانه‌رو و دیوانه‌ها را دارید. دیوانه‌ها می‌خواهند تا آخر بجنگند.»
رئیس جمهوری آمریکا گفت جنگ خیلی کوتاهی در پیش خواهد بود. ترامپ تاکید کرد که میانه‌روها در جمهوری اسلامی از دیوانه‌ها می‌ترسند.
دونالد ترامپ از پایان هفته سوم جنگ می‌گوید با توجه به کشته شدن دو صف اول رهبران جمهوری اسلامی، تغییر رژیم در ایران پیشاپیش روی داده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد که در حال بررسی دوباره «پروژه آزادی» در تنگه هرمز است، اما هنوز تصمیم نهایی درباره اجرای آن نگرفته است. او گفت هدایت کشتی‌ها توسط آمریکا در تنگه هرمز تنها بخش کوچکی از یک عملیات نظامی بزرگ‌تر خواهد بود.
ترامپ همچنین درباره مذاکرات با جمهوری اسلامی گفت: «حکومت تسلیم خواهد شد.»
او روز یکشنبه نیز اعلام کرده بود از پاسخ تهران به پیشنهاد آمریکا رضایت ندارد و آن را «کاملا غیرقابل قبول» توصیف کرده بود. همزمان صداوسیمای جمهوری اسلامی اعلام کرد پیشنهاد آمریکا رد شده، زیرا به گفته این رسانه، به معنی «تسلیم کامل رژیم ایران» بوده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، به فاکس‌نیوز گفت واشینگتن در حال بررسی ازسرگیری عملیاتی برای بازگشایی تنگه هرمز است.
او افزود واشینگتن فشار بر جمهوری اسلامی را تا زمان دستیابی به توافق ادامه خواهد داد.
ترامپ همچنین گفت هنوز تصمیم نهایی درباره ازسرگیری «پروژه آزادی» را نگرفته است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در گفتگو با سی‌بی‌اس نیوز درباره پاسخ اخیر تهران به پیشنهاد صلح آمریکا گفت جمهوری اسلامی در برنامه هسته‌ای خود امتیازاتی داده، اما این امتیازها «کافی نبوده» و پیشنهاد تهران همچنان «بسیار ضعیف و غیرقابل قبول» است.
@
VahidOOnLine
دونالد ترامپ در واکنش به اظهارات بنیامین نتانیاهو که گفته بود «هیچ‌کس پیش‌بینی کامل و دقیقی» درباره تنگه هرمز نداشت، گفت: «من داشتم. من می‌دانستم آن‌ها تنگه هرمز را بسته‌اند. این تنها سلاحی است که دارند.»
ترامپ افزود آمریکا می‌توانست در چارچوب «پروژه آزادی» این گذرگاه را باز کند و گفت این عملیات می‌تواند از سر گرفته شود و در آن صورت «بسیار شدیدتر» خواهد بود.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده یک روز پس از مخالفت با پاسخ پیشنهادی جمهوری اسلامی به طرح آمریکا برای پایان جنگ، به فاکس نیوز گفت که ایران فنآوری لازم برای بیرون کشیدن ذخایر اورانیوم غنی‌شده مدفون زیر خاک را ندارد.
ترامپ در این گفتگو تاکید کرد که اورانیوم غنی شده ایران آنچنان در اعماق خاک تاسیسات هسته‌ای دفن شده که آمریکا باید آن را خارج کند.
براساس آخرین گزارش‌های آژانس بین‌المللی انرژی اتمی، ایران دست‌کم ۴۶۰ کیلوگرم اورانیوم با غنای ۶۰ درصد دارد که گمان می‌رود در تاسیسات هسته‌ای اصفهان مدفون شده‌اند. این تاسیسات در جنگ ۱۲ روزه و جنگ اخیر اسرائیل و آمریکا بارها بمباران شدند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده در اظهاراتی گفت: «مردم در [ایران] می‌خواهند به خیابان‌ها بروند. آن‌ها هیچ سلاحی ندارند، هیچ تفنگی ندارند.»
او ادامه داد: «فکر می‌کردیم کردها قرار است سلاح بدهند، اما آن‌ها ما را ناامید کردند. کردها فقط می‌گیرند، می‌گیرند، می‌گیرند. در کنگره هم درباره آن‌ها شهرت خوبی دارند و می‌گویند خیلی سخت می‌جنگند، اما نه، وقتی می‌جنگند که پول بگیرند.»
ترامپ گفت: «من از کردها خیلی ناامید شدم، اما ما برخی سلاح‌ها را با مهمات فرستادیم که قرار بود تحویل داده شود، اما آن‌ها آن را نگه داشتند. من گفتم آن‌ها آن را نگه می‌دارند، اما چه می‌دانم؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75408" target="_blank">📅 20:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GenxTOXXWTdGswWSYmRezGrXg9cUJc8GjMAn0gyRU6OgnV-D7j0KDd9N405XvumM9MfjBUH-UGuDWFJhSFywzm_0p6rPaHwFSsUaSM_gFe8fbXyVI0novUTTfhjbTtYxQsvqo1-EgdQZJOpPWfjL9PQ4bvi9xLFtbXxYThFJkQpRcSzO8TqA4n7ZE7Nrame-i1JDEEEVe9MBzFRccGWpIx3cOXqF8Cnwpu0XLCrCvgEMip24DF3VQrrcYD0KyuXNMGQijusClW8aFF4oixdElXuFQsh15fQF192l11hvo-INCssFFrKLYLcU5cc_0Q3AOrmLhyMQVQ0Dph8nrSXwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EffAz7HsBV8Q5c94W2Olj2p5d-hu1LVpcseWBSGQPgA0Ja3pWBJmE5H15x_13MzxGOVmU6VA39-ckIT-X6iLUm4QpJHUpAcXEQv1n3BQaSmOFn3wRo85Bz1DGXg1NyIzcweANytXtIPeERnQhsMPNuuOeBeu7PR0RJGii4SPppsvFMiCclj_7DOJ30xUeJaBuiRXxl_6m9WRv_t0Zv-uuQG4Od8D53QTLZuneHHV1mlMHHOAd1eQ9mrNBEc2Gnn6rUccr2Bw6AzI2_c7_eygH0WStIUaMSlaWQrugklB0nqlWwtpwidnXRB_tygMPOYI57u-1aeQrqibZbFFAgSWfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">AmirKh1982
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75406" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قطع اینترنت نه تنها ربطی به تأمین امنیت زیرساخت‌ها ندارد، که «اقدام علیه امنیت ملی» است.
در ۷۲ روز گذشته میلیون‌ها گوشی، کامپیوتر و سرور ایرانی از صدها پچ امنیتی حیاتی محروم ماندند و در معرض انواع نفوذ و هک قرار گرفته‌اند.
در این
#رشتو
بخشی از این آپدیتها را مرور می‌کنم: @
hamedbd_channel
hamedbd
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75405" target="_blank">📅 18:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4BIgRtpXDFVUOqDuZ1SRHsNxDMOw82Wy7pTf2pVaD2rpxYY-gPwwfTCZegxHheINNKT7YoQpDzBM5Osb9z43zDGRldy8T32y_OVOSS7tZ5TAX3rQF2QdLI1ZH_ptJDkxeJX0R7OT7zdlTWdH0yTqUqSRAr5MCNc16Xz3LiGApKyvZ2pm_WoCnLlezT7_E0hutEMYK3yWz1Xg5XRuBkW9i7x40GOTvV8NfsKxPloe7DblmJyMkQNZ3U7rqnyrcxzkX9VNrQ8Vi7svnL2-nkqsro-HLPR9Oza3OlJHKdGUVcHpLd5NZ_j8PVlrmHIMbpxFeejvMVma-1xMgI961v0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار روز دوشنبه ۲۱ اردیبهشت‌ماه در بازار آزاد تهران به ۱۸۲ هزار تومان افزایش یافت.
این جهش قیمت کم‌تر از یک روز پس از مخالفت شدید دونالد ترامپ، رئیس جمهوری آمریکا با پاسخ جمهوری اسلامی به طرح پیشنهادی آمریکا برای پایان جنگ روی می‌دهد.
علاوه بر پاسخ منفی ترامپ، بنیامین نتانیاهو هم اعلام کرد که کار اسرائیل با ایران هنوز تمام نشده و ذخایر اورانیوم باید از خاک ایران خارج شود. این اظهار نظرها احتمال برخورد نظامی دوباره را تشدید کرده است.
قیمت هر سکه طلا هم روز دوشنبه در بازار آزاد تهران به ۲۰۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/75404" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UE7IT9wpliO2T1sT42WDpfyHTBnulPHutyJTDGGDdrLf_A7kn61pzV0-qSyGD7V8gzbSFiM0rPM02J28R-dT8pqqQ4S1DidMugHqNX3VC5gvfPluK1xZyK0zbgdWz4JQoqDAiTVGTwFG9YqIo44w0LU4CCIOePZrJAXO3Irkz2UdzKs_ogUBO4Ulp4-dVH9flJ94xXnmZKLmgE-J7LjjSQVpKriufTXrkKnJWjARMco0lIp81S_hGqW6qvLxk18k56a22djEmU4gCVABFMwWZvFM7ye72UmnWoryfDuOnobYaZlUYUA_X8bpISU9NeVves7ou-AI3u3lqpL0j4Q6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/td1MmuUO2z5oW761s7-ygCEfTSJYa_rUxc1bIfTpTaWaPMwAYtvNh7kVXtnGSZXf7tjopQ2zVjk84nNfoylTiYQNv9PjlelZcxxKwVf3L2hNyip88ysB0vQ4Mb-_xK4C0XnQ_hIsAr_Akx9SbnK27aaJDlZfpwdvbKAqcoRu47Aob4wjhqt00Ne4PJ9UJyuXk8UnFFAtf0gfJNlPjqNsr_YHQmlmqlhRKQ4ImnRN4DQ-4U0gRHc8qogaI7ShtGmcIwG2ma-rOXjmP4tPgKGJwd1WJGwEbAyyGCekE1D9Vyp8GzK2bOsr67_d5_WRgvWb7IXL321iOIWtNeIYEprnIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😋
💩
«محسن محمدی عراقی» معروف به «محسن اراکی»، عضو مجلس خبرگان رهبری، انتخاب «سید مجتبی خامنه‌ای» به عنوان رهبر سوم جمهوری اسلامی را «کاری الهی» توصیف کرد و مدعی شد در روند این انتخاب «دست هدایت امام زمان» را دیده است.
@
VahidHeadline
«ابوالفضل ظهره‌وند»، عضو کمیسیون امنیت ملی مجلس جمهوری اسلامی، مدعی شد حکومت ایران به ظرفیت‌ها و سلاح‌هایی دست پیدا کرده که «بمب اتم» در مقایسه با آن‌ها «ترقه» محسوب می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75402" target="_blank">📅 18:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FHd5rVh_vgB9qUNxN1MlUI5t9Tc9hl8V7nm995cnOXgesfS_DcTAwQcL2hq3FpArLILOziKVR0o-nWob5PH55Uw615PO469ae6YcU3Hg5MuczebEYAOCOrrTexBIh9Xi-hOX53L3p5ARn8RKQ_8Ez4UWowMNZSehmGZi7abyXd9l7DfQYabJkW0CDV_SUS2McNAMJpV__IboyErsZC7gdnhNS9Cuqb1Tf_JOZrkOzB1TSNqGOWjhZEByIx1o37Nb_WL41CZE36E4BqBtrSfi85p-gRel2cmlrjidcAKhG_EWIePjwtYxOTeU3UnHuIhmPTNfLUSQo_7vCg8Z3jzsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UcLIRPaJ4hcPoN9Bwp29bIapA8R37fz-Hry7b5-nRUUttoQQAZlSrcj16Sruwzd-lAtmBEjRZ8k_le-0rJ47zP26vkYairwh5eSyoeiN3qsavzLEPOfMSY4t8LWCLRYcRUxF7IjgVYhP-emZiFdhd_XQtA8VbDcVOgEYFXA-f8IjhY-ZsDUHWOXjtNEQCvsHJJqOuBEaH_ahiKGfzeroyYzgQuMBWJGv0_crRspZaG4MXmTI8tfH-9ufLnn6LBODAhOVKkyk77B5dLT_K-gr-ewJVISv0KIdm7tev4PdA-BygEzZ30RLs1iyu81J2zoEgDJp52PvaHjqxnJXMIMs8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا تاکید کرد که از جنگ ایران حمایت نمی‌کند و افزود که شهروندان این کشور نگران افزایش قیمت بنزین و تاثیرات اقتصادی آن هستند.
کی‌یر استارمر تاکید کرد کشورهای دیگر می خواستند بریتانیا را جنگ ایران بکشانند اما او هرگز این کار را نخواهد کرد.
@
VahidOOnLine
دولت بریتانیا روز دوشنبه، ۲۱ اردیبهشت، ۱۲ فرد حقیقی و حقوقی مرتبط با حکومت ایران را تحریم کرد.
به گزارش خبرگزاری رویترز، این افراد به «مشارکت در اعمال خصمانه» علیه بریتانیا و چند کشور دیگر متهم شده‌اند.
در بیانیه رسمی دولت بریتانیا، از جمله این اعمال خصمانه به «طراحی حمله و ارائه خدمات مالی به گروه‌هایی که در پی بی‌ثبات کردن بریتانیا و دیگر کشورها هستند» اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75400" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkXTn_9g3Ce5xP7LiZvIX2HZUrO0HqmstKpwvFiI46B1GRjuKzIbVh80fiZmRm3Iolhb8rJF-d538aWnB8ILMkscZWFxlyomCZQeWRQNJGB7gxrlzrcTYjE_MkqCeZfoi6R8-ns2UV9fTM0isqPNZp6rs8NftZCx2LJxPQNsEWlS3Q3BxcCyVUompqNKyFYljLAJSXpCybXE4bWenRL7oU2YD5aHO9zNkywoBF2oazxnFhtrm0FtgHjs07U-mZ9tfJD8qusBJ-xXJduueyMNbFx09cOoV-O99plmtDFHkxoW3YK8Oy-iRDIwJvNfrNPqLMZhCIVadACuUoOqMQGClw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی جعفری، فرمانده قرارگاه «بقیه‌الله» سپاه پاسداران، گفت: «تا زمانی که جنگ در همه جبهه‌ها پایان نیابد، تحریم‌ها برداشته نشود، پول‌های بلوکه‌شده آزاد نشود، خسارت‌های ناشی از جنگ جبران نشود و حق حاکمیت جمهوری اسلامی بر تنگه هرمز به رسمیت شناخته نشود، هیچ مذاکره دیگری در کار نیست.»
او افزود که با این سطح از بی‌اعتمادی به آمریکا، طبیعی است تیم مذاکره‌کننده با هدایت کلیت نظام، شروطی را مشخص کند که همه حقوق مسلم جمهوری اسلامی را تامین کند و این شروط «حداقل انتظارات» ما است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75399" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HBr6Qi6Sjrx1K-Q6KZVkcG8OOxlRPM-Wp0eTIAoba0KEANoQtEOr5sBS1hfdZAfCOkt5WFKHHdiziQmRNTM2vqkhIZ2QvGMM2o1oWVnVJN-gR2cMHM9043on8WHy29_eyMTrs4uiLIyjMr6yhCvPUViLACzDyTLSCxMQiuTosYd6FpmtqIA77HyrRMY1IjRFEzg8E0oEjVx55giTzyAjtjQr7eM-znACFuI66Xn9uBw1-_AShgFy6yyC8zrhBUs_hKjHW3_3T5aZ70uXSlynT21jiTRsiFZ8qVJVUV04BsK2kmKtOk3oFqoZRtXVu_aK9AwHBplkMFCO0rAqj7dS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EfSk7jVFRiEdEruyK30nMc2zdNdbZS0EVzhr6QD4fOtboz-Bsp4R8gZqPdVVtMCxSr9UDC6iOh8DdQgZwt68MMYhnizmt4UZP2T_PqW44njw-N3TF_xYB6gSyc5EGjGa2fBIT43aWdDrt97Kfg4CyEQhWB2LWFPgNdjXzjeu5Svs35FU19V93y7YYvYPpkG0s1GkhxvO9ywx2qJL7dxa5Pfwp6sFgQCNWNTRp1kuOGbPJOuuhP4nuswC-QGqoI000Irs5pGW6H1J9suDfxkjlwh9lGJufeNZL-xSTmlrNlQpN_E2U_xES57fWVpf_t0ovPrBfp7HTex3NljyY3h2VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=O58fG2DyrVmso3dMQDQYj6JsV713QzNvbNKn0BPLkuRvRr_IJoo1E_mkmLZ3_LDVfFSchQlJmfXqtdVGz7tBzPkV587II7230Xsdc-xQIbwzM1pbudAgbBRs0oZL_weaDrUIZTvHd0ZbudMDvaLuRkNjYcua3tGXKi7M-aZBTAQppEeQe2WEOllUj_Bdfnp-KQucFykYbOQBk1T9N8BezeBhytDCG6fAPyYmu06zt3z9fnPbG78oPailTBuZE2QUWMVREKJGGWBR6o3T0VBpjnrcJOht5r5PRPSqJRzsZ1hmWL0rnNTPVVKc620a3ljaobeutyCZG01MGLDclAb9DA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=O58fG2DyrVmso3dMQDQYj6JsV713QzNvbNKn0BPLkuRvRr_IJoo1E_mkmLZ3_LDVfFSchQlJmfXqtdVGz7tBzPkV587II7230Xsdc-xQIbwzM1pbudAgbBRs0oZL_weaDrUIZTvHd0ZbudMDvaLuRkNjYcua3tGXKi7M-aZBTAQppEeQe2WEOllUj_Bdfnp-KQucFykYbOQBk1T9N8BezeBhytDCG6fAPyYmu06zt3z9fnPbG78oPailTBuZE2QUWMVREKJGGWBR6o3T0VBpjnrcJOht5r5PRPSqJRzsZ1hmWL0rnNTPVVKc620a3ljaobeutyCZG01MGLDclAb9DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نشست خبری روز دوشنبه ۲۱اردیبهشت۱۴۰۵ گفت در شرایط کنونی اولویت تهران «پایان جنگ» است و نه تصمیم‌گیری درباره آینده برنامه هسته‌ای یا ذخایر اورانیوم ایران.
او در بخشی از صحبت‌هایش بدون نام بردن از دولت یا فرد خاصی نیز گفت: «هنوز با کسانی که علیه ما تجاوز مرتکب شدند تسویه حساب نکرده‌ایم.»
بقایی در واکنش به اظهارات «ولادیمیر پوتین» درباره آمادگی روسیه برای انتقال ذخایر اورانیوم ایران گفت: «در مرحله کنونی تمرکز ما بر پایان جنگ است. این که بعدا در مورد موضوع هسته‌ای، مواد غنی شده ایران و مباحث مرتبط با غنی‌سازی چه تصمیمی گرفته شود و چه گزینه‌هایی را مد نظر قرار دهیم، موضوعاتی هستند که وقتی زمانش برسد حتما در موردش صحبت خواهیم کرد.»
او همچنین درباره روابط تهران و پکن گفت جمهوری اسلامی با چین «ارتباط مستمر» دارد و گفت: «چینی‌ها به خوبی از مواضع ما آگاه هستند.» بقایی مدعی شد چین نیز مانند جمهوری اسلامی، اقدامات آمریکا را بخشی از روند «تشدید یک‌جانبه‌گرایی» می‌داند.
سخنگوی وزارت خارجه جمهوری اسلامی در بخش دیگری از سخنانش، آمریکا را «بزرگترین تهدید کننده صلح و امنیت بین‌المللی» توصیف کرد و گفت: «جمهوری اسلامی ایران ثابت کرده قدرت مسوولیت‌پذیری در منطقه است. ما قلدر نیستیم، بلکه قلدر ستیز هستیم.»
اسماعیل بقایی با اشاره به حملات آمریکا و اسراییل علیه جمهوری اسلامی گفت: «حمله به یک کشور، از بین بردن زیرساخت‌های آن، ترور رهبر و شهروندان یک کشور، مصداق عمل مسئولانه نیست؟»
او همچنین در واکنش به انتقادهای «دونالد ترامپ» از طرح پیشنهادی جمهوری اسلامی، از مواضع تهران دفاع کرد و گفت: «ما امتیازی نخواستیم. تنها چیزی که مطالبه کردیم حقوق مشروع ایران است.»
بقایی در واکنش به صحبت‌های رییس جمهوری آمریکا گفت: «قضاوت را به مردم واگذار می‌کنم که آیا مطالبه ایران برای خاتمه جنگ در منطقه، توقف راهزنی دریایی علیه کشتی‌های ایران، آزاد شدن دارایی‌های متعلق به مردم ایران که سال‌هاست به ناحق محبوس شده، زیاده‌خواهانه است؟»
او همچنین گفت: «هر آنچه که ما در طرح پیشنهاد کردیم معقول و سخاوتمندانه بود و برای خیر منطقه و جهان است.»
سخنگوی وزارت خارجه همچنین مدعی شد که این وزارتخانه، از هر تصمیمی که از سوی نهادهای نظامی مانند سپاه پاسداران برای «تنگه هرمز» گرفته شود اطاعت می‌کند.
@
VahidHeadline
گزارش ایسنا:
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/75396" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBcutcswZ-3We4md8eN0PMCquPoAnzjqLbPn0pprTbMCpv_iBzwp-Nq5B_ukcRm400K48bEfGYpg4puizMB4aIPfVm3Y9hJjLil628R2E5m8Rxf9d31hmx43HpF4sXRCz7faf0RNjW2SWPwOh3StUja4vNTFkLbjlGQu10uZMddBv4v-JtN1f4qsA4DA8d4K-52WelG2UoA_iQvFXA3iS92rb1ioXxTy8rRN54_Iz66PG2NsEQJimBeEqdxGE8RGt6tubsHU9xYfapkcwyd4uZON9vnY1vZ9zZi5hd6KpFzmoex7C775FiEbHL54YvXG-cxY_4rMaaAMDVOXQ5SXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار تصاویر ماهواره‌ای که نشان‌دهنده نشت احتمالی نفت در محدوده‌ای در نزدیکی جزیره خارگ است، سازمان حفاظت محیط زیست ایران می‌گوید: «منشا آلودگی مشاهده‌ شده در اطراف جزیره خارگ ناشی از تخلیه آب توازن آلوده یک نفتکش آسیب‌دیده بوده است.»
این نهاد گفت: «هیچ‌گونه نشت نفت از خطوط لوله، تاسیسات پایانه‌های نفتی و یا سکوهای متعلق به شرکت نفت فلات قاره ایران در جزیره خارگ مشاهده یا گزارش نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/75395" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7AaV-dwWq3iTpPluTun9re3fmucsFS8fv3hx2CY7jV0MQAI56D02lvKriyD8_qyWAumlE_E66rv_toUdBlTOQSeDbA-d7YylzdqVXJCiVwo54urCBBUZlIZuB8yRGHlqAfGHgExE4nxeu6mV-VtkgSCH7wAQLIUMKTj3o44iEAM5ncgHvwuoAWcoOTBI2Vksf-g9NI-KvWRYMUu9b7vxyejkzEr2Z9sUoO7MAlUYoCg4RcclsUtVYPKY8vCq2AxvjY74BIAMiW5WBMB3rsFvIa9S6PnfSy0JR4KLf7dzKz44VPxa3Jr3sRXKsO6JnWjvhgzJGvCqI3xvPzk2kx47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گزارش سی‌ان‌ان از اینترنت طبقاتی؛ «فکر کن با بدبختی وارد اینترنت می‌شوی و می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است»
♦️
سی‌ان‌ان در گزارشی میدانی با اشاره قطع اینترنت و رواج اینترنت طبقاتی در ایران می‌نویسد، قطع اینترنت در ایران اکنون بیش از دو ماه ادامه داشته و طولانی‌ترین اختلال ثبت‌شده تاکنون به‌شمار می‌رود.
برای میلیون‌ها نفری که زندگی و درآمدشان به اینترنت وابسته است، این وضعیت ویرانگر بوده است. فراز، ساکن ۳۸ ساله تهران، به سی‌ان‌ان گفت: «تصور کنید با بیکاری و تورم دیوانه‌کننده دست‌وپنجه نرم می‌کنید و به ترتیبی موفق می‌شوید ۵۰۰ هزار تا یک میلیون تومان جور کنید، فقط برای خرید چند گیگابایت وی‌پی‌ان تا بتوانید وارد اکس یا پلتفرم‌های دیگر شوید، خبرها را ببینید و صدایی داشته باشید.»
او افزود: «بعد وسط همه این استرس و خشم، وقتی بالاخره موفق می‌شوی اکس یا تلگرام را باز کنی، می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است؛ واقعا مثل مشت به سینه آدم می‌ماند.»
متوسط حقوق ماهانه در ایران بین ۲۰ تا ۳۵ میلیون تومان برآورد می‌شود. سی‌ان‌ان می‌نویسد، اینترنت پرو، شکاف عظیم میان فقیر و غنی را عمیق‌تر کرده است.
وب‌سایت «خبرآنلاین» نوشت این طرح «جامعه ایران را به دو طبقه متمایز تقسیم کرده است: نخبگان دیجیتال که از اینترنت سریع و بدون فیلتر برای تجارت، آموزش و ارتباطات بهره‌مندند، و رعایای دیجیتال که در محدودیت شدید، سرعت پایین و هزینه‌های سنگین بازار سیاه وی‌پی‌ان گرفتار شده‌اند.»
قیمت وی‌پی‌ان‌های بازار سیاه به‌شدت افزایش یافته و بر اساس اعلام سازمان «فعالان حقوق بشر در ایران» مستقر در خارج از کشور، قطع اینترنت طی دو ماه گذشته حدود ۱.۸ میلیارد دلار به ایرانیان خسارت زده است؛ رقمی که با برآورد اتاق بازرگانی ایران نیز همخوانی دارد.
روزنامه اطلاعات نوشت: «قطع اینترنت ــ که خود منبع درآمد شمار بسیار زیادی از کسب‌وکارهای مجازی بود ــ وضعیت بحرانی و پیچیده‌ای ایجاد کرده است.»گزارش‌های داخل ایران نشان می‌دهد «اینترنت پرو» از طریق «فهرست سفید» در سطح اپراتورهای مخابراتی و بر پایه «سیم‌کارت‌های سفید» عمل می‌کند؛ یعنی برخی سیم‌کارت‌ها، حساب‌های موبایل یا نهادها از سیستم فیلترینگ کشور مستثنا می‌شوند.
برخلاف وی‌پی‌ان که با رمزگذاری ترافیک اینترنت سانسور را دور می‌زند، «اینترنت پرو» ظاهرا کاربران تاییدشده را از مسیرهایی با محدودیت کمتر عبور می‌دهد. گفته می‌شود دارندگان سیم‌کارت سفید همچنان به اینترنت جهانی کامل دسترسی دارند.
بر اساس گزارش‌ها، هزینه اینترنت پرو برای بسته سالانه ۵۰ گیگابایتی حدود دو میلیون تومان است، علاوه بر هزینه فعال‌سازی ۲.۸ میلیون تومانی و حدود ۴۰ هزار تومان برای هر گیگابایت اضافی. در مقابل، اینترنت عادی ــ که اکنون به‌شدت محدود شده ــ هر گیگابایت حدود ۸ هزار تومان هزینه دارد و همین باعث شده بسیاری ناچار به استفاده از وی‌پی‌ان شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75394" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oysl2FAo2e4fsjiIh6Woxit2O-kzX6Kt8FSH-keIedCo-9JkubJDMQ8nE-_KT1pUUmJKHADUnNUv6lq4_hmQsaXFMx9IwUz-mBcPGFdAF4MDuM80yWUXXE4_t8KIFzbqtcTNwUYazHoui5PtGHVX5-DjAxETNj67fMZka69Ov27mbdUwdDADqyPo0YeJ2PWCz6hSqIwEepbZSLrZwqGhU0JbQQGbugh1aIhmI7awlHYi9PmiX6NpjTnCJOqadv89Nogh-jPmENDS9ZqMEyFeyj_ZZhmduDyOALRAewaqdvXWCNybNx5dNgS3-NmIPY_eutj6RLNIDgYBDKpnuLPX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، صبح دوشنبه، ۲۱ اردیبهشت از اجرای حکم اعدام عرفان شکورزاده، زندانی سیاسی، با اتهام «همکاری با سرویس‌های اطلاعاتی آمریکا و اسرائیل» خبر داد.
شکورزاده بهمن‌ماه ۱۴۰۳ از سوی اطلاعات سپاه با اتهام «جاسوسی و همکاری با کشورهای متخاصم» بازداشت و به اعدام محکوم شد و حکم صادر شده علیه او به‌تازگی در دیوان عالی کشور تایید شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75393" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mscWN3gHVosFdaefIafRiY7RfE2UY9Q9jO9l3TDZrrnpZbgurOIWT6savJZ2cElZQipTRs2gC03nCVDMjVyXi-G0iOhdpuHOwhKtFIUjsgjDxSPDty2Z2TsKnpAYqNHT4EQ0AvkcJJ1czljdLD28oetn67NvMML0jnfFQIVZlKFYDvTBoqRoxn6djxXq9nT9Sb7BB1yc6achWvkNOBbktZKaQjz8uXV0DUYFUrL4v7DoE2YxNZRDl4hj5fJKgYnSo-EXvjybrdQvusbvZ7YvvZ8xEXXVtCWap76TZyBQIr_TNXlMm05S4hpEzRZD1wmQL1Fp4QpyctZnaYEr3kyADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nRbP6eRePvdIowI75rE2ijQlN1wG70dBDkJ-ok_ZggKnxJgeU_tUsKlGHPk6t6YRQC6rLIxoKwnDuFUXYp-fMZl3zSpTaeMqThM1pTTqfcEfXlrcRlAU691lkZ7wlrNXSAXK0fhFwhh4KCyz35hlkp84KUZWqKNl-EN9jyryPadihNe9Dx0eOIKOdqWfc_da9PdXXFOYwwWZASwntpBNnNYoF-RTnz0ixGJCI37fcX0tnfwqVy4BjKPwHIzbaT1IZDfaQIowkYIyEOg-FQLQUY5kMleq6yk6S5jMjSvqqGgmSzSH1bqaaDChy-6LVzcZpM49hvRab6HCg7T2pij8QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس
: پرزیدنت ترامپ روز یکشنبه در یک تماس تلفنی کوتاه به آکسیوس گفت که پاسخ ایران به تازه‌ترین پیش‌نویس توافق برای پایان دادن به جنگ را رد خواهد کرد.
ترامپ اندکی پس از این تماس، در پستی در تروث سوشال، پاسخ ایران را «کاملاً غیرقابل قبول!» خواند.
ترامپ به آکسیوس گفت روز یکشنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده و در میان مسائل دیگر، درباره پاسخ ایران نیز گفت‌وگو داشته است.
او درباره نتانیاهو گفت: «تماس بسیار خوبی بود. رابطه خوبی داریم.» اما افزود که مذاکرات ایران «مسئله من است، نه مسئله دیگران.»
ترامپ در این مصاحبه کوتاه روشن نکرد که آیا قصد دارد مذاکرات را ادامه دهد یا احتمالاً گزینه اقدام نظامی را در پیش بگیرد.
سناتور لیندسی گراهام، جمهوری‌خواه از کارولینای جنوبی، در ایکس نوشت که ترامپ اکنون باید اقدام نظامی را در نظر بگیرد؛ موضعی که گراهام در سراسر آتش‌بس یک‌ماهه بارها تکرار کرده است.
او نوشت: «با توجه به حملات مداوم آن‌ها به کشتیرانی بین‌المللی، حملات پیوسته به متحدان ما در خاورمیانه، و اکنون پاسخ کاملاً غیرقابل قبول به پیشنهاد دیپلماتیک آمریکا، به نظر من زمان آن رسیده که تغییر مسیر را در نظر بگیریم.»
گراهام نوشت: «پروژه آزادی پلاس همین حالا خیلی خوب به نظر می‌رسد»؛ اشاره‌ای به عملیات دریایی برای هدایت کشتی‌ها از تنگه هرمز که ترامپ پس از کمتر از ۴۸ ساعت به‌طور ناگهانی آن را متوقف کرد.
@VahidOOnLine
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، روز یکشنبه، ۲۰ اردیبهشت‌ماه، به نقل از «یک منبع مطلع» در واکنش به پیام ترامپ مبنی بر «کاملا غیرقابل قبول» بودن پاسخ تهران به پیشنهاد واشنگتن، نوشت: «همین الان واکنش به اصطلاح رئیس‌جمهور آمریکا را به پاسخ ایران دیدیم. هیچ اهمیتی ندارد؛ کسی در ایران برای خوشایند ترامپ طرح نمی‌نویسد. تیم مذاکره‌کننده فقط برای حق ملت ایران باید طرح بنویسد و وقتی ترامپ از آن راضی نباشد، قاعدتا بهتر است». تسنیم نوشت: «ترامپ کلا واقعیت را دوست ندارد؛ به همین دلیل مدام از ایران شکست می‌خورد».
@VahidOOnLine
خبرگزاری صداوسیما گزارش داد طرح تهران که ترامپ آن را «غیرقابل قبول» خواند، بر ضرورت پرداخت خسارت‌های جنگ توسط آمریکا و حاکمیت جمهوری اسلامی بر تنگه هرمز تاکید دارد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75391" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbrqGANubH1do50m0DtmMJtS4snWzzkIvPmAyov2pIEOc1lgG68xp8-y3NXXiDJRkh8BFpFnCfAyKlDvkHB7tp0uu9Ztj741Xat7jONlnsHrvk153wMZ28lZeLJgv_3RkOzqr8JJVSUCm37KPQER0cxzx2eOrMpycLEKP0LYiZXGMdIvU8C6r6XoUqshmrlmvu-bRIpI_xojWvoOpfm7q_tYkjGwN0ymGlm_jb7SP5wr0wZk05ulhcYArxCkkpwAU-9wqtQLfgYr7tV174lIdH-nFFLxBWPBaR30Wcx9WHy-0T8jtPgLTZH1uKYguHXzPDrlFkUXT-BFmPuYKAF0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ پاسخ جمهوری اسلامی را رد کرد
پست ترامپ، ترجمه ماشین:
همین حالا پاسخ به‌اصطلاح «نمایندگان» ایران را خواندم. از آن خوشم نیامد — کاملاً غیرقابل‌قبول است! از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75390" target="_blank">📅 23:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edaUgUZO-EjgE-jomHoQk1lxr_3ybfgo-_SIWfTAVDKf6jvWUA4SpK0h2OhZCDkxccMFchq1i0qF_ap_M4UbKCyGyvdn3u58t8wCbz0CSq1ZjyE6Yc5Qt_z9rQjwL4icmDXIDg5HxwJ9TL1pqsNyKQ80IBOToTtzfWZBum1OIHSfyv1fhm_QNyvx-kCFjtqrUxC23ICTHf0O1nnpuDE4xCyGt-QpqYMUxz3JghP4cmy1_afGaGyDHi0E7fG6vHs82Mua_88dnIBcDs15hILIyn9O5-wX_Th83P2zSvy7Ch_90623ribXl4bc6KaxwiA3Le1gkV_f3qJhTs2a0VVI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال، شامگاه یکشنبه ۲۰ اردیبهشت ماه، به نقل از منابعی آگاه، جزئیاتی از پاسخ ایران به پیشنهاد صلح آمریکا را منتشر کرد.
به گزارش این روزنامه، پاسخ ایران که از طریق پاکستان به‌عنوان میانجی به واشنگتن منتقل شده، همچنان اختلاف‌های مهمی میان دو طرف باقی گذاشته است.
به گفته منابع وال‌استریت ژورنال، تهران حاضر نشده از پیش درباره سرنوشت برنامه هسته‌ای خود و ذخایر اورانیوم با غنای بالا تعهد بدهد.
ایران پیشنهاد کرده مسائل هسته‌ای طی ۳۰ روز آینده مورد مذاکره قرار گیرد.
مقامام‌های ایران همچنین برای رقیق‌سازی بخشی از اورانیوم غنی‌شده و انتقال بخش دیگری از آن به یک کشور ثالث اعلام آمادگی کرده‌اند.
وال‌استریت ژورنال گزارش داد تهران با برچیدن تاسیسات هسته‌ای خود مخالفت کرده، اما در عین حال آمادگی‌اش را برای تعلیق غنی‌سازی اورانیوم اعلام کرده است؛ تعلیقی که به گفته این روزنامه، مدت آن کوتاه‌تر از توقف ۲۰ ساله پیشنهادی آمریکا خواهد بود.
بر اساس این گزارش، ایران در پاسخی چندصفحه‌ای به تازه‌ترین پیشنهاد آمریکا برای پایان دادن به جنگ، خواستار پایان درگیری‌ها و لغو محاصره کشتی‌ها و بنادر ایرانی شده و پیشنهاد داده است تنگه هرمز به‌تدریج به روی رفت‌وآمد تجاری باز شود.
وال‌استریت ژورنال نوشت ایران در مقابل، خواستار تضمین‌هایی شده است که اگر مذاکرات شکست بخورد یا آمریکا در آینده از توافق خارج شود، اورانیوم منتقل‌شده دوباره به ایران بازگردانده شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75389" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLPMLmMQ74yVg0u7G8kq-8R8w1GcSxEL2oHnQwtmsxmEpDWtniQ2s9W6Z890aOVI_xLa67A57Rg_NaDg1yLPYBQhEbN_QppscNt3uJdxMpz7bSAmeeK_Hzdc26aCJzhkxeiedsIFOQTWq1lqiv0sPDhZ-u_z6m0uxzEcvSgnou_gMqKxceyfW1tVzTb1KAYuW0aop6dqV0iDrDMZKz4dRknAU3eMARS0fqIhy2TutVvouK32C4xjJqsg2u7bTkO0myHyj0aSL9jsfW9QdT2ax2yULSKHK0673hdDYE7V2uEv5rMz3-ayjkf_kIgGYKTrDzhRkKFQVXmpm5kZ6UjGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران شامگاه یک‌شنبه با اشاره به شنیده شدن فعالیت پدافند هوایی در اندیمشک و شمال دزفول از سرنگونی «پرنده متخاصم دشمن» در اندیمشک خبر دادند.
شهروندان نیز یک‌شنبه ساعت حدود ۱۰ شب از شنیده‌شدن صدای پدافند در این شهر خبر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75388" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#دزفول
#اندیمشک
پیام‌های دریافتی از شنیده شدن صدای پدافند:
پیام ساعت ۲۲: دزفول حدود 20 دقیقه صدای پدافند میومد
دزفول وحشتناک صدای پدافند اومد.جدود ساعت نه ونیم
سلام پایگاه چهارم شکاری دزفول از ساعت ۲۱:۳۰ تقریبا یه ریز پدافند فعاله
پدافند پایگاه وحدتی دزفول فعال شده از ساعت ۲۱.۵۰ تا الان ۲۲.۱۷
فعالیت  شدید پدافند در اندیمشک ساعت 22.15
اندیمشک
ساعت 22:19 امشب پدافند فعال شد در حد 30 ثانیه.
یه صدایی میاد انگار پهپاده
سلام، اندیمشک ۲۲:۲۲ دقیقه چند دقیقه ست پدافند ها فعال شدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75387" target="_blank">📅 22:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q3lGcaffy_PaTVQkRM1hHXPdP9UwvC5zv9bpjtYxhasL79zctBTn_7rcB6UyytU8w6zeCfSf6kO2UafmIQLM2ev--bpX_8Jkzl9ec-PS49AXANDWvQTv1Fhp69gKLgYxy8DGt0JxLtMtdB3py39X2B8fKpjQMYTt7jNcnE_vTaZvbZ_cyxmxSpnziF9FfHb90QXLBWVKM54f2wYMsjOj6M-3N0TqGauxCe1XgwpvSZCHh1IGZoJbneccpR_0V1TNPFr6SrrVh-kNHNamFxYBYgk_8IZ6HlwVIor7qR_U3sOoqWnayx-hOV06t4DsvswXKZLXGCy-1DdEwccWaOSbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آن‌ها دیگر نخواهند خندید
پست تازه ترامپ پس از آن که جمهوری اسلامی گفت پاسخش را از طریق پاکستان ارسال کرده. ترجمه ماشین:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است؛ «تعویق، تعویق، تعویق!» و سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به گنج رسید. او نه‌تنها با آن‌ها خوب بود، بلکه عالی بود؛ عملاً به طرف آن‌ها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه، بزرگ و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار، و ۱.۷ میلیارد دلار پول نقد سبز، که با هواپیما به تهران منتقل شد، مثل هدیه‌ای روی سینی نقره به آن‌ها داده شد. همه بانک‌ها در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند. آن‌قدر پول بود که وقتی رسید، اراذل ایرانی نمی‌دانستند با آن چه کار کنند. آن‌ها هرگز چنین پولی ندیده بودند و دیگر هم هرگز نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما پایین آورده شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آن‌ها بالاخره بزرگ‌ترین ساده‌لوحِ همه تاریخ را در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی پیدا کردند. او به‌عنوان «رهبر» ما یک فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
ایرانی‌ها ۴۷ سال ما را سر دوانده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای خود کشته‌اند، اعتراضات را نابود کرده‌اند، و اخیراً ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند و به کشور ما که اکنون دوباره بزرگ شده است، خندیده‌اند. دیگر نخواهند خندید!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75386" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXzl7bdVSa-3j5ZylNJr180PF_TZNk4-1c1v2qAF05OHtODjvvdntoVYTNf0wJsr4sxnwNvZ0CFpK8ZYSnVeCzZbFQnrYec_XTtuZMoY9ARz78FGdtpROFa03BiLahsJUecy8PsWLxF32MUDDWEekvul4BgkidZiouiGnssa9dThthQctY9NRp1KArSCrPi_SPmPO_M4HqFBP18ipBc-Atkd9uYe_XNg5InGLrDWl78fe0XyRtilWPsgu1pM5AiVYVI7fABFtU30jrgoW3dlSdZgiMJ8J0GiWEdRKfX2DYIdbIIHTH2zTdAvJgCIdCOTqSTfGGJKuAAJhnZUsqME7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در بخشی از یک مصاحبه که قرار است ساعاتی دیگر مشروح آن پخش شود، گفت که ذخایر اورانیوم غنی‌شده ایران باید از بین برود تا بتوان گفت جنگ آمریکا و اسرائیل با ایران به پایان رسیده است.
او در بخشی از گفت‌وگو با برنامه «۶۰ دقیقه» شبکه سی‌بی‌اس گفت: «این [جنگ] هنوز تمام نشده است، چون مواد هسته‌ای، اورانیوم غنی‌شده، باید از ایران خارج شود. تاسیسات غنی‌سازی هم که وجود دارد باید برچیده شوند.»
او همچنین گفت: «ایران هنوز از نیروهای نیابتی حمایت و موشک‌ بالستیک تولید می‌کند. بخش عمده‌ای از اینها نابود شده‌اند اما کارهایی باقی است.»
آقای نتانیاهو در پاسخ به این پرسش که این اورانیوم چگونه باید خارج شود، گفت: «وارد می‌شوید و آن را خارج می‌کنید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75385" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X8uqz5MiZ8Auwjb_4iZBugcHM-RwJ7AYgDAqoZCPN5vv3fkANXl86qU7Qt3lFFkyO1M7GjUVzy0B160YIJ15H_EEzfv_BlK2hG9TUYWCfY2DJhggOnaX7-ltjY_-2OPp2vKmKYdBtrSLogQfWW__GdUpJqCvyiuN_vZOl87IqccRhDr4TO_rmVnJuaJy4IuLcX1kZwK78c4_e-l8FXAY9SLEKAZPovmPaDn-p0s6Nuo0wFUTtDZdhwqY9aqxWkWFd8YYgDTqcUYWWSkG7kidgnMeW29gqF1g7QHw5t6UI7a5zZk7_8_zpE_NKTwCCcIlRkdMHGUeEl2fhSEnw_rZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Afkham_minus
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75384" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpcxRKBpIHPQLqGr_pgi3oi8VlfurxF2F4F80Sc4w90QDGtrvClLimsSEJI--zAFRQ33lFEr4jjxe-d1D8m9D40nRKJeIwVPoclfeUjBEmZ3WnWCjMbirDROgBhgyBH6KEf9r9o2vibWzREIOcJoDtGzAlsgVTSqbMPErkVYAQCCz0Wrpo0izLZHyDcmGYyKuqiI-dKitDhnW71UAltU5d5mAPLUx09u-zAkP0Ec-Y76pJUVc0kosblrfTt3tKaUIGDmIJC7yOc4OoDWjjX82WinL4d8uniP_VYJmDy9yZWYKQkodZQ5hKZjL_iuibQEEX_Yut3yTlQ7Xugq6cDrSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیم نادعلی، معاون فرهنگی سپاه «محمد رسول‌الله» تهران گفت: «در جشن بزرگ پیوند آسمانی زوج‌های جان‌فدا، خودروهای جیپ جنگی برای جابه‌جایی عروس و دامادها در نظر گرفته شده که با گل‌آرایی، پرچم جمهوری اسلامی و تصاویر رهبری تزئین شده و زوج‌ها در این خودروها در مراسم حضور خواهند یافت.»
او افزود زوج‌های شرکت‌کننده قرار است با «ماشین‌های عروسی به شکل جیپ نظامی» و «خودروهای نظامی گل‌کاری‌شده» در سطح شهر حضور پیدا کنند تا «فضای شهر را به یک شکل هنری و نظامی» درآورند.
به گفته او، هدف این است که نشان داده شود این «زوج‌های جانفدا» جان خود را «زیر پرچم جمهوری اسلامی تقدیم این نظام خواهند کرد» و «از هیچ چیز نمی‌ترسند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75383" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FhICTORbVHV66_F8oaoZznCH6Ewg09AWeHiqtTFoSe_q2NvSSYuxKZQJD0LxiLvZLlEvynM_8IT24NOtqC-2voL-jTLBYdn0o2VaqYINO0DKElANHehPa1gNiAU1_ogA3OrObu5NDjChj1N7qbTc_MJcYZZNe3YoJX3wWTOGW4lcm1gtByKki2GY3iaNy988IRN-XstBn98iqstc8_g-ErRAPlqaUoC97qbZ8lw9W83ukqu_yUSekq05h4cMeC8TLsUwbntiXfMnDy9bSqILSwvB_Rom4O27ctvYfkXh01zI8SkaWE_zan7MMggbAaIOVr6KBFIWWYOX9P13-awU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dRJDCZ_9vCIRf_HqPsJ9jReRh21rCDjuv8cWjpIl3EAdrsXoWyygEnbHyNRcksS-64K_T7iViU4SvIZDeWml2pvpgS2ix9WoPJbxN5IW7K65hTX6zdECk5EiQCCFnqbaOUUe1tnF9SgFxHJEqcfKZqCzivKDlEMqryMXJMwJKXQxPfvE5-MtThTZYyKrweh9tkE5NCQAj8eSbxKLNfGT76HpfEfbyWqhn2utRghihWTr4wXnmhoKaOX0Qgri1zEk1YNdU_dFB_JZvGlPT0n7Dd0DTA2Q6J1pHJYbrYJCagetmo09adIhzxFBKJ03h9fNg9cVPvdhocXtG9Vg6tYJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i_ULqOupFyWQv2hO2__X-eBUm6DKYV5It0QNXND0Z949FB_cd_CfnuCn_e5SjD9nZ6QRXKgWfWKZ5cZyIxB2aJL0lcxNZcdrZFZ3Zt1HchH6YGkMrwNDjMMG0dT7dnq99bhhW6FAikYwONVx_RwVFwuKRj1XmKyLWp_-ZiLxw6pL-EagbYWbpH1QUKyslTyslPe0m_dzIvAZofxHvRJPz59c71otdnj9r6QJAa9Z4xF36iGUUoA1a8KPyK89fCGvK44piPiUwrR_A7XAudBZhkBSYOY3euFFii1EwWgGpFPumPs-g5Shm4-sj6auQ2fZH0mdTGmynCg0iS2wV_iXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l_RskToDg2T2FgmysHs5iRkPWIXkT0lxy-JGU5fkqmVJRABMTbSI-KuleC54upHWZOREair8MXfy5Zvwp0JWvFbFKwSh0Fes6dYdqWJC0tHQ10U4fySkX3F3UdZc7cY6kXprNHCVGiS1RdGnJN1Nfzpq7UE0qJEbUlJ29fjUYcODxEbEj6vcdRqusHlACZbibte5N5tvpS1yKn6N1cnkUw_iCJYUqtRxXKszyRcWCWXAlTlsITGhAuebKUuxrUp8hHFwJHYuducCkGBjM7ltJ3oVcjXspD-3sVX20rS15Mj3mgFMlLdPenOb9LIJ1_R8P2sAfrLEFIAe_0LlgQaQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Aw12ft15zMBYPYocKJlZgXOop36NvirPLbBFk_gD6p6kHFQbLUUK00bdmTaY15rz7rfZG8Q_sDU9tGR09uIs2eF2Uj2AWgN3z2hf3yh6WHcMsfV_gvDEBu-1i8tKjilHTedLXIBAYTU9xzM7_uCozFiAcV9SKEV50F_d19n9-n6oI0IO5ULIPkliQdL4tSTEPauBMwhT8PTDg7EdBEJdv1zpIL4-cHfZ-fDJaDdnH2bccANVFEPVTGGKvE_O9G1uw-lSa_LwSe-V6ZCcifmABFTd9vl9Et2pYJQi8bDdhRB2BI5aL6a3UnUaGpyDol2EWoa4nLyKQgUmJ7GaCGsGDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید عملیات نظامی در ایران تمام نشده و ارتش ایالات متحده می‌تواند اهداف دیگری را نیز هدف قرار دهد.
دونالد ترامپ در گفت‌وگویی با شریل اتکیسون، مجری آمریکایی، که هفته گذشته ضبط و روز یکشنبه ۲۰ اردیبهشت پخش شده است، در پاسخ به این سوال که آیا عملیات رزمی در ایران تمام شده است، گفت: «نه، من چنین چیزی نگفتم. من گفتم آن‌ها شکست خورده‌اند، اما این به آن معنا نیست که کارشان تمام شده است. ما می‌توانیم به مدت دو هفته بیشتر هم وارد عمل شویم و تک‌تک اهداف را هدف قرار دهیم.»
او با اشاره به این که در حملات آمریکا و اسرائیل طی جنگ اخیر «احتمالا ۷۰ درصد» اهداف مورد اصابت قرار گرفتند، افزود: «ما اهداف دیگری هم داریم که احتمالاً می‌توانیم به آن‌ها حمله کنیم. اما حتی اگر این کار را نکنیم، سال‌ها طول می‌کشد تا آن‌ها دوباره بازسازی شوند.»
به نظر می‌رسد اظهارات آقای ترامپ پیش از ارسال پاسخ ایران به آخرین پیشنهاد آمریکا برای این توافق انجام شده است. هرچند که او پیشنهادات قبلی ایران را رد کرده بود.
رئیس‌جمهور آمریکا در مصاحبه با شریل اتکیسون همچنین دربارهٔ اورانیوم غنی‌شده ایران که در عمق زمین و در تأسیسات هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون شده‌اند، گفت: «ما در مقطعی آن را به دست خواهیم آورد… ما آنجا را تحت نظارت داریم.»
ترامپ اضافه کرد: «من چیزی به نام نیروی فضایی ایجاد کردم و آن‌ها آنجا را زیر نظر دارند… اگر کسی به آن محل نزدیک شود، ما مطلع خواهیم شد و آن‌ها را نابود خواهیم کرد.»
او بارها اشاره کرده است که توافق با ایران باید شامل تحویل ذخایر اورانیوم غنی‌شده ایران به آمریکا باشد. تهران چنین درخواستی را رد کرده است.
@
VahidHeadline
رئیس‌جمهور آمریکا گفت: «ما نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد، چون آنها دیوانه‌اند. نمی‌توانیم اجازه دسترسی هسته‌ای به آنها بدهیم. اوباما این کار را کرد. اگر من توافق هسته‌ای ایران را لغو نکرده بودم، الان سلاح هسته‌ای را داشتند و الان علیه اسرائیل و خاورمیانه و شاید حتی فراتر از آن استفاده می‌کردند. می‌دانید، آنها در واقع موشک‌هایی دارند که دیدید می‌توانند به اروپا برسند.»
از آقای ترامپ سوال شد آیا این درست که عملیات رزمی علیه ایران تمام شده است.
رئیس‌جمهور آمریکا پاسخ داد:«من این را نگفتم. من گفتم آنها شکست خورده‌اند اما این به این معنا نیست که کارشان تمام شده است. ما می‌توانیم دو هفته دیگر هم وارد عمل شویم و هر هدفی را بزنیم. ما اهداف مشخصی داریم که احتمالاً ۷۰ درصد آن‌ها را زده‌ایم اما اهداف دیگری هم هستند که می‌توانیم بزنیم.»
آقای ترامپ گفت حتی اگر هم این کار را نکنیم، بازسازی سال‌های زیادی برای ایران طول می‌کشد.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با سی‌بی‌اس نیوز درباره اورانیوم غنی‌شده در ایران و جنگ علیه جمهوری اسلامی گفت دونالد ترامپ به او گفته می‌خواهد وارد آنجا شود و به نظر او این اقدام از نظر عملی امکان‌پذیر است. او افزود اگر توافقی حاصل شود و بتوان وارد شد و این برنامه را برچید، این بهترین راه خواهد بود.
نتانیاهو از پاسخ به این پرسش که در صورت عدم توافق چه رخ خواهد داد خودداری کرد و گفت برای این موضوع جدول زمانی تعیین نمی‌کند، اما این ماموریت را بسیار مهم دانست.
IranIntl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75378" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_fynmDKbQz-LbcQDeoHxQMwubZKTYSc6BKYqc-ytYH4IrwVI9wOUyi2fN0QpaD4mUGS61RmDMZR0ClpBScmGBe-JNyUv41yo_cQq645U_vot7kmVSD350ZvOAWzMfuwt1_nEG8MZybAXTSNEvn70gIcNGwHJOrDlp1q9A-2yrob2rWBVBKfqDAydm4FUIx9kHFH1CuF4wLJhOjRqHvle4amSvqfkhFzoEVhVBUvijO4JqvV1_Rrxq1g-mFFQF7R-uk80tLt2iBrlLtovefP84O8sj5S2M35pRIH8ASii0MHREKYmtKRMXEeV7BCMLCvH4bn-B2fhBL4TnKs1WSj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایرنا، روز یکشنبه ۲۰ اردیبهشت ۱۴۰۵گزارش داد پاسخ تهران به آخرین طرح پیشنهادی ایالات متحده برای رسیدن به توافق بر سر پایان جنگ، برای پاکستان به عنوان میانجی مذاکرات ارسال شده است.
ایرنا بدون اشاره به جزئیات بیشتر نوشت: «بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.»
وب‌سایت اکسیوس و خبرگزاری رویترز، چهارشنبه هفته گذشته گزارش دادند که واشنگتن و تهران به یک «یادداشت تفاهم یک‌صفحه‌ای» برای پایان دادن به جنگ نزدیک شده‌اند.
رویترز نوشته بود در این تفاهم‌نامه حتی به تعلیق فعالیت هسته‌ای ایران یا بازگشایی تنگه هرمز که از سوی سپاه پاسداران بسته شده، اشاره‌ای نشده است.
در مقابل، روزنامه وال‌استریت ژورنال گزارش داده بود که در طرح پیشنهادی آمریکا، تهران باید ثابت کند که به‌دنبال سلاح اتمی نیست، تاسیسات فردو، نطنز و اصفهان را برچیند، فعالیت زیرزمینی هسته‌ای را متوقف کند و همچنین بپذیرد غنی‌سازی را تا ۲۰ سال متوقف کند.
رییس‌جمهور و وزیر خارجه آمریکا روز جمعه گفته بودند جمهوری اسلامی تا پایان همان روز قرار است به پیشنهاد ایالات متحده پاسخ دهد.
@
VahidHeadline
ولی جمهوری اسلامی به جای جمعه، روز بسته شدن بازارها، صبر کرد یکشنبه پاسخ داد که ساعت ۸ شبش به وقت شرق آمریکا بازارهای مالی هفته کاری رو آغاز می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/75377" target="_blank">📅 17:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOtIWc772PFG4RK-xcGlbQ9tHKCgWssasNPjSgZ0Wady3azpola9BYG09qLSxPYDivEzFsEoAyaG5CKprUaxPumti5U5pJf-SVdRMJgH7C4c5VH3F--xpQDv662Ao_zbaw_mUx-MyE2LmgsHYWddTSns_WATmCy3MKPiQjOn-5p7DEzdD3kmmI7JRWip1Fz8SFDL5K8mMqWoNLdr5cGB9hf701Ogi2V7o_bpYuDMXGdZyyb8vHTnl-V4UN_OlWaTaS5Pw9aUpWXUDrf0D0cd2MsMvyToNGcrk3Yr8GtZkbAeBkZRXI8U-mjtdeusMk5EX98C-VJ1hbgI62m-7Zceyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی روز یکشنبه ۲۰ اردیبهشت اعلام کرد که سامانه‌های پدافند هوایی این کشور با موفقیت دو پهپاد پرتاب شده از «ایران» را منهدم کردند.
این وزارتخانه تاکید کرده است که از زمان ««شروع حملات آشکار ایران، پدافند هوایی امارات متحده عربی در مجموع ۵۵۱ موشک بالستیک، ۲۹ موشک کروز و ۲۲۶۵ پهپاد را منهدم کرده است.»
وزارت دفاع امارات همچنین گزارش داده است که از زمان شروع حملات آشکار ایران، تعداد کل جانباختگان نظامی به ۳ نفر رسیده و تلفات غیرنظامی هم ۱۰ نفر از ملیت‌های پاکستانی، نپالی، بنگلادشی، فلسطینی، هندی و مصری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/75376" target="_blank">📅 17:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojC9C1OVrJE8gmkp5fLCeIHJaLExw9lHn-4Bz7gIcV7z_f8U3Si7Wrm2FFstmg1Zem9CGAvljGFs648jTAHQAlYFq9VRuMnR_HhRJOsslKgVEVQ9HHp06CmgJfjR38PQNTiW7rAjXEwGExVO5Q2zEQlQJJZGd5xRfM6x_ZoiTjkwxdBmfRkpNGiw7TSjhEiT48sUuT9NmL-6O1akwdsj0qC7I1wV7SDgepvOG1Auxmj8q_eWfcENc5nWjZkFCV5nIojcCZSja2eOd_q5PjM-qZF5mC5151yQzk5TsuT4B3PqMmYti0PbbceXrHWLGYB8JZfEEvGHsyVsl8cuaT6Huw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی گفته‌اند علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، با مجتبی خامنه‌ای دیدار کرده و گزارشی از آمادگی نیروهای مسلح، از جمله ارتش، سپاه، نیروی انتظامی، نهادهای امنیتی، مرزبانی، وزارت دفاع و بسیج ارائه داده است.
بر اساس این گزارش‌ها، عبداللهی گفته نیروهای مسلح از نظر روحیه رزمی، آمادگی دفاعی و هجومی، طرح‌های راهبردی و تجهیزات لازم برای مقابله با «دشمنان» در سطح بالایی از آمادگی قرار دارند.
این رسانه‌ها همچنین نوشتند مجتبی خامنه‌ای در این دیدار تدابیر تازه‌ای برای ادامه اقدامات و مقابله با دشمنان ابلاغ کرده است. با وجود انتشار متن این خبر، رسانه‌های جمهوری اسلامی تصویری از این دیدار منتشر نکردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75375" target="_blank">📅 17:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeaWFduTomq7DVPLBuIgLtjdY03zKLB49rHfIaZOGlLGJm3vgfty2oKuXQPWJv4gHTeRbzUBzsDUgV7klsCb_LBMqxkakkfPNNzSxXkLD_Ozpe_l01uE_JpeOJ4tcutbnHyKPNDJXwAieD3Mdew5n2JZOF8gezy9hricomrHaqKUaWSFGi2jZXxxScWBXHWb6Sbb850ZGiD7Cb-4CdY3wcARwtOf1FaNiHbBn9IafC_sESapafMF0Eh3krIrEm5ZMsGjdu8nxISqB0J0oOO5RTXsIScwaEKg8q5a52K_eePT0m2GxuppAWtRRkeOdfb03NTUSJ_-WxEtPeVsQEIO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران درباره کشتی باری هدف ‌قرارگرفته شده در نزدیکی سواحل قطر، به نقل از منبعی که نامش را فاش نکرد، گزارش داد این کشتی با پرچم آمریکا تردد می‌کرده و متعلق به ایالات متحده بوده است.
سازمان «عملیات تجارت دریایی بریتانیا» (UKMTO) صبح یکشنبه گزارش داد که یک پرتابه به سمت یک کشتی باری  در ۲۳ مایل دریایی (۳۷ کیلومتری) شمال شرقی دوحه شلیک شده است.
بنا بر این گزارش یک آتش‌سوزی کوچک در این کشتی رخ داده که خاموش شده است و تلفات جانی نیز نداشته است.
این خبر در حالی اعلام شده است که مارکو روبیو، وزیر امور خارجه آمریکا روز شنبه با محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، در میامی دیدار و گفتگو کرد و شراکت دو کشور را برای بازدارندگی در برابر تهدیدات و تقویت ثبات در خاورمیانه حائز اهمیت خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/75374" target="_blank">📅 17:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0N8tN82lZDhHFUcTOrpz7itxBbfJmVP15chKeNRQXKyib6NhZ5iqvHLm_P9XiDpRGMkOhwi35lmbuFObAhTFxcGIsaQBLVOWd-SoOrvSEHIpDKcueTxAeZ89cYk2hIViabpzBXoJmlEb0Sh3fN95rckSaR-cdWNOweXGxKh_ICnsuiZtEuEJuwTfmpJf1rJNrLkV6WCmB-hSRf9JhK_D5MO2arXq3OJKrbouqhYVY__QuTynzTJOj7qhn0TYW-I_eBGWiFIl8Ir7k0UO6BcAYbIxm8poV1IiQyMmbobTwiJdeOvWlJa63zG4ut1bQ0fEzOpfR4OICJxoQK054Gj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
خبرگزاری فارس می‌گوید «یک نفتکش حمل‌کننده گاز طبیعی مایع متعلق به قطر به نام الخریطیات» با «اجازه ایران» از تنگه هرمز عبور کرده است.
بنابر این گزارش، این نفتکش «روز گذشته در دهانهٔ تنگهٔ هرمز دیده شده بود و پس از آن سامانه موقعیت‌یاب خودکار خود را خاموش کرد.»
به گفته فارس، «این نفتکش که مقصدش پاکستان است، نخستین نفتکش غیرمرتبط با ایران است که از نیروی دریایی سپاه اجازه عبور از تنگه هرمز دریافت کرده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75373" target="_blank">📅 17:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK5r-kL7A8jKRRrM3V68hNvQxActcxE-pGHndM8QhAoWEKXFCdblaE4nMgsY9KksvEO5_MGxDY0Pq2YP7_agUTggea_OfWk02p4AkKXWp25oXRv7sqdUpRDAq2AwTRgmkaCWqP-QIDVDrZfFh6jUXQPWzsdNWLQksNkTIOK1EeVUmR5u-5MpPQo7EojEEQYvS_iLqZNO5gnJSPfaCQ2yeb4J_6egqYKUtJmWtLhNaQe4Nzugc2PBXaJk9dinkVY7fEyfwnl67xP20hY6C0-t4BO7QYqYZoaFBVlF--c1LyaK8nSUAhfNECVAYpt4aZ5EXvp50B_rJtNSUhItxf8KNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخل ایران روز یک‌شنبه به نقل از مدیرعامل شرکت پایانه‌های نفتی ایران هر گونه آلودگی نفتی ناشی از تأسیسات جزیره خارک را تکذیب کردند.
او گفت: «به محض انتشار این اخبار، گروه‌های متخصص اچ‌اس‌ئی و اداره شیمیایی و آزمایشگاه، همه منطقه را پایش کردند اما حتی کوچک‌ترین موردی یافت نشد.»
خبرگزاری رویترز گزارش داده بود که تصاویر ماهواره‌ای ثبت‌شده در روزهای ۱۶ تا ۱۸ اردیبهشت، لکه‌ای بزرگ را در آب‌های اطراف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، نشان می‌دهد که به گفته کارشناسان با «نشت نفت» سازگار است.
بر اساس این گزارش، لکه‌ای خاکستری و سفیدرنگ در غرب جزیره خارک دیده شده که به گفته یک پژوهشگر «رصدخانه منازعه و محیط زیست»، مساحتی حدود ۴۵ کیلومتر مربع را پوشش می‌دهد.
به گفته عباس اسدروز، «طبق اعلام مرکز بین‌المللی «میمک» به نمایندگی از سازمان بین‌المللی دریانوردی هیچ‌گونه نشتی در زیرساخت‌ها، مخازن ذخیره‌سازی، سیستم‌های اندازه‌گیری، اسکله‌ها، خطوط لوله این منطقه و کشتی‌های در حال بارگیری وجود ندارد.»
اسدروز توضیح نداده است که لکه موجود در تصاویر نشان‌دهنده چه چیزی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75372" target="_blank">📅 17:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBFOwgXbWywzcuMp0KRiJ70GUqesCdmtF1yj7KJ-SAsJCjE1f2S9Oup3xqZ77m2R5LupuWwrRas67uH-hYuorZMp3Ar_CYV-oxwFrXnIKlsUeRy1dLnIxGKNMAD4YcLwAg6JA7ncxPXQNZ5zLSs6UEBPZsOdQeHloj1ZZ55beRysXMBNTAk0-FBLIgcwP_baep79v5ry6z2slyTUYQglykCbQlFgUgfLg451yItRikbVu5TlngLvChjJNEisFa7TWPcb7rnqZCqXtvGqt4-FbrXF1eDthYnMpT8xeB2GbkHw7ENnKczV3Ebv91oj9JOKWcZJzVWnQB0LbCJg-jRdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «وال‌استریت ژورنال»، اسرائیل در اقدامی بی‌سابقه یک پایگاه نظامی مخفی در بیابان‌های عراق ایجاد کرده است تا از این طریق عملیات هوایی گسترده خود علیه ایران را پشتیبانی کند.
این پایگاه که پیش از آغاز درگیری‌ها و با آگاهی ایالات متحده احداث شده، میزبان نیروهای ویژه اسرائیل و یگان‌های امداد و نجات برای خلبانانی بود که ممکن بود در جریان حملات سرنگون شوند.
طبق گفته مقام‌های آگاه، استقرار این مرکز لجستیک در فاصله ۱۶۰۰ کیلومتری از اسرائیل، نقش کلیدی در مدیریت هزاران حمله هوایی تل‌آویو علیه اهداف نظامی رژیم جمهوری اسلامی در خاک ایران طی هفته‌های اخیر ایفا کرده است.
این گزارش فاش می‌کند که مخفیگاه مذکور در اوایل ماه مارس و پس از گزارش یک چوپان محلی درباره تحرکات مشکوک هلیکوپترها، تا آستانه لو رفتن پیش رفت. در پی این گزارش، ارتش عراق نیروهایی را برای بازرسی به منطقه اعزام کرد، اما نیروهای اسرائیلی با اجرای حملات هوایی سنگین علیه سربازان عراقی، مانع از دسترسی آن‌ها به این سایت سری شدند که در نتیجه آن یک سرباز عراقی کشته و دو نفر مجروح شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75371" target="_blank">📅 01:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VJiuzHKnd7BjuIXkZoisI6lbkOuyAIdmQWmAmbIGWXSCOcLysaUnEKXJfNJsXSCDz8x-hbGgW-Q7YZxTHYZY5pYxfwfclE89uYEx2vUY1CAzZsUILiaOBZIJV_0eRWvDqc-7pVmD3xdH-HS6Y5mrQ9Hp18ln3u9BiQnpytWDGhq0cjFHz9IwmVxy7-foMvqIyZiXJVqkIWcn_KQYo0eXKAj24lav1WBlpPQj2FnKn_p78-1RjhCGB8_ckmyD5x48qPdKmt5hVl69tssVc7qbEIMjx5WoDhQTAK273PS6QCjXgrK_VBvkKjBAZHCvdSLAhW3ZCSF6qC4SaRLKsZLxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cw0SwmlBseCENfsONh78_srwtfy3KKR172sqgL2C6bfrfs-q8Q9yajwj_V-R3SAHEGWqLeCaVhJgljBJqSdDdZh4u528yS3D1t1ugdneSrz35a4LmG7svX6oiixPZhnOTSw54ciYSInSIN89EgIKm2l9N0bRfh_UDFo4UjvpV7cSKqxykLna18sowXPoihP6grjZhKOYPkcMPrrozzwu9PpCqzsCefAYlA9DWjxJ0lbt1cb9MqBAoSgrlsedp4SKhVxCtHV0clFdOAtN8bA7x3kQ-dZwkVnrugd63lMvDLNp3TzfMKF3mVzUF2Upmj6cJDal51u4EJx8FQQFDn99lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ساختگی دیگری که ترامپ در صفحه‌اش منتشر کرده
:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75369" target="_blank">📅 01:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iwrGu_3p75Zl8aGmw7gE8gZ0QJfWO710y4NOraoI_uwUn-Fa-6Zycinwo958pRlLBPO2m7Xl29byB8zySY2R2GdpicHth6sH8bqlSq2SJsbyVTgmrDiGBotenNpNRqIrsyNberFzzDCGR0YMK6e2LasDZJqgUJUk3ar3K5WOMmfHghmAAciV2pEFtkp0hrZCbW23D5_vLa3iaEZNXrt3-UWr9OcdAq3KA2A0gK07BwQprrxkh_4dmNKHsPZb1e5_0rrkteVJ1nysjOibhMDm-jXJvBNl_gamEDDlK5fMfxllL1rEBTGjd81gO_dT6Kmg5zbGx6iBRgnnn_a5O_smcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75368" target="_blank">📅 23:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI5WMhNLu9Lu9XPwWhDP8hs4fpz4cTuN28a-W5HRlj58t9g16r8qqTvXmxEuEnZREdbEkoaurEFRuVFd34Ycg6vcQ_u1w160Di1u-7u87znkltXo3dlxvxaB1wo4xVlyc7UQxmhkdrKhSvVOojfF9ReeFoWoFWWUVCxkjoWHA24i-a4BwFnzJa24SWuTyBsF3bZGoeNi403bhkhEhYd5GAAIHoeG2BJE4Wlz3bYGtwNp-WT2MBWeh8nvnIdiew6NI5L5_WfTjINf1PZ_2MxgQLhnRx10Ve0lZ_rMRGlPpUSRNAo_qV57pBQanN954li_8MXjtsflVbkWVlhwKjEZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، با اشاره به کابل‌های فیبر نوری عبوری از تنگه هرمز و تهدید به اختلال در اقتصاد دیجیتال جهان در صورت آسیب به این کابل‌ها، خواهان اخذ هزینه از شرکت‌های خارجی و الزام غول‌های فناوری نظیر متا، آمازون و مایکروسافت به فعالیت تحت قوانین جمهوری اسلامی شد.
تسنیم نوشت: «کابل‌های تار نوری زیردریایی عبوری از تنگه هرمز روزانه حامل بیش از ۱۰ تریلیون دلار آمریکا تراکنش مالی (شامل پیام‌های سوئیفت، معاملات بورس و تبادلات ارزی) هستند.»
رسانه وابسته به سپاه در ادامه خواستار «اخذ هزینه مجوز اولیه و تمدید سالانه از شرکت‌های خارجی، الزام غول‌های فناوری (متا، آمازون، مایکروسافت) به فعالیت تحت قوانین جمهوری اسلامی و انحصار تعمیر و نگهداری کابل‌ها از سوی شرکت‌های ایرانی شد.»
فارس، دیگر وابسته به سپاه، نیز در گزارشی نوشت که ده‌ها کابل فیبر نوری زیردریایی که آسیا، اروپا و خاورمیانه را به هم متصل می‌کنند، از گذرگاه تنگه هرمز عبور می‌کنند و تهدید کرد که «هرگونه آسیب به این کابل‌ها می‌تواند اختلالات گسترده‌ای در اینترنت و اقتصاد دیجیتال کشورهای مختلف ایجاد کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75367" target="_blank">📅 23:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWTyy0W3BAPyYyv7m_6i8Xy114gCUlJri7LM9jM1dlzEDH6t3gm9aqCFIU0M3IlmARwwVC1PC9cq0BPkz_Xyu379daFxYkPzSPJNIz3RsoKoAPPON7_PfmgLYEQcyefW24Al0sxW_u49bbdZZdX1cw52727R-Mqts-saiWfGqdCBTpVCeGsdbqVEuL6Go4Gb6--bY0qqze6cb80Hc5qZnHrpwR3J47X4xbINrumL5J3kJURnEgryYB8B7m0lpUFi6_K8JPAxjpfDjMM5Gc4_Q5sOmX4P4ZhE6CsTUHk8WXcQx4soLg-A6v9snF3-CcHJoNqeKGiENjvSDW2C363-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، روز شنبه ۱۹ اردیبهشت، ساعتی بعد از برپایی رژهٔ «روز پیروزی» در مسکو، گفت که معتقد است جنگ اوکراین در حال اتمام است.
او بدون اشاره به جزئیات بیشتر دربارهٔ این جنگ به خبرنگاران گفت: «فکر می‌کنم این موضوع در حال پایان یافتن است.»
روزنامه فایننشال تایمز روز پنجشنبه گزارش داده بود که رهبران اتحادیه اروپا در حال آماده‌سازی برای مذاکرات احتمالی هستند. وقتی از پوتین پرسیده شد آیا حاضر است با اروپایی‌ها وارد گفت‌وگو شود، او گفت که گزینه ترجیحی‌اش گرهارد شرودر، صدراعظم پیشین آلمان، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75366" target="_blank">📅 23:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=lpu5iFX6vdMohOLG4AS_-OVoiG-prb9Ej-lHss0UZRgQ1v558pgnwGgqOy5MhkpgQf4bfMped4BwHEjmnKv46HbHAxdLwqIu-RFrvxKITs-mV0dv8J1wMrCRoN33QbRdyqq4AKkR_c8KS5JHwvKQCK4ueergH8kOdRR5nA7zQ3TC9MqxPwSdGck8AvUjls0UiH2vYa7oOCHW5EZGST078m1VKXVDvczmJAYQK_vlSQzj60O_oImCngc818GzWAKErP5bT_ORbGYOaxGU1k-tBUQyHQBHxBnI66QNoNsznaJfXMyAdMTaGZNagGeLmri9kDJ5iWLO82nsr069T--fyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=lpu5iFX6vdMohOLG4AS_-OVoiG-prb9Ej-lHss0UZRgQ1v558pgnwGgqOy5MhkpgQf4bfMped4BwHEjmnKv46HbHAxdLwqIu-RFrvxKITs-mV0dv8J1wMrCRoN33QbRdyqq4AKkR_c8KS5JHwvKQCK4ueergH8kOdRR5nA7zQ3TC9MqxPwSdGck8AvUjls0UiH2vYa7oOCHW5EZGST078m1VKXVDvczmJAYQK_vlSQzj60O_oImCngc818GzWAKErP5bT_ORbGYOaxGU1k-tBUQyHQBHxBnI66QNoNsznaJfXMyAdMTaGZNagGeLmri9kDJ5iWLO82nsr069T--fyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از تجمعات شبانه طرفداران جمهوری اسلامی منتشر شده که در آن فرد خواننده می‌گوید زنان «کم حجابی» که در تجمع طرفداری از حکومت شرکت می‌کنند «نور چشم» آن‌ها هستند و ظاهر افراد ملاک نیست.
نظام جمهوری اسلامی پیش از این زنان بدون حجاب اجباری را بازداشت کرده و طی لایحه‌ای به نام «حجاب و عفاف» قصد ابلاغ جریمه‌های و محرومیت‌های سنگین علیه آنان را داشت.
با این حال، در هفته‌های گذشته حکومت سعی کرده با انتشار ویدیوها و مصاحبه‌هایی از تعدادی زن بی‌حجاب در تجمعات حکومتی، پایگاه اجتماعی خود را گسترده نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75365" target="_blank">📅 21:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odLdo6Rmd35qQ7wuXLERAN25okQTJTFzv5VN8bIukHCetRe4XkK7TjrVXlk99i1gwqkpj9dRGYFKPZvzpLH_dr4Q6Q2r67eKPoeOJ36dHk2H9cy895VD1NBVEz4eZ8lsMmNbJvQZxdXgftH071TtsGeutfAogfoNfjddLoNtaMxKtVj151Mld_dqlfm3t08CaS4OWAHBkJiqL4C_NdqV-A4PHs_NlWSATRClcWno5x2MK2Ub0uefeaQcDeR5Emmk3CcPe_hDcbez_0IyK0kLTtwc9fkN-fS6I5Audup-rnn-H3h1IbwrPJEFbtmD3r7yoDYqjmlp7QEiXizV4DFMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های لبنانی روز شنبه اعلام کردند که در حملات هوایی اسرائیل به جنوب لبنان، هشت نفر کشته شده‌اند. همچنین بزرگراهی در جنوب بیروت هدف حمله هوایی قرار گرفت.
این حملات تازه با وجود آتش‌بس سه‌هفته‌ای میان اسرائیل و حزب‌الله، گروه مورد حمایت [جمهوری اسلامی در] ایران، انجام شد؛ آتش‌بسی که تأثیر چندانی در توقف تبادل روزانه آتش، عمدتاً در جنوب لبنان، نداشته است.
حزب‌الله روز شنبه اعلام کرد که در واکنش به ادامه حملات، نیروهای اسرائیلی در شمال این کشور را با پهپاد هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75364" target="_blank">📅 20:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cheuheZ7TEY-mRUQu06oSdRRTQiKC1oT_yvq6EYE4f4WnW5k2t6eim0iiIfIrE11g2Hl2oD0BZqdbjxQQ5fthKA1DEIGAVu51J-dHZtvsnRLXTO_hT2pTH98vRqwiAqn7iHe5wTlpOkb7NRi9TAo5IGY8GVukxf0qwZDovH4Sbsnuq5sQFTfTdmiRIpWREaG0LwDapK4tlagEWuppciYJKPgdCmC9CHmwkO-NGG1kN-doga7ERRX-khxGMp4zyKdu9J_xHg-bt9mnT-vdYZ0NlMLSmp6HBU4JflFWso829FR9iStgeK67K3XpZLzYXkAkxq-zxxxPAqkUAKIeWi5sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا، سنتکام، روز ۱۹ اردیبهشت ۱۴۰۵ اعلام کرد محاصره دریایی آمریکا علیه جمهوری اسلامی همچنان به‌طور کامل اجرا می‌شود و نیروهای این فرماندهی تاکنون ۵۸ کشتی تجاری را تغییر مسیر داده و چهار شناور را از کار انداخته‌اند تا از ورود یا خروج آن‌ها به بنادر ایران جلوگیری شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75363" target="_blank">📅 19:40 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OQPWnWUM3Lv8dQNLp8iPi67gRjo8JoLVYx8WuGah66VT_FwnhzlV3oDgwpQU4Sai06Y0j5g3Ei7pY3bdEz2UX-UQcic71QHqaFb-6Bew0sPTYGJrZlBf7EteCHp085WsFQJjFWDJwZ__Lvfd2vKp7L0DKZUrIzfqjIgmQievxKF7Q_2hPYLzVaVJLrOaBUiThKkmz7TKqII4tOh4z3kNv9nHjCBuG1xbXVOtfQ2UIywBR_BWF_VKdC17jfksoN0Vpw5ZAGBZ6OUyLF-TI61OhHSzElFhpMSsFLb4Sf9bTjsP77plWPtg0BzKZa3XGVCp0n80zynku_s_DTuCbux_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RDlgxwmh8dYzeoPxg7hl0FmvImZRW8b8AnHmglD6SBk5wY2WQ0NgF5rL-z0jdxZPcwTM6YnR3C3T5g0xhYAw98-lG_3ubor5gavRgFvcxHKgPtoOVzTNFMZ15Uy1Ivg2GXEiFxm0bkZm8mLPxk2DpZvXamo6ff-oOKqM29sud4XSNb6FUtFi4nMsIphCTdD2SPrrXu4BITuWhzclCBiw_EMnxKhHeKLM1HWKl6eAlMzKWNWwbLPl3DJyn0mwT6sJlv4GY_nL7aCxxu-4NJVoTAgmiHUyd-fGEBcNVJZkwr0mmHv3vusRdBPzF0X7IWaU1PJvMwe_oN695nLRoh1J4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JqH5k1u32dt9owDPlCA8TSMztbQNXiCuA8XddUHgZo98Q6rzvgBaikSpKDOTYZ9RfiN9z8DtnYURkx9zsGza2Sog1UDK-s9SVp9679petXmEvSFRcOiDXZEUh3qVB_0IBQxwUKWIwMnW_mVkLFZD67xOCGkFtTEBArDrPnp29BWREyZ6Do8NsJZkPKJhz5IBUhduFxeaVlzFgKEeABco1fK5daBHSrFXRiIQApDejQ8oNUJoISiYZnAbVxOgn61w96TQCVxz1WWKULCmcZWdJMHxnN1VQnWF2Y_eDrcvbFOZ3prWILjyE_kskJVvOJc6IFb1YD-JJocCkJ2xaTfQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HqzHZ2PFOSudKc_ZMTHcSeibi_iPhlGnVvPh97M_QZ2KzT4s53f7skWb8IFKwe3BYE9vGkQayNy17EZoH4m-9WwKUU_QpATZD0CKeJ3kLqFNthniNmoWmiCXzCWtvdwWt8xvQ8D91JYYabXNstwJlNkYJ7ksK2MQ95ostzeDZT_x2neSP0JLkyJWMY7-oI4Cc7iELbTmPPXqmrW-EhRdXYkNSU9WWXLnSoXTbrCvtgBgJxblIUv80FnC4-QhGVHY6AfqpsCloZcP0gnnM43sUHfpKP09Z1By_LBRmyM4020yNKradbR29pa8ZLbRgQhwAvfRwXCLEr4Kb3qppYnHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GDMietIzbTX1So_0oiIBeIcHKrf38u-h0JnVqEqxUcFXQ2HyBIThi183MEYz3Ot68_dv_V88kd3aXXasLaJrsu_4RLqEFCfGfiBBO5VoO3zUhx92Gr6M2vh5tkJe7RG_atSI75VFQPRNN40ZBgGt6zIPhyp4PGbqp3ffuw4GHuhNltLh35azGA9KyR1r0A9LvPfDl15IM4mO1uV_jLJamMRsVUY7jug_iLAI6mWtJC3hpO5lfkls5gtftcozEfyBaTYtyAHIcahibqufJm3hMqVLEP46a8jnklxvVpZ3m2yUvjp0KAMDTjJkSvuHbF9Uwdq1HjOpGl82tNOUZMpNpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذشت
‌ عبدالله امیدوار، یکی از دو برادر امیدوار که اولین نزدیک به ۷۰ سال پیش با موتورسیکلت دور جهان را گشتند، در سانتياگو، پايتخت شيلی درگذشت.
عبدالله،  برادر کوچکتر پس از پایان سفرشان به شيلی رفت و در آنجا ازدواج کرد و شرکت فیلم‌سازی در شيلی تاسيس کرد.
عبدالله۲۱ ساله و عیسی ۲۳ ساله،  در سال ۱۹۵۴</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75358" target="_blank">📅 18:51 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPdZW4gL1sN7299CuQV4r17M6N6APoqn7H9PjsizAkzKF2lLO7qhinyKKWYeWudfr8pDADWBsCfZnikhsWkVeR0DyBqY2OBshz06VXqt8wIWCuxela8TEzgi311zmOvw4xRJj5dfz-JHrNlnUPLsyEv-AujJ8l1XWdpPlxSGOKerS8YN6_ufzTFO_F1mRoR9-DHMSvE9jXZWSsoNgNl2GvPdvObg6YjPoOejvheSOQNjkrA8FBzmpy1IO9AL1ZWcO59GNM6RprSrD7YDTW8d9rKcAZrapb2jBI6MYMlfS-oXq7EFY4sn-qFqO8EgyHA0QUX8sBhcQR5e7jg2B57LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع بریتانیا روز شنبه اعلام کرد که پیش از هرگونه مأموریت بین‌المللی برای کمک به حفاظت از کشتیرانی در تنگه هرمز، یک ناوشکن به خاورمیانه اعزام خواهد کرد.
سخنگوی این وزارتخانه به خبرگزاری فرانسه گفت: «استقرار پیشاپیش ناوشکن «اچ‌ام‌اس دراگون» بخشی از برنامه‌ریزی محتاطانه‌ای است که تضمین می‌کند بریتانیا به‌عنوان بخشی از یک ائتلاف چندملیتی به رهبری مشترک بریتانیا و فرانسه، در زمان مناسب آماده تأمین امنیت تنگه باشد.»
لندن و پاریس چند هفته پیش اعلام کردند که طرح‌های نظامی برای تأمین امنیت تنگه هرمز در حال شکل‌گیری است و در بازگرداندن جریان تجارت از طریق این گذرگاه حیاتی موفق خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75357" target="_blank">📅 18:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IP0rReq8JfDagDMXiZWL2b7gslRfY5NGgrB7mMBWCy6DAbTbhd29kwDV_KRxxxpBjpYeYjyDgqqUTVejL0_eOj_-REYibQWsqIdJ23YPbqarzDP3cBtXjQc4Ln1xh_Fl9ei6yg7Dtz300WjPv4DyxFTsQX2DtfX1s9SgqHx2faYk1QfITJFk9sdllc6zIA9lT_p1ksval6IsoRy3COmagTazW2vYHGC5jzHcF6lEOoJkT0qCWmbvyhuvTSnh7YaPu3L2-FRg7UWxeOI_7-r2aUw8Jo_oUVaj39XDCXH6GMhe-HkerdKmRFSsMp2EL8LLCYTcP1c7sdb0JRwmNPhx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/utn84IxOw-3dWppBaM1zcU7fjN1M-pj2uvA5_B5M98WsO6x9VLD_v2tvJ8SylLxFYwv7o3YwqKnO2iovhjx9pfGoMoR7sxhNG1pSNkjCvHVyHPq7W-djsgU7_sZWD9zNcAWLcC-U1A3al3AfzoMtCy94RouE-A1Z3Wc09jTB-ievVzxGH2fCp0qx9ZbWH5-aD92D37hQ7k555hbQi2fColAdeQvb6H_O8POLc5bXhviHSJZ_XlIw8oRJaAapUEn3lSSYwlhntGur9c8Wb6K0YpM85woX7ZhzRMst3e1BF91klLWXx8stpwuWUDqQY0rFlDhE7GvxmN6MJ-1akGN0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UjH-EBTGEtrpG0gF_K-nyKK8DqNIOyZBNxlBvXAFMYI14YDvK9CQ1hYdxpfptXIkj8-xV8ODi2ZuqkPqU37ZKCX362bzfKLMb1crjRAqotaKhS2w_HxCLhi80HajFEVB-uS1TYm113-zHCUTuUWg391-ouQ9pNy1mpsjTVt5e4iJdlc5G_Zzs0ZXgYKb63UNz3YlimaFzz29oR7Zgc2RVDylqAiX7PHO2o6iY70d1Uk-b9yrZHBlB07zWBahABzoLDTu7zHHv8epeZV899oURXsgb-FMJkGhG78B4pFP6j1fluIvnFUU_vjN9pLT9GaxZbdQCVyfwHC6jiNoIBt2YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت کشور بحرین روز شنبه ۱۹ اردیبهشت اعلام کرد که ۴۱ نفر را که به گفته این وزارتخانه با سپاه پاسداران ایران مرتبط بوده‌اند، دستگیر کرده است.
خبرگزاری دولتی بحرین به نقل از این وزارتخانه گزارش داد که مقامات امنیتی گروهی مرتبط با سپاه پاسداران ایران را شناسایی کرده است و افزود که تحقیقات برای شناسایی و برخورد با هر فردی که در این تشکیلات فعالیت داشته ادامه دارد.
@
VahidHeadline
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی، روز شنبه ۱۹ اردیبهشت، با انتشار پیامی در شبکه اجتماعی ایکس کشورهای منطقه از جمله بحرین را تهدید کرد که در صورت همراهی با قطعنامه پیشنهادی آمریکا در شورای امنیت سازمان ملل، با «پیامدهای جدی» مواجه خواهد شد.
عزیزی بحرین را «کشور ذره‌بینی» خواند و نوشت: «به دولت‌هایی همچون کشور ذره‌بینی بحرین که در حال همراهی با قطعنامه آمریکایی هستند، درباره پیامدهای جدی این اقدام هشدار می‌دهیم. درهای تنگه هرمز را برای همیشه به روی خود نبندید!»
قطعنامه مذکور که با حمایت آمریکا و کشورهای حوزه خلیج فارس به شورای امنیت سازمان ملل ارائه شده، از ایران می‌خواهد که ضمن توقف حملات علیه شناورهایی که قصد عبور از تنگه هرمز را دارند، محل دقیق مین‌های کارگذاری شده را اعلام کند و از دریافت هرگونه عوارض عبور از شناورهای عبوری خودداری کند.
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای حمایت کامل ریاض را از اقداماتی اعلام کرد که پادشاهی بحرین برای مقابله با آنچه «اقدام‌های صادرشده از سوی ایران» خوانده، اتخاذ کرده است.
در این بیانیه آمده است این اقدام‌ها به گفته مقام‌های سعودی، امنیت ملی بحرین را تحت تاثیر قرار می‌دهد و با هدف بی‌ثبات کردن امنیت و ثبات این کشور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75354" target="_blank">📅 18:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwZjiz7ZEsf3MjL7EfptVvxfQxTVpJlubQQJXbrHzkl2LYqzgUOn2oasPzkM9Tr9u8Jolx8F017H4DMB75Dmye_3KIWM7nF2x-fxNDCKzw4iE3Ofv2-m0imS1cM-tSksuOgi4zALZoBwgIV9QobTZLsdkG3rOodW6pHo8j93bJ36R4p2WQUV795nkCA5I8aMETCUmEfFvC9kFI200NsC1kiV4bjhxnPFB6NtJvsQjNPf2G0WGb95Wrko6bjGR-jofM0bgNbrHn_Ve_IA31xNPyMzMjYURBxDAlsuq6HyZtuMglYj027Y7LiOoFaJLy5DMK_z07Ulqffs8lFGdRZMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75353" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tiuk7-yGT1RhpCE79FdCHCrbq4dzMpPOEKHVw4p6CK7TtfYbLYe8N2-elOA5D8asWV6FfGAfPJkthBQ8GnSGK_DRuy459MAq8dXtHSrtkAt6So6oqjbVO0SaImAhbmKCP5SLtEDuiXTcDKAJTXAvpMZO1RKxZl_3BE5OuSXSAokvBwRDVGCe7g4vVCj5UFClLlxqIRYkwOgFyZFt45c52pno7RD19W3Ux-265nTTljNHi2VBRRXAnwICwO9XeoM4JTzaeutcjLeQJwjU7qKWD10RcC5knQaiZWoGa719V86PF7Cs9o8TKJ0rRBWBw7RHwS799krbOUuvHPXjbxRlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ueu1wnB1yFXr0T_SYf3DjdmVc-vqcFk5MTE6A8r1l2Xs-Xx4K5-7TnvC1TrCptiLnTxBaQlr3FIfUfuLj0yyllunK47byyXK6cIcck03A7H5a7Osp0WY_LCPoKCsmiBsk8ouAXDiRsrGq1uGnzdlPT4M2bM6S5wfXPNG3s7qnp1hzvH6b7sg9opk8qjap7YI9pULSuAAMxfvfWAeLn2XKdjfbBVmAeDgPqPSBoh-uX3IAPGAC14nln-MJothi0Mac9QZSwmCBkdjqJDXPZeDNqIQ0Jsm1r_x2XN4MWiy9ik9lSLf6HP9NUA_oHWsDlUBtisGj17sDeiRgdaoqVFjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C38RWQZLTsBl7g4EsGZC33o94rHraRODHzOrRbKUgMhrJVfHauMdyhi8Zj6NvtNTdRocDZmbVaetPd4NPmH-uNbX_ckmCe0w1zIS6-EjCR_k6vabagGjH43lg-_kDHKTm33eSHKisYHpCDuOONNwAHQFY_wQxIms_dsopJ9rDTFtjXTXlWR_ZI17F0dC2jSnuN3vM0laPStyuTOQ4A3VUnqjcIokGsvnzDQ_tL1lFlRxEKmQTIXD1XoPc8OWQxlz6TPGPstuCYPGEVfp3BU1t3o1-C6MxWH1VgCb7VNkFOPW1VXhe9SeNcrRb0AH3RhXd-1p26Ddj8QfnHDn2msG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XZjj6XA7uzhPhHl9dq_a4PHIZxypxufNJH-8zj3sNSDp1Nz2U98mNRB3eXJDQL9_0YT2jdBY8IUvRrmIksdWLOVyednnaj7RgJaEEuG0N76JlXKM40CcYBWbiG2KavX46x9RvWLizAPiF57vvxu3bxj6US4Eg6ptT32_1OseFICpHdqhhgenTSQvA1wKKJa13mTqVML9hywrw6MO7wyrOKss9QAeBJTgZ82hJSqFyhW8cKHVox2hsb6_yiWgD4kkhDJ1nuZy7L9NOnsyGoH__jk9Cd_DnX1NTM8myH-lksaX39wluXJIhWTYZYYEAGs_cVjJvvumD_wVppLlbuRykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f78A1XKlF4T8Brd6HbnKxhKFhnzwhy7pqmgMwnzNvfVI_f77dtSAmkbqnFx1pXu2SlDySMaLBCegtkW_EriVL2U050jAQqbV-cra6-_8Koh-sSHjb9XwxXKj762PQBPOOroLBybWGUGPvJykOQXI6Z6nR7y951E73Yp0vJzESqCL48OofY0cua5059wNPO1eC6p32HN5UQMByZb42kvqU8cAP4-xChlZlDftD_B8dTon5FIhEcjWWX93y0A3UBFN3ObEyckI9BaXM7Xl_UyYmd5V28K3_ZOuNcEOcZAOzt1HNFV2-4Gm6K4ozDpsjfpiYHvAAjrYLEVkaG52d5tn5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در آغاز یازدهمین هفته از قطعی سراسری اینترنت بین‌المللی در ایران، یک مقام دولتی هشدار داد که این اقدام حکومت در درازمدت خود به «تهدید امنیتی» برای جمهوری اسلامی بدل خواهد شد.
احسان چیت‌ساز، معاون وزیر ارتباطات در دولت مسعود پزشکیان، گفت: «قطع اینترنت فقط در بازه‌های زمانی کوتاه می‌تواند کمک کند و در بلندمدت تهدید امنیتی است.»
قطعی اینترنت در ایران روز شنبه، ۱۹ اردیبهشت، یازدهمین هفته خود را آغاز کرد، در حالی که مردم عادی در کشور تنها با صرف هزینه‌های گزاف می‌توانند به اینترنت بین‌المللی دسترسی داشته باشند و مقام‌های حکومتی و عده‌ای از حامیان جمهوری اسلامی با مانعی در دسترسی مواجه نیستند.
@
VahidHeadline
معاون وزیر ارتباطات ایران خسارت‌های ناشی از قطع اینترنت برای اقتصاد دیجیتال ایران، در پلتفرم‌های بزرگ را ۵۵ هزار میلیارد تومان اعلام کرد.
او گفته است: «مجموع عدم‌النفع (کاهش درآمد) این حوزه نزدیک به ۱۶/۳۲ هزار میلیارد تومان برآورد می‌شود.»
معاون وزیر ارتباطات ایران همچنین گفته است قطعی اینترنت در حوزه مخابرات و ارتباطات حدود ۶/۴ هزار میلیارد تومان کاهش درآمد مستقیم کسب‌وکارها را در بر داشته است.
آقای چیت‌ساز گفته است: «قطع اینترنت برای کسب‌وکار اقتصاد دیجیتال ممکن است برای چند ساعت قابل تحمل باشد، اما قطع گسترده و سراسری آن عملا یک شوک اقتصادی ایجاد می‌کند.»
یازده هفته از قطع سراسری اینترنت در ایران می‌گذرد.
افشین کلاهی، ازاعضای اتاق بازرگانی ایران، پیش از این گفته بود که خسارت مستقیم قطع اینترنت در ایران ۳۰ تا ۴۰ میلیون دلار در روز است و خسارت مستقیم و غیرمستقیم این محدودیت تا۸۰ میلیون دلار در روز می‌رسد.
@
VahidHeadline
خبرگزاری دولتی ایرنا در گزارشی میدانی از تهران، عملاً تأیید کرده است که قطع اینترنت بخشی از فروشگاه‌های مجازی را از فضای آنلاین بیرون رانده و به خیابان و پیاده‌رو کشانده است.
ایرنا نوشته پررنگ شدن دستفروشی فقط محدود به نقاط مرکزی تهران نیست و از بازار امامزاده حسن در جنوب غرب تهران تا شهرک اندیشه شهریار نیز دیده می‌شود.
به گزارش این خبرگزاری، مدارای شهرداری و «دستور آگاهانه» برای برخورد نکردن با دستفروشان، این روند را آشکارتر کرده و بخش‌هایی از شهر را به ویترین بساط‌گرانی تبدیل کرده است که به‌اجبار از اینستاگرام به خیابان کوچ کرده‌اند.
ایرنا نوشته فروشندگانی که تا چند ماه پیش با صفحه اینستاگرامی، پرداخت آنلاین و ارسال سفارش فعالیت می‌کردند، حالا در نبود اینترنت آزاد و پایدار، ناچار شده‌اند در خیابان بساط کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75348" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75346">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nGp-2urn1VvEc7vhr0N9dQHbUa8Ua3HvRz2lJ58GXpy-v6SQWpBxiPgnugmmNaTfSnrR-2vPjIhjv-r5-EnL22Xpaj55KBo5EjiHVSUH8vqmxtQsaahUbQHR85WCE4EXQHuS5otd-1s3OPNZNn4HCFDyR5eu6M9_f5M6gR3CBs4YeDlQd0E0kcFLZgP46S4gAVBB77gZiAbTAe5Rtz-OhQ81Ish1L5kUNAVPC5W_FcS5Lm4-4y58xLs1U4RqfNv5C6i7WoAuiGDo3FUaCwipJU7XkoEdSTXu8xEmZla015jzE94SYbqiHOP9FAODVt_K06fMKRbIDxoiQfOD_1mJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aUsDzJL6RketIWpuf7Emyus0FCqFdOGKwhRtXNkCSClztNmTbS30ZBWTjst9eetJX-AuX4m7yBSbVyXSXk6vFSep6ePmHaiOryyTnoiu7bdJ7CgxLEpHHowFXb0EmbnpENdDenzqYSycTfnXLbg1lDqwUwjyMusOnn32TB-Zbouclx1zd13z-WZ0eDhMfQxmI7XvKP4JdilEX9BD4qsVIHbL_3If67hgFyaa6Sey4PGBM_syxHzN-aKdjCxvd-iBN0em1o9Sz8TzLbcDAudYqLqGG88DnldeYkw5M0E_F_jikEyhgf51hGty3ENps9hhJZIaNi1XLLMoDY5mSD4mRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه‌ترین داده‌های مرکز آمار ایران نشان می‌دهد قیمت برخی کالاهای اساسی خوراکی در فروردین ۱۴۰۵ نسبت به مدت مشابه سال قبل جهش کم‌سابقه‌ای داشته است.
بنابر این گزارش، روغن جامد با تورم نقطه‌ای ۳۷۵ درصدی، بیشترین افزایش قیمت را در میان اقلام خوراکی ثبت کرده و قیمت آن از حدود ۸۱ هزار تومان در فروردین ۱۴۰۴ به بیش از ۳۸۵ هزار تومان رسیده است. روغن مایع نیز با افزایش ۳۰۸ درصدی، از حدود ۷۴ هزار تومان به بیش از ۳۰۰ هزار تومان رسیده است.
برنج خارجی درجه یک با رشد ۲۰۹ درصدی، مرغ ماشینی با ۱۹۱ درصد، سس مایونز با ۱۹۰ درصد و تخم‌مرغ با ۱۷۰ درصد افزایش قیمت، از دیگر اقلام پرتورم بوده‌اند.
این جهش قیمت‌ها در حالی رخ داده که فعالان کارگری سبد معیشت خانوار کارگری را بیش از ۷۱ میلیون تومان برآورد کرده‌اند، اما حداقل مزد پایه ماهانه کارگران در سال ۱۴۰۵ حدود ۱۶ میلیون و ۶۰۰ هزار تومان است؛ شکافی که نشان می‌دهد حتی درآمد رسمی کارگران فاصله‌ای چندبرابری با هزینه حداقلی زندگی دارد.
@
VahidHeadline
خبرآنلاین در گزارشی نوشته اثر افزایش ۶۰ درصدی حداقل مزد سال ۱۴۰۵ تنها در ۴۵ روز از بین رفته و قدرت خرید کارگران دوباره به سطح پیش از افزایش مزد بازگشته است.
بر اساس این گزارش، حداقل مزد پایه ماهانه امسال ۱۶ میلیون و ۶۲۵ هزار تومان تعیین شد؛ رقمی که در روز تصویب، با دلار ۱۴۳ هزار و ۷۰۰ تومانی حدود ۱۱۶ دلار ارزش داشت. اما با رسیدن دلار به حدود ۱۹۰ هزار تومان در نیمه اردیبهشت، ارزش دلاری مزد به حدود ۸۷.۵ دلار سقوط کرده است.
خبرآنلاین نوشته قدرت خرید مزد بر اساس طلا هم افت کرده؛ حداقل حقوق که در اسفند معادل حدود یک گرم طلای ۱۸ عیار بود، حالا به ۰.۸۱ گرم رسیده است.
این یعنی افزایش اسمی دستمزد، زیر فشار سقوط ریال، تورم و سیاست‌های اقتصادی جمهوری اسلامی عملاً خنثی شده و کارگران دوباره با شکافی عمیق میان درآمد و هزینه زندگی روبه‌رو شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75346" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRuiw4SDn_fDBWSB-kltwLtS2rWdS3zO4uT1Ijuam3XB0XrWGgSQy5-gFiRQjPH-pjBFZ6YssTQwbSg1HWr1B-td3dBpqW3FhPd3snKE3NrZVonATeZCGgy7h2oc_fQsDjfEocwIshRA6i7CNOmIYBCdh-dv-9uFzrHr427RzQfdRWTcTblVlO4eqscz3m9RWBPME2jpjxPMZCIIg8mXQxPKm6kfHwDtIJU-9y82s-HbtvjZxP4r8KDiu1CIq9h9-LWOdUt4bDiZ_ywFDn1F_kPcuevi7509rLJ49dgI6hdXYkDoC6XzeIfyYhW3PunK4PnbrfK-SNr2VFZsrxwuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جمعه،‌ ۱۸ اردیبهشت، یک خبرنگار در کاخ سفید از دونالد ترامپ درباره نتیجه تحقیقات دولت آمریکا درباره حمله به مدرسه میناب پرسید.
او در پاسخ گفت که این مسئله هم‌چنان در حال بررسی است و نتیجه تحقیقات «به محض آماده شدن» در اختیار خبرنگاران و رسانه‌ها قرار خواهد گرفت.
در جریان حمله به مدرسه‌ای دخترانه و پسرانه در شهر میناب در جنوب کشور که در روز آغازین جنگ مشترک آمریکا و اسرائیل با ایران رخ داد دست‌کم ۱۲۰ دانش‌آموز و ۲۶ معلم کشته شدند.
چند روز پس از حمله، تحقیقات رسانه‌ها نشان داد که این مدرسه که در نزدیکی یک پایگاه دریایی سپاه قرار داشت با موشک‌های آمریکایی هدف قرار گرفته است.
از آن زمان تاکنون هفته‌هاست که پنتاگون اعلام کرده است در حال تحقیق درباره چگونگی رخ دادن این حمله است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75345" target="_blank">📅 18:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBq_vsgcbv4PurEpgpO7Eq4ClQPvhQTiWF7yqf8PY-F-WiUp9NXmwx5SwsPgCNd7zMcwGHUdjdgbUMEwq0jp_PB_4iqyKOErD48AflXvwzduFrlK3B5dycBaCxVRX5WI8moGbkagi21fFgUQplJmLnpbFOjatIch2eeWAmV6xaBuAvir5pii0XhO54whTTWW2vVXMN3m128pdk2SxzL33MIFlFa6EkECRfktwOrOCKnPZ1zLqqf63HHNhDNT5SAx_7f8YLp18qYcwa9NgVbL4lC7UImJ7p0-744AMhSYW0_19swCUFZvoi-MSokyicuH5r0n2pfPYkjYLeGrmNQKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به خبرنگاران درباره چشم‌انداز توافق با جمهوری اسلامی گفت: «اگر همه‌چیز امضا و نهایی نشود، مسیر متفاوتی را در پیش خواهیم گرفت. اگر اتفاقی نیافتد، ممکن است به پروژه آزادی تنگه هرمز بازگردیم، اما آن پروژه آزادی پلاس خواهد بود؛ یعنی پروژه آزادی به‌اضافه موارد دیگر.»
او در پاسخ به پرسش یک خبرنگار مبنی بر اینکه آیا جمهوری اسلامی عمدا روند مذاکرات را به کندی پیش می‌برد، گفت: «به‌زودی خواهیم فهمید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75344" target="_blank">📅 03:02 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSJ_NB3sfjS2O-931Ii7PMyBH2OaXBaKY8aEdR560bYWtz0y6zTjae-CEOunBh9ELiv8rG89-DE9EAbVxktDLD9fBndDdM9Qf4wK54-DjRGfROQI_YmY1MTKjWOgTqlQAhH6L2T0wpTXOot13SC7d3W2sTy5uBbiHv3rJlyOhk1sRGTPYDir_fEF7qaNyJV_rUfJmAaY8hE2jTpi-g7gadXPU9_PL5bXlk6McwzwRUSxLqqcn0wvwU0bhc3yCcdCRiCtiOj3IabCGeBxBV1BOGPoKVmmK7R_n9EhhN0snk-BY6dQIHGnpZyWu5ZAi1LH-cbTl4BoYP-rtmvIhKmIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داده که لکه‌ای نفتی ظاهرا از بخش غربی جزیره خارک، پایانه اصلی صادرات نفت خام ایران در خلیج فارس، در حال نشت است.
آمی دنیل، مدیرعامل شرکت اطلاعات دریایی «ویندوارد ای‌آی»، به ای‌پی گفت که از روز سه‌شنبه، معادل حدود ۸۰ هزار بشکه نفت از جزیره خارک نشت کرده است.
@
VahidOOnLine
شبکه خبری فاکس‌نیوز به نقل از کارشناسان می‌گوید این موضوع ممکن است نشانه‌ای از فروپاشی زیرساخت‌های نفتی جمهوری اسلامی باشد که زیر فشار فزاینده ایالات متحده قرار دارد.
به گفته تحلیلگرانی که خبرگزاری رویترز از آن‌ها نقل قول کرده است، این لکه که در تصاویر ماهواره‌ای کوپرنیکوس سنتینل بین چهارشنبه و جمعه دیده می‌شود، منطقه‌ای به وسعت تقریباً ۴۵ کیلومتر مربع از غرب جزیره خارک را پوشانده است.
مقامات آمریکایی بارها گفته‌اند که با محاصره دریایی جمهوری اسلامی، ذخایر نفت در ایران به زودی پر خواهد شد و رژیم ناچار می‌شود که تولید خود را کاهش دهد، امری که می‌تواند آسیب دائمی به میزان برداشت از چاه‌های نفت وارد کند.
حالا، نشت مشکوک نفت در دریا این نظریه را به وجود آورده است که جمهوری اسلامی نفت خود را به دریا می‌ریزد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75342" target="_blank">📅 01:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFvJSabgoAeGbbDDN7Gbtyeiigv8Ad09HZTUB49QDAxepijdyick_yBF3uNC0OD4ihEhgGiqEQnnW15fgf3CEpPLw07qi2xnMvorh7n-yKt2jlzfUV0cREG4uuQCxMYbYEq9cIuYOqv_EES4UjimlQnKvBWRRjPHHam6ryyrM5JhdK880oFA3CSNrqlNZPXIetKbnVb7ooctXJ_CW8Tamy6FA6EgCRpVl7a-iHayJCN6dWLicRyAmzG9rc8Rvg217ExbcC17uJjfG9RRYZjr-ifVwY3g-_Tpl8HXBpGQfZoq8icacl6MRlhSOL9hZK6QxAmJdxcLvxoUVmk-qU-tMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «واشنگتن‌پست»، معدن‌کاران در میانمار موفق به کشف یک یاقوت سرخ بسیار کمیاب و غول‌پیکر شده‌اند که از نظر وزن، دومین یاقوت بزرگی است که تاکنون در این کشور کشف شده است. این سنگ قیمتی ۱۱ هزار قیراطی (معادل ۲.۲ کیلوگرم) در نزدیکی شهر «موگوک» پیدا شده؛ منطقه‌ای که به دلیل استخراج یاقوت‌های سرخ تیره و باکیفیت که در جهان به «خون کفتری» (Pigeon Blood) شهرت دارند، شناخته می‌شود. اگرچه وزن این سنگ حدود نیمی از رکورد کشف‌شده در سال ۱۹۹۶ است، اما کارشناسان معتقدند به دلیل رنگ سرخ ارغوانی منحصربه‌فرد، شفافیت بالا و کیفیت بازتاب نور، ارزش مادی بسیار بیشتری نسبت به نمونه‌های قبلی دارد.
میانمار تامین‌کننده حدود ۹۰ درصد یاقوت‌های جهان است، اما تجارت این سنگ‌ها همواره با مناقشات سیاسی و حقوق بشری گره خورده است. سنگ‌های قیمتی یکی از منابع اصلی درآمد برای دولت نظامی میانمار و همچنین گروه‌های مسلح قومی به شمار می‌روند که برای خودمختاری می‌جنگند. در همین راستا، سازمان‌های حقوق بشری مانند «گلوبال ویتنس» از جواهرسازان بین‌المللی خواسته‌اند تا خرید سنگ از میانمار را متوقف کنند، چرا که سود حاصل از این صنعت سوخت لازم برای ادامه جنگ‌های داخلی و تقویت قدرت نظامیان را تأمین می‌کند. با وجود تغییرات سیاسی ظاهری در میانمار، ارتش همچنان کنترل بخش‌های کلیدی این معادن را در دست دارد و کشف این یاقوت عظیم در میانه بحران‌های امنیتی، بار دیگر توجه جهانی را به ثروت‌های پنهان در مناطق درگیر جنگ جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75341" target="_blank">📅 01:18 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=jFVg_bigIYQ7jWi51E68O-tTxi2uAOoxiaIXzVZjSRuWWxV6BV8f9jInTR9pJfAI-ONHWvn4roJseBmKT_9GIr71jdVytutvkDQQVmdLsCkaWOFQQ0nWTLFCOEBl3JH0xeka61DWk25I3CtMoq1PdHCwOJyERx54ldPYYkfDYEwTbaiwrHm7yLscquok8UWvwnKZS5PTgwfN2qwwOk-z76wQu4cNCG1lvva2U68CPK33Bjt-AC49xYchMbK7dr-DvSCu9WPsEPiMN3UOxRGYVoRHQN7JkEgkGkHJjOn2pL1adjVaoratMBVLZJeO3c3TGKOGeH6Tt4ioKSbIWiyFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b37b7b7858.mp4?token=jFVg_bigIYQ7jWi51E68O-tTxi2uAOoxiaIXzVZjSRuWWxV6BV8f9jInTR9pJfAI-ONHWvn4roJseBmKT_9GIr71jdVytutvkDQQVmdLsCkaWOFQQ0nWTLFCOEBl3JH0xeka61DWk25I3CtMoq1PdHCwOJyERx54ldPYYkfDYEwTbaiwrHm7yLscquok8UWvwnKZS5PTgwfN2qwwOk-z76wQu4cNCG1lvva2U68CPK33Bjt-AC49xYchMbK7dr-DvSCu9WPsEPiMN3UOxRGYVoRHQN7JkEgkGkHJjOn2pL1adjVaoratMBVLZJeO3c3TGKOGeH6Tt4ioKSbIWiyFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی، مسئول دیدارهای دفتر علی خامنه‌ای، در تجمع شبانه حکومتی، گفت که مجتبی خامنه‌ای در جریان بمباران بیت علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، از ناحیه زانو، کمر و پشت گوش آسیب دیده است.
حسینی گفت: «زمانی که در دفتر بودم، در ۳۰ متری ما بمب خورد که شیرازی [رییس دفتر نظامی علی خامنه‌ای] و دوستانشان پرپر شدند. ۷۰، ۸۰ متری ما جایگاه کار علی خامنه‌ای را زدند که آن اتفاق افتاد.»
او افزود: «منزل مجتبی خامنه‌ای را زدند که همسرش کشته شد. مجتبی خامنه‌ای در بین راه که آمد در پله‌ها که برود بالا، موشک آنجا خورد و خانم حداد [همسر مجتبی خامنه‌ای] کشته شد. مجتبی خامنه‌ای در بین راه ضربه موج [انفجار] خورده و روی زمین افتاده است.»
مسئول دیدارهای دفتر رهبر پیشین جمهوری اسلامی، درباره آسیب‌های وارد شده به مجتبی خامنه‌ای گفت: «یک خرده کشکک پایش صدمه دیده و یک خرده کمرش. کمرش در این ایام درست شد و کشکک پایش به زودی خوب می‌شود و در سلامتی کامل است.»
حسینی گفت: «یکی از عزیزان در هفته پیش با او دیدار داشت، آن بحث پیشانی که گفته‌اند بی‌خود است. یک ترک کوچک پشت گوشش خورده که آن هم پشت عمامه است و اصلا مشخص نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75340" target="_blank">📅 01:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTAW5iPLylHMcdPNhCpm5_BeFzmei3MfMwGvhCEUiBsgr24BjQ0_ZJO5LMCWSuw5cxbxyCI6UZf5bNzLunevXKb4YrIkQ2YlCnOU8Y5RTi_koqvZZH7tJGgKTIFjLmecQLCiVza_Y_fRC5KtGbJtZ20_dN-QqN7hh7X9sioPfA7upJZ1z87flh5kgcGQY3EfbRlod8C6vV74rvgucybPD0j2FKkabp8DBebImUQHZx-dDsKruDsAGC2aHTbt_4L6kD1hjCRP1-g2jK8x5uT8bE3mg9MvHc1eHAvxa7Ust9cSHpDuY0TuIXUcpkD3lO0ABfhEC2smKc-EXxSidYQwgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۱۸ اردیبهشت، اعلام کرد که روسیه و اوکراین بر سر یک آتش‌بس سه روزه که از شنبه آغاز می‌شود و همچنین تبادل متقابل ۲۰۰۰ اسیر (۱۰۰۰ نفر از هر طرف) به توافق رسیده‌اند.
ترامپ در پیامی ابراز امیدواری کرد که این آتش‌بس در روزهای شنبه، یکشنبه و دوشنبه، «آغازی بر پایان این جنگ طولانی، مرگبار و سخت» باشد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75339" target="_blank">📅 22:20 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzmfIfe3Dlgf-U9Ki4ZeWzQhY5zj-bpNccY0emrLFfUDWbqY5FTCDJANWlDoyYfwSMhKpstps6nhvIem0HlNahagCZ894tcY0gBYRjF6fkgkLysHk70jk6264QvXeYQDf84IM1rejJzBVE1QRaChk__TMH4uRGehaMPEKpnR5uIKPDExrd8fOIBwYLKIIE23nQu8VbqxmovDcSxpXaR2Wh3Z7JYrCwjuCjv5y1YiZXXzImspLZZk2IUrNPpcCt3QDTUhfTMkBPdFsJzIUVYBdi0qetPUBHY96QSxJu9XQgFkxxoAcdTUzw-ib3P5srLOlsl-qBiE582ueLVtwkmTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»،رسانه نزدیک به سپاه پاسداران به نقل از یک منبع نظامی نوشته است که  «پس از مدتی تبادل آتش، هم اینک درگیری‌ها متوقف شده و فضا آرام است». او اما در عین حال ادامه داده که «اگر مجددا آمریکایی‌ها قصد ورود به خلیج فارس را داشته باشند و یا برای شناورهای ایرانی مزاحمتی ایجاد کنند، مجدداً پاسخ قاطع دریافت خواهند کرد. بنابراین احتمال ورود مجدد به درگیری‌هایی از این قبیل در این منطقه همچنان وجود دارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75338" target="_blank">📅 21:34 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jUZcbCY1Kttx79g8SwymjamuB9RbeK0lgF_L_J7LUpexbJTZCTkVQjrpvxLKmc7uNbtVQgkl9hGucAQUHzsJ6X5BPKvn1Cy_tQFfQo1CVzEfLdCq1CUK8OqZidvuPxHd_8fxFChzRXNdjeyQvr0XFERNfX4Ilm2GqymYMYUp4Y_BpNB3SIsJ-FJK7h2SdJEWZRkEETls3Fb1-Yxyf2GiZGWmBvmeVYlg0uzDkabO045g6xO3LEyX9wcyczM6Xu6JsQZlpDlwBsdWFFAyBcXQU8-3FySZxBJGcFYfm3nwyIZwgaM90P8KoMpPBC8xRd3G9yqFnwc2VMu5rOL3tA4nPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CFkfnf6_iY_n9NOIudaHqKWDashH5mKxv8i-cgd5FBegyTT1UGO5sWGovAVYZwGxYYWc9ehZnZFIW7-urWgU3vOAnbaOrvT_v6MvY7BcJd6n1Qew-mQwT1WqJjCNrNPPVXConxjVC_HYBKAQWRl1cPMqYpF8-zNjfLgUDnESMinfpSv5wLCmsdmDaIxqsy9voeNrWNNLLwTagJmgTbGunLY1oDbEfKc3IELHtT7mSVR6nreyigZUSxRmg9tSzRM67RRhUeToknPVcDIUsENzRX5dRiLkO_1TqF3BK7KliLZlnXPVe7mncOpYqdqEEAPvjddNOdYDBHTe24LJWi1K-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که در راستای اجرای محاصره دریایی ایران، نیروهای آمریکایی طی دو عملیات جداگانه، سه نفتکش با پرچم ایران را که قصد ورود به بنادر این کشور در دریای عمان را داشتند، از کار انداخته‌اند.
در آخرین اقدام در تاریخ ۱۸ اردیبهشت، یک جنگنده F/A-18 سوپر هورنت برخاسته از ناو هواپیمابر «جورج اچ.دبلیو. بوش»، با شلیک مهمات دقیق به دودکش نفتکش‌های «سی استار ۳» (Sea Star III) و «سودا» (Sevda)، آن‌ها را از کار انداخت و مانع ورود این کشتی‌های خالی از بار به بنادر ایران شد. همچنین در ۱۶ اردیبهشت، جنگنده‌ای از ناو «آبراهام لینکلن» با شلیک توپ ۲۰ میلی‌متری، سکان نفتکش «حسنا» (Hasna) را هدف قرار داد و آن را متوقف کرد.
دریادار برد کوپر، فرمانده سنتکام، با تاکید بر پایبندی نیروهای آمریکایی به اجرای کامل محاصره، اعلام کرد که این سه شناور دیگر به سمت ایران در حرکت نیستند. طبق بیانیه سنتکام، تاکنون چندین کشتی تجاری توسط نیروهای آمریکایی از کار افتاده و بیش از ۵۰ فروند دیگر نیز تغییر مسیر داده شده‌اند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، روز جمعه ۱۸ اردیبهشت از وقوع «درگیری‌های پراکنده» میان نیروهای مسلح جمهوری اسلامی و آمریکا در محدوده تنگه هرمز خبر داد.
فاکس‌نیوز به نقل از یک مقام آمریکایی، اعلام کرد که این درگیری‌ها ناشی از اقدام آمریکا برای مقابله با حرکت یک نفتکش متعلق به ایران بوده است. بر اساس این گزارش، نفتکش مذکور قصد شکستن محاصره را داشته که با مقابله شناورهای آمریکایی مواجه شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75336" target="_blank">📅 19:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPrhpYiD9_xRxrpuPux042scKXwAWEoBRkMDVrQuznhIAxOI48sO52jr_I_vDHMpB2fWc_rHJX7TX-kT1vmwSE5COaIm8du71g_uQAPxVYL7lARdsw4FGt5ClGjxQZseqMuvKEm4gbCPjmjcT0WA797jLRS9K4PqKSLjvW7Nb1GPelPQLzFvFwMdexsNyWfNFyncT842VI3Nqa6dU6F-oXMTaXyPXGDAaOsihjNj2KEnIESJJKuen2uAheWbGENogeWpoxglXjwqV8HCszFdk9ls0lqzIUEcOxwW2KQ4ivkCUCHib7Qf8j59BXz0F_86kX8kp_yUZBgrsoF_f8g9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روح‌الله مومن‌نسب، دبیر ستاد امر به معروف تهران نوشت نمی‌شود نیروهای مسلح، مرزهای ما و تنگه هرمز را به روی دشمنان ببندند اما دولت فضای مجازی را در اختیار آنان قرار دهد.
او افزود که «فضای مجازی به هیچ وجه نباید به حالت قبل برگردد؛ همان‌طور که امام شهید ما به حالت قبل برنمی‌گردد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75335" target="_blank">📅 19:23 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/svRigZ4-w2t8JB8MIMu3HF_5qEoXuuBhds3DgNqjQrGDIdAlt1RTdj7mcA4GLcJ3fEq-AYieVREIoyXTrEUsMaVrb-dYipMyeknchsMaYnjE-YdQ6k89mBg9QAQ7A7jAo2YDAqtObwfD8uN67hsCABhSkAfUx6zZ0Zb9BF-Dt_hgFiy8a2vkdmoXzKtTqBOjfkp-ljxfGMd0Nz3tVj1hj6gM4SFdiA_Bql8oJBndeCcjcblhsDeGUYQGsw0t7Qn7UhYaOln8gEXnxIIqS8B73rHZWLs4pj5-_9ljQ89s7jEv9R4ZVPxvKrwGhYanxV3kZgusy78yJQ8j0N1Pny9-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در حساب تروث سوشال خود با انتشار تصویری شبیه‌سازی‌شده از انهدام یک پهپاد ایرانی توسط سلاح لیزری نیروی دریایی آمریکا، سرنگونی پهپادهای جمهوری اسلامی را به «پروانه‌ای که به سمت قبرش سقوط می‌کند»، تشبیه کرد.
او در واکنش به درگیری‌های شبانه ناوشکن‌ها در تنگه هرمز، این تبادل آتش را تنها یک «سیلی از روی محبت» (Love tap) خواند و تاکید کرد که آتش‌بس شکننده منطقه همچنان برقرار است.
سلاحی که ترامپ به آن اشاره می‌کند،سامانه لیزری ضد پهپاد «لوکاست» (LOCUST) است که پیش‌تر اعلام شد بر روی ناو هواپیمابر «یواس‌اس جورج اچ.دبلیو. بوش» نصب و آزمایش شده است.
به گزارش وب‌سایت «وار زون»، این نخستین بار است که یک سلاح انرژی هدایت‌شده روی یک ناو هواپیمابر کلاس نیمیتز نصب می‌شود.
مقامات عالی‌رتبه نیروی دریایی اعلام کرده‌اند که هدف نهایی آن‌ها، تبدیل این سلاح‌های پیشرفته به گزینه اصلی مقابله با تهدیدات نزدیک در آب‌های بین‌المللی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75334" target="_blank">📅 19:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75333">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LFQ9Fuz0XUB-_WARRv3uZ7qALPaA6BJUGweL8z9fd02dihwQnQxq0p5OxzHzNtkhdfX-uRPowEmJcYstIiJFla4okVjrBZUwb_JfWDAwToTuSqvavFiwglMpBy5E_aI5_nkBzYR4CeO3tXQXFXoq4EDkOZR9_FrFhfkeDpDeKtyShN55ebHhKSfg4-YTcksUmyghZ_BUCgqQvqeJtjKjzIYdvxCWblm4nOwRzKc4UFOgpXN7W6V743-brnF--1SGaVAkMApAmCg0hru7EunQRcaWXVhfgQaaYE-ZZt9BUsJiVkW6hAL168XMbS8S7nVF-N2MCiG2FHDCNc5pI3laQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار میناب: حمله آمریکا به یک لنج باری یک کشته و چهار مفقود بر جا گذاشته است
فرماندار میناب می‌گوید که در حملات دیشب آمریکا یک لنج باری هدف قرار گرفته است که منجر به کشته شدن یک ملوان و مفقود شدن چهار نفر دیگر شده است. [گویا قبلا گفته بودند پنج مفقود داشته بعدا جسد یکیشون پیدا شد]
به گفته محمد رادمهر، ۱۰ ملوان دیگر این لنج هم مجروح و به بیمارستان منتقل شدند.
به گفته آقای رادمهر این حمله در نزدیکی آب‌های شهرستان میناب رخ داده است.
عملیات جستجو برای یافتن سایر مفقود‌شدگان ادامه دارد.
دیشب نیروهای ایرانی و آمریکایی در آب‌های جنوبی ایران تبادل آتش کردند، هرچند دونالد ترامپ می‌گوید که آتش‌بس همچنان برقرار است.
آمریکا می‌گوید که نیروهایش «بی‌مقدمه» هدف حمله موشک‌ها، پهپادها و قایق‌های تندرو ایران قرار گرفتند و ایران می‌گوید که حملاتش تلافی‌جویانه و در پاسخ به حمله آمریکا به یک نفتکش ایرانی و یک کشتی دیگر در منطقه تنگه هرمز بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75333" target="_blank">📅 19:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cBRoBPz1eeC31XpDKiwztSMNGHoG_Yir1N5c0k6T81fLKD1GIbGTWYrE9NqjRaIuMaXe8RAyCaDXTL1eMXFuh9arP4Bk_kj0IyiLRv_mB0VI5oXkjfcuU77S5TRf0t2BLZEfH-2foRtNUKJpx3O85yPKgtmVYt9NtXmppmOvqYpoJaFgeDgn8-bPaOxWBpHMlQjhNIQ_8nq1B_In_mfyPEIuEOYiIwQNIZMxdzZSQxvx57xC3yJVVz5PW886Qax4LAoTVcM0dsVAiZ_7w0MkmU0qxMHZME81HwF4t17yOTsueF6QUYIo7DvIH8TEADflMyJl8XY5l4ulXXkR3jxYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BdUDIzjLhqLuaZLs3hMhhe-bYa6Ry9xMaEYMcdtivoL1ytmOcNJFsmzW6KHZkHFxe-wmUYAr1wGdIY3W7QKKYvLvG_4IyJx7i8BqQKny_or85IIurWxx2kC8uRP9CqJMC87V2U97RFIC1y8I31ZQinUVdxq6sjMhXoEQlkxWJ6F3BXbiYZkDhz1zB5Za0afA0FfegwKJp9Wu28V_fNEl15mNpEVoVy20_PTclWQMWjFCo1ck9sXiD0IIPHyN77jaFxpWjJq8pB8DD5fnehccUDsPYD14C2p8gVIprKLD-k6cfy_MmfAfnlJs5vipbb8AXkXUUV4iqsGa-u3nsJqWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bE4Pq9wqE1eHDv4AF-_39Fao0gwWo8I6ZyEZZ56uok1qpnSlhlH9TfqK1ZBG_RdQyvd8iK8yLnwycCvqCQXbmHJNdU20a02trY9eHw9kr5_Nxt1UW7Ne4ReUhpIiLI1MENpxGMLAuWPXJ2L6RDxyDRFTc9pftBEUnKxodMMqwwQC8xMKRNKj7AsJHwMesGPM7VADqEAAdkw0SxZ-bAVKFiZH0IZYVVh0BxJU0PN9sy3dCEMTSRmACpZtWrIWFiwo2nWsRhb5ugGJpHqim5y_QTJyDNg7rKeH_DqAM1vATcIrVHsWlqzhWfg1t4HK1BMujHl0gP1Ijf7Q7UARPuRp8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=RKjaC0HvG_0x6BW09US6gaBMNNk5105tDLgzecBTGQMIM5Roh4I5zqPDIg3sRic2Rzb-cz5Py1aEsU1K0RMsHVDqXce3ZSsben18hljccKce_RM8lE97w9iHMHWjaY164uwRm8SOVMJuDDKZjfB-w2dkSqky3I8QmC47pi2i4Gf-WR-jCFyRlRpQVMkm3uRQejPhspCPGJDv_UqjXWgPVoT01HP5SUll0bMsplJkMWc2-UfU3pJIbHCERwg4vwivpOWoRjZgIOB60CBm8OIGVzLUNpNsCOMYeSQnfD6X14UjzqGRAdDUtYZPQJYPDDsuDaNVDFuqTPUTrf8pcI_O-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858d7055f6.mp4?token=RKjaC0HvG_0x6BW09US6gaBMNNk5105tDLgzecBTGQMIM5Roh4I5zqPDIg3sRic2Rzb-cz5Py1aEsU1K0RMsHVDqXce3ZSsben18hljccKce_RM8lE97w9iHMHWjaY164uwRm8SOVMJuDDKZjfB-w2dkSqky3I8QmC47pi2i4Gf-WR-jCFyRlRpQVMkm3uRQejPhspCPGJDv_UqjXWgPVoT01HP5SUll0bMsplJkMWc2-UfU3pJIbHCERwg4vwivpOWoRjZgIOB60CBm8OIGVzLUNpNsCOMYeSQnfD6X14UjzqGRAdDUtYZPQJYPDDsuDaNVDFuqTPUTrf8pcI_O-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، گفت اقدام نظامی آمریکا علیه ایران در بامداد جمعه «جدا و متمایز» از عملیات «خشم حماسی» بوده و ایالات متحده همچنان به‌صورت «دفاعی» واکنش نشان خواهد داد.
روبیو روز جمعه در شهر رم، پایتخت ایتالیا، در جمع خبرنگاران اعلام کرد «خشم حماسی» که او اوایل این هفته گفته بود به پایان رسیده است، «یک عملیات تهاجمی بود که برای نابودی سکوهای پرتاب موشک، نیروی دریایی و نیروی هوایی آن‌ها طراحی شده بود.»
او افزود آنچه ساعاتی پیش رخ داد «ناوشکن‌های آمریکایی بودند که در آب‌های بین‌المللی در حال حرکت بودند و از سوی ایرانی‌ها به آن‌ها شلیک شد، و آمریکا برای حفاظت از خود به‌صورت دفاعی پاسخ داد.»
دیپلمات ارشد آمریکا گفت: «فقط کشورهای احمق وقتی به آن‌ها شلیک می‌شود، پاسخ نمی‌دهند. و ما کشور احمقی نیستیم.»
وقتی از روبیو پرسیده شد که آیا آمریکا خطوط قرمزی را به ایران منتقل کرده است یا نه، پاسخ داد: «خط قرمز روشن است: اگر آمریکایی‌ها را تهدید کنند، نابود خواهند شد.»
وزیر خارجه آمریکا همچنین خبر داد که واشینگتن انتظار دارد روز جمعه پاسخ ایران به پیشنهاد واشینگتن برای پایان دادن به جنگ را دریافت کند.
روبیو در این زمینه توضیح داد: «خواهیم دید که این پاسخ شامل چه چیزهایی است. امید ما این است که چیزی باشد که بتواند ما را وارد یک روند جدی مذاکره کند.»
او همچنین تلاش‌های ایران برای کنترل تنگه هرمز را محکوم کرد و گفت: «ایران اکنون ادعا می‌کند که مالک این آبراه بین‌المللی است و حق کنترل آن را دارد... این اقدامی غیرقابل قبول است که آن‌ها تلاش دارند آن را عادی جلوه دهند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75328" target="_blank">📅 19:18 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
