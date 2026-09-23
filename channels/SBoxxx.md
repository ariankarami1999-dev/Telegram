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
<img src="https://cdn4.telesco.pe/file/NMWIfQ4HGdm3EbmbMQF6z5ky8onf_kjAXb0Q1Fp6g8XO4aMArY4ZZHQ-6zciu7mSliE1I7f9RP7Pp1SjtT2dDRRpTM2hzADzWXNp5wIhViCqPO3HdlYxftVVRg4-VKI6wMzK0-JbtgPBcnPgDeNr7pYFfpLz6ZtP-Ihfv9wSQa0yf_7EUbo3l6uVAJBHglfWSSYGYTr0fdgpttN0W5vdUkkHe7bWFoYJkl9zkZQ1hjSK6cdKWHS5ceT3che0vSeFDWZwgtV8NH7KDbGiyFqSTMK1ya2Db7vvIbsZ0etVkhqBrxRJhRnTes0Dk5VY6sHgzSip5Ri-4kjm7ae0GrrZQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 01:53:59</div>
<hr>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 775 · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEi7lzw36nMItqtGIpk9HbfthlpT8MnG4kk8qSolnlSQL3_j2BiRNtgTCbWO4JH6Ii6ak1boMZMXACawGenC_SvvXERazeCAdICRi3M5VoobNS6trYEK2g-ZKP6oHUK9uQfl1WNqw9kX3SUGucBabZBxFql-z-A6QmR6_nPCxHcxKue2_DF1rUkPwPbJO8I9O6Ymn5c-rnos9XeCJedPGFlCnkHUwnhPSZR321fSnvbuMzNoKbwoFHgARXx0MnUjgi72kFeu-Ko7aOjwARG4yPQSbUgyIe6sD9S8z1E5WH8iEBg6O_anzCvAOkgJYiu70wUonQQrrbyni8Zwzjg7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbAVDZ93w51VwaPxnGjnDzFAG3P1TJWbegZv-mWiNPhA-oa39SlHttJ61mT34JCVky6Dxv5nAYCG0E9YuRwRThYsbstAQ6rsJUr_ub1APMB7ASnJcOipSeaxaBRDScMd4ndttH5RkxFxHQYNFR_uXUELZ1th0bjnAP9twV6HN4xi80luudXafMLxdaTZbAR4vSwq9JA7Mi0Tt49GCTdtvdAordjvXLzuUfzZLJhvR-uIyHjqKws7l7I4fN4eI5qjLh9IUp7auHkyk6Sd_KfbowCOdbULNHcqjyWyr2wUNvMVKsC0ck-SvLAU-eLZj6wCu4YBGZ3AFRroYFIYciYWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/21153" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ نخواهد توانست علیه آن اقدامی انجام دهد.»</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21152" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پزشکیان:   بمب اتمی در اسرائیل است، اما بازرسان در ایران حضور دارند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/21151" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21150" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/21149" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پزشکیان:
با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/21148" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/21147" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز:
دولت امارات فعالیت شعب بانک ملی ایران در این کشور را از امروز ممنوع کرده است و بانک ملی ایران دیگر اجازه هیچ گونه فعالیتی در امارات را نخواهد داشت.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/21146" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگ ایران.pdf</div>
  <div class="tg-doc-extra">300 KB</div>
