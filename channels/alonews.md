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
<img src="https://cdn4.telesco.pe/file/Gua1mKPH5OSODsMiHvsoFP0zw1nJMdPLEynKog5l_ObSE3nF65ZAVOo0nrExm5-3x6U8beYQZU2JD_LhaKypWL_UvRjHlUVckEHi9phJ-4c9xNnkWoQmNXxnI6H_ahcm0P_RbxCjJ1PjiXlrnXxvo0Qud4e86PLMWO7xFQfeyXDwJzwALoL5Jn0eZTMc9OI7UYvpBO7U5UjwBV7m3USngpJ0xkig6N1vgsuGFe76Jq9KyLwogxYuOz5K_1cLCGLQKhIxyUk_bG2AEhWLQMUAAZqnk630jdh7PWgR3HgnNqzj-vPvKtf2SarnyDkmfw0xuQ1DZHE8hM4H8m3REbnd_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 945K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-145536">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37707ac0d.mp4?token=Sxjv67lVca594k5qozY4ZpkgZkZRsbKOFfrNF-jklH2BbxGA_tKyPQQUN6XBxr0CeJ61cxueeLzNrQQiGAsSv8N2tFkDXShHIoxh9-5671_rwOGoFUa8qOSZV4gx0PXJxVV-2kp7eq7EbljJjhJymHY9w-DO27IKm4WDXj9i2ZCREeUOX0CYGO7kUK7aYLiixLSG8StD81xa_FmuKCiVC2MDxjf936rKoYwUTJAtakj74QgqXUs-26b9uEKyY2yIZ31fYsUhuW4spRK7cXv6kJ1UGxxzrh9sfotShXyAS25HezAQusYMnMA6AIMcts5XNjQZA8T5S_zoOaEf55cekA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37707ac0d.mp4?token=Sxjv67lVca594k5qozY4ZpkgZkZRsbKOFfrNF-jklH2BbxGA_tKyPQQUN6XBxr0CeJ61cxueeLzNrQQiGAsSv8N2tFkDXShHIoxh9-5671_rwOGoFUa8qOSZV4gx0PXJxVV-2kp7eq7EbljJjhJymHY9w-DO27IKm4WDXj9i2ZCREeUOX0CYGO7kUK7aYLiixLSG8StD81xa_FmuKCiVC2MDxjf936rKoYwUTJAtakj74QgqXUs-26b9uEKyY2yIZ31fYsUhuW4spRK7cXv6kJ1UGxxzrh9sfotShXyAS25HezAQusYMnMA6AIMcts5XNjQZA8T5S_zoOaEf55cekA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو ویدیویی با هوش مصنوعی منتشر کرده که در آن شهردار نیویورک، زوران مامدانی، رئیس‌جمهور ترکیه، اردوغان، مجتبی خامنه‌ای از ایران و رئیس‌جمهور فلسطین، محمود عباس، در یک تماس گروهی حضور دارند و درباره اینکه چقدر می‌خواهند نتانیاهو شکست بخورد صحبت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/alonews/145536" target="_blank">📅 12:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145535">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی ارتش: دشمن بازم تو دستیابی به اهداف خودش در حمله به ایران ناکام موند
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/145535" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145534">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت اخرونوت : اسرائیل درباره ایران آمادگی ویژه‌ای انجام نداده؛ وزیر جنگ اسرائیل با اظهارات خود قصد دارد توجه‌ها را جلب کرده و در صدر اخبار قرار بگیرد. ایران منافع واقعی در وارد کردن اسرائیل به جنگ ندارد و ترامپ نیز نمی‌خواهد اسرائیل وارد درگیری شود. برآورد ارتش اسرائیل این است که ایران قصد عملی برای اقدام ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/145534" target="_blank">📅 12:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145533">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فایننشال‌تایمز تایمز از تلاش میانجیگران عمانی و قطری برای تدوین چارچوبی جدید برای مذاکرات میان ایران و امریکا با هدف مدیریت بحران میان دو کشور خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/145533" target="_blank">📅 12:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145532">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJAS_rb4ydb_8I5uSZSruUpmPzcrKBtlNYp9xbD40Go0JNHtnMSmPEi5CmFkDOsGduUxAKLwACSbLciuWQ72GFrPwsJzwOO--qmYk83GLtPO9QnALKYOc66ULIdAiAS49SMTWPsIvooCovo7yrfrvbjW3CoMfHtn5j9Po7P8G0rFWXzF90w_-3nTfOYc4xuza_NdrXKPG63mNiklSYjAXidQU1Id--PowCw5_aiOORB9K1SObcE5sciHlchw0jljzQaqK7TaxI-ckcVXax1AzKq6Q7hqJrp5wZvJXS9kRCrn1ZhjjWyyTAJMVFp7efHp2T2xdjNUPkVzfwODiVXmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : به نظر وزیر خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔴
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته‌شدن ایرانیان بی‌گناه انجامید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/145532" target="_blank">📅 11:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145531">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvMcT3OYN-R2U9juM-iJwHRUqj7Rjlib134uoIszKCAjfZ8fhEUp1HNk1KhNNv2PLxLKOmOUoeNYAMoLIJhVcQ06ueTKq2A6-tT74o06FCzODG4_8u8a9N3oiNfW4RbF1k-y_P4MnNqb-ieCTN4R9dHWqNat6UOEziBrQtFDmUPri8P7SRT2f_r0KjadD24u4fRG-Tf7K90pS8XfQz0Lf1AtuXrpf6iGQMsyxlaxOFq_7VULXwqVzK3B6-uDCZ7y0LnbzzsG08qFdJkP7Pf5l9iMc9DtIUmC7igKsJQQi5uaq3xrQ6o4pUeLVsiHiB01Ot_-JAkkV7QDgv5-AjhNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دستیار قالیباف: اصحاب ناراه‌حل برای فرار از پاسخگویی به تفاهمنامه حمله می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145531" target="_blank">📅 11:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145530">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مسکو: یک کشتی حامل تسلیحات غربی، یک تأسیسات انتقال سوخت در بندر چورنومورسک و یک کشتی در بندر یوژنی اوکراین را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/145530" target="_blank">📅 11:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پنتاگون: حملات ایران ادامه دارد، اما «خشم حماسی» به پایان رسیده است
🔴
یک ایمیل نیروی هوایی در ماه آگوست به پرسنل دستور داد که از به کار بردن عبارت «عملیات خشم حماسی» برای توصیف فعالیت‌های نظامی جاری آمریکا علیه ایران خودداری کنند. این موضوع سوالاتی را درباره این که واشنگتن چگونه به طور رسمی این عملیات مداوم را طبقه‌بندی می‌کند، ایجاد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/145529" target="_blank">📅 11:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu58nsII2V_Iget6JhHYrPnu3FbEZCSermBIuR68p4_8_uj77tEKqdSb-pd1LbVzHtakCJi4ImS-rlyMMWShAa8_UYL2K4GDvP0Rr87Bfb9L7I1NlZ640hS0q6OeyyKU3Mx6_vWi6fqx4cdP1kojfGZ64NLzT3ML4l8JO7eiCCYy89qeA1ExxLwvtz7ACSkG7P4fnVgh2Cuzl7n1S1pP1exL5Q2CXkWpwc344zcfjgQt9F_e9aqCj5kXZjJ-xRuvsRoUYjNn1fFqGHVGBzqr0cyM4ViKVikPS0VsJN72CyDR489n5O4FD_tEIGZSQX69lDE5_t2Fd64ahqsPLY8t4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت در آستانه 96 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/145528" target="_blank">📅 11:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خاویر میلی: جزایر فالکلند متعلق به آرژانتین است
🔴
اجازه دادن به اجرای پروژه نفتی، انگیزه‌ای برای دولت بریتانیا جهت تعمیق اشغال این جزایر ایجاد خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/145527" target="_blank">📅 11:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145526">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
صندوق بین‌المللی پول: اقتصاد امارات وارد مرحله خطر و کسری تجاری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/145526" target="_blank">📅 11:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/الجزیره به نقل از وزیر دفاع اسرائیل: کنترل ارتفاعات علی‌الطاهر به معنای تکمیل نهایی منطقه امنیتی در جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145525" target="_blank">📅 11:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: مدارس حتی در شدیدترین شرایط حضوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/145524" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145523">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مرز، صدراعظم آلمان: ما با یک اختلاف تجاری با آمریکایی‌ها و عدم تعادل‌های قابل توجهی با جمهوری خلق چین مواجه هستیم.
🔴
اگر می‌خواهیم پای خودمان بایستیم، از جمله از نظر فناوری، تنها یک راه وجود دارد: با هم در اروپا و با مدرن‌ترین فناوری‌ها.
🔴
هر کس که مانند حزب AfD بخواهد از بازار واحد خارج شود، از شنگن خارج شود و از اتحادیه اروپا خارج شود، در اصل پروژه‌هایی مانند آنچه اینجا در حال ساخت است را زیر سؤال می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/145523" target="_blank">📅 11:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145522">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=NJZnvI33K_DiNSdLog5JX1wDftoKwIu_gXo_gDdKJlF9_MBq0fPKtSJW_h3fnp3tDhTxz7U7QvgWiZ5LHwiE67e8qvlDzX_4Ot5EOt-Onq3hYEzgHJGg6lsuLBNszqMavpQl5Yw7gqtsRqbbrYIDE5PIeSYKkbsexNI4XSuM8M9RBzpMDbaqu_RwSPGusRnmNqLbUtrA7nq_8QYCc7_GO5lcsyRMIQjZ_ZgCgkyYCSluzNXGP0eFcPTnuo0P3pIyeFMMI7y_RbB0MBLZ8jLOeDQbhZZf-1zG1ovmB4hL5J98HDuBWmKuMoDP4yt0BT0uQwqiMJ1VfRegwr92uZLUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=NJZnvI33K_DiNSdLog5JX1wDftoKwIu_gXo_gDdKJlF9_MBq0fPKtSJW_h3fnp3tDhTxz7U7QvgWiZ5LHwiE67e8qvlDzX_4Ot5EOt-Onq3hYEzgHJGg6lsuLBNszqMavpQl5Yw7gqtsRqbbrYIDE5PIeSYKkbsexNI4XSuM8M9RBzpMDbaqu_RwSPGusRnmNqLbUtrA7nq_8QYCc7_GO5lcsyRMIQjZ_ZgCgkyYCSluzNXGP0eFcPTnuo0P3pIyeFMMI7y_RbB0MBLZ8jLOeDQbhZZf-1zG1ovmB4hL5J98HDuBWmKuMoDP4yt0BT0uQwqiMJ1VfRegwr92uZLUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 23,700,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145522" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145521">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
منابع خبری گزارش دادند که بر اثر سقوط یک فروند هواپیمای کوچک در منطقه «هیلزبورو» در ایالت فلوریدای آمریکا، دو نفر جان خود را از دست داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145521" target="_blank">📅 10:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مسکو: همکاری با ما به پکن کمک کرد از بحران انرژی ناشی از بسته شدن هرمز عبور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/145520" target="_blank">📅 10:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
حادثه امنیتی در دریای سیاه
‏
🔴
وزارت دفاع روسیه اعلام کرد که یک کشتی باری را در دریای سیاه هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145519" target="_blank">📅 10:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کارشناس صداسیما: درسته حزب الله شکست خورد و اسرائیل خیلی از مناطق رو اشغال کرده اما حزب الله در اصل پیروز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145518" target="_blank">📅 10:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم‌الانبیا: به‌زودی دشمن رو در میدان غافلگیر میکنیم.
🔴
رفتارهایی با دشمن خواهیم داشت که کاملا گیج، مبهوت و شگفت‌زده خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/145517" target="_blank">📅 10:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145516">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پوتین: روسیه در رتبه نخست تأمین نفت و گاز چین قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/145516" target="_blank">📅 10:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145515">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d55fc1fc.mp4?token=s1-B1hAUyP3I6ZgJHIwzG8s2NqXPrzBu2W99dQ9VGl5Nu1cK0_x5mP-bP_P_XanSbOayjvUdW7UcD23ATDgISS2WMFtuzvl2XPh1I96D4U-AdPER-KBMVzG2J41TEycgivemhdCecg6l-9AqVBkhky4tCQyePtuSx5Fy9KizcimN2GnPzpv8Bf4P6DxMajYALXj8LZ0cyxGOGLoBpl_W3SMezUBdRfgdTRr_tbbhg1dnTupHulP0cNJjKDtDlsqHgsCfHAy1YQZp5hfwl1wVQiB-hYO5EBDvAPltUA2DUNydtoieSgo2RcK_4-T0qZhf4zbLFcGthHgzCL6GnRPXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d55fc1fc.mp4?token=s1-B1hAUyP3I6ZgJHIwzG8s2NqXPrzBu2W99dQ9VGl5Nu1cK0_x5mP-bP_P_XanSbOayjvUdW7UcD23ATDgISS2WMFtuzvl2XPh1I96D4U-AdPER-KBMVzG2J41TEycgivemhdCecg6l-9AqVBkhky4tCQyePtuSx5Fy9KizcimN2GnPzpv8Bf4P6DxMajYALXj8LZ0cyxGOGLoBpl_W3SMezUBdRfgdTRr_tbbhg1dnTupHulP0cNJjKDtDlsqHgsCfHAy1YQZp5hfwl1wVQiB-hYO5EBDvAPltUA2DUNydtoieSgo2RcK_4-T0qZhf4zbLFcGthHgzCL6GnRPXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم زیر فشار اقتصادی اما زن سوم عراقچی و سایر دیپلمات‌ها در به در دنبال خرید طلای لوکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145515" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145514">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK0VAY99hUliGE2xTqYcudPw4UafXS9IwtKj31aAjxwpUkyuxmoDn5O-aFKLptkF2hlgrEwa5QSVq44wW5ZxoBDVMAuKPUe_QEfKQHt9ffvNUIMRYqCGaBUs86KSYB6_gfyOaPo5h3DyYrWbJlLhgBNhV970mBzij79c6kGCeMvUAzpDFhDf9V2PXvJ0Ut9MqlPdXjTbDfSZapRamM0CIE9dUXnuHP2fVD_YIs21ZWeQ5EiQqUIDZvFl8B1GcZJMtWI0E64UT2aZ3EH_ptwalgDE1mRxinupPricG8Y92k3R2H1TNGXHRIlwaZupybKgWue048Ue1ZavIscjpnR6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه فاکس نیوز اعلام کرد که این احتمال وجود دارد که جنگ ایران تا سال آینده (۲۰۲۷ میلادی) ادامه یابد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145514" target="_blank">📅 10:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145513">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnG0DvfnLHV_I7-eAAOZU-kkSFd1e9nfFnC1tF6hIUhNZW8EGptpU0Q4ugFmK1wSGWTK65VQgrwO769kryh0wNDdQrCAtY-ub9zyRBWmeHfvgnntgumvQLqrQyfwbs7k-wBoBmKXDliSCbnBwnSaC_ReU_oBo3szY1nxvBHBOrFoVwxhAUecelU_it2jQ2T3366DkcDdkR1v2qWu2heDMT5PXslVqn3z0TQfh3SnTDY6V4GRWUgwdkO3BZ34tv3MiKgzHnKU4GbEOb3_RjXd8BXxIjVtgQLQEoQka8SlXG3fdYyEMyrOivx0jJlaVUvvx53Sdtt0-JwDp1XIChENgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور اقتصادی قالیباف طی توییتی درخواست افزایش نرخ بنزین را کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145513" target="_blank">📅 10:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd9d65c4d.mp4?token=iYV2nk_Ym2pYhjFJTsj4yc4cJrb2IIe7KHYFWz1bwq1gxvEaEcTlkNO04yuimTO4qKnWS8m93Y-3iW7xwmhT2Ql47qeX_kF1oX4Hzw_BlQ-dpEj5HXs7pu5vBMVnZf7xu8rWoOa0pzNdgl3uUPT-2kxkeapMwNCgPzIx9wSdOoHT-P5X8Y8apbZWvQtK1D8IH4EVEZKkvxjLS1_G1O2b2PJ_2wQD9F3fyVDQLBCbLfgtqYA9gQg1n6DFpb0CaUpV4muW-beKiTcHfO-cl1_TSDNDl1scZ_snqZ1NsQclZGlCJW-v53uCRzDpbFaqUQ3EIkVcUxktm_O6h5ro4ps4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd9d65c4d.mp4?token=iYV2nk_Ym2pYhjFJTsj4yc4cJrb2IIe7KHYFWz1bwq1gxvEaEcTlkNO04yuimTO4qKnWS8m93Y-3iW7xwmhT2Ql47qeX_kF1oX4Hzw_BlQ-dpEj5HXs7pu5vBMVnZf7xu8rWoOa0pzNdgl3uUPT-2kxkeapMwNCgPzIx9wSdOoHT-P5X8Y8apbZWvQtK1D8IH4EVEZKkvxjLS1_G1O2b2PJ_2wQD9F3fyVDQLBCbLfgtqYA9gQg1n6DFpb0CaUpV4muW-beKiTcHfO-cl1_TSDNDl1scZ_snqZ1NsQclZGlCJW-v53uCRzDpbFaqUQ3EIkVcUxktm_O6h5ro4ps4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل عملیات جستجو و تیراندازی توپخانه‌ای مداوم در حومه زوطر شرقی به سمت مایفدون در جنوب لبنان را انجام می‌دهد.
🔴
شلیک مداوم توپخانه منجر به آتش‌سوزی در مناطق هدف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145511" target="_blank">📅 10:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b608c09a87.mp4?token=bNDVSDtBDSqYNFp2ZlTGTfQgjG-Bkw4WxBrxYr4gZeNtoYEllwhw3RLzWbqAVEKhzx-zXp8PFxWZ2Mz__XPmkF8MyQZ0Np65JtuSkDI-h0XVKTlSVjDKkT-QY4E9VQWyVJrQdh7i5IUWutDl-xyJJ8QJGB3e6Tqe4XDH67VIfhJOtD-YAjuC5xz7BIpiB7z-UhvyL5QMlEpppgNhmHSrthOxphcg8XMa3sI4kWalhxNabMg2Mg4pepO5aKuIVoQEfErSQnvT0JNV0P0OSi3WdlD5bKOFU0RPPvIwbUG1SfNq3IxkBJ56towO1d9C-22zRLlEm_kRN4r4pdOaTCNfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b608c09a87.mp4?token=bNDVSDtBDSqYNFp2ZlTGTfQgjG-Bkw4WxBrxYr4gZeNtoYEllwhw3RLzWbqAVEKhzx-zXp8PFxWZ2Mz__XPmkF8MyQZ0Np65JtuSkDI-h0XVKTlSVjDKkT-QY4E9VQWyVJrQdh7i5IUWutDl-xyJJ8QJGB3e6Tqe4XDH67VIfhJOtD-YAjuC5xz7BIpiB7z-UhvyL5QMlEpppgNhmHSrthOxphcg8XMa3sI4kWalhxNabMg2Mg4pepO5aKuIVoQEfErSQnvT0JNV0P0OSi3WdlD5bKOFU0RPPvIwbUG1SfNq3IxkBJ56towO1d9C-22zRLlEm_kRN4r4pdOaTCNfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل به زوطر شرقی در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/145509" target="_blank">📅 10:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کره جنوبی: تصمیمی برای اعزام نیرو به هرمز گرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145508" target="_blank">📅 10:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
یدیعوت آحرونوت به نقل از یک منبع مطلع: اسرائیل درباره ایران آمادگی ویژه‌ای انجام نداده؛ وزیر جنگ اسرائیل با اظهارات خود قصد دارد توجه‌ها را جلب کرده و در صدر اخبار قرار بگیرد
🔴
تهران منافع واقعی در وارد کردن اسرائیل به جنگ ندارد و ترامپ نیز نمی‌خواهد اسرائیل وارد درگیری شود
🔴
برآورد ارتش اسرائیل این است که ایران قصد عملی برای اقدام ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145507" target="_blank">📅 09:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از منابع دیپلماتیک:
میانجی‌ها در حال تلاش برای تدوین چارچوبی برای مذاکرات میان تهران و واشنگتن درباره یک توافق جدید احتمالی هستند
🔴
دولت ترامپ به دنبال توافقی جامع‌تر با ایران است که موضوع تنگه هرمز و پرونده هسته‌ای را نیز دربر بگیرد
🔴
واشنگتن به میانجی‌ها اعلام کرده که خواهان باز ماندن تنگه هرمز، صرف‌نظر از توافق احتمالی میان تهران و مسقط است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145506" target="_blank">📅 09:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f448c460a3.mp4?token=ENNvVjYss6KZEy2Vd4f8YtjkoCHx6Ql4xrk146uZMIsF2SJnr1KLaEtofEvRZFKL5dVv6-OA7qQqdN_JWB2ledKR-VqIhRbXFPNPg--LIOCE5SIZCdb11K4aZKlxaC9JzAoKAuzG2ldHDuzRok2pK0NCuTUvoJUJJ8Ah-zGpb3zg0IwGyKDsV92gsLaGT9x_KVZdpKJXABuLaJc-ZhKTAs3DVWSatsEGcfkCMOJlE24km2trPMTmLeseYLwP_mAqb2rMtmpdovN8XYvqoopO5KkPyMHYYoOKo9kqvEsYH-Fx9qRz9iZzXsWCZn_e28IlpI8JMBTEO3Z9n55dnBOPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f448c460a3.mp4?token=ENNvVjYss6KZEy2Vd4f8YtjkoCHx6Ql4xrk146uZMIsF2SJnr1KLaEtofEvRZFKL5dVv6-OA7qQqdN_JWB2ledKR-VqIhRbXFPNPg--LIOCE5SIZCdb11K4aZKlxaC9JzAoKAuzG2ldHDuzRok2pK0NCuTUvoJUJJ8Ah-zGpb3zg0IwGyKDsV92gsLaGT9x_KVZdpKJXABuLaJc-ZhKTAs3DVWSatsEGcfkCMOJlE24km2trPMTmLeseYLwP_mAqb2rMtmpdovN8XYvqoopO5KkPyMHYYoOKo9kqvEsYH-Fx9qRz9iZzXsWCZn_e28IlpI8JMBTEO3Z9n55dnBOPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی نیروهای روسیه به یک مجتمع انبار در روستای پوغربی در منطقه بروواریِ استان کی‌یف، باعث انفجاری شدید و آتش‌سوزی گسترده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/145505" target="_blank">📅 09:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
هواشناسی: سامانه بارشی یکشنبه وارد کشور می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145504" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145503">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید مقامات لبنانی نرسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145503" target="_blank">📅 09:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN9Qbq45g_pp9HlE0jZ7umIxL-sDARRIRgAEgNNIdzuo5zsSgKgL0cxgx8bSwK1L7ah-Z8HKD43omIDLL_8HZGKRNqvkzyj2I2Pfr1bH1MvO0oSDidMNv0eUstyFuQcJWO7o71gVLFL7gcyZgOe4I-aBjUoycYBPHfFTE42I7A3cI3A596dSvYln4movQptGHVijFP-4jV1NYzeD7eWfwX7ZTQ3BQ6D34LhLkWgi436zvpvwftmQ2b77OBcEC3MXIly9-wFZJcUgvscGVktC7orH-OZ357e9HMlCHcb2oVhS2t682b9o-lDjzY2xeuf44RBaT918SpxN6m7hlxVLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: آمریکا در حال بررسی حمله‌ای در ایران است که ممکن است به یک مراسم عروسی اصابت کرده باشد
🔴
مقام‌های آمریکایی می‌گویند این حادثه در دست بررسی است، اما ارتش آمریکا هنوز تأیید نکرده که این حمله توسط نیروهای آمریکایی انجام شده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/145502" target="_blank">📅 09:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده: اتحادیه اروپا رسماً به تحریم‌های اقتصادی علیه ایران پیوست و ما از این موضع قاطع و به‌موقع او قدردانی می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/145501" target="_blank">📅 09:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ونس: احتمالا به شکل مخفیانه عملیات‌های خرابکارانه در ایران انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/145500" target="_blank">📅 09:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
الحدث: تنها ۴ نفتکش روز پنجشنبه از تنگه هرمز عبور کردند.
🔴
داده‌های کشتیرانی از کاهش مستمر تردد نفتکش‌ها در هرمز طی ۱۰ روز گذشته خبر می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/145499" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145497">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqyKDDJLDquFZLjEEzl_AkmMmmR6pyimD-H7PXF_RQnWtLDjPhPsR6dKb8fkxWXFgpfg3ZgU5byTkDMdrqUvZBfO-j6KDaI0TRH-8y8UkFvb-xDKfHtAu_it49s_hwEeEhHT9NHZtKBV5dFduHGUQyAaCgOQgbMIITnognFGGxjhSzCtB6qaZGHqBaD1cDZTF93XtYj9eR493RTSaIMvheBnrf265puqSN1Bv9VmYvQlSPs1foJKpdpuGHoYwXf08jhbX3ycSAVs3V3C3SyE1PmnRktBnv2UJrhqy0vX25uuwfBG5Qk5Y494RLxydtjED6dxnMbLNO-eK-KKdcU8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق جدیدترین تحقیقات نسل Z (متولدین دهه ۷۰ و ۸۰) تنهاترین نسل ایران هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/145497" target="_blank">📅 08:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145496">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
پاکسازی شهر موشکی حرب الله . خنثی سازی تمامی عملیات های الکترونیک و سایبری توسط ارتش دفاعی اسراییل در رشته کوه علی طاهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/145496" target="_blank">📅 02:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145495">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3cfabd42.mp4?token=NPGe19OTyoiR4Uxmxu0rwmD_WRiRUTEL3OijH8Y6d8X9AJAHM84rnyA8ZnVdsTIWSzSDT6fQ6TMbc1a1WwV7OSlcwzNOMfHVFa4vBQQPrDmlDEXiIOpuozKq-mdRN0XCPSRHKZ23Sw3WK3XT9_s3iqTJ7Aa_Kly9fvBT12-qlywjGFZKQCuS8YkeJV5OFxWaDV6sCJBIVFc1QjnBCTTBhRNJtoFnEvMP97VDyAVQE1k2H04ST2fi5xAlFleec2oU3jSdjCpzx8jpHSy9UYblyhzWQEXQW-UaYyJEmyqYBuvRyvR_T6oYDe-1PkzMk1hfZSS-8pVfFGdcemMBbXcOgA-Vj0UcWEN2BAl9RKaLEEBGVajg-qnq_d09hcm9ZCLLCsp_BZSI3hcvJ2mSZKZ65b0iFkTuUX9l6jNxRTqE-1KyxJunushGhD6MucFZ3IBOpee8FoscDgyUW_LhrZgp3NPaLc0djj8ZdG9lkn3keCQXDiV63Ntfq_-zwOLTATDIDoaKM1SijbLR3BnvMUapEDXVl4QdSLETxGknTj24fQmuWPIu18t_PoDJrj07-tcQGZoK_NfttFq6Lzp_jJUHPjXz2-w5Qe74BNAZLdnZCTs8s4OYBrfsDlKZfwsSINW9DRl9V3QfCjsMAj1L_S05wR8wk06VIjkwWDXqFo8WvgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3cfabd42.mp4?token=NPGe19OTyoiR4Uxmxu0rwmD_WRiRUTEL3OijH8Y6d8X9AJAHM84rnyA8ZnVdsTIWSzSDT6fQ6TMbc1a1WwV7OSlcwzNOMfHVFa4vBQQPrDmlDEXiIOpuozKq-mdRN0XCPSRHKZ23Sw3WK3XT9_s3iqTJ7Aa_Kly9fvBT12-qlywjGFZKQCuS8YkeJV5OFxWaDV6sCJBIVFc1QjnBCTTBhRNJtoFnEvMP97VDyAVQE1k2H04ST2fi5xAlFleec2oU3jSdjCpzx8jpHSy9UYblyhzWQEXQW-UaYyJEmyqYBuvRyvR_T6oYDe-1PkzMk1hfZSS-8pVfFGdcemMBbXcOgA-Vj0UcWEN2BAl9RKaLEEBGVajg-qnq_d09hcm9ZCLLCsp_BZSI3hcvJ2mSZKZ65b0iFkTuUX9l6jNxRTqE-1KyxJunushGhD6MucFZ3IBOpee8FoscDgyUW_LhrZgp3NPaLc0djj8ZdG9lkn3keCQXDiV63Ntfq_-zwOLTATDIDoaKM1SijbLR3BnvMUapEDXVl4QdSLETxGknTj24fQmuWPIu18t_PoDJrj07-tcQGZoK_NfttFq6Lzp_jJUHPjXz2-w5Qe74BNAZLdnZCTs8s4OYBrfsDlKZfwsSINW9DRl9V3QfCjsMAj1L_S05wR8wk06VIjkwWDXqFo8WvgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکسازی شهر موشکی حرب الله . خنثی سازی تمامی عملیات های الکترونیک و سایبری توسط ارتش دفاعی اسراییل در رشته کوه علی طاهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/145495" target="_blank">📅 02:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145494">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUPpmwJsteVggI7jJiEC1832-oem7VZReZHKt_DRp35TEBMJvzLX3ADl39GkK0MD40u5vy1XPA4_uuYunI70hOVg3EwSIc_TLt6ByXUm0o7T68poHc9H5Bbj2PsKYc03hDMKvoxm-F6rJRGh6GqGJ53HtK0xhs0sD2K6AY8bAFwUmEJIbOBA4dalAzLELKJC1RppxS_Lb_7SL5xug9OgUNOhZqqOFlDHm_Zr5Hu3DgowRYn1rwzPcGsRGQbq_moQugDDbcWLBnzwBeq3sN940_69fyC6ZRGGesXpMNEv-M6MfKhLnsrk7tBHOd0lvPppgEfS1bLCGouyli2x0jzE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تکرار مجدد داستانی مشابه داستان الهه حسین نژاد :
ملیکا ۲۲ سابه دانشجوی ترم آخر گرافیک بود و بعد از پایان کارش داشته برمیگشته خونه که متوجه رفتار عجیب راننده میشه .
همون لحظه لایو روکیشن برای دوستاش میفرسته ،
اما بلافاصله بعد از فرستادن لایو لوکیشن با راننده درگیر میشه و راننده اونو به قتل میرسونه و دو روز بعد جسدش توی یه کانال آب پیدانیشه
و طبق آخرین اخبار ، قاتلش هنوز دستگیر نشده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/145494" target="_blank">📅 02:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145493">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قوه قضاییه: حکم اعدام رضا پهلوی صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/145493" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: اگه ایالات متحده همین امروز از جنگ علیه ایران خارج بشه بازسازی این کشور ۴۵ سال طول میکشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/145492" target="_blank">📅 00:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b9e7185b.mp4?token=DEAffNQ0X9Rf9dM_yjb-_P3k4fK_Pi1Ebv9Uc8PxI_6SjcuWn2um9xryuUexzFBlc9srW7WfaPIL2esuQKfgtOeQaa4Bk7e_hQZVyMX9wJLIE0GuZUhoqedFUPGX0jcfi6TCCRuHHKRdnMZ_5JZ7MVq1Cor3CPdON7PHYvaANAqrwmB7-hDoG2613HSoGbHdfX9jD_uJTGBrmOo5-NysWvqSMTOUq23hIXmnTYssbSXLz7rTdNcZ3RUc2fKhbhznFsSbsfDBxWwMIwgkFgo_X4xtr8_i890gtE5OuZcqB5YhnViYQI-dhwVwmSTwVKsAiijzemRKrAGjgP4JYKdQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b9e7185b.mp4?token=DEAffNQ0X9Rf9dM_yjb-_P3k4fK_Pi1Ebv9Uc8PxI_6SjcuWn2um9xryuUexzFBlc9srW7WfaPIL2esuQKfgtOeQaa4Bk7e_hQZVyMX9wJLIE0GuZUhoqedFUPGX0jcfi6TCCRuHHKRdnMZ_5JZ7MVq1Cor3CPdON7PHYvaANAqrwmB7-hDoG2613HSoGbHdfX9jD_uJTGBrmOo5-NysWvqSMTOUq23hIXmnTYssbSXLz7rTdNcZ3RUc2fKhbhznFsSbsfDBxWwMIwgkFgo_X4xtr8_i890gtE5OuZcqB5YhnViYQI-dhwVwmSTwVKsAiijzemRKrAGjgP4JYKdQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «من انگلیس را از تهدید ایران نجات می‌دهم. اگر ایران سلاح هسته‌ای داشته باشد، احتمال استفاده از آن در اروپا بیشتر از آمریکا خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/145491" target="_blank">📅 00:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp3GxK4GvXpqaRZ9M1QxKtnQZOVyQM3AgqWL8Qm-Y5eZS72MnP7sgIMNt7gZPDyZPIGlerR327DqCPAYCP5q0Jy2QTjYeDQtLycMDGdzX307jrOzMIIQVfRyK_UiH0E4756DIi0BMdhaGQPrGEiS7h9muZy0o1dRwbZC02iI3JhcgQB6zchyuBge2hRUJ1Ug7k31iHt1In0EaeEFyucYsHn4UdN6m4mEydEkeMu5CGUlISWT9-OVkhuQFEPY6mwqeQIzQ5cEsJdMet3JGeJcCsaSvoDkgsSFHemFiTeQYFfW2-Ck7HeyXea9BIPYBnUd8VVG2JN6-p2s6VF6kqaejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiAK013DRm39xMmt-U_VQoy3IJfsdvs5HgSUvTW6LbcysOmoGOq7Pftqzpu1_fPycI2kk20_2e4cHMLtQK0w5RoQu7h6Yn1sszr1Wd2o_U6hwSm7Y2wwuGh3n3Gxc1phWAUSs26Amt0lM6YWkvHBGjYsJy1dFcSkAG6Duk5iO2dnFjNP9OFJR5VuyomCREEIe-PRTOboi2LxS2-RRXPc5g_3c1lbEwtvL8YsE857Kvt5MIy9XbLuYHR92o98BtCp0l-YtjYWshbqPXLfRxfHXhbzOqPWBthlRO_OynMczXHGc-3GbuDLtxI-Jj6K9y_b0jw9De6TGTL6wxEELnKIsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی نفت‌کش "میرکان" متعلق به ترکیه، از تنگه هرمز عبور کرد و از مسیری استفاده نمود که توسط ایران تعیین شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/145489" target="_blank">📅 00:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhaZAPoa50VF2dju7grgxYheXmg1N1w0auqJqNhlYqAlcADMBu4JuvCmYUuNhYnOEfxAX5gM5y-Y_HtBobcrCu-tx77TAiveDkpuhauHV-QRTSXAR2LWRSW6_N4_pB4mQ9Eg3w2YxXXxnmwg6LLpHj-crMlLtLN_XdfWK9AxWI9LJ2mkkZOCURtmKHJUtNcNtFUIsTRXyEvX4j0Gl82v2Eq15_2KxvLnSb-FZ5YYY1wOd9znbgwfyRbCoGZrKhC3PJIkuc2lj1u0tYNSb0ULdhHkVrZq_r37BbBgoTDGLHmtoQWS7BWQ8L0BhBGxZJEr6tYot1ILU4kjoBXiWCMARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی:  احتمالا هماهنگی جدیدی میان نتانیاهو و ترامپ شکل گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/145488" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lOScdEGG5yaaTevkMcUMJlSMWZVhcrAvIKks6xB-xe6UsRJjurHWvxB_AY_Z3hOeElOv8LbgqtlPe6G2fAb5zXGvoMEgzlZllG2aU5oJYr0IO4-MURWShjb_Z3UPv7kwWuNcScq9WfTiJpT2hhMynSCsVlbjxsBkQGkeL88YnciFPFvF2YAvFiFpAVaLnEwH0FlX-A09lpX1iLiIYTTbAi-HxbtAzqqsHsF5MbDLoijMMWFVh3JyFQvELIuzy9JudyMy-i3HK9onjIBGQfJJksvTXFSra19u8mHP1NhUr934OfN0w07qxZfrYJAtBncY1sQcfeGx-NwI4WLkD8vH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دادگستری ایالات متحده آمریکا پاداشی تا سقف ۱۰ میلیون دلار برای اطلاعات مربوط به امیر یاریاب، رئیس فرماندهی سایبری نیروی دریایی سپاه ، تعیین کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/145487" target="_blank">📅 00:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
متکی: آمریکا طرح چهارده بندی را پذیرفت برای این که بنا نداشت بهش عمل کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/alonews/145486" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itYGGw3EZmTlYPnel9gG_U31BuIyArJ_PaQPwlBKBjHcud5903KLOa4JuYtR8LXKAWAXIoVZAKMkuJwuJkM5PP5CyVScHYDt_soG8uz8bfvGntJKmtqGg5mWFlzCAXht6xFvpdXUC3vqnPXMZPtC_NQQngGv3iejc_Lt_RJFTZ1m9D9o8LvAJ1U1e9WwyDLUXsx78jkzPL4pvT0NAcoNa9XwUxKQMULFPwL3UKwWb_WMfH3y4K7JjJsJM2LE8h0wMwuS6T3y7wXE0edKCKGvukHaQvuMK91FKg0SSBhFGoLcyhboCuph_aaeuqnhwVC1OSykbCuxGvpVJGK-YJCXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی، سخنگوی وزارت امور خارجه ایران: دولت قطر، در یک سند رسمی که به اتحادیه بین‌المللی مخابرات (ITU) ارائه شده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر، "به تأسیسات نظامی آمریکا وارد شده است [...]. هیچ منطقه‌ای مسکونی هدف قرار نگرفته است."
🔴
تنها استثنایی که قطر مطرح کرده، حمله به یک تأسیسات گازی در تاریخ ۱۸ مارس است. با این حال، باید به یاد داشت که تأسیساتی که در آن روز مورد حمله قرار گرفتند، در خدمت تهاجم نظامی آمریکا علیه ایران بودند.
🔴
این موضوع، تضادی آشکار با سابقه طولانی ایالات متحده در حملات عمدی به اهداف غیرنظامی - مانند مدارس، بیمارستان‌ها، محله‌های مسکونی، مراسم عروسی، پل‌ها و غیره - دارد.
🔴
تفاوت بزرگی بین یک ملت متمدن که اهمیت پایبندی به اصول اخلاقی و انسانی را حتی در شرایط دشوارترین شرایط آموخته است، و حاکمان جنگ‌طلب که هیچ قانون یا اخلاقی را در اعمال قدرت خود رعایت نمی‌کنند، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/145485" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979fdd9589.mp4?token=h-FZrszrhHacws92A2is4bzbhlBEAo5NFUONaf8T2LrQm8juDbzKKBOfdRusxFVXCrFYbTG56bFL4i4BWjKmGjLacnv1gXixIp2Phe56TzHcRDHB0auZt9HcGN5NcPPTkIf4w9FFaCvwfVRp0Vrr3r7D8cxHu1r-GLi_dED9QgWs76EI8W1noXXGPV_7X4hGWzto5QCYMW6n8iyvEANMHAygf-Pn3OElXagQb716IR4sY_yQbuM9QsIp8Ha7zU0ZdSM9ZGpUc7BN9efbEQEqdfMhEp1RXZwDtFC7HQZZevX67nJxVK1JDUZEQjW1_EleNkDn5Lf6sOyP8lkANGsQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979fdd9589.mp4?token=h-FZrszrhHacws92A2is4bzbhlBEAo5NFUONaf8T2LrQm8juDbzKKBOfdRusxFVXCrFYbTG56bFL4i4BWjKmGjLacnv1gXixIp2Phe56TzHcRDHB0auZt9HcGN5NcPPTkIf4w9FFaCvwfVRp0Vrr3r7D8cxHu1r-GLi_dED9QgWs76EI8W1noXXGPV_7X4hGWzto5QCYMW6n8iyvEANMHAygf-Pn3OElXagQb716IR4sY_yQbuM9QsIp8Ha7zU0ZdSM9ZGpUc7BN9efbEQEqdfMhEp1RXZwDtFC7HQZZevX67nJxVK1JDUZEQjW1_EleNkDn5Lf6sOyP8lkANGsQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه رستوران اومده قیمت هارو به خاطر نوسانات قیمت به صورت لحظه ای تغییر میده و‌ تابلوی صرافی طور گذاشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/145484" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تحلیل الجزیره: آمریکا نتوانسته توانمندی‌های نظامی ایران را از بین ببرد
🔴
در حال حاضر، هیچ‌ یک از دو طرف قصد تشدید تنش را ندارند
🔴
این خوش‌بینی وجود دارد که در آینده نزدیک شاهد تشدید عمده تنش‌ها نباشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/145483" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ارتش اسرائیل: عملیات پاکسازی دو تونل زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر در جنوب لبنان به پایان رسیده و اکنون در حال خنثی‌سازی این زیرساخت‌ها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/145482" target="_blank">📅 23:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد که نیروهای آمریکایی مسیر ۸۷ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و ۲ فروند را بازرسی کرده‌اند تا از رعایت مقررات پس از تشدید محاصره بنادر ایران اطمینان حاصل کنند.
🔴
این تعداد شامل یک کشتی بیشتر است که از روز چهارشنبه تغییر مسیر داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/145481" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گاردین: رئیس سیا در سفر به روسیه از مسکو خواسته حمایت خود از تهران را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/145480" target="_blank">📅 23:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
‏ کانال ۱۴ اسرائیل مدعی شد
🔴
پاکستان و قطر طی دو هفته گذشته دو بار از ترامپ خواسته‌اند بخشی از دارایی‌های مسدودشده ایران را برای کمک به کاهش تنش آزاد کند، اما ترامپ هر دو درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/145479" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L30w30cPBR-l224taXYouXbYjhRp-a3x_33bMcPkg0XC24WUamadIEXsN6-VFXdTIECkuJ-4P5377nbiD40vFid1ZZGcTI3u5HBVXAaU10w-Nt4N9OrUxN0bKe1oi-H0BFt_274FDJNb0Kl4BF0cGLqwHxQt_NujzkNZ-PO33ByVT2x_G2jI-od_7bV-vRrRCgPYieO4luGZyHUfx8PIo0GaK6e26HsyjDyyxAw2YJdNgLTyuPD08pAQOGUug-1fx45vSAKJIza8HEiQuAE6SHdVSEyPAZ_gAbs9F2krpfebxdW9LQiJ4Fgqe9tLkKq5mip6mbts_4YwcA1J8YY7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت نتانیاهو پس از خبر تسلط بر ارتفاعات علی‌الطاهر: با ما درگیر نشوید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/145478" target="_blank">📅 22:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH7rjFgM3YNVPGiG4KVG2ofZXctb3l_2Lu45oDEDgzKG1l-NnrM8mUrGXDYnNgyl8AiRwj3UW7J-tWnNPrLAAEsDyUJkB24bt8CBUAbOAqGx4BJEzslWyDcPBle_WeV3HK_aVq-UB1pvEsr9p572np6BIBhwCdE-uE0exzT8avnzuZF0rKzIcgXXTQSJ0Qh2AVPI81QTL09g02UTdJqdGcuNfNSJJjXlP3q1M3rvAb8-zu2lacDjYis-G-HmwZ5ei96Cs--65VTI3BPVQcs3I2_VjPeA5ZEp03_RZG-oOeypER5LduQJiuJOQs8qYZKTbf3gGOR2NgQdeoLSx1W7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به روستای المنصوری جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/145477" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOtRTrRxftFW_wCAWH-u49d99ZQV0lw-wckn37A67pt4p8L3bixiBEOTjAVIu6spTSdPIlA5U48yrPNUK7OAdzIFluOsjSkxTwrcn4J8L7tq5L-I-3QGGz-eK1LZfKmPy8bUGwvxU-hjz3QOYax3Nxzf9sEGIFIpTxAqEixeJ00tvgFexDfAYwhVPE5zlENoyaYKf4EO2hYPQ0ymAGomjEuN5DenJNSvRwhoIepUmFGmFRJGvOKbPLj1P-usf9t9GX4W1M_rsZZ8hJ12Yb6SmRjMZurc_nKELPzqR-d0XyqJBZftm7mD4t81nck-wGgnXpThYka0aUK4ahVNtfWY0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه: امروز من نوه‌ای از راوول کاسترو به نام فیدل ارنستو کاسترو کالیس، بانک بیرونی کوبا (Banco Exterior de Cuba) و چهار نهاد دیگر را که بخشی از شبکه فاسد مالی و اطلاعاتی کاسترو هستند، مشخص کردم.
🔴
دونالد ترامپ و من در تعهد خود مبنی بر اینکه کوبا آزاد خواهد بود، سست‌ناپذیر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/145476" target="_blank">📅 22:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=tLnpRKEZ53pYaYSK__OwjbHYiGVJpVksEV1-ygQnMlYO5-ka1oz4ojFfNYjfBqagxiHYlWQIElMRzIFOWm7b3ANUOMc_L2nB_EiOY5aokXTBovEJfVf5UibNz7gFGA5bFYXCMFd4Q5fDioL0fBLfP7dc8SqNa9Y9KigpjicBTWg9Kt24z2YAK1g23PvNvp3ScncQ53ebTpXKe7f_yshG011_gGJkHSGYhyAtUuhDdgL2aAlyvmfreVvr7i7INKlbI8pI9hx5AT3SfJNYoL2yF2rTIWbNios6K1HJypVg25r-duok8FdbkhKmkWph-mqu9BEIK71EfIJSWSqGgMdjOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=tLnpRKEZ53pYaYSK__OwjbHYiGVJpVksEV1-ygQnMlYO5-ka1oz4ojFfNYjfBqagxiHYlWQIElMRzIFOWm7b3ANUOMc_L2nB_EiOY5aokXTBovEJfVf5UibNz7gFGA5bFYXCMFd4Q5fDioL0fBLfP7dc8SqNa9Y9KigpjicBTWg9Kt24z2YAK1g23PvNvp3ScncQ53ebTpXKe7f_yshG011_gGJkHSGYhyAtUuhDdgL2aAlyvmfreVvr7i7INKlbI8pI9hx5AT3SfJNYoL2yF2rTIWbNios6K1HJypVg25r-duok8FdbkhKmkWph-mqu9BEIK71EfIJSWSqGgMdjOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 23,600,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/145475" target="_blank">📅 22:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz2oyxHank9SufFrf7umgsHh5BVZVJvzpbtSTNabVThqdh68Lt_hsxcBs3y2_U_AoB4mpbj0W-jwSfZMO6oWCM3CZsCLna0AvKZjcH43qL5LmASVgt3vScRFzfRSx42lreLNIhIp9_fSEeQYCy5sZWKlUfDnjIaBol9GyLoFwBlWlWlQ_gQPo5dJ-ViD2rurZZ2RmXZVKrhUA5T3fYM3s8JMPzCQBhZXfJndpT8MwepwbT8VbtQLVx3188fad-VMjA8w3ggS7MCY7m9S8L1wdm-J32vMoPbi54Bgrjte4vFt691-oIQkJbXu0_1dBd9Yq6jiEf8e4nFArR20MDcLxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایمز اسرائیل
:
گزارش قبلی رویترز مبنی بر اینکه ایران به آمریکا هشدار داده است که به هرگونه عملیات تهاجمی اسرائیل علیه علی طاهر واکنش نشان خواهد داد، کاملاً بی‌اساس است.
🔴
نیروهای دفاعی اسرائیل (IDF) از چند هفته پیش در تونل‌ها حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/145474" target="_blank">📅 22:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۱۸ نظامی امریکایی کشته شدن!   رویترز گزارش داد وزیر بازرگانی آمریکا سخن قبلی خود مبنی بر کشته‌نشدن هیچ آمریکایی در جنگ با ایران را پس گرفت و تأیید کرد که ۱۸ نظامی آمریکایی در جریان جنگ با ایران کشته شده‌اند. این رقم مربوط به کل درگیری است و رویترز آن را مشخصاً…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/145473" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ونس : اگر به ترکیه، آذربایجان، قطر، امارات متحده عربی و عربستان سعودی نگاه کنید و به طور کلی به سراسر جهان بنگرید، در واقع شاهد تعداد زیادی از کشورها هستیم که گاهی اوقات حاضر به بیان علنی این موضوع نیستند، اما در پشت پرده کارهای بسیار خوبی انجام می‌دهند تا به ما کمک کنند تا اطمینان حاصل کنیم که ایرانیان به دلیل شلیک به کشتی‌های تجاری، مجازات شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/145472" target="_blank">📅 22:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145471">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ونس : هرچه بخواهید درباره چین بگویید، آن‌ها از آن دسته کشورها نیستند که به دلیل نپذیرفتن خواسته‌هایشان در یک اختلاف‌نظر بین‌المللی، به کشتی‌های تجاری شلیک کنند.
🔴
آن‌ها قطعاً مسئولیت‌پذیرتر بوده‌اند، هم از ایرانیان و هم از چند کشور دیگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/145471" target="_blank">📅 22:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145470">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ونس: ما می‌توانیم منطقه را ترک کنیم، اما کشورهای عربی حاشیه خلیج‌فارس به ما می‌گویند این بدترین اتفاق ممکن است
🔴
با وجود اختلافات سیاسی ما با چین، آنها مایل به همکاری با ما برای اعمال فشار بر ایرانی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145470" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145469">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996568e758.mp4?token=tCQjwsx_gw17aOGFJcnDnvBBgCXaR5iTIUfRiGBzs568jl9PT15K8WBatgUjOS1bu1kr9jzh90UzNTHUNCMGe6rDrVbC2eV2X9p7Tlex0-tLf1l47c_uY57u2VIxwkGQ2zT0xE5C01ji6U4Js6KGPq-ZL3humRmoCxqxbXDAypx1Rts-PKQgFBubgP00i1aPwSOW5EKylaAS57IChVQd3QngnyZSihfXehMHfeinDKYDbI8U6ev8hTBs0CNko47tTXWZnxHqGPKicFLksbHxfzftqd1zbmmzVqKa1B30FbrG8C80JL-Aj3JgL3NvxcnaXDnqGtZbrYYljHV6g_jzPSDhKpT90zcQA2e5BbnqcPedem5JzmTsJj0zGo7bhQZsb6W2yDr5GWe7vvgUoMuwz3KR_SksseEcModJiaxeD8zCyEpsDn-Y9KlD1veTLQj8Pq3tB6oFuq09QhVV9eoVSB-MqbcmXLhA9cl1jhEn5c04qwik0D0_1E57A5wQCFpFozzYr_4G6qILhWUI-7lC2Mf0ed8ikm2WmlxcGOeMdY9oiBxb7oioFQKQbZGPka6yB1_kGFPYViSnZwyRiAiksFkZIzxFyKC2Ac9T-K5v_rTtlH5DBkfGS65XByAIyGB1rNYONMrxbEwKZtv3AhFlt8cYLoyGMDGF9Vvr9FVMFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996568e758.mp4?token=tCQjwsx_gw17aOGFJcnDnvBBgCXaR5iTIUfRiGBzs568jl9PT15K8WBatgUjOS1bu1kr9jzh90UzNTHUNCMGe6rDrVbC2eV2X9p7Tlex0-tLf1l47c_uY57u2VIxwkGQ2zT0xE5C01ji6U4Js6KGPq-ZL3humRmoCxqxbXDAypx1Rts-PKQgFBubgP00i1aPwSOW5EKylaAS57IChVQd3QngnyZSihfXehMHfeinDKYDbI8U6ev8hTBs0CNko47tTXWZnxHqGPKicFLksbHxfzftqd1zbmmzVqKa1B30FbrG8C80JL-Aj3JgL3NvxcnaXDnqGtZbrYYljHV6g_jzPSDhKpT90zcQA2e5BbnqcPedem5JzmTsJj0zGo7bhQZsb6W2yDr5GWe7vvgUoMuwz3KR_SksseEcModJiaxeD8zCyEpsDn-Y9KlD1veTLQj8Pq3tB6oFuq09QhVV9eoVSB-MqbcmXLhA9cl1jhEn5c04qwik0D0_1E57A5wQCFpFozzYr_4G6qILhWUI-7lC2Mf0ed8ikm2WmlxcGOeMdY9oiBxb7oioFQKQbZGPka6yB1_kGFPYViSnZwyRiAiksFkZIzxFyKC2Ac9T-K5v_rTtlH5DBkfGS65XByAIyGB1rNYONMrxbEwKZtv3AhFlt8cYLoyGMDGF9Vvr9FVMFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ماریا بارتیرومو از فاکس نیوز رفت. آیا او قرار است سخنگوی بعدی کاخ سفید شود؟
🔴
جی‌دی ونس: نمی‌دانم، رفیق. نه، فکر نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145469" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145468">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754c0d566e.mp4?token=s9dA--EzXXAe4GAX-t5j-bMdjCmw3A3rtoy0WIXkC3-vm3DvNb8riE6oRVC8-cjAr9npboLt6vMOXl-vSPuqt_f-Zqu7t0PgesXs_wWAPpLnGEHOMKAqLIiOAAt_866Hc5nOwjtYaea7IVA3aukEt_Sz9JJBheheVbSpiko6G0ENyqEI0vnkp1fASuultQDvMqsxhtfFysv5T8b6o3-X-rKCjphZtRhV-17_f0_zLU46D0CRP_iYUV6B0Bq6zqfKjwog-hp_7Pns3EnzWxz71fAQMLZcDfgS5ynVEEjgCEIq4KZOAj1Go6x2gBjmVE8NuacjH6f1TGbAOWJl3oYEHiwWgXvZy9qe1yVbXOLuQMHnsGGbem4aZe7TBgteXHF4U1xvP3b4xe3EripIA6ecjVAYIGD1pvOrNNzNZj1zIMb0b1C-QjEUDhV0AMrQz1FAkateVCBm4bvntFsIGFAEV0bYquSnzjqDQ0NsLf1ks7oX3m-xNLilNOjIecN6ZTAvwSG_hj_K049ejDXU6nnTA51EXH-eQGNYX8Dip_fHaTTC9ZIjgnDt7LPUscIYyT7CRd3Xhqm2SzZ2bqR9ApTtAIjUCQ78P-XHtzY-agDXEvA7VQFTuG8zU4hoqJmYG7V-UX5frLmfwYnCX0eiN798MG_2szEZIrhz5WQIBOHNEM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754c0d566e.mp4?token=s9dA--EzXXAe4GAX-t5j-bMdjCmw3A3rtoy0WIXkC3-vm3DvNb8riE6oRVC8-cjAr9npboLt6vMOXl-vSPuqt_f-Zqu7t0PgesXs_wWAPpLnGEHOMKAqLIiOAAt_866Hc5nOwjtYaea7IVA3aukEt_Sz9JJBheheVbSpiko6G0ENyqEI0vnkp1fASuultQDvMqsxhtfFysv5T8b6o3-X-rKCjphZtRhV-17_f0_zLU46D0CRP_iYUV6B0Bq6zqfKjwog-hp_7Pns3EnzWxz71fAQMLZcDfgS5ynVEEjgCEIq4KZOAj1Go6x2gBjmVE8NuacjH6f1TGbAOWJl3oYEHiwWgXvZy9qe1yVbXOLuQMHnsGGbem4aZe7TBgteXHF4U1xvP3b4xe3EripIA6ecjVAYIGD1pvOrNNzNZj1zIMb0b1C-QjEUDhV0AMrQz1FAkateVCBm4bvntFsIGFAEV0bYquSnzjqDQ0NsLf1ks7oX3m-xNLilNOjIecN6ZTAvwSG_hj_K049ejDXU6nnTA51EXH-eQGNYX8Dip_fHaTTC9ZIjgnDt7LPUscIYyT7CRd3Xhqm2SzZ2bqR9ApTtAIjUCQ78P-XHtzY-agDXEvA7VQFTuG8zU4hoqJmYG7V-UX5frLmfwYnCX0eiN798MG_2szEZIrhz5WQIBOHNEM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : ما با اطمینان کامل احساس می‌کنیم که سرزمین مادری در امان است. همچنین با اطمینان کامل احساس می‌کنیم که مقامات جمهوری اسلامی قصد انجام کارهایی را دارند که توانایی انجام آن‌ها را ندارند.
🔴
مردم آمریکا باید بدانند که دولت آن‌ها با تمرکز وسواسی، هم بر پیش‌بینی هرگونه تهدید سایبری بالقوه و هم بر پاسخ مناسب به آن‌ها و اطمینان از عدم وقوع آن‌ها متمرکز است.
🔴
اگر به توانایی ایران در اختلال‌آفرینی در زندگی عادی آمریکاییان نگاه کنید، فکر می‌کنم این توانایی بسیار محدود است. صفر نیست، اما بسیار محدود است. من بیشتر نگران حملات سایبری از سوی بازیگران دیگر هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/145468" target="_blank">📅 22:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ونس : وقتی می‌پرسید «این جنگ تا کی تمام می‌شود؟»، در واقع دارید از من سوالی مثل «ایرانی‌ها تا کی به کشتی‌ها شلیک می‌کنند؟» می‌پرسید.
🔴
من پاسخ این سوال را نمی‌دانم. باید از ایرانی‌ها بپرسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/145466" target="_blank">📅 22:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5614d226b.mp4?token=etJC8ev88e_PoNoMFaoy5oIpVKik2A3FT3fApSzIQ8VIYXEQJaOFWUiSsHRzF3pMpam8TbujYlDJkU2Z30lb7JK9sNLUGwqB1gx6Y6HqA6HZFSity5IzrAVU9NygJ-T278i_RbeQxBICrwIUSNNE8nZ8WboE0HpCjXy9PSBplsGsdTDncVyrIeWCy2nh1-ksQffYelaOjLjMYMFAsJQar3bHGZ2BZX0HfagMGuiz0_FtP9b1ZkDwJBit22CUQkq0OWoOzGhGX-4pw1hoduJZQxNsPSgiLZn_6HAoLxRoCAgiLJQFS1aFUx18vi_Fcu4JL83F2KKM-z9BrmIlCYGmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5614d226b.mp4?token=etJC8ev88e_PoNoMFaoy5oIpVKik2A3FT3fApSzIQ8VIYXEQJaOFWUiSsHRzF3pMpam8TbujYlDJkU2Z30lb7JK9sNLUGwqB1gx6Y6HqA6HZFSity5IzrAVU9NygJ-T278i_RbeQxBICrwIUSNNE8nZ8WboE0HpCjXy9PSBplsGsdTDncVyrIeWCy2nh1-ksQffYelaOjLjMYMFAsJQar3bHGZ2BZX0HfagMGuiz0_FtP9b1ZkDwJBit22CUQkq0OWoOzGhGX-4pw1hoduJZQxNsPSgiLZn_6HAoLxRoCAgiLJQFS1aFUx18vi_Fcu4JL83F2KKM-z9BrmIlCYGmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
در مورد جمهوری اسلامی آیا جنگ تا انتخابات میانه‌ای تمام خواهد شد؟
🔴
جی‌دی ونس
:
من آن را جنگ نمی‌نامم. در حال حاضر شلیک فعالی وجود ندارد. من می‌پذیرم که در برخی مکان‌ها این تنش‌ها تشدید شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/145465" target="_blank">📅 22:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f8eb7ba2.mp4?token=CPrwGebi0ErTlYQ8QH8emolGHi4zpHdpC-8fbFdb2IKN-ST1g2O1oBfeKDb3jiTyaEN1ge5NOlZyBzXfqb3v1x3fFcmQte6kRY1sF7M6M0rtkXs3KDUMAi6XfILJaHTrwtbcSwxFXmWa-JFKOMfTcV1qF9QYnnBgajk0x5LVlBPX3w2DOuvmRXlgeI2xQqiVtyFSio4Zah4jbStexecjJ8xwlNUJgTXfa8dw3H54lTo0WTHC--5ls0EWJngRMNODVBii7-i_JFQkxuhyqixkoanAAJdqWRh6kNjWRDwtpxkOnJIKmoS-WT3DAGmaL1jfQwZNQegrZkKS6OPmfkKfig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f8eb7ba2.mp4?token=CPrwGebi0ErTlYQ8QH8emolGHi4zpHdpC-8fbFdb2IKN-ST1g2O1oBfeKDb3jiTyaEN1ge5NOlZyBzXfqb3v1x3fFcmQte6kRY1sF7M6M0rtkXs3KDUMAi6XfILJaHTrwtbcSwxFXmWa-JFKOMfTcV1qF9QYnnBgajk0x5LVlBPX3w2DOuvmRXlgeI2xQqiVtyFSio4Zah4jbStexecjJ8xwlNUJgTXfa8dw3H54lTo0WTHC--5ls0EWJngRMNODVBii7-i_JFQkxuhyqixkoanAAJdqWRh6kNjWRDwtpxkOnJIKmoS-WT3DAGmaL1jfQwZNQegrZkKS6OPmfkKfig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس : دیروز شب، ۱۵ میلیون بشکه از تنگه خارج شد. این به دلیل ایالات متحده است.
🔴
اگر ما این کار را انجام نمی‌دادیم، هیچ‌کس دیگری آن را انجام نمی‌داد و اگر هیچ‌کس دیگری آن را انجام نمی‌داد، با یک بحران انرژی جهانی فاجعه‌بار مواجه می‌شدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/145464" target="_blank">📅 22:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ونس : ابزارهای اضافی زیادی در اختیار داریم.
🔴
برخی از این ابزارها توسط رئیس‌جمهور استفاده خواهد شد و برخی دیگر نه، اما من قصد ندارم دقیقاً تبلیغ کنم که چگونه در ماه‌ها و سال‌های آینده با ایرانیان تعامل خواهیم داشت، زیرا صادقانه بگویم، این کار فضای تصمیم‌گیری رئیس‌جمهور را از بین می‌برد.
🔴
اما هر آنچه ممکن است رخ دهد، روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145463" target="_blank">📅 22:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129206ce04.mp4?token=Jlxlw_H9QqLr5jKu1nnaTW5i3iSf6Z34F34tnXxTRLlmeY8_xd1HoHj0gg-n42r51WASbLkfbscgxFBd5KG4iinQij12tEdz5ItshuRjlMUQcr3LOz9m3py4IgpgxhfMt7HNTNT38Z2qWIXg7Z7vN210nPP-tOXt1E6WM9E_xOYC3QDo_yL9G3M_37nspvLZflKhDyT9XL6FsLFcMSOrjN4sDkVOaq1zzKWBlHtldagVy7ager9tgQzvX9QiP32pwevJKxs_NWnTNJmHQK8zXiSs8suMKvUgtGwxHvy14s7pOwym9y4V2Ruwwcr6uwgVK_zzdtyBIPNJ0z9gY1RoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129206ce04.mp4?token=Jlxlw_H9QqLr5jKu1nnaTW5i3iSf6Z34F34tnXxTRLlmeY8_xd1HoHj0gg-n42r51WASbLkfbscgxFBd5KG4iinQij12tEdz5ItshuRjlMUQcr3LOz9m3py4IgpgxhfMt7HNTNT38Z2qWIXg7Z7vN210nPP-tOXt1E6WM9E_xOYC3QDo_yL9G3M_37nspvLZflKhDyT9XL6FsLFcMSOrjN4sDkVOaq1zzKWBlHtldagVy7ager9tgQzvX9QiP32pwevJKxs_NWnTNJmHQK8zXiSs8suMKvUgtGwxHvy14s7pOwym9y4V2Ruwwcr6uwgVK_zzdtyBIPNJ0z9gY1RoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در مورد ایران، آیا این درگیری تا زمان انتخابات میان‌دوره‌ای به پایان خواهد رسید؟
🔴
جی‌دی‌ونس: من این رو یک جنگ نمی‌دونم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145462" target="_blank">📅 22:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51942fb259.mp4?token=pAr0T5qXsem0eEGbI4wLYn5TktFFU0ycdTpgP3VImFq9aZxRDB_rbEbUY2AzwF4mJsI5lyJR2afPrvcZxcDG56NvaPhmFLeVhfpvtABfMFHwSn6iPLWRg6q8075MKwbUCAWZkfR5Y4GUZ8QfQyhqIleJ6_4cIEP0AIn0Z46yBzpeM6SFG4-58RtrmVGmaziGLaGOA3q6dpdTD3qrzxI3jt93aOvJbuMZqkNiYXDvS3BnvcbydZJ9GB5k_0bHsdi7pvyGKrkTUzcwK6WmB5mfv_1r2UOkrwoIYAQfeH8kF2rtMxMIwgDbb1GAVXfiDwdpwqmSNYMvxBZwJQ5afyDcDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51942fb259.mp4?token=pAr0T5qXsem0eEGbI4wLYn5TktFFU0ycdTpgP3VImFq9aZxRDB_rbEbUY2AzwF4mJsI5lyJR2afPrvcZxcDG56NvaPhmFLeVhfpvtABfMFHwSn6iPLWRg6q8075MKwbUCAWZkfR5Y4GUZ8QfQyhqIleJ6_4cIEP0AIn0Z46yBzpeM6SFG4-58RtrmVGmaziGLaGOA3q6dpdTD3qrzxI3jt93aOvJbuMZqkNiYXDvS3BnvcbydZJ9GB5k_0bHsdi7pvyGKrkTUzcwK6WmB5mfv_1r2UOkrwoIYAQfeH8kF2rtMxMIwgDbb1GAVXfiDwdpwqmSNYMvxBZwJQ5afyDcDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس:  اگر به توانایی ایران در مختل کردن زندگی عادی آمریکایی‌ها نگاه کنید، به نظر من این توانایی بسیار محدود است.
🔴
این توانایی صفر نیست، اما بسیار محدود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/145461" target="_blank">📅 22:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019a996d7f.mp4?token=QMV-g3GuCQCxQh3qhYUevH2IABD0UtbRsp8EW1al43qsjEN8akTI4_38RNJCNPeScUfY5m0OjisSEo_UXRR2yNKlf7U960p8pdixTVey73sCljnv2Wkyx0vuzO5CSiTXMuESVBA3RVTvtZswO9PoyXhSphKY8qAQlT8ourafbk5wSDg4iP8ZG6Mk5YP3fTjq-9llnzYViAx8VtPxidGjwW2zVzKHL4BtZ5dfqfLiaEfSguAqr96adVR2dPHb9xt27G6jP2XZ6BFBc3Y_9A43CPukEGrWbT8GlNNFaWtz09x3Fj4dWlXtEy2ov3TteBkWXEQnVrobKx-hDjQD5B3V8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019a996d7f.mp4?token=QMV-g3GuCQCxQh3qhYUevH2IABD0UtbRsp8EW1al43qsjEN8akTI4_38RNJCNPeScUfY5m0OjisSEo_UXRR2yNKlf7U960p8pdixTVey73sCljnv2Wkyx0vuzO5CSiTXMuESVBA3RVTvtZswO9PoyXhSphKY8qAQlT8ourafbk5wSDg4iP8ZG6Mk5YP3fTjq-9llnzYViAx8VtPxidGjwW2zVzKHL4BtZ5dfqfLiaEfSguAqr96adVR2dPHb9xt27G6jP2XZ6BFBc3Y_9A43CPukEGrWbT8GlNNFaWtz09x3Fj4dWlXtEy2ov3TteBkWXEQnVrobKx-hDjQD5B3V8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : همه می‌دانند که تاکر کارلسون و من دوست هستیم.
🔴
بسیار واضح است که تاکر برخی چیزهایی را گفته که من با آن‌ها موافق نیستم
🔴
او برخی چیزهایی درباره رئیس‌جمهور ترامپ گفت که به نظر من کاملاً نادرست هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/145460" target="_blank">📅 22:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ونس: ما تا زمانی که ایران از شلیک به کشتی‌ها دست نکشد، با آن مذاکره نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/145459" target="_blank">📅 22:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ونس: آمریکا از زمانی که من زنده‌ام، جنگ‌های زیادی را تجربه کرده است. ۴۲ سال.
🔴
و تا زمانی که دونالد ترامپ رئیس‌جمهور ایالات متحده نشد، تقریباً هیچ‌کدام از آن‌ها را برنده نشده بودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/145458" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ونس،: توصیه من به مقامات جمهوری اسلامی این است: از رفتار مانند افراد دیوانه دست بردارید و از شلیک به کشتی‌های تجاری بپرهیزید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145457" target="_blank">📅 22:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817351e76e.mp4?token=s9dLoqB7QMpTJo89sGIX82TvE0tOPNk-NrpYZKQXmzbBcwvHBrJyl44pkHYhuxpPm2C8VjfiofuQq-NRbjUkEB9ymkA6kQ5DmUNkxOnRwkVcxMEbbE3yKQ9wwJmZnkXI9gUAXPl_WMCptztWLgQ8qfUAlfwUxu0r5MKRz6tfvXwwQI_DEUxIetIgWNdV5WwKKu-gppAlUwVT0kDjqvS8VMsC-DhbE-oqviNkDL6tFQJfpIGm-5AQJDd1633BodwN_Ziq-5e7xbIvjAA1w0Uj-EHpOcU1iNTqNLVYjqpNJ3ayttCX43Fa4y6iEoNigXC_NzBGdFq8pS6nbf1n0Xvomg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817351e76e.mp4?token=s9dLoqB7QMpTJo89sGIX82TvE0tOPNk-NrpYZKQXmzbBcwvHBrJyl44pkHYhuxpPm2C8VjfiofuQq-NRbjUkEB9ymkA6kQ5DmUNkxOnRwkVcxMEbbE3yKQ9wwJmZnkXI9gUAXPl_WMCptztWLgQ8qfUAlfwUxu0r5MKRz6tfvXwwQI_DEUxIetIgWNdV5WwKKu-gppAlUwVT0kDjqvS8VMsC-DhbE-oqviNkDL6tFQJfpIGm-5AQJDd1633BodwN_Ziq-5e7xbIvjAA1w0Uj-EHpOcU1iNTqNLVYjqpNJ3ayttCX43Fa4y6iEoNigXC_NzBGdFq8pS6nbf1n0Xvomg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس درباره ایران:
رئیس‌جمهور ترامپ گفته است که ما واقعاً دو گزینه در اینجا داریم:
🔴
می‌توانیم منطقه را ترک کنیم و کل جهان بسیار بدتر خواهد شد، زیرا دسترسی تضمین‌شده به نفت و گاز وجود نخواهد داشت. کشورهای عربی خلیج فارس به ما می‌گویند که این بدترین اتفاق در جهان خواهد بود.
🔴
یا می‌توانیم بپذیریم که ایرانی‌ها مانند افراد دیوانه به کشتی‌ها شلیک خواهند کرد و ما کاری که باید انجام دهیم را خواهیم کرد تا اطمینان حاصل کنیم که تلاش‌های آن‌ها منجر به بحران انرژی جهانی نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/145456" target="_blank">📅 22:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
جی‌دی ونس: تا اینجا عملکرد بسیار موفقی داشته‌ایم.
صادقانه بگویم، اگر تلاش‌های ما نبود، قیمت بنزین می‌توانست بسیار بسیار بالاتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145455" target="_blank">📅 21:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bb4cabcc2.mp4?token=fggZ4Y7qukUOm0ZANu5DI6uMppzyks8M-Jgm00yoIabWJ2c8fQ9HLNJt8kqBmudlcXpSPwP1rQpVFtojhwQq6JNVqwiPPPRzmM-4yMCO8TXa5rxZati7HC9a-PENCBq5-TAgJZCD3rRksGT7UsYS1h2fLgUAaed9QfYf00qjIXlAX4fTks_H3xFafJknzzjBLw6O2o7HMu6lT1TfwZbVqbFGSVmghsbYXg8sbTYHTmg95qfIF3ZU1hJ6RQhdjJoaJ6Z3tWjUsX9xwyuK62rzU4JtvqbWAlsbpMfKRwev-d6a9pX3kPYqCo39f9yP-Ks_Qm1X0VWdHq5GtWSQlRAnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bb4cabcc2.mp4?token=fggZ4Y7qukUOm0ZANu5DI6uMppzyks8M-Jgm00yoIabWJ2c8fQ9HLNJt8kqBmudlcXpSPwP1rQpVFtojhwQq6JNVqwiPPPRzmM-4yMCO8TXa5rxZati7HC9a-PENCBq5-TAgJZCD3rRksGT7UsYS1h2fLgUAaed9QfYf00qjIXlAX4fTks_H3xFafJknzzjBLw6O2o7HMu6lT1TfwZbVqbFGSVmghsbYXg8sbTYHTmg95qfIF3ZU1hJ6RQhdjJoaJ6Z3tWjUsX9xwyuK62rzU4JtvqbWAlsbpMfKRwev-d6a9pX3kPYqCo39f9yP-Ks_Qm1X0VWdHq5GtWSQlRAnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس
:
برای مدت بسیار طولانی، دولت بایدن ذخیره استراتژیک نفت را صرفاً با هدف کاهش هزینه‌های بنزین و نفت تخلیه کرد.
🔴
هیچ بحران بین‌المللی وجود نداشت. هیچ کشوری خارجی تلاش نمی‌کرد تا بازارهای جهانی انرژی را مختل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/145454" target="_blank">📅 21:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رسانه لبنانی و اسرائیلی ادعا کردند که تپه علی الطاهر لبنان و شهر موشکی اش سقوط کرده، هم اسراییل و هم حزب الله پذیرفتند
🔴
نیروهای حزب الله بدون جنگ عقب نشینی کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/145453" target="_blank">📅 21:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رسانه لبنانی و اسرائیلی ادعا کردند که تپه علی الطاهر لبنان و شهر موشکی اش سقوط کرده، هم اسراییل و هم حزب الله پذیرفتند
🔴
نیروهای حزب الله بدون جنگ عقب نشینی کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/145452" target="_blank">📅 21:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اسلام آباد: نیروهای امنیتی ما ۱۵ شبه نظامی را که قصد داشتند از افغانستان وارد خاک پاکستان شوند، کشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/145451" target="_blank">📅 21:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مقام ایرانی به رویترز: در نهایت افزایش نرخ تورم و سوخت در آمریکا، ترامپ را به ‌عقب‌نشینی وادار میکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145450" target="_blank">📅 21:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rhd-uw1mdGo916hqwqydfBUVLAIfe2IGKDWuvuql3dhgtCU7nRk5Go8gaDWApf_5h57Nu1F6yOAhJTSYuaikE-6wIqaCYnw9GPzbqRRo-UuIbcxRxFFif-Bxy3-R1dHIE3QzrjqF9_x8zN608tzXiR1Er02NZBbI9W9mpQeu40ntcFoO598GTswu-7NdnZmmmdx60L2aoxH92C7hWY7zTuvthK9CKQAm9JXO1ijB_CRl-EDvqYO2XOa66-g7_12bqocBJqmrJ2tFe3XXvuMhk9ABo0ekIOHGiJ1S0yuUVUgrTi7F99rujGps9ROhAt68HDP_EfrKUwU0crwg55Cqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X7SqrvyQ3ON9X9fXpCqpqybGPyfVc71lLGnt3QsMX9BB_zybvKgnVWonpTEGI4sfTMb44VKnvUjuEr9PgfJgC-ZrnHaRtgwQcWb6bGCE7Vzt3kAS0_n1E6KBKKi0uPCEcUfOWrV9ypC5aVbq3oYEBFseQgaOpX_psL9UrN8QseokjRp5bm3Bmwm-ogwT_FV4fgGJhur6G6kULGZFKCHPxlpiEoWgAUqu5U2XYayEZFBkJoYUl8Yboy3pJG4G9t9QhaCqyXKYL3nyTtCSKKVey6_F84NcFLg1DLVmsDPLizfnqSi_qo62gT-Odfdp5aqdc4YgG3ypWrAyfM2tEZR2hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات سنگین شبانه اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/145448" target="_blank">📅 21:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر نفت: در جنگ ۱۲ روزه انبار نفت و پالایشگاه‌های فجر جم و پارس جنوبی هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/145447" target="_blank">📅 20:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیروهای اسرائیلی با چهار راکت، اطراف تپه «باط الورده» در نزدیکی شهرک «بیت جن» در ریف دمشق را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/145446" target="_blank">📅 20:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhSGEPov9Ad6TJsGt9u1MX9URjTNHJxZbR7dPybjE1bsEu73JG3d0Ecm-G1h7xeCIhMkFozFriwwakirpT0iE_PiFl9sPy0iKqiKOU0UUqjSesqC60250wkbt0cTU3MJeMMPP4ZB8Adw1RZL08HtzjG_k_th8l7qh0RUqDGCuerLv8cEP-XG7NZ9lgk0cW9en2xtuPg3Pa9FBh3Z4msa8Yu4qo1qnchpmzDfykPElwqnIGQNH7hLHV_v3RXV3Rlb2s_kFfCqPTDXdfCrhjyVbI19qzeY1orsghzGdh_RnZ9cOgmf3jk5indX764PAQyED33HCck3WhW9Hq1i9Hzb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری های جدید علی کریمی که بازخورد های زیادی داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/145445" target="_blank">📅 20:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007137e607.mp4?token=cSN_nc_pWUMQv7aXd6KjqZzt1cNEf65HSuhZl8kad9IUbN-5_AxSgkmlyNKAOQZyEoWBzF_WPBwEsgXIVbKcyOcRBHpsKSh0ZyCULu3HOPeC7osxU2iHZLoELlJR4RYhRA-81HlxluG6_DTlRC9dJtuL8p1JTpXPVy_c3l7pJ28msskIcPEeKAoJwIVcJANuBa54Omei3kZW0YUmabMAoJQ1e7j-WwSDIdLnvQHy7hI6wUMtJwzI5teA3Q9TUWKYpRXsp4Z7lADLBiZ_rM8xT_uKIJkET2fUDE1DpRjBDTRk7iJ0vwfsqp26EHoPEHK6nYPkVD8V97cOQ24Y2pwogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007137e607.mp4?token=cSN_nc_pWUMQv7aXd6KjqZzt1cNEf65HSuhZl8kad9IUbN-5_AxSgkmlyNKAOQZyEoWBzF_WPBwEsgXIVbKcyOcRBHpsKSh0ZyCULu3HOPeC7osxU2iHZLoELlJR4RYhRA-81HlxluG6_DTlRC9dJtuL8p1JTpXPVy_c3l7pJ28msskIcPEeKAoJwIVcJANuBa54Omei3kZW0YUmabMAoJQ1e7j-WwSDIdLnvQHy7hI6wUMtJwzI5teA3Q9TUWKYpRXsp4Z7lADLBiZ_rM8xT_uKIJkET2fUDE1DpRjBDTRk7iJ0vwfsqp26EHoPEHK6nYPkVD8V97cOQ24Y2pwogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به بریتانیا: کشور شما خوب پیش نمی‌رود.
🔴
فراموش نکنید که درصد بالایی از نفت خود را از تنگه هرمز دریافت می‌کنید.
🔴
و شما برای کمک به من آنجا نبودید. کشور شما برای کمک به من آنجا نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145444" target="_blank">📅 20:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbA29adbTby555X3FUlSn9j45B9T_1hpHV2vEvC0W-cyoBceu4fbMT-tkgWuuBcn7YNbNL4EQiNYoI9EmiH5XOUoHfRG284PQythgsZfAEWHhzKRL1V-m5nn-FsxQu7MSm79AGLT4prOT-nFsT7ab4wvL2Dx5Zvqp7eB_2Ep1DWd3l6b5PuU3VUUyH4jTQEIBlFXTJDQy7v34tQX-geSqUDK70rRfuIiswptX-qGuBWlWn9MG-XmlYl2gJFc6dyQXkgRy5grLkcUBbVbqV_O2SXsawNXh6LtgXba6rPpdLc-Y_vMft4u3DllqI3R5DhXM0NA73O5RUJ45YjmX9L-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف خطاب به وزیر خزانه‌داری آمریکا: «قیمت نفت آتی عمان، بازده اوراق قرضه دولت امریکا و میزان ذخایر استراتژیک نفت را خوب تماشا کن.
🔴
قهرمان! هرچی زور داری بزن که در قیمت نفت آتی بیشتر مداخله کنی! چون کل حرفهٔ تو به این بستگی دارد. یا اینکه به تخلیه نفت از ذخایر استراتژیک بیشتر از حد خطرناک ادامه بده و سقوط غارهای نمکی ذخیرهٔ نفت در اثر کاهش شدید ذخایر را تماشا کن، یا به خداهای نمک تگزاس پناه ببر و دعا کن که چاه‌های ذخیره سقوط نکنند. دنیا پاپ کورن خریده و تو را تماشا می‌کند»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/145443" target="_blank">📅 20:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کانال ۱۴ عبری مدعی شده سطح آمادگی و هوشیاری در داخل اسرائیل به‌طور محسوسی افزایش یافته است.
🔴
به گفته این رسانه، این وضعیت در پی نگرانی‌ها از احتمال ازسرگیری درگیری نظامی مستقیم با ایران ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/145442" target="_blank">📅 20:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سپاه اعلام کرد که هفت نفر را که ارتباط با گروه‌های کرد در استان ایلام در شمال غربی کشور داشتند، دستگیر کرده است؛ این افراد در حال برنامه‌ریزی برای عملیات‌های مسلحانه و حمل مهمات بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/145441" target="_blank">📅 20:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نیویورک پست: عمان به طور پنهانی پیشنهاد ایران برای دریافت هزینه از تنگه هرمز را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/145440" target="_blank">📅 20:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هم اکنون حمله اسرائیل به حومه دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/145439" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به گزارش بی‌بی‌سی، دونالد ترامپ تلویحاً اعلام کرده است که آمریکا ممکن است در مناقشه بر سر جزایر فالکلند از بریتانیا حمایت نکند.
🔴
ترامپ این موضع را به عدم حمایت لندن از آمریکا در جنگ با ایران مرتبط دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/145438" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل گزارش داد، «اسرائیل کاتس» وزیر جنگ این اسرائیل، با حضور «ایال زمیر» رئیس ستاد کل ارتش و شماری از مقام‌های ارشد نظامی، نشستی امنیتی برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/145437" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
روزنامه فایننشال‌تایمز گزارش داد بازار بیمه لویدز لندن انتظار دارد خسارت‌های ناشی از جنگ آمریکا و ایران در کشورهای خلیج فارس به حدود ۱.۴ میلیارد پوند برسد.
🔴
مدیرعامل لویدز گفت برخلاف حملات به کشتی‌ها در تنگه هرمز، بخش عمده این خسارت‌ها ناشی از آسیب به زیرساخت‌های زمینی است. از جمله، شرکت سعودی سابک در پی آسیب یک مجتمع پتروشیمی در حمله موشکی، در آستانه ثبت مطالبه‌ای حدود ۸۰۰ میلیون دلاری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145436" target="_blank">📅 20:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نتانیاهو بار دیگر تاکید کرد : "ما اطمینان داریم که قادر به سرنگونی نظام ایرانی هستیم. این وظیفه اصلی است و به زودی به انجام خواهد رسید."
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/145435" target="_blank">📅 19:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=Jh18z_4WNKl-V5v-kQWLry7tC3Rl3Hv7hf97KwIeoUaG9G5xvzQhRt8AItKYYmXWJ2Y_MOU6Agy4fMlqWDhWnZaA2Hp6rHKcuDMIFz_iPyVlBa02nitDQpZJOmCZawzQY7uH1dkcx37BjIZl_m-9u8iNACB9VsHeUGI_H1NESUb3UAPpjoBOZmiCJoJSGqQ2aL-4CAQCjGrJrxBJ149yW6B_UvaxHtQG8EpTbgHKPj1Oz33i1Zvntc5CuaghKWQsCBnYevfZBPmZeZwkPtDkH2EUXGURlK-TvAtaxierhSW5pbVG8gHxyjpymw4dtsiixcsrMD1yhR3dfgHW8KHpYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d448ff03.mp4?token=Jh18z_4WNKl-V5v-kQWLry7tC3Rl3Hv7hf97KwIeoUaG9G5xvzQhRt8AItKYYmXWJ2Y_MOU6Agy4fMlqWDhWnZaA2Hp6rHKcuDMIFz_iPyVlBa02nitDQpZJOmCZawzQY7uH1dkcx37BjIZl_m-9u8iNACB9VsHeUGI_H1NESUb3UAPpjoBOZmiCJoJSGqQ2aL-4CAQCjGrJrxBJ149yW6B_UvaxHtQG8EpTbgHKPj1Oz33i1Zvntc5CuaghKWQsCBnYevfZBPmZeZwkPtDkH2EUXGURlK-TvAtaxierhSW5pbVG8gHxyjpymw4dtsiixcsrMD1yhR3dfgHW8KHpYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا، مارک کارنی
:
ما از آنچه پیشنهاد شد یا از دوام آنچه ارائه گردید راضی نبودیم.
🔴
ما نمی‌خواهیم در کوتاه‌مدت به دستاوردهایی برسیم که چند ماه یا یک سال بعد از ما گرفته شوند.
🔴
این امر برای کارگران ما، شرکت‌های ما و جوامع ما منصفانه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/145434" target="_blank">📅 19:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
برنامه های هوش مصنوعی ChatGPT و Claude و Grok‌ و Gemini به دلایل نامعلومی از کار افتاده است.
🔴
تمام هوش مصنوعی های آمریکایی از کار افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/145433" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مدیرکل فرودگاه بین‌المللی قشم از برقراری دوباره پروازهای مسیر دبی ـ قشم ـ دبی پس از ۶ ماه توقف خبر داد و گفت: نخستین پرواز این مسیر با یک فروند هواپیمای ایرباس A320 روز سه‌شنبه ۱۷ شهریورماه انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/145432" target="_blank">📅 19:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
به گزارش سی‌بی‌اس نیوز، چند مقام ارشد آمریکایی گفته‌اند پیت هگست، وزیر دفاع آمریکا، در گفت‌وگو با افراد نزدیک به خود از شان پارنل به‌عنوان گزینه اصلی‌اش برای تصدی سمت وزیر ارتش یاد کرده است.
🔴
بر اساس این گزارش، پارنل در حال حاضر انتخاب مورد ترجیح هگست برای این سمت به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145431" target="_blank">📅 19:35 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
