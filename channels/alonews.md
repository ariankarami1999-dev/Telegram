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
<img src="https://cdn4.telesco.pe/file/ZtlW37VfZnXBGn-pDwlfbQ-QbkcxYOJrrZO8qIVSPbMekE_Mkmaz6TFb_Bk7NrtTmQBssp5kAoKY3iTAw1LvbMbtVv74rIk2GpZ7DFJmVKMZiI3hwsFiB5gVG-FThpN67aZZeqQs438s_qm-rtaQRaW9SRJ9Ukrj0VbKclcAzEbYfCJbNEomI-EuV7zduPiSOy1dTFm7_KCzL8kf8pK1Qa3VnMght3UQK58_PiVn63vdcRQ9lM-j_1A1X_BaSQtSQ-td8TUwwNwHfTlCPLQO6aSs42qk81A8vOQCWLWKZqTmB__Mvkd5UYvyn9mBbp48SW6ut3UkPCSKipNMHMd1Dw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-128891">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
میانگین قیمت بنزین در آمریکا برای نخستین بار از ۳۰ مارس (۱۰ فروردین) به زیر ۴ دلار در هر گالن کاهش یافت؛ موضوعی که همزمان با افت قیمت نفت و تحولات اخیر در بازارهای انرژی با امضای تفاهم‌نامه میان ایران و آمریکا رخ داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/128891" target="_blank">📅 14:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128890">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsMlr-FKueE46RXqadjlgOBYAqphTwDy3MrxAMZeDO3LBRh0v_Ah0V4MNXSuoRfNnit5j2hU7j58IqVsNDUQynfHS9x6z_mBVGV6H3VXHYkDpCNbq06yyLlmxc7TajgJ_W5YQzbyj9G26UKvoXoiu2nO6PPknUP-gfBxv5cQTnsYnwyZelJKSQTBqpkWe4WBoPLVPv42rXX2WckWFI5icOXClnrZFmBmNV5OX0JzJaxZdHHu0tRROL6J82VW0qgpbzYoMr9Mit9yaUfxh715TeIp1aRusbWXej8svYu7HJ5N5zaB4L0mzd71hCa2r_N27MBhT5c36gyDyA47SURAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به گفته چهار مقام آگاه، وزارت دادگستری ایالات متحده در حال تحقیق در مورد چگونگی ایجاد یک سبد سرمایه‌گذاری جهانی گسترده توسط مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با اتکا به بانک‌های وال استریت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/128890" target="_blank">📅 14:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128889">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_MZUMiwdT6qH5nF-hzfV0tzrU1zRLotKBfWWqUsjbn853rGZDHfzHeknAiP93n9nXxomiA8Pwg04bBPXaYkQIwDN0piuJE9w-jljiDo57s1NwLttJJECKL9wL8dlCBxc8YoSgZL_T2v4DBZK0UEdmO_6ikrzgK4nWKTmQ_2Ra6Be6MhaOYPdt_I6gwaQqIM7seq4QRlwfr14bCj7bUsAAQQbfqcoD9O9Fm1e59Ai37BHE2RIuxyOdeY48zDLGIJSHDpupLfBTVOip-K28ypjKjeHbpLbe_TlCPUPplNFuXvn8E2QxUaoU6o4ZKbBj5qdC-xZr3w6sIUm_x2A50jKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: این یک سند تاریخی و پیامی از ایران مقتدر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/128889" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128888">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5nOL3JTkUnqTi7ttPEQUHKruyzPvOymHcHvcdQNbjq_qIb1EIYr9I_f_Vcrna6PDBCC0NA5pVBWkD1pmJislhOlV9qC2oNDwPcqHbyPKJ2CEsgBbKb5_xXGtXLkR8BhvLFcL4WKxC5THuC6dZxVmqWb0bU-PC2GrPLK8XzsD_Jw7ZJssSwXfma0M4j8lXpv7TKNE278ETICNY6tGHlNV6D58fBdjdl1EVwtAF6CoxVGY5_0F_nl1Jh18ze_x5PLW7YIX6aFel8oXlFISsBdZlKRL0f1bNhRxk9tOd1KDSwrdQEmvxWBXJ-lK6NVQCBDl6EKE5VgR9XlzoRkJlXJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهرام پارسائی نماینده سابق مجلس:اگر کشور بی در و پیکر نبود این حرام خوارها بی کیفیت ترین خودروهای جهان را ناگهانی ۵۰ درصد گران نمی کردند اگر آنقدر که برای مذاکره دست و پا می زنید و با هم رقابت می کنید کمی به حقوق ملت اهمیت می دادید در این کارخانه های غارتگر مال و جان و عزت مردم را تخته می کردید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/128888" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
به نقل از المیادین، یک تحلیلگر اسرائیلی در مقاله‌ای در روزنامه «یدیعوت آحارانوت» از آنچه «شکست راهبردی ایالات متحده» در نتیجه توافق با ایران برای پایان دادن به جنگ خواند، سخن گفت و مدعی شد: «این توافق، جایگاه ایران و حزب‌الله را تقویت می‌کند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128887" target="_blank">📅 14:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
زلنسکی: اگر اوکراین بسوزد، مسکو هم خواهد سوخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128886" target="_blank">📅 14:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
فیصل بن فرحان آل سعود، وزیر خارجه عربستان: «حمله ایران به پادشاهی و کشورهای شورای همکاری خلیج فارس، اعتماد متقابل را سلب کرد. پس از تفاهم پکن و آغاز روند عادی‌سازی روابط، ما در آستانه گشایش همکاری‌های اقتصادی بودیم، اما اکنون عقب‌نشینی کرده‌ایم.
🔴
پیش از هر بحثی درباره سرمایه‌گذاری یا همکاری، باید درباره بازسازی اعتماد و رابطه گفتگو کنیم؛ این مسئله برای بسیاری از کشورهای شورای همکاری نیز صادق است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/128885" target="_blank">📅 14:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAP-8k8uhrzJmEhDsLNs-CeBeEmCibCQq4SVAaNZIj97qx97FnfR-PxudavLQijkV_CqUveZIJDINe-gcgg2j4ZZQc8Z2FCDXXM1ttmDOQwZKfX-6zd5Vql6rpbX7hOFIWn8MUzzUywv2fgyMylO3eqtFUJvMr4To-Rht3ewqUS_pyhoUbVyVvA_Sh38Gr42OiMmTP2Q54mL3I_Mwa9VYWpiwSdO4p9lwwTOm51P0uZcx7YHSNOSd_6qTayBskMk4XtasiKFJgGToBTYPKYiTJgWUF9FZawAA9_iOnWxo0vcsmPjFpGAbRPTmwefy8mfdaB-xP1KvXWHV6tE329XVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان نخستین رئیس‌جمهور، جمهوری اسلامیست که امضایش کنار رئیس‌جمهور آمریکا برای پایان یک جنگ قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128884" target="_blank">📅 13:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: به طرف ایرانی اعتماد نداریم و آماده هستیم در صورت لزوم حملات علیه ایران را از سر بگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128883" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128882">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رشیدی کوچی، نماینده پیشین مجلس: متن تفاهم‌نامه ایران و آمریکا بیرون آمد؛ آقایان پر مدعا؛ دقیقا کجای این متن ما را مستعمره آمریکا می‌کند؟
🔴
آقایان فحاش؛ کدام بند مغایر با منافع کشور بود که اتهام جاسوسی به مردان میدان دیپلماسی زدید؟
🔴
شرم بر شما که این‌گونه به خاطر بغض‌ها و کینه‌های سیاسی، امنیت ملی را به بازی گرفتید؛ رو سیاهان تاریخ شدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128882" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128881">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: تنگه هرمز یک آبراه بین المللی و برای بسیاری از کشورهای جهان حیاتی است، اما ما به آن متکی نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128881" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128880">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3g9oJPRvwhafhc-atA1zBWMINXHBmzGS-NgVQH7MmqRkRey7lm7NXu3BX4-_sMgvi_iPIjhCWjYMawK_SrF2xjY_AB2LKydcgxYyLQpctJgDD1yEVtGnAdtxeSVQiKfWJZ9sXfTC3ncMk0KKDDIpi9qL4AZV8KZKfU2JUG9KmXQLsT312G-zPy1eWl-IKzYamEGwRC8mdmwUpjuGXecwqAuN1sEPt-vuG9_AvjKcG--yhxHJ433F71n42rqRYyEaR5YjBL9HVbGuY-jx3L2FaOWCZQro3I0tmuZ83Bp2nlB-8oMwfF0hjq0vioHBVtStW702QQAMLPdv_jYp290dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128880" target="_blank">📅 13:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128879">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1nMWaOPBAvFyZlxbvQEpQNADi1YF809uuPXRASMsUae3neRYue8nHDn80QvQnQKcVXR0JxMkZo5oGfseECsy64bQGk5UzK3G-DC4_H6Qh8e3kVd21gEEz31z_-1J57wsjTf5FwK07qrwEKwqjclRIRkANOMXE12_iNgsUZp2s1xJOD5kor0IKkTRD54ficdsPbR2QsKbMfk5QUg43u90l8n1R8OPipqT50VRh9sSIYE18Ah-FPWDFRjmIhK_Md6EqL38_aNCmaThVHtt5nalDDZ6Doo08uS59giw0gwoLum9VMwvu8O9PS57vY7j6jqt8OUmHcujB6YOCRx2NuEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه  اسرائیل اعلام کرد: پس از آنکه کایا کالاس، اسرائیل را با رژیم آپارتاید مقایسه کرد، روابط خود را با او قطع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128879" target="_blank">📅 13:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128878">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دار و دسته رائفی پور بُت سوزوندن
😐
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128878" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128877">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js_omgd2e3s759hJSKNUazAiSFFqNfGOnP7B3dFhJpwqSuM4z_ZPXpCKXT0etmJmGk7nMxr65_Jl7bpGve-ev1g5oCV1C3Z94_6_zqIT9wmVJAraQAAWXoFnI8a_do7RpwTbfHKwc__d0UbOi-GvTJvMWsy1L56lm6UKg_VyVXUAzArICdG56Tu3JaJii7jx5br_fpxKwlEAEDcf7SWQSnQMpeOrNQc__pxSASOTA3F7DKMXmRPLECRVIgkLoAxQYoREMDevgYEpBJuv4R6jbKpqGOad7hm-sQa09YhakV_aIsK2-oHZkqx7GFf7W9EbUS1Iq6VedIusztga6Fp3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار وال استریت ژورنال: چه عکس جالبی. امانوئل مکرون که کاملاً اروپایی‌ها را در مورد ایران نادیده گرفته و مخالفت آنها با جنگش را سرزنش کرده بود، موفق شد دونالد ترامپ را وادار به امضای تفاهم‌نامه در ورسای کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128877" target="_blank">📅 13:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128876">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
شبکه المنار اعلام کرد که حملات اسرائیل به شهرکهای کفرتبنیت و حداثا در جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128876" target="_blank">📅 12:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128875">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTCmGC7cMgk5S-62lI2pSn_QP49E-FG0IDjTAA7tWLG6Uz9d_vVvM1YU7tnp88vN_laq32CVRtKzBfFgS95rFszDb4AsziVDd_mW_tUEAPV6AS3aTYcmHGVSaCmFPr1j87QuH5A59V0Mg-6rYvBzh8O5eVQqJhHrBkAuIwUHG-28igpAbUcUAuHXnfXh6Rztxb3lCjUNG237BY5YhTHGRcBh3H1Zz6l9B3UniaVtU1aVutjSeRbQ2CZLOZ09CKLULw4X-9M0UNzDHRdtSlCbbfqNVMu_JJMXEzQIsCB-SFBxzVRTo7-SOTgh5F_3AiZcNoIm18cSlRjjWQPpjW1gQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دانش آموزها دایرکت سوراخ کردن که اینو بزاریم، ماهم گذاشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128875" target="_blank">📅 12:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128874">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی اعلام کرد:
در حال حاضر، سطح تماس‌ها و ارتباطات با ایران در پایین‌ترین حد خود قرار دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128874" target="_blank">📅 12:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128873">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anHbsEk5vCBZU7j4MUAhw9HKH2_LtHaGF0CcsjHDtuimEjrXevitRqyEwkZpLL8sdhbNmzCT_WYpwLoJe3oulMBTxzc_Mb3wDPNXmU0qPNpfj5JS31JFH-j7PApOQ93dCyJOF2MuHdjJauQdeYrA7hgKYzU28A8Oxw7T3TpiMNgi7XeaAeLaf5eRkrl1KNv1FtSAR4sGFKTAbonuCqAuGN3ouS1b3UVD7j63A8mmwG7a5DadkUwXN-2AAAA6L3CtusFo5PA3Oc34hqDsAqeMCY1WSYgBTl0KJztcveIkzcOttqbO-CjtGpB0WjlADKwbAAFlMJYeis02Y9i9aBesgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، هنگ‌کنگ در راستای تلاش‌های پکن برای بین‌المللی کردن یوان و جذب سرمایه‌های خارجی، آماده راه‌اندازی معاملات آتی (Futures) اوراق قرضه دولتی چین می‌شود. این اقدام گام مهمی برای تقویت جایگاه پول ملی چین در بازارهای مالی جهان و تسهیل ورود سرمایه‌گذاران بین‌المللی به بازار بدهی این کشور محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128873" target="_blank">📅 12:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128872">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfpjvdtDQEyHc1xX58BJMmtotq6s9H15ye5bNR-HipfjD4op7IIQj6vsin2zdFa97zwvpKF_E8ZxI99_BC88yjhbdC5UDYGDAU_I8Kg-rcFDljmxvs2kyQivXzg7SbKBK7T3pCo50ZcLnriWuPxWiYWlNNlGbNIcFKShmZ2Cn45siOVOMf1SzsPTkKUqcywtyx26O8ae7MihArei8vFrGzBRKhn32tDDROxs5EUAW3aupq2GCrUeooOBhZsONOESmXD7Pg8jx5hESPB1cmbvmTlliXIXKwvocgBvDBJJ1XjEIPB2t3m0-n4wTGnz0uSmLrq4qcibyozVEfYuADXHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: انتقام آقا رو، امام زمان میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128872" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128871">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان به عنوان میانجی، یادداشت تفاهم اسلام‌آباد را امضا کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128871" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128870">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
منابع العربیه گزارش دادند «نخستین دور از مذاکرات فنی مستقیم واشینگتن و تهران فردا در زوریخ سوئیس برگزار می‌شود.»
🔴
به گفته منابع این مذاکرات فنی میان ایران و آمریکا شامل جنبه‌های حقوقی و قانونی مربوط به رفع تحریم‌ها علیه ایران خواهد بود.
🔴
منابع العربیه خاطرنشان کردند گفت‌وگوهای فنی ایران و آمریکا پرونده دارایی‌ها و وجوه مسدودشده ایران در قطر و همچنین پرونده هسته‌ای ایران را در بر می‌گیرد.
🔴
قرار است در نشست‌های مذاکراتی غیرعلنی و اعلام‌نشده، پرونده‌های مرتبط با لبنان و حزب‌الله نیز مورد بحث و بررسی قرار گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128870" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128869">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وال‌استریت ژورنال: اپل تایید کرد ، قیمت آیفون افزایش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128869" target="_blank">📅 12:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128868">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTAQzr5_pfiyUz1yH07mZTbbT0i5H5p5nR5tTNQ-rXEiFiRtM9HX3ZsZJgz7wBX_DhA4JSWNGZ1DN1Vr2WWki2b9qpsxYy_o4WxbKztsL3ce-jEbBdVXJ8GJ6FhSZH_f_xFy1YSO_2v1x2ZwDy5wgMTcaF4pPi2mR5Psl2syb4XwjRsb62MbQ02kyWvKYSzJppvdwafdaqWbGE1Y9Dyv9PFbtL7b6TPc_-CDULbi-27gJXfstc0Mzf8QXWHj8It3bR0Q1O-5aHa8h7i_sO_gae-1xZcQMaQ5wr_kFS_6kPontdQsKoJaXmKP-zMKOvO-osfPlp6_D6NmlsciVyoHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سختگیر نبودم، در حالی که بازار سهام به تازگی به بالاترین حد خود رسیده و قیمت نفت «به سرعت در حال سقوط» است، یا حسودند، آدم‌های بد یا احمق. آمریکا را دوباره بزرگ خواهیم کرد!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128868" target="_blank">📅 12:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128867">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38821025b7.mp4?token=ifBz6Y1C7tzv4MfjnjvjTHFZRQIdfRwMm2exI8K8YEH26O2vhinNPVR7giZlHQgvm7KhnyYvol2Zhdi0b7Gw6KqvywvG0YRlCGHV9Z3EwfkkrYrc0PIdaCAtISy8nf7MQILVeZb8UpAVjbkp5nWuECIpug7dfuMTtKj3usDCsFyQw1rLicHcsdATdHe6jOSnsW6MSrM-EOUUqkZEnM5X6qXOwOO3WPMWtP1sx5Zmi6-QnNhfsYsjiEeOlybqhsYGuvpe2m3XQUspS62uGrKn-xKrs62bvh-bfAchHkx1iO9oN_3mh_HINe6EBUcUKIDnq7M5a5GBKJf-WOAAWfzjQT6TT1op4MCtsInv9x18L6rOE4U__Kv1qSEFUEXaASJFdDBVCvfL-6H9Yrgckora9SpNR8aS1Q4C1weLptWT0TGuiDZOqj2dksKl3RYDld0AhhlSEgQtjwz7EmEzvrGjG3yPudjJCNQjaCKkDzE7We1t2XEL_usFAeHyYC2zdXZA0tcmds7G8i5kGSnsWHhnuDI1SUqyxvaDtTHWfqhMoUqOA2vkHFXBocL4lTph5xFp-18jjcs8wRsrzmFAanahsw5aOPE6n4_9FM1LdfvRaLPiCmpq8AZcAkd6jD6DWb6j2JfC4gcZnb-ybnwl135g2yiHFsfjqCfIcNyBRIGRrd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38821025b7.mp4?token=ifBz6Y1C7tzv4MfjnjvjTHFZRQIdfRwMm2exI8K8YEH26O2vhinNPVR7giZlHQgvm7KhnyYvol2Zhdi0b7Gw6KqvywvG0YRlCGHV9Z3EwfkkrYrc0PIdaCAtISy8nf7MQILVeZb8UpAVjbkp5nWuECIpug7dfuMTtKj3usDCsFyQw1rLicHcsdATdHe6jOSnsW6MSrM-EOUUqkZEnM5X6qXOwOO3WPMWtP1sx5Zmi6-QnNhfsYsjiEeOlybqhsYGuvpe2m3XQUspS62uGrKn-xKrs62bvh-bfAchHkx1iO9oN_3mh_HINe6EBUcUKIDnq7M5a5GBKJf-WOAAWfzjQT6TT1op4MCtsInv9x18L6rOE4U__Kv1qSEFUEXaASJFdDBVCvfL-6H9Yrgckora9SpNR8aS1Q4C1weLptWT0TGuiDZOqj2dksKl3RYDld0AhhlSEgQtjwz7EmEzvrGjG3yPudjJCNQjaCKkDzE7We1t2XEL_usFAeHyYC2zdXZA0tcmds7G8i5kGSnsWHhnuDI1SUqyxvaDtTHWfqhMoUqOA2vkHFXBocL4lTph5xFp-18jjcs8wRsrzmFAanahsw5aOPE6n4_9FM1LdfvRaLPiCmpq8AZcAkd6jD6DWb6j2JfC4gcZnb-ybnwl135g2yiHFsfjqCfIcNyBRIGRrd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره مسلح کردن معترضان ایرانی: در واقع کمی دشوار است. می‌دانید، نمی‌توان فقط سلاح‌ها را از آسمان رها کرد. واقعاً زیرساختی برای رساندن سلاح به قلب مردم ایران وجود ندارد.
🔴
یکی از چیزهایی که رئیس‌جمهور را بسیار ناراحت کرده بود، همه این معترضان بی‌گناهی بود که چند ماه پیش توسط کسانی که در قدرت بودند به قتل می‌رسیدند.
🔴
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم رفتار متفاوتی دارند؟ قطعاً امیدواریم چنین باشد.
🔴
و اگر چنین نباشد، وقتی رفتارشان را ببینیم، می‌توانیم بفهمیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128867" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128866">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پیت هگست: حق عضویت سالانه ما در ناتو منوط به این خواهد بود که سایر کشورها به اهداف هزینه‌های دفاعی خود عمل کنند.
🔴
در جایی که سایر متحدان با فوریت هزینه نکنند، سهم ما از حق عضویت کاهش خواهد یافت.ناتو یک خیابان دو طرفه خواهد بود.
🔴
من امروز یک بررسی شش ماهه وزارت جنگ را اعلام می‌کنم که وضعیت نیروها و پایگاه‌های آمریکا در اروپا را بررسی خواهد کرد. تا شش ماه - می‌تواند کمتر باشد.بیایید آن را بررسی ناتو ۳.۰ بنامیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128866" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128865">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام اسرائیلی نزدیک به بنیامین نتانیاهو، نخست وزیر اسرائیل، گزارش داد: اسرائیل در حال انجام مذاکرات پیچیده‌ای با واشنگتن در مورد حضورش در جنوب لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128865" target="_blank">📅 11:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128864">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06953ba6ec.mp4?token=bu4-Y9YhIU5Lzb6jk4p-ni7Es7_EIm0CjNI6xrB7-DUchH2csLVLreeZacHQ7_hjPQEHs2dgy_IPL5vc9GrjQ-Qt1S3MkOpnqGxbnQB-OHQeT8hzZb5m06VfQL3WuLbfDEDoplBIISGdSaYGgfJ4vZA15tYI5acaep4Np421H5fiQfY6oFKiOBolqkG4pHl7HvMBGJaIsCRMgsJLYfgBrOt32wPZurTHk3tUbGWlFead_8ltmf1CAXxlfCZnRaVYwOhGUo7PObz73QV0K03kG6WSowYgp5oiUke31Zqvv46t9lwsXNqlPpLtMtdqK6X5PAGZb1rKPngwhMk59SssZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06953ba6ec.mp4?token=bu4-Y9YhIU5Lzb6jk4p-ni7Es7_EIm0CjNI6xrB7-DUchH2csLVLreeZacHQ7_hjPQEHs2dgy_IPL5vc9GrjQ-Qt1S3MkOpnqGxbnQB-OHQeT8hzZb5m06VfQL3WuLbfDEDoplBIISGdSaYGgfJ4vZA15tYI5acaep4Np421H5fiQfY6oFKiOBolqkG4pHl7HvMBGJaIsCRMgsJLYfgBrOt32wPZurTHk3tUbGWlFead_8ltmf1CAXxlfCZnRaVYwOhGUo7PObz73QV0K03kG6WSowYgp5oiUke31Zqvv46t9lwsXNqlPpLtMtdqK6X5PAGZb1rKPngwhMk59SssZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست وزیر جنگ آمریکا: برای مدت طولانی، ناتو یک ببر کاغذی و یک خیابان یک طرفه بوده است.دیگر نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128864" target="_blank">📅 11:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128863">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3xihItxLpMiSfdCzqPRA3Or13zFrMhKej2Egw71n2nRcOWT98t1XOdwqiIeoWOU1-V2Bcz-ZxcxQAzo72_9kcLDXzflKbz82LHEWUUJWOSUIHDWsMdZh3Zx-F2lPhN1FuoKGcrpUw3RUJxtQA2Fp-YbAfStyeIhTMD-fAzvrfZ34CB-xqQ36qchnUUUczlqDjOM7jKiCi--6vLoF5mk8RwM3vSeRfn8wWOz3u61WVHol98CtAeGVu1azOPZlaEEDhmZM2OHmD4IeRMX0sfv4Jxx6oYWzExddjbcxWwUD61QS04LVVSlH8ql070tjkxKyKid3ohDsTDYx4rlAULk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار ارشد آکسیوس:
ترامپ به توافقی با ایران رضایت داده که بسیار کمتر از چیزی است که در ابتدا امیدوار بود به آن دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128863" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128862">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMmRIxinDwYIg93rvnQP9Q7Hseo_4esM0oQ-0lU8nx2AvodWkq-jhMIv3O_tbH4UmkuYVyjvMA1NgI8Zf-Dp7aFdqQc_GeNywKxwE73kKsgnEow_Bl-sXht59LjKswkIsB6is8xv2aGofCrmOOxJUDgoL5piJOn062YVr361Ep5g9MLroXP4dXOvF59quwU6FqYQ2c4VpmtA4CGGEM2cWFpReZh2uGafjWFp8agNqV2AGbLMiqECIQE3j5gubDi2MgMxAKIPONT08fk6KWqVcdM0_irc8WanSttAGJUEeinVap_6prqU3k2s4SLvEADfG00x3sGkTTA9MLoGZNTiLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ اعلام کرد پروژه ساخت سالن جدید کاخ سفید با سرعت مطلوب در حال اجراست و برخلاف پروژه ساختمان فدرال رزرو، هم طبق زمان‌بندی و هم با هزینه‌ای کمتر از بودجه پیش می‌رود.
🔴
او همچنین گفت این پروژه شامل زیرساخت‌های امنیتی و نظامی مختلف از جمله یک «درون‌پورت» (محل استقرار و عملیات پهپادها) خواهد بود و آن را برای امنیت ملی آمریکا ضروری دانست.
ترامپ در ادامه از شکایت حقوقی مطرح‌شده علیه این پروژه انتقاد کرد و مدعی شد شاکی هیچ جایگاه قانونی برای طرح این پرونده ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128862" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
️سناتور جمهوری خواه بیل کسیدی در مورد تفاهم نامه ترامپ: ریگان در قبر در حال لرزیدن به خود است....این بدترین سیاست خارجه آمریکا در چندین دهه اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128861" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf672333e.mp4?token=LHwioOpP2CaIQG1hfJFfImU0o2CUd_JDxwUfp2ccMO0ozxtnA0tSxkYFxxD598ZuMYcghVuRMcqpRj3iy-AexC3qPk1p3C5tpCH7MjHvSlm_7saz9MoCYAqXWmkAzEjgXeMLYWWP-thVmH0V5mohR6I8IAauYik-zpxrZjcy2W6Cn8YQbmjFj58mJk5mRWygEhPIX7uQ2b6zRbODmbceQkA3jmBclqoBtEU4zEXKLhSwgMx1CnvkzS7r0LgVK3ViYO-5jnaLUS8vecRDOmvrpQhiqtB4nqFY4SeFNTJJa_vJvpmGc78GjwxurFqkv-DT7QHJRmPIttsP_moK95LIsjCun46t-D2L2N7NuwbZ0pb3madJ6TSbj7zQ519zsrCTjZ0f7uNwWr-mMAV07YFy4y1LEIdJERvr9fGUEAg3LN1p9MPWVUh7wBYiTQajI-N27OS3tHeZ-qpBDnmB395qwKeIJ001_R7Pei5Ng_wyw_0FhbDGzFOb5eMn8vKU3aN4ULwjhu0CU6MlnV9LsNVXBXyqx4vPMjYg60NXXngPAMolCG4G_XeYdmz26bM_NBOsW-FafwpyR6u5SNQBQvZPI1ThP9WRuPR2Vmvw-wphuqNTdIWf7RbS6XMJwaUHU_klVndJ1zfWFDCSJpWa2xgVjP7_Q4ONea2iWs4Yi3-73bY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf672333e.mp4?token=LHwioOpP2CaIQG1hfJFfImU0o2CUd_JDxwUfp2ccMO0ozxtnA0tSxkYFxxD598ZuMYcghVuRMcqpRj3iy-AexC3qPk1p3C5tpCH7MjHvSlm_7saz9MoCYAqXWmkAzEjgXeMLYWWP-thVmH0V5mohR6I8IAauYik-zpxrZjcy2W6Cn8YQbmjFj58mJk5mRWygEhPIX7uQ2b6zRbODmbceQkA3jmBclqoBtEU4zEXKLhSwgMx1CnvkzS7r0LgVK3ViYO-5jnaLUS8vecRDOmvrpQhiqtB4nqFY4SeFNTJJa_vJvpmGc78GjwxurFqkv-DT7QHJRmPIttsP_moK95LIsjCun46t-D2L2N7NuwbZ0pb3madJ6TSbj7zQ519zsrCTjZ0f7uNwWr-mMAV07YFy4y1LEIdJERvr9fGUEAg3LN1p9MPWVUh7wBYiTQajI-N27OS3tHeZ-qpBDnmB395qwKeIJ001_R7Pei5Ng_wyw_0FhbDGzFOb5eMn8vKU3aN4ULwjhu0CU6MlnV9LsNVXBXyqx4vPMjYg60NXXngPAMolCG4G_XeYdmz26bM_NBOsW-FafwpyR6u5SNQBQvZPI1ThP9WRuPR2Vmvw-wphuqNTdIWf7RbS6XMJwaUHU_klVndJ1zfWFDCSJpWa2xgVjP7_Q4ONea2iWs4Yi3-73bY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه سی‌ان‌بی‌سی: فدرال رزرو آمریکا ارسال محموله های ماهانه ۱ تا ۲ میلیارد دلاری نقد به بغداد را تا تشکیل دولت جدید و قطع دسترسی گروه‌ های تحت تحریم به ارز متوقف کرده است.
🔴
بر اساس سازوکار مالی پس از ۲۰۰۳، درآمدهای نفتی عراق مستقیماً به حسابی در نیویورک واریز می‌شود و دولت آمریکا کنترل توزیع نقدینگی آن را در دست دارد.
🔴
با توجه به اینکه نفت ۹۰ درصد بودجه عراق را تأمین می‌کند، این تعلیق بازار ارز را با بحران مواجه کرده و پرداخت حقوق ۷ میلیون کارمند و بازنشسته عراقی را در معرض خطر جدی قرار می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128860" target="_blank">📅 11:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8UqP3s-zH6I3b05PBV9DhHqb6kPHURWaivPGFUxt7ncrhRZUk2a05A0vurDUG0FYhwj_xVChG1DBqeKBn6G_IeYZ7-uFK066iDIFIAMkM817mqckXoBVZxD0hmIyNi20i4OtE4aA5Ev-iLil9aNj95raNiEuQR6zzFljyO1i0cFAcUyY9FlLFkNwZPXnfCAEvYeOxX9vd0QNTYr-3jJThxo92lqAjOo26DyzaEDZUQ50VBUu93YdM7kiS0eeZGoge7UIKWwqHrF_c9x8ly4i3TfR83nm3M0Qg03qG-NyyKTCrOal0bjlLbesFm077T7funIj49AJ_pzOYsIg5MBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی عضو تیم مذاکره کننده ایرانی: استاد خوش‌چشم درست می‌گوید؛ ترامپ کوتاه آمد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128859" target="_blank">📅 11:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وال‌استریت ژورنال: به نظر می‌رسد رابطه ترامپ و نتانیاهو به طور فزاینده‌ای تیره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128858" target="_blank">📅 11:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پیام حسن روحانی پس از امضای یادداشت تفاهم ایران و آمریکا: باید از دستاورد تفاهم اولیه، حراست کرد
🔴
باید نسبت به توطئه و عهدشکنی دشمن هوشیار بود
🔴
امروز هر ایرانی در هر گوشه دنیا، به ایرانی بودن خود می‌بالد
🔴
رهبری نظام با صلابت و درایت و حکمت، انسجام ملت و نظام را مدیریت نمود
🔴
نیروهای مسلح جان برکف حسرت پیروزی نظامی را بر دل دشمنان گذاشتند
🔴
دولت خدمتگزار لحظه‌ای میدان خدمت به مردم را ترک نکرد
🔴
همسایگان ما می‌توانند با مشارکت و تضمین این توافق، از ثمرات امنیت و توسعه مشترک منطقه بهره‌مند شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128857" target="_blank">📅 11:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گروسی: در مذاکرات سوئیس شرکت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128856" target="_blank">📅 11:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل: اسرائیل حق دفاع از خود را دارد. هیچ‌کس نمی‌تواند به دولت دیگری بگوید که اجازه ندارد از مردم خود دفاع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128855" target="_blank">📅 11:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / نتانیاهو: اسرائیل به بند لبنان در توافق ایران و آمریکا پایبند نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128854" target="_blank">📅 11:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / گزارشات از پیشروی ارتش اسرائیل به سمت ورودی علی الطاهر در لبنان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128853" target="_blank">📅 11:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e98533ee.mp4?token=tQhvgnvb899T_HP9AZyz0_QpCEHTOLdY0MoJ94fnf7aB4-kYs7jU24Vbr_BmYE-5wBiZna2-qSiwMjk1RGK2i-AxHp5LyIX9YAx3vOXNAvQxY2At_YFehuRcd2nTceUyiwbgDW2vrBX7I0zWnp8m9dxqwqClR4kRyUHZf4BmrU8KsBtsuQHzD4zof4BuqFj13uAP99IzSacecO0lkOtH66Xr1oy1dU7-REh3hv0Nad250WkFFcI6QZkvB4uPKwpbWRfXKlVqfor9mziq_vrgzYmZbIRl8D1HrkS_a1ZClA72VzTX4c4ywYt-YnzCyP6c0vHGmdR5vtZg3jrT1u_5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e98533ee.mp4?token=tQhvgnvb899T_HP9AZyz0_QpCEHTOLdY0MoJ94fnf7aB4-kYs7jU24Vbr_BmYE-5wBiZna2-qSiwMjk1RGK2i-AxHp5LyIX9YAx3vOXNAvQxY2At_YFehuRcd2nTceUyiwbgDW2vrBX7I0zWnp8m9dxqwqClR4kRyUHZf4BmrU8KsBtsuQHzD4zof4BuqFj13uAP99IzSacecO0lkOtH66Xr1oy1dU7-REh3hv0Nad250WkFFcI6QZkvB4uPKwpbWRfXKlVqfor9mziq_vrgzYmZbIRl8D1HrkS_a1ZClA72VzTX4c4ywYt-YnzCyP6c0vHGmdR5vtZg3jrT1u_5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی آقازاده‌ها میفهمن بعد توافق قراره پول بیاد به کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128852" target="_blank">📅 11:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / گزارشات از پیشروی ارتش اسرائیل به سمت ورودی علی الطاهر در لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128851" target="_blank">📅 10:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128850" target="_blank">📅 10:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ناتو: توافق ایران گامی مثبت به سوی ثبات است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128849" target="_blank">📅 10:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سازمان هواپیمایی: یک میلیون بلیت پرواز در ایام جنگ لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128848" target="_blank">📅 10:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcba069447.mp4?token=R9yUBO9WhaRq0ldPilD6N5B2zdMqJbJ4CNq35gxjtx_z6f07hQryqt4X45jAzvYIspJCnzSJEydf4DmACjLVprBQkByLMdrihYc0zweobm8G40KGeoogpCIp-2S_JHimzR39AAi4girdiVvTLLSBaLH9tMnyf5v0yWLwD9t8RLemgSls97owfv4rhzlb39zqfvvQdAUNUXmdi3XNJcshPxhRp7zfF7qgrb4lQ8nXhxgqKVhJswGPyyoV6Ixx0EyDOP90LAtWZXAjZNjE1vtkN5DA6R03hgHyUgXQ8c9rwd_LnqMVKHihuXYZcx-rdVoK7r3shUTqv7FAb-sj7lz7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcba069447.mp4?token=R9yUBO9WhaRq0ldPilD6N5B2zdMqJbJ4CNq35gxjtx_z6f07hQryqt4X45jAzvYIspJCnzSJEydf4DmACjLVprBQkByLMdrihYc0zweobm8G40KGeoogpCIp-2S_JHimzR39AAi4girdiVvTLLSBaLH9tMnyf5v0yWLwD9t8RLemgSls97owfv4rhzlb39zqfvvQdAUNUXmdi3XNJcshPxhRp7zfF7qgrb4lQ8nXhxgqKVhJswGPyyoV6Ixx0EyDOP90LAtWZXAjZNjE1vtkN5DA6R03hgHyUgXQ8c9rwd_LnqMVKHihuXYZcx-rdVoK7r3shUTqv7FAb-sj7lz7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد از امضای توافقنامه با انگشت اشاره می کنه و میگه: نفت پایین، بورس بالا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128847" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر دفاع بلژیک: ما یک کشتی مین‌روب داریم که آماده است به محض فراهم شدن شرایط، در عملیات پاکسازی مین در تنگه هرمز شرکت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128846" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بقایی: اسقاط تحریم نفتی ایران از امروز آغاز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/128845" target="_blank">📅 10:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
🔴
مجری شبکه ۱۴ اسرائیل: ویتکاف و کوشنر یهودستیز هستند و اسرائیل را فروخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128844" target="_blank">📅 10:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128843">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اسرائیل به حومهٔ شهرک کفرتبنیت از توابع النطبیه در جنوب لبنان حملهٔ پهپادی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128843" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128841">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29f737682a.mp4?token=TxjjrcmTZ5J0bbic1-xIwgGo_ENLrqlsyOdceBgy_F2me_DiTljYAyoP5rT31uCTQFgqoDNyeGEVUQYyTO1LYi9rEvS7o4Ev-GFXxXuS_hw8j-sZC11-avYUBPTMrG4RvNyW_V9BFVprs2ANIEW0qE7Z_FWqWqTtD-FblxlG4CkH2LVCv9i0MUp8hx-TcwE96swYyji6FetpU8oVuwUXGlTLgDDl9mQE7MEkHMQ7LNqsuuHiIHaV-mvK0XofmGIpQgJwDquIVmuunhPGOwfDyMT1m7-mQ0MX_uqgRtpG65pHzSYXlP-TMubKR0yogCHpPUEXaiSVWAoXIZcskwMJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29f737682a.mp4?token=TxjjrcmTZ5J0bbic1-xIwgGo_ENLrqlsyOdceBgy_F2me_DiTljYAyoP5rT31uCTQFgqoDNyeGEVUQYyTO1LYi9rEvS7o4Ev-GFXxXuS_hw8j-sZC11-avYUBPTMrG4RvNyW_V9BFVprs2ANIEW0qE7Z_FWqWqTtD-FblxlG4CkH2LVCv9i0MUp8hx-TcwE96swYyji6FetpU8oVuwUXGlTLgDDl9mQE7MEkHMQ7LNqsuuHiIHaV-mvK0XofmGIpQgJwDquIVmuunhPGOwfDyMT1m7-mQ0MX_uqgRtpG65pHzSYXlP-TMubKR0yogCHpPUEXaiSVWAoXIZcskwMJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسکو در دود و آتش
🔴
حمله پهپادی وسیع اوکراین به پالایشگاه مسکو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128841" target="_blank">📅 10:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128840">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnsDwYWhKTDaG2q4kr__azc7u9bA9FzaPd6b9aKIf7Clq9ghRMbtHhkbVu0Q5wg_iXnTQLfOGyqMwssf19y0kM2Tb9iSN8rKr6QJA5tqBZvfWCEhtMTP6vRZKMRIYtgU1j9ANpuvjI70bMKNEayUrTHWNg1pqaVLf94wCCbLApTHb61svMARpvosP4XFLmy8G6zwo8IyfEaaPEI16fdoWet5Nk2EA46g6SB0Jv-6QaZud0b7LngISuOraC3TCXIxvvdzLJPrDVG2Pp_DtidcFHqqPmD804rzs3xMUJCDHmcj5HaOO8bNSmEYi075a529IeFPkVUY-wTskUMDGsJ4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردند
🔴
بسیاری از محافظه‌کارانی که از رئیس جمهور حمایت می‌کردند، نگرانند که توافق صلح به اندازه کافی برای بازدارندگی ایران کافی نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128840" target="_blank">📅 10:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128839">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
دولت سوئیس اعلام کرد که روز جمعه نشستی با حضور نمایندگان آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مرتبط برگزار خواهد شد تا مذاکرات مقدماتی انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128839" target="_blank">📅 09:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128838">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVEG8YWzDf-iKcYko94aFOGJoKAUwqdbff0xr3-iO5QDbLbKSB7YujbtSA2t8kY8VXtyVSxbl450sCivdzXG5L6pjdxBMCZt3-K8a3_9uINb-rX8iPRMl8GN7Pm20WP_on4VMwRIbM73E2df78AllFz--BlRf51IO6MqUS8pvCygSXPmUXFkN9N5sliPWkuZ54NNBHjzo6-tnt7pefL2H4MlSUOFo27m9LlUjJo-dRQPeAZAqBtXJKImSdqyAy0CPQCUYNIs-Rdh8dNIkVpnCMXpUGR3kTSl29AGf5Py8A-KGCqQ13BRTjOAXs-kgjPt5pQnOE96K7QW9KQJqQdp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور بلومنتال: سنا قطعا توافق با ایران را تصویب نمی‌کند
🔴
محکومیت دو حزبی برای یک توافق ننگین عجیب نیست که شبیه «تسلیم بی‌قید و شرط» است، نه توسط ایران، آنطور که ترامپ خواسته بود، بلکه توسط آمریکا.
🔴
بیش از ۳۰۰ میلیارد دلار ثروت بادآورده، لغو تحریم‌ها، فروش نامحدود نفت، عدم بازرسی یا تأیید کامل. همه اینها به خاطر وعده‌های مبهم و غیرقابل اجرا در مورد تسلیحات هسته‌ای است که ادعای ایران برای پیروزی در برابر شیطان بزرگ را تقویت می‌کند.
🔴
هر چیزی شبیه به این توافق به محض ورود به سنا از بین خواهد رفت. برای اینکه اثر اجرایی داشته باشد، باید در اینجا تصویب شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/128838" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128837">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCo9ACtRy0aAHQjbE8rnmoAThQuGU0YJpe5djTIGyuL-RxeWZ1KpovffbBwrqtopBWE1JxabHqZKfjKGIgx__kCpNnBM0ArYjRGX9mU3VuhgxyS5F-VxL94rLx5qnxNHMaRW8aveqVj6Za-V9Ukq-E5syS15D1JMSsl-LwzJs8abvcGSsjz9spYrvq_Q-e4YxQBF6TqKGxTcAfYen_pIKVfIHO4lOYbQXVkPsPoT1bz_3gY9JZTFRUnjXYgo8twDZjRZiFGsTEoI5Uv68IZkF4z-oIfpySg2d5NgIYADIlHHpdQurSt8l5wUoH3G_GXQ9tySUoPzaPWTj2ZbrdlfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری متفاوت از ترامپ و مکرون در ورسای
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128837" target="_blank">📅 09:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128836">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
روزنامه خراسان: مراقب باشید در مذاکرات ژنو، ترامپ یا ونس با مقامات ایرانی عکس یادگاری نگیرن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128836" target="_blank">📅 09:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128835">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام کاخ سفید:
امضای رسمی که قرار بود در ژنو انجام شود، پس از امضا در ورسای لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/128835" target="_blank">📅 09:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128834">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
تاکر کارلسون: توافق ایران به امپراطوری آمریکا پایان داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128834" target="_blank">📅 09:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128833">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ارتش اسرائیل: کشته شدن یک سرباز اسرائیلی در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128833" target="_blank">📅 09:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128832">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
الجزیره: موجی از خشم سیاسی واشنگتن را بر سر توافق با ایران فرا گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/128832" target="_blank">📅 09:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات جمعه ایران و آمریکا در سوئیس قطعی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128831" target="_blank">📅 09:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نفت خام برنت ۷۸ دلار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128830" target="_blank">📅 09:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کانال ۱۲ عبری: افزایش نارضایتی‌ها از نتانیاهو در دولت ترامپ
🔴
برخی از اعضای کاخ سفید می‌پرسند آیا نتانیاهو خواستار طولانی‌تر شدن جنگ با ایران بوده تا موقعیت سیاسی خود را تقویت کند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128829" target="_blank">📅 09:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ :  در گفت‌وگو با وال‌استریت ژورنال: بنیامین نتانیاهو فردی فوق‌العاده است، اما گاهی بیش از اندازه شتاب‌زده عمل می‌کند.
🔴
در برخی جنبه‌های جنگ، نتانیاهو اهداف متفاوتی را دنبال می‌کرد و اسرائیل به ایران نزدیک‌تر است و به همین دلیل در برخی ابعاد این جنگ، اهداف و ملاحظات متفاوتی داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128828" target="_blank">📅 08:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: ممکن است رسیدن به توافق نهایی با ایران بیشتر از ۶۰ روز طول بکشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128827" target="_blank">📅 08:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128826">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شهباز شریف، نخست وزیر پاکستان: توافق تاریخی اسلام‌آباد میان ایران و آمریکا با امضای روسای جمهور لازم‌الاجرا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128826" target="_blank">📅 08:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
واکنش مکرون به امضای تفاهم‌نامه میان ایران و آمریکا : این اقدام راه را برای صلح پایدار هموار کرده، گامی مهم در مسیر درست برای هموطنان ما است و به زودی به کاهش قیمت انرژی منجر خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/128825" target="_blank">📅 08:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee38c0f1e2.mp4?token=rQXiWS81QHlBlVWaR4cSZqcfKG9vTvz_6zLe7YYxJfrE5oOZINcMZkqqHooz6G0kXeLvQYXay_zpMYEJQBTELDtdjgDCzS1oIzqJebrfjBD59H3kwYbuvBIR8xl6p7SFUsecxrPsqk1mJMltxR3MTG2OJnJGR_nsPfoUQx6tLJIuM6LbuXTy-lezFn_XCz6vRHAJWhjAlK5lBcNfjadLXS3W9xF1DsaeG0T9pDSHRCpOk0ZgS2ek1az8fSilLK3FKsfIJwgKjlnzZc0CFhi6jjeTCK5tB-jCWAt8PyY-8aT9msbrUit7diZgGwbjay9iEuv4BRVMnSXPJ6Q6KmSYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee38c0f1e2.mp4?token=rQXiWS81QHlBlVWaR4cSZqcfKG9vTvz_6zLe7YYxJfrE5oOZINcMZkqqHooz6G0kXeLvQYXay_zpMYEJQBTELDtdjgDCzS1oIzqJebrfjBD59H3kwYbuvBIR8xl6p7SFUsecxrPsqk1mJMltxR3MTG2OJnJGR_nsPfoUQx6tLJIuM6LbuXTy-lezFn_XCz6vRHAJWhjAlK5lBcNfjadLXS3W9xF1DsaeG0T9pDSHRCpOk0ZgS2ek1az8fSilLK3FKsfIJwgKjlnzZc0CFhi6jjeTCK5tB-jCWAt8PyY-8aT9msbrUit7diZgGwbjay9iEuv4BRVMnSXPJ6Q6KmSYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه امضای یادداشت تفاهم از سوی ترامپ
🔴
متنی که ترامپ در این فیلم در حال امضای آن است به زبان فارسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/128824" target="_blank">📅 08:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stSUKwEhqV-xz5gkSZkHUZK51KZasuXV77DKxe9R3igW8ZkieNbGotDCkb0KCe8FYibgqcsbaIFP4e1cbGmM89rn83vE5iJdb78I-Q4mf4xxIikI21DF_K1-1WF12EkfEXFzKGTuk2YNUloR1YQkYSwf4TKzT2g1wOrUHmailq3UaKbjETjaBELR7eHZ-Weg_u_bW8wy6zcEXGCyVNSZXvqbkZNX6JlxorlczHatlMiNaRdnJQ4ReeVEOeqD_w8ZqhOttlu6BCVW7Enl4SkTPrwurTiMsbKcpcxEPvv5s102UjJeiCFoL_jfhthFiSsMZx_reLw8vZks-9fx9d1aUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظۀ امضای مسعود پزشکیان، یادداشت تفاهم‌نامۀ اسلام‌آباد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/128823" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7HnN2gBCUXmr4yBfl0xGKMXQt_q0qovVVpah01eY7dd-bzVFx6-_bnLkPxnHO8TTkEtEnY0X9K5ZgbQ7MbImtkGky7hRSGRzxGVipMB8vPGWHqkQcCKv0LwK882kSf-NL1ceb4pRku0Q-LFjGchfZnGZ27F13WO5rPOuF1fpV6QHmi8NWeLptia6YsSdU5ju_2K84CmKaD7vWaPcDn8NKztHmvRtt_WvR8874tid9Jekcm4F1as5yfiIszdh_SxZI8rPygcj00Z-7sieAv2Fx-XLzf12EODJ9shFQ-44DEqmqLFY1znazoOk17eAXqGc_LSrzoqOmr4EGljENn32Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
🔴
آنها باید بتوانند دفاع کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/128822" target="_blank">📅 07:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNNUBrtXAQwVtpDt6K0eDr5Vtb0mvn_pdhwl4mjhWHJfAPhU2H8l2UCHDn5jFOdU9z3b-6RBHN0TjpFjL03ZtsNR7-ZOtzzVWYmj0NpK1sUv70NwM3GIYD0HIQAXBD9fDlmlglyM0-NpghtzpVNCtGxizYzVFsMxUgJvdEplzObUkcrxAcZvVccjtecG_HvaauxwH7iT3mTdbLIn0QUHTmb3P1yGhlH1xM9QZg2EAwoBD5hFY6cCQ5cY3JZN-pHV86ch3tLEzPO0t7jTuhYGXgb5NprYV1KRH-c9HEJrtt_kQWs8IZGvbA6E4Sz6Ll_zDLj_nFdSkmEns0EysLcqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/128821" target="_blank">📅 01:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
هم اکنون ریزش شدید تتر و طلا
تتر 152000
طلا 15میلیون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/128820" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjuSe0Kt2Hy4VZppCpxooyT3NMV2jwoQdlxAPW6YVzHDLjCo2iMD2KL2h8vxKCFZ0TewQXtSCdzYn68sfn6s5Zby-vK0MWrGj46SaokWyTTskCmteXI7nXtvtFbEuPLxjiJFnAfIAskmAM-7sb6MuvdVnckUBMhoSm2lubyh5zepKnAts4-cgT-5mYg78DPssm7673DYvAugw_r2VWVUoiv-ASTwZP9PlhPn_aHGKO8_0Lap4o33phXy81IUQ4HO2-NsNAtUR2CO1JKZphs_3Dr2UDf8ddPipS1nSE4eKjLD3LdxQ-jjkEUPk6ZyPnhtD4QXfq45vLrQYTivlScHxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاضی زاده، عضو تحریریه اینترنشنال: کجای راه را اشتباه رفتیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/128819" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128818">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQzWXWzBEJSAddepGlifTe23oI4vqx2biO8i44YI8hdsTnnSwcJvgynr28I9ShwiiQ6MushXLIMHiFJIqiubvOB76t41S0O6Tu2BxruXSIE4rELo7VuuigOQK5vOG5thhX1jztPhjnUZIm657-oYEzN1AUgno6IPULduvfnv8xyJaIsPE9Z_dUJvVHfMidHl6g_JwDRaXBpRkLVzuGCK5JSPRhyMkhmTC6zjcZZYvrt0OFx1QlmCuh1qGNAiIsvoqJUNWACSor5kFszkx5hNrbdEB6_SgyzNpM9XKqegf7L_XAxuEaSF_T7PjJy62U7st5xmQ6zpjmx2oqjzMuARAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: ترامپ شخصاً یه نسخه از توافق رو توی یه مهمونی شام با مکرون تو کاخ ورسای امضا کرد و عکسِ اون توافق امضا شده رو هم برای ایران و کشورهای میانجی فرستادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/128818" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128817">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heztpjVJzGjqiEg6mJPoig0rNG1UGbQ5rtOKHhsHcXbtjAkDTc_cl04QxitRzRr6hGUrfAQ8Vp-liJTZTlQLCzSH1vUD4PlKZr4Kq1jieY8czUss6w384Du3Pa9mEa3qPsXEEaILpsV0_vRhi5B9ZSaBgs3Ms01njgtC_3h117A7H8eqO5iO5jGcxv2HrpuA_nDULXmyTUcCNd9nY1UlAq_IcEUYon0awqAL-ED8megAhXUNmKmcZST_urjlTkjgSJxyDHNDpBl5pMs0QE0y_agjCPKggYLvq5jG81AbupLshyvvgtd_sWyL4BIYE9fGyDPUdI_2FFChh7tClYFPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندسی گراهام: انتظار بسیار بالاتری از این توافق داشتم و فعلا نظری ندارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/128817" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128816">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t646BCiGZqNtXUCe-dRHWY8OfhcZw00CkZLtXFqBZSBDPh4PX8f67CZ9vDPjLeKSTEl3yUrhpzPCuxVIdp1ybW4-0WDHTV7Y25tI6Yda0ND8Su9YK4I20lGTXxeek4b0RAHwHxESZFhi67EFQ759WX4uxCrSlmWFtcYtMhGz3hG5nSeqMTGT1BNyipHre22sVN7rWGdxYE4-BgJ_BTJpmFp5ih69jOeiHNiVD8ORf29Ib9u0VXp0fW_k6_YN7YZ7BzGbmCFPSONN-Ap3O_uIOLSsauMMxQs2H5Fncl4GjTkKI8JMGg0nkJTvEmUjSVVWe2U4eaqxST69B_xLIts83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: فاجعه‌ای بدتر از برجام رخ داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/128816" target="_blank">📅 01:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128815">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:
قرار بود طی ۳۰ روز محاصره برداشته شود و متقابلاً ایران هم درباره تنگه هرمز این کار را انجام دهیم. اما بعد از تحولات مربوط به حمله رژیم صهیونیستی به ضاحیه و تهدیدات جدی که از سوی ایران انجام گرفت، مذاکرات فوری انجام گرفت و قرار شد آمریکا تعهداتش را فوری انجام دهد.
🔴
در رصدی که انجام شد مشخص شد کشتی‌های ما بدون مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما ‍بس از امضای این سند شروع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/128815" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128814">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
تسنیم: متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/128814" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حسینی با یزیدی صلح یک ساعت نخواهد کرد
کسی مانند ما با مثل او بیعت نخواهد کرد</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/128813" target="_blank">📅 00:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در متن تفاهمنامه تاکید شده است که فقط منحصراً در موضوع هسته‌ای و رفع تحریم‌ها مذاکره می‌کنیم.
🔴
از زمان اجرای تفاهمنامه، که الان است، ظرف 60 روز درباره موضوع هسته‌ای و تحریم‌ها مذاکره کنیم. اگر زودتر هم مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، عدد 60 روز منطقی است  و اگر لازم باشد، این زمان تمدید می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/128812" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128811">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عرازش برید خونه‌هاتون</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/128811" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
خبرنگار اکسیوس: دو مقام آمریکایی به من گفتند که ایالات متحده و ایران روز چهارشنبه تفاهم‌نامه پایان جنگ را به صورت الکترونیکی امضا کرده‌اند و اکنون لازم‌الاجرا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/128810" target="_blank">📅 00:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFO5HbXO4lgFmWuY1G8wNSDpkOz7M573joU1wKlp5MHS1BSbz9rDVby98fXsHohSpAEUwpUhrnAhXpCMvalHCp_PTAlA99AuEWCGcZgcQk4KnsXgwwxXTMtxqtLZxZjXWc0orCsuiSM7PXvihD-6fP8EvJT0aHTg1whwBCv40CVz_ZKai7nfMtqy_XSkG2ZMzFtjmJ4-b-8fBRMSMS5qG9xB_4QhipKFljhHn2Wp4dMlZHc7d3lpYhJn2_WzoW7Q8Pq5J9AObquVRi_NUsDFGvapTtlYIU6Ye_pwrOWg8nLFIq5yYpoaJtJtcB4NJll_qk9YaXqE-Rmj3r8KuIwhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/128809" target="_blank">📅 00:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128808">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/128808" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/بقایی:  الان که با شما صحبت می‌کنم احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/128807" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128806">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری/بقایی:
الان که با شما صحبت می‌کنم احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/128806" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128805">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=S7b2Xl7MlDADU6H38_M5-saWjig6hHYD6M4Iz08SVAKGh2CQJKWYJCF5tx-lTs_h7yAgdx7jsEbz7u0OJPVEMsUgIlxeCs0lp9sovomsl2P3Em8uqOL5yh-ahRz2ogy8BX2XC3RKf_HdZENqRNrOXSqBwZCR1YqWqmgw70HHovOJyomcq8ep5vz3Xu43im9Jk5ZCmwFIBRth4vlNJw22AS2uRKu39S4Mf-2ybXUtFUjTQqeKpOIY8r7BhFWxVZ9yhUKzAAIT9BY9MmSlVe8KiClZG8xx8YhRBIlSwcJrRF6IeLpiMbHFO0N7l8Ovdw_pvsjkDVRkCS_CROxiXbEXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=S7b2Xl7MlDADU6H38_M5-saWjig6hHYD6M4Iz08SVAKGh2CQJKWYJCF5tx-lTs_h7yAgdx7jsEbz7u0OJPVEMsUgIlxeCs0lp9sovomsl2P3Em8uqOL5yh-ahRz2ogy8BX2XC3RKf_HdZENqRNrOXSqBwZCR1YqWqmgw70HHovOJyomcq8ep5vz3Xu43im9Jk5ZCmwFIBRth4vlNJw22AS2uRKu39S4Mf-2ybXUtFUjTQqeKpOIY8r7BhFWxVZ9yhUKzAAIT9BY9MmSlVe8KiClZG8xx8YhRBIlSwcJrRF6IeLpiMbHFO0N7l8Ovdw_pvsjkDVRkCS_CROxiXbEXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/128805" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سناتور جمهوری خواه بیل کسیدی در مورد تفاهم نامه ترامپ:
ریگان در قبر در حال لرزیدن به خود است....این بدترین سیاست خارجه آمریکا در چندین دهه اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128804" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf1d3e6ee.mp4?token=HPFKR7F8Kdpwsf1mpX8lCwnMgdgK9js75RvjoMweklg6_ItsGC0Y3PAxmJXoc2p2NRCYtsoGzUeV3M1SQCEgs-wbJv2Qq34TtDeJezSSMGrmw4_CT4Hph9PlAwUjIP-6jMF6wGD1UX83HYAPfNGgMZORzqhit2pBN2A8kD0k-FhirlU-FgA9es9to75azm1sn7hSAFx4XWvrr3Gi5dc36b8rVtiija17c4M7ZqGfBgIJhIwCwbFF0KW6NGI1GBdIR3Mt0hbdu8iCDId-UanHPAtyRq0E4cdukNPKyyqyZ6pmvNuW8KyZJvuBxTNfveJe_qy-s5J0UNRJxceHuZHlnJVqjGP5K1k4Z-_7ediVNraBpn_xNx9VMtihhCvgFza7GUcqd7pyXgZgWM1RhFq4UnZ0-L-kg1-AzWvYSjlvyWfpJtimSQTza9KoVp95drfkmwUy_QmMXmzEYeS1OBvd0aZnoD_i2iOARV3YT5mceegFSA1ss-ZmxjPkyqHkx_AVSKtMUh2QrsxY4VSsaIbZhIYybk70M55NeSLCa7nwP-vseSXBnwkhaLSLFcvz5Pkmz517daeFH3qCQqOEMmMwOSsE4DDesqDcAw9ZOu1_KxgV8fDUT9k1vBeAjEgHOwBOdOxFBgFR6aF-7Zy1p91FoyIb16Mauo497pFKMfS-BWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf1d3e6ee.mp4?token=HPFKR7F8Kdpwsf1mpX8lCwnMgdgK9js75RvjoMweklg6_ItsGC0Y3PAxmJXoc2p2NRCYtsoGzUeV3M1SQCEgs-wbJv2Qq34TtDeJezSSMGrmw4_CT4Hph9PlAwUjIP-6jMF6wGD1UX83HYAPfNGgMZORzqhit2pBN2A8kD0k-FhirlU-FgA9es9to75azm1sn7hSAFx4XWvrr3Gi5dc36b8rVtiija17c4M7ZqGfBgIJhIwCwbFF0KW6NGI1GBdIR3Mt0hbdu8iCDId-UanHPAtyRq0E4cdukNPKyyqyZ6pmvNuW8KyZJvuBxTNfveJe_qy-s5J0UNRJxceHuZHlnJVqjGP5K1k4Z-_7ediVNraBpn_xNx9VMtihhCvgFza7GUcqd7pyXgZgWM1RhFq4UnZ0-L-kg1-AzWvYSjlvyWfpJtimSQTza9KoVp95drfkmwUy_QmMXmzEYeS1OBvd0aZnoD_i2iOARV3YT5mceegFSA1ss-ZmxjPkyqHkx_AVSKtMUh2QrsxY4VSsaIbZhIYybk70M55NeSLCa7nwP-vseSXBnwkhaLSLFcvz5Pkmz517daeFH3qCQqOEMmMwOSsE4DDesqDcAw9ZOu1_KxgV8fDUT9k1vBeAjEgHOwBOdOxFBgFR6aF-7Zy1p91FoyIb16Mauo497pFKMfS-BWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آسیب دیده جنگ: خونه ما موشک خورده و کامل تخریب شده اما مسئولان اصلا براشون مهم نیست و وقتی میریم پیششون نگاه هم نمیکنن مارو
🔴
الان ما آواره شدیم و چیزی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/128803" target="_blank">📅 00:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523f0d92be.mp4?token=b-xduJp-3cog27QvI4BZ70D_gqflfPxtq5NvTHzQyCWLppZLZsX_H03L_KsE1lzb-tj1rWFsvDxL5YUjCQ1HQv5TiAL15M2p4Jhod61vJ-2sWSRKWGssuxUQpOIlO1gifShCYi6NOBPEinGw3NVrJnjQXFcpvFi-jBKa3am4aOySVID___sPMeFUZ4fbMD0reDz8EQcQr5zYMN5EoTQ0IjbVt2vUpmEJlsii6uWuksS1QACBSffbwrihG2iq87IJQL1tAH-zpcIN4z17CHblT_DTPlH6yXQjgy-78Zqr8R3-39RflYD4HoZEd9oUb9s7DmtJbZHIVNWErk3Xyc9HCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523f0d92be.mp4?token=b-xduJp-3cog27QvI4BZ70D_gqflfPxtq5NvTHzQyCWLppZLZsX_H03L_KsE1lzb-tj1rWFsvDxL5YUjCQ1HQv5TiAL15M2p4Jhod61vJ-2sWSRKWGssuxUQpOIlO1gifShCYi6NOBPEinGw3NVrJnjQXFcpvFi-jBKa3am4aOySVID___sPMeFUZ4fbMD0reDz8EQcQr5zYMN5EoTQ0IjbVt2vUpmEJlsii6uWuksS1QACBSffbwrihG2iq87IJQL1tAH-zpcIN4z17CHblT_DTPlH6yXQjgy-78Zqr8R3-39RflYD4HoZEd9oUb9s7DmtJbZHIVNWErk3Xyc9HCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
با بغض: برای من کار راحتی نبود با ترامپ قاتل سردار سلیمانی مذاکره کنم / نفر دومی جز من برای مذاکره نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/128802" target="_blank">📅 00:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128801">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgSAYczpo_yPHShG9s8awlUqaXTiuJrkK70xo5aRitAQNPjfvhjzmT92qtb6eHY5dDSciwgmAQvpOLSaOuvBE8wk_Z-8O7lG00CwN7dj4PRN_ajq1DUHRu14SDKuJPwL0qrl46Lqgmz0N0Wswu9Za_vYYcSYPW5cmehF1BeJY6godTdrsV3lDprEFHMzsgaB-m2BCqrqxj9sxLg8HIvntg6SvnlCWXG7q2hET2no1PE9jMb1wMEJumvIoKo7hx12psKLTByxKs7p9fSnNfYC95aVYoQ_TJACOdgWg6rvKVhRAd9J7EqkV7tdcTnNkv6OUZQotuNGE1brqlJDgdl76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری میا خلیفه بازیگر مشهور لبنانی برای مهدی طارمی:
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/128801" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgzYRFvY1lGsdomfPQwJBUKBYGXStanXHPNRxseYd_ppI3-KYg3vaLfxUNGpCJROPQAVUMOKbiAzDsz9HQwgsrr0qvIxwkCGG3owtnbKrVJa_Hyi9f9bIyS5MK-wjAFBbc6XrXV0LwV5Yc5O0KtPIHnn31mpA22CwKvjKW909BrKwixAGQrSgJOUqe4H8fVFIwloClHZYxA4CDUjjDiHJDf4fpwHtX7IBu-5RaOoiUpl3pxRHcEppjNplMnf8TiUTe2RScBg9GJY5RFBg5n6ZpVV6fUh2t6E5NauRgFS4VRMCAv8gsAp3pkqUKj5nzmh4fZ_92ib2l9lXC2C16u_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a5eac0f85.mp4?token=GMyav2y7d4tX_ecNgRQzVL6LLdQsIX1DMfxKD4HJTRl-F89xoVtz3pb7HZ-yJp5Sw5X6Q9CAD1dcSup74e82Q5-htitpXEgzy-IIUdnzggW9VyVx_ygK8xSdxxYVX_4d8cdX5QrItKMjLhosoh75525gjluacYfZFepDMops-H2bkKUk3DQaHUfR2ZV7ffi4NYyhRLvzZXSZFzwAC8CEXM8hEXVR80fNXoe38Zloh3tpWo-NwfZiMuUDH68fV_6mhog207MlEeZ2vS3jtquJRCHb2reN1F2wI2GQ7stITC_ndeFOa36e933YGoLZWf85ySaM4EZ-hKJFZVTKdw1aRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a5eac0f85.mp4?token=GMyav2y7d4tX_ecNgRQzVL6LLdQsIX1DMfxKD4HJTRl-F89xoVtz3pb7HZ-yJp5Sw5X6Q9CAD1dcSup74e82Q5-htitpXEgzy-IIUdnzggW9VyVx_ygK8xSdxxYVX_4d8cdX5QrItKMjLhosoh75525gjluacYfZFepDMops-H2bkKUk3DQaHUfR2ZV7ffi4NYyhRLvzZXSZFzwAC8CEXM8hEXVR80fNXoe38Zloh3tpWo-NwfZiMuUDH68fV_6mhog207MlEeZ2vS3jtquJRCHb2reN1F2wI2GQ7stITC_ndeFOa36e933YGoLZWf85ySaM4EZ-hKJFZVTKdw1aRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جرمی کلارکسون از مستندساز های ماشینی معروف که در ایران طرفدار زیادی دارد اعلام کرد به سرطان مبتلا شده است
جرمی کلارکسون:
سرطان پروستات دارم، ده درصد از پروستاتم را برداشته اند و اگر همه چیز طبق برنامه پیش برود، در فصل ششم «مزرعه کلارکسون» می‌بینمتان. اگر نه که مشخص است مرده ام. مراقب خودتان باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/128799" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/128798" target="_blank">📅 00:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9TOJX5i4GZQuQLJ8btYLyZqZOqEA-43cDG4RDTMbjXtGkRdBVfFvFZYhtHwu0kn8vt_rxETX334LSbnZrfiCr3Y-vY_tZ4aAGsFPkZrbardGHgowv4ev9JtBAM_dN76TKc-rJ2ObBquAL7n6DG1YwK5SlkRYeEO7sz01ZqENLAOIDomWoBnYHXEBAccVyEKXZo1wToKmLuti4e0jFp6djT-i3Pwl0ayAuzTP03pMBvqUYDWpDHikG2GWR1HinrMg_jBStj6TFXjyYv5ZYcVBBZugsa8xbsiVJaVTIsCXsKl387LyLFYWOSWanHiyPRlOVqLSkghS1NXVglQWNUe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر کشور: ۶۰ درصد مردم ایران امیدی به بهبود آینده ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128797" target="_blank">📅 00:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ebf99a2f.mp4?token=kIapw1radrHSYSypPYrpl6AImTeSxq42JtkMT6c7fLAMjMq6KNxDo0N9feIm_xeI6bgL8YZU7HJZZaEfsgHybRCKfHGiIC_aD63NSuJU6JzdseKhe5CtX3tn0yv-sYbDc3eGxKqYLikMOxOqX1lYU_Srw2T4Ztheax9qQlUVtSD75H1R9RlQkE6h-HOOgl3tRuH0_83DsxisZI-jWye67G3zhEfPwQ3vAe5t-ShJOLXlcMzDKbG2HREs_ARooOjvaxv_Hw5rqR83tor_gJsKR8YDG8dZvjTRXs9EAKM3STgSplFcfdx_zhMTlSVO-DOx2A4bdlRt-P0hmeUnT8S12g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ebf99a2f.mp4?token=kIapw1radrHSYSypPYrpl6AImTeSxq42JtkMT6c7fLAMjMq6KNxDo0N9feIm_xeI6bgL8YZU7HJZZaEfsgHybRCKfHGiIC_aD63NSuJU6JzdseKhe5CtX3tn0yv-sYbDc3eGxKqYLikMOxOqX1lYU_Srw2T4Ztheax9qQlUVtSD75H1R9RlQkE6h-HOOgl3tRuH0_83DsxisZI-jWye67G3zhEfPwQ3vAe5t-ShJOLXlcMzDKbG2HREs_ARooOjvaxv_Hw5rqR83tor_gJsKR8YDG8dZvjTRXs9EAKM3STgSplFcfdx_zhMTlSVO-DOx2A4bdlRt-P0hmeUnT8S12g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: ما میتونیم تنگه هرمز رو بر ضد آمریکا تبدیل کنیم. هیچ کس به کمک آمریکا نیومد. این موضوع که باید عوارض تردد در تنگه هرمز پرداخت بشه، تثبیت شده در تفاهم نامه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/128796" target="_blank">📅 00:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af930f2ffc.mp4?token=IRHkj28bBQKajiEIpk2JkDHMItQXiAJNQ0sZ8frjxThuyj4ewKuDqF_YOKd-FTsB6LwHIPXECMOXH3QVlifgQiKy4MCUyofPYSyBTRBSajziSLg49Yxn_jUEtaSvi_UaC9A8XoChn8voLgggi9UTgpXSjBqBjKF4o4-GKE4muI14twtqu41_mAQMG51ube892lDJ-8V0HGjDGiI-bLF99nab9xM6yENwW_IFXmWu7LryGYJ7c026kS7rV15NJ2vP3Vv8Cdy5bGFlvMhZeZlYv-ZGD1QBWNVo8hzMa1v89FSi2gr86aHDOhf35OQm8XSVZ8bbqCqrF11LosS9jp3Z66cJZRoRjRxBNLqQ1zahFGMXljptvVc8QzH3mqZk2_m5pJ2yOCulYLprBxpkTotMXiuJ8yNOnwmpM29Od_7Z-cyortircDMT8W-Av1Xo8X7gjVwYWklOobb6wSlm28NehRl6GSRGfZGgdZg4fUOeH6pekaZEnx9O9OW6mHHey7FeRXeORkvYMB8x7rwgrPEBvQvXXgI052Q5wQ83PnCpJ9ncV2trGUqzlDx7kIgqSSRp7J44A-pX-ITlsAcWHk699Vf1ohiU3DtnRJnGicCBaWLr-5GN2_OZe9p7X6VtHBePNB_NCLya82u-Rklp5QxpQYMG2jQcUtN0g92LrEC9CEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af930f2ffc.mp4?token=IRHkj28bBQKajiEIpk2JkDHMItQXiAJNQ0sZ8frjxThuyj4ewKuDqF_YOKd-FTsB6LwHIPXECMOXH3QVlifgQiKy4MCUyofPYSyBTRBSajziSLg49Yxn_jUEtaSvi_UaC9A8XoChn8voLgggi9UTgpXSjBqBjKF4o4-GKE4muI14twtqu41_mAQMG51ube892lDJ-8V0HGjDGiI-bLF99nab9xM6yENwW_IFXmWu7LryGYJ7c026kS7rV15NJ2vP3Vv8Cdy5bGFlvMhZeZlYv-ZGD1QBWNVo8hzMa1v89FSi2gr86aHDOhf35OQm8XSVZ8bbqCqrF11LosS9jp3Z66cJZRoRjRxBNLqQ1zahFGMXljptvVc8QzH3mqZk2_m5pJ2yOCulYLprBxpkTotMXiuJ8yNOnwmpM29Od_7Z-cyortircDMT8W-Av1Xo8X7gjVwYWklOobb6wSlm28NehRl6GSRGfZGgdZg4fUOeH6pekaZEnx9O9OW6mHHey7FeRXeORkvYMB8x7rwgrPEBvQvXXgI052Q5wQ83PnCpJ9ncV2trGUqzlDx7kIgqSSRp7J44A-pX-ITlsAcWHk699Vf1ohiU3DtnRJnGicCBaWLr-5GN2_OZe9p7X6VtHBePNB_NCLya82u-Rklp5QxpQYMG2jQcUtN0g92LrEC9CEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: بند 6 تفاهم‌نامه 300 میلیارد دلار برای موضوع بازسازی و توسعه اقتصادی در ایران تعیین شده!
🔴
در این بند 300 میلیارد دلار تعیین شده تا در ایران سرمایه گذاری بشه که بخشی از آن صرف بازسازی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/128795" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0842a70573.mp4?token=q50V1QPEVnl_MB8m4xQYLcJZlSR9UU_Y8eATeTm3J0SodY_LMQLw2zZy1AOo5oGuIoqsf2TO_3YjUXOPKjqHodDVSpCm97AVRCUoh6OqM5QMtDbWkRHGSvtcdi7i6cAk0u_jJyRdHMogvTk6Ify62JWf7rEfVhbbH5aosPTLNz67XiIQG3M1I-buyW5mJSL79y9nn0oVbyafAWjMXPeWLpC07MqSyhSg2csREMiJfilUq81Sl6eF29ebnsUf-B1ZiUnvzMeJzxXUCcNUUa_3CJ1cJPRDdYEDWbgKo0tLOA7w9hLSxNuBDkspzEJUrdDlgekWzVfX2gCwbV2Lwt9C1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0842a70573.mp4?token=q50V1QPEVnl_MB8m4xQYLcJZlSR9UU_Y8eATeTm3J0SodY_LMQLw2zZy1AOo5oGuIoqsf2TO_3YjUXOPKjqHodDVSpCm97AVRCUoh6OqM5QMtDbWkRHGSvtcdi7i6cAk0u_jJyRdHMogvTk6Ify62JWf7rEfVhbbH5aosPTLNz67XiIQG3M1I-buyW5mJSL79y9nn0oVbyafAWjMXPeWLpC07MqSyhSg2csREMiJfilUq81Sl6eF29ebnsUf-B1ZiUnvzMeJzxXUCcNUUa_3CJ1cJPRDdYEDWbgKo0tLOA7w9hLSxNuBDkspzEJUrdDlgekWzVfX2gCwbV2Lwt9C1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، ژنرال 10 ستاره هم کماکان در حال گذراندن تمرینات آمادسازی برای قبل از مراسم برکناری خود در سمت وزارت جنگ مشاهده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/128794" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ برای شرکت در یک شام رسمی که توسط رئیس‌جمهور امانوئل مکرون و بانوی اول بریژیت مکرون برگزار شده است، به کاخ ورسای رفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/128793" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
قالیباف:
در قوانین ایران هیچ مانعی برای حضور و سرمایه‌گذاری شرکت‌های آمریکایی در داخل ایران وجود ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/128792" target="_blank">📅 00:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128791">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/128791" target="_blank">📅 00:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128790">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قالیباف: وقتی اظهارات ونس را هنگام سوار شدن به هواپیما دیدم که درباره لبنان صحبت کرده بود، پیش از پرواز و در فرودگاه توئیت زدم که تا وضعیت لبنان روشن نشود، مذاکره را آغاز نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/128790" target="_blank">📅 00:02 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