</div>
<a href="https://t.me/SBoxxx/21145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشتی از Foreign Policy درباره علل ناکامی آمریکا در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/21145" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/21144" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21143">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">با این منطق، فاطماگل قوی ترین زن تورکیه است</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/21143" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/21142" target="_blank">📅 16:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21141" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrB4PwJJanIp-KzQ_hgDdM2MYFGFwue-aTnt-yuYHiXXvU7cuTSbDTsjUV-YOGaMiqqZt5OwZx3u2Tneew4h4UvpHVUL_YwT2l96atbrKWx8zQqef2KyjC0Q1ha4FuvMsg-jcsMqdLPATlgJQcyKATSBaAVwgmkg3r6pLD9LKqveyW7cD21Cs8NgE9d-L-qywKVvEVxp39CzFI8xTmP_F45SYotRL0NX3Z-GBq1cToR4VBTX2e54YDXQ94SpqfBsMs9cY07YtQGedg_uF8WwND9yxRaNVQwpsNZuo-g_mTfc8z4ZI5BjMwXBUzH2hOR_mcqo5602oHpa9ZRs04vb8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باربی های وطنی به مقر سازمان ملل متحد وارد شدند!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/21140" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/21139" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/21138" target="_blank">📅 15:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21137">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/21137" target="_blank">📅 15:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21136">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چکیده تصویری پادکست</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/21136" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21135">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری  خروج عربستان از mBridge در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.  بااین‌حال، این تصمیم به معنای توقف دلارزدایی…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21135" target="_blank">📅 13:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21134">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smvvLtdwv6-XvTIdAZ0PrtbBGTD7UWH4ubHYL7FfTnnRxyUaLOPklIMlQaZO1d9L_MY0tiDnEAn8rA2KkztM3s-W2IVr7YgJldzkQh4QNvpmkcE342ROv6BS7Fpht4GKEUBIzAyZYy646n2Hlll-qXY5gY0SijAN-feTseNEkU8XmVX0tsmNTfk7o-E8iEBNhOHWwppjlB3mJ0eBokdXw5zRZXDam3kD4UqHYSIKtTgUkxQNsGel3XBhmqlB-fYFQRmGnXklxRnA4AUUFOu6Wb0XKkRrgryffbYpPwu-xQbR8D2P0j6UQhehCzZ7H1oI0ISelZx2qTdyAC5g8wkzUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری
خروج عربستان از
mBridge
در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.
بااین‌حال، این تصمیم به معنای توقف دلارزدایی نیست؛ چین و سایر کشورها همچنان در حال توسعه زیرساخت‌های پرداخت جایگزین هستند و
mBridge
نیز ادامه دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/21134" target="_blank">📅 13:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qANtQB5rloMysNHbagNG00NZxOGOBAKUIyBTVYXYzVDl0FhPC2C_JQi8-VTPDbwqbNgLzSaagHzvD9MSv3rN1yq1zs6Ou_4EDJHqXNfmGj-kIOAaFeSJnjR_LtiBvEif7opjuAVvhWeSTm78XU_UltiS1ks9GgxexUXN3FxflptCxhSYOY3O_fMlB_RYLj0b0EIfnkquCPVf4yl7dCzNPaiDIWpYGnN3AvTfMABz4s430XDHW_3E414HvBT9nVLPeEDnXWzcMen9rZSxGz3Hd7EM1b_e0rjyjgQTazJJ5H6rO2YQEWYPiG_xcia8eYjFf9rCRW527jWxPN3n1fWhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.
محدوده  مناسب خرید:
4302</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21133" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrlI7HeT7djki5xb4UgStm02q_hHYsanIcI_tud95X9ztqi0oSFstiA6Gt2EJIKucUUaH9Up3-ySPL_s4B06meeBv4AKqn8O8TXVWEMOhPY59MoQMsk7qfMWoy55GMwD65jNtcO4bIoFURUlcktX8JDbfL2DcIkm-5J1GfXHvP9u1MyOIsuiW6OLNNGDHkqe7QlXe2fXm3a0zZ73bQegpYhYjlXgU_pFFYgPoaMrrTIbeD6OfgpLuwqYTJ30g_NJ_PZFtIziqFiXwzRkktuOqM4qHGAojIhZHixM0KuRWUFuTbwzj-Gg4QpylzBhWKaogmH4JgFVkE3L05ByMI5kwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی است.
اما طلا از صبح ریزش سنگین داشته و لذا دیگر وقت فروش نیست.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/21132" target="_blank">📅 12:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=OG4mPhfOq3wD7n4WwKnEkNh0psGE_3z_LUlDflIH2pehm5iTe2MTDrPTV_SYu_1LUnMTEKRGJvQxqM0SLBuWfGybFteRo_lgwIKe0kTkXXR284CoCycC623lsxxj4-1z8d5_x8eZEI37ZE0XaeWcszbYmw6BOn9j07NnUOhG4fYAX5W1MfgLmRM_khY-8_Ofi6IoZZenPt4jMkip97PRh2arI4-wUFau2AUrFKsNcZkPu-ZaCNm8cY5BbiiWjERPhuxVgXihbw1uabS4QZ5ClkEbYxcFqPDLydW9kO0PJZ9sm81mYuc5wPzrUi2h1FrXOLgpuei85jq7uSKs3ZnKDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=OG4mPhfOq3wD7n4WwKnEkNh0psGE_3z_LUlDflIH2pehm5iTe2MTDrPTV_SYu_1LUnMTEKRGJvQxqM0SLBuWfGybFteRo_lgwIKe0kTkXXR284CoCycC623lsxxj4-1z8d5_x8eZEI37ZE0XaeWcszbYmw6BOn9j07NnUOhG4fYAX5W1MfgLmRM_khY-8_Ofi6IoZZenPt4jMkip97PRh2arI4-wUFau2AUrFKsNcZkPu-ZaCNm8cY5BbiiWjERPhuxVgXihbw1uabS4QZ5ClkEbYxcFqPDLydW9kO0PJZ9sm81mYuc5wPzrUi2h1FrXOLgpuei85jq7uSKs3ZnKDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21131" target="_blank">📅 12:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زلنسکی
:
ما باید قوی باشیم و باید به پوتین نشان دهیم که او تنها در این سیاره نیست، حتی اگر این رؤیای اوست. و به همین دلیل او باید به مردم احترام بگذارد.
متأسفانه روس‌ها فقط زمانی به مردم احترام می‌گذارند که نشان دهید قوی هستید. آن‌ها به ضعف احترام نمی‌گذارند.
طبیعی است که گاهی اوقات مردم بخواهند ضعیف باشند، زندگی خود را بگذرانند، وقت خود را با عزیزانشان بگذرانند و به فرزندانشان عشق بورزند.
اما نه، باید با روس‌ها نشان دهید، باید نشان دهید که قدرتمند هستید.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/21130" target="_blank">📅 11:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آن دو دیگر (کوبا و میانسوسمار) هم که میبینید ستاره شوم کمونیسم بر بیرق چرکین خود دارند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/21129" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">موسسه مطالعات جنگ:
به نظر می‌رسد حوثی‌ها با تهدید شرکای بین‌المللی عربستان سعودی می‌خواهند این کشور را منزوی کرده و مانع تشکیل ائتلاف علیه فعالیت‌های آن‌ها در دریای سرخ شوند.
حوثی‌ها در حمله به پایگاه هوایی شاه‌فهد در طائف عربستان در ۱۷ سپتامبر، یک جنگنده اروپایی «یوروفایتر تایفون» ایتالیایی را آسیب زدند. ایتالیا این جنگنده‌ها را برای پشتیبانی از عملیات‌های دفاعی در برابر حملات ایران به عربستان مستقر کرده بود. مشخص نیست که حوثی‌ها عمداً این هواپیما را هدف گرفته باشند یا خیر، اما حوثی‌ها پرسیدند که چرا آن هواپیما آنجا بوده است.
حوثی‌ها احتمالاً این مأموریت پدافند هوایی را تهدیدی بالقوه برای کارزار تهاجمی خود علیه عربستان می‌دانند؛ کارزاری که عمدتاً از حملات به تأسیسات نفتی عربستان تشکیل شده و در میانه پشتیبانی دفاعی کشورهای مختلف از عربستان ادامه دارد.
حمله حوثی‌ها که به هواپیماهای اروپایی آسیب زد — هواپیماهایی که برای پشتیبانی از تلاش‌های دفاعی عربستان در برابر حملات ایران به این کشور مستشر شده بودند — در واقع اهداف ایران برای شکستن ائتلاف مدافع کشورهای خلیج فارس در برابر ایران را نیز پیش می‌برد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21128" target="_blank">📅 09:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM3fz9ApuwFIRIr0VeUMschVy-EdRtQ2OvnsxEeCMBj0fFm5OhK2lFCZ-53PE5ljTclTjoz1TQ7ysS0pQFAQAa3Ahc6ZR2k6Bks3M-dyX4Vxx57uUdIr5sVf233U9iCx5XUpdhjkMroVZ3TiPChY777BHR7ExUoOkBz3Y0JS74fGWD0pM7MLS1ySuibBrDawwu5kYlyLqDjWebjapTNY71pk_FjcZ9QnwgFgEdmQ6LEx5suObZB_qfBV8QyoW2d1yti0orSm2umw6L-PtSxJnpAWm2KMYvv6G4apYYYwEfPi268IgrrAX-ikrA2--9B-4K8bXxou2rCtGKrD_bZzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21127" target="_blank">📅 08:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نخست وزیر یونان، کیریاکوس میتسوتاکیس:
ما در ۳۰ سال گذشته هزینه‌های زیادی برای دفاع صرف کرده‌ایم، اما در زمینه صنعت دفاعی داخلی، دستاورد چندانی نداریم.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21126" target="_blank">📅 08:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان خواهیم داد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21125" target="_blank">📅 08:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، انتظار می‌رود این هفته سفری کوتاه به ایالات متحده داشته باشد تا در مجمع عمومی سازمان ملل متحد سخنرانی کند، در حالی که نگرانی‌هایی در خصوص اعتراضات احتمالی وجود دارد.
نتانیاهو قرار است به جای فرودگاه بین‌المللی جی‌اف‌کی، در یک فرودگاه نظامی در نیوجرسی یا فرودگاه بین‌المللی لیبرتی نیوارک فرود آید، که این تصمیم تا حدی به دلیل نگرانی از پیچیدگی‌های مرتبط با ممدانی، شهردار نیویورک، اتخاذ شده است.
هیچ ملاقاتی با رئیس‌جمهور ترامپ برنامه‌ریزی نشده است، هرچند گفتگوها با مارکو روبیو، وزیر امور خارجه، و سایر رهبران خارجی همچنان در حال بررسی است.
بر اساس اظهارات مقامات نزدیک به نتانیاهو، سخنرانی او قرار است بر ایران متمرکز باشد و ممکن است «غافلگیری‌هایی» در بر داشته باشد.
مقامات اسرائیلی همچنین برای احتمال اختلال در سخنرانی او در سازمان ملل، از جمله آزار و اذیت یا خروج هماهنگ هیئت‌های چندین کشور، آماده‌سازی‌هایی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21124" target="_blank">📅 01:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21123" target="_blank">📅 01:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21122" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گویا جلسه برگزار شده و به نتیجه نرسیده!  First Time?!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21121" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9yKlFy_uhnSMoxBTgqfHitIK04HFWiJkfzsjzurY1rtCplreHO8xQFKelSOTr7jknKDo0NSa8096VyEfT49-7ZUTZKeAIthVeb2DMzUvyA11KspdccgMzfPIXGXvv9oEH0Aw6pB4xCU84qZCVT3r5AGNHTNSsjqxJHIjvWIHL--7gQ64bF7wfchSecS02M74o0sWZ6KHSMYy87rEPtp9X-kiJBLMiXgFe_HP6BcpVG9Wwlye1RanMU2th4AlTm-BTqqFs_VBGUbJYJ1pK5oSgYrnFZjK3fZ5lr60pI_CgVX5_WtIHIga_edwnKNCVtu1w3bpAImmWH3XSC1jNY00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/21120" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAgvSqFwpk-9jEU7ZoLmF4I7PNHaf5GLm88DYNFcTKR8q-oICa4co0RTqKJLYapfYjk02LbvDyq7ea4eqJEYUe2vLDXUqR1NI8kKmktaILiMrnboXJ29QN-aUH7ottUlobaz6NHLquIwMbOCas-5-sKKAr4dKlFPMTGoA-Xy3OODyXKYqTj3Xh2Njy14fhVXrHgfLLaOotaVSpRxCqQLRIld9TWP7CQ3E8UVSdQTpQlD5VsXrOWfMraUUpd4G9SrFgpMhxlJXpmwkGiGFgxRXCczZEnITb0p9Ll6lhu5LhKvsODSyScsD-YyDMOhvim1t4Ib16tt0PSGUkzHztnJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/21119" target="_blank">📅 00:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTrhmCXXtXKvDdgfr-AifEnQqnMthin-n9dJoLCi-9wOruTG_nTi_70aZootiSekuk0J-I5JAY_CWaU79b99elelTF-zXa-ev37PVdwHP7VcYI9l-W1RW3cdoLaTm0o6XzVGL_wJALL30yvvliFXRXTu18LgAXpKKtCLL8yFSLF4P4npXiKl8RogqZbQYo0PB7SO61GzuQpdg6r2Du95NqgAU5CTHtfwf2eS-xoZfq13fypd2-_2Q5Unhcm57p5WK263oL9_Xla6xCKvvOEjHPHZie4pUlO90xSI0zpeaxVWXOEJy37w885iFRvFxQ4ULGoODNcEa0BckI3MaktvfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUN_CFD — D #SUNRUN  از محدوده ورود دوباره حتی اندکی نیز پایینتر نیامد.  البته هر چه پایین تر بیاید خوب است، این سهم یک رشد دستکم 3 برابری دارد.  همراهان Secret Box در خارج کشور این سهم را دریابند و هم میهنان اسیر در درون مرزها نیز میتوانند روی بروکر WM Markets…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21118" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odWKxnj7tBMDHGJY3k1-QEU_VzYk1eJtKTMPtWoX2S3NfEfTBfPFHDPSk2G-PyGKqPGlmUnxqXkjeh7oCCcUSMSYgRl7FeQ6fdCENW10JKyZ7uMcA_Gtg7P8PZi367utoMQS-klk2ZuJrkvkYQN5J2IQIVzAG1mi-UUGO511VtraIWY3BkRjzsM1WJSV1OK1vp6fV2G2gj8RMAB9rEMxXEBMvTqTi98b0-98DpeENFhDF8uCAXrg2IorpJe3FdrAi8AbAnDWQsJjNzhP_1RW8794VQFhpYfVXPaJDMFED9DtfAVbJQsP2__jMqCOqHiw6cGgjrOwpJDiQx_6WxHFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL   دوستانی که درباره نفت دایرکت دادند؛  پوزیشن های خرید ما به هر دو TP پیشنهادی رسیده اند و فعلاً خرید نداریم روی نفت.   تحلیل جدیدی از نفت ارائه می شود.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21117" target="_blank">📅 00:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGBCMgnsLMPNXDQnPR6ImNF_iJ9zjXUeBcjS54DmznYKZ3U0WTeOwdRBuXZfpvLwnZpUn521jMuLsHQFvn5o6eN4qyy2hg5Bblts3Ae4GGJ2v39XruUDkMp7WNh16ZY_1SIHiNs713B5rK0qZOlH0ZdlrxaJoCwWuoOj-I7WAasBuTbkwkHXwtleYATyaRZNpB40JrRyS-wz_f68gUaVoDEn1o_PqirUUXZ2GejStm0SgxG7IPGJKC4nlFGYysslVEp4kkdPTOMkU_waAaTQ6jOScswtKY2YJdzWIH_O_neFvs8liZCftEc2XIyCEHaVeXxHBIj6NqIMLJ9hlebOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21116" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تایید دیدار عراقچی و ویتکاف
صداوسیما:
با اصرار نماینده آمریکا دیدار آقای عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
رفع فوری محاصره دریایی، پرداخت فوری همه اموال مسدود شده ایران و پایان جنگ در همه جبهه های مقاومت از جمله شروط ایران برای بازگشایی تنگه هرمز است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21115" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so0hYtnt35767DEG1hCsl4wyXz_wI2FC_azILSe0kCNuCc-N2foALuTd2UBTJDGhuQD-sdrI5S_zms9cGLPn69g7XKuovpwnQySk25KgA7OblezsKIpuxRdYFgIIjpVCuBpKznR0-YWHxHbfHOJD_D-GmWJG-aoEiv9iLcXfKt5IqPyuV4H-5b5cfDLK-X-amb2Jw_DcMihJsnXjqeHvpcWH_7hc4bPRA5Y5OGQvf_Da0HtX6oBkuEdfgMZZRZHTMkam7u4Cow8I9a2I4udUE2QqlQXX8QWbREnJ9TqESyY3m7CH36OaxemIcq5m-uONnSONW73-CJN5gWRLptzpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بز برای پاسخ به کشورهای همسایه که در محاصره ایران نقش دارند</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21114" target="_blank">📅 22:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ادعاى ترامپ:   ایران در حال مذاکره با ماست؛ روابط با ایران در حال توسعه است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21113" target="_blank">📅 22:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLUx7hi5yYilWO4l2W6ZUNJUKMA-XdZNALNmSAcSI4DvBB8wlAJN_yu8T6uOKPWlNiu3CTu7C4MV8w2bzHyvi67ceZg7UQXgNbkqaAatFuv13t52yPjwqz3dpwLW848y7g1is9c8snFJRU30vzrrHaGxpNogvuYwYbFhFAs7jNZjSkO6vfDbSa6KIjkzSsw2DhsTvQ7_yQ8w03yfBr59C20OeDvUAFo5TRXeKQ_AYEO8P7S3qR42DioXUOwYC3bim9T4SnRicF8Izm4AzQ8mKlT0d0ua_VDSZVrVvVOYG-u7lHVrP_Q3twHUer9GMY2vNLv5GHpmWKvLqkWZyjvRjD0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLUx7hi5yYilWO4l2W6ZUNJUKMA-XdZNALNmSAcSI4DvBB8wlAJN_yu8T6uOKPWlNiu3CTu7C4MV8w2bzHyvi67ceZg7UQXgNbkqaAatFuv13t52yPjwqz3dpwLW848y7g1is9c8snFJRU30vzrrHaGxpNogvuYwYbFhFAs7jNZjSkO6vfDbSa6KIjkzSsw2DhsTvQ7_yQ8w03yfBr59C20OeDvUAFo5TRXeKQ_AYEO8P7S3qR42DioXUOwYC3bim9T4SnRicF8Izm4AzQ8mKlT0d0ua_VDSZVrVvVOYG-u7lHVrP_Q3twHUer9GMY2vNLv5GHpmWKvLqkWZyjvRjD0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روند ساخت اسلحه های دورزن در یمن!
با همین تفنگ های دورزن، حوثی ها صدها نیروی مخالف خود را در هفته های اخیر کشته اند!
ثانیه 29 جالب است. یارو در دهانش قات می جوود اما دارد اسلحه دقیق زن هم می سازد!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21112" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21111" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=RELUZwJ7GqM1LGePs6oXhw7TzrWznL329k7fQmotTjFHZ6sIXjFbNsskFPbM5f7TJVoNqXDONGr-X78sXZjiG8uq_LVo5_kaltxQ7_VjJx0ytGu_tsMDsI6VzCD6q58w1YrcGU3yZ-ciggLx63bw2dIWSShvEdso8ugMH0tfsTi0pIofB81DVuuYwZn5dLRPKenljiWf1n7lTigsWnE9YYkqzGvqR5cUNblMxxJFLGTAhWcFdXmdjFSHw9Vf3vej4NOxBtq-4WCxhBPVyZDhHVSh-7RlW3fWMYCjMh_72ARJ-dSzvT6ispsDq8-z4AGOvbFjNUvoLP7K2G62VSKpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=RELUZwJ7GqM1LGePs6oXhw7TzrWznL329k7fQmotTjFHZ6sIXjFbNsskFPbM5f7TJVoNqXDONGr-X78sXZjiG8uq_LVo5_kaltxQ7_VjJx0ytGu_tsMDsI6VzCD6q58w1YrcGU3yZ-ciggLx63bw2dIWSShvEdso8ugMH0tfsTi0pIofB81DVuuYwZn5dLRPKenljiWf1n7lTigsWnE9YYkqzGvqR5cUNblMxxJFLGTAhWcFdXmdjFSHw9Vf3vej4NOxBtq-4WCxhBPVyZDhHVSh-7RlW3fWMYCjMh_72ARJ-dSzvT6ispsDq8-z4AGOvbFjNUvoLP7K2G62VSKpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:  باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.  از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21110" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21109" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آکسیوس:   تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21108" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آکسیوس:
تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SBoxxx/21107" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:
باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.
از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت بشناسد و روابط سیاسی، دیپلماتیک و اقتصادی با آن برقرار کند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21106" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !  یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21105" target="_blank">📅 19:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=MTDdvbhRJmSu-oFPLONhgIa1fMOCWWQyNq7ag0y8zVvDRtqeIqCjKbxB7nABvWKxOd7ewIDyBolXFOoUfHZeyUE1dcm9gKLaDxWN_ysGuFEXjTnx0fR8Cqow0_CBokVee7gar-szOyUsvOfKkoq3uQm8WVeL_sAU5AidSvc0WptgVEz0fh1QQfiOWm6T5giL_JNJGZ4nCB0EJJxM-BJjNyzT2WjlMWD-5ab8wK4VzqbunMQrufUakjyySGU5GF5btaME4ONjeHKOrYyNX3JTU-kt0J811h45nsy6MVavLcK3v7R01l7tNiS0BoZhl66NXJrhsGkxNoCRp2SOQAtpdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=MTDdvbhRJmSu-oFPLONhgIa1fMOCWWQyNq7ag0y8zVvDRtqeIqCjKbxB7nABvWKxOd7ewIDyBolXFOoUfHZeyUE1dcm9gKLaDxWN_ysGuFEXjTnx0fR8Cqow0_CBokVee7gar-szOyUsvOfKkoq3uQm8WVeL_sAU5AidSvc0WptgVEz0fh1QQfiOWm6T5giL_JNJGZ4nCB0EJJxM-BJjNyzT2WjlMWD-5ab8wK4VzqbunMQrufUakjyySGU5GF5btaME4ONjeHKOrYyNX3JTU-kt0J811h45nsy6MVavLcK3v7R01l7tNiS0BoZhl66NXJrhsGkxNoCRp2SOQAtpdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !
یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21104" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 28</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 28
سه شنبه 22 سپتامبر  2026</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP-2bkkk4KrjcPS8-egPIGopwxvyPJc-RCqObsr7bYV2cT36zFrueKpo3_Gx43mc1QTFAOTl3eRWaOsk16RG01rbIJmuNnzPkMDpH1AsUz9p0BmB671Qe9lDOkb_e5HUrZDhJ97NKSN-EYS3sKWpUbGAZOXyDXO63C2mCTSzBCKH8KzF3gQ9DdQOHr_AqBzxnj1lwi8VnfDFCNzYm0HEaqmHduvVjVzz6hvXVthYSZ_qNt12NjIikr9btzTpAhsSaa3wkGm42cCwT6TSBDXtysiCcZc43MrrYh_H75IWfB99c_P6jSl8RC2sfeW7FkIHZaLSpSGDHV7VCgoBFM_Qsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6zvBcCIt7s3jklGreNL2gHHhN2A2olMetpFhOzLYYsInYJdb8nVpOV3VOBaHr4cudlPGxqasrulEbqYbvpBriX47pfrfPPj_8AyxeAelVkod14BapWDqYj8qRISSYdUvxgJQ1G35PxILaBk1jE9CGG5-ktewX4PYEjr2IXW4LlHa9Yw-GeteN_5oWTA4uyJenWC-sFweIFQdnzJHzZAjnDokWK55wZMCP480xgC09OGBqXRD8DxhQ5WhbfB5oeVhtC-ox76O4iM9J5DgjFiv8h6dknx8ce-m8JwtwGpMw79TRBHud_Gc01cDTM9GYoWB_7M8ge9gJnz8x9j2tQANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEwjrOkM5tVRi2CFAWa_BOIMswBo4_VT1Eb7I9fXD4UQQiOUxNs4yjJ1sSsFxrJ0Z41sHjGOivBOD-9ysWXdTym46UifUCql7s1fLylFR801YVFtixOEey1oU86i6E4yL5yKs5Kzjd84F43KmbeAnTdLjk0aGEQ_qG5k5cWke3aiT3QkBy12u9P3TqJxywsjusfB2g76qmmfBFLnvN5z4o43phoXI8qvo-YMG8bZkRtL2WCi60AFh_eTK4ZbUVuOzyHBxu9cfR7RErXtg-sSoO4NV4bdvkq50GxTqKh7VdzGhnwTIKcEbJYPbkOge7USRHmiC4SSb5YprAB5N_PvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLPIseaTR8cNmbjZUDyovoC6WG-Rp-RPqiTsc4q07peS-iTtaHeZNVoKbfX07xXze71n4AHr2GNe8-rGkgjJ3csmtGwaHhKEZ1R6S-3ZTAccGe_mkmJRzS8m0rAEnhiK8UNPq3imxlKaw7zJWCMAvmKggr--mrlM6ifg85-8wKWn3kwcwQKQu3hDXRZrC-FUBxYjzkji1u8r-1G0XH0XzqtJRlcKeahv8ODYJlBX-YeBtDaLLsbdyE_a6erJwcFUdINaYJCDGdgNB7fb6UzSuF9qX3sdD-kf0SxhzoypQp2sD7ov9k7oLEvxVbuRX3PRZTETJDVd7y2tOd5rxCzkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtrF-ksRWkuyDtFGB6o4VJKQPEmj82Z412omJ4BDMwBY8NecejInyr4D91PT6xFrSsJwsE8IhcQBWLz_jnDuSI7d1qEHGBYC1MJ9JWbOAVg2axf_cnLB90uipyyO8J8WgC4khY6kcjAWxyT9ThoDPNCqA25KFPTITXZulG6FcGWHYx4oKtnBZ0AlEjXQnuHwEHfP1LziUddhNpZW7kh2fLiUvIqmxmeGXKRHUbZZUpL_I2ZvjWEw6Z633N52j1xQv38Lm_oyMUGoqluqIq-gsnSMGDgWT9Emm7s8jIGSXVIv2ipuan08cjPtFjb71X8t4xnImVxQBqMvoG8dli46FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-_IhDr7vo90zpyzWXOaHRirU1H0F3GNPM3TBB0VikqmkA-_h8baFoOLWFdB4q0wiNB9cy9b_j2apXXRqpmH8YWfObgRms0TXl8kXUwstWZRczPUocav-IAX_mkENm6ddgtmDG3Ja-UIWYVo2Kb06ZFnC4mkK-qmQiABR1xHrlDaanrXEQROBdKg5EFRgYHCp1buB75KYzYPyLgezoehx_9aO4gl8IxMLlR5wUkVisVhJTNvzkgIAPoVJgBi-GokkqwvevCUY-ABjAAOgaWRqH_Vq9ox-rO75MOa5U1tclZeFRF0r-YjJSOzqLe2JchxihHm2VboXNWlfqvDz6kX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDn_-KFUwaGS8iAj9bMj-pnN6x2lPVPLF2yYgOwwV86Ny4bAi4ychsotiSE90UbkVaQujX_bjgG1vMuUn1bDK80CGO5C5sJSi0kYbdThAJeSub-bgPP-Pjcfa8UuR1gg-MSivL27ydDROdRBVwj6Z9DQ20iPIK9X3IgY021Ab9oMHCa8XLdIWm3V1StZtc7IrhFT8VDpsbi0ZWEklqvh7Ta2793H88bqy7Aq1dg3daWu0vbLnH-7jIYuSwJyqGm-IEQ_kBG_Soz5fxfKq2kJVRUZVxOzLV2exKamlXHoFFNo2tdK7lp8RGlVXeJ6R8hzsTMeVH6AkAPv-mzt-bPZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHPmd8EPBnpP-3fqA4b7o1ebBEV60edcR0DrOhJ5_MWiFPuT6R0lDT40IWfTtGaHOBPel92TQHPC46qw0GOx9o-M2iR7jvfxeZkUR6W1mhD5mTzoQuE9YAw7ssrHgK2xt2xHTjlF5DGu-mcICjEi-FVkkn5-YyPeIooEDl-f5ZxGgoKcbVRpKjJog9iSAD6JVdXu6tOxv2Ob-FW5GGhjYtgJlABprW5mPqeKfE_K7snkV6HcN5TDa7mpN1s1vboJL2SAYHlMGcJw48Jx0QnYSeG-iVQmJwLS8gX3VweTGRP4Cx6cCbW_AeN5tujHFxwvdP4L-pbAMCNkK_mj-gUW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX8qt6NFuOZYOP8AreYvr26LjwjXvjbqYRF5N2jXasiVDDVcEsS4JXXVAUHYsDijrE1FEEYHPqe_etI7PzcFlXEn4YUhlCUVvzgAKFK0gms1pfbSF5MnPJUThc6AwvyR5dvt0ZA8knEIsTJlgAwbfWt_zK0hzjYZT4QVxUb7nAGZLvfn5OhAiOuyc3AjlTuqQ2t3oVBBLdrpoblgif960nqaiL1FGpP0QmCS0Bfyj47_2Wx42f-2HjbR7Pj0r-a9sH7xPWJQ414l3dwDA0DIGCaDG8pP-uasE5xFk4XARtd6DRVfpa1IJFjlPdZZjX-h_sU0qNsC_chn83W-UZg4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
دلار، نفت و موقعیت های معاملاتی گرید از دید موسسه Danske
موسسه Danske با توجه به رشد اقتصاد آمریکا، سیاست انقباضی فدرال رزرو و اثر شوک نفتی، تداوم قدرت دلار و فشار بر یورو و پوند را پیش‌بینی می‌کند.
در بخش معاملات گرید،
GBP/JPY
به‌عنوان یکی از سناریوهای نزولی مطرح شده و ترکیب تحلیل بنیادی و تکنیکالی، افت قیمت تا محدوده 181 را مورد توجه قرار می‌دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNiXxEL-BXxHx9X4d1YGFOHKoGrcxxCBwMdYeAMghSMdqYBukqlgdsYLQIkxA2ydiGtaL1SV6ATPJRf9sgwkZEVav2iuvSZNqgkFq_DTUgCpMKj2Ixk_57cF5er9FLLRSQhwYz4DrWGZYMRGdY25-tgBYCz-v2NFBbwamHmBbjclK5lHOtBQMkykzRqghYdC_XPp0i-72d-tQpOpoQV0j3r0qHFMHMrGPeRTNnOsuwCItPNirjVtE7zHopEGO0j_mOg4mUH5-m2Y4n6yKT02SxjJqf_ecofnYNqaMk5Pc_KN_xN6BZ6gFQ_KJ_Vvdm008siWdCVyTGNY9n7l6MGCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzjoRxPVwh1bvOnz64ncY3V37hKl140rX-TJxkG5ms57cCj_np64MHME25wMzjMBrcE_PHvy4dFxGgAaALNiFyATSgb0QGPdykLVtRpn14WHIem0s6UUIUpkdAKnPm0zgfSA-Uu_kfgWWThWPMAi_OWIlrsCwclOexgwPHwOSneJmzUxcU4hGg6ORwrxa9gb_Q-HDXxK257h6Gr_w8eE6P1ya8SfBvt88H--prrbjui2v1J20ejiYMksaEDWkIOguACK64Wv6regtpZKCGpT2rCG4tF45z0hCbrgIy5vrWzkRfuS9R4aWCvUMIQexaMhKQwghzd6ZfBqC_M-55ntqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mioave-w7ziZi9hmLUSLENpLT7mQ-PKSCgq57026cpoKpeo5RDr8XruzsxNvG-o-JhLevxlhSWUYD6s6Bp29snAu-NXi6R_UbJ9koFuMUQRbvAj39zE-YRoW5nBTLwaO57szlZRlePqbO-I1PACPLvHcBoRua2s4xldm5bhnPwFCdiqeGix2CXbLENOrSMSTp8oGDLILdr9aXOi46EPotbGCKR4T_AZyQHJCJ0mM-unc7uRr4EiOHsEUZKwT21aFI78M86I2m3xFOYQ6XRYH56gt8IyQja49WRtxEP60HHP7fUvlQEeZrtKT0oT94aEf-xVH-EusJUqqZciPncfN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8mhFvAWRRdkeip2RAPj4d3a1X0RoTyS8L6oZ7smm-Urycoyc08YUR12dJJjoy48EWw5izTBsrva9nQSlAAOXPrGmEo2ioYgjR9QhOuoTWs3ILU0y7GHSwBUrxx3KeR2OdTejIciUppalSsmCMBC3OTP47ZuGiVp_RvrJCID4wxkDI1wZlVdik6QvSz4te8sWujkDqPrmQqwTJ4cTLaIxa0nmXoUa11skdgbEek_vedIfW7jAMuwPfDC_4yvuaidSPaPcS6hoBiwht3s3dG5DQ68M0xDXHqtM9qaU7x_v76mIJm80i8QbO8a5ADePtjZGaaW1wprp4ENKz05ozP0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2Veq30Q1rLHqyarZLaahtlBbd8WLyVJ_CXjtPSuWh0RpUtaD3r_D_kA0h8NE4u9FKPhSdW2LzoTEgFimDBv6N2yZ60j6_YX1eMkL4lnXymLON1rqlxLjAILq92xSlNfTG6xujvYhXuGnmQNJsN7722kaJ0yLT2k7mm4mqd5SDAxOwG9QSy3Ny52NiKRVeUMVcnDQ4oF24AA9LZ8r9Soc0hdHiNOmA29cqqoJDgq5QyY0FybChzQ6TL-brjiX0X_0k744ZPW6aTOiTCuRCG7azmZATZBC7-ZLUkSsV2AMCqKzod7JF0KMPmBLg8fhcWuU6Ipx1CJRZtRclZhZ_W9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9N7T2603dJh6-91osGHWw3xKfILUijQozKzoJqS5qjCFgjTrIGxqTUm_Kx98O0Pwfvkql7CvW3Ls6p2NsYu6quI41eD08PWIcA5_3RwnCZrHAFiqK0ILlW3J08d4NDlXIRkr2RiVj5bYXbFwNEIKdQRXHbUf8ssX7pkPuq4iJ56wRn_Oy87-Jb0ti0qTTJvVs3yEclbHdWOscYuc2lDsNS6CpY_eM8h_jbcdbkQBzeU9elZjA3OJojrTOmAUysNGDRgojE7h_PtQcCbQLQfdH2d1rWOqaksyGMB4jYLQ_jk53panFzJLRTOSXKQK7SnSBfaW73xJLrjZ7SxSuDwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZteAvzhfLp0RTPjKuIkUttUrde5LcEMfONMeM4ife9rIA1Wb53Oy0KLkygxtZUQAnflh6x8QpSZx_oK3jlRai5dHZfxffAZtnhHFQvcF5ZzvrUPFD01HzUfckoq7lSWfrQs979B8pjNKGw67YEE3VW5eRtM_iQRxic9-3mX_l2teqEfqajnkKxhC0ujrv4aOBgCz3bkVvCNxFybeommWnItlVOscBqsqGZOyTp1GP0ZOQ4yyhS_TUu7fwMUAFq3s4ParhOI2pB94PB3Sb81k-bSnTqE_3eJw6yFUU9EIqEYwqZADvQcY29LLcz42ht7cjD76lmlv_t5lhl1fSCQDDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
