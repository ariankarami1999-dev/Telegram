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
<img src="https://cdn4.telesco.pe/file/MsfGKxPucBbE4jpfY9X16yL8FQ5n6TGcND3qN0GOFTl1zRqAo3yps14AhyU6CHLmMhIdJZsPc0iiuTH0Q9UcxrEUXp4hu_aQCiYM_GsOUUim9FoJ6X3wAlkLqBmec62g3V36xiQJC8-iXhrZnLwpy4zoMndgnUrlEM8F-hD8M2epZqb6HKVw2MY6T1mCLzRIIDyrtPEhibvvvoAbEAgrSeW1tv31aID3QIn-Iwpe1gtFg01P03PuFjdEZeadwHnQcS4UQy3MxNNHXyO1Q7Y0t7_5fBm8ktF470-XsJv0tvAA7eho4BY5uRi64600PlBVbmxflyR8YwWHFOV4Rrz4QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 332K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 02:27:07</div>
<hr>

<div class="tg-post" id="msg-16027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صداوسیما : جزئیات عملیات امشب رزمندگان نیروی دریایی سپاه علیه متجاوزان آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/withyashar/16027" target="_blank">📅 02:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16026">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صداوسیما:  شناورهایی قصد داشتند از مسیرهای غیرقانونی و ناایمن جنوب تنگه هرمز عبور کنند که نیروی دریایی سپاه پاسداران با آن‌ها برخورد کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/withyashar/16026" target="_blank">📅 02:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16025">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وال‌استریت ژورنال : یک پهپاد ایرانی به نفتکشی حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز اصابت کرد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/withyashar/16025" target="_blank">📅 02:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16024">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/16024" target="_blank">📅 02:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16023">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">https://t.me/boost/withyashar
این بوستو بترکونین ایموجی اضافه کنم
😕</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/16023" target="_blank">📅 02:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16022">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇭🇷
کرواسی 1
🇬🇭
غنا 0  پایان نیمه ی اول @withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/16022" target="_blank">📅 02:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16021">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/16021" target="_blank">📅 02:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16020">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اهدافی که توسط آمریکایی‌ها مورد حمله قرار گرفته است.
دکل مخابراتی
پدافند هوایی
سایت های کروز
سایت های پهپادی
توانمندی مین ریزی دریایی
@withyashar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/16020" target="_blank">📅 02:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16019">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/16019" target="_blank">📅 02:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16018">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شب حمله
💥
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/16018" target="_blank">📅 01:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16017">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هم اکنون از مهرآباد جنگنده بلند شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/withyashar/16017" target="_blank">📅 01:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16016">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی: حملات امشب آمریکا به اهداف ایرانی تکمیل شده است
@withyashar</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/16016" target="_blank">📅 01:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16015">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">همزمان با حملات و تایید سنتکام بیتکوین دوباره اومد زیر ۶۰،۰۰۰$
@withyashar</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/16015" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16014">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری مهر: شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@withyashar</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/16014" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16013">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه سر باید برم بیت رهبری
😂
الانه که موتور بزنم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/16013" target="_blank">📅 01:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16012">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC91IyXkzzyNU2eV6ZYw17hOkWlRZVE30nnCGIvf22Hyo__Dv0SuKjqMoLTV6QHaGKrFcCzftiP72R5i6qmOhWjpwMvQuTUgMEYsh7O14KdJZL0zQqBTAOZTpgGkZ6seJw94sJOFDY-mDqusO5co79jqYjmQw9GRrO3gtYAS_k4aC97fUb4oT8o58eEjcWaXnf39-qlJQn0S7vFyN05PYW5KtELU-7HwBQ7qvrAMfQIT0YUyTN-sStdnefhDfl5BzeQaaw3QJUVUv9Cv9WhPhlp2lDcupXMPf_oFXVoA82-OXWKP7GspxiSdNH7WbqBAm6grkPse0CDxG8xNoNkCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ، حضور نُه هواپیمای سوخت‌رسان آمریکایی در محدوده خلیج فارس و کمی دیگر ملحق شدن دهمی از اسرائیل به آنها
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/withyashar/16012" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صدای پهپاد و هلیکوپتر در قشم همراه با یک انفجار‌ جدید
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/16011" target="_blank">📅 01:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16010">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس نیوز : حمله فعلی آمریکا به ایران بزرگ‌تر از حمله دیشب است.
نیروهای آمریکا و بحرین ۹ پهپاد ایرانی را که به سمت نیروهای آمریکایی در بحرین پرتاب شده بودند، سرنگون کردند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/16010" target="_blank">📅 01:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16009">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/16009" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16008">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اتاق جنگ با یاشار : انفجار های جدید در‌ سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/16008" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16007">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتاق جنگ با یاشار : انفجار های جدید در‌ سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/16007" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNS4</strong></div>
<div class="tg-text">سیریک خیلی بد صدای انفجار میاد</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/16006" target="_blank">📅 01:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">هیچ شبی مثل امشب نزده.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/16005" target="_blank">📅 01:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16003">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZtEI9B9gPpW-MgxjZnoDXmEtHu4pSeDnH6Z3POfalWAjEq1Giev9kFSKOPAXreRavKlUCT2neGph_OJqrl2a5X-EMHIWYth4Ocqk2pmASlXjtQfBuk5v3ztR-Rg4TUu0HXLjjjFgoPirZGQ43Tx5gkL4r9L6_hMRJgQEIILMH4gqjDoCtsHylsSXTSzT0Hl211kRSLUYMjxvWVLNXAmZMdr9dkqVyFTEEt9nEZhWPuozUGmXPj1Uh8Sgw4X4AI2oB9M85Uk5iNg8VPZyse-HMud0B5hFG9UqFxlPGPqs-JNePlOStmfPjEKPhb6MQOOBrhjuVdEQml327duJwldrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای آمریکا پس از حمله اخیر ایران به یک کشتی تجاری، حملات بیشتری انجام دادند
فرماندهی مرکزی ایالات متحده (سنتکام)
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۲۷ ژوئن به دستور فرمانده کل قوا، حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی «M/V Ever Lovely»، به ایران فرصت داده شد که به توافق آتش‌بس پایبند بماند، اما این کشور از این کار خودداری کرد و نیروهایش یک پهپاد تهاجمی یک‌طرفه را صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به کشتی «M/T Kiku» شلیک کردند. این نفتکش با پرچم پاناما در حال عبور در نزدیکی تنگه هرمز و حامل بیش از دو میلیون بشکه نفت خام بود.
در پاسخ مستقیم به ادامه اقدامات ایران علیه کشتیرانی تجاری، نیروهای سنتکام امروز حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های شناسایی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، مراکز نگهداری پهپاد و توانایی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز همچنان ادامه دارد. نیروهای آمریکا در حالت آماده‌باش، تهاجمی و کاملاً هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/16003" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16002">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">سیریک رو چرا نمیگی بخدا نزدیک بود پنجره اتاق بریزه رو سرم</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/withyashar/16002" target="_blank">📅 01:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16001">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجار دوم در قشم اطراف فرودگاه
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/16001" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16000">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromₕₒₛₑᵢₙ</strong></div>
<div class="tg-text">خدایا یا من پولدار شم یا اتش بس نقض بشه امشب</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/16000" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15999">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدای انفجار در قشم
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/withyashar/15999" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">باراک راوید، خبرنگار نزدیک به ترامپ: مقامات آمریکایی حمله به تنگه هرمز رو تایید کردن و آمریکا رسما مسئولیت حمله رو به عهده گرفته است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/15998" target="_blank">📅 01:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15997">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">صداوسیمای ایران به نقل از یک منبع آگاه نظامی این کشور گزارش داد صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/15997" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15996">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش‌ها از شنیده شدن صدای هلیکوپتر در قشم ایران
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/15996" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15995">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دکل مخابراتی سیریک مورد اصابت قرار گرفت
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/15995" target="_blank">📅 01:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آکسیوس : ارتش آمریکا تو منطقه تنگه هرمز حملاتی انجام می‌ده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/withyashar/15994" target="_blank">📅 01:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15993">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش مردمی تایید نشده : چند تا انفجار بندر لنگه از سمت نیروی دریایی سپاه
@withyashar</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/withyashar/15993" target="_blank">📅 01:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15992">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCaptain</strong></div>
<div class="tg-text">پولدارا کوشن یه گونی استارز ول کنن رو چنل
😅</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/15992" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرنگار صداوسیما زنده از سیریک:
دقایقی پیش صدای چندتا انفجار مهیب از حوالی روستای طاهرویی سیریک شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/15991" target="_blank">📅 01:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15990">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش مردمی : یکی طرف گز سیریک بود یکی دریابانی سیریک یکی هم طاهرویی
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/15990" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15989">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش مردمی‌تایید نشده : شهرک صنعتی سرخور طاعرویی رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/15989" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مثل همیشه دقیقا ۱۵ دقیقه جلو هستیم !
💥
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/15988" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صداوسیما: صدای انفجار در سیریک شنیده شد
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/15987" target="_blank">📅 00:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15986">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای پهباد در قشم
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/15986" target="_blank">📅 00:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان از سیریک ، قشم و بندر لنگه گزارش ۳-۶ صدای‌انفجار‌شدید
میدند !!!!
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/15985" target="_blank">📅 00:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
۳ انفجار
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/15984" target="_blank">📅 00:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ امضای توافق با اسرائیل را به رئیس‌جمهور لبنان تبریک گفت
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/15983" target="_blank">📅 00:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فارس: کلیه خاموشی‌های شرق تهران برطرف شد
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/15982" target="_blank">📅 00:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو: توافق با لبنان ضربه ای به ایران و محور آن است
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15981" target="_blank">📅 23:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیانیه مجلس خبرگان رهبری:
بنابه‌نظر مجتبی خامنه‌ای، موضوع هسته‌ای نباید سرش مذاکره بشه.
باز شدن تنگه هرمز، خلاف تعهد مسئولان بوده.
«تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» از مطالبات رهبره و «هرگونه سهل انگاری در این زمینه» با واکنش مواجه میشه.
«بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
@withyashar</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/15980" target="_blank">📅 23:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فکر کنم تنگه دعوا شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/15979" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سردار حسن‌زاده:  در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/15978" target="_blank">📅 23:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فکر کنم تنگه دعوا شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/15977" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9aaef7b78.mp4?token=BuRwH_ykn6dtNgJiV0ypbeBs_Y5CgPJtU3aGfqbebbflNfKdpJif-t7abeGzzijh0G9MlzGIQfBbgJ4RPsj8kXt9Ff9yjpGvycmfHjq1l0d2ueqljE5_DrZyK2TYcHB02CdgIhq7LfXLRZjfxFedz0xsMTT-jiXNCEauokft2oDWHKv1Jofc_67a_UCb7XZZcszvrOB6XJnOWBqZeWMeoME50tYrSs_tzGPtTuaki6Wgp-gEcs4Du1MWS6EsDz6RI5V_prE5ngHREIMzDdJuZWHFTeMnqy1tytrpALVboozqNnKpWY3UExu5omcndUhQWaYWfnP6hnC4oitjh1w-Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9aaef7b78.mp4?token=BuRwH_ykn6dtNgJiV0ypbeBs_Y5CgPJtU3aGfqbebbflNfKdpJif-t7abeGzzijh0G9MlzGIQfBbgJ4RPsj8kXt9Ff9yjpGvycmfHjq1l0d2ueqljE5_DrZyK2TYcHB02CdgIhq7LfXLRZjfxFedz0xsMTT-jiXNCEauokft2oDWHKv1Jofc_67a_UCb7XZZcszvrOB6XJnOWBqZeWMeoME50tYrSs_tzGPtTuaki6Wgp-gEcs4Du1MWS6EsDz6RI5V_prE5ngHREIMzDdJuZWHFTeMnqy1tytrpALVboozqNnKpWY3UExu5omcndUhQWaYWfnP6hnC4oitjh1w-Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف : اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه. @withyashar عرزشی
🤣</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15976" target="_blank">📅 23:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قالیباف : اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه.
@withyashar
عرزشی
🤣</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/withyashar/15975" target="_blank">📅 22:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فارس : کیفر خواست رضا پهلوی و چندتا از عوامل منوتو و اینترنشنال صادر شده به جرم دست داشتن در اتفاقات دی ماه و باید برن دادگاه
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/15974" target="_blank">📅 22:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ونس: قیمت نفت الان به ۷۳ دلار در هر بشکه بازگشته، در حالی که تا ۱۲۶ دلار رسیده بود؛ این نشانه‌ای است که یک اتفاق واقعی دارد می‌افتد
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15973" target="_blank">📅 22:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ead84832.mp4?token=BvaqePfzr-qe4DAVatIQe82R2snYqrSl15K0gr_KtuDQMA6EqjA9Ty5SxbBI6SRnxrKgWkYgXHoAgWkioHZaFrGh1tr_v0nBBQLzacYfpYIG0RAgchrmgjw4HBAGnwslJYq4Tk_TTHIOYLZQyQtrR--p61r8SKt5-DNpzv5P0ppdZlhfTXdNfsLn_Cav_RCM6Nyl0juLCubiFoO8Pl-sx1E4nOQvfkibVw63iM0VT9D7Imw_1i9-3mKPgnHBXfrWuQctw3p6Zwit6Su_9Og-7SEOOPLHqc-nPhWbxdNlsQx_Z7EaEqH_d5IUUVZwU2nyvZJRO_cbpBOsvg_rVXywKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ead84832.mp4?token=BvaqePfzr-qe4DAVatIQe82R2snYqrSl15K0gr_KtuDQMA6EqjA9Ty5SxbBI6SRnxrKgWkYgXHoAgWkioHZaFrGh1tr_v0nBBQLzacYfpYIG0RAgchrmgjw4HBAGnwslJYq4Tk_TTHIOYLZQyQtrR--p61r8SKt5-DNpzv5P0ppdZlhfTXdNfsLn_Cav_RCM6Nyl0juLCubiFoO8Pl-sx1E4nOQvfkibVw63iM0VT9D7Imw_1i9-3mKPgnHBXfrWuQctw3p6Zwit6Su_9Og-7SEOOPLHqc-nPhWbxdNlsQx_Z7EaEqH_d5IUUVZwU2nyvZJRO_cbpBOsvg_rVXywKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر کانال صعودی بشکند، در پولبک، ما میتوانیم قهرمان شویم.
@withyashar
😂</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/15972" target="_blank">📅 22:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15971">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4f5549fd.mp4?token=e26op9L9a7SbXrKGj5MorHz0Fa3zb7SrMjaNffocOrW7FPeBJ77A6PbaTpH-bK2K9PdpLELalVxQzos8a_Hjjot-24cg71LQq5Ja6fW-S_HXhQRp4cmYeXmoOxIArSm-MAeu861yFwfR3CNhATw7j8gqoqSijwBiK2U3j6GbKg2t11yaCoEtxUsTJ_PwkHfCUO2O5xSIVMBVtZj0GXYJh1xdJxa-PjYnsNaIF3DIiCUBEk5pz_qwzs6JCr1yqL4zuFoIiYrRfMTg31eHRS6IcNDIXw8Y4QNNXsYeX0y27_aWqaWXUs4Ugl1kHuvdgHrmvf1c71iDBd6bufjLptYxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4f5549fd.mp4?token=e26op9L9a7SbXrKGj5MorHz0Fa3zb7SrMjaNffocOrW7FPeBJ77A6PbaTpH-bK2K9PdpLELalVxQzos8a_Hjjot-24cg71LQq5Ja6fW-S_HXhQRp4cmYeXmoOxIArSm-MAeu861yFwfR3CNhATw7j8gqoqSijwBiK2U3j6GbKg2t11yaCoEtxUsTJ_PwkHfCUO2O5xSIVMBVtZj0GXYJh1xdJxa-PjYnsNaIF3DIiCUBEk5pz_qwzs6JCr1yqL4zuFoIiYrRfMTg31eHRS6IcNDIXw8Y4QNNXsYeX0y27_aWqaWXUs4Ugl1kHuvdgHrmvf1c71iDBd6bufjLptYxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا بیت‌کوین در آستانه تکرار ریزش ۲۰۲۲ است؟
تورم آمریکا دوباره در حال افزایش است و احتمال رشد نرخ بهره بیشتر شده؛ اتفاقی که در گذشته فشار سنگینی به بازار کریپتو وارد کرد.
برخی تحلیلگران هشدار می‌دهند اگر فدرال رزرو دوباره سیاست‌های انقباضی را تشدید کند، بیت‌کوین می‌تواند وارد فاز اصلاح عمیق‌تری شود.
هفته‌های آینده برای بازار بسیار مهم خواهد بود.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15971" target="_blank">📅 22:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15970">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش هایی از فعالیت پدافند بوشهر
@withyashar
🚨</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/15970" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو:ما محور دیپلماتیک جمهوری اسلامی را می‌شکنیم.
ما توانستیم به این چارچوب تفاهم‌ها برسیم به یک دلیل ساده: چون به حزب‌الله ضربه سختی زدیم.
و حزب‌الله که انتظار کمک از ایران داشت، آن را دریافت نکرد.
می‌خواهم به شما یادآوری کنم که در لبنان چه بود،حزب‌الله 150 هزار موشک و راکت داشت و ما حدود 90 درصد از این انبار عظیم را از بین بردیم
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/15969" target="_blank">📅 21:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">افشاگری کواکبیان، نماینده سابق مجلس:
مسئولی گفت کاری می‌کنیم اسرائیل دوباره حمله کند تا مردم بیایند پشت نظام
@withyashar</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/15968" target="_blank">📅 21:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو درباره لبنان:
اسرائیل همچنان در منطقه امنیتی زرد باقی می‌ماند که ما را در امان نگه می‌دارد. و این یک دستاورد بزرگ است. عظیم!
چون آنها چه کاری سعی کردند انجام دهند؟ آنها سعی کردند ما را از طریق انواع ابزارها، انواع فشارها از آنجا بیرون کنند. و البته، این اتفاق نیفتاد.
من از رئیس جمهور ترامپ و وزیر امور خارجه روبیو به خاطر مشارکت و سهمشان تشکر می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15967" target="_blank">📅 21:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">https://x.com/yasharrapfa?s=11
تویت جدیدم در اکس ، واقعا برام سوأل شده…</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15966" target="_blank">📅 21:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسرائیل معتقد است که حزب‌الله ممکن است ظرف چند روز آینده در پاسخ به توافق چارچوب اسرائیل-لبنان، حملاتی علیه نیروهای دفاعی اسرائیل انجام دهد، طبق گزارش ینت.
اسرائیل برای احتمال تشدید در بخش شمالی آماده می‌شود و اضافه کرده است که انتظار نمی‌رود حزب‌الله «بی‌حرکت بنشیند.»
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15965" target="_blank">📅 21:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سازمان پخش اسرائیل به نقل از منابع:
ارتش اسرائیل خود را برای عقب‌نشینی از دو منطقه آزمایشی در جنوب لبنان در فردا آماده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15964" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برق در بیشتر مناطق تهران رفته
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15963" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">منابع محلی گزارش دادند ارتش اسرائیل عملیات انفجار گسترده‌ای را در شمال شهر رفح در جنوب نوار غزه اجرا کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15962" target="_blank">📅 20:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg6zxT6Z2dVUy-L-sdlhCURlNgRJpaZO78Vwv7CKqXkJRMhVdF1vYoCTPt8R4A3u2RqwibaD8JpD1bytpbCrpDMFsIWLYtigeg9r6mXiUoxfrklASMrlgVpDTAfEp9RbwU0u3o5vOo7WzWyUI6Vga5V7SNQl0jTCehAI-kfflxEqwyHmxSNej-_2z379nwvF45CSDCZMoHLCJrnAtHbu4Y2Oy6HLS1E8Zq4GRsdWz0aV6iqEsA0RaJTJb6LTplNrGrI9chltGw0yDDxhlsoAh6nLwyxMYVoCl7FgPLStcfDDw9EimgibcMfFAhLH0A7pw3ITnq8Z9UW_P_74Cnrd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث :
گویا طلبکارم هست حتما یعنی بار کل دنیا رو دوش خودش و آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15961" target="_blank">📅 20:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8a55c1168.mp4?token=PKRQhJfw4aQuC5ao8AMVrqX8rWBiMxHYibxcFr4sf-p4Hj1fZPLh3z4aS7KnpMTxbtAEBl1e57Iib76urTmJ62oQTiJ5BQDM58biJqCkybVkf_A50szm1n-IKohvCqDF5Ty-pZNi5O2B0Ulx-xI3HFEo5NMnzrWJLkLzn71DLVPqxbua-ozWgOolNUtXDsUZDLKgJEQKGkq9uPPPolr2aMldmMGQRHxrVACcLJasi-RH2DzjhRIrcZyF9EPRAyJZk_GcYVWTpzGMOZ7o8FGMMBvHKXZM5GxiH5CfWUjZOFaPV1j_7KOLe5g4E_LRv9YmOY9ZcZGGfiRxBtLkb_8Q8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8a55c1168.mp4?token=PKRQhJfw4aQuC5ao8AMVrqX8rWBiMxHYibxcFr4sf-p4Hj1fZPLh3z4aS7KnpMTxbtAEBl1e57Iib76urTmJ62oQTiJ5BQDM58biJqCkybVkf_A50szm1n-IKohvCqDF5Ty-pZNi5O2B0Ulx-xI3HFEo5NMnzrWJLkLzn71DLVPqxbua-ozWgOolNUtXDsUZDLKgJEQKGkq9uPPPolr2aMldmMGQRHxrVACcLJasi-RH2DzjhRIrcZyF9EPRAyJZk_GcYVWTpzGMOZ7o8FGMMBvHKXZM5GxiH5CfWUjZOFaPV1j_7KOLe5g4E_LRv9YmOY9ZcZGGfiRxBtLkb_8Q8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر هوایی از تهران ساعتی‌ پیش
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15960" target="_blank">📅 19:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15959">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مظفری مسئول مراسم خامنه‌ای: احتمالا تشییع جنازه هوایی انجام میشه
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15959" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15958">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از یک مقام آمریکایی: دو پهپاد ایرانی بحرین را هدف قرار دادند. یکی از آن‌ها رهگیری و منهدم شد و دیگری در منطقه‌ای دورافتاده در محدوده فرودگاه سقوط کرد. همچنین یک پهپاد دیگر یک نفتکش حامل دو میلیون بشکه نفت را در نزدیکی تنگه هرمز هدف قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15958" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c803f6a313.mp4?token=S0yAIrf2q6GE0WOA47e2RePYgZIAeKn9J4jlAPREKd8BTQw6HC0ZfkP2sxnAllAJFLyQvRAZv7twcz9xVpXDPeKpXnyDTA1gTKR45_agoRZnlTKXXoLEsDSsz0uS5CKlgzHtjz-rZqZjTy3EyjM9b5_j4KosCF9cIqujqfI3pnWHkgUQNG8-ATdZRLR4ft9AP7AP70mvJwoEXegmJJjrjntc0LsIccHHt13NcMHdZTJkfz0XNHmHQelg-gDmQq8tdYr2RshBsfWsYFQLF0a-kqcLAMNhxhcM2KAkPFgTufOZ5me20py3aa9Z5OZmED4tua3bghfRCQ1cxo4UHww7xU8SLambh40sbo78vc8geCVF2YIpO0V6OgLKMMphRw7R6lNFv0It3LZU1d4kItX7xQPkVgX1PPB5da3j6KzLFYik8ElBCavzqzI6QDW_F8ESwya0nWTtbE_wAY9k-h--HFCHGnUg3kXW1711biOhQVvIvBxm09KHQgCKAuFVhtQwdtctPVahxcKu_uCriBKON1jj61lPD9ZuXv-Po3-FmFn7RFkU1T5eJ9joJKIP9my0GTcq5UcbKCI-yqQ5YeIxW-FvNE2povGzlWRuo-x1CR4S04Seh7r-H6PoyCsgqtI7m0lHyvJHQkkBTXjkHxJGgpz4VqepjXWFaSgun6bfeEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c803f6a313.mp4?token=S0yAIrf2q6GE0WOA47e2RePYgZIAeKn9J4jlAPREKd8BTQw6HC0ZfkP2sxnAllAJFLyQvRAZv7twcz9xVpXDPeKpXnyDTA1gTKR45_agoRZnlTKXXoLEsDSsz0uS5CKlgzHtjz-rZqZjTy3EyjM9b5_j4KosCF9cIqujqfI3pnWHkgUQNG8-ATdZRLR4ft9AP7AP70mvJwoEXegmJJjrjntc0LsIccHHt13NcMHdZTJkfz0XNHmHQelg-gDmQq8tdYr2RshBsfWsYFQLF0a-kqcLAMNhxhcM2KAkPFgTufOZ5me20py3aa9Z5OZmED4tua3bghfRCQ1cxo4UHww7xU8SLambh40sbo78vc8geCVF2YIpO0V6OgLKMMphRw7R6lNFv0It3LZU1d4kItX7xQPkVgX1PPB5da3j6KzLFYik8ElBCavzqzI6QDW_F8ESwya0nWTtbE_wAY9k-h--HFCHGnUg3kXW1711biOhQVvIvBxm09KHQgCKAuFVhtQwdtctPVahxcKu_uCriBKON1jj61lPD9ZuXv-Po3-FmFn7RFkU1T5eJ9joJKIP9my0GTcq5UcbKCI-yqQ5YeIxW-FvNE2povGzlWRuo-x1CR4S04Seh7r-H6PoyCsgqtI7m0lHyvJHQkkBTXjkHxJGgpz4VqepjXWFaSgun6bfeEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و صد افسوس…
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15957" target="_blank">📅 18:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15956">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد ، توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/15956" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15955">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc1i7-zAhIGe_dJ55aTTvNQBYFIJfEnXjEHwtqlStsziQrsPYMXi489A9o7Y1p-BzsHSvWuwDdSFkgwFq3A-QkIVkwRKHVjoh6spkrTkHpYFsBnwzYWyiXVHZs51JYHe8KDa7wYqX-WP-zy9DJBERsdCnsvZ_H5oH3m1S9ezkuRCV_frAzVoKk-Lye7Hk4u1hV3f4lCe4FnMIZlN4hc7g9cNoZzz-d36rOm-CfO4d8VD8I2PibihE-ZonA-dTIGC9_boSaWbC8KZ82ch_Osi_c0_lnh3TMAx2-JySVgKTullrHuOtbvZMx_-xEHJW-2vfQ-sWX16Exj2Z0VzOkSRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل آفساید شجاع : شجاع خلیل زاده اولین بازیکن تاریخ جام جهانیه که بخاطر شادی گل نزده،کارت زرد گرفت @withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15955" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15954">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">علیرضا حقیر(دبیر) :عامل اصلی خوب نتیجه نگرفتن تیم ملی فوتبال ایرانی‌ها خارج از کشور بودن که باید ادب بشن.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/15954" target="_blank">📅 17:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15953">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15953" target="_blank">📅 17:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-wQiLrufTALtA_UYWWtpND_MUuAN-ZTHUJZsyfz-_pBVBKHaZT5Xo3DHSxru1vpFgS_oRaS7j85TGzhcFeFPzmjaYycj8cANjGDCO0UhpGglNSF7vnhxTFk57S1joslL1aEZ1UjAPzE8EJUEg-a8NT-OGccKSVC6YbNDd8PaRNBjhSqn_PNmmVtHsTWvcwy5MMV1nEeIIt09_x9asMP1O07DclIOxBDMtUTApvQbHcJZURbYL-f5h0sWZhrfpqIba9jYjpxXi4gxKyLjZjhdqyve-hKITl2ra-JN2f7uPyPEk63nsMc9xDGZ2atvU3Hf4AmibZrYA8nGhrfbC5yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده @withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15952" target="_blank">📅 17:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBPmCgVOtsduxr_uT2BimGII4sJ7oSlMNx2edbhibpfGjn2QjwblKeaTf2rcbwYcPOpcwI8i___7-LU5J4Z9fGCJ6baMqYj7YGb91Mdu1gT7veVG5X7FHaqrJThiLAAotdC2ko4jRts5NabWZijCOpI2d0wtH2JGaDCmrjRiDbF1TkPjGIZxtOWRhRXAHgIS7YMqQwfm8S6XOIvuNy0P9qzxiWJgTE9UMMRJsErUX5L_6bM96cGuAkY9U83he7bX3vFd6Oa1Y_o0mhRv3PJkW_aE6cnrR3TGebfykgKlx-FflSdApu3WSfWhUzqof7tKnGUPaSezS3g3ujrXrKmU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پر ریزون الان کرج !! ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15951" target="_blank">📅 17:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/15950" target="_blank">📅 17:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15949">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سازمان دریایی بریتانیا: یک نفتکش در تنگه هرمز مورد حمله یک پرتابه ناشناس قرار گرفته است @withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15949" target="_blank">📅 17:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6530513224.mp4?token=IIU1bxySOjIlJzHZIhmqlyq_c6toFznUVHXNqmgLsCKQxaMeMJc7tmRyLHAUM8ZbLZSypXgOZ9yf6u1mmMAClqPTYFq0CLWM8qH2I5fo3OMtO5yQVj0St0aXx2QeiLWAA6QGWeqdzZ60BDhA5ZgHUgZJ2fru3er0b53ZtlyxOZU8dfpBwvKPC6GVAAVzRMFW1HOb3IT1JQM5myJNmMvmYEPYmPjJouaPV4oHesTZWhfxInCTVKqcJHaA_gaQgguxbP0TINB8XuSVwXBm-TlbsjxxvthLkOSCs20o1uKBl_q9dEHj8_tt33s7gxwlDMqjI57YRiDQxaex06cvjxdVqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6530513224.mp4?token=IIU1bxySOjIlJzHZIhmqlyq_c6toFznUVHXNqmgLsCKQxaMeMJc7tmRyLHAUM8ZbLZSypXgOZ9yf6u1mmMAClqPTYFq0CLWM8qH2I5fo3OMtO5yQVj0St0aXx2QeiLWAA6QGWeqdzZ60BDhA5ZgHUgZJ2fru3er0b53ZtlyxOZU8dfpBwvKPC6GVAAVzRMFW1HOb3IT1JQM5myJNmMvmYEPYmPjJouaPV4oHesTZWhfxInCTVKqcJHaA_gaQgguxbP0TINB8XuSVwXBm-TlbsjxxvthLkOSCs20o1uKBl_q9dEHj8_tt33s7gxwlDMqjI57YRiDQxaex06cvjxdVqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت پر ریزون الان کرج !!
ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/15948" target="_blank">📅 16:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15946">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL2r0V4xOXAHDUdURUPG5ipB2XUowiPC5X5NyEJ8Nk8LQoMz6Ap9YgwkZg6f4mO63hyZLzEZR4VL4j6LSRuuE9b4SgSYb1jXruKQz6D8Vqu1XFG7zbaII66RNPspJm5pRf6-mmLz3yKDb9hBVXk-LtDa5adIdlNHdRg3vHz5VGRkQvt_ql_87DKa6vmGaQy8563Kfz2XIOeDuNj-I-olqWFb9QGwNSOttufBrwI43cSeWY3NkbZq90-hPxvWbB8Gja7rxlB28GmDPj3TIEBtB0s-NUNvB_o09UjgYCIWb5NKKjcxBYIdSCJKoxMiSYDuHnnjSvVdxU1glhmqp44XYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=Jr1OTBOVLdGRXeYxgeYIkC2tC6Njipb2BzqygsK7Rwh7Vc_Kw4wf_q1-jBhpb_Zw7AYHBHJYkJo8iPk0Mdu_CF1zfwQAET_lL1sBUfv1IyjUZqHLbfdp8TRLmHT4ZhVJ1vd4vIRp8fLIlF0DzENvCf_Xwmc5DuaQrr8zS9sfWJGPgyRiUlwfeU_nJeMEuTEhsj1AwQKyQDJVGwHiSDDOkN_ac0uFow0I2_5c85N_fA9Y_vSIOHJAlvN9FXpmAilJtLSS6-T3pyjI7TkS8tTOYP1qeipB4eKSmj6G1vUZQsTQapfdPzwmwPvsEGme1vFZElvakWiNSN28IhlcFj5inQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=Jr1OTBOVLdGRXeYxgeYIkC2tC6Njipb2BzqygsK7Rwh7Vc_Kw4wf_q1-jBhpb_Zw7AYHBHJYkJo8iPk0Mdu_CF1zfwQAET_lL1sBUfv1IyjUZqHLbfdp8TRLmHT4ZhVJ1vd4vIRp8fLIlF0DzENvCf_Xwmc5DuaQrr8zS9sfWJGPgyRiUlwfeU_nJeMEuTEhsj1AwQKyQDJVGwHiSDDOkN_ac0uFow0I2_5c85N_fA9Y_vSIOHJAlvN9FXpmAilJtLSS6-T3pyjI7TkS8tTOYP1qeipB4eKSmj6G1vUZQsTQapfdPzwmwPvsEGme1vFZElvakWiNSN28IhlcFj5inQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/15946" target="_blank">📅 16:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15945">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=JERfNDTSHkqiyqWRzUuSaIe9bE-X3tGJX-3618YNWQYHtWDk1bVmyls6KuaHBIN5EOxw0xgORQSwKzsjRLxYlp4e2QlUagffwzXwch4l69PwrqJkCFp9fk8FEGnF2as9oLrcyGy1PwAXZ1h450QNJ45GkU57V-tNwmPuR6dRiHugyZsIDD1VAhSpHV2yoJlQQOYQhlohTJVTOujwJ5Y4YvOGLPNt0WrcGn-XF2BNQaeNmLETuWbW7sTUsOnHxrhomfSV6Rr9--f66HWeDbTnNO7GvtgqJSSzA_B9Bi7S8aXaEYC5uV624sL185i5AODyGcN3awtQFlrzqbPlbFJnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=JERfNDTSHkqiyqWRzUuSaIe9bE-X3tGJX-3618YNWQYHtWDk1bVmyls6KuaHBIN5EOxw0xgORQSwKzsjRLxYlp4e2QlUagffwzXwch4l69PwrqJkCFp9fk8FEGnF2as9oLrcyGy1PwAXZ1h450QNJ45GkU57V-tNwmPuR6dRiHugyZsIDD1VAhSpHV2yoJlQQOYQhlohTJVTOujwJ5Y4YvOGLPNt0WrcGn-XF2BNQaeNmLETuWbW7sTUsOnHxrhomfSV6Rr9--f66HWeDbTnNO7GvtgqJSSzA_B9Bi7S8aXaEYC5uV624sL185i5AODyGcN3awtQFlrzqbPlbFJnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتیش بسیار بزرگ هم اکنون کرج
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15945" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15944">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdKMVptRikl-Pj000wb-Q8_TUXLm1RkGtE_5Ge1PCcSWZ1l4cBWk8ROsdDQjANxgQ9-r9dDAvhIjnRA9ajmRHz67MGk7AsFoPWXzv_5Eg2ATe74IWYOTQqalAQOZv_Q6L-EGEvi8dRUHo-DAc0vI9kUGmeef5dD54y2FsuRiiRWnZgCnxQRlpXsRzUxK2R-HTbcC3OKpSZNH2dJK3oEpH0NMmpesPEYIyalTaBJ-tyFsh8cJcHbyIqm3w34uRiI4Dd4uD8-80d2vPz879vaSxiZdNBZrzqNvf-94eK-7eNEuNa2MMCS_maWs3Qntu_AYmasWWsF7rXBmcGUNd9VRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز
شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند
شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است
شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15944" target="_blank">📅 15:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15943">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">محسن رضایی:پاسخ سریع و کوبنده‌ای در انتظار ناقضان تفاهم‌نامه است.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/15943" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/15942" target="_blank">📅 14:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15941">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمله اسرائیل به النبطیه  در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/15941" target="_blank">📅 14:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15940">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حکم ضبط اموال ۲۰۰ همتی برای مؤسسهٔ مولی‌الموحدین صادر شد
رئیس‌کل دادگستری تهران از صدور حکم ضبط اموالی به‌ارزش بیش از ۲۰۰ هزار میلیارد تومان در پروندهٔ مؤسسهٔ مولی‌الموحدین خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15940" target="_blank">📅 14:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15939">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرگزاری فارس : ۶ نفر از دانشجویان دانشگاه امیرکبیر به علت آتش زدن پرچم جمهوری اسلامی در تجمعات اسفندماه از دانشگاه اخراج و از تحصیل مجدد برای چند سال محروم شدن.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15939" target="_blank">📅 13:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">برقراری رسمی تجارت ایران و امارات پس از توقف چند ماهه به علت جنگ
معاون خدمات تجاری سازمان توسعه تجارت ایران از فعال‌سازی مجدد مراودات تجاری میان ایران و امارات از مسیر بندر جبل‌علی به عنوان یکی از مهمترین بنادر جنوب خلیج فارس خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15937" target="_blank">📅 13:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3GunpkWm4OguEOCHeemP7VcbiEHpq5qh_RHIeYBWfVexJOKsJ6rxrY6Vs6T9KItwRvJVRlfY693DoeXk5sBchbRd8PdUucerXgT51pknMiRPGVzcR2Re34Yjv4oXFPGESGXKz9_3viigbzDk6m5_TMauW9ef5drdtxc0aR9MLn7VZcqPUXr1z-mjXKXzo9EVm_iSf2rtU9zQmeM9ajUd40_SLYRX0RGmGmmZFhYMLO9qvHv0EUo-JfPI-qcb_cL3z-zutrI1IpHgcgHiP_VDJ6fuvUDc_KkfKeOtTdncWVGxbGWeX0FmqrBDYi4dkWUa_7G-5F0lmRHW8HLX93U3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از صدای انفجار در تنگه هرمز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/15936" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش‌ها از صدای انفجار در تنگه هرمز
🚨
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15935" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بحرین : صبح امروز جمهوری اسلامی به ما حمله پهپادی کرد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/15934" target="_blank">📅 12:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15933">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1def3414e6.mp4?token=nWHuPYVj33EP_BgizLCGFkP1La8hBFIbmVFRb8_v1SbkjqY-WB5U6pdVDgvIShbNmdMcKGsDxDveVUVsRciW5M72gmX5E9paw-kj7lZhWmdf1puV0kUZwWYWGrusYEkfzOHvQTZUDaen4h1GhtinHOM6CI26iIuE9wmISFDZEQtkxZLv_tF3NRUKrB165OJYtxdPd05iln5AwJWisvzcxbaW9SS56KDg_wHFNIAA80ab6vGfPXbXqtWS91xpSChyev88q8q-yl4bWOp7N6Sg-g8qdipCiTJQ5a1PaYjH0eZGvNbg5JfbGc9qVEWlUZrXFCV9twVeO7cUI3GG2U-JHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1def3414e6.mp4?token=nWHuPYVj33EP_BgizLCGFkP1La8hBFIbmVFRb8_v1SbkjqY-WB5U6pdVDgvIShbNmdMcKGsDxDveVUVsRciW5M72gmX5E9paw-kj7lZhWmdf1puV0kUZwWYWGrusYEkfzOHvQTZUDaen4h1GhtinHOM6CI26iIuE9wmISFDZEQtkxZLv_tF3NRUKrB165OJYtxdPd05iln5AwJWisvzcxbaW9SS56KDg_wHFNIAA80ab6vGfPXbXqtWS91xpSChyev88q8q-yl4bWOp7N6Sg-g8qdipCiTJQ5a1PaYjH0eZGvNbg5JfbGc9qVEWlUZrXFCV9twVeO7cUI3GG2U-JHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو دیدم با توجه به لحن و قدرت کلام و گفتن ابتکار در مصاحبه ، خوشحال شدم که این ساعت مردم و خودم میتونیم مستقیم تماس بگیریم و سوالات رو بپرسیم ، ولی الان پرسیدم ازشون و گفتن برنامه از قبل ضبط شده
😕
به هر حال من از هیچ تلاشی برای پرسیدن سوالات شما ، فقط بصورت مستقیم از شخص شاهزاده نا امید نمیشوم و دنبال فرصت دیگر میگردم در نتیجه فکر نکنید که فراموش میکنم و پشت گوش میندارم
🙌🏾
❤️‍🩹
با توجه به اینکه خانم قاضی مراد پیج رو دنبال میکنه ، اول برای ایشون آرزوی موفقیت میکنم و دوم امیدوارم دست کم بخشی از سوالات ما پرسیده شده باشه ، خواهیم دید چه خواهد شد ، دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15933" target="_blank">📅 12:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15932">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ارسالی زیاد: یاشار داداش ساعت ۱۱:۵۰ همین الان شیراز صدای انفجار اومد حوالی فرودگاه و پایگاه هوایی شیراز همونجا هم پایگاه پدافندی شیراز هست
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/15932" target="_blank">📅 11:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flqPPE33I0luqc0Zh05a8N2Y_gfkHkL6bwpXTJFWjtzkvXKTvAVk2Zp2DM80bfosLNGx9OXnvGxBw7VgFTMUFVlfGDgBAdU5Ousu-U2R8wDx-kMhO16_rF64YyoQt91muuT47K1St_-qieWT8fYVG8SUK_s9wtsDDvhMZImglLIAGBaxdkngdpNiVhbVmrmyFuxzLXQ2WxiFkHn5uxdksNTMlzeVz5YKlMkX5GdAE0KiX28dCDW6KhHFYPXc0UMfCBzgqHCWELPTRft6IShewnw2UrTAvXd2Rs9ZQSou9zjWtlkinTOiKrqtwRLeVoAJDq69tARH-Lmtnr_EtV-tBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام :  امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.  سنتکام این…</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/15931" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صادق خرازی : یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور دوباره قرار گرفته بود و کشته شد ! وی گفت کمال خرازی را به صورت استنشاقی(مثلاً گاز، بخار یا ذرات معلق)در بخش عمومی ترور کردند
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15930" target="_blank">📅 10:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شبکه PBS News به نقل از یک مقام آمریکایی : ۶ فروند هواپیمای نظامی ایالات متحده، چهار هدف ایرانی از جمله تأسیسات راداری و انبارهای موشک و پهپاد را در منطقهٔ سیریک در ایران مورد حمله قرار داده‌اند!
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/15929" target="_blank">📅 10:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87cfede001.mp4?token=oXIVoFyyi2dQQDq8nzWu3xz6GlMREzBwLaUzzfh7b4QaAm6FEEfbzneACIzavSBe6rN_FeD-ua7AP_4OgVm4hQmeAtuJgO237medhwoa3NQHaLT8Arq-LZmJATxSDlFskb5UVUEibhSeMeUSfFY2ZrAlEyOLM4gNbJWb0El-6ZhEJ4f01ZXp5WB2opnSLeUSj18iGO7jPgZu7JyzTIBh4ktcfP6kg8hmSEDuApuJw4sbyhIT3Ie0wTv5FTJ8RAGxBL7dI01iiV4ER4l2cCHVk21p_MEinbp0WOih7vRXai0UTzr9otlQXyNjvSXzQc-ojNKlr9vnqUBLRgmNUfOR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87cfede001.mp4?token=oXIVoFyyi2dQQDq8nzWu3xz6GlMREzBwLaUzzfh7b4QaAm6FEEfbzneACIzavSBe6rN_FeD-ua7AP_4OgVm4hQmeAtuJgO237medhwoa3NQHaLT8Arq-LZmJATxSDlFskb5UVUEibhSeMeUSfFY2ZrAlEyOLM4gNbJWb0El-6ZhEJ4f01ZXp5WB2opnSLeUSj18iGO7jPgZu7JyzTIBh4ktcfP6kg8hmSEDuApuJw4sbyhIT3Ie0wTv5FTJ8RAGxBL7dI01iiV4ER4l2cCHVk21p_MEinbp0WOih7vRXai0UTzr9otlQXyNjvSXzQc-ojNKlr9vnqUBLRgmNUfOR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون تهران گشت هوایی     Sukhoi Su-24 با دود سیاه معروفش
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/15928" target="_blank">📅 10:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">داداش ، چون دروازه بان جلو بود اون بازیکن جای دروازه بان حساب میشه
@withyashar
Bro, since the keeper was upfield, that player counted as the goalkeeper for the offside rule</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15927" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15926">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d4769eb6.mp4?token=Fe7oP1saUIxUSpUIrZtcmFllzCthE1P9qTeSBpoPp7QSU4IkxBBC8x14qgSDdtRi9hLkrebfLuZApvm9gY-S6vzuIy_j8yV87f5lpAmFBpB4qxz_sLmNCt3ugm9OnCkQdBZYwdRmZ4nF2ii0OMkRLpLatIamZWLrfImkFwbn9eURJ-nuVXIE9creu9OTv0O9SBz8T_6In7oP4DUoDJ51Syz-XbvFRi7zRn2m3r760QiMxosC1Z3gP14iqLPJG6wsbD1qm4cjqjzH16ednqc3O8myKA25jjssuDi1LR_oYZtO7J1WvMvm4s1FEa8x5LAaiK3dw-FZi3En_ei57t46cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d4769eb6.mp4?token=Fe7oP1saUIxUSpUIrZtcmFllzCthE1P9qTeSBpoPp7QSU4IkxBBC8x14qgSDdtRi9hLkrebfLuZApvm9gY-S6vzuIy_j8yV87f5lpAmFBpB4qxz_sLmNCt3ugm9OnCkQdBZYwdRmZ4nF2ii0OMkRLpLatIamZWLrfImkFwbn9eURJ-nuVXIE9creu9OTv0O9SBz8T_6In7oP4DUoDJ51Syz-XbvFRi7zRn2m3r760QiMxosC1Z3gP14iqLPJG6wsbD1qm4cjqjzH16ednqc3O8myKA25jjssuDi1LR_oYZtO7J1WvMvm4s1FEa8x5LAaiK3dw-FZi3En_ei57t46cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/15926" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تیم ملی دوباره از استادیوم به فرودگاه می‌رود!
بازیکنان تیم ملی فوتبال مانند دو بازی قبل ساعتی پس از پایان بازی خود برای بازگشت به تیخوانا عازم فرودگاه خواهند شد.
پرواز تیم ساعت ۳۰ دقیقه بامداد از سیاتل راهی تیخوانا می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15925" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
