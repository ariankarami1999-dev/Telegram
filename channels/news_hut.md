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
<img src="https://cdn4.telesco.pe/file/vUmC49vl6pGnpCEUl8hOqJf0S-cfXGkzQI3wQ0ASwSLcSn4sSNRvs3m7IEVl3nHzxgJjMQj4cgtzUMsSy3lSot_5Ne3czpGAhB9--qa4_DPhRRBpqNQAGnu9InomOJ_SB5z_lq9d5gUABdcqocttMte7zdc7xqw1kIVo0tMc9tLvEnAuGj5XgkhTFh-ldsFl_YhtdYKmFgPlVn8DUJYlT19wCGse8xC3ZYxZh2K30JxLBbxq-lvViNONd-wDCs1CdSIH3p1IZm2ectMjEgiqcSzvvkUjqblCg26pQm_5gm4X3hEUh7aM8Ce92MMeqZN0d9urzvYcK-xWzqaL4nZVSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ritkojX6Rm8zfHmJ_bSG8VDis8tSW7S1RMdgNaRyFlsYSHEHuMD8mUhL6jsFGeRvyEo9Yoclc7RBn7Ph7mEhpEzvYlcf4YzPEGEfhd_HSRHcOS1HN-p02Q-CKgeC87iQpDkatLrcwkp7cCKcupjh64Kf6J8ap9n7NYxdTu2yIy6WNaCFsNK3Efvj0upsr4CXEGtTLFE4GXCFJy1p1oIDyRUpdErLf_UKHDXzWIb_Zx6hUNTrPrAGoROLcUjRsAvxfU2-ScWV6XylZ8A-FoU3gS_JKTUlQMUWDYjurnD068_gaWXCwpcif-TVR5augkr-3WckRJScBxtUv8IgR3HMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzONjUlKW5dUrqwBhZQ8USEH4E6NgWzSS_r7MnuRuiZMVbk9C8L6ffQMMMPXRjUifj7jHIXFTK6K0BGI-Dm8dWMBzc0ZIsAmvFApLkKdKvQaMSx1IUqcrGaMP31LmJ4Orb4LQtvivWjQoVKQY8rZAVCVpVZ-tK0NBM3xsRswmI0OUjAuTNFoFvceAKSrFw17FeXS48mZ10FJfEIgEoWp98VVUBUtGh_LMIZQUIIfD7kvMad8G37QdQBxlEbwXiRnQL3xQ_Hmu_9GXNM_Ub_5RBp5phhJnSRV33GW-yFlG2STeIRYLUHsPCVnNabSrkHvNEY-2ANT0LshCwNJo2VhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmANSvseZgXSPmWiRw_jxIQgRIC8Ik3SXBdIta2yfqqqhqi-VcvhMgjZfRhvx8eW4qzfbkEgjG2o83rdLvutLRtTJm9Sh6iUWY67M4VwYsyEmYd8ER9topIw5lGPK_2vb_dEB5j7_Pbw1IULyfKoE8y-9HZG0GAEry3owslAGkxsswqSyTUA8ZwiWxb1_aGBdzYzGqJ21ucGwwlOzrjq2EhUD6dI9VhcuP2eOMMi6jkbf0421eXwmQJ2Z0Q-teWmgANiksOchDqR2SRBDDGdkf8vHM4fY0abk-G28rsUiR977kiqwiQLYAZC8OI9LRJlOj4-Cd8sT-2Lb82Wvg2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=oOcNcLVduYBqv1n038tVvMvM9l8koIpz-4TqO9r_oC7sEs1UdNapKqoC7Sm_0krCHdWo-9Bc5P0iZTmwlZ16zaf7_v9-ltuDF0uuli6TU5jcpqR7q5FCxC_kJKirfhcUnxFjWSv6GNxMw2xHdGV5OsrhsWJCpBgcLduJmmOPgvhmomjZgXyFqF0XXpbwHE0kztf2t5JMA0m3jCCCK8IEcPT60xMhlM8qN6UvbucTXc1oJgLkg3zEaUA2lID80KNNmcpt8RLAkAn38TZTPX1FGy-YXxUEnZMtic_-28__bQrE1mjhBxOsHebjpZehBYCfwbWDvgw4Zp-s545i6Lwdpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=oOcNcLVduYBqv1n038tVvMvM9l8koIpz-4TqO9r_oC7sEs1UdNapKqoC7Sm_0krCHdWo-9Bc5P0iZTmwlZ16zaf7_v9-ltuDF0uuli6TU5jcpqR7q5FCxC_kJKirfhcUnxFjWSv6GNxMw2xHdGV5OsrhsWJCpBgcLduJmmOPgvhmomjZgXyFqF0XXpbwHE0kztf2t5JMA0m3jCCCK8IEcPT60xMhlM8qN6UvbucTXc1oJgLkg3zEaUA2lID80KNNmcpt8RLAkAn38TZTPX1FGy-YXxUEnZMtic_-28__bQrE1mjhBxOsHebjpZehBYCfwbWDvgw4Zp-s545i6Lwdpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=beJ0ukUELKF9xM96HSbh6az1F0azkl1OM0lzneh89RT05op2yPidEZfGR5YELrCyGxqx-4aLvASVikKsFZx7PVX-4rPZ-O8pgOapVMVj5cx5OBvS162glxiulTt_3_TZgaPJabQ2FXKK7-y_2BI4Y5t7s76bHe54v7G7RztNPOMKEZL1StrJ1D_9x6IAlqai6uwHmiTlTuxue2HKhQqH_CF8gmi3BgZn13wQREXvsSI23NgF0VQqHbgOmTtzwnWbly-L4hKNzM1wR0aD9_vRPTNDKLimIv2FZXXFMKrYxxbEIeLYjBVYyc5gXWbfC2qtZeFRY7ODcVwYavcNee4EGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=beJ0ukUELKF9xM96HSbh6az1F0azkl1OM0lzneh89RT05op2yPidEZfGR5YELrCyGxqx-4aLvASVikKsFZx7PVX-4rPZ-O8pgOapVMVj5cx5OBvS162glxiulTt_3_TZgaPJabQ2FXKK7-y_2BI4Y5t7s76bHe54v7G7RztNPOMKEZL1StrJ1D_9x6IAlqai6uwHmiTlTuxue2HKhQqH_CF8gmi3BgZn13wQREXvsSI23NgF0VQqHbgOmTtzwnWbly-L4hKNzM1wR0aD9_vRPTNDKLimIv2FZXXFMKrYxxbEIeLYjBVYyc5gXWbfC2qtZeFRY7ODcVwYavcNee4EGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=ec1FUYDnk0_AKcV26Af73mvY2GToWqqqjpXsW3fYWYT2MzveeGv438SOor4AwiBdw6hMpidGRDQK0SrxnJY4oeoeFWwahPX6LIj8nJke66xhcWxgDL_WDg8_Uy8Ae4ZzeSVwrbmf4MqFRUFh367jAbDi1n9mq0Rq0pme58tOrY-TwcJjfXl1GbUlEo_IjhngWoMnTeKgk1sT8a2WXKHOjPT1Cz8GY_Shl3MrRj1tcUoNhbWbANwx_9f_oX0O_lVa2YvFluiVlcsXIOpWLg-Y-tzZmRjKxAAuCdWKLJ54lPnJen1jIWqu3YuhJVxtwg-YG_LRT9q5p228j16nOGyH2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=ec1FUYDnk0_AKcV26Af73mvY2GToWqqqjpXsW3fYWYT2MzveeGv438SOor4AwiBdw6hMpidGRDQK0SrxnJY4oeoeFWwahPX6LIj8nJke66xhcWxgDL_WDg8_Uy8Ae4ZzeSVwrbmf4MqFRUFh367jAbDi1n9mq0Rq0pme58tOrY-TwcJjfXl1GbUlEo_IjhngWoMnTeKgk1sT8a2WXKHOjPT1Cz8GY_Shl3MrRj1tcUoNhbWbANwx_9f_oX0O_lVa2YvFluiVlcsXIOpWLg-Y-tzZmRjKxAAuCdWKLJ54lPnJen1jIWqu3YuhJVxtwg-YG_LRT9q5p228j16nOGyH2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9GQhYWoPG7opZe6Nvqs975y73sJ_dx_tWPo1HbisXhEHrwE5N6b72V-X9_O4VIXNUescwkDaWlnWGTgTmBepCsiY1cre6gVb7nPa7t9na5eXqp8Gt0-Ha8v04xiOdbKCRfQhb4njb2BkFVjXYQr0SIXeIGIuhRAGB6k1pmJZb-zzvtfBNPvFV7zS00_ZLtSUXlpB3bnig-0LdZwZz5LVq19DVIcM4HHI7wINd6RDCQ-DYQRWnvk6Gc4nPUKBwvOjjsTs-jhNxHae86zj_Dl6ZO7k0jV55l6RC1XlbMHcAS_q382_8xVs9TtRuphuPnGymITOLB6Af5OpyRypoT_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=OfE8wbOJTMerljbxhBsZu0q0MpeteIkmyJ9NrQiInIOSHH8jA0fFRt7gRkhOQBI2GLcf7zcTc2rhhXUh448M8S2HxMGidOVPdJnBPKltFEfVzt_ss56k5YrlCjoR27SAihO3MHXhcbONZILB4c30pJpcNJuRFE0KIRdip5KTXarqes5VsGmYd_7YwN9C5_eAcWmMRZ-_YEo6Zrs1XPB0IiayW3D7v-hk-9iQwzPu46-i8Q1Cv1ijWm_qpZncOIzrP6UYHSvo5FbMLx-rYO3_f7_tfGDrnaTMXAUyH9fN2TDWxjQM-CfaWjoby3YmeyBSAK8tueElA014czzrCpLBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=OfE8wbOJTMerljbxhBsZu0q0MpeteIkmyJ9NrQiInIOSHH8jA0fFRt7gRkhOQBI2GLcf7zcTc2rhhXUh448M8S2HxMGidOVPdJnBPKltFEfVzt_ss56k5YrlCjoR27SAihO3MHXhcbONZILB4c30pJpcNJuRFE0KIRdip5KTXarqes5VsGmYd_7YwN9C5_eAcWmMRZ-_YEo6Zrs1XPB0IiayW3D7v-hk-9iQwzPu46-i8Q1Cv1ijWm_qpZncOIzrP6UYHSvo5FbMLx-rYO3_f7_tfGDrnaTMXAUyH9fN2TDWxjQM-CfaWjoby3YmeyBSAK8tueElA014czzrCpLBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Wex88sT9wMdUAqdBZiVC3lZUYImn0_-0f5Bv3-GPf0AY208mu60XRxBDgqYxNMK8OZJ3fXmtE5peoPCFaPqiI3sJpDszThJMUlLM7Dlg6sDEy7X5uAlGGCuKVBOzUxYLlp-x9IyJrpwka5zKDVEOGGaynl7EC5HvSLenBzXmmy6y47BYLhN--F5ZONvJADbe8qNcMqm9kwdrhFzX3Vao-jaLj1zXS5pHVrA_SpGWk-wesTDLc233vRPLjWCHXqzH6OeVyjd7LxsT5TME327DSU6pi6jVsSDzHDDBvqkpYE6zYIm6478stWMbrOBOS5bulVEANDMRhQaFf16USYVqGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Wex88sT9wMdUAqdBZiVC3lZUYImn0_-0f5Bv3-GPf0AY208mu60XRxBDgqYxNMK8OZJ3fXmtE5peoPCFaPqiI3sJpDszThJMUlLM7Dlg6sDEy7X5uAlGGCuKVBOzUxYLlp-x9IyJrpwka5zKDVEOGGaynl7EC5HvSLenBzXmmy6y47BYLhN--F5ZONvJADbe8qNcMqm9kwdrhFzX3Vao-jaLj1zXS5pHVrA_SpGWk-wesTDLc233vRPLjWCHXqzH6OeVyjd7LxsT5TME327DSU6pi6jVsSDzHDDBvqkpYE6zYIm6478stWMbrOBOS5bulVEANDMRhQaFf16USYVqGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzOdNu2lj-6rXeMcFoA9VZp1V_KIFO0BkHv4rqc7ltHWFWLKYZngtbQrXTnG4YyXGGg2Hy9y2LFyOe6uN8kqQM0ZiooEy51BzCsIOsSUon0U549rfxi1vPLDR4Q-vKnbA7gMRUUAG91bChGmt3loF02EcSysdyWYWJQPDhh1RCxHArb4PJ_JbbCHBot9T8B99-IeFbxFAelvMlLYFaOFyt0rAd9-cIvFvICMaSBPns_oCdI0MoxtEVWIkEWbCvtklGkHR9cXFQJD-2u_RY3Gbb2Vwv3irEbVs1zycs3l-CwfTqj9yCxWng3HsIJ-E1Zf6yFTXaW2B5b83tb_UlWpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=le1TCrsP2ZvLP6DyaCjQchYABN-ARjOnyt8NStE7mDd5rMs-A4eWbamlKDfK3EnMDeXgfgo0R3pHRUe-YbZrK450DFprlkySeA6dwThVhKnG_AGjp8mhwH61mDZ4dfTU16Q36VMTegmivbSSYNEBDD9vQM-So8oLV_gTk7r1AJj5LnTJRr19I6DFNr7h_FsmTsLRvW1zSulfnD6kVFAj1D-RQUREMYmr5sMOu_lXuzyqEWORN0d3yyMuyCdG49iVvTwInk-nm9_3JfNc5MtdQnEVrBcEce6oQ0ZW6t9ZaT-0lXR4XXoKsfj0uaT7V1k3utRK16BCFMEKYhLpOSKkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=le1TCrsP2ZvLP6DyaCjQchYABN-ARjOnyt8NStE7mDd5rMs-A4eWbamlKDfK3EnMDeXgfgo0R3pHRUe-YbZrK450DFprlkySeA6dwThVhKnG_AGjp8mhwH61mDZ4dfTU16Q36VMTegmivbSSYNEBDD9vQM-So8oLV_gTk7r1AJj5LnTJRr19I6DFNr7h_FsmTsLRvW1zSulfnD6kVFAj1D-RQUREMYmr5sMOu_lXuzyqEWORN0d3yyMuyCdG49iVvTwInk-nm9_3JfNc5MtdQnEVrBcEce6oQ0ZW6t9ZaT-0lXR4XXoKsfj0uaT7V1k3utRK16BCFMEKYhLpOSKkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aVWWDCNN-vZ2ukjYShV2xUT4Jv7YT3nHxIwQ0d3iygc01Obx6IltFrhqWGC_46WtfDlM6aSLiq5K3M0-31KkS2gRcSKou15qk5cepybmn9fLN6DPSO9qq2NICzLOZJygT_nFRG5XA3MpeiyUN-wefOcDam6QB3Ko8kdE8LDKZPtRGrHA1t45jiUMA_lnSZSxPIah00gPmPthfVro6uoBu1ITbvWSj6R51rtkbryOPsZzIvPzTZhzcQBl4JVK1lhfIFUcgxhbIUA-ZK32DmSBXQedVIlWp_dXfo3mrFr5svxsx8MpWS8_LHFEun50S3BpELTiinu-cDrEL0QvHNCehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZsiIvjX3d6_t1AHZkbCd064-_Uiogf0kLFFXOg4Kase5Gr_71iO8dlmMeXupc3fNsCVvqRUOJT8tEjbgd_6faIazTApbKo9ROKNhiIgHh5CHoygJTBv4Tr660HSTOvA4pwC3J9C5PrFpBhjT1Xz6ybBRTtPbPpSzvmBdYNYeW0Y39oAtyWa5YBItHKQTfp4JDyAlbcrkXhxz37p4m4mkdDNDmuC7k0P3glmO-aH0hMWYHwanLh2YU-SgPa5CNQ_fcZ-U2oAHCvenfTIIMEdOq4nZ2RLXMQsid63HhCN2ffPdMJ_vIXaJBG1xKHQbyj2XesJGYIMaMGp9xfiNfSmmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pt9Xws_zCsd2xDM2z6IpUKuPstakXWG6mlrnrspwks446fCE39k5_ILUXbDHZ4r3XmvU_lcLsQvC4LLpftS0L9hnJ0Tffse81gSVWGBWiMF7S9aWz1lic_naGEYHxp8GTm0Mc4fdKHsg9JVOD2AjB1Qp8yrrRV8hs_7YLZB8GAwIHJMOUBo0SD5qOBG0wmHnknSae-GnW_ykuEuADQnflp4WE42felsPnrt8hzgXNuAL2TpTN_0pc-J9oqccTfgdczUN51WxdJXzQO-Oumqwv242buCzGXafg4KEIXOaW7Ntf-SPL_lv6KYlDFMSYCaCd4AebZk4EqPYZSeNsU7_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YtEPBmtb0edi7molDxe8t8Y_1vYQL150bGZebV_psEkCPui_q0Ez1LcFkMWr14tZ94cGZGvaAh1DIXQLibNeZ-uUNT2xslfOuoI1nRJEdcHr6uDcD7xkiDaRmL2NFqM5t4FRKNoWe45iRvGkuK9V60TvFXovg2y2Rcv3WChpRsnOgbivy0QtOwY3pqWPp-LKLTCIY5cs9FggNvC7o8HiV1Tf7DuR2ABC4Z7Bp6_W-nrkJCxXZg78d92r47Ii8ay740bWaHKj_2L4iV9fUhcAtCHCEmiYDwp_Xz0KYBGYYlvl9_26T1KhCcgl5Y9RkwtiLZWzW_DwdyOoHrHvJ6mTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t559uhyYee_NASDPFLWZcnnBuro2WRBMD45Z5ti9LJzI24b4XOlJ3IxynyD-j-SrL_pIAgI2kMvJsH5Ie1vfZdePszfcYfVsGbJjC2uFEWClL76aUrrL90D4wv8oB2lClSht4ChBqWfJUed1N9s9t8Ip1LpsK1ghVfHbAsGi91Bk_20Wta8FtuPCIfTi_Zp34R9SzX4tlJXzl_4pN4g4eNcfXUuWBaWmV640pwtQfkM06NHWfLRpLNlkFKmwgfDlsyU9MSP2gVcB8CC5iDIv_7Z7pq_vyeRaGj8rU8U_tEEEnR63bbFZDKS9bhkj5O8q_Q3f1yAWwvvteqVdAdAwLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bz1fbC8rOuwh6n0ufRiicBOrhJ2W3GuhOd-6bzfdvBf_I_D4nD1TI0vQP6oP-FZGbD_zNQVkaHIiUCcdmOCMg_g4eieU-uS5aidRe13riK14zs-2YEl4VFJsw8eeKLH1erZb0GVyjYpAp3-mx86O9zit3Idi-OOR7Hf4BReRwOzCMiDnm63WXxGRxNSEftQIJxb8UpkikrQu2-Wq0DUOYimfDtK2oupy86mTG5jfgUw4ETWNOSOIzOJdUXU8expj5TnYGX3IBuSk_NLdbY-TcLTHWZ-XYaFCwlvS7IefCGW1dMgG7ObwEJR-MRg6iMRbPgcmHWXwwJLyBPXadJXfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-AY3qFZ7yNGq_Ff4WAoGPw_WOHStATIZuZESOadQzx-3tT8Qr_cg6lti_GbkeYdo4RS5kv_6c-321S1Vi9Tz5f7k5dyqR2ypTI2X4Bn5NfMkgbXgQaFe36ymnsnqRhFicf18y5Yc8Ts_zaV4gjlY9i4vdd4S5B_4ZxdrDMVFqabjBwZVyxTyF9jIARnncq7F53MOIcygzskM-42GYDiGPo8g6Vi_usVd_c-_ymm-A7cy6-VVBYDU5EOHZ37i1QLtunXgvtzMQRIISERH6dNVWLH13NHu7xxi9uwft28s_lK5NBatqTgJRmWMz35bNQ00zS1qL3aL6iLyEM0CqrzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5-b5b95OC08KmPDvL5LosIF3smD0JmMMIAQ_r3t8wQrhlnOGRC7-fVZ0k0MfhACQQzWlTMQ-B40JgpGNq1EdAGPH_dJir-dTY6t_yfrRYSTVVNBWiGXHXb8iHFviVvvPN7YvTz-xrRO5IyERW_Gz8XW-IbliPGY5V9WxqgVhJFlqPZ4idyEI7DoacQBYX5_hhi6zk_oAdTfzzHdHq-Hjn8Trha6ew3dtTBNkpz68dp4som4eXq9RU5N7qyBhTo10BacqSCzFSUBE2Ao4Pl-xRoEMZig2Riv37ODOsSvYE1Ja7jdGSPo3Sx6-Gu07L3kQHbsbwZdbvknEw6V7GEqNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=W5TMRFPmKmR2tNH-5JTkolfOLAjJ98VGPt4RRTniRj0RRZ3nuMbm5sh9l1kv71EzXpCG0jihs0RJBySS6a1Nfod4AwmGUMXUqYvngej4FL0f2RNoLVBa_koohr1qK-raMcihSq30iuwBjBdPrIHHZE8NVj75tzqwN1m5diIDoasrQnhh4RcnJASE8Rw1fBuJd9YMYQmzbnX50x71JG5ZewD0jA9RE9FnYdHYab6R20-7ZgmHnEvQkpxeDEs610f3oYKVSys2HPYaMOKAqRTgHa-mi_WvXMWZsIMhRYn5QRfRvknhpp1PAddUpw1gYHCKT9fSlo0v2iLHExI56h3piA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=W5TMRFPmKmR2tNH-5JTkolfOLAjJ98VGPt4RRTniRj0RRZ3nuMbm5sh9l1kv71EzXpCG0jihs0RJBySS6a1Nfod4AwmGUMXUqYvngej4FL0f2RNoLVBa_koohr1qK-raMcihSq30iuwBjBdPrIHHZE8NVj75tzqwN1m5diIDoasrQnhh4RcnJASE8Rw1fBuJd9YMYQmzbnX50x71JG5ZewD0jA9RE9FnYdHYab6R20-7ZgmHnEvQkpxeDEs610f3oYKVSys2HPYaMOKAqRTgHa-mi_WvXMWZsIMhRYn5QRfRvknhpp1PAddUpw1gYHCKT9fSlo0v2iLHExI56h3piA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=qHIJn0QecIDFgUDq1VAH6tGIT3_tof6t9pzt346nyxraVPRioLujXUszK2R9x04Y4Bq4mpDpISjWYZygCK2zHxAClSZ0Z6ZGqWkpnXlcDfczmCeqXrY3rmw15WL5yt7Y6gfjSjmVq9ABIvbacKrui0CRU1exszHV0xvFxEFFgLNo1W-Y28sm8gDpGGloNlh2IcGMDk53in0R_ov-kA4NIS4gnG3dTh-92Kj6lAf26X658vRgdOQ0a8eJPboKYJHGn77t0M0xqgfeT2BSs-S30xRxrWU2NVnE8W-_FJhe1m7mWlU5UGQLgZMBbyKpTuQK2LO2HUlsi8Sbh2xiH3YG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=qHIJn0QecIDFgUDq1VAH6tGIT3_tof6t9pzt346nyxraVPRioLujXUszK2R9x04Y4Bq4mpDpISjWYZygCK2zHxAClSZ0Z6ZGqWkpnXlcDfczmCeqXrY3rmw15WL5yt7Y6gfjSjmVq9ABIvbacKrui0CRU1exszHV0xvFxEFFgLNo1W-Y28sm8gDpGGloNlh2IcGMDk53in0R_ov-kA4NIS4gnG3dTh-92Kj6lAf26X658vRgdOQ0a8eJPboKYJHGn77t0M0xqgfeT2BSs-S30xRxrWU2NVnE8W-_FJhe1m7mWlU5UGQLgZMBbyKpTuQK2LO2HUlsi8Sbh2xiH3YG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=NSrGMbpb8OMObJ2CnwmthfApIqfDxbRwINb0fv3VtfWKPysOYngByNku8cgRZG0amOMHTD-yBsT3wTuph3CTJzQy4D80OOUOoxAwzw920UYUtmosu8KwPIcSSYtnt9EVE5uikRHVilCQ6LaM4Rx5HwhcKpZrZSudUDImZJ5-tOISdCPy0KeYmjWM2YG1wrBTCGe4MbDkaC-pNNkjkLtdlCtRDXUZjxgVWtLFRxUMqbnx4mnhp0vJ92VWw1NSu-Y85VVQB3PXEWpNxawhbXM9g6j1hNO0YJm3ctoax5G85CrZj46jpfBHBhXGe2arGZwsSnQdqAA8yh0mv6a2ro1zAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=NSrGMbpb8OMObJ2CnwmthfApIqfDxbRwINb0fv3VtfWKPysOYngByNku8cgRZG0amOMHTD-yBsT3wTuph3CTJzQy4D80OOUOoxAwzw920UYUtmosu8KwPIcSSYtnt9EVE5uikRHVilCQ6LaM4Rx5HwhcKpZrZSudUDImZJ5-tOISdCPy0KeYmjWM2YG1wrBTCGe4MbDkaC-pNNkjkLtdlCtRDXUZjxgVWtLFRxUMqbnx4mnhp0vJ92VWw1NSu-Y85VVQB3PXEWpNxawhbXM9g6j1hNO0YJm3ctoax5G85CrZj46jpfBHBhXGe2arGZwsSnQdqAA8yh0mv6a2ro1zAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=EFx8L5WHAKrToZ3G9YmGuw1NqJ2vQrmHn-zcVjh2HHxSe-kLJvPlvD9oj7FyNI8WPqwqU4E6NSb9O9MqaYGLmICb5WicOQ5Vqab2xaXJCi8Hrws4MgghXPeyIUXA2OV-lQoLp8wnXLVujSfHQuxPiD5Oh7AnNQi4xQTfB57edZc6XKlCwdftTCasVr5gjLYxFVtpbFn544GuauUjQWGgEKkJ_JnxjBe95SUPDK9OUlvtwj37c9XbfwkXo_uADtOZsLu0AYgwjztck-jpCq-0ibTWaijKD1VSyctSOr8kYuohhg2Az6jGW8p6aaiVUgyX3yOnHrfa8tZBGWyUH-7WSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=EFx8L5WHAKrToZ3G9YmGuw1NqJ2vQrmHn-zcVjh2HHxSe-kLJvPlvD9oj7FyNI8WPqwqU4E6NSb9O9MqaYGLmICb5WicOQ5Vqab2xaXJCi8Hrws4MgghXPeyIUXA2OV-lQoLp8wnXLVujSfHQuxPiD5Oh7AnNQi4xQTfB57edZc6XKlCwdftTCasVr5gjLYxFVtpbFn544GuauUjQWGgEKkJ_JnxjBe95SUPDK9OUlvtwj37c9XbfwkXo_uADtOZsLu0AYgwjztck-jpCq-0ibTWaijKD1VSyctSOr8kYuohhg2Az6jGW8p6aaiVUgyX3yOnHrfa8tZBGWyUH-7WSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lerTSedMnYIHbUqzfrxWOC1gfnUAPV4W_6AcanVfVtjtwZRqQEfhgKMWdPPYL_PEfYW4zj2U1lSAWxhmIJaSOILwQZDGMN5NvavVWfuoT_x1CR9D42N15K1lKLUoKHS9X7HU5Lew9i60RYd3vg-uOuyJ61qe9EzRVjqFl_6q8Q-gdSNMyO8uI5aC15pkNHBCofQmLjBSHRW2XEqVU5ufV6iCI90BXWmetWIR3jb4zP4OR4QSK4_VbIXGLoFQlidtXP_ZmD7Bvd7fUpx5n6i1kneYNaAztaLHZ1yWJ5ETL3lwaRKqtG-TOaoqYSOeSLwICQdWvC3K4_LCgyJQtUV8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=AY33DIeiNs8SaHcNcVmMANXSlN7qGFVEtrI-Pi0iDltArys-lvj6QSWZ_JJVu41zIxm_Kr7PvY_3iCxW2gkyaSawT5U43w0ms-fm_7HwZX6ejc0lTSKUXI2LIK-m5ZCGb871Hi-4LXXiIK5_cglz13NIjhUhVLZHe58neH2dX20HVPEY7al640wDHQUQrTFg4-cg83ct78hPR7XiR_aRTQ7AM_5EX3Z5l-2Y1AHseYiXAIV8kaNaQh70-hSb_Ofitc1JWKo55qIlDOlbyGEx6J5yiNFZSxexUX2ZlMHJhagCesC81s186rOtWs01kpRyMlv8mQU0Z91-xVXSnp5CHhm_haTS2MvGcfqgbsbzh_T1ZM4rtWSe742znAOwMGHppQnG8RIOlPVB7uC_JkAazZNNrQvyJBhRpF3MFEbdLUeSMiJhE1vQsxRHN0RoDAxnkbuVLoUOpL3QFGi4w2UV-sBX4Nh6LUKi2AIZF3NAFi5UOZSeoXm9aIFRWGS0MAd6NiCz9VPEawC_YQvaGCFcwNU1bZN9Hza3eQb-SExDdcvTJDmmIye2f1-c3V1wCdn8CjSW89ZDj2_ark4YHkCd8ttJyXOp2uegBmX-TqBqBqpTnBaiVoMLQqvjCHpRemPgJyfIsH8HZbDhDgUUrGfi-MqTOQjA43nLi985lPwDY7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=AY33DIeiNs8SaHcNcVmMANXSlN7qGFVEtrI-Pi0iDltArys-lvj6QSWZ_JJVu41zIxm_Kr7PvY_3iCxW2gkyaSawT5U43w0ms-fm_7HwZX6ejc0lTSKUXI2LIK-m5ZCGb871Hi-4LXXiIK5_cglz13NIjhUhVLZHe58neH2dX20HVPEY7al640wDHQUQrTFg4-cg83ct78hPR7XiR_aRTQ7AM_5EX3Z5l-2Y1AHseYiXAIV8kaNaQh70-hSb_Ofitc1JWKo55qIlDOlbyGEx6J5yiNFZSxexUX2ZlMHJhagCesC81s186rOtWs01kpRyMlv8mQU0Z91-xVXSnp5CHhm_haTS2MvGcfqgbsbzh_T1ZM4rtWSe742znAOwMGHppQnG8RIOlPVB7uC_JkAazZNNrQvyJBhRpF3MFEbdLUeSMiJhE1vQsxRHN0RoDAxnkbuVLoUOpL3QFGi4w2UV-sBX4Nh6LUKi2AIZF3NAFi5UOZSeoXm9aIFRWGS0MAd6NiCz9VPEawC_YQvaGCFcwNU1bZN9Hza3eQb-SExDdcvTJDmmIye2f1-c3V1wCdn8CjSW89ZDj2_ark4YHkCd8ttJyXOp2uegBmX-TqBqBqpTnBaiVoMLQqvjCHpRemPgJyfIsH8HZbDhDgUUrGfi-MqTOQjA43nLi985lPwDY7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=k4TXoXqPxcnZTC91Kwx6iximDeqzVjEB0QFlH8tdgDHgxQHH7z5oXn6vZaMB0wgVEp9GZRQSuX-7JQd37Ff2DOE4FRSq-_xsmCpJLhb62_kjEdv4ZRDDMwzPF2Qpj-mRYbZBuDxXvr3Cs1vG1BoEC1KmnFkQoTMZFo-4zI-35XM-gS3sSLbD2DUaHjti5FNl-mkUyjCebz74JovN0JzrFf_s98W7CEXWvfIojgm0pznTsEior4d6Sr2yBJMD6cXAaDa8A3J8VT-1TX9BoL5Yoz2GiH3szCq9zxXpxXrFfqf7vh5aRQJY7p9HEoy1MNPZOTmOklRCDbqg-vKwz1Socw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=k4TXoXqPxcnZTC91Kwx6iximDeqzVjEB0QFlH8tdgDHgxQHH7z5oXn6vZaMB0wgVEp9GZRQSuX-7JQd37Ff2DOE4FRSq-_xsmCpJLhb62_kjEdv4ZRDDMwzPF2Qpj-mRYbZBuDxXvr3Cs1vG1BoEC1KmnFkQoTMZFo-4zI-35XM-gS3sSLbD2DUaHjti5FNl-mkUyjCebz74JovN0JzrFf_s98W7CEXWvfIojgm0pznTsEior4d6Sr2yBJMD6cXAaDa8A3J8VT-1TX9BoL5Yoz2GiH3szCq9zxXpxXrFfqf7vh5aRQJY7p9HEoy1MNPZOTmOklRCDbqg-vKwz1Socw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=d9cPwO5dCSkJcJ8a-Wt3V5-YCRVy3j4j2mjT3TmIiAoal99xXRNMIEQECqvVViwTNPgiIamOoPDAeEDyMuXPONXxyfeiIdAQasqSpkilOBnmbOjasjvqGScA5VAJxr-9sMCADtnWxhlMvn9AZiwD3pKp11Ds4Cu_opRc3myzxu9Q3J6gP4pwx24Mo57xDE5csW2fveEKLFIUfOEbMs5l8zwMlMUvS6KmZB3380M44oXfLDwbWF67wGccj3QFAnHGdYOvzPxbljAYhgKQ8KE6GECELAeqaIOn-NOo5iyaup-2uLEQ2VeRmm-gSGy6-heBD2VKLeBKCQDJDxisgznhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=d9cPwO5dCSkJcJ8a-Wt3V5-YCRVy3j4j2mjT3TmIiAoal99xXRNMIEQECqvVViwTNPgiIamOoPDAeEDyMuXPONXxyfeiIdAQasqSpkilOBnmbOjasjvqGScA5VAJxr-9sMCADtnWxhlMvn9AZiwD3pKp11Ds4Cu_opRc3myzxu9Q3J6gP4pwx24Mo57xDE5csW2fveEKLFIUfOEbMs5l8zwMlMUvS6KmZB3380M44oXfLDwbWF67wGccj3QFAnHGdYOvzPxbljAYhgKQ8KE6GECELAeqaIOn-NOo5iyaup-2uLEQ2VeRmm-gSGy6-heBD2VKLeBKCQDJDxisgznhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=LoDEQx3tY-2xutJZ5j76c83vwwmcAuuKCfGwXJlXXeYsr_wfhrVZrnSc5vDFKiDoPcs-0ms9gd6z4TkQO0YlGtkk5ZeiDJlpX9XIc8dfZQ8wpOBxEzlggkqsYFX6CZ-v6sgs3t8ojB0lDiYe26lv-JOjCfo2O5xV4Z65fzO-cUytqRkoyIj-Nw1RwrkpM_sLCAoE6Tj5Q5X_TNu9t224J_oJJtrWqqzs_hwUKdOB9SZzq3MNABnMdnYxDhL5oqRk9INbrwA8zwsme9eWywSpBoydxaljEXJGogRZVG6IxlxZE3L7TDr38LjRXVCTiwHyIiDFRFxWFhq_PeCd-KPg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=LoDEQx3tY-2xutJZ5j76c83vwwmcAuuKCfGwXJlXXeYsr_wfhrVZrnSc5vDFKiDoPcs-0ms9gd6z4TkQO0YlGtkk5ZeiDJlpX9XIc8dfZQ8wpOBxEzlggkqsYFX6CZ-v6sgs3t8ojB0lDiYe26lv-JOjCfo2O5xV4Z65fzO-cUytqRkoyIj-Nw1RwrkpM_sLCAoE6Tj5Q5X_TNu9t224J_oJJtrWqqzs_hwUKdOB9SZzq3MNABnMdnYxDhL5oqRk9INbrwA8zwsme9eWywSpBoydxaljEXJGogRZVG6IxlxZE3L7TDr38LjRXVCTiwHyIiDFRFxWFhq_PeCd-KPg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=md6TyJlCg4zQXmSjrvrGu3IIgooD6bVp8xVB-D2ddneJw1FPsxuc_GcbkEkGA9nwo47-dUR97KH5ZbAHaB6Az1sttSXpJBmZW8IpwsF_bi9gcfYqH6ibSAUrgx0UdxX2Og3oyFr_Nfptcx4eioM8ZuSVVJMTghG5fGVFQ80I_5g0X9oSv3rjY-74dmbT9dUMlR6f-_m6TrFaHHgGvlwK9zTLimAa0Ouxy3OWncSlecOXzNamYixe5LESnZiM8rZn5JT2jp9if1Bbwum_noExkU55A2z18hQtrRezaIYryxU9oVVSsUzZjS6xOFSaByovjrbILLryfot7MDZWex-5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=md6TyJlCg4zQXmSjrvrGu3IIgooD6bVp8xVB-D2ddneJw1FPsxuc_GcbkEkGA9nwo47-dUR97KH5ZbAHaB6Az1sttSXpJBmZW8IpwsF_bi9gcfYqH6ibSAUrgx0UdxX2Og3oyFr_Nfptcx4eioM8ZuSVVJMTghG5fGVFQ80I_5g0X9oSv3rjY-74dmbT9dUMlR6f-_m6TrFaHHgGvlwK9zTLimAa0Ouxy3OWncSlecOXzNamYixe5LESnZiM8rZn5JT2jp9if1Bbwum_noExkU55A2z18hQtrRezaIYryxU9oVVSsUzZjS6xOFSaByovjrbILLryfot7MDZWex-5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=ZuQ5Ihi_2iuhJbOtDhglBOoiGuAit24XHcdlGQDtXXuevF_05nCChealQqoyWTPEFxZigTBcJagK7eaope_Tqq2tYeWSw4U0eAV-4Ok91X29XDvqHMnQ7hhjohV5nPiwLVTN7TEdIpyS2McVTRIMUEW54tsETVVZ8EJDxIJlJmZeLUsY3kPKDBkLJS2nNJHzx-1oPGardQhk4A7w2CT_DLm-FIKL_Dqlol0H9HALeUSRzDZaH4F3_p1yEpebY-wYufVYFyXqu35zXB-yHIAej4QORpZW_jYOxcfZichboDMOEatiUsHYSSVMxdzxU0RNxQo1-FYKp0VIjNcY9EQ2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=ZuQ5Ihi_2iuhJbOtDhglBOoiGuAit24XHcdlGQDtXXuevF_05nCChealQqoyWTPEFxZigTBcJagK7eaope_Tqq2tYeWSw4U0eAV-4Ok91X29XDvqHMnQ7hhjohV5nPiwLVTN7TEdIpyS2McVTRIMUEW54tsETVVZ8EJDxIJlJmZeLUsY3kPKDBkLJS2nNJHzx-1oPGardQhk4A7w2CT_DLm-FIKL_Dqlol0H9HALeUSRzDZaH4F3_p1yEpebY-wYufVYFyXqu35zXB-yHIAej4QORpZW_jYOxcfZichboDMOEatiUsHYSSVMxdzxU0RNxQo1-FYKp0VIjNcY9EQ2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=pPptVCpzwQSzyTPnJvHDXkZ_wG4PbIyRLryqsgDuXGq2HRxCbeapPB_I9rf6mOQrZWxVQvnQJdaG24IGD3iDwGAJKWUuDq7xt_mhnv1mEDbI_7O9HD0ks0WQxPQaTq9wgno9AadU5S6gB8dg0_RYCVKV9wUhQP1pNhpshHQbOSsbypJjZymYOHwPee0n6lvkvibgEKD-A0Za1i8W_-LDJoj_84wtsRaeqKZ5VehSa3w31uMA6C-1mfK2PLCbD5gH4V2ZrxyXugYJBY60bgyaVKz4LUwU3E3ausz4uOcybDZZPErUILAgoOlBF_59jSdPdf6Hie24sGyVqmqBdNvSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=pPptVCpzwQSzyTPnJvHDXkZ_wG4PbIyRLryqsgDuXGq2HRxCbeapPB_I9rf6mOQrZWxVQvnQJdaG24IGD3iDwGAJKWUuDq7xt_mhnv1mEDbI_7O9HD0ks0WQxPQaTq9wgno9AadU5S6gB8dg0_RYCVKV9wUhQP1pNhpshHQbOSsbypJjZymYOHwPee0n6lvkvibgEKD-A0Za1i8W_-LDJoj_84wtsRaeqKZ5VehSa3w31uMA6C-1mfK2PLCbD5gH4V2ZrxyXugYJBY60bgyaVKz4LUwU3E3ausz4uOcybDZZPErUILAgoOlBF_59jSdPdf6Hie24sGyVqmqBdNvSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=LR23HCrn7oKwnnfI6IrpzVOtmMjhehr2yCm9p0E-dl0Zx072i8-lUbTdeYNHxnZIcRsenkv0UaD6eFBf080PydrYhsNe_CqC7zI9lFrT-3_plIMz9la3rUyVXcH1ysYuTJG6krwRZQeLKkcnYF_Cxx8Rg1gSEioeib9E1qbH8fSoHrTBgNg_L4FwUsUbEi3ogNxsQFdzjBzvhBiQJt6KbIrIHUQpmXj7X82ZzLypymzjIfGGvDFXEYAvATZyDVUauOsE43uZR5rOs1Fi8USPPXaaCRrbW_cWceHANsa7voAq2BjI1HmFF9R4MjSXGBiF-f5V25HrzZzojAPF-g2NY6xWf6V0ABmWNOmyOQaOlRSw6Ez6Tra5K910ylimu3ksOgXyOXOXmXEyf4_wpzdFJo0b4u18_vRFP4iSL_1iYoSBFEXLS1p7yVBkSXeRNiqafZfLvbZSD_R2sBdVBq8mELE7F2L9bLixfNLxqNs3mlsGhY6A-GPh0Cggq7O856gpZVFQFH4ZY32XhbaseF-IcPGblQUTqY8LWWOIZz5u3jMkG0TFNJqtZTBv-SbXLK9vGquwD7p6037mRtSSPcfrPvUiyLxVX7oA6-Ri0BODNWHZ3CpyuxqzqDKtLt0IAlcaTg9KfkDCThU0Rg-VAFWyMnVnvO8wRDtSzlUfF7dtVN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=LR23HCrn7oKwnnfI6IrpzVOtmMjhehr2yCm9p0E-dl0Zx072i8-lUbTdeYNHxnZIcRsenkv0UaD6eFBf080PydrYhsNe_CqC7zI9lFrT-3_plIMz9la3rUyVXcH1ysYuTJG6krwRZQeLKkcnYF_Cxx8Rg1gSEioeib9E1qbH8fSoHrTBgNg_L4FwUsUbEi3ogNxsQFdzjBzvhBiQJt6KbIrIHUQpmXj7X82ZzLypymzjIfGGvDFXEYAvATZyDVUauOsE43uZR5rOs1Fi8USPPXaaCRrbW_cWceHANsa7voAq2BjI1HmFF9R4MjSXGBiF-f5V25HrzZzojAPF-g2NY6xWf6V0ABmWNOmyOQaOlRSw6Ez6Tra5K910ylimu3ksOgXyOXOXmXEyf4_wpzdFJo0b4u18_vRFP4iSL_1iYoSBFEXLS1p7yVBkSXeRNiqafZfLvbZSD_R2sBdVBq8mELE7F2L9bLixfNLxqNs3mlsGhY6A-GPh0Cggq7O856gpZVFQFH4ZY32XhbaseF-IcPGblQUTqY8LWWOIZz5u3jMkG0TFNJqtZTBv-SbXLK9vGquwD7p6037mRtSSPcfrPvUiyLxVX7oA6-Ri0BODNWHZ3CpyuxqzqDKtLt0IAlcaTg9KfkDCThU0Rg-VAFWyMnVnvO8wRDtSzlUfF7dtVN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apiee6y2ZPrSJbu1xKkiYldxCVUGd6qUJdg3YWe1OKZHoQGil0GapJeX21kBO-Kbbow4m6fYLtPeIozPZ5RFuUvifGXVsR3BfUHXU5qatgMd3nbzUXbVDFXQwdBASlG4Z4FRrdKbZSfY6FboHupM_sOyOzK-iqvF7j5P7UZKPFlciXFWWdvrZX6YX-X65MsJl61Pe316ittdTgX0YIturYuT2PiY96KcraFn2WsXkNBkZZibuXojbIodICSTOMFgtSyJ-sl7ljLZJu0XeAykFHX28VxuxluJttpdBscnT5JPSZFARn1DAkiNZbN1PxlbLkFhMPcZou5WbVIBhw3osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjXEzXm5OpVFVaE_db-WtyWrLeGqJd8nxMYt64JSushTsEihaqeBZRqYQhZOtj213c55grFdIHmBbbX4l2nDGoeS_7Vk1CWFbsZCEW42Gc2Ik4a5iKl1ilGmS_WndW6s4Yps2E__8W56unq6jgF6OO9FcdnoI2CJinh0U16gN1Rjs2OKac0mgEBGqDL0jqn15XF51-675B2QXWb9w4CQRmO9jBU_7pDl1EwPLyq49T4Soq7qvPwwxlAArkuQXek6dEnkEJujHG5AnudO6__M7yrfth1L5hhGtY7d7ad1Veq6jdAVTolKC16XlPeQ5wnFphImzcPDZI3v_TiadBbfhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAcPkJOZ8ke2Ek6OATSFXP1eSUXYhiL35catWjo59ej6Mcey9W6G_0VH4yGJryrwVm9rkYu2z2R6aRWL-LhdHqWEIr9Gz7GV-7-NITUMCJlKqwybPvjHvER26_obS53-zcXUzgMBC72nAUNvoBQwgONlpXZoufVh06s5r_m-8jrAztd9BoQMUHxtAZ20v76mCD8imwmOWJH5CZVzoD_-ZzGDrgfXftEkTWWqXBWbb3eEJYQjkFlukY8mFfU7xJ6EGwDsFskKVUdOQddZxcwSoaG-ofD32pxnBeYPoLePPTxULqh3rAkNSei1mQ_Bpu3SlQF-MgwocSj5nfKcwBzctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojR7vSyCB-2nGq7gOgUtstA-guKpfUhftYST-FYRwKofTH9Nlobz3VgK3UPVFX1z_VEwb5bBewbykNzkJrsgL1cwmHq5WGall0QzNtqvdFn3Fhn3LGGmPgayqib3YisGZYCq768lcfadTxoiIbu0k2Yvjdi0lvcWEYl5O8hvLOv7Y84FE3MqfOvLuwPS5zSP4HUCRNn7GVKYw2nk-WUXq5Nq5toYxnTLrvB3t4dQsNZY5hoDxL0PE_krJQumzIux1HtSHx6bt3AU33hH3aGmjU-wX5vYX0LK6P2NWoc2G47KcJ3jd8GChlXuOHLqqPRbNvbnoDt3B865vzpo3r7WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpZHDr4jJVnvyuJtVWgivT3M7jrfJMXzD_NSqH7oqKbRrH901E1YHmLyw2Ybih0fI34fzGanvBlgWZvzeawjMtFk7gCsBz6qyt-mttt9_bFlkgUnEsrBDjXLZ4WhsTg8FwRXvhY_HMmdaYFuJS_8Mvc-8wzZPZKo7LYcihmTkokfiRrJRS73R0dkCRO12oyFycmFkWapNbw2HqL8uOAXQLN7j70H9ywtIEPc9wXHEe4yrNg5kw36ICRlbcAfqwUHY3vygpq8OsiljFK2gaZgi2Do70Yg5zSw43P9RifPYd5z9pmA08ZXXsW0Mo55ZnuZkfsULe3JYy1UENAucmDtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pp2YOb79Nlou4tE64usHV5LayFbZxOlBYfkvHYSW8VZsRtXcIyM_aTf5mJelC7jwKZ48AMF8JtmFhLlgQi1AljM23tFPmbccnpf9Q6VcUhPJ-0TfROZYUeWyOQU7pIihMCAvlSBFEhkF-ALAFeAMEZfx5lsdpiYODZ2XtBokfR2bc2dwk5YKiCIqiGB4n9GNbYRtfOFgeAwXo73VI9BoHTmcMEbJa5lyHdZ9GuEkhtb0wq4GTvMDpI5fH4rA_y9qzmrwxO526sbdo6scJoB34u7et1GeHWkfDuVAvgyXTejyUvDEj02NY-jcKaw7EqeVWLgrcqxtkAqhDWRB386mzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=RFYOI9ff1f99GRl1LaFJJCBibPuVqbipcUQAJNXi4CzSBP9kquCrct4cmcbPnqKC1VO0j2sXVEplAUL2TOR1HXD0NHJChG77p8pb3V5M2-6PBtq_j8loRr91DwiPmo4oUvJ97wDMfzxjo7Qc7mU15Hn9hc28wFP_DKmt6nlvwLNtV7zy7MLyaUWwn04yDCq5SxB6LFze7ZsHVg58Jr_RS6-hIgyLJgPJVX2pUZym61DXIT57jB4UI9mX_ZhxUKvBpzNla0_pMgRSW7iIbrajzfm9VnX2B7ECm9g1pLRNAMVxxp4rUQyX7e5T8YjujvXpO-8kLQApcnL6GfdiF_nHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=RFYOI9ff1f99GRl1LaFJJCBibPuVqbipcUQAJNXi4CzSBP9kquCrct4cmcbPnqKC1VO0j2sXVEplAUL2TOR1HXD0NHJChG77p8pb3V5M2-6PBtq_j8loRr91DwiPmo4oUvJ97wDMfzxjo7Qc7mU15Hn9hc28wFP_DKmt6nlvwLNtV7zy7MLyaUWwn04yDCq5SxB6LFze7ZsHVg58Jr_RS6-hIgyLJgPJVX2pUZym61DXIT57jB4UI9mX_ZhxUKvBpzNla0_pMgRSW7iIbrajzfm9VnX2B7ECm9g1pLRNAMVxxp4rUQyX7e5T8YjujvXpO-8kLQApcnL6GfdiF_nHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=HZJJnIHiFUVTuCbUAkclpeHJRVJjZMAB7_Twk3qmrrGDJgmuUM_SotUIsXFVl2bbDgSf8JHp0elLCm4xhf2EcY8ZkCTZIi0hi03iI9cSjBBG2fJ3HzaKJv3EqUaR0tjSijWD--UtDpMaMPR0URxHuS0nUddxdP1x3x6tWeqAJ45wKfCmBI3t7r2EjWKvvxMRkKebLll8uD99WfSNGzPoMtspLHvp-wClW_m2QXlWyaG3Rlt6CUo-nMcvgglyKf2y_eyEm0V5ZF4dJZ3oqEBYHDT1w9ge58S44qVnqLrXHCfZXEtYsNeseQJIm6AllIZ3X3dJnmwi66cs_uBOvmDhMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=HZJJnIHiFUVTuCbUAkclpeHJRVJjZMAB7_Twk3qmrrGDJgmuUM_SotUIsXFVl2bbDgSf8JHp0elLCm4xhf2EcY8ZkCTZIi0hi03iI9cSjBBG2fJ3HzaKJv3EqUaR0tjSijWD--UtDpMaMPR0URxHuS0nUddxdP1x3x6tWeqAJ45wKfCmBI3t7r2EjWKvvxMRkKebLll8uD99WfSNGzPoMtspLHvp-wClW_m2QXlWyaG3Rlt6CUo-nMcvgglyKf2y_eyEm0V5ZF4dJZ3oqEBYHDT1w9ge58S44qVnqLrXHCfZXEtYsNeseQJIm6AllIZ3X3dJnmwi66cs_uBOvmDhMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SG-EvRjztu3dcxl8u6QlKHjeadMb6oF5QdOUHF_4GBulLaTnrzakQKa8GQGEac0XmMo84T8JvmSZBRlBru2djVHcK0XTVxlbFUOcyNYyjsEFMf4LYdm9Vkg5R9EQWkGuzpbM6iLnv29Wwhl4rhk7YJLFDjB3HrHOc75t7k-l_5n3hkjM2m1gzvn7wjHBSHrT_3APdFd2jpimHgvZbW1vlXz9IpGYKzUes8T72X94zEBvYVTdKJtO1_s2rms0becJ6FDLNTMvh3S1ptaR5WXPYlZlV3BSH-dOnGTiPFVg6H5dgh4zgVoN8d2EqZ-Esci96TyID1l2J-_L8P8UvymjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mig9Vl5i-XCTvYyK2BNmZQtEE1kRbq_ptSNSzRQ4ov59hkFyh0DEvedPwYGZZC2Q5O6rf7n2a7oM-95DaBfRm_e8gnu1VcWXaiQwD15RbCKKwASHDbsdPitWe3fluh6JueeUzGfLfw3dSub7vV2XUHNP-m6qJQUNGYXFRjEqtoWTFe0vEn3o2rQAjGpacOEvo27mAvO56klN1umSZf54rMxTdh6XtBe3R_8L3hcBDNC288ToGRpGTF_3989aLFiwAPzRhM0554GwNYlplmP6NH07-c3R0kWwNKD928R2bBfWZHJO6g8WLyMyyZ2n0sglMzuL48Qfou-s4lGFW5qcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/strSwdeNOx-uLx-t4ObS-IbdkygXGRIJUY8zI3SsD6ofZySkUOrtJCsnhq2IVHCEnB-sedRLuFo8LoiFcNqDWwxHLJ9ghvWesDRFOAQ--5Wv3jIKjmxVZ_ETJNiFS4YItJBj9odjl1sqIxLBpz7NmUEy9a7qpYc0G68IOIISQS5LchMlUrweQZWPsuNhLNn4f6z7Ij48NMmVqO3deKdTdxYBOQZ4DlCm8EgtrEm1PcGMiJlOvqUgwfmQxU-picO4HEww4-ogzCpoEsodkYcjK1QD9DZTQryg5uBmUESYi5pGPejlmByMSuQ7bTPxnC_I6OOrny8X-zRVt-UvMF7_9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=ngpuafns8wBZUJ5oL3vBqbgRBsO_qpWy8s2iwdWTiKcwNZWvx--HmC7NQhMOo5Y4bl9ZbQFXyBerREtl4Khn3RMbxDKUZpRrMHcWUQbztyO4XcCcPoSxlMV4-OwkmRBsQAzzXpGw6E_IEjwOOtVqmD-h41W3_5MNd78jqN5-X86scS2Fyrmo6_D_KxbKGG8Go2hCkX0lHKq95F_V7VwkWNKswGgD9E5htrELDDCFWXg5SLxCypVKQzhReRrP2W487SkPYtDhOmFwxU_weB7HrxMC3eduURjAGp_47GGRl5wA3RvpKFo0PVuzxtkt_YEMuCwMYSpCo-1Gvx2vsuO3nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=ngpuafns8wBZUJ5oL3vBqbgRBsO_qpWy8s2iwdWTiKcwNZWvx--HmC7NQhMOo5Y4bl9ZbQFXyBerREtl4Khn3RMbxDKUZpRrMHcWUQbztyO4XcCcPoSxlMV4-OwkmRBsQAzzXpGw6E_IEjwOOtVqmD-h41W3_5MNd78jqN5-X86scS2Fyrmo6_D_KxbKGG8Go2hCkX0lHKq95F_V7VwkWNKswGgD9E5htrELDDCFWXg5SLxCypVKQzhReRrP2W487SkPYtDhOmFwxU_weB7HrxMC3eduURjAGp_47GGRl5wA3RvpKFo0PVuzxtkt_YEMuCwMYSpCo-1Gvx2vsuO3nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=bM0y2KcbCLw5clddN2RSPgaqTD2S7PleSEMI_9gqq_4MPc-RwVKaVB2VnYskhlnM4OEIJfcbZ_HTO6bKP1Qs2e-AW5Cs-RRdQcW8SihB0DcD7PWTjj2xwmmlX6MMmEChrZ0qhzgKU80qNWdFGHliCHLL2MOvMizfLPGIFLO5yOtdto9XBpAdFPCgUsIhVpXy0lu34RCu7yOis48CvzSfcGcGhcs3Ale4qKWrsZ0lIqqaGk97556fYP-gTGLJroPS1Er7jP7z6dGFiIDiB46bSZM7bX6n3-eEQX4MFu4bGhlW99-tiNQmED08BankhVssVbyVifp4gGqRBvYUgXflPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=bM0y2KcbCLw5clddN2RSPgaqTD2S7PleSEMI_9gqq_4MPc-RwVKaVB2VnYskhlnM4OEIJfcbZ_HTO6bKP1Qs2e-AW5Cs-RRdQcW8SihB0DcD7PWTjj2xwmmlX6MMmEChrZ0qhzgKU80qNWdFGHliCHLL2MOvMizfLPGIFLO5yOtdto9XBpAdFPCgUsIhVpXy0lu34RCu7yOis48CvzSfcGcGhcs3Ale4qKWrsZ0lIqqaGk97556fYP-gTGLJroPS1Er7jP7z6dGFiIDiB46bSZM7bX6n3-eEQX4MFu4bGhlW99-tiNQmED08BankhVssVbyVifp4gGqRBvYUgXflPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=S6zAPh_gKW8WBL4a0hUQ6uKEbasJFbo9IVDiYiqjsT3d5H7FgR3FCi8iIrxIvpy7ZIheQHDrN6pe691zK5BjLgxnmgqEA8GY4Wrrt2XUlPUIaIU-JBuMZZV_-bMO8RuHzFyGNenooovlt2EIMtoelecFBG7_bZ988Oa8DtAs5zQJSTKjO3qEltkRjOEI5QcK51vFa39xyadcsXjsD0ZLvdO8-6lbPCEiyY7TD23HSsEGx8rymzvA8-Fu8VCxuExrlVKjHJC3dlRn8hFVRIQ8nbiTHIiVl-EpAyrXD1O9jhVooeiqAYODHJrrOZ-lqdxD22Nn4btk3BqS4WhzdRZXCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=S6zAPh_gKW8WBL4a0hUQ6uKEbasJFbo9IVDiYiqjsT3d5H7FgR3FCi8iIrxIvpy7ZIheQHDrN6pe691zK5BjLgxnmgqEA8GY4Wrrt2XUlPUIaIU-JBuMZZV_-bMO8RuHzFyGNenooovlt2EIMtoelecFBG7_bZ988Oa8DtAs5zQJSTKjO3qEltkRjOEI5QcK51vFa39xyadcsXjsD0ZLvdO8-6lbPCEiyY7TD23HSsEGx8rymzvA8-Fu8VCxuExrlVKjHJC3dlRn8hFVRIQ8nbiTHIiVl-EpAyrXD1O9jhVooeiqAYODHJrrOZ-lqdxD22Nn4btk3BqS4WhzdRZXCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UXL0TyC7KdageAyUe50dntydU1PAPqruvikvWKyotLWx27qN2u143TGvAvDTjAVQ_1wXqz9BXH1P6H6OyxaQfglkAbO9mbCpUyBFfwm9ZwdD0sXhp-KrYSWPSjVnm5JD6HxuoLQ8oCHP5ScmJeSRE7Plo6YLSaJdmTbk_plbEmcu4u142VliBi33J_8DlHBQYCnisJHDTayn9_fKAZClKRDemXSPyzQYOu6OBDM3-LcS3dbxNLZ0ygHt9vPOFmBjHcNKFK_PDXrfIBGhN0MrkhzWM3gRH5Y_i3gTLToRJ8fJaiGLF55Wi9qx93einhTWro-YCE0peRfj6nY9nLSojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StT2wyU2Jkpne5PgqT8__mwcZonrIulotWSMf15CUrjFUKfZ3tJ-Ly4VHKtG6U7_jdffIALoCCL5F_jwKWuKoUM6EiRgqpXblLXrtSoJg_qK0jMM2Avu_B9J9EMZjj2rDR7VX3z-N_GN21JFiQajGTIbM1z6eTLJftpYLcEfyydl6Ipns6Uo3HBRTiwVlQ_BoTIMBpudoXFGMa7eDYMcs2nlOZvZCH0PFyd7vOD1RO9NYNsVZiElApM4BFShxjBpzjfVYxB83teDgR3YW7G1ap8geb0VTSsA7riI9C4AgHv4jmskTPTaf4KyPDb3nx8fcvd1y7jgCE6I8jgX8xFWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=pSrenixG7ysOdnLazBCZz7SbHv8DrZZyOzS530vkC0yQT4nzArY9CHtnZo8-AYx153q7w60V2s0sp1K8oioulaXMDMTwr-WZ1YLRwXtPtKzmy7fx5oRN4lGM2oIGE3l3CslU5of7sd1Btxcp7mBSFzw5aAzgDRnYZNeWgR3jGx5gWmJv1cAsCsV_ah7w9-WE9JW7ZjhSJEalnBXucG-W7GW18kxhnX83uclVRiut1BPCBDGHxbx2LL0hG6g5qKB3v5ZAPfO4dxU5wcomdEtjzDYwivPghftzpafTJcYSW9r_9wykKp2sxDNQiGylrpys1RWzZV1ycx-Tbtc1mZ8OYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=pSrenixG7ysOdnLazBCZz7SbHv8DrZZyOzS530vkC0yQT4nzArY9CHtnZo8-AYx153q7w60V2s0sp1K8oioulaXMDMTwr-WZ1YLRwXtPtKzmy7fx5oRN4lGM2oIGE3l3CslU5of7sd1Btxcp7mBSFzw5aAzgDRnYZNeWgR3jGx5gWmJv1cAsCsV_ah7w9-WE9JW7ZjhSJEalnBXucG-W7GW18kxhnX83uclVRiut1BPCBDGHxbx2LL0hG6g5qKB3v5ZAPfO4dxU5wcomdEtjzDYwivPghftzpafTJcYSW9r_9wykKp2sxDNQiGylrpys1RWzZV1ycx-Tbtc1mZ8OYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-bH_cCLcFLGfS74VFZ6nrkhPGPlu2njQ9P2dG_rdCLOWGeqhi2mq9-Huv93zJYb5X8ES1-xH0LaCJYsLSHupp-Oy7xgTVSpFkIXNJeENJuB8XTKEdSmOQ_omdjsMOudlheJGFgBC2lHu4HlVciTj4mSQoseNCdpSZ3SIFI89hzs5tp8kSXb44eNcb8A0ov2Tv-fDg9UMP8XT0f84mMVlKxWmQj0IBjXnaM6BYr-pJMMa78GFOd5UH3gSruzLpN7aRht3nR67Hzqod0XiSWAg22ov-VA18JE5BlNW3_7D3V23CtZj7PUXTO1k8jFTGOWHysvZbkTWIRhR7qNprcIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=JGX81qubvGCmuxil8vQQ6nvU5iMQc5X1U58O-QuJEi13QHlUCuAkIcJ2D-l-yoG7EsS0q4Jqt4hRapUMgeEYefynWnzsQxv0O0_QCiajJfXrsjDbFibtoe-Mw9p1ckiTsTG1ggD16boR5Yj179txAGYimnUlm_AtGevW4aEzukXg4XE7a7H26NnodFkhGDilof1Wn0TYaMX1PgWaLvchbydvKgvkYvTKJjin4E3R6XypWRWtztT7JCN9YeQVd0RP4dMm8hLsSgklS2_p-JFhksf9KvGJg7m4T5m5nw_qzu-n0NDUDl6jF022NfXjELBQSiwPD_AX8OxVTPVxN73_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=JGX81qubvGCmuxil8vQQ6nvU5iMQc5X1U58O-QuJEi13QHlUCuAkIcJ2D-l-yoG7EsS0q4Jqt4hRapUMgeEYefynWnzsQxv0O0_QCiajJfXrsjDbFibtoe-Mw9p1ckiTsTG1ggD16boR5Yj179txAGYimnUlm_AtGevW4aEzukXg4XE7a7H26NnodFkhGDilof1Wn0TYaMX1PgWaLvchbydvKgvkYvTKJjin4E3R6XypWRWtztT7JCN9YeQVd0RP4dMm8hLsSgklS2_p-JFhksf9KvGJg7m4T5m5nw_qzu-n0NDUDl6jF022NfXjELBQSiwPD_AX8OxVTPVxN73_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/og7cCaANmArWUc3rpC4KqfycihGwrSQyzVCbA7be6K_UrjmeUjuvAZTgfaHRuKSECYiFwR82dMz00qZsi4Y7GGCdGmeQ6cg_Tre8xKjzl6ABwFNvnvUlGO_Tn9AeqzWL3IIYGpk8aqYW3FaXzcfXWFslQE_FHFp3D0q7YtnrC7UxmpkvtYST_ZFbgwzUJiCthq2oHYeXwTMhYTNotkyf69hMT6Uzban1wqiZPszxPeZEFVt1NqDD6BdVsm9uBEeUD70Kmu_q_AkoGujMkH6dr8RozhzmCnrvklNmQaKUQJLYLqMYmG4hNKBIZBcbN2SyVKvTBMvUbLkGi9GgTjOdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=Qw-6N1HP2Z33ENu5FXQbFhtdfnBNTvZld4M_CBdZrHm9D1e6SGmEbU-rwxBRNcK6yUWkG6S0YX8pmL0jsdJ0l1A_rK0OJPtnnWnBILnfW_5okOy7eQ3DNtZtO-MMiGaDnPpvTiB23QLzjJtjvyfo0heL2liPnZ-BTmoFxWw2W-F17l4n5y8w5iL96ZEh9dTUHnGLAE3o8Bud5IbumTC7foEyt6Qj-CBRlt5qUHYHjKhfYj8dQ4t8itRfU_L1Et2mPeLoCu8Lw9I6rzYpdX72-9FpoXt9gBWWV9L0eLiOAdZcWyevp66mmvv4pVFZFLjWZYs5p9HlsTzBH_OUr8uqbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=Qw-6N1HP2Z33ENu5FXQbFhtdfnBNTvZld4M_CBdZrHm9D1e6SGmEbU-rwxBRNcK6yUWkG6S0YX8pmL0jsdJ0l1A_rK0OJPtnnWnBILnfW_5okOy7eQ3DNtZtO-MMiGaDnPpvTiB23QLzjJtjvyfo0heL2liPnZ-BTmoFxWw2W-F17l4n5y8w5iL96ZEh9dTUHnGLAE3o8Bud5IbumTC7foEyt6Qj-CBRlt5qUHYHjKhfYj8dQ4t8itRfU_L1Et2mPeLoCu8Lw9I6rzYpdX72-9FpoXt9gBWWV9L0eLiOAdZcWyevp66mmvv4pVFZFLjWZYs5p9HlsTzBH_OUr8uqbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=WwuhitB0wqU_hzdItHyGgG6aucDBRA7p9Wgo7EOm92m6Y_p3ykK72h0otrEErpv05ktQaCIktNFfg2hCjOY3Fnw3IA-NJ3audsA0M1kIqqOPnIawkW2hIQKrfxtxpUURMKzCtU9o8sTOvgNYND3SjyqWl92b1vTmC-XsqMUM3fM5G465K_2bmP1B_7C3yzJEiKIR1GT_FsT8t4fbFCq78BXz9xzvLtWSd-vq1T-EziUfKitZ-45PsvOYChIATs-Jd9f9jSc700oVQykHttp0WVN17k264UfGUe-_TEvvZJnX-M6rvKTJPk2qKO7l9G0KvpmafDu2Cb5micBWHi8pUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=WwuhitB0wqU_hzdItHyGgG6aucDBRA7p9Wgo7EOm92m6Y_p3ykK72h0otrEErpv05ktQaCIktNFfg2hCjOY3Fnw3IA-NJ3audsA0M1kIqqOPnIawkW2hIQKrfxtxpUURMKzCtU9o8sTOvgNYND3SjyqWl92b1vTmC-XsqMUM3fM5G465K_2bmP1B_7C3yzJEiKIR1GT_FsT8t4fbFCq78BXz9xzvLtWSd-vq1T-EziUfKitZ-45PsvOYChIATs-Jd9f9jSc700oVQykHttp0WVN17k264UfGUe-_TEvvZJnX-M6rvKTJPk2qKO7l9G0KvpmafDu2Cb5micBWHi8pUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71826">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=fCEhzQR_ZKTotyfdl2c3bnihNPbOUhR7J37va7oJcM7qP53naQ_FT4uqa-okfrIk87VAi6HhuXAz_aEhEgq7GitiMCuz7J0R7UzWCihj4hgIy6S3s0tIiKTLCVUYxgte9ZgPcoX6ji6T1PUVnThPnYO6aau7RDKVAd-if3peRAVKytmDbYMqdKOxLdK3YN4PqzAn2BbdGEeIWuYu5Yj-8UbgVrAyeNphdSDZ6yC79EgcmITnvolWvM80eRDn5l11Os3v_Icl-isvuqqXw-0RR5b_wQeY0BiA0HhNHMkhmRIdbddjeD9jWqDFi41m9ug8x-62k3xn-tk2PsL0nX3GUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=fCEhzQR_ZKTotyfdl2c3bnihNPbOUhR7J37va7oJcM7qP53naQ_FT4uqa-okfrIk87VAi6HhuXAz_aEhEgq7GitiMCuz7J0R7UzWCihj4hgIy6S3s0tIiKTLCVUYxgte9ZgPcoX6ji6T1PUVnThPnYO6aau7RDKVAd-if3peRAVKytmDbYMqdKOxLdK3YN4PqzAn2BbdGEeIWuYu5Yj-8UbgVrAyeNphdSDZ6yC79EgcmITnvolWvM80eRDn5l11Os3v_Icl-isvuqqXw-0RR5b_wQeY0BiA0HhNHMkhmRIdbddjeD9jWqDFi41m9ug8x-62k3xn-tk2PsL0nX3GUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند‌روز قبل حدود هزاران تریان که عمدتا سگ، گرگ، گربه، شغال و روباه بودن روبه روی پارلمان آلمان در شهر برلین تجمع کردن و خواستار به رسمیت شناختن حقوق جامعه تریان ها به عنوان شهروند عادی شدند
به آدم هایی که رفتارشون مثل گرگ، گربه، سگ و ... هست تریان می‌گن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71826" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=pIp3Xhug4_psRQGWj7FkVxfEVXUbiFpeCXjkFUcS9e4gZ0hHroYAEfAR8vJjLBHGyLrK1soEAwveNOZLYz0ItvePUyA1X-lIjtFyJGOHijJhQajQIMqEvWf5FabdufyUh5McxjNBZCoBRlxO6aCCq4MSdTjmJNYolF_X8e9kIeItQ5UvwAgxW_LUHYEcx5H8CeTCTqL1Z8kTkeYXTCE-zf7eXxYYLnxfGKTQUCnJmk667fOHq3r333CynMlCoHDUH-OkqzxsRN9-_fN1sgHOiV2CZPu6jrEBy7DbwydKEfzQhmlqbbnEdz1SXrMZuh974lOpAQNn6xRRtiJOmHCDYz1yKJF_HlLBJlg62OiTZUGO3uiJhqfVOftsmBoNhgwnkprm0TjrF7hEo0lnW6tUxl7gCLfYc_huW4k6VbFHpcVngY2ApI3LHriUzAhEkUoYCAOrVknAG1fzt3gAe3DzkHd7LLbUpVdr9Uq8nk_hqbVRZW1ptANgyUm4xTmtOo1bLlOegb1b3NAvh2mWVmTnWH3TXF1xiR0osYeP3LJa3Ck0uBf3mWT_ayFJw71a9HCSh-oOeHdNAqsrdJc9Njiq8FThtOBQ1JxXE2lXG3lJ8QE0UARL_fPjA6P2Zk3VFMqkXecJ14KfJSne1aAWtl0edt9Ve6zF8eA4o4_ldYOFgiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=pIp3Xhug4_psRQGWj7FkVxfEVXUbiFpeCXjkFUcS9e4gZ0hHroYAEfAR8vJjLBHGyLrK1soEAwveNOZLYz0ItvePUyA1X-lIjtFyJGOHijJhQajQIMqEvWf5FabdufyUh5McxjNBZCoBRlxO6aCCq4MSdTjmJNYolF_X8e9kIeItQ5UvwAgxW_LUHYEcx5H8CeTCTqL1Z8kTkeYXTCE-zf7eXxYYLnxfGKTQUCnJmk667fOHq3r333CynMlCoHDUH-OkqzxsRN9-_fN1sgHOiV2CZPu6jrEBy7DbwydKEfzQhmlqbbnEdz1SXrMZuh974lOpAQNn6xRRtiJOmHCDYz1yKJF_HlLBJlg62OiTZUGO3uiJhqfVOftsmBoNhgwnkprm0TjrF7hEo0lnW6tUxl7gCLfYc_huW4k6VbFHpcVngY2ApI3LHriUzAhEkUoYCAOrVknAG1fzt3gAe3DzkHd7LLbUpVdr9Uq8nk_hqbVRZW1ptANgyUm4xTmtOo1bLlOegb1b3NAvh2mWVmTnWH3TXF1xiR0osYeP3LJa3Ck0uBf3mWT_ayFJw71a9HCSh-oOeHdNAqsrdJc9Njiq8FThtOBQ1JxXE2lXG3lJ8QE0UARL_fPjA6P2Zk3VFMqkXecJ14KfJSne1aAWtl0edt9Ve6zF8eA4o4_ldYOFgiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=oQW0Bo_Hq6kkrNXusnAr9a9fCnRxgUzdIhRivZu5RlJHz2MkZVZSIS49IIu4CVcaePs_3r7qJUHSAAIBrYdy0PN9aodI0OmQMnuDkgLQABoMK9CUqsqq760z_oS5xPgum5Ipjy7IfahwOif_h8L6CQ0EjuZi96apMFR6QKg_Jlbhm_U5nqQOL5NcjclJPVe9oc_GfZ0AAbJh467mRz4B2929MZqyI7iYdMPfc9BeSD_KhtJU0ap3sa4bem7L44V9C2HmPFFx8Mfug0h-4_9IDfYou3mUJF1YbjAYWS3QDMbUZPiSKXzMmrI8yi5JvwQatXgXLtJ2vytzuXtSMS71hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=oQW0Bo_Hq6kkrNXusnAr9a9fCnRxgUzdIhRivZu5RlJHz2MkZVZSIS49IIu4CVcaePs_3r7qJUHSAAIBrYdy0PN9aodI0OmQMnuDkgLQABoMK9CUqsqq760z_oS5xPgum5Ipjy7IfahwOif_h8L6CQ0EjuZi96apMFR6QKg_Jlbhm_U5nqQOL5NcjclJPVe9oc_GfZ0AAbJh467mRz4B2929MZqyI7iYdMPfc9BeSD_KhtJU0ap3sa4bem7L44V9C2HmPFFx8Mfug0h-4_9IDfYou3mUJF1YbjAYWS3QDMbUZPiSKXzMmrI8yi5JvwQatXgXLtJ2vytzuXtSMS71hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=r1Xk767KNtUBV8DmStK9rfeAJcjx_oofa1_BbrvDLe850JtvDgX3eUQkooWnjxd7EjeEWvPK7yTS5T9FoufoQz2dbR_HQJ6Jfw7BqyMCnqzw5a6ZJNmPNIXewNXeBiTUVuyh7NqBoWWnxOBTf-DBZlcj4eQhCqmhirTBOx3Fnp7kEkN8xxYP9xYysoXOvGwhEq_iepvOZyUNBqSTjkTMZgPhSOIwgB7dcV7qQhSVd52fJgY19508ozwO-jkwlQZtXKGK7etpEe5-U_TwLb5-P4juIPlCh5zx4CmxFxJG5bLWbAiK_pq1gvvi2Ea-VvLRN0lGdtEF8Z-48Xft_rQBDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=r1Xk767KNtUBV8DmStK9rfeAJcjx_oofa1_BbrvDLe850JtvDgX3eUQkooWnjxd7EjeEWvPK7yTS5T9FoufoQz2dbR_HQJ6Jfw7BqyMCnqzw5a6ZJNmPNIXewNXeBiTUVuyh7NqBoWWnxOBTf-DBZlcj4eQhCqmhirTBOx3Fnp7kEkN8xxYP9xYysoXOvGwhEq_iepvOZyUNBqSTjkTMZgPhSOIwgB7dcV7qQhSVd52fJgY19508ozwO-jkwlQZtXKGK7etpEe5-U_TwLb5-P4juIPlCh5zx4CmxFxJG5bLWbAiK_pq1gvvi2Ea-VvLRN0lGdtEF8Z-48Xft_rQBDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=kWXewof9EzHiRryjYu6kP73A4ux5sJSm5Pkq4-kC5zwXSDa4Sx6SsDV8deYdfay4is5Z4ma3mjAAa0ukKiEED9qF5BAY8VvoIZs7Jk8nOUHAYiuHX_M9z7jxgIhBSzPB3CXhZslJH8R9K72ILSzAHbt7eO_HwoMscJ6peU8BsKQ-c82QP_ceF6Qt0RtkOn7rwqS30OTbSS6zJAyoxnMl6Ba6oup0WyLO4kj74he5gvgdFwgUrtLM4bUVRsV1aoL7JMQWlG9S8B5MMuEHWqruTi0OUxX_08RCh8dx_mVcUKUTZFHDkZd3N1kV9ZN2wXwo9CCFev5LJCoPTzrKoZUYdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=kWXewof9EzHiRryjYu6kP73A4ux5sJSm5Pkq4-kC5zwXSDa4Sx6SsDV8deYdfay4is5Z4ma3mjAAa0ukKiEED9qF5BAY8VvoIZs7Jk8nOUHAYiuHX_M9z7jxgIhBSzPB3CXhZslJH8R9K72ILSzAHbt7eO_HwoMscJ6peU8BsKQ-c82QP_ceF6Qt0RtkOn7rwqS30OTbSS6zJAyoxnMl6Ba6oup0WyLO4kj74he5gvgdFwgUrtLM4bUVRsV1aoL7JMQWlG9S8B5MMuEHWqruTi0OUxX_08RCh8dx_mVcUKUTZFHDkZd3N1kV9ZN2wXwo9CCFev5LJCoPTzrKoZUYdYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=ikkMF5aboJDV7MTp8tfd8boyZ_Dbtmq60PkxJfRUVSfzBCRshMTqiAmmtKZW-3WNQPhu_EUOBbWT6GYEZJLBuPlg20SKc85fpZIj-mwv-A4JWb_1M83H_BnYEPJgY9wlA2UAVFPGokrrbbBYrBTw_76FYquhCq9c3Ss2fl2wKYOJuZZ-SpbJn1kQSDParBFnOlAOt9Tq0bQNRuFEgsBzfgMaZ21EzTyX7FTZ4chIaHswc7UcjEl_dA-Es-qOpYSlPj2kPDAc_UeoHaySWpLdHDv1xnZHgkDePe-W3RVv3k4_TIrRN-TcZ22UvldUbjHZGIRTnoxCr1U4p_UpUbxGfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=ikkMF5aboJDV7MTp8tfd8boyZ_Dbtmq60PkxJfRUVSfzBCRshMTqiAmmtKZW-3WNQPhu_EUOBbWT6GYEZJLBuPlg20SKc85fpZIj-mwv-A4JWb_1M83H_BnYEPJgY9wlA2UAVFPGokrrbbBYrBTw_76FYquhCq9c3Ss2fl2wKYOJuZZ-SpbJn1kQSDParBFnOlAOt9Tq0bQNRuFEgsBzfgMaZ21EzTyX7FTZ4chIaHswc7UcjEl_dA-Es-qOpYSlPj2kPDAc_UeoHaySWpLdHDv1xnZHgkDePe-W3RVv3k4_TIrRN-TcZ22UvldUbjHZGIRTnoxCr1U4p_UpUbxGfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=FjAfWOHWlEbrmu3O3PRi6bkR-HfIT3ZEhxR4Jsg25GT9bb3SrHwxmVCFsOH9zhYsmeUsG7clGoPB14Vj3BLNXacZ1bCBJugeVy6WSS94jnwXwr64AmZ3-Vlmj5mvFM8Sb3F_lxhShttTmL_MnPQR1n7Bylsm-mv5eHA0cBk7RCHlJO2ixSto5ViaSt9YxciIOzox56SpNBmxq2cdoFU9cahPGnAw440fGNbkPm87LezPFB1u2OvPeXh__TjxGThdWV-bUlsz6NqfnodzIgOYnPLIE72ZteALZ-oOsHUwJvb4a12ChGQKUaKnTSbEHADPX16txO6ZN56cMU0_p2oqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=FjAfWOHWlEbrmu3O3PRi6bkR-HfIT3ZEhxR4Jsg25GT9bb3SrHwxmVCFsOH9zhYsmeUsG7clGoPB14Vj3BLNXacZ1bCBJugeVy6WSS94jnwXwr64AmZ3-Vlmj5mvFM8Sb3F_lxhShttTmL_MnPQR1n7Bylsm-mv5eHA0cBk7RCHlJO2ixSto5ViaSt9YxciIOzox56SpNBmxq2cdoFU9cahPGnAw440fGNbkPm87LezPFB1u2OvPeXh__TjxGThdWV-bUlsz6NqfnodzIgOYnPLIE72ZteALZ-oOsHUwJvb4a12ChGQKUaKnTSbEHADPX16txO6ZN56cMU0_p2oqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ZnjUTaLpRcu3De7azOTCuIjdxlQpicBTGhKtfTz5jCOHqD6hreUQ_PH_23G9YH-Lc6jJjJc9o8b8lEwun5qc-6106EzUgNhmalMAnFJ6l_3bdZfbDsuqaX1VXXmDOAgQmDpjv0LpJNUKh0U8cmkjrlAYyDtq_4zBjoPvbYKiB0pc5FbPTUBoaMVKHIUbc2iwxeuGiuxRmPtaDbSJ4ql4g95HRR8JmqjzXanYw7bdhV8-Ya13mLPwrKiI8vRXLHUhDjtBuyvAz1sJzkErcetoAGZZYRF011LvUS1Uel5TbG46HWSLs7iMwQNA1nVeMQyVES0jTM4Tiu2fufUUgYuddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=ZnjUTaLpRcu3De7azOTCuIjdxlQpicBTGhKtfTz5jCOHqD6hreUQ_PH_23G9YH-Lc6jJjJc9o8b8lEwun5qc-6106EzUgNhmalMAnFJ6l_3bdZfbDsuqaX1VXXmDOAgQmDpjv0LpJNUKh0U8cmkjrlAYyDtq_4zBjoPvbYKiB0pc5FbPTUBoaMVKHIUbc2iwxeuGiuxRmPtaDbSJ4ql4g95HRR8JmqjzXanYw7bdhV8-Ya13mLPwrKiI8vRXLHUhDjtBuyvAz1sJzkErcetoAGZZYRF011LvUS1Uel5TbG46HWSLs7iMwQNA1nVeMQyVES0jTM4Tiu2fufUUgYuddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71813">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71813" target="_blank">📅 12:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71812" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=AWoEmQgENxktpHnghrzlDMA38ya0KH2hmGhb_tLX8e-xBuDICF5I8VW4VVVqu6zBXTNe01thuLcq0Y4PH7J0C1YMgAUL76_lWwpOQUX5xqdFWCxAqdK9fldVvo22CWHg1-fcZ9d1ZLBP_bE2wiXG06PGqLS5cFsfSQaOhOhJvZPZMo38zSYWA8JD9gGZK13BGmdq0OTRceXlo97pGhMqc-LipHHXIsAOj083ZDGrFxBZsJznsOQZv3ddo8KpWy2B6yr0WhQe2PxZtJJ1NsJb1_8M2g2fBg9OqVjX1We33fKwGSPErerTAA7lEULZYUqRXRDLN4pOFcLWvlwu7Ng3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=AWoEmQgENxktpHnghrzlDMA38ya0KH2hmGhb_tLX8e-xBuDICF5I8VW4VVVqu6zBXTNe01thuLcq0Y4PH7J0C1YMgAUL76_lWwpOQUX5xqdFWCxAqdK9fldVvo22CWHg1-fcZ9d1ZLBP_bE2wiXG06PGqLS5cFsfSQaOhOhJvZPZMo38zSYWA8JD9gGZK13BGmdq0OTRceXlo97pGhMqc-LipHHXIsAOj083ZDGrFxBZsJznsOQZv3ddo8KpWy2B6yr0WhQe2PxZtJJ1NsJb1_8M2g2fBg9OqVjX1We33fKwGSPErerTAA7lEULZYUqRXRDLN4pOFcLWvlwu7Ng3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGUBu74FbcSngzepdZ9nkcqZwH6nZTROoSI0duke_Koz-nrIaOcJo1-xW535nF75FU--vzQ3tDur0q_DgBUljWs_iFq6r8u2YzmjhaKl7JA4IGKBRPdfO9RJEnpyvAtJX5qNDhxHOZlviPw-zNM-S2bfYUh9-pboTuaT3TvDcZj4H8BSjVVg1j2vqFSja9bV6-4VUV85jXPMVlWmOr_U9jModNvMJ3Z5G2uKF1Jr8Y1VKwKwdF31gWKHbKxgPcCKknncTW3SV7GjA-7AABWHb79TK7jfcKYuFAmQdxgdtTmawO4KeCfd4KXDqnxZ9kiLfhEVwnLsfATQxcmgH-njDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=EiINhxUkfxBACWeGdhuwJDZ1g0-tHb6spxHpKvGKA7AnbN_GTIPg4xhK4xLbEJexh53GFAWRqTthmwk_6UHoT5HG63-7BWNnnTZjNWlmnUAq4dirPuOXRsvku_6LtV8a2t6Q-tYFT9alFBxMiCioEEMseDLpZt7EWsUY3fs89KBkeUSE1Fnd468jAm3shOyCFePKt1saMPJasFWpKFpN28Wd-_1xRFBbXa6LhmtSwjsyXZrA4AC9CW1lZv4v98yCBjrhs8wHElhAVodHqty4i8TdjXdO0ZfRlUTA4udIJDImnlssgRA3lfR1j2GgxxhEFeSa_HoWcm3NhgkQsc13rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=EiINhxUkfxBACWeGdhuwJDZ1g0-tHb6spxHpKvGKA7AnbN_GTIPg4xhK4xLbEJexh53GFAWRqTthmwk_6UHoT5HG63-7BWNnnTZjNWlmnUAq4dirPuOXRsvku_6LtV8a2t6Q-tYFT9alFBxMiCioEEMseDLpZt7EWsUY3fs89KBkeUSE1Fnd468jAm3shOyCFePKt1saMPJasFWpKFpN28Wd-_1xRFBbXa6LhmtSwjsyXZrA4AC9CW1lZv4v98yCBjrhs8wHElhAVodHqty4i8TdjXdO0ZfRlUTA4udIJDImnlssgRA3lfR1j2GgxxhEFeSa_HoWcm3NhgkQsc13rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=iZ0d-JqXMV4m_i58mS7GP-mlkj0fZBbc00KJ4LTbsJ4WIvutZ3rbeycH9yfpJ7KNwVcds_foZN00mEX_FgAQJwFe6HFbQO-7cKIRU5NXToYXsYRV7VINjZw48pPt9_yIUCvbnSNVPv7r6_LEVsCCzW0jy-BHlYwbZXma586qXx5kUWJhS0Mdb0uzerF3LlcIO4MnvTf3MHJWAb01hB-AJCY-c1AndYb_h02M_nOtdNWdm8qv8wf6MzwRO90ecNxwUUj-tKQTzBEjRx_V5BMR1HvCk-XXk2jafMdZhP-saziJvtmvjsomQJHUApSwXHR5_ETSKl40fPYvowemGBzgKoVBoDkCO8BLiEA_CCYEEztPDQa0qLmv04NAYrgLo0aH_0riN4o_I62rkeji9gJNqSo_aBVNUvgY9B6ZMetthHfwSNwudxmG0GyzWkC36oOQAt2_40JlbMgTIgQxBl8kpDysgxhMxjR5_WuFZ5ld5IkaMzcwSC18i4gz2jnr_9UZZ1hIjkcrxaX5mQtiU9nhXlvz0TgmZEBmhOX97np8XbAfAYC27TT3UBTxBSfMhqe6KPJnZdZqP0lxaFxFW2youNS4EqmQKB04_tDAjxD9uQxRzR51nqCI2SDOmPO6smB3DDQwcGHipxwrZ_F-0yGCRzRGH2qn-q11wqTJd4vLFBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=iZ0d-JqXMV4m_i58mS7GP-mlkj0fZBbc00KJ4LTbsJ4WIvutZ3rbeycH9yfpJ7KNwVcds_foZN00mEX_FgAQJwFe6HFbQO-7cKIRU5NXToYXsYRV7VINjZw48pPt9_yIUCvbnSNVPv7r6_LEVsCCzW0jy-BHlYwbZXma586qXx5kUWJhS0Mdb0uzerF3LlcIO4MnvTf3MHJWAb01hB-AJCY-c1AndYb_h02M_nOtdNWdm8qv8wf6MzwRO90ecNxwUUj-tKQTzBEjRx_V5BMR1HvCk-XXk2jafMdZhP-saziJvtmvjsomQJHUApSwXHR5_ETSKl40fPYvowemGBzgKoVBoDkCO8BLiEA_CCYEEztPDQa0qLmv04NAYrgLo0aH_0riN4o_I62rkeji9gJNqSo_aBVNUvgY9B6ZMetthHfwSNwudxmG0GyzWkC36oOQAt2_40JlbMgTIgQxBl8kpDysgxhMxjR5_WuFZ5ld5IkaMzcwSC18i4gz2jnr_9UZZ1hIjkcrxaX5mQtiU9nhXlvz0TgmZEBmhOX97np8XbAfAYC27TT3UBTxBSfMhqe6KPJnZdZqP0lxaFxFW2youNS4EqmQKB04_tDAjxD9uQxRzR51nqCI2SDOmPO6smB3DDQwcGHipxwrZ_F-0yGCRzRGH2qn-q11wqTJd4vLFBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnqgjGbzhjD1bHZo9u0CVbB3lZl04gIJHkAe8B9hHMDIB9Geiu8VuaGjPwpt4u8W5iHt2tIhqwq1okPgbcnekNqo50XeseFiwyX_EVHQrKSYeRsSo15KMsZCDcujBFoFLd8CW8NXCrIJUnOWYxLlrCVfM7heKv6C572JHjhwCXH56tLEKT7mLBxLCOIBQcp9Wf-fhi0TQSeRex6cKytKU_eTLmlHn_26ev3MWGkWGE_loC75tcaXs4h77lQwc4FwYnuTuEeZmkFz8HOwQ76eLqgsiQkg5OV1M9-aJzh__pQz1lHnAP4anCh3SIFO2szJq2TqEs2Wvoo9RnRbnXh9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=E7-04nVSMGskmu95nFaznmgSUUqk9zlAynY2mDcZ3QCK1l6B-3sBxYbp_UcP_ojcvOT7eVoFv-9_oWfTmnZ7UKerbQ0UC6WZ9uSfSO-Ef23JQqNXiNNQzUfTrea7BuDPBBh-Po0gIzMiELp6ggl3IjfMsvI_NnHbSyRCerssNYH-UBO8uzqGb2q9TovoO-ikR2QxKSYnEFzo45CtI912oeYOwV7nU55TXXlNrP0eAvjqps7A8qPsOGQKmC7TU5c1R3KfU7vKdBlAFOgfsrO-1J4abbAuc-ReSAfrfefRTe5gE-kkxilQiTWCm3QmZTIyieiwrr52aCAzDhgLiIR7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=E7-04nVSMGskmu95nFaznmgSUUqk9zlAynY2mDcZ3QCK1l6B-3sBxYbp_UcP_ojcvOT7eVoFv-9_oWfTmnZ7UKerbQ0UC6WZ9uSfSO-Ef23JQqNXiNNQzUfTrea7BuDPBBh-Po0gIzMiELp6ggl3IjfMsvI_NnHbSyRCerssNYH-UBO8uzqGb2q9TovoO-ikR2QxKSYnEFzo45CtI912oeYOwV7nU55TXXlNrP0eAvjqps7A8qPsOGQKmC7TU5c1R3KfU7vKdBlAFOgfsrO-1J4abbAuc-ReSAfrfefRTe5gE-kkxilQiTWCm3QmZTIyieiwrr52aCAzDhgLiIR7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=HR1go8_mYJnxcm35TKQdV2VQ5hib7F3G2qZ4FYb6X7TCkHe62DJ_wuwJZVjCQtH7eaq4E6XEGUijrD2Vg44ZCtIPmmULCJ7iTLJcHaaPK7WlZwUxSDx1yGCT1V3rvYn1iR8Kkz-j1MQenf2Aq41ibN2otoY9xU-q_hkUKo2FaWa7SEphgLajQRu6MxFUhsrXGE2a-hn61XqSVGM-AV0aFVPw_FzUXke5Ryy-nhB512J0RfiOFdCa0R8btJR8xUu9P-TJp6uOJUxZo7qMXMApROkxBl3Sl8q6AWsDj53IToxPAnStOH8i7apNdCu0iLzjbHpRl0-bvf7iV976r1lH0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=HR1go8_mYJnxcm35TKQdV2VQ5hib7F3G2qZ4FYb6X7TCkHe62DJ_wuwJZVjCQtH7eaq4E6XEGUijrD2Vg44ZCtIPmmULCJ7iTLJcHaaPK7WlZwUxSDx1yGCT1V3rvYn1iR8Kkz-j1MQenf2Aq41ibN2otoY9xU-q_hkUKo2FaWa7SEphgLajQRu6MxFUhsrXGE2a-hn61XqSVGM-AV0aFVPw_FzUXke5Ryy-nhB512J0RfiOFdCa0R8btJR8xUu9P-TJp6uOJUxZo7qMXMApROkxBl3Sl8q6AWsDj53IToxPAnStOH8i7apNdCu0iLzjbHpRl0-bvf7iV976r1lH0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=aObe8Ow5iVgfpZi8eUOJTwFsxKgtCZokvoS_NS-T0vXQ2sHxETdH98BtzFeVmZFLzCivQUDEme7Z0EpwNa5H1N9ZvP0AREmv4ewIpmgqn_YQnmOWfBvpe4oSBk9yQJ2rGNUeXXFMW-yReHRXF53SR5Anu02r3M1HDGs6a-eXfOgUCVoQGJrTT8I6XCKjYO32cmR_GvTdxdzZLYnxmTnjm3PfAZHJXQscRtiZbTpWj1_VVNnWQX2i3Y6-UQ_aIATjgNtZPoDdjdZ0AXP7rdj2aO-9G8mx05kHQjVC_jQuAWlXPL4gzarARNa6CPbdtMTvjrK-3RLemMMB2WDs81VNUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=aObe8Ow5iVgfpZi8eUOJTwFsxKgtCZokvoS_NS-T0vXQ2sHxETdH98BtzFeVmZFLzCivQUDEme7Z0EpwNa5H1N9ZvP0AREmv4ewIpmgqn_YQnmOWfBvpe4oSBk9yQJ2rGNUeXXFMW-yReHRXF53SR5Anu02r3M1HDGs6a-eXfOgUCVoQGJrTT8I6XCKjYO32cmR_GvTdxdzZLYnxmTnjm3PfAZHJXQscRtiZbTpWj1_VVNnWQX2i3Y6-UQ_aIATjgNtZPoDdjdZ0AXP7rdj2aO-9G8mx05kHQjVC_jQuAWlXPL4gzarARNa6CPbdtMTvjrK-3RLemMMB2WDs81VNUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71795">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بی‌بی نتانیاهو درباره ایران:
پیش از هر چیز، باید رژیم ایران را سرنگون کنیم.
این مأموریت من و مأموریت اصلی ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71795" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71794">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ساعت ۲۲:۴۰ پنجشنبه؛ ملوان‌ها در اطراف جزیره لارَک، از چندین انفجار در نزدیک کشتی خود خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71794" target="_blank">📅 23:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTWQnuX0U-jF_YpqGXNGPFO3zbxCwKG91s8aDVQiCJaEHpz-eXo_Xmr5rJ3uWjQfHGvSILThNLBvWe0UIQwLnl7A-wXdbWRq85gum-IwPAVdJrDetvw1KP99I15TW9LDU3CYNYszy2jPlGV-X3pduHGElR2ls3OPxzSGopTAIHiAZ0MYdPmOwwKB9RWLU3JFSBbcSB8pQjkDxIAw4CRXDXlfrOEDmcXVSIPuvPD_lT971fx6lAHonV9I3UF_gfV7uyEZtB9SW4ke5A3Yop3_FYZWwG5e8NBdubV_BwjnUG9JQzK99bgk4mTjuPEYBDn5ygVHHS6d3k56cm_vfM2i7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک «حادثه امنیتی» در فاصله ۱۶ مایل دریایی شمال شرقی «خصب» عمان خبر داد که شامل حمله به یک شناور در تنگه هرمز بوده است.
هیچ‌گونه خسارتی به شناور یا جراحتی میان خدمه گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71793" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK4tPSHOVtMp2HND6dXrFCN02PFJrogGMZlIy-mBu6ZTJYUHFd7E1AbWDrfDplhaUkOKn53qhzkCZNvifaQYD3AHphQ209TNT3Z2ZkDOot9Ib53Dm2sfOqvk-65c0a8LapwYPyEsfQQRFXSMnO-l-YhthN80dUxunWZQi2FVH4Mbt0b9DZsGTF28-efZQ4CGaBIbrQ7BX6NR_FqjKMgxaR7ivDlUVi_k4eOY2PVjmAoWwu94N9wXZ_84XIyIPCsY9lx0wfYLhgxl1mVUvjSVY9ZCi_ZoElfuUYj6tjkugjpS7e7VDDPD1Gdm2LHXk-aURX81__w1aipJU0VWwSe3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا «بیت‌بانک» (BitBank) — یک شرکت فعال در حوزه دارایی‌های دیجیتال در ایران که تحت کنترل بابک زنجانی، سرمایه‌دارِ پیش‌تر تحریم‌شده، قرار دارد — را به اتهام تسهیل دور زدن تحریم‌ها و انجام فعالیت‌های مالی غیرقانونی، تحریم کرد.
این اقدامات همچنین شرکت «تجارت الکترونیک پیشتاز سیمرغ» (توسعه‌دهنده بیت‌بانک) و سه تن از همکاران بابک زنجانی — شامل حسین‌علی ذاکر حسین، محمدمهدی ذاکر حسین و سید عادل حیدری — را هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71792" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71790">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCo28JcRi0RczYTzWNLfYK9R0c0yKG7UvN6O0Bkdc2qzZOy0JSADVVmrU8xBTaPakqCRiY4pTCCWbS8GX8D8dfzEtEbv56HjH-4EEM7T33pvYVswpk58U45MURg0zLGj5K6ofdvtz-XNUW0FiaidKtkfZLWFyYTz2Wh55F-sJ4VpeRL1LstbPzT8e0cVd7YfSMQax7BMz548r-myOf0Vd279VDyJ4ksgjqnewWkdIjN92Ou_T5mGw8iMPSHam2gG93dPGCarXNlBNRSM70MulZmiChM87D--7O7oXtB_qw9cCq7DvBpSXZDUyOkVqrdgqqhpQnZmt_uLSR_XIQ6DuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAWgN8RWDEAFJklv_ZPTY0crveLER3HthAkzLw0meBHUb6KuALlaqkXuFzWulCcSNwMuLcc72WkIac6iwRdG1ffD5GiO85bgq2aJzgoG3WgS7D4ef4C5vw2tdWRjGK5zPZX73QiwKb2YxoyGqnCUE3wkjmx7JEFnOOGyK_VkV_d1EWO2C9AoDk5heO-v_aUTjtq4bUD5Pf2uwKajf3oTas8cWgFHqHfFYFnYbKtp7re5zrixTiIzu244Obrxbh4CQW3afPWM8a4uZ5uLJt-8Ybvl951bBv_jCcqlBwMsgu937q5BmLUJy05OQak37R6Iq_dDcPxM62XEBODX_aiJ2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران به سرعت در حال بازسازی تأسیسات طالقان ۲ در مجتمع نظامی پارچین است - یک سایت سابق برنامه سلاح‌های هسته‌ای در ۳۰ کیلومتری جنوب شرقی تهران.
ایران یک برزنت بزرگ روی این سایت کشیده است تا کار را از ماهواره‌ها پنهان کند، و در زیر آن ساخت و سازهای سنگینی مانند کامیون‌های کمپرسی، بولدوزرها، پمپ‌های بتنی، جرثقیل‌ها و دیوارهای تقویت انفجاری جدید قرار دارد.
این سومین چرخه بازسازی است. اسرائیل در اکتبر ۲۰۲۴ به ساختمان اصلی حمله کرد.
ایران آن را با یک مخزن مهار انفجاری جدید که در زیر یک تابوت بتنی دفن شده بود، بازسازی کرد.
اسرائیل در مارس ۲۰۲۶ دوباره با بمب‌های سنگرشکن به آن حمله کرد و سه سوراخ در محفظه ایجاد کرد و ساختار داخلی را تخریب کرد.
ایران تعمیرات را تا ژوئن ۲۰۲۶ آغاز کرد و اکنون به طور پنهانی در حال سرعت بخشیدن به آن است.
ISIS (موسسه علوم و امنیت بین‌المللی) بازسازی مکرر یک سایت آزمایش انفجاری قوی سابق برنامه سلاح‌های هسته‌ای AMAD را "عمیقا نگران‌کننده" می‌نامد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71790" target="_blank">📅 22:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71787">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvL347RA5-PnyrG4myOow0gR89jmIF1XZ1dsiujkZEqRsO9_6e20Gnk4r8dDKshBKOTI122RzGjyellqdwZzokfPJAxelkjQAmIxh-gfhPu_mRy07P36qN2Ym_5RdxTfV6aetX5DmH-7d-GJj0E572zRCp_jRXd_SOG0-Tm5IQ5cGqWZlg3_0ikGNxTn03U8sFEBSqh8Whvgv3TBFJiizEv6rDb3xgHVeioywOCISuraq-zMOJs4euNoklcZ62wDlXL_BvQgG292i4hlWoWi4_su5wC02gyIVkeI1Qv1IEjPxs93mEH4hRmrfMlI4pSCvmW02nRybLa7QX6J70hJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTluYKhkuPn_1URG08vtgT-dZ3SrhNNiZlZJG9dayb6_9SM0GiYCA6DGR_hsfW0leNHfNtIg7bSRo5OVU-tiQCfLEI0B72J-MCusB441rqzR3h8f_luf50RgvIcoigkwIVotKn26do72_wiMfzpcHQrI__vh5AveWp9cvaPBluAcWWpW93hvquMMYCilEL8XQ2J0h3sPaXC87GypBeeSmpSsVrUutrPao4Po5qHzHe0Ykc6LxHKsmPwgIjLSd3Sl-faOaioY9AODc86QCPYXHOmugNwrEz3ClpE1AAOfpQKsmYbXr6Z4p9kFfdlEIa3_TAH9YRWWt2f2bci-rMELLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-6sCcnPi-oUGBcvtTAHRfl-VZxCMnhYnfVmnJNEvdtepU5ZlJ_OvlaMqPmQMpmWAFdeBXqMKUP2sCOkJaN77Te2luSCZIfljmaZkWFjbGEh6TWPTQ5Lm11oBcyvfQCoLUWICNULtDAAYNG0n8jN4_EvtGecMadLL9NJDzNwj0Yqm-S3tOKzV21stmUGpatdkWTjXe6uA2t2Lc5iwMPp_HkiQVWBnpyh8KY8p_1NehvGWYDJZJ-B3II7PWGI2GXOzhK-nizG457hsgxBdbGF-YVrFvgW0QIW1Gy2pih2J-Ys92VfcjBU5tBLzxTKM-vFgo3g43TNcgZ8Th8CoiGrgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس های وایرال شده از علی ضیا و زیدی در فلورانس ایتالیا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71787" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=hp1IQuENLrxoLCa5aiU80vp7NEdAFzG6EZ4dYH4X2XdOCvdFpAk0x6kftWsAy0bU-DTYKm_Tm7i1coZhSe5UVqf40bqceKYbatTl5oXfruAhn5oBWAbBCq-y9pFyh8TjcQ5MAMnbOIeGNTV82lCefqXLzvF8jA61CLrVCcDHjBii4R-Hwevpc0yBvl2--XJCqh3z23gdX1KY98Q891GH-65HfKh5_vH9lsBYCS6s8PDAcnWYDebRsTUitudqbab_-7ooqBDLU1LpqUXdIWFGpVqQGoM5s4m8sVMHvD_r4qCIcnIds--RCWYdmT1LTU8BsBihEx4vp-rYje_Qln7kfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=hp1IQuENLrxoLCa5aiU80vp7NEdAFzG6EZ4dYH4X2XdOCvdFpAk0x6kftWsAy0bU-DTYKm_Tm7i1coZhSe5UVqf40bqceKYbatTl5oXfruAhn5oBWAbBCq-y9pFyh8TjcQ5MAMnbOIeGNTV82lCefqXLzvF8jA61CLrVCcDHjBii4R-Hwevpc0yBvl2--XJCqh3z23gdX1KY98Q891GH-65HfKh5_vH9lsBYCS6s8PDAcnWYDebRsTUitudqbab_-7ooqBDLU1LpqUXdIWFGpVqQGoM5s4m8sVMHvD_r4qCIcnIds--RCWYdmT1LTU8BsBihEx4vp-rYje_Qln7kfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv7HOTr4PVuIIR6MzddsQdCc5V9npkLjZpjOmcEoGzUzKEXbr1UmSzjffr5zHtAjFij5ZU4xqMgsQZOwzbWoxNuLRJBlmdxMxbOjrJ7a6aJJpkELn2Wxsq2tHgV9IFIfwLX-dryOoyb2OjaumzdpClI7kDqCS-a9xc_S5xdyU8RRY8zwQMqtjzL7oKpQwm8moD-wsCvSC09PndBkMVL0hD1hFgFx8v85oBAJEDUr6QT2O2VHi-6QDNGGR67gLBK5kcC-0SUURkxMIp9k2v1LWqcYQrNR29fNcgMP0DBGhyjr_oDBVbxbYHZRHMQuRPpjLzkvYkhTok7Q1FQBld0qWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tHQ1paaIML_gdBn-OLO60u9yWEg7ykUfDOk2K4B6eM-NZriqCGH1woWzY-C7mXJ-QBH5AZc8xBxp0yCfIDInqz54Qw2c857bIC7nx54Frh9_qpODq9wniE5JqJfjJ2MeGnShzeYMLPfJ38uc-B2QmOdZgIeaKw1v6CdfVxtAhHZvn3uiPHWZkr4axOItrVlGbEu5q_IacmdZm9zISA1nGlIu1QImXR0jc1AzyyicuMDkInWJSzqgNhqMXcQOGHjFyYgzRClg0SBzMhaj-R8Wyt0EYYoODDW74zBQE0bi5ArY50f9voIKJXzOeUPjVrbTNA3JEO9KC38UzSvY-OfErQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=tHQ1paaIML_gdBn-OLO60u9yWEg7ykUfDOk2K4B6eM-NZriqCGH1woWzY-C7mXJ-QBH5AZc8xBxp0yCfIDInqz54Qw2c857bIC7nx54Frh9_qpODq9wniE5JqJfjJ2MeGnShzeYMLPfJ38uc-B2QmOdZgIeaKw1v6CdfVxtAhHZvn3uiPHWZkr4axOItrVlGbEu5q_IacmdZm9zISA1nGlIu1QImXR0jc1AzyyicuMDkInWJSzqgNhqMXcQOGHjFyYgzRClg0SBzMhaj-R8Wyt0EYYoODDW74zBQE0bi5ArY50f9voIKJXzOeUPjVrbTNA3JEO9KC38UzSvY-OfErQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOtppBLJdhfqwIh4lJEUW_xJvck1UGiW2z9PJhLQchFbYeQsMnRM7tZwuB4FMEy3_5tcfLJHvYBgLdtb_OdBFlFhxEILA2olSkpwVMX4QsLofHeNvEkk0mCjq39RTczUmLIXgad22YVSe_GxY8PRv0bdLU0Zrwsg6Bu64qVL4MkuFjbeCCmu--_e3BRdN0EFnI_JDQbpfZH9w4e-B60dTspmwi-IemtsvCVNOb1UUg0SP2ZVQ575xV_iQty8QTJ-Chk6lb3YxI-TndCAWyKxoWoNAapjpXzB-zsBQrcfsiCYhFVNsMVR0cLh7Pu3kKvV0rJWuVkqm3YnnHyGtS3PBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=F4DAZhoBzBw-JmvOKMuFCGZIJ4ecf3uNkZ_louRYsO0RwdF6i6CdxpLyZoi3lNOY1I0fVGYQnB1el4KwGRZCnH67_v8O-M4OA1SwRF2baYUKzYKQ6-yS5tuSpbLI1XvcMapus2b9Vb0rR_8QcLUSXOBLdrJ8eSP4b3tkWKvlGVPoRuGYQ3Pwaok_Pqhd7_S9inNF1WL0bMZ7qXzEm4dSnwHk6sEb7I_V94hz2oV5gHQW8WWZa6gna2EspMyLk-9EALflmBWiwErF8Af9KBQtUJsbgak47cLRfzEMte7IdcjNRZoFQeKsy5Y3PbM34vLc_NPAJy-5NxmBpsdjI4LP4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=F4DAZhoBzBw-JmvOKMuFCGZIJ4ecf3uNkZ_louRYsO0RwdF6i6CdxpLyZoi3lNOY1I0fVGYQnB1el4KwGRZCnH67_v8O-M4OA1SwRF2baYUKzYKQ6-yS5tuSpbLI1XvcMapus2b9Vb0rR_8QcLUSXOBLdrJ8eSP4b3tkWKvlGVPoRuGYQ3Pwaok_Pqhd7_S9inNF1WL0bMZ7qXzEm4dSnwHk6sEb7I_V94hz2oV5gHQW8WWZa6gna2EspMyLk-9EALflmBWiwErF8Af9KBQtUJsbgak47cLRfzEMte7IdcjNRZoFQeKsy5Y3PbM34vLc_NPAJy-5NxmBpsdjI4LP4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=qeSi33Trd3utbevYo52bOHGjf1fZCzViaMyno1RO9QkcWlap-Vd94WoSnKsnvVKqPJ27AAInwLyNW_Da6VI6GLH06nOWHiYVH8lK_cBmT1ZH6u069Kx6sx-Vu86O3H_h7XW7_WudtLykouSdJpYdb0BUjCmLPGPorX0qrsun81OtOFbEWpScFGjiSuOx_xxHJrCg5d4ktlXI0ZiIAE1cbFCfeA44M11DzgT_UvACxjytQuDCS5872TBQq209lF7mKODVybyFPysTHEvJwG4qCR9_GSgdTSMZkBuEgaH73xnA5ryjadaEr9PDxWa02XwayfA5CsGW3iH6vTHd2-Mqqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=qeSi33Trd3utbevYo52bOHGjf1fZCzViaMyno1RO9QkcWlap-Vd94WoSnKsnvVKqPJ27AAInwLyNW_Da6VI6GLH06nOWHiYVH8lK_cBmT1ZH6u069Kx6sx-Vu86O3H_h7XW7_WudtLykouSdJpYdb0BUjCmLPGPorX0qrsun81OtOFbEWpScFGjiSuOx_xxHJrCg5d4ktlXI0ZiIAE1cbFCfeA44M11DzgT_UvACxjytQuDCS5872TBQq209lF7mKODVybyFPysTHEvJwG4qCR9_GSgdTSMZkBuEgaH73xnA5ryjadaEr9PDxWa02XwayfA5CsGW3iH6vTHd2-Mqqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=dqpnkQLW9ciRouymuOJci5lp-HIX_BWunyQJRvcJNU9bGZ2ajTXrOj99Hg_wWqqFUF0lBHaApu3oAvnq-T2deBug-0mt9sHpsV7V8tXQwESE4G9fLIv152UwL9_QWpJ4NZtw2rCdGQfJDTNtU_tZDKQg1TyxR2trF3Li04GDJ4KHZvQFIugyR2asOrhiW_jOpwkr9puVURpTr5wy4uLOzx4x6SfblMBAlW7p6nBZ3ccqqCCZzIn3ZLZObKwHaGy8fB24_dU4OnYDkpMirXp3dy0d1JdPDFNcxtXQLdZR1KOUNtQpzSsPBmz8JczgcqG91nKq_4LgSbLbTSbocCFZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=dqpnkQLW9ciRouymuOJci5lp-HIX_BWunyQJRvcJNU9bGZ2ajTXrOj99Hg_wWqqFUF0lBHaApu3oAvnq-T2deBug-0mt9sHpsV7V8tXQwESE4G9fLIv152UwL9_QWpJ4NZtw2rCdGQfJDTNtU_tZDKQg1TyxR2trF3Li04GDJ4KHZvQFIugyR2asOrhiW_jOpwkr9puVURpTr5wy4uLOzx4x6SfblMBAlW7p6nBZ3ccqqCCZzIn3ZLZObKwHaGy8fB24_dU4OnYDkpMirXp3dy0d1JdPDFNcxtXQLdZR1KOUNtQpzSsPBmz8JczgcqG91nKq_4LgSbLbTSbocCFZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7ne_POiGX6r5xp2RUo8oixbf_2yhHsHi8MZxFTGJqax97K_mu1SNYnZe29vEDpPxTu9TFaKFr9FXCjyziqN9pwIFaVfFf8GNj_LG7LBgThYQtllO6OgYKMo1umISvAFvltljy0ywUKqOvJxsgnMx45tAzYkL2_QpksEubDRGa_lvuEh90m75c_2FR7tq1kaEkDcYIEONK1nWiOQ7wgIgAV58Bq2oEANipODWM2HmuGU8BcLqHJRxc3weOXxZ9LUtSSbmuzDd6fb2VYkjQXRwoLzCYf8lgBOL9gIKZoePszg1NDq1aUnefxuKM8sUPKAefp4UcYgh8Szp3Hy3b2Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=DWax8hwiQ1g9gbhU49Hr3ZLq58IbXleKswbVC7GhKc97XMoF8QhLETNVXqvwN30AFW9d40GrZBOVSF30U02olRqLfpWIQQ5ImfaSvyON81Mh4eN8OookgcNAwNj_tIyv-CcFBpD2cleOp8RxVPeBnFdG3ojnjHuFmWmvzvE0OI-4GLclN_yz44uwLn8_F_A7alYIh6W2Sd5o8GzUN_X9HF27LI9YwmS6yQLTGrfiB0YLKSKuzUKxCbtGwmDYxb0k8dUgRsHZzPFIMMImGQA116AHXhY8pH8hGuYa1VTz4n-QJAJM4bpMqVu-uk8QTUmkEsrp6298oh1MsZMzX-o_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=DWax8hwiQ1g9gbhU49Hr3ZLq58IbXleKswbVC7GhKc97XMoF8QhLETNVXqvwN30AFW9d40GrZBOVSF30U02olRqLfpWIQQ5ImfaSvyON81Mh4eN8OookgcNAwNj_tIyv-CcFBpD2cleOp8RxVPeBnFdG3ojnjHuFmWmvzvE0OI-4GLclN_yz44uwLn8_F_A7alYIh6W2Sd5o8GzUN_X9HF27LI9YwmS6yQLTGrfiB0YLKSKuzUKxCbtGwmDYxb0k8dUgRsHZzPFIMMImGQA116AHXhY8pH8hGuYa1VTz4n-QJAJM4bpMqVu-uk8QTUmkEsrp6298oh1MsZMzX-o_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=Rc7vntFq4mUsFGOTKQVesnEY1hMWtK7qAdP731C_tVynZlkID90raPzwKkBT8mlr39gUE4T1trFkrJqDC3eSV-8Qi2IMAORmUJGcNSrsplhLNSTrXXBGCTlBXr7CN5IDaX5mZEP92oFFYrxjcUGOFRZ2Tw0XS6I42Frkg9EhF8el4eq5S1w664H4QwPNTrDzasT23DBtlMjgbIRpExtMMY3MYjELVK-8NRGknFaNUOr2qT4QIE7dixRpwK3o654C7nO6I7BEpsu1-b4DEWVWUgWBb9Db7e8rPXYKKAycjgrmkzJGvLX1L4BrBfJWJcjjB4z-BA44i9qblGGxKWvxcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=Rc7vntFq4mUsFGOTKQVesnEY1hMWtK7qAdP731C_tVynZlkID90raPzwKkBT8mlr39gUE4T1trFkrJqDC3eSV-8Qi2IMAORmUJGcNSrsplhLNSTrXXBGCTlBXr7CN5IDaX5mZEP92oFFYrxjcUGOFRZ2Tw0XS6I42Frkg9EhF8el4eq5S1w664H4QwPNTrDzasT23DBtlMjgbIRpExtMMY3MYjELVK-8NRGknFaNUOr2qT4QIE7dixRpwK3o654C7nO6I7BEpsu1-b4DEWVWUgWBb9Db7e8rPXYKKAycjgrmkzJGvLX1L4BrBfJWJcjjB4z-BA44i9qblGGxKWvxcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=kSg9QjA33ySWHszOVPG1ToiMPw0SifxJ0uBcg9Q8xgBvGdHotVSegV-FuelHbloGQ5SikTagTGhmUiz421KlBsCwKVg2kwjICc6bIbnIA15dxjglTa9TC2orQjVkv2J2LvtN0b53sm_mRxMEePjV4a1ceOgOodKYfIRSQ98YYh168tuzz4Kliyt5rz4Ob__z_ErP_6zL7KFfgeh9Tq1oBFImTk191z_x86b7WYW2PMTUZrDCqI6cvvGC8BgTkSu089RSUC3cXO90Kxk6xPXRmsZaMS3h1Y3fBk1_BaDlc27TVs2ptkG1ceXuk6T2IdbufCCXGznyi4WVvKYK736CjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=kSg9QjA33ySWHszOVPG1ToiMPw0SifxJ0uBcg9Q8xgBvGdHotVSegV-FuelHbloGQ5SikTagTGhmUiz421KlBsCwKVg2kwjICc6bIbnIA15dxjglTa9TC2orQjVkv2J2LvtN0b53sm_mRxMEePjV4a1ceOgOodKYfIRSQ98YYh168tuzz4Kliyt5rz4Ob__z_ErP_6zL7KFfgeh9Tq1oBFImTk191z_x86b7WYW2PMTUZrDCqI6cvvGC8BgTkSu089RSUC3cXO90Kxk6xPXRmsZaMS3h1Y3fBk1_BaDlc27TVs2ptkG1ceXuk6T2IdbufCCXGznyi4WVvKYK736CjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=iNzBNmAfNiQQADrrNEBODxQchIUPIJxtpJqJkPrn-_C83-eaMACIKwdCVNJcvs-9j6DqNoAJrjEGePCAT0zMlAyPG5K3DXMAQq4ZaQ_X0IXKVIVABlOS4YwxRHpweM-rZp6q0gMTfENBCEWwCjsM3x_Kh_FVA41F5c04zUo8lyj1N61oag-fx6zJ6tRzqc17HriPq0qdnVt6YzXh3L5tcCGSkcaYK7z2BVmgmVLbiv9KvCxxhgxoEByrUxiowgIqJNViv1-XETPQ1SwlfEQczZT0de8OePh2Ae1eY9U_tByyPnqPqYDozg8BjUApUQO7hkZvYPrpXGcC1-wlM9pYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=iNzBNmAfNiQQADrrNEBODxQchIUPIJxtpJqJkPrn-_C83-eaMACIKwdCVNJcvs-9j6DqNoAJrjEGePCAT0zMlAyPG5K3DXMAQq4ZaQ_X0IXKVIVABlOS4YwxRHpweM-rZp6q0gMTfENBCEWwCjsM3x_Kh_FVA41F5c04zUo8lyj1N61oag-fx6zJ6tRzqc17HriPq0qdnVt6YzXh3L5tcCGSkcaYK7z2BVmgmVLbiv9KvCxxhgxoEByrUxiowgIqJNViv1-XETPQ1SwlfEQczZT0de8OePh2Ae1eY9U_tByyPnqPqYDozg8BjUApUQO7hkZvYPrpXGcC1-wlM9pYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=M4mpxYmrEttGpVO2DMehA9ccfvDTmJgKlFIMngi95c5dN2BLSVazZGvZo-iEOnvRDdAB5TcA3g1DWo8vwRCEQT7I_QrRe3FfFQz_bW1Z97hgqSTXh4cXuivFLjpjY8GOC_EvcD5MGlyLYPdgW8sj8x81JG3zUNeBOIBMlqh-EXGO5QftdkJInHg0dj2F8hig8U0a6ppXKlv4Gk0NK8wdfa30ztyBJvEgGjDYW9vG4Qjx8Xd-8wEZMQkTlbYcPstPcCC7kIj0XnyPyQELNDMmnYBQlDmD7cFrwK9uGIkMe0Z7WW3nurTN9ZW288Y_2UlECZkxlBonwC2bbNoJ6Dtubg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=M4mpxYmrEttGpVO2DMehA9ccfvDTmJgKlFIMngi95c5dN2BLSVazZGvZo-iEOnvRDdAB5TcA3g1DWo8vwRCEQT7I_QrRe3FfFQz_bW1Z97hgqSTXh4cXuivFLjpjY8GOC_EvcD5MGlyLYPdgW8sj8x81JG3zUNeBOIBMlqh-EXGO5QftdkJInHg0dj2F8hig8U0a6ppXKlv4Gk0NK8wdfa30ztyBJvEgGjDYW9vG4Qjx8Xd-8wEZMQkTlbYcPstPcCC7kIj0XnyPyQELNDMmnYBQlDmD7cFrwK9uGIkMe0Z7WW3nurTN9ZW288Y_2UlECZkxlBonwC2bbNoJ6Dtubg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=iKw0qyIZR-UoTuB5zgoGRQ38OJ-Cn7JpoCAJjc6tAGvEvLtLjCcj9IiO9lH9Zfw0dK0Kpj6HVzoaUPmJg7ARrLcfV4Ll1n0sljJbWFvVTGEyZkcyHBzkBc_I26wbCPLqBNIjJBTcRSqF5Kw6rA3aUkirObSYTugBERvEJ4vEYD5U0xtaZ2_-QOaxp9BIjEksTfeeUL6p1SBUk30Vo2-QrAnateZm3gqXlwP5oqm2K7HvjUotBOrllzfwcF26lO7buvlkIOLvofhl0iL0lwTgylK9KEFG-MK-Lx4c12j_LEu3kOiLaf2ZCRjwEsdhlCVAALZxiGxcWmX0RBYJOQ_UJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=iKw0qyIZR-UoTuB5zgoGRQ38OJ-Cn7JpoCAJjc6tAGvEvLtLjCcj9IiO9lH9Zfw0dK0Kpj6HVzoaUPmJg7ARrLcfV4Ll1n0sljJbWFvVTGEyZkcyHBzkBc_I26wbCPLqBNIjJBTcRSqF5Kw6rA3aUkirObSYTugBERvEJ4vEYD5U0xtaZ2_-QOaxp9BIjEksTfeeUL6p1SBUk30Vo2-QrAnateZm3gqXlwP5oqm2K7HvjUotBOrllzfwcF26lO7buvlkIOLvofhl0iL0lwTgylK9KEFG-MK-Lx4c12j_LEu3kOiLaf2ZCRjwEsdhlCVAALZxiGxcWmX0RBYJOQ_UJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDRttYd4_e_QaCb5opX6Vdm6R2Gt-rDVm1w27URpn2go2Ud3MXlKZO6Q8Dby3POP-nLBQd-Fw7H2RGYCVB-sp2D6cmMEXiP-C54KbQOYtfXNU4O3UxdEyeX8MQ3--YSTKRtPRNyYNyEWYvLHhRCwhveCTWlIV3Subncj-ric9A7DY_cp2pfMP71-QmWigGw4tmh7IyEOL-Tumwi3E5Xeesico-sscoLUmFFT6nDkAcQJ6OFszmyHnV-juq6Lt2tqiGltuV1T81HT67ZkP2Zkr9XbW6MkOM1zbdiB5wmfXREFWxVh1NNpl6aWusmOW5aqTQFfbeA7oV8byqbfl7rkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
