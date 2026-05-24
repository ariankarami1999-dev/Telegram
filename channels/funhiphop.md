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
<img src="https://cdn4.telesco.pe/file/V1vEagIvlliBZ8AqabnI9k1mZUCiSQojMQhovJoH61r9NwcVSWRLQ6BRlp1hlzEB3iba_mSE8577es9496VtLQQuTAMSKN6cKkajkzUsOLzYHVXVu1ppZK3U_ELhfenVm042rL6u81GsUmRsllk8wjzfFz12_pLPJWjyUmaXdu16i9eghci4cFt-qsDwugN7FxVMn_ze8ZqAn55Yy-Y5RV9iyPuN_R-5S7y2KfkzyzudY5xpWFkIfFHHFwzDavvsYD3k6sEZKuNbCRwi9K-Y1D5u0x37yx8oJ16A8_6C8xqUxfnnSsgyUd0qfpiiNKqCbuRXbjYMMLfvTz69Sb_ADQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 21:24:52</div>
<hr>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عملا هیچ چیزی تغییر نکرده از دیشب
ترامپ کصکش فقط خواست مارو حرص بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/funhiphop/75787" target="_blank">📅 20:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگه کانفیگاتون ضعیفه دست به گیرنده ها نزنید و پول اضافی خرج نکنید، اختلال سراسریه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/funhiphop/75786" target="_blank">📅 20:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الجزیره: مشکلات جدی‌ای در مذاکرات وجود دارد. از جمله: موضوع لبنان: آمریکایی‌ها خواستار این هستند که نوشته شود اسرائیل می‌تواند «اگر تهدیدی وجود داشته باشد» عمل کند، ایرانی‌ها مخالفت می‌کنند. موضوع آزادسازی دارایی‌ها: ایران قبلاً در چارچوب توافق کلی دارایی‌ها…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/funhiphop/75785" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الجزیره: مشکلات جدی‌ای در مذاکرات وجود دارد.
از جمله:
موضوع لبنان: آمریکایی‌ها خواستار این هستند که نوشته شود اسرائیل می‌تواند «اگر تهدیدی وجود داشته باشد» عمل کند، ایرانی‌ها مخالفت می‌کنند.
موضوع آزادسازی دارایی‌ها: ایران قبلاً در چارچوب توافق کلی دارایی‌ها را آزاد کرده است، آمریکایی‌ها روشن کردند که این فقط در توافق نهایی اتفاق خواهد افتاد.
ایران به پاکستان گفته است که توافقی وجود نخواهد داشت اگر آمریکا بر این نکات اصرار کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/funhiphop/75784" target="_blank">📅 20:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کم کم دارم یه رابطه عمیق بین خودم و تسنیم احساس می‌کنم:
علیرغم برخی گفتگوهای امروز، کارشکنی‌های آمریکا در برخی بندهای تفاهم از جمله موضوع آزادسازی اموال بلوکه شده ایران همچنان ادامه دارد و تا این لحظه این موضوعات حل نشده است.
بر این اساس، در حال حاضر همچنان امکان
لغو
شدن تفاهم
وجود دارد و ایران تاکید کرده است که از خطوط قرمز خود برای احقاق حقوق مردم کوتاه نخواهد آمد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/funhiphop/75783" target="_blank">📅 19:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس ستاد مشترک ارتش اسرائیل:
با دقت تحولات را درنظر داریم و آماده بازگشت فوری به جنگ شدید برای تضعیف نظام تروریستی ایران هستیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/funhiphop/75782" target="_blank">📅 19:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یعنی کسی هست که واقعا خشخاش میکاشته و با پیامک قوه قضاییه پشیمون شده باشه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/funhiphop/75781" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یعنی کسی هست که واقعا خشخاش میکاشته و با پیامک قوه قضاییه پشیمون شده باشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/75780" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز: مجتبی خامنه ای دستور داده که اورانیوم غنی شده در ایران بماند  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/funhiphop/75779" target="_blank">📅 19:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7Q6PY7z5srxQBrkB1YOpLRLZXQGxRaYb9vo-zJX9_avOaTiyh0EWl3ALu1UkKBYAKhYfdTnJeqMS9TQ2vvq6aatoRL6joVn-qFFPpa1Gs6o44sYQWQ5aqPfgxauDFcpoDD6Ac12yvTOJ1BFjSC_LrUaFls5PGHeAtbqtyjQPaPLWnwhry3zZYtUK0iUtxqiOLoxb_Yeh0Ct67727j4St_i_yCuDwwoZSE_Tzd6p-hhbh87yFzCpgxamZy4F-ZetvHtqoo-rxArW7n2G3CEyRpM1oP30q9JkZDRLe6tmbCFCeW5BJBXY6lgKwt4rPG3wg2BTEBCgs6uSokB77MFcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FunHipHop
| blue</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/75778" target="_blank">📅 18:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75777">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام ارشد دولتی:
اگر ایرانی‌ها در مسئله غنی‌سازی امتیازات قابل توجهی بدهند، ما نیز در زمینه رفع تحریم‌ها امتیازات قابل توجهی خواهیم داد.
در موضوع هسته‌ای، برنامه فعلی این است که با کل ذخیره مواد غنی‌شده برخورد شود.
اگر توافق نهایی‌ای داشته باشید که ایرانی‌ها در آن خواهان ادامه‌ی غنی‌سازی باشند، پس توافق نهایی‌ای ندارید.
درمورد تنگه هرمز، این مقام گزارش‌های خبرگزاری فارس را که حاکی از کنترل تعداد کشتی‌ها توسط ایران بود رد کرد و گفت «ما فکر نمی‌کنیم دریافت عوارض نتیجه قابل قبولی باشد» برای این مسیر آبی که حدود ۲۰٪ تجارت جهانی نفت از آن عبور می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/funhiphop/75777" target="_blank">📅 18:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آکسیوس:
برخلاف گفته‌ی روبیو، یک مقام ارشد در دولت ترامپ گفته است که انتظار نمی‌رود توافق با ایران امروز امضا شود.
چندین جزئیات باقی مانده که باید نهایی شود، با رفت و برگشت‌هایی بر سر بخش‌هایی از توافق (برخی کلمات که برای ما مهم است و برخی کلمات که برای آنها مهم است).
مقام آمریکایی گفت که مقامات ایرانی با سرعت کافی حرکت نمی‌کنند و چند روز طول می‌کشد تا پیش‌نویس از تمام مراحل تصویب عبور کند.
رهبر معظم ایران، مجتبی خامنه‌ای، قالب کلی را تأیید کرده است، اما اینکه آیا این به توافق نهایی تبدیل خواهد شد یا خیر، سوالی بی جواب است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/funhiphop/75776" target="_blank">📅 18:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75775">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کان نیوز: نتانیاهو در گفت‌وگوی دیشب با ترامپ، نخست‌وزیر تأکید کرد که اسرائیل آزادی عمل خود را در مقابله با تهدیدها در همه جبهه‌ها حفظ خواهد کرد و این جدا از توافق ترامپ با ایران خواهد بود و ترامپ هم این را مجدداً تأیید کرد. ترامپ تاکید کرد که در مذاکرات بر…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/funhiphop/75775" target="_blank">📅 18:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZl6GcP_bKBSyqtZe21UzhhW_3lnzilpS6-qoQhlAEUfmdnMs2ALhqRLsYwWDE_f_nNjosUI2ktWjNGXrZDwE58i6pGK6KI8ky5qe3XpwI5wh-cBWxrBGFSOvfhEtedyJavgb7IbaI5U_TKvkH3PTMfTtJgy-wOasIw8vDZoiBgAvujgD2oT7G8-TDW6EugNUQ7YWfecrV99uJdMuWtN-yvwGs9xHoj-93EAx6pKie489-bCj5E2o-8b2aK3QxUjbnTfBS7oA4czfrzhbNofGitYQ3iZfrjXt2ov5vRhzQbGoQK4dHWnIz1YqhwoVC2eEe-jVJBSH8TJpZEkPYpDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ که اوباما رو برای اعتماد کردن به حرف خامنه‌ای برای نداشتن سلاح هسته‌ای مسخره می‌کرد، حرف پزشکیان که می‌گه ما سلاح هسته‌ای نمی‌خوایم رو پست کرده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/funhiphop/75774" target="_blank">📅 18:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ یه طومار فحش به برجام نوشته و گفته نه ببین مال من فرق داره:
یکی از بدترین قراردادهایی که کشور ما تاکنون بسته است، توافق هسته‌ای ایران بود که باراک حسین اوباما و آماتورهای دولت اوباما آن را مطرح و امضا کردند. این یک مسیر مستقیم برای توسعه سلاح هسته‌ای توسط ایران بود. این موضوع درباره قراردادی که دولت ترامپ در حال حاضر با ایران مذاکره می‌کند صدق نمی‌کند - بلکه کاملاً برعکس است!
مذاکرات به صورت منظم و سازنده پیش می‌رود و من به نمایندگانم گفته‌ام که در امضای قرارداد عجله نکنند چون زمان به نفع ماست.
تحریم‌ها و محاصره تا زمانی که توافق حاصل و تصویب و امضا شود، به طور کامل و موثر باقی خواهد ماند.
هر دو طرف باید صبر کنند و از صحت توافق اطمینان حاصل کنند.
جایی برای اشتباه وجود ندارد!
رابطه ما با ایران حرفه‌ای‌تر و سازنده‌تر شده است.
با این حال، آنها باید بفهمند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه دهند یا به دست آورند.
من می‌خواهم از تمام کشورهای خاورمیانه برای حمایت و همکاری‌شان تشکر کنم که با پیوستن به کشورهای توافقات تاریخی ابراهیم، (عادی سازی روابط با اسرائیل) این همکاری تقویت و مستحکم خواهد شد و
شاید جمهوری اسلامی ایران نیز بخواهد به آن بپیوندد!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/75773" target="_blank">📅 17:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سرلشکر محسن رضایی:
پشت صبر راهبردی ایران خشم انقلابی ملت است.
در صورت هرگونه اقدام نظامی علیه تنگۀ هرمز و تلاش برای ورود به خلیج فارس، جمهوری اسلامی پاسخی سخت، دردناک و بی‌نظیر خواهد داد.
اگر دشمن به تنگۀ هرمز وارد شود و سعی کند با زور آن را باز کند، ما هم محاصرۀ دریایی را می‌شکنیم و ممکن است از NPT خارج شویم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/75772" target="_blank">📅 17:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNHMHl9Jj0ak3Ahi1T3y7e6bOhTv3MOVvEkgOMtF2nwIjuFLosEkIHdqyf9yXXpfyCizhDcMTt_cuB0MGBu8LhhYBe97KlbUY56SmM5wCm4iLntweSL03S9miaEQX6Nbby6T6PHsxLDVmx-Zq-0oPIdFn7AEcxy-pjSior1zUyz9TPn_hPS5dS062E1ziadkMQdvJTykvjRz7Cr83ndp1V1H-FYSHc92LyRrrN-qlWO_KxkP7myuRFZr64nPD21t6O3XeSRcwr8mC8g3qY6gOMLvZG8Gye31il5LbgB3OcbrAZCHZo90rXEJ977shJCorqVpjgw3EYEsji2mQHDUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نتانیاهو رو هم روانی کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/funhiphop/75771" target="_blank">📅 17:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به آ‌ب‌ث خبرها:
نمی‌توانم درباره توافق صحبت کنم؛ این کاملاً به من بستگی دارد، و اگر خبری باشد، فقط خبرهای خوب خواهد بود.
من معامله‌های بد را انجام نمی‌دهم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/75770" target="_blank">📅 17:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a2494136.mp4?token=FEYfZjioHJmUG9hhfpqr8fE1YuVsubVaTJpxywh7eg1cLn7EJJgAFxGpT7Z5enjZ3hHqMAOXZs-e1nLefLi-PnZCwFKuJdmipDTy1RE-JEUnSacFrCyJ1NDyEURdBKfMfuAA7JUPP605wVhP9F0aL_Pu4umds-saBsU03LtuB0wmbaAbBxraRnLy-Jd5Hw3hou-aA_4xt2nprzHa1-aONLPLapnm1GkL1G5-9A3G9Xb1E1hxz8L8lVtw_XF_fA4We5rUxc_z8vIK2YFFJyBdMXt_cGLfAUzyabAHfhJvxr9NCfLBnDCPYPGLZj0nWhWCGVGIxQv9r52K6L6rNhj2iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a2494136.mp4?token=FEYfZjioHJmUG9hhfpqr8fE1YuVsubVaTJpxywh7eg1cLn7EJJgAFxGpT7Z5enjZ3hHqMAOXZs-e1nLefLi-PnZCwFKuJdmipDTy1RE-JEUnSacFrCyJ1NDyEURdBKfMfuAA7JUPP605wVhP9F0aL_Pu4umds-saBsU03LtuB0wmbaAbBxraRnLy-Jd5Hw3hou-aA_4xt2nprzHa1-aONLPLapnm1GkL1G5-9A3G9Xb1E1hxz8L8lVtw_XF_fA4We5rUxc_z8vIK2YFFJyBdMXt_cGLfAUzyabAHfhJvxr9NCfLBnDCPYPGLZj0nWhWCGVGIxQv9r52K6L6rNhj2iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من در حال تماشای ۲۳۹مین لایی جرمی دوکو به صالح حردانی و سوپر دابل هتریک روملو لوکاکو مقابل بیرانوند :
@funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/75769" target="_blank">📅 17:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75767">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWinro.io</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGtyjEi7Q8ieazfMlN5u_30YH6Vl_n8VZD_W_i0_DHaUPIbCZCdr6gbbb3kBIsprheLbkq4Jco72ZEKKzI2tSKb5YWv5GOXvxkitzE5RMQFKtDfI9NBjRux44BYM2o-6K_xpywPxxGQMCsAw297PmN7qKlpNHVufnufV2oNXniyUuXWzQQistxyyO0XV9GnKHRJrF-V18QREJr8Mj5yGHKLV4lrPqtqRGhBS1ZNrVItSxcd8nAtAJFF4zZiZQMnhXWuqwxFdEZ7h3OrWUYar1x5m8LzCrFavzsJTmIDFcmo_ThDx8unCvgmDCMzQ098YQHFQW5LE7zFiSD7xNdtnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
بونوس ویژه ثبت‌نام – ۵۰۰٬۰۰۰ تومان رایگان
با ثبت‌نام در سایت، ۵۰۰٬۰۰۰ تومان بونوس رایگان دریافت کنید و شانس خود را امتحان کنید.
🔥
چگونه کار می‌کند؟
1. ثبت‌نام کنید
2. بونوس ۵۰۰٬۰۰۰ تومانی دریافت کنید
3. شرط‌بندی کنید و بونوس را به موجودی واقعی تبدیل کنید
وقتشه بازی رو یه جور دیگه ببینی
⚽️
پوشش کامل مسابقات ورزشی
📊
پیش‌بینی با بهترین ضرایب
⚡️
تجربه سریع و حرفه‌ای
💳
پرداخت مستقیم و سریع
بدون واسطه، بدون دردسر
واریز و برداشت در سریع‌ترین زمان ممکن
⚡️
📲
کانال تلگرام:
@winro_io
🌐
هدیه خود را با ثبت نام در سایت دریافت کنید:
Winro.io
سایت اصلی در روزهای آینده بازگشایی خواهد شد</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/75767" target="_blank">📅 17:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75758">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcDTVhU5m6n8puSzUCszqogQDDoyNqbB2NWRT5KBO5pbDYitdhW0RmL5QYfYPEmGCqsh3rVRGoJGzZmgFqxy_56y6yCqvvAXWQtzqn33KH5B3e0POMwoaiRloXes5uAryQotpS9H9rBlvxB_ZGu86OWd3udDoodVjD3vEkQWJTNTiqNEMQtRN6fFQxaUSdCnlrVMV77LtaT7_LB7uHB0D2mr1sQTsU2P5nGuPTM67xTzDMK9cdTPKhL86PWXrV4aW3lk4V_HNJFRQ7POkdl35kFUzmASVvwf29yFyYYZZAdqdi5dD4EPS8YQYKTlZA1eCN0l1WOO2a-GHZBgSzyhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXjLnzlmYcVTBbCTvOInGVI-5DjFm1knj4XEDeMzJtdv-Sko4BQIwDNSOpkUMEc4QyZ0tVIGMje05tY8VHqyPQ7ktR5t4pz4HFm2xSicSv8KreMHv_TQ4OUyj6i9J0JjzcdEOVgHRBBJqlWwVcmSS_FZVqb34wDlfNetjjBHZyS04ALf8gcc0T6SGUKsubjrRsfuFjDiYgEX4LfahKslDabVYLxarE39V5uolnaBTCTtfNCS4BHPhD80Tx7paMkucmyfQVjFjAlu3Zi_HpYN-EHs6ZqUT7sU7KYaCSsw4UeoCVZpf-19lBm4Py6iTT6LmOXnuoOl5_aFd-23gcyf9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/75758" target="_blank">📅 16:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75757">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/manSrJheIwGDYo8YwzWsMHClw5aeZuHA7hnd6Cot7hAZe1xONqhspM-aui1VZZPMY_dI1_PIks35jJEPg-iatRkCaI2CldwNASkkjp1BdsJuZ5RLubY25NMGQ1HweObUb_SLv7-a3jJFGK1THtGDKkAD189xePKjpeR7SQU3RvknN0q2dIScEiemfi6HB_uSnspe6xk0CtiqU182mb9urPPBcliRRx9LE-ohRJkuMyh1wD8OaQdCeXQ1IEJUfPZBR8D9JXsILGehGCJwUZuSGjUqnSyn8jEKe8YkYGQAgS4mOmg17WzXa3t_0tlt6eDAQVKohPJz3VYKcZbCZzhwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی بیا یه بار شبیه آدم بزرگا رفتار کن ببینم به جز دلقک بازی چی بلدیخارک
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/75757" target="_blank">📅 15:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75756">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیشرف خیلی خوب گفت</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/funhiphop/75756" target="_blank">📅 15:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75755">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خب کسخول توام رسانه رپی داری درباره همه چی نظر میری</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75755" target="_blank">📅 15:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75754">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در آخر هم کیرم تو کشوری که چارتا خواننده و فوتبالیست و بازیگر بخوان توش راجب همچی نظر بدن و لیدر چیزی باشن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/75754" target="_blank">📅 15:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75753">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">علی کریمی اشتباه زیاد کرده تو زندگیش، ولی گاییدن مادر شاهین نجفی یکی از اون اشتباهات نیست.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/75753" target="_blank">📅 15:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75752">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تسنیم:
عبارت «تمدید آتش‌بس» اصلا در تفاهم نامه نیست.
برخلاف گزارش یک رسانه آمریکایی که می‌گوید طبق تفاهم نامه «آتش بس میان ایران و آمریکا به مدت 60 روز تمدید می‌شود»، این عبارت در متن وجود ندارد و
تعبیری که به کار گرفته شده است، اعلام پایان جنگ در همه جبهه‌ها از جمله لبنان است.
بر اساس متنی که هنوز نهایی نشده، در بازه 30 روزه موضوع تنگه هرمز و محاصره دریایی پیش برده می‌شود و زمان 60 روزه‌ای برای مذاکرات در مسئله هسته‌ای در نظر گرفته شده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/funhiphop/75752" target="_blank">📅 14:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75751">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=G9uMo1kyqqwU92ZEelDstDUI2b_8xg2MtLzfr9OEj2yw5gQAe8yY-k1iRlkIgO1PnyM5eirY81WRTpXoG23xaLdv2FYihkGqhH2IY9mcy6DOrVfDyjD1rb57QU_O2OMKLaAwP2mxb0lWsH_xiKo4wo9Zdrl2O2OHX28qfXnsNkIHpiCYHV40a30Kfgb0VZ27iKykZNZ0-RoSvR7GpQoVL7GOeVN5msJ9GtuSdUeJMnK4apuJtaVow8OkhY7HhY_ybLkb0r35lkjilL8_rSf1uHE6v5XPynJBS117ZkQTKkf_tHQjZRnFe21jZXau4tZ0w4imk9N9bdTEtke7OaPRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=G9uMo1kyqqwU92ZEelDstDUI2b_8xg2MtLzfr9OEj2yw5gQAe8yY-k1iRlkIgO1PnyM5eirY81WRTpXoG23xaLdv2FYihkGqhH2IY9mcy6DOrVfDyjD1rb57QU_O2OMKLaAwP2mxb0lWsH_xiKo4wo9Zdrl2O2OHX28qfXnsNkIHpiCYHV40a30Kfgb0VZ27iKykZNZ0-RoSvR7GpQoVL7GOeVN5msJ9GtuSdUeJMnK4apuJtaVow8OkhY7HhY_ybLkb0r35lkjilL8_rSf1uHE6v5XPynJBS117ZkQTKkf_tHQjZRnFe21jZXau4tZ0w4imk9N9bdTEtke7OaPRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
به پیش قراول امت اسلامی، نیروهای مسلح و مقتدر نظام جمهوری اسلامی ایران موفق شدند، یک فروند پهپاد شناسایی فوق پیشرفته مداری اسرائیلی را، توسط آتش پرفروز و پدافند قدرتمند هوایی ایران و یک سامانه دفاعی فوق پیشرفته و نامشخص شناسایی و در منطقه بندرعباس، سرنگون کنند.
جزئیات تکمیلی متعاقبا اعلام خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75751" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75750">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فاکس نیوز:
توافق احتمالی مقرر می‌کند که نیروهای نظامی آمریکایی به مدت ۳۰ روز در نزدیکی ایران باقی خواهند ماند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/funhiphop/75750" target="_blank">📅 14:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا:
به مشت گره خورده پیکر رهبر شهیدمان قسم، نیروهای مسلح مقتدر کشورمان اجازه نخواهند داد تجربه‌های دردناک تاریخی در حین مذاکرات تکرار شود و به اذن الله اقتدار و سرافرازی جمهوری اسلامی ایران را بر دشمن تحمیل خواهند کرد و آماده پاسخگویی سخت و جهنمی به هرگونه تجاوز هستیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75749" target="_blank">📅 13:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی ترکیه با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید
✉️
:
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/75748" target="_blank">📅 13:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTAqACOxp2qrPfp9VJGxmFgJbRnK6falk_6pP3AZIBVUfqdsuCYpo2_jYOhyazlOw5KuOli5oUu34KEKNq82_TB1MWidZdyoRgOfNMjKHuko7RYAncG20Z1fNwnUOk-qE9zEPzr-AcjGOQHs2BUyWlGHjS2DZMAUNwRUejQ_HQ0eeAKAE-dN4jrA2D1s9tKzWmalCFCOYUBlKDCAXv2NTKQzlAL7huf2-rvlJZXIbeZPVOG0fTEj6AG3qhPTJ9cbQkTia8nYiv9c2WnodvMyD2sNusGZ6Z3fhk5KJ9nYASCzBktPx93GcttOUebLabQwxvsdJds1etuiaPI9iBfeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/75747" target="_blank">📅 13:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کان نیوز:
نتانیاهو در گفت‌وگوی دیشب با ترامپ، نخست‌وزیر تأکید کرد که اسرائیل آزادی عمل خود را در مقابله با تهدیدها در همه جبهه‌ها حفظ خواهد کرد و این جدا از توافق ترامپ با ایران خواهد بود و ترامپ هم این را مجدداً تأیید کرد.
ترامپ تاکید کرد که در مذاکرات بر خواسته مستمر خود برای خلع سلاح برنامه هسته‌ای ایران و خارج کردن تمام اورانیوم غنی‌شده از خاک این کشور پایبند خواهد بود و بدون پذیرش این شرایط، توافق نهایی را امضا نخواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/funhiphop/75746" target="_blank">📅 13:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک منبع خیلی آگاه ایرانی در گفت‌وگو با خبرگزاری رویترز:
در صورت موافقت و تصویب توافق میان تهران و واشینگتن در شورای عالی امنیت ملی ایران، متن سند جهت تصمیم‌گیری نهایی برای آیت الله مجتبی خامنه‌ای، رهبر جمهوری اسلامی ارسال خواهد شد تا به تایید ایشان هم برسد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/75745" target="_blank">📅 13:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پروفسور امیرحسین ثابتی، نماینده مجلس و عشق من:
در هر حال چه توافقی در کار باشد و چه نباشد، اولا؛
جنگ در عرصه نظامی ادامه دار خواهد بود. چون هدف دشمن نابودی ماست نه مذاکره و حل مسئله.
خصوصا که جمع بندی دشمن بر این است که باید "مخالفان تسلیم ایران مقابل دشمن" در همه سطوح ترور شوند که گزینه اول‌شان رهبر انقلاب و گزینه‌های بعدی‌شان فرماندهان نظامی و سپس سیاستمداران ضدامریکایی ماست.
ثانیا؛ اگر توافقی در کار باشد آن را با خطوط قرمز رهبری می‌سنجیم. چنانچه توافق با آن معیارها تطابق داشت از مذاکره کنندگان حمایت میکنیم و چنانچه نداشت، با آنها رفتار دیگری خواهیم داشت.
کنترل تنگه هرمز به دست ایران، عدم گفتگو درباره مساله هسته‌ای، گرفتن غرامت از دشمن، لغو تحریمها، آزادسازی پولهای بلوکه شده و... بخشی اصلی خطوط قرمز است که باید در هر توافقی رعایت شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75744" target="_blank">📅 13:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شمارو نمیدونم ولی هر سمتی که امید دانا باشه، من ترجیح میدم برم سمت مخالفش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/75742" target="_blank">📅 13:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کاش اپوزیسیون امام خمینی هم دست شاهین و علی کریمی بود واقعاً
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75740" target="_blank">📅 12:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc-ZcV9CWGGI9BHwNq8sHRmdgdQmcyIHE18W7_-400j5RjQxzCi77xIuhoT-mHon5auqJkkTuCDbJb11tlRjAGj-MpndKbg-CUmuW9KNZpe_vHVrNfyCZiuFmfi-kJjNFuN4U0OmwPy11_OBlt6L8nlmbUHQ_BBqnfjqnbZ8Rr505m0FXyAymhglTjhRiZ6hyEO1bkwgSUdPgmVCUzY7gFCTZ1Aci9vq74Di_LdFwTtMf1xQqejVPG6owx1g3I3Ji7FWTbmoMl0khIBIRKReQhQ7qtQMxq67f3bV8jFH04VMADWsgwYbDDkL48RYm2wzVLHb7TAEpLY4E5-dJy8rPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی بنده خدا چرا کاور شده   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/75738" target="_blank">📅 12:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W67yz-y09htOIKeNY6rV6_MTvD0MJ4G49UGj79imz29CscnGk-QWR9L6xcI7TMdQaIDL480JQsL6JhELSb1a3bZu8yBH3vPT6fBTBiQ7z_14yPb95RuTUdZBVi6g3LMnm0gYPjuDFHqqHmKKQzcXnlwYUJfdeQdwGJPn3TtB_2Fqp4hwDirNSMV5EK8TfgkDlDHyFNN5bHh4BZQWOekKSjUi9nJKrO8ONTM-rs5AethZCZK3BwHdY0ks72MdZKO0MHzljd5VxAmN4yZhJoIekiJ5zJu6u2nEgNgRmNksYZbpR8Iqmm995kaIdm0qR-ttjllQOgfWYBkXb6OnAc9cpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfQXcN1Zneamt3oG6E57jekVr7UPhledQrZN_91bMQ4LLrI01Q4KFhlVio5EjwQpQss9CpjETqK3BT1jYZXbq5V11NmEnsIhizv6J9-b1mHTDOBbXaG7QlXFcRbiwjF6l8FjVATHd4t9ssF5p05HV4OJUEi0UxH19Rw74v5hS_z93gLdj_K-Vk_nGbNH6QW8DLaeE1iC-45T3KPMc4AYY_wKR8q4plnfAuUhwgIb8cdU1vU9dF1NxD3LmPwu5AxEeS69xQMA4WfOLDoe5jKkjn3fXo5R9cxm-C6AFNztKSr1AlslYGgyu1Z6Rw_GdjXk0cVdhH2WFuWVi-JKUR-cfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رضا پهلوی بنده خدا چرا کاور شده
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/funhiphop/75736" target="_blank">📅 12:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بمب جدید تسنیم به نقل از یک منبع به شدت مطلع و آگاه:  اختلاف میان ایران و آمریکا بر سر یکی دو بند از تفاهم نامه احتمالی همچنان ادامه دارد و به دلیل مانع‌تراشی‌های آمریکا هنوز موضوع نهایی نشده است. ایران بر احقاق خود مردم خود تاکید دارد و این موضوع به میانجی…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75735" target="_blank">📅 12:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بمب جدید تسنیم به نقل از یک منبع به شدت مطلع و آگاه:
اختلاف میان ایران و آمریکا بر سر یکی دو بند از تفاهم نامه احتمالی همچنان ادامه دارد و به دلیل مانع‌تراشی‌های آمریکا هنوز موضوع نهایی نشده است.
ایران بر احقاق خود مردم خود تاکید دارد و این موضوع به میانجی پاکستانی اعلام شده است که در صورت ادامه مانع‌تراشی‌های آمریکا، امکان نهایی شدن تفاهم نامه وجود ندارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/75734" target="_blank">📅 12:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مارکو روبیو درمورد توافق احتمالی:
پیشرفت‌هایی حاصل شده است. پیشرفت‌های قابل توجه، اگرچه نه پیشرفت نهایی.
شاید در چند ساعت آینده جهان حداقل در مورد تنگه‌ها و روندی که در نهایت ما را به جایی که رئیس‌جمهور می‌خواهد برساند، خبرهای خوبی بشنود.
این ایده که به نوعی این رئیس‌جمهور قرار است با توافقی موافقت کند که در نهایت ایران را در موقعیت قوی‌تری در زمینه جاه‌طلبی‌های هسته‌ای قرار دهد، مضحک است. این اتفاق نخواهد افتاد.
درباره تنگه هرمز، آنها مالک آن نیستند. این یک مسیر آبی بین‌المللی است.
کاری که آنها اکنون انجام می‌دهند تهدید به نابودی کشتی‌های تجاری است که از یک مسیر آبی بین‌المللی استفاده می‌کنند.
اگر اجازه دهیم این موضوع عادی شود، ما یک الگوی خطرناک ایجاد خواهیم کرد که می‌تواند در نقاط مختلف جهان توسط افراد مختلف تکرار شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/75733" target="_blank">📅 11:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز به نقل از یک مقام ارشد ایرانی:
برخلاف ادعای رسانه‌ها، تهران با تحویل ذخیره اورانیوم با غنای بالا موافقت نکرده است.
این مرحله از مذاکرات فقط بر پایان جنگ متمرکز بوده و هست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/75732" target="_blank">📅 11:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قوه قضاییه: امروز صبح مجتبی کیان به جرم ارسال مختصاف صنایع نظامی به شبکه های ماهواره ای معاند (ایران اینترنشنال) اعدام شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/75731" target="_blank">📅 10:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ان وای پی: نصیره بست ۲۱ ساله، مهاجم تیراندازی نزدیک کاخ سفید، طبق گزارش‌ها خود را «عیسی مسیح» معرفی می‌کرد.
او پس از شلیک ده‌ها گلوله توسط نیروهای فدرال هدف قرار گرفت و کشته شد. گفته می‌شود وی سابقه مشکلات روانی و نقض محدودیت نزدیک شدن به کاخ سفید را داشته است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/75730" target="_blank">📅 08:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نیویورک‌تایمز: مقام‌های آمریکایی مدعی شدند ایران در توافق پیشنهادی ترامپ با کنار گذاشتن ذخایر اورانیوم غنی‌شده موافقت کرده است. جزئیات این موضوع در مذاکرات آینده بررسی خواهد شد.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/funhiphop/75729" target="_blank">📅 07:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8mCZP6gCXC8FL_WnFTBMz3_eOJCicj5cWtUgXc47CtDH70u12I6LzOvbZjCamfbKI_bZzfURmCAaSmJgUHU3A5mE_52jBWr177r0HzthLyXX0AN8-QHATvNMXoiAOJNQhq6ODgM1OzKcDqIfD7DRNZeG-G5Or2RpndNlNgc-X9_bqAbuoHHgS7pUQuxDI3hBKxEC4xaBgief8stD3CpyJcho7uOyvro6p6aRsamOHfMk_K59tpbRYmVrIy_tEgAcDVNEmuBDlTnvBu-x9-V5G5smzY9et9EARBloa7vRHeCyWiq3wmB0gBOZb7cB2HHcgIgzkPkptNUGh98nLdUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا قحطی بود برا اون عکس پسر؟
باید سعی کنی تا انتهای مسیر نیش ترمز نزنی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/75728" target="_blank">📅 05:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikURi3GNgThs-8qiDbtLFh_p8daSmgOi2_hRD3_R8T9lNvkUyDQeGuak8qY1vXsMhBpKhbFyv9xAAy1A42B-R1pm8UajAoIPU6ot9353sBQoXYsp8Lvq39gQvBWFpq8IbGq5vWxwqN0Vbku5XCUFr73naL4nzez3BPhW3stKUZA25_oelb6pfV4DbnW-Vm9XDs1TzHCNASeNcsQt-WRrhLUXwe41-CQGpnL5B4nhbFuPn55PA8DLE8verZ8CCpw0iZ11I74baS10I9xWK31qamvu-mQwDZj4uWgpbyjHbqi7xp476M7gvVehKVo8YW30DaiuBw9QrFUYZGpsnVb-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه یه سری حرومزاده برای چس تومن پول، اقدام به تبلیغ بدافزار در قالب vpn کردن. روش کار به این صورته که با عنوان “نسخه فلان مود شده / رایگان” یا “قیمت vpn خیلی خیلی ارزون” شما رو توی تله میندازن و میگن برای اجرا باید فلان فایل رو نصب کنید.
از نصب هرگونه فایل تحت عنوان vpn از منابع مشکوک در تلگرام، جدا پرهیز کنید.
گوشیتون کاملا بگا میره و میشه منبع تبلیغات برای قشر حرومزاده دزد.
الان همه وی پی ان پولیا با همون نرم افزارهای عادی v2ray کار‌ میکنه و نیازی به نصب چیز جدیدی نیست.
@Funhiphop
| Comentive</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/75724" target="_blank">📅 01:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
نیلی افشار بلاگر اینستا رو یادتونه که بعد قطعی اینترنت بی پولی بهش فشار آورد و اومد سمت Only fans ؟!
👀
برای ورود به چنلش صد دلار هزینه کردیم تا عکس و فیلمای جدیدشو برای شما بزاریم توی رباتمون
💵
‌‌ مشاهده عکس و فیلمای نیلی  ارزش دانلود 85 از 100
🍒</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/75723" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcKqjzQh3SsbFrefLtCliu1BcaFSgNmCCTUqj48VyivXSLsPn8MBQlAw_vqgIES18Ew3MnDqP0YELuUlpNxyukiLk1bFpq0Gx9i4CByKojocnaZnvxWhUse6Uueglr-SnFR1pRVev5bncFyk_xdEyqb6Pf36OhfSDGfgKWxwbzeiUy8iZ7PZAK7etLMom-Jrgd_3DoRZbVvAwwLmWwDrPGF3-iq6Sx4IHM-TZk_xo7hhCsUbPuAWYLCMScYsKehK3r6V9t6ItwG0ntQPZFAcf5qhEnBEJU5Fhgh_2QvARNvuIBQn47rO_bdS3d2CAEaKaBPyJyFIqOwrsDGIfk64Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیلی افشار
بلاگر اینستا رو یادتونه که بعد قطعی اینترنت بی پولی بهش فشار آورد و اومد سمت
Only fans
؟!
👀
برای ورود به چنلش
صد دلار
هزینه کردیم تا عکس و فیلمای جدیدشو برای شما بزاریم توی
رباتمون
💵
‌‌
مشاهده عکس و فیلمای نیلی
ارزش دانلود 85 از 100
🍒</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/75722" target="_blank">📅 01:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الجزیره: توافق موقت بین ایران و آمریکا به مراحل نهایی نزدیک شده و احتمال کاهش تنش و باز شدن نسبی تنگه هرمز وجود داره.
فارس: برخلاف ادعای ترامپ، تنگه هرمز کاملاً به شرایط قبل برنمی‌گرده و کنترلش همچنان در اختیار ایران باقی می‌مونه.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/75721" target="_blank">📅 00:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjcFobkTaTJLrL-fjNiPJcikiAj_03W-tDXPYaTGC8BSLrjtYSPJZDAdEGzvbySiC3hBhseqNK4Wb84UuURQDRwEzhK6SnRyi9W3bZp80W-oSvaYEgOHEKOAUWH_9J5OsGSixucpX81qHl8gpyUkdc6vpBu6Eccg6Tqn73eEo5QYKFckQ3xBIsuTDn2eIl5PsAKsYUQfea421CzPVMTiD6A_Jg207wKief-3HK4y3dU7lEnkoaZ91smuDbFLxzVXzx-Ww3kLnR9hzl4dSnYqvunfBr6S_CcTgzgv6mOSc4BNPLbGp2wAUY9T6UoULC-Sj4kx-Joz45ZtOw-1ceN0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/75720" target="_blank">📅 00:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ کصکش من که میدونم داری دروغ میگی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/funhiphop/75719" target="_blank">📅 00:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه:
«در نگاه رومیان، روم بی‌همتا و مرکز بلامنازع جهان بود. اما ایرانیان این تصور را در هم شکستند؛ زمانی که مارکوس یولیوس فیلیپوس (فیلیپ عرب) برای جنگ با ایران به شرق لشکر کشید، نبرد نه با پیروزی روم، بلکه با صلحی بر اساس شروط ساسانیان پایان یافت؛ تا جایی که امپراتور روم ناچار شد شرایط صلح با ایران را بپذیرد و در برابر آن تسلیم شود.»
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/75718" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVtpdDxlCQpWweaOeVc7OAaUKaULAKWoijAvkmdDyDhGTbML7_u1Qe4ivYsJ6oZkAkFacxNxRKbOSkk2Dejg4SYtjEpJdvz56O171zVQq1BA2DaMcIpUSHya-4rC5FcBqWjAU--1j-8eP5EWnzkchBsd7y0TtovXvP9yLM7XLfpx7-uLOWas0EyCz5r6VihVpykKbFpd2Dkited3H5YKcOL-nLLnjBXE0Q9Ei8jHSmXWZTnnKZmDjoPGivbuVeyy5ai8VQ98Fvvid3OcNFe5n4oCgFqch2FCXhZ8iRtT4qpcTQ2ThyTC9fnhK0q01pERmlKeJRXQ6yEyWunWG3z-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش اتریوم به خبر های مثبت مذاکرات
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/funhiphop/75714" target="_blank">📅 00:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قبل جنگ دوازده روزه قیمت تتر ریخت و بعدش زدن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/75713" target="_blank">📅 00:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">از من به شما یادگاری، هروقت دیدین یه جمهوری خواه آمریکایی داره از صلح و مذاکره صحبت میکنه، دقیقا همونجاست که مطمئن باشید قراره دیر یا زود عملیات نظامی رخ بده، و البته این عملیاتم فقط در راستای منافع خودشون و منافع آمریکا انجام میدن، نه کمک به کسی.  @FunHipHop…</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/75711" target="_blank">📅 00:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](ChamanDarKhak)</strong></div>
<div class="tg-text">از من به شما یادگاری، هروقت دیدین یه جمهوری خواه آمریکایی داره از صلح و مذاکره صحبت میکنه، دقیقا همونجاست که مطمئن باشید قراره دیر یا زود عملیات نظامی رخ بده، و البته این عملیاتم فقط در راستای منافع خودشون و منافع آمریکا انجام میدن، نه کمک به کسی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/75710" target="_blank">📅 00:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دفعه اول جمعه زدن دفعه دوم شنبه زدن  قطعا دفعه سوم یکشنبه(فردا) میزنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/75709" target="_blank">📅 00:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
ترامپ:  من در دفتر بیضی شکل کاخ سفید هستم، جایی که همین الان تماس تلفنی بسیار خوبی با محمد بن سلمان آل سعود، رئیس جمهور عربستان سعودی، محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست وزیر محمد بن عبدالرحمن بن جاسم…</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/75708" target="_blank">📅 00:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
ترامپ:
من در دفتر بیضی شکل کاخ سفید هستم، جایی که همین الان تماس تلفنی بسیار خوبی با محمد بن سلمان آل سعود، رئیس جمهور عربستان سعودی، محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الذوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رجب طیب اردوغان، رئیس جمهور ترکیه، عبدالفتاح السیسی، رئیس جمهور مصر، ملک عبدالله دوم، پادشاه اردن و ملک حمد بن عیسی آل خلیفه، پادشاه بحرین، در مورد جمهوری اسلامی ایران و همه موارد مربوط به یادداشت تفاهم مربوط به صلح داشتیم. توافقی تا حد زیادی مورد مذاکره قرار گرفته است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همانطور که ذکر شد، می‌باشد. جداگانه، من با بی‌بی نتانیاهو، نخست‌وزیر اسرائیل، تماس تلفنی داشتم که آن هم خیلی خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به زودی اعلام خواهد شد. علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/75707" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75706">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلام وحید
‏تعداد زیادی جت جنگنده با سرعت بالا از اسراییل بر خواستند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/75706" target="_blank">📅 23:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دفعه اول جمعه زدن دفعه دوم شنبه زدن  قطعا دفعه سوم یکشنبه(فردا) میزنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/funhiphop/75704" target="_blank">📅 23:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دفعه اول جمعه زدن
دفعه دوم شنبه زدن
قطعا دفعه سوم یکشنبه(فردا) میزنن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/75703" target="_blank">📅 23:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdHr5OxQ5Jd0w-otx4_WpU-GSJ5YMWCWs98gy462Ir2QANs9EudV8YXX09BN91tKOTb_Tnagez-vo7G1TuW_hhHr5QoUOwAseXGijgRdeJMNMFKkLfhV7sWuaLm5xIVfUNXutXfZNF1xKIIW5j2kUL5PKx9xQr2F2LrlPjItIbTeRhF2S1JCzlM6NOePYCdQHn3nW1IWtgrtI_hJVfWq1jRC-YvIE5AwBaSq1lzJ5Rw4dWXRoMm6kPapbHSYzQP2EneM8W4VwKovsSH9XjPxy91n22dBoQRx9FBT_l1Re0ts6gTzt1rbmbB2F-ABLP7jqmivP0toaOsoQlGeFpkUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه: تنها چندساعت تا نهایی شدن توافق میان ایران و آمریکا فاصله داریم.</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/75702" target="_blank">📅 22:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فاکس نیوز: هیچ توافق بین ایران و آمریکا صورت نگرفته است.
یک دیپلمات منطقه ای گفت تماس دونالد ترامپ با رهبران منطقه ای بسیار مثبت بوده است و رهبران منطقه ای از شتاب جدید گفت و گو ها استقبال کردند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/75701" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چه توافق بشه چه توافق نشه چه جنگ بشه چه جنگ نشه
ایرانی ساده فرقی به حال تو نمیکنه چون تو جفت حالتش برای اینکه نشون بدی زرنگی پامیشی میری باک 30 لیتریت رو پر میکنی برمیگردی خونه
دلار و تورم پایین نمیاد که هیچ چندبرابر هم میشه صدات رو هم نمیتونی در بیاری
جلوچشمات رانت خوری میکنن بازم کاری از دستت برنمیاد
پس توی هیچکدوم از این حالت ها اوضاع و احوال ایرانی تغییری نمیکنه
اینه سیاست آخوند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/75700" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیوزسیتی پرو: جلسه اضطراری امنیت ملی دولت ترامپ در اتاق جنگ کاخ سفید در حال برگزاری است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/75699" target="_blank">📅 22:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">48 ساله توافق نشده نکنه انتظار دارید توافق شه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/75698" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الحدث به نقل از منبع عالی‌رتبه: ظرف چندساعت آینده توافق میان ایران و آمریکا اعلام می‌شه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/funhiphop/75693" target="_blank">📅 21:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0l8iIQZ41Me8TBDXB4F6DsPIu3ZbqJJGLX7AVilQMjtuwcJLQbOuvBcI2QhikVxNYINwA9EreiYE3UlXzhiejgjd2zt89sbh_C2FHb3WDNcCu3Ir9nYa7mjUTh9YrSl66onHCmnn9d-1KK4zOoKE6mIp9hXvnOlYlc9FKWAJCdi4HFW136eht5DQEq8Z6EFa0aVGWRvKSjhbvXPl4sRwWwgcn7a7-oorl3MS1fYjPxGSbtZPbAO23vOleiiaNtErl_LZxIrNlstSfi4r4hPTW2jnqOgvSV2WGZjX_Fmcjytjilw6EypwTcia4I5FW_gwn9ytsHgRXUPOI2sDbw2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا: آمریکای خاورمیانه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/funhiphop/75692" target="_blank">📅 21:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نمودار محبوبیت ترامپ بشدت کاهشی گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/75691" target="_blank">📅 21:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مقام آمریکایی به آکسیوس:
توافق میان ایران و آمریکا برای پایان جنگ، نزدیک و در آستانهٔ نهایی شدنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75690" target="_blank">📅 21:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الحدث به نقل از منبع عالی‌رتبه: ظرف چندساعت آینده توافق میان ایران و آمریکا اعلام می‌شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/funhiphop/75689" target="_blank">📅 21:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/75687" target="_blank">📅 21:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6ptI0owxDU6F7HPDS0XkQKB_y_wnfxxiCaKYl-uKliOjkv2S_fyCG96n_C-tXcScH3-yrcdlqoAfqZxSAWQFtyQs94qeesIRp8a6jSgXpvC3f1agg1z3BuxTvlPkmOceGEXvs4_p52ldFu3z1l5eMtV_kkbw_pwcHILgH9IrPw5yv19HaGXL4elB6L0BTYIk_hF5M7jitlw-seChAAIIKl34P__InypYMy3tq7EVQcrIduBFKP_YloNZ1nfLP3j0o55rjIB990XzXX2vSX5wN8UyO5TiZpCvayoaPbjbZ7SIGZZp52p0Uvj62wtxXl7BcOc2fAU1dd0Acuo0id6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75686" target="_blank">📅 21:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله کنسله   منابع آگاه می‌گویند به ایران ۲۴ ساعت فرصت داده شده تا چارچوب توافق را برای ۳۰ روز مذاکرات بیشتر بپذیرد، در غیر این صورت حملات از سر گرفته خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/75684" target="_blank">📅 21:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حمله کنسله
منابع آگاه می‌گویند به ایران ۲۴ ساعت فرصت داده شده تا چارچوب توافق را برای ۳۰ روز مذاکرات بیشتر بپذیرد، در غیر این صورت حملات از سر گرفته خواهد شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/funhiphop/75683" target="_blank">📅 21:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لیندسی گراهام: تو منطقه بعضی از قدرت‌ها ترامپ رو تحت فشار میذارن که جنگ با ایران رو از سر بگیره (امارات و کویت و بحرین و عربستان احتمالا) و بعضیا اون رو تحت فشار گذاشتن تا توافق صلح فعلی رو قبول کنه (قطر و عمان و پاکستان).
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/75682" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نهادهای حکومتی در تهران در حال تخلیه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/75681" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: اگر برای اسرائیل خوب نبود، معامله‌ای انجام نمی‌دادم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/75680" target="_blank">📅 20:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آکسیوس: نتانیاهو از ترامپ خواسته دور جدیدی از حملات رو آغاز کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/funhiphop/75678" target="_blank">📅 20:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپو پوشش نمیدم من، خستم کرد</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/funhiphop/75677" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=gM5ahcQya38QsgpN_GXCK62BRpLADEzsmepbLXwMxKYWmqY5McUlD8ri-ZIO3mtCrnBxex9b7nARyq8Ui5ry2pw2s2KRakrxxERE4KUocL5MX0lMYU1LlTrZdwi9tV3LvadabCCnucM_UP7QHNnBUkekXqds_UgzXyN9OlEu26S_8_Fhso7fDfE-FccULUHEqgrjxC4JPpOYrUzuoZu_6lJxie-yNA2CHyrHwNq04X6Gb4ecicRGgCCAEX3CRvKDNNBUK8CyWwvf93H4bN3HcZkx4YKm8HuPBp1kK3ddYJ9Ly0NosnOwSixlhMq3bDvMPlO0hgR1BCyXunl0jLOVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=gM5ahcQya38QsgpN_GXCK62BRpLADEzsmepbLXwMxKYWmqY5McUlD8ri-ZIO3mtCrnBxex9b7nARyq8Ui5ry2pw2s2KRakrxxERE4KUocL5MX0lMYU1LlTrZdwi9tV3LvadabCCnucM_UP7QHNnBUkekXqds_UgzXyN9OlEu26S_8_Fhso7fDfE-FccULUHEqgrjxC4JPpOYrUzuoZu_6lJxie-yNA2CHyrHwNq04X6Gb4ecicRGgCCAEX3CRvKDNNBUK8CyWwvf93H4bN3HcZkx4YKm8HuPBp1kK3ddYJ9Ly0NosnOwSixlhMq3bDvMPlO0hgR1BCyXunl0jLOVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا من هزینه نمیکنم برم اینستا اینارو ببینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/75676" target="_blank">📅 19:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/funhiphop/75675" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqYyLYjln1XOqBu4UDdhD-fFN7ae-Oivfi71UTbNlghwv7Rl9oUuDSQDMYYlptAzYJ3bfNU3VGaHdQWbK6rsPyQ5ndOMcpWNiig-2XCjP2wmoW5pDZ47wkR9cv5Q8ReDDZWRLeeAhfL2bBNd6FRTe9zDc8t8c1QZ1IvfN4GgZ6o5SVfVW8cqZ53toINLADFTuphQ_0QIuth9_lsW2EbzKAny25VSu1UxFIZSEJ-Hv5rdLIzaJDmABMFU8x9fwOuu84kSxpR4_crSFYmP3aWGVYrAGsA9dAxoMQoaidFBszWMADJ1juXV2GJFVCmI4oa_tJTvn5ZEDHLtYF5EKVMmug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/funhiphop/75674" target="_blank">📅 19:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرنگار اکسیوس در توییتر: ترامپ میگوید پیش نویس جدید توافق با ایران را با مشاورانش بررسی میکند و احتمالا تصمیم نهایی را روز یکشنبه میگیرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/75673" target="_blank">📅 19:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیویورک تایمز: فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند. این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75672" target="_blank">📅 19:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75671">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فایننشال تایمز:
میانجی‌ها معتقدند که آمریکا و ایران به تمدید آتش‌بس به مدت ۶۰ روز و فراهم کردن زمینه برای مذاکرات هسته‌ای نزدیک شده‌اند.
توافق پیشنهادی شامل بازگشایی تدریجی تنگه هرمز، بحث درباره رقیق‌سازی یا تحویل ذخیره اورانیوم غنی‌شده بسیار ایران، و تسهیل محاصره آمریکا بر بنادر ایران، همراه با رفع تحریم‌ها و آزادسازی مرحله‌ای دارایی‌های خارجی تهران است.
یک مانع بزرگ همچنان درخواست رئیس‌جمهور ترامپ است که ایران ذخیره ۴۴۰ کیلوگرمی اورانیوم نزدیک به درجه تسلیحاتی خود را تحویل دهد و سه سایت اصلی هسته‌ای خود – نطنز، فردو و اصفهان – را از کار بیندازد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/funhiphop/75671" target="_blank">📅 18:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">من خودم بتمنم ولی الان بحث، بحث وطنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/75670" target="_blank">📅 17:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNkkezGj_0oNQBB8bdSIRB3hbXlfGdIOD18j47eM4G_OJDH2gaM05l4v3vZbO_8VwFZ50pTukuDLiaxU7bkmsX6imwAcHS076vJzRcs--BgJH0uSOmwo5Ryw9Tv4TUcF9C1_GSM9nFZhyUk1zNIVbZqM1FDgvh5XoYk40jyNFjxuSbJ3c4qPDgWb752_bYo-scrVeUMRJx2QhZDsQ9haDilmK8-q6CxwMdBGSKk85UzEmrnE78rtBe5FPNh0lRLMN3QR7rVio1Yu4MOKaR1pSvEe6dwQOyObasyLLDOmfGv76e1lkIG17BzJ345oC_1MTcynw8fTECCs3J-D8FWrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور پررنگ بتمن در تجمع اعتراضی دانش‌ آموزان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/75669" target="_blank">📅 17:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آخرین باری که اتابکی گفت میزنن ۸ روز بعدش زدن امیدوار شو ایرانی   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75668" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75667">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75667" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک مقام ایرانی به الجزیره:
ما به یک تفاهم‌نامه با میانجی پاکستانی دست یافته‌ایم و در انتظار پاسخ آمریکایی‌ها هستیم.
تفاهم‌نامه شامل پایان جنگ، رفع محاصره، باز کردن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود زیرا این مسائل پیچیده‌اند و نیاز به زمان کافی برای مذاکره دارند.
پس از ۳۰ روز از امضای تفاهم‌نامه، ممکن است درِ مذاکرات هسته‌ای باز شود.
قرار بود رئیس ارتش پاکستان [عاصم منیر] تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی به واشنگتن رفت.
برای ایران امکان دادن امتیازات بیشتر از آنچه در تفاهم‌نامه آمده، وجود ندارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/75666" target="_blank">📅 17:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا: آمریکای خاورمیانه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/75665" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHRiWOEis6vuvDiooWzMz_MbDLnDoYP5x4MxtJtILenuup8yhjwAEoqVm8Us3qBHyA6DUC-971Nvs_T_alKVsFwivU10evV8Y1JoTcE_qg76mzU4zyb6E44sxQhVkUTg0seW4CJChiacbipEJ-HqlhbjDbd2Fbbnk98PjxOF0EnqnIBSAX0I029SKjrlLyo614XyMHsKdU0W07a-xgaC8kn9tpl_Be9ZthS1OgpaC5OfUQo1UBkzJVm4xOrYe9Fk-iO5ES--prLjyDpAm9xu9mye2Iek_wI-zPqCbpEeTFsVLj82gYOBNuMJMWySInS1VAImBNeKOYNn9Wh8mS-RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا:
آمریکای خاورمیانه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75664" target="_blank">📅 16:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b026396695.mp4?token=ebvKaAaOhWck23mSqDuzURLClMWNII80WILg3uMTNZIOU7UM18airn_StG98n1P2JrSTWOor5CFEoK8qRiRfo8nhtZLZ25WxVxE13hj1mczAJ3Q8p36m8VceaI3zQlRJjPgWg1MnujRF3ioithfnkkeeL7KsqzqQP2hWsRF3dGPnUK9t7VUAiJfOzezXXTBWA6Kx4ScSHf7kWWGwBzOy2y3kvdIRdYYRhy5LlGzXaJXNKMrG1ktXeppPTpJUNZMuGEyNAg4z5J3ZTfEvkNgsmGcmYvR3Z1gNsYBfbFBMjCprCtjdGJcnRZd-YkUTv5tvZoOqzVZER2szvBt_g7Xtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b026396695.mp4?token=ebvKaAaOhWck23mSqDuzURLClMWNII80WILg3uMTNZIOU7UM18airn_StG98n1P2JrSTWOor5CFEoK8qRiRfo8nhtZLZ25WxVxE13hj1mczAJ3Q8p36m8VceaI3zQlRJjPgWg1MnujRF3ioithfnkkeeL7KsqzqQP2hWsRF3dGPnUK9t7VUAiJfOzezXXTBWA6Kx4ScSHf7kWWGwBzOy2y3kvdIRdYYRhy5LlGzXaJXNKMrG1ktXeppPTpJUNZMuGEyNAg4z5J3ZTfEvkNgsmGcmYvR3Z1gNsYBfbFBMjCprCtjdGJcnRZd-YkUTv5tvZoOqzVZER2szvBt_g7Xtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75663" target="_blank">📅 16:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75662" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75661">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیدار عاصم منیر با پزشکیبان و قالیباف در تهران   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75661" target="_blank">📅 16:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cr_9T3nBxzHqK6GKIJG-sfUMKsI9OTwJJURct3C7TVEXe8-MoMf4hiAALuTHErueRDT7es8uxkw0Sso-GoKKlaSXVN_djaVivQqkU5Q5qz2Y0PAJCv6wF6XZkTJuGqxYBPfrNs0dzlJ30OMEbd_iLv79oIp_SbdFsj-ZaF-sAuTG4haLsxEoiY8QvVD5T9qmaeKUbmixCIcH440bfAG9G2Gc8Gg1CBKa7CLCxvOa92w5soOQ2Bft4IrboK_JFVae0NQSzk9xfyOoKSVpF4dPR6IjL8S8b-BP0MuAMBCkY3vQwuIPR-3osT_g-Mw30hNSVBSSc3u-dGKoSOv6jIVwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا واقعا</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/funhiphop/75660" target="_blank">📅 15:05 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
