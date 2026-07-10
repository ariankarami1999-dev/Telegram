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
<img src="https://cdn4.telesco.pe/file/Uey9xI1TvSn_7vJSN913eJJ37MSYbhL6W4N8-K6MJAGj0dyzsCs_Z6YgSEJvslBSaJFnw-QJg9x-ayAWWR-hwsPnz_wR2-r_dc-5OgJdR6-DjygIUUu1hTXCj4NsiXmXU6Eporc059gLDmOSKVYAOWDNgx2EUJqgS_dH9nF9e2p02eUXxWTDMpOl3qSd52OI9HsUoSzB6Fev9NZRba8ugLw0wsx9ZPzqkMQyNMdXvAz8B7GnunTTZ7LGwj3SFftjfRQh9Ime4SDTvIz_rNp8ZQ0CrmaM8NPB4LFYkwTc1kjb7klZ5TzOjy8XkkRuCPKcX6FAfMNgj-iXRERpMZHTEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 20:46:25</div>
<hr>

<div class="tg-post" id="msg-669554">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9bbba72c.mp4?token=ZPjq_Kqdj04Nb5ibr_Dyd0lZUMcmzheVMUZ_Jbz2p8rWhsTr1hG_oHEjjPogurBUusVEUZzUKobWhUAhpmAdrZPCUrHTDUaB8_ld47mtD3U19wZYGnBKYm3GbMFwFzQPDxdZmB9ZTaATeWwUyyrOwInRQu9O0yshfaW0xwgaG7d00H6ugLawcKdyMFcrb9yifPz8T1TPhboIetUsJ1C4CMt3GTjmQXijRnQogpQKYLivduQzfsGR08zgXehjWIOmHrQlPrJkeZ-aiMZ4LTG9hpOKuX5wO96ik7AXRRvmypN6Cwn56y7lM-aNG_hKmyYPzJF4U7yA9t3w6Cmd4c3VEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9bbba72c.mp4?token=ZPjq_Kqdj04Nb5ibr_Dyd0lZUMcmzheVMUZ_Jbz2p8rWhsTr1hG_oHEjjPogurBUusVEUZzUKobWhUAhpmAdrZPCUrHTDUaB8_ld47mtD3U19wZYGnBKYm3GbMFwFzQPDxdZmB9ZTaATeWwUyyrOwInRQu9O0yshfaW0xwgaG7d00H6ugLawcKdyMFcrb9yifPz8T1TPhboIetUsJ1C4CMt3GTjmQXijRnQogpQKYLivduQzfsGR08zgXehjWIOmHrQlPrJkeZ-aiMZ4LTG9hpOKuX5wO96ik7AXRRvmypN6Cwn56y7lM-aNG_hKmyYPzJF4U7yA9t3w6Cmd4c3VEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان امام رضا(علیه‌السلام) مشهد و جمعیت ۸ میلیونی حاضر در تشییع دوباره تاریخ ساز شد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/669554" target="_blank">📅 20:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669553">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شهردار مشهد مقدس از ثبت رکورد تاریخی مترو مشهد خبر داد؛ جابه‌جایی ۲ میلیون مسافر در ۴۴ ساعت سرویس‌دهی مستمر
🔹
محمدرضا قلندرشریف، شهردار مشهد مقدس، با قدردانی از عملکرد جهادی کارکنان شرکت بهره‌برداری قطارشهری مشهد، ثبت رکورد جابه‌جایی ۲ میلیون مسافر در جریان مراسم تشییع پیکر مطهر رهبر انقلاب را حاصل برنامه‌ریزی دقیق و خدمت‌رسانی مستمر این مجموعه دانست.
🔹
وی اظهار کرد: «در راستای مدیریت سرویس‌دهی در ایام مراسم، شرکت بهره‌برداری قطارشهری مشهد از ساعت ۶ صبح روز چهارشنبه تا ساعت ۲ بامداد روز جمعه (در یک بازه خدمت رسانی ۴۴ ساعته)، سرویس‌دهی مستمر خود را با حداکثر ظرفیت آغاز کرد. در جریان این بازه، تنها در روز اصلی مراسم (پنجشنبه)، تعداد ۱,۰۱۴,۹۰۷ مسافر جابه‌جا شدند که با احتساب کل ۴۴ ساعت فعالیت شبانه‌روزی، مجموع مسافران جابه‌جا شده به مرز ۲ میلیون نفر رسید. لازم به ذکر است که این میزان جابه‌جایی در شرایطی انجام شد که میانگین جابه‌جایی روزانه مسافران در شرایط عادی ۳۰۰ هزار نفر است.»
🔹
شهردار مشهد افزود: «این حجم از خدمت‌رسانی در شرایطی محقق شد که شهر با موج گسترده حضور عزاداران از سراسر کشور و محدودیت‌های شدید تردد در سطح معابر اصلی روبه‌رو بود. در چنین شرایطی، مترو مشهد با اتکا به توان فنی، تجهیزاتی و سرمایه انسانی خود، توانست با مدیریت هوشمندانه، نقش شریان حیاتی و اصلی در مدیریت سفرهای درون شهری ایفا کند.»
🔹
قلندرشریف با تقدیر از مدیران، کارکنان و تمامی عوامل مجموعه بزرگ شرکت بهره‌برداری قطارشهری مشهد گفت: «این موفقیت بزرگ، نتیجه همدلی، انسجام، مدیریت میدانی و تلاش بی‌وقفه همکارانی است که با روحیه‌ای جهادی، طی این ۴۴ ساعت به‌صورت مداوم و بدون وقفه، در بالاترین سطح عملیاتی در خدمت مردم، زائران و عزاداران بودند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/669553" target="_blank">📅 20:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669552">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dc68004.mp4?token=aZsR8w3xUV536af3d-OW3aiblWHyBYK-gy_0wLLAsmNr-0LlX5146YZ9-PwXJ3TeghJaWVs9H17NBB6_wa5WZ-WOwqk--bYOVIXAlIdsz_7DjGuED5R2zwmKlvNemOYovD_eXU2XGB2FFvn7OnGpD7z7OXvZG6vzfeu9P60wa-JMRernTpwtXYJu0lWtIW5VrPR8eHhQDIELZAlYJkO00PUIVdK7R7W9cwdww27vay8UkmeuBwiXYJeGfVUXuE-JcFuDTFNxm9Hbx2-mBIN6JMTTO1pB_jCHVPt-663YjrH8H_k8snrLrO4b8oioLdPoqBB_yO9Ua0PcwSMCLO94pKWwkRc-y9qpfkkxu98Tpl0yNDuSmW1U-IziIs-Zo2TVE4dAmo2kqFCoK946bdcJ4BlJbV69KIwgLQr_zcm3R0h-nnIm9DasrjQN3tZ6ZokcMoi7PafNzD-A3WCYkFhP6KTXeCS6qnbQRPvPFBNpIOGnzTZwTav4f35mh0cRmCUtKTYES5ZOKELXur2KHknkl5PxX2LdpgkIFpU5QOPFDpngfPjIkbbm4My0lbDWazuLwFnGpJZc_lpP5SfZQvbmZe4JSj4Oh2-qY4Xe9Jtpvug0Qp6hwD7f5eN8IcKhWMEcwqVZbvp-ItyPokNObV4RR8koNIod4obYYD0hlDTwHCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dc68004.mp4?token=aZsR8w3xUV536af3d-OW3aiblWHyBYK-gy_0wLLAsmNr-0LlX5146YZ9-PwXJ3TeghJaWVs9H17NBB6_wa5WZ-WOwqk--bYOVIXAlIdsz_7DjGuED5R2zwmKlvNemOYovD_eXU2XGB2FFvn7OnGpD7z7OXvZG6vzfeu9P60wa-JMRernTpwtXYJu0lWtIW5VrPR8eHhQDIELZAlYJkO00PUIVdK7R7W9cwdww27vay8UkmeuBwiXYJeGfVUXuE-JcFuDTFNxm9Hbx2-mBIN6JMTTO1pB_jCHVPt-663YjrH8H_k8snrLrO4b8oioLdPoqBB_yO9Ua0PcwSMCLO94pKWwkRc-y9qpfkkxu98Tpl0yNDuSmW1U-IziIs-Zo2TVE4dAmo2kqFCoK946bdcJ4BlJbV69KIwgLQr_zcm3R0h-nnIm9DasrjQN3tZ6ZokcMoi7PafNzD-A3WCYkFhP6KTXeCS6qnbQRPvPFBNpIOGnzTZwTav4f35mh0cRmCUtKTYES5ZOKELXur2KHknkl5PxX2LdpgkIFpU5QOPFDpngfPjIkbbm4My0lbDWazuLwFnGpJZc_lpP5SfZQvbmZe4JSj4Oh2-qY4Xe9Jtpvug0Qp6hwD7f5eN8IcKhWMEcwqVZbvp-ItyPokNObV4RR8koNIod4obYYD0hlDTwHCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلبسته یاران خراسانی خویشم...
🔹
تصاویری از تشییع ۸ میلیونی رهبر شهید انقلاب در مشهد.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/669552" target="_blank">📅 20:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669551">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW5YbUXcDZlS8BXNAdbCGtcn8FuVHVGcSpy3EL377CrC9DyH8hLZb2WG812oMWas7H5N5RiK4MnhCv5o2aHmWLnufOBXhmA7XEd4EEB_0nF5q_duidWNd1TVGggom1N_R371Nu1NyPGZF82CBgWNl76tMgsN8-56Epv9UlNM8NVFgYXIJlIpD3GFBZyXnI90OqkqUrES-GHNz4kUt48aY_K7lkkqAW-g75LhffBVfle5gy5EKihSEusmVs1pRLSHhWh_0SYTR0AmJI_NNI9r79LWNe42SrXALOrATYkpR72drAvSNxqDNV6eLUd4QnSfRM4BFw_LFTxYeLBGx54MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از پزشکیان و ناطق نوری در مراسم ختم پدر محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/669551" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669550">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قرائت زیارت امین‌الله در اولین شب پس از تدفین رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/669550" target="_blank">📅 20:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669549">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
روایت هولناک زنی که هنگام نماز روحش از بدن جدا شد
🔹
00:09:40 عطر عجیب شکوفه‌های چادر روح خواهرم
🔹
00:13:10 القای ذکر "یا ستار"
🔹
00:24:50 حضور موجود سیاه در خانه‌ام به جز حریم سجاده و قرآن
🔹
00:34:30 قرائت سوره انشراح در عالم برزخ
🔹
00:37:30 پرده‌برداری از شخصیت اصلی خواستگار توسط روح مادربزرگ
🔹
00:47:15 عاقبت خوردن مال یتیم
🔹
01:00:00 فریاد ملتمسانه درخت از بازماندن ذکر خداوند در هنگام شکسته شدن
🔹
01:07:50 گرفتار شدن شهید در برزخ به دلیل حق‌الناس‌های دوره نوجوانی‌اش
🔹
قسمت سی‌ام (بی‌نهان)، فصل چهارم
🔹
#تجربه‌گر
: خدیجه مبینی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/669549" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669548">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
قالیباف: تنها کسانی می‌توانند با آمریکا مذاکره کنند که آماده جنگ باشند
🔹
محمدباقر قالیباف در دیدار با رئیس مجلس خلق اندونزی، ضمن تأکید بر بی‌اعتمادی کامل به آمریکا، اعلام کرد شرط مذاکره با این کشور، آمادگی برای جنگ است. وی با شکست‌خورده خواندن محاسبات آمریکا، اسرائیل و ناتو برای تسلیم سریع ایران، این تلاش‌ها را بی‌نتیجه دانست.
🔹
در مقابل، رئیس مجلس اندونزی ضمن تأکید بر صلح‌طلبی ملت ایران، از تمامی تلاش‌های دیپلماتیک برای پایان دادن به درگیری‌ها استقبال کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/669548" target="_blank">📅 20:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669547">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=Cq8QEmza7qSZ9z-h7Gydu9dDBiq8ujLZ9CUsstIyyewKGvonZ4hTNzBJm_qbOcswEGmXMtYNh9AthnPEvH3nSw54JOQprK216kSNwwtzVT_GcrfNlwKewA4tLPod8Sgm_WelA0TrEvQtT2ePAbztbKJEWlkST5w8-_MtGu3JkWW3pVsm75cOk4KYxyyZQKM8D5sTtF4g8njeHbEsobvCJd0PG8yhfsn-yznxLBSrvk9LF0sy1pVGIzzkljU0I7W7Bj7J2OqvpNpDx3GqGNQmvFJCBCB2TqpjjePoPjbFWjc-FJtQEyQJxAVGwuBpzY10B8kewGftdFoonfR805PJvR6T_YUvBeL3ScKMZBsE6xl6LWis6CCKgnD7LtUTtXOj_Ut9DoN-TN6FKm5AFsY6iLyEqzBrnUlXs0Bi5PYVa5w7_X5eSO63nnqAHoOV_ytvooiGU4flK-M38A51hAvZ2M3DE4e1ljAxQy8kWKx3JX67QRg9YiKfaA7Nb0LapdVKOfQasWrOr9vYO1aJZK6rmfNvkrakx05MmyeyQgB4BYOAsbH9VzOF3K1wv63GY5B3Jo7U5yG-KNuko4lchE59ngu23kfzjqCbPg0uPIsQjvsCFSCAWj3BIu8RS2VvPOgnNSFSENmU6n3hT7HQ2uFYjCnk2i_4UfdfPGE_GSGvrgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=Cq8QEmza7qSZ9z-h7Gydu9dDBiq8ujLZ9CUsstIyyewKGvonZ4hTNzBJm_qbOcswEGmXMtYNh9AthnPEvH3nSw54JOQprK216kSNwwtzVT_GcrfNlwKewA4tLPod8Sgm_WelA0TrEvQtT2ePAbztbKJEWlkST5w8-_MtGu3JkWW3pVsm75cOk4KYxyyZQKM8D5sTtF4g8njeHbEsobvCJd0PG8yhfsn-yznxLBSrvk9LF0sy1pVGIzzkljU0I7W7Bj7J2OqvpNpDx3GqGNQmvFJCBCB2TqpjjePoPjbFWjc-FJtQEyQJxAVGwuBpzY10B8kewGftdFoonfR805PJvR6T_YUvBeL3ScKMZBsE6xl6LWis6CCKgnD7LtUTtXOj_Ut9DoN-TN6FKm5AFsY6iLyEqzBrnUlXs0Bi5PYVa5w7_X5eSO63nnqAHoOV_ytvooiGU4flK-M38A51hAvZ2M3DE4e1ljAxQy8kWKx3JX67QRg9YiKfaA7Nb0LapdVKOfQasWrOr9vYO1aJZK6rmfNvkrakx05MmyeyQgB4BYOAsbH9VzOF3K1wv63GY5B3Jo7U5yG-KNuko4lchE59ngu23kfzjqCbPg0uPIsQjvsCFSCAWj3BIu8RS2VvPOgnNSFSENmU6n3hT7HQ2uFYjCnk2i_4UfdfPGE_GSGvrgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما را به سخت‌جانی خود این گمان نبود...
🔹
شعرخوانی حاج میثم مطیعی در مراسم بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان در حرم مطهر امام رضا علیه‌السلام.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/669547" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669546">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhrFtoAbg6_ZKemLWdIxF2H0HmG0p4uJ-uYHwTdPAs2nGN1paAv4ng7a-OEwvRvKO0rajMAcHjmUQAx2jr2S0mK5a51k7EDK9znhMFbiaRzYHCXSJaO7Yjbt9GcGhPs77tR_IXTjytPHWWdEsUrN6lvoyE2BSSN3YgcGXFcI5-fQmE8iNGlXtU8ZqFFRjsYisjWsI2I4d6J7Z7JaQqq2hn73XiSciZ7lGq_LVnBJWEwESfoZZIE37LuialATIZ7aEVBEyul5_SLRmXJwSJ-keq_MxwVyX6N4SYDeu4rfTATTx990kcZx0Eljv7vbQ-4n8Fbbc7gqIiChNRULR16NMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با توجه به اینکه پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی سید علی خامنه‌ای اعلی‌الله‌مقامه‌الشریف و شهدای خانواده ایشان سحر گاه جمعه ۱۹ تیرماه دفن شده‌اند، مؤمنین می‌توانند اعمال مستحبی مربوط به شب اول دفن از قبیل صدقه و نماز لیلةالدفن را به امید ثواب پس از اذان مغرب روز جمعه (شب شنبه) هم بجا آورند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/669546" target="_blank">📅 20:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669545">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d9791b8c.mp4?token=aehq_8Yw2kpSOZw8AaK0_JzIrxcsT9HOHQeOhg5PtXFhYswqXbMVrqknc7nsB9s51gXUnIcqKX4LDfrfoB_ZqpIl2rSPqQl0Yd7Ijm8vnamJZr3RgobhkvUQtMH5LT-1_369nKNIqUI7hiSKfJ3hoLJW3_0toMsHiM8AuWJUOU4WfDsxW4rAfZiT5RWT4rZudn9UcxLJ9hcdZRnpU7rbq3DjBHm4ztBOPMBF9TFl6X6HKTFw5wiKD_R_cR2zSIdWAoMLi7CeQG8Oi5manWY6wBqk7Vjoyvuxv2soLDy104bHI2T_6mBBeR8e0C6mLI1-II9XNwtg6wgu8WKx_E310g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d9791b8c.mp4?token=aehq_8Yw2kpSOZw8AaK0_JzIrxcsT9HOHQeOhg5PtXFhYswqXbMVrqknc7nsB9s51gXUnIcqKX4LDfrfoB_ZqpIl2rSPqQl0Yd7Ijm8vnamJZr3RgobhkvUQtMH5LT-1_369nKNIqUI7hiSKfJ3hoLJW3_0toMsHiM8AuWJUOU4WfDsxW4rAfZiT5RWT4rZudn9UcxLJ9hcdZRnpU7rbq3DjBHm4ztBOPMBF9TFl6X6HKTFw5wiKD_R_cR2zSIdWAoMLi7CeQG8Oi5manWY6wBqk7Vjoyvuxv2soLDy104bHI2T_6mBBeR8e0C6mLI1-II9XNwtg6wgu8WKx_E310g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاوت آیاتی از کلام‌الله مجید در مراسم بزرگداشت رهبر شهید انقلاب و شهدای خانواده ایشان در حرم مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/669545" target="_blank">📅 20:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669544">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
این حمله آمریکا به ایران خبر از یک جنگ جدید می دهد
🔹
ترامپ بارها گفته که اگر ایران شرایط ایالات متحده را نپذیرد و آمریکا مجددا وارد جنگ شود، این بار پل ها را هدف قرار خواهد داد. این تهدید ترامپ نشان از این دارد که ممکن است در صورت ازسرگیری جنگ، شاهد نبرد کریدورها باشیم.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3229282</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/669544" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نمای دیگری از مزار مطهر رهبر شهید انقلاب در رواق دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669542" target="_blank">📅 20:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پاسخ به چندتا سوال ساده میتونه تو این روزای بحرانی سرمایه‌ خیلی‌ها رو نجات بده
ما در حال بررسی دغدغه‌های مردم درباره امنیت سرمایه توی شرایط بحرانی هستیم. تجربه و نگاه شما می‌تونه کمک کنه این مسئله بهتر فهمیده بشه و راه‌حل دقیق‌تری براش درست کنیم.
اگه چند دقیقه زمان دارید، خیلی خوشحال میشیم، این پرسشنامه رو پر کنید.
تکمیل پرسشنامه
ممنون که توی ساختن یه مسیر امن‌تر برای سرمایه همه هم‌وطنامون همراه ما میشید.
❤️</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669541" target="_blank">📅 20:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9075da9719.mp4?token=ZYqiIUnuVaJ2LRhv8M9SSB_qvlQZjeVJxM3Pmtl_4AqCzZl9Bc2qTsdZtPXi0JEzsLuvLfWyC3UNUHhQnxZ3JY3EX4HynVe_hBXVJYK7ogALdCPuhg-zlO348SNV6ZWbJ3_xjTY_oklNSmbIa6qlGhScT9sUquTeQjxG38P_G7ogBGyISSfSKKaruuq1PlS4D0JG4mxjNPrBg0-5thXIIbsJsMU56omsr18CZjXr5d4uLglSm_o-Pu7-ku35T5PnrKZVWWWRmOjoydaYfp8rkUwVGG0xzvQ0khmMAfMZnstSVKzpK6exA23xD5yPt1dXtfyCXMwUd_Z1FPqEzFZntA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9075da9719.mp4?token=ZYqiIUnuVaJ2LRhv8M9SSB_qvlQZjeVJxM3Pmtl_4AqCzZl9Bc2qTsdZtPXi0JEzsLuvLfWyC3UNUHhQnxZ3JY3EX4HynVe_hBXVJYK7ogALdCPuhg-zlO348SNV6ZWbJ3_xjTY_oklNSmbIa6qlGhScT9sUquTeQjxG38P_G7ogBGyISSfSKKaruuq1PlS4D0JG4mxjNPrBg0-5thXIIbsJsMU56omsr18CZjXr5d4uLglSm_o-Pu7-ku35T5PnrKZVWWWRmOjoydaYfp8rkUwVGG0xzvQ0khmMAfMZnstSVKzpK6exA23xD5yPt1dXtfyCXMwUd_Z1FPqEzFZntA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقامه نماز لیلة الدفن رهبر شهید در حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669540" target="_blank">📅 19:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669539">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سگ زرد به نیویورک پست: در صورت موفقیت ایران در ترورم من دستورالعمل‌هایی برای اقدام صادر کرده‌ام
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669539" target="_blank">📅 19:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669538">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c806945c6.mp4?token=YURbtgPFqC2VzgFk1s8CN4dFi6L8aOyHt21_Y7UhsYWB470nOBpbM-oFxvX4m1Q2IJPyssDWKpcgyzHpNkQ4S3xDi_nQuhtZARt-Am6lvY6qwE6XIx1Nb_JBENycpD07nA5oHXRHsVZNeGJ2GTeuZsU_eFFPR4NCzpkpYRy6ck38iS_9MZjy9MDENMG-PRWHjFApqzfJCzCI5JJ-MrDmU7P54ATcJafME_nDRy0tjxtxe3e7ESBWZzsgwtuz_K7hvOXReOWM-sXu26GxpsUDfsCqAXjCgo8vq-1z18522p_jB6AMbJRuQ-xMU7x1uxmIUfa2npDCy0Y0hoSiIsPNbz9pzdQGQIlOM2sex5wqLk33ptCZoCmhUXxJUysLCrgju3xq8umts2CPEqrV6xkGQ5T2YWTllrF_P-QoLqEd7IdrMJOnMim2hoEueItJoJ8_f0_8vuylSDJNBPCb6vd3pG6OvJ9sUcKaBcBTELdUKAt0Whb-OWZ-2v2ZBhXhMVZQxwGYWgg0VAxEPKQ_EHXguRwSZUF71NNy4IO1EK6smiwo4zTwMQzn3BHfutA_ImvqFSzWTTaFINOlTw2H1Oej0DkWzzfuodNzzRS5fvG3yT4sAIj7jeO5s-kbHiyrDlFQGGntBamIJI73IfETYj5VaHD5SlWVJh9VFrUzme1uLA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c806945c6.mp4?token=YURbtgPFqC2VzgFk1s8CN4dFi6L8aOyHt21_Y7UhsYWB470nOBpbM-oFxvX4m1Q2IJPyssDWKpcgyzHpNkQ4S3xDi_nQuhtZARt-Am6lvY6qwE6XIx1Nb_JBENycpD07nA5oHXRHsVZNeGJ2GTeuZsU_eFFPR4NCzpkpYRy6ck38iS_9MZjy9MDENMG-PRWHjFApqzfJCzCI5JJ-MrDmU7P54ATcJafME_nDRy0tjxtxe3e7ESBWZzsgwtuz_K7hvOXReOWM-sXu26GxpsUDfsCqAXjCgo8vq-1z18522p_jB6AMbJRuQ-xMU7x1uxmIUfa2npDCy0Y0hoSiIsPNbz9pzdQGQIlOM2sex5wqLk33ptCZoCmhUXxJUysLCrgju3xq8umts2CPEqrV6xkGQ5T2YWTllrF_P-QoLqEd7IdrMJOnMim2hoEueItJoJ8_f0_8vuylSDJNBPCb6vd3pG6OvJ9sUcKaBcBTELdUKAt0Whb-OWZ-2v2ZBhXhMVZQxwGYWgg0VAxEPKQ_EHXguRwSZUF71NNy4IO1EK6smiwo4zTwMQzn3BHfutA_ImvqFSzWTTaFINOlTw2H1Oej0DkWzzfuodNzzRS5fvG3yT4sAIj7jeO5s-kbHiyrDlFQGGntBamIJI73IfETYj5VaHD5SlWVJh9VFrUzme1uLA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت سه خواهر برزیلی در کتاب گینس
🔹
سه خواهر برزیلی به عنوان مسن‌ترین خانواده جهان در کتاب رکوردهای گینس ثبت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/669538" target="_blank">📅 19:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669537">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تکذیب شایعه مذاکرات جدید ایران و آمریکا
یک منبع آگاه در تیم مذاکره‌کننده ایران:
🔹
ادعای العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات در هفته آینده کذب است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/669537" target="_blank">📅 19:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ce956558.mp4?token=XggMJFY0SOC8c84o-5CXS9TAX_TNBGJb6Rg4V75BEb_WwdoaQPKyDHIa7xmpsRpjOkPNFPWMUmWNlpL2Zz6f0s0hBeJIfUXwUW3hyMWc6YL-No2iwwet1XnrudHna_YaR9vDDBkAkxIadwcflEN0t0ah5n5insfCPATyrHdiXC3v-He29GqJoGhvHBUVWPz_MNjD1sKFEYbmlbFPZRvgCCVq7zChqmFFV__icKaXwkRoRhMMTs0G-Eg_GnNun6PkqNxmZ6Gi0jaMSOGEbhxDXhcW0TFAji5xd0743l2sSSDJ7L8pc2rjIUDdPwRIo3Bnt1jm19VA1OkSgXNvzeAF64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ce956558.mp4?token=XggMJFY0SOC8c84o-5CXS9TAX_TNBGJb6Rg4V75BEb_WwdoaQPKyDHIa7xmpsRpjOkPNFPWMUmWNlpL2Zz6f0s0hBeJIfUXwUW3hyMWc6YL-No2iwwet1XnrudHna_YaR9vDDBkAkxIadwcflEN0t0ah5n5insfCPATyrHdiXC3v-He29GqJoGhvHBUVWPz_MNjD1sKFEYbmlbFPZRvgCCVq7zChqmFFV__icKaXwkRoRhMMTs0G-Eg_GnNun6PkqNxmZ6Gi0jaMSOGEbhxDXhcW0TFAji5xd0743l2sSSDJ7L8pc2rjIUDdPwRIo3Bnt1jm19VA1OkSgXNvzeAF64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوهٔ خردسال رهبر شهید انقلاب، شهید زهرا محمدی گلپایگانی همراه پدربزرگ خود، حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای در یک مزار به خاک سپرده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/669536" target="_blank">📅 19:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832ce6082.mp4?token=NSIF1OpwW7MtkOAx_5snBFkBeKJ3yc81esAN57kmp_0U1vO-i0EpRg0POZVKwz1n92Nw9Ea9d22a6NrmCFHhJSzS9v_rPPFRwaWwUZUl_nGB7ZMu6wcHmL_LeRzZyqT2H0VEvXLNCHpDQxieTESxpxfuqezCMWnhzmlmzDxUBRYHu8RVtt2Ju1a6SEDzGNuF2W0Fsa9DLATStNRq-joNljCKz2xhlmfuVKrcalelrPv1DcMhtP9i0ebkwrT1_2Qyv9UaFVbQjuOlK1e-pUWyw0t_c4rhIRmmdjpXjGCJeaMLiOvkiVzIeb38f776Hxe67MtFuhOIGB-scQ4haFBEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832ce6082.mp4?token=NSIF1OpwW7MtkOAx_5snBFkBeKJ3yc81esAN57kmp_0U1vO-i0EpRg0POZVKwz1n92Nw9Ea9d22a6NrmCFHhJSzS9v_rPPFRwaWwUZUl_nGB7ZMu6wcHmL_LeRzZyqT2H0VEvXLNCHpDQxieTESxpxfuqezCMWnhzmlmzDxUBRYHu8RVtt2Ju1a6SEDzGNuF2W0Fsa9DLATStNRq-joNljCKz2xhlmfuVKrcalelrPv1DcMhtP9i0ebkwrT1_2Qyv9UaFVbQjuOlK1e-pUWyw0t_c4rhIRmmdjpXjGCJeaMLiOvkiVzIeb38f776Hxe67MtFuhOIGB-scQ4haFBEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای زیبا از تشییع ۸ میلیونی رهبر شهید انقلاب در مشهد
🔹
کمک امدادگر به یک زائر سالمند هنگام نماز ظهر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/669535" target="_blank">📅 19:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام ارشد سازمان ملل: دیپلماسی همچنان تنها مسیر ممکن رو به جلو در خصوص ایران است.
🔹
اشپیگل: آلمان نیروهای خود را از شهر اربیل خارج خواهد کرد.
🔹
قطر بر حمایت از توافق جامع میان ایران و آمریکا تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/669534" target="_blank">📅 19:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfrXttDWo1LFSr3Kl6R6_e5PJ-3yYTe6u8Lh6T0dngsC0jyDKuknlGggmTlquL6HK3lTblWTYqXy-Ocdnb5bLo0gf6a6qdjJfg0DaVz8g0YKGRbB6u64GJXc749QiMuMi14SDqKaRtD92k5twWsWPP54YLuMbrmezbKgbB-WlthMJMRSBFEESnqu2xyDdSBXShSajjw2mK0Zg0JgTFMAkxw7VzpK1cAPNZIapPTK5zN6BpDIMpraEdkAUPLg6hSnv-yIk_PmCbk43eclEnJLUxdYxqiZpnaD6_MWUzwFtPtcEVJ0IHpdlXHIXl-RsnbuFvvD8WpOw_JuQfXGnRyVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️
♦️
بازیکنانی که در یک دوره جام‌جهانی بیش از ٨ گل به ثمر رسانده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/669533" target="_blank">📅 19:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnvr0KKcw8E4CqxmxXbs0J_3gxyfydQ6NPPiUn5dRxA7xrVaxbMh6FA2ODyvPonHD4Y4IpkruEoabPSqsh7ZHYsfXqMW3NTrEQCkjz6xMXR8W6VSn-abwqSiqzlcSqbfjrvx2DMqKSTvKKBsQEk7nXTKep3gQwBDGTT5jeBXbYrnkBNBodSn3E4Pi-WnoXAIkdyD19pFz1BPXFvdxmHAYKEZw3FI5phFrCdKPLnvwjO_yshoisXkBQeX-QnQW_koNsrEt0PHszIud-5MEJ6U1thU6j95-CtdOX5QEtGe0F9sfvdLYGBQ1jn1xdlpaOGghHRWEZZIBKT5fHW--rJsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه آشنا به سعید جلیلی
🔹
۵ حق ملت و وظیفه دیگر مسئولین را به ترتیب اولویت نام ببرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/669532" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بلافاصله بعد از غذا ۲ لیوان آب خوردی؟ داخلش قشقرق به پا میشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/669531" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای آکسیوس: هفته آینده مذاکره ایران و آمریکا در سوئیس
🔹
رسانه آمریکایی-صهیونیستی آکسیوس به نقل از یک منبع آگاه مدعی شد:
انتظار می‌رود دور جدیدی از مذاکرات ایران و آمریکا هفته آینده
و احتمالاً به میزبانی سوئیس برگزار شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/669530" target="_blank">📅 19:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669529">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0W2LyLHqWj9tBnXIQQOi9jwnGCz1rY6zFC7ADRDM3fzGTHLNLXWduMXPD3DS8KVMFeG8vk8CIrCBPpxjwAV-jsWRee1V6Z7TUcL5drwHVazDqZ6DdVBAOerZydlAhr4D5eb-sd2rbLIoYSb014j68DLyF32NE1AdFHGU6ggaaQ8D7Vmq_3ROVHhqbxnf5ofEg2VxDYrK9pXo0Tz7okAWGxIHOHVR9pSrABv6rTLtxP-Tp4v0k73ebo6Yh_-PCCuK68lkIF1EhEx_oElnHd0eYEk0LSA1BgfGZ6UBWu017l5-tOL826ScWswbNvfD-hOzUBMpT33qIZRtcAaYWRIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ تیم حاضر در مرحله یک‌چهارم نهایی جام جهانی، از سال ۱۹۸۶ به بعد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/669529" target="_blank">📅 19:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669528">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q14276Gps1KbI6UkK1Q4zw0xWL2P9uwyIcFpcT0H7dCjLG_koFVKFYJotQUZYUGCYYXgaSeFCuIM278r1LJQKn89BBNGipCb0ejFK243SmvdpXgiYOwAR1v4L-x3Sn-zosk1GD9bodfge5v5U_du72ZM8Ypw24KNmVmRsFSxYDOrW4ltPyY-Kf8Ut5KZgKSBOiQ-li5mCxO1Wto0FfNPNoMN21bvF7On60b_9H2CBfJNYEmnkC4-lwpH62ZnYkrISWLoUXWVlbyEXXHnxGg5wOcPW9DzUjy1zHJVSePDcDszlWgOk7vzlX3PsJVjMr6gmFVEAgle1Ho0zP_2Z48dHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/669528" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/669527" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669526">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f37a4c15.mp4?token=ZBQSh_MzKj_j1wbOj8ttsL0duIb9aZVHxbNMp-PJKsjqgkYoGTwo2zADso5bCeMREhkdRzBvk_kf68Ta6L4MYxhMm13mqbmMMy1yonKyvaj_FMvnRSB3Yk3cx7iqnZVmCdMfnrPoRNZtJFd-GJ_INouBK-R_O7HCU1CKXRa2fJ-LU5XBDF1N99Pj9CUXthFXuZpwGLUC34l7avtfCSh70cSJsEMgspxyTrZJR0JAEP7m_b7FgM5aYCc0fxIxB3jTghZlwa-RNyypnZTPwhGmFk9nYEpluiEPMyZUhu19tfRjEb32RtUWPH0GgTBAmVc_mugYz-eX45tqOIuKkYbjWRukRi0cJjYojFXWk_WOvPHUZhPWjSChjqF8So4ofB5KOqGMlEJ7933vOlxSd3mRpTpdSd8k1kh1_ATjhqfhhbZvZ6-lghqYPePSTxhoN4kiTi0uwT_NgJxJ5qD_NuP4iSg22vo4Qasc6UFXMVoXkaclCpihNRyrhn_4sSIVIxG5-cFVgkw0y-bpbd5lE7gJers3W2JtciXFE3nyBYnkPY5rtZBsrBi-icfxb0zMSRT6Il9qq7i1cOc01HfC6wXNANFoOqFZgqVWOHGUl6Qij5j5AO28Buyiwao2LNZE5ls14WqL0V4kDVwS9UxejNzJG-1sj265ocnP9KM62NMOf7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f37a4c15.mp4?token=ZBQSh_MzKj_j1wbOj8ttsL0duIb9aZVHxbNMp-PJKsjqgkYoGTwo2zADso5bCeMREhkdRzBvk_kf68Ta6L4MYxhMm13mqbmMMy1yonKyvaj_FMvnRSB3Yk3cx7iqnZVmCdMfnrPoRNZtJFd-GJ_INouBK-R_O7HCU1CKXRa2fJ-LU5XBDF1N99Pj9CUXthFXuZpwGLUC34l7avtfCSh70cSJsEMgspxyTrZJR0JAEP7m_b7FgM5aYCc0fxIxB3jTghZlwa-RNyypnZTPwhGmFk9nYEpluiEPMyZUhu19tfRjEb32RtUWPH0GgTBAmVc_mugYz-eX45tqOIuKkYbjWRukRi0cJjYojFXWk_WOvPHUZhPWjSChjqF8So4ofB5KOqGMlEJ7933vOlxSd3mRpTpdSd8k1kh1_ATjhqfhhbZvZ6-lghqYPePSTxhoN4kiTi0uwT_NgJxJ5qD_NuP4iSg22vo4Qasc6UFXMVoXkaclCpihNRyrhn_4sSIVIxG5-cFVgkw0y-bpbd5lE7gJers3W2JtciXFE3nyBYnkPY5rtZBsrBi-icfxb0zMSRT6Il9qq7i1cOc01HfC6wXNANFoOqFZgqVWOHGUl6Qij5j5AO28Buyiwao2LNZE5ls14WqL0V4kDVwS9UxejNzJG-1sj265ocnP9KM62NMOf7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ تشرف زائران عزادار به رواق دارالذکر برای زیارت مزار مطهر رهبر شهید انقلاب اسلامی.
۱۴۰۵/۴/۱۹
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/669526" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669523">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icXXzrL6vrsQBad4asYL5aBUDxKToLhyUfDNmjQH6s9NLeZDulf-xGEsFqXEhSFdHucMoqtDth8poqnHhGoCELoiNYb7wAH_94NL2SRF-UuNlOJLz_N9Wwthvgz7ZT5Nc0N1vhfbXdqzTuNCOu6Z0XfszS0eLN1p6KzwOY2ZppVdDdr0ZICRqs5GptQwAEGSbDaYDF0_Fzv5H88A0JCWIS6tbFDQ1Bp2-O70uJzJTztgo1VaUBxci8-cpGigoLA_zOzPlF8VPNjOqzFqCvqGS6iIIzVSY84L4j0HwGwKQFZ_qqsSAnYoErEkhw1RgNjFmdtE3TwAlj9Ne8mzpHCNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNQe-UHjai5fpqgR_klMT985K7-Ctuc6Jwk4p1LzlGhq38beMZm5MNRpwxQHPZgg0oAS_eRpugPxa6e3zQadsFvqZXEgnwcg49JsNeteHjroVglCw9JLCFFksAX3WUCDo8pQfgCpdUKZNl-IJkhReugEq2TjVsi8VqiDzt_9gWbzve-SkLvFw9aQQC1yGlNOEAfhwHi1qQJVEFo53nHZYLs9Yipx53moGkpNn4ZirqQYfY4g50J9FUJZISECyxGQ0BV7Ug0zZKG49iGlag5GPGhLApYfo82u5NFU631bjV9bDAne-bBfImeQ2-bvlh9t4rDBuQtAAVGba1VejaSLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4SXIUpli_ZS1KIkJpiX8u8Vboe1em501rH13dXrna_ETzcaAz_L-QHe9cMsf7tUswEVJyuVAb_BmIQnehGbjFZuO0tjasCRLxqOJbwo_E1zj9_aRlLQtW_UCwHVI1j2KJQcfq9ZXHNLo0SwSZ5HO4UCi5YH8b_DmoSH3B3miBsTBp5FV5zgXiOSz1M_G98Ts07YEw5BoY0PLWMOoQT9kA7EqGBVh9LYMDcfnLmHCbj6qOvf41TUUce1duOStnQhJjp2bZlF0xTBMf7xHv8_05K40AgPJhoOdcLOeUFGZlGhU3yNp62o30nQJBnErb_STfnoVlYXVNn2VEKwCbfnzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خودنمایی پرچم ایران در تجمع امروز یمنی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/669523" target="_blank">📅 18:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669522">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
نماینده چین در شورای امنیت: قطعنامه ۲۲۳۱ منقضی شده و بررسی پرونده هسته‌ای ایران پایان یافته است  نماینده چین:
🔹
قطعنامه ۲۲۳۱ در ۱۸ اکتبر ۲۰۲۵ منقضی شده و رسیدگی شورای امنیت به پرونده هسته‌ای ایران پایان یافته است.
🔹
اصرار برخی کشورها برای برگزاری نشست درباره…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/669522" target="_blank">📅 18:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669521">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
خوک زرد: من دستور بمباران بی‌سابقه ایران را در صورت موفقیت در ترورم صادر کردم
🔹
هیچ برنامه جدیدی از سوی ایران برای ترور من وجود ندارد و تهران سال‌هاست که می‌خواهد مرا بکشد.
🔹
مدت‌هاست که هدف اصلی در فهرست ترور ایران هستم و اسرائیل هیچ اطلاعات جدیدی ارائه نکرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/669521" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669520">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بندر دَیّر داغ‌ترین شهر جهان شد
🔹
براساس آخرین آمار پایگاه بین‌المللی هواشناسی «Ogimet» که وضعیت دمای ایستگاه‌های هواشناسی جهان را رصد می‌کند، بندر دَیّر در شبانه‌روز گذشته در صدر فهرست داغ‌ترین نقاط زمین قرار گرفت.
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/669520" target="_blank">📅 18:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669519">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نماینده فرانسه در سازمان ملل: ایران باید حمایت از گروه‌های مقاومت را کنار بگذارد/ ایران تفاهم‌نامه را نقض کرد.
🔹
مصر و قطر خواستار بازگشت واشنگتن و تهران به مذاکرات شدند.
🔹
تیم المپیاد ریاضی ایران قهرمان چهارمین دوره مسابقات بین‌المللی ریاضی در شانگهای چین شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/669519" target="_blank">📅 18:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669518">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWXPVWsLx6ICmUck8QR969vzTVUt96TqB8kJRZiITvH_sd4Vuvmg821kPPMHuzhOTG3AYrtpRvgcU2YdE5KpV003K-wO32MYdGo3gVA10qLOlg08KAcqnPK-bL2h2C1ukWIKyuo836xHZBzJL_JC4Ts0KQF-qRv7NJgrKSuoju0taxYpTblNACQmlCI14rXBl3qeXppA1UZSiVgb4i5IBJApny5IzncgtivSF9L4GPz0YcMKZGCCFV9paZR63IMlkl7Fef6LdvE82Y0Ej97E8OxGuW_smH6U64tzK9vhaHYnJiOP1cVnxkCLEVzsddf_6BpwYA0VQ5IXi3ZwIkC2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روی جلد نشریه اشپیگل: محور شرارت!
🔹
تصویر روی جلد این شماره اشپیگل با عنوان "محور شرارت" با اشاره به اسنادی محرمانه به برنامه‌ریزی راهبردی، تبادل اطلاعات و همکاری‌های دفاعی روسیه و چین برای مقابله با نفوذ غرب اشاره دارد. همکاری که می‌تواند بر موازنه قدرت جهانی تأثیر بگذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/669518" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669517">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57ad67f6e.mp4?token=OdpOo96_ZQfn5Lk5-Z-tY5fWHHbkBatHZmc3VX6Fzreo2PqEDSreZfWGcso1fkoltSnuvkPTK1ZxZsvIVJvCHPa_1i1XZAo7feR-Z8dmgDG5Jpnx3016KQUbj30xpus8gUXBy1vSHg2th-IlO13cBJR_z1qrPNj0rYiv8M9Z1bxIltqLRQ7NRDKLQfarb4l9itaMpX6Mx01TbyCgCRd80TTsu-DkoSMoPwaXTZ5IRZFnpcG8hZbTNgcwg7uopnKOVePsaqLJoU899hLoKosjnMbsGKaV-VCspCpyXp7gHVcqYTZrzhmotz9squE4qFYw_Oc06KWb4EcBy7tq-O45XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57ad67f6e.mp4?token=OdpOo96_ZQfn5Lk5-Z-tY5fWHHbkBatHZmc3VX6Fzreo2PqEDSreZfWGcso1fkoltSnuvkPTK1ZxZsvIVJvCHPa_1i1XZAo7feR-Z8dmgDG5Jpnx3016KQUbj30xpus8gUXBy1vSHg2th-IlO13cBJR_z1qrPNj0rYiv8M9Z1bxIltqLRQ7NRDKLQfarb4l9itaMpX6Mx01TbyCgCRd80TTsu-DkoSMoPwaXTZ5IRZFnpcG8hZbTNgcwg7uopnKOVePsaqLJoU899hLoKosjnMbsGKaV-VCspCpyXp7gHVcqYTZrzhmotz9squE4qFYw_Oc06KWb4EcBy7tq-O45XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کپلر: فعالیت کشتیرانی در تنگه هرمز به شدت کاهش یافته؛ تنها ۲۲ تردد تأییدشده در روز پنجشنبه ثبت شده است
🔹
تنها یک شناور از کانال متعلق به عمان استفاده کرده و مابقی از مسیر دریایی تعیین‌شده توسط ایران تردد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/669517" target="_blank">📅 18:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669516">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
بنابر اعلام منابع خبری، روسیه و چین بحث درباره برنامه هسته‌ای ایران در شورای امنیت را رد کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/669516" target="_blank">📅 18:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669515">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
بنابر اعلام منابع خبری، روسیه و چین بحث درباره برنامه هسته‌ای ایران در شورای امنیت را رد کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/669515" target="_blank">📅 18:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669514">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">وه که نشسته بر دلم، مِهر تو و وفای تو
هر نفسی که می‌کِشم، در هوسِ هوایِ تو
گنج نهان من تویی، قُرة اَعیُنَم تویی
سائلم و نگاه من، بر کَرَم و غَنای تو
ماه مبارک جهان! عید سعید لازمان!
دوخته خَلق چشم بر، نغمه‌ی ربنای تو
شاهِ شهانِ عالمی، پادشهان عالمی...؛
دستِ طلب نهاده بر، گوشه‌ای از قَبای تو
سیبِ درختِ طیّبه! آدم اگر هُبوط کرد،
رفت که تا گذارد او، پای به جای پای تو
دل که به آب می‌سپُرد، نوح پس از هزاره‌ای
در هوس کِناره در ساحل دلگشای تو
آتش اگر که سرد شد بَر تن بت‌شکن، یقین؛
بُرده به لب همان زمان، ذکرِ گره‌گشای تو
تِشنه به شوق دیدنت، هاجر و طفلِ پاک او
مَروه به پُشتِ سر دوان، در طلبِ صفای تو
یوسف اگر عزیز شد در دل چاه، بی‌گمان،
خوانده به اَشک دَم‌بِه‌دَم، ذکرِ فرج برای تو
نیل به پیش و پشت سَر، لشکریان و بیمِ جان
نام تو برده زیرِ لب، هم سخنِ خدای تو
عیسی اگر که رفت تا، کور شفا دهد؛ فقط
چَشمِ اُمید داشته، بر نَفَس و شَفای تو
بر همه چَشم بسته و دست کشیده از همه
هرکه به چَشم دیده آن، چهره‌ی دلربای تو
ای که ز دیده غائبی! در دل ما نشسته‌ای
باغ و بهشت من شده، سِدرةُ مُنتهای تو
ابراهیم طوسی
"خاکستر"
#من</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/669514" target="_blank">📅 18:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669513">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULlnyZ4h0WWb2i8N6uUY3BC9lflJzZr2TLg5jJmWOQSAUsP3VMUDmy_nE8GzH0epNO_YFc2X_ovDE5MTSTAPmYHkmU4F95DxTs9kSxVbVHlUjXrkHWvb4Dznl8WXm6oQblki3iyHWcIwlpAVmjqCZPSH1jg3rS2dqbVU_NO8FEcCI6uiLwDZzGTYYGk9uNl_oZC6Vr8VWov-5T35HSL4gRx87GPUMyOSfewg3D8lPDlc09ydwR8YuFSQAZkwwgS3WdM-GVMgg59hpTnFRYDHtMPUG7xEXD3TpNUNwiCZbBvY2t4f-sRBS_zElttpTBoF2w5nnNQcjW2mc10va5FqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک زرد: ایران از ما خواست که مذاکرات را ادامه دهیم
رئیس جمهور آمریکا:
🔹
ایران از ما خواست که مذاکرات را ادامه دهیم
🔹
ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/669513" target="_blank">📅 18:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669512">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XneAR80neI4uIDV3lVaPRbDif1N1Y0h5eyB2FL1D85j-Djq8YmcfIer668gVFMvfKENSgni5SbOvqKeJV2FR3g8CgX2ctj7UAk1cs845KIRFeGn-4yClWCgRqGO9oQ2htvvv2kQvkQMrouWoJqqDQadfCs7rOLEChA2w77CnKxClo_-u9ll7bnOAz1ljkSTvRAOHKH_FOnnx_5JyEVLE1EKLIyC5HvG9HxWE8BjU9dOhfPDErIE8CwsN_9f63bMMWvUYEkg9NMtSZjc2rO6wsn-gJJeqYtn_-zdQbnM_rHmqcfNTEW5otOAj3SskKCD8_1apwCjzMH0vO-oXsRMb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/669512" target="_blank">📅 18:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669511">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk6Uacvb0hOczqI-YVN3HmhzOg4wbxO8ORijMw5Oq8YN5frUC1HnCyQB7Fi4eKH8VXbbausiHpMbLNR9_FE8Z3JoXNk5sdNzaYBWzD252rlB4MQXkMksv9sdkr4j9vcbkawiRW36dDxLfJIhcB70FpaFKDH6CXPKPc45mCC8dAR5go7-TyaIUILvS_RfmM_c1_RdoUD21mSYeTG4eV6V2JMleT5ykMOrFVFWBDOMLW4QGxfz71UkodpWesWcwLvl3C9k2K_jXTEWRhsrk9aVYV1_00rkNCMg5x0nJYqt2z8jSX4u9mxfuQQ9ANLyFwD3yPQARH1y6CUHBKRy8-FM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارلینگ هالند روزانه ۶ وعده غذا و حدود ۶۰۰۰ کالری مصرف می‌کند؛ معادل تقریباً ۲۴ چیزبرگر
🔹
رژیم غذایی او شامل مرغ، پاستا، استیک، ماهی، سبزیجات و عسل است و تا حد امکان از خوراکی‌های شکردار دوری می‌کند.
🔹
جاشوا کینگ، هم‌تیمی سابق هالند: «او مثل یک خرس غذا می‌خورد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/669511" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669510">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664a513f54.mp4?token=Dc1_rAuKnayK4cLGQN71g8C9tebhMjomEv7TM2JFOT_UYMjnPuRe1KPn7XTR5ScziKlJUlh9-VClV9SxkZZNobgLERGZyFytN_8iySGIPi-JfUdal9LtStgQXLBa4G4c12ql4fVZ0f1PNc-YeFM3rRcVg83UR9YtTDzU0yp4tOwlQKW9GI2V_5qtz-FZ_kXikxRCYBTNsuA9LJ8Yk0Z40V4DUsYM4lJhoU2U7fpBZvCYFK9-IJG0pjjXSJM_WwMrRZQ9CCI_KTzRdOLusYKT0VjxckglF_3ucdb9fhxq5Eh2NvHYwWr9JmMmR1XymRYay797o7klxASufyow3DxO3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664a513f54.mp4?token=Dc1_rAuKnayK4cLGQN71g8C9tebhMjomEv7TM2JFOT_UYMjnPuRe1KPn7XTR5ScziKlJUlh9-VClV9SxkZZNobgLERGZyFytN_8iySGIPi-JfUdal9LtStgQXLBa4G4c12ql4fVZ0f1PNc-YeFM3rRcVg83UR9YtTDzU0yp4tOwlQKW9GI2V_5qtz-FZ_kXikxRCYBTNsuA9LJ8Yk0Z40V4DUsYM4lJhoU2U7fpBZvCYFK9-IJG0pjjXSJM_WwMrRZQ9CCI_KTzRdOLusYKT0VjxckglF_3ucdb9fhxq5Eh2NvHYwWr9JmMmR1XymRYay797o7klxASufyow3DxO3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تایم لپس مراسم تشییع ۸ میلیونی پیکر رهبر شهید انقلاب اسلامی در مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/669510" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669508">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
شبکه آمریکایی سی‌ان‌ان به نقل از دو منبع اسرائیلی مدعی شد: خوک نحس نمی‌خواهد اسرائیل در درگیری‌ با ایران دخالت کند، زیرا نگران است کنترل بحران از دست خارج شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/669508" target="_blank">📅 17:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669507">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی ستاد انتخابات کشور: گمانه‌زنی‌ها درباره زمان برگزاری انتخابات شوراها صحت ندارد.
🔹
گروسی: در حال نظارت بر وضعیت نیروگاه هسته‌ای بوشهر در ایران هستیم.
🔹
روس‌اتم: ۶ نفر از کارکنان ما بازگشت به نیروگاه بوشهر را آغاز کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/669507" target="_blank">📅 17:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669506">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
دلایل سفر هیئت قطری به ایران
تسنیم:
🔹
یک هیئت قطری به منظور تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای اخیر به ایران سفر کرده است.
🔹
گفته می‌شود هدف اصلی این سفر، تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای سه شنبه یا پنجشنبه باشد که در جریان آن متعاقب اتهام زنی قطر به ایران در رابطه با یک حادثه ادعایی در تنگه هرمز، ارتش تروریستی آمریکا حملات گسترده‌ای را طی روزهای چهارشنبه و پنجشنبه علیه مجموعه‌ای از اهداف نظامی و غیرنظامی ایران انجام داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/669506" target="_blank">📅 17:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669505">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
کپلر: فعالیت کشتیرانی در تنگه هرمز به شدت کاهش یافته؛ تنها ۲۲ تردد تأییدشده در روز پنجشنبه ثبت شده است
🔹
تنها یک شناور از کانال متعلق به عمان استفاده کرده و مابقی از مسیر دریایی تعیین‌شده توسط ایران تردد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/669505" target="_blank">📅 17:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669504">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmnfIcjunzSG-7z5BrStu9ny-8cOgbMbohH_OZlQGrUa42ued4olCGgotoGpAl0K7MLnqSCH045yqfLnj7mgAsnNbNifEwIwUqcTgIe4aiA0Z12anrZwZMdgGbQVSQfzFNtazRo8ZFZpM8FCoBdpwT2igoivJiHsJt2fMj8m5JclWGi-d5on7sGlMWWalGEqWs-rBTee2XMm1E6AEK1zL4PHsjpXr3JC2A2mVUs4eeUIMesff92zCpiVbZjAZtcaBqsCDWNBjX0LGDiX-0wUbx_0ptG-5H7VY5RDvvMXNRTQdPAhC1DhcRbuaJQeWeqBaU-4nl611kUJPFaXq5ArGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل مدعی ترور فرمانده یگان نخبه حماس در نوار غزه شد
🔹
ارتش اسرائیل در بیانیه‌ای مدعی شد که «یحیی سعید محمد حمدان» یکی از فرماندهان یگان نخبه حماس را در جنوب نوار غزه ترور کرده است./ایرنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/669504" target="_blank">📅 17:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669503">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1becc8f22c.mp4?token=vKaKUmAwbdCQlpS7oZY7RzwOgY3nNt1V04cdkMrnPxR86NP36moWhSP4MJcme1n-0vonWJ_A7sw_ZN9K_ENRWv18Yr_feCY0FJjyzBEW8kswXGDV_F406JzCT-IWaux52Bw2ltNOkxptt_0m3thEYLQYADFoBQ-3vlH0hqja3MLtW4Me2mbYgGznCnV1NBrUMGJffrVesAXb4uDZMq_7GkF-DFxz404W_uPMD5sfzjuWgs2vdjH-qllOc3NS8Qp0gqSG3ngoyBrVfJyhCDO31430OMtJlei9ztUFdDhmB4NuZz8grzY7uo7g88j7kIm24lvwGBwjaZpuettT9DPaSUhE8m931C86jDM5ACK7jponi75v41zBqIRLd6s0dHY-mMFWM80GOcqjDT4EBpXbf5_8r_RVFUDR84OQ3ZRMHTwbHNQS5TNPfMkgIRd6xP74I8ZBh3iI-ft885RQi9chkMyT_wgOJYalpOAJFlqTLH27VLa-bj5e_qkOfDOlrxg8LKUH2xV9mdLaU4nd6R56f48F2DSr-HTdq2ez6-moStysseStqdmzxKmray24o8GXBJTeYsgeoKp1ImjWGMcEhX93l34ZQ5v6LZjBfDYseXS1MFBrVTDipws8MT_gNlxsPBQaQdOoBRnqXKY2mLhfApO72M7yckWbAALgxqUg6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1becc8f22c.mp4?token=vKaKUmAwbdCQlpS7oZY7RzwOgY3nNt1V04cdkMrnPxR86NP36moWhSP4MJcme1n-0vonWJ_A7sw_ZN9K_ENRWv18Yr_feCY0FJjyzBEW8kswXGDV_F406JzCT-IWaux52Bw2ltNOkxptt_0m3thEYLQYADFoBQ-3vlH0hqja3MLtW4Me2mbYgGznCnV1NBrUMGJffrVesAXb4uDZMq_7GkF-DFxz404W_uPMD5sfzjuWgs2vdjH-qllOc3NS8Qp0gqSG3ngoyBrVfJyhCDO31430OMtJlei9ztUFdDhmB4NuZz8grzY7uo7g88j7kIm24lvwGBwjaZpuettT9DPaSUhE8m931C86jDM5ACK7jponi75v41zBqIRLd6s0dHY-mMFWM80GOcqjDT4EBpXbf5_8r_RVFUDR84OQ3ZRMHTwbHNQS5TNPfMkgIRd6xP74I8ZBh3iI-ft885RQi9chkMyT_wgOJYalpOAJFlqTLH27VLa-bj5e_qkOfDOlrxg8LKUH2xV9mdLaU4nd6R56f48F2DSr-HTdq2ez6-moStysseStqdmzxKmray24o8GXBJTeYsgeoKp1ImjWGMcEhX93l34ZQ5v6LZjBfDYseXS1MFBrVTDipws8MT_gNlxsPBQaQdOoBRnqXKY2mLhfApO72M7yckWbAALgxqUg6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این همه لشکر آمده
🔹
تصاویر هوایی بجامانده از تشییع ۸ میلیونی رهبر شهید مسلمانان جهان در مشهدالرضا(ع)
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/669503" target="_blank">📅 17:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669502">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تصویری دیگر از مزار رهبر شهید انقلاب در رواق دارالذکر حرم امام رضا علیه‌السلام.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/669502" target="_blank">📅 17:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669500">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c77fdae4f1.mp4?token=ImZ3gmq4TuJNupPG-lbVXLe1YodJwglR4QLpFh_HxxD7HFSJvvAuszokpZCpPJx3aGGipwzMGfG46TIu_yssmH_mHmNV7SiCPfhwHKGYZQT3TdPfwKctF6aSNnyO7-BlgJUyYYC7a_xtoOGCiNkxHN2EJyhDbJ2TtH_kjDnlGjkACN4SGkJ9i1uVe8OM-xm1oevHbGULoBp-wwWCHm3wZ8P2e5pMpy3Hw9bySIOo1qa6iulZpOVcqHZsHYmgFwsAaPo58Qj66zi9I1e-2jAFLuqXuB13Aaz9TiRIiWxncBzywh5sSHcXFxlXjmc_18CQytvp4T3AfR6gz8f6bYrY5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c77fdae4f1.mp4?token=ImZ3gmq4TuJNupPG-lbVXLe1YodJwglR4QLpFh_HxxD7HFSJvvAuszokpZCpPJx3aGGipwzMGfG46TIu_yssmH_mHmNV7SiCPfhwHKGYZQT3TdPfwKctF6aSNnyO7-BlgJUyYYC7a_xtoOGCiNkxHN2EJyhDbJ2TtH_kjDnlGjkACN4SGkJ9i1uVe8OM-xm1oevHbGULoBp-wwWCHm3wZ8P2e5pMpy3Hw9bySIOo1qa6iulZpOVcqHZsHYmgFwsAaPo58Qj66zi9I1e-2jAFLuqXuB13Aaz9TiRIiWxncBzywh5sSHcXFxlXjmc_18CQytvp4T3AfR6gz8f6bYrY5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین و بازگشت موفق راکت ماهواره بر بومی در سکوی دریایی
🔹
اسپیس ایکس دیگر تنها نیست…
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/669500" target="_blank">📅 16:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669499">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اطلاعیه مهم دفتر رهبر شهید انقلاب در مورد نماز لیله الدفن ایشان
🔹
با توجه به اینکه پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی سید علی خامنه‌ای (اعلی الله مقامه الشریف) و شهدای خانواده ایشان سحر گاه جمعه ۱۹ تیرماه دفن شده‌اند، مومنین میتوانند اعمال مستحبی مربوط به شب اول دفن از قبیل صدقه و نماز لیلةالدفن را به امید ثواب پس از اذان مغرب روزجمعه (شب شنبه) هم بجا آورند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/669499" target="_blank">📅 16:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669498">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7ffa_yk2oDZu1Qbi_3ltQLl6HZb8IZVpkMBQZUgHd3TEbeY_ar_-bQVvF-b9TSu3-FCjonW1pv4kiOPkWkVoQEXQW3O_ndpkzJDi8vgOv7dKVdP_696Wf88Cof11wmiLeAjvyYiybTnlIr5IJucqxx8a4mor5E_v_iVAwDVqM04pNCLSQAy19NaxJN6cs8su4SJiA0Vi6ItxJ1hSl_8rVNylgowh57dmT4ps_qOF-9MGLHXUd9VnFL6IoRnnUd_xci6uDAb_VCdSv_Uu3PJvOe0ChpBnLehgTnRQR13MZPeHz72FAcock861ocwMY-fcD7Vizn5CgRQFCBJsqBFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مزار مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان در رواق دارالذکر حرم امام رضا علیه‌السلام
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/669498" target="_blank">📅 16:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669497">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
بماند به یادگار از روزی که بیش از ۸ میلیون نفر از عاشقانت در مشهد خون باریدند و تا آغوش امام رضا(ع) بدرقه‌ات کردند...
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/669497" target="_blank">📅 16:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669496">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d1cc1e47.mp4?token=jEFFtlU_Ass04LlzWwbTMjfPDHBeFvhPW9Qwm1Jzc7oBbItfgBhE9PIRM6gJrzxp-6c0b5CqnKTQI5HUUlIB2twEb4YM-ken2ruejNknBzsLqrkR09aQptsW6oxXiz8ErZUYibkhIN1yaiiVStRdFIHMH7Ald6ujGvShYH0z17FlrXFHSSKLV2iumm4kdSY4ve1W6de4R-19A8SPNBJxByFaAVIwwijGu4wfcezOwE7XewyY4BIC3N1HqduK7jacgQBb-aHfmZ5XphhUN1A3otXZlQUCmJ9oQwVeQ6P_gEHSstnmsKsWJYTUWQ4pqarRqT-MF3WoBfn8IZY_mQ2nwHyyUfxNry3yRiT2tcjsOcoUlA0Xunq01ujtdfGhPnw6rI22AFOMI26RXpMp8cRFQeU0L5AsFJ4pVl-YcTdUbfe7uTSj6I4ekINY6XVtm7y8re_89HXfsC8qwn23Ri2ziyZGij5cev2tkgUlz2h23_EBtF7sekJMTy49n0Nc7pphFf_mj-t3CmqAdSZ5YmA9zIiP47ZPEgXdEyV3JHHBa7tUk6ER5-gYx30MSQx84k-Sc0hD3mV1dSPsEuQndJh3avp39PYsy_7ebas-11eZQjWG5KA8Lu18sp24Wu7tPPRsynFj6FWupU7r_BeZ2mBHUnG4FxXxQm1x1mS30deVBFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d1cc1e47.mp4?token=jEFFtlU_Ass04LlzWwbTMjfPDHBeFvhPW9Qwm1Jzc7oBbItfgBhE9PIRM6gJrzxp-6c0b5CqnKTQI5HUUlIB2twEb4YM-ken2ruejNknBzsLqrkR09aQptsW6oxXiz8ErZUYibkhIN1yaiiVStRdFIHMH7Ald6ujGvShYH0z17FlrXFHSSKLV2iumm4kdSY4ve1W6de4R-19A8SPNBJxByFaAVIwwijGu4wfcezOwE7XewyY4BIC3N1HqduK7jacgQBb-aHfmZ5XphhUN1A3otXZlQUCmJ9oQwVeQ6P_gEHSstnmsKsWJYTUWQ4pqarRqT-MF3WoBfn8IZY_mQ2nwHyyUfxNry3yRiT2tcjsOcoUlA0Xunq01ujtdfGhPnw6rI22AFOMI26RXpMp8cRFQeU0L5AsFJ4pVl-YcTdUbfe7uTSj6I4ekINY6XVtm7y8re_89HXfsC8qwn23Ri2ziyZGij5cev2tkgUlz2h23_EBtF7sekJMTy49n0Nc7pphFf_mj-t3CmqAdSZ5YmA9zIiP47ZPEgXdEyV3JHHBa7tUk6ER5-gYx30MSQx84k-Sc0hD3mV1dSPsEuQndJh3avp39PYsy_7ebas-11eZQjWG5KA8Lu18sp24Wu7tPPRsynFj6FWupU7r_BeZ2mBHUnG4FxXxQm1x1mS30deVBFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیفات خبرنگار لبنانی از تشییع باشکوه آقای شهید ایران: مردم ایران همیشه ما را غافل‌گیر می‌کنند، ایران همیشه ما را متحیر می‌کند، من شک نداشتم که ایران روزی بلند خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/669496" target="_blank">📅 16:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669495">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
آتش سوزی گسترده در نزدیکی فرودگاه اربیل
🔹
منابع خبری از وقوع یک آتش سوزی گسترده در نزدیکی فرودگاه اربیل در شمال عراق خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/669495" target="_blank">📅 16:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669494">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c64bd76ff8.mp4?token=G0LL3VKPRYu0kI5Sw3E6az4W6I3Gts8RDbdaMtuLYWGbA_zFfL8q7x9XRCRRdeuX86cwloN4xMbe1QBAosFsriNSxyYHicg5I4wrFafpkIgVhqsMbdLO1EDN0WE1fpBXy8ioRyTFP1P4-W5g3rw3L0Pv3uEHOr6Uw5yaA2lWZVu77MHVPL-sdorv48YCv_uQJI7he-76f1Z52Yw8p2bUioGj9IvaiQEKFaqO62qnCKy7H2hP0sxr_JNq9VlqH6Q3yuPBx9RNnMz4TkTGcHsLBV9LdfLTc_3ERPXOU5XV2y2mUVKge-16K9IE4duJrA71GorOW92-iBT_zSRCsc8Lhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c64bd76ff8.mp4?token=G0LL3VKPRYu0kI5Sw3E6az4W6I3Gts8RDbdaMtuLYWGbA_zFfL8q7x9XRCRRdeuX86cwloN4xMbe1QBAosFsriNSxyYHicg5I4wrFafpkIgVhqsMbdLO1EDN0WE1fpBXy8ioRyTFP1P4-W5g3rw3L0Pv3uEHOr6Uw5yaA2lWZVu77MHVPL-sdorv48YCv_uQJI7he-76f1Z52Yw8p2bUioGj9IvaiQEKFaqO62qnCKy7H2hP0sxr_JNq9VlqH6Q3yuPBx9RNnMz4TkTGcHsLBV9LdfLTc_3ERPXOU5XV2y2mUVKge-16K9IE4duJrA71GorOW92-iBT_zSRCsc8Lhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزار مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان در رواق دارالذکر حرم امام رضا علیه‌السلام
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/669494" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669493">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6a585d68.mp4?token=RZu3vTANfO6WsD-wAYZK2qfbp7a_OIOav3tuh1At2kIb4vLmPWS9Sfcq0_uUEE4OzIadK9S9hwQdiYh_iaLJPN6KsJBUqg7bIQBqQLckjnuDiyPxjU_dT80q7RE5KzUW7LO8zgrb_Oe_lBJb3mpyMnUPWwckkbWUOXqX_k90-OR6V9FFvgSCp6j-tEvfHEe2GailNhlsSWM3nn1z4eILXfFaUDKzFJkGvNQ2Y0Uk1hiA1v8J3dMu5qHoijvorLghjN9vtaY0iy9WTEzqftRuGHTXnYecEzN_-Tpu1nelAyv9uxDIoyL-NUzbRJkOsIYhxXF9frW6XYRpXqDnQZVlR2C3AKzaDIKUQTAVpHldgEfLW0WdBkZ0-ga2PqErC8lI9QY1A_BqQZTUJSYstiTe3KuhfJdI6dLqsQx2UpOfKv2iZ4zJysRsPCbc_VzYYLstoc9jgW4Iyv65JQgC6AIrwXhvkJRAnBWRwR14WuVnxnemDJ3Rm0tUY5l6eJUUGBQgiAFKxbMWVFQeX4ysUqIn-TQ7ZOcjyUw_CVr3XrpAr9bZXEDhec3m4QqmqV63eQd5IqOOTSqHC2_1LVxyzd-yG-WwaxmlbDprJwBwthKndK0T7GkVTH-xgEAy09h0UCcsvWIyBxw382MFhhAJzbWdtL9ylGwCg7RJSFm9wEaMxTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6a585d68.mp4?token=RZu3vTANfO6WsD-wAYZK2qfbp7a_OIOav3tuh1At2kIb4vLmPWS9Sfcq0_uUEE4OzIadK9S9hwQdiYh_iaLJPN6KsJBUqg7bIQBqQLckjnuDiyPxjU_dT80q7RE5KzUW7LO8zgrb_Oe_lBJb3mpyMnUPWwckkbWUOXqX_k90-OR6V9FFvgSCp6j-tEvfHEe2GailNhlsSWM3nn1z4eILXfFaUDKzFJkGvNQ2Y0Uk1hiA1v8J3dMu5qHoijvorLghjN9vtaY0iy9WTEzqftRuGHTXnYecEzN_-Tpu1nelAyv9uxDIoyL-NUzbRJkOsIYhxXF9frW6XYRpXqDnQZVlR2C3AKzaDIKUQTAVpHldgEfLW0WdBkZ0-ga2PqErC8lI9QY1A_BqQZTUJSYstiTe3KuhfJdI6dLqsQx2UpOfKv2iZ4zJysRsPCbc_VzYYLstoc9jgW4Iyv65JQgC6AIrwXhvkJRAnBWRwR14WuVnxnemDJ3Rm0tUY5l6eJUUGBQgiAFKxbMWVFQeX4ysUqIn-TQ7ZOcjyUw_CVr3XrpAr9bZXEDhec3m4QqmqV63eQd5IqOOTSqHC2_1LVxyzd-yG-WwaxmlbDprJwBwthKndK0T7GkVTH-xgEAy09h0UCcsvWIyBxw382MFhhAJzbWdtL9ylGwCg7RJSFm9wEaMxTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی تصویری از ایرانِ دهه ۳۰
🔹
آرشیو ملی آلمان ویدئویی کمیاب از فضای ایران در سال ۱۳۳۶ منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/669493" target="_blank">📅 16:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669492">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e12067cd2.mp4?token=nNU04XTSxXlkleeJhmx_CipPVrua9z8sZ5mVEbDJLhCU9MzV3lNQEIgSDB5odfBOi9WYMyj8w26mBEPEBNKvTz7lFuSt_uP_r80yzejaADQTALMqNujp7Xs445FaZp4Lt5McSBQRaVmBmyqTsV0-8tqL17rcbY8V-7pc8HRgMs9cWQ_em3_gw5BjAgYWeevoWULyxRdvoQHb14GoOYOtQCZNkaVSzQyXIm2KnE5yUT-OTSxAVYTAQ5bRlA6hMiHThsXmQz_MbVuwSoWqdDoOrtXAom53uyYGM9_VDbCMhIbOW3Jgb3adoq3sxHXSW2l0Z0LUFLFI-TjG__2qVrSrbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e12067cd2.mp4?token=nNU04XTSxXlkleeJhmx_CipPVrua9z8sZ5mVEbDJLhCU9MzV3lNQEIgSDB5odfBOi9WYMyj8w26mBEPEBNKvTz7lFuSt_uP_r80yzejaADQTALMqNujp7Xs445FaZp4Lt5McSBQRaVmBmyqTsV0-8tqL17rcbY8V-7pc8HRgMs9cWQ_em3_gw5BjAgYWeevoWULyxRdvoQHb14GoOYOtQCZNkaVSzQyXIm2KnE5yUT-OTSxAVYTAQ5bRlA6hMiHThsXmQz_MbVuwSoWqdDoOrtXAom53uyYGM9_VDbCMhIbOW3Jgb3adoq3sxHXSW2l0Z0LUFLFI-TjG__2qVrSrbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ پربازدید از دکتر فریدون مجلسی: آمریکا از اسرائیل جدا نیست، جنگِ برای نابودی اسرائیل مساویست با جنگ برای نابوی امریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/669492" target="_blank">📅 16:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb0fWUdHOa53onL1DToBo7tnylaLVLMSl26XtT7Q9Nk8tqYw5sc4Nc2FwJ9-GatrmBcfOf_7MIk3spATLBE-ExWIysiHx4sB1NhWFTRtVqW1N7itW83OHjhDHtJaB_QcNrXUBSIEw9FbqNLE3qLPWr5o4Gg7p_o9kJAr9oAM2YGFXwgDKMCYp4bmOR07ekA0ior2MG5emZMKtHx0zCE_f2FoJlVl8ygqDAwdaqHuxJqoYe1l76nhui2EejyRKal2VtG22nE2obR_QTD0LAzDSlPzDWBA0XxpKjiGz_jVMuqEYHyetYK35QuZbbjcDyarVK93JLh9uiM0zsvNMbCGNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669490" target="_blank">📅 16:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/289303c195.mp4?token=tcpigQsGiF8UsQPTwDpRKNJ4xmvTl55wd2oz_RnaUHoKWogQPaZC4GX9ApTYGGfKTsLeFpyKTE0e2cy3fB4c7m3g56EdpWdOgYrEcuvtNR-d6nj3Ef6SNYOXh9GorrcjtpMgtX8n-fUCY1DAXCWP1oiuvsKILeD5T4rj87G5bR8gKSkGxCZBGn6gYKBBz8Pff4exUr4DkT6L-FNRT2rSgz1QdyfDydrfowl73XZpfK_7wrTcGIqMoqrB-SgkJJk-NuFHR5TC_3kIxyBRIJp31qMc_hUsP9IX93zTt9x_KOVKIZJk_E7VYnqIEKEhV8Obky6uxJ0fmdJgxalij5puwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/289303c195.mp4?token=tcpigQsGiF8UsQPTwDpRKNJ4xmvTl55wd2oz_RnaUHoKWogQPaZC4GX9ApTYGGfKTsLeFpyKTE0e2cy3fB4c7m3g56EdpWdOgYrEcuvtNR-d6nj3Ef6SNYOXh9GorrcjtpMgtX8n-fUCY1DAXCWP1oiuvsKILeD5T4rj87G5bR8gKSkGxCZBGn6gYKBBz8Pff4exUr4DkT6L-FNRT2rSgz1QdyfDydrfowl73XZpfK_7wrTcGIqMoqrB-SgkJJk-NuFHR5TC_3kIxyBRIJp31qMc_hUsP9IX93zTt9x_KOVKIZJk_E7VYnqIEKEhV8Obky6uxJ0fmdJgxalij5puwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این حوادث غمبار آخرالزمانی باعث شد که
فرج توسط حضرت زهرا (س) امضا شده
و ما فقط منتظر دستور حضور آقا صاحب الزمان (عج) توسط الله تعالی هستیم</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/669488" target="_blank">📅 15:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/669487" target="_blank">📅 15:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669485">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
تغییر هواپیمای ترامپ از ترس تهدیدات ایران
روزنامه نیویورک‌تایمز:
🔹
سرویس اطلاعاتی آمریکا به ترامپ توصیه کرده در بازگشت از ترکیه، به دلیل ملاحظات امنیتی و احتمال تهدیدات ایران، از هواپیمای جدید (اهدایی قطر) استفاده نکند.
🔹
طبق این گزارش، هواپیمای جدید فاقد سامانه‌های دفاعی و ارتباطات امنِ تاییدشده است و ترامپ باید با «ایرفورس وان» قدیمی سفر کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/669485" target="_blank">📅 15:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669484">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5207abdcf.mp4?token=aLrffZhamksttiSZzsZCVqujJJvrmpXaU9a_P0nVI6EFHK0NGJkXVDLib8agPAUsHziEq1DI8K6I_fQXvwc2EAj_u4KfGPsTkqd7stDaxqkhaMmqukWf9lu8oj00Yjhf8s-RGOHtYtKLF-wnGnb7Fk-iRKHJLB4ihjt_TfMOPPlD7ylBAEDCKVLAiIgPjylCOsUSXx_oaMyWdSFIzh-eE1AwV-uM267H7xTIsgxA4iTNP7tgg3y3OYCgKqz38Ebxssy7NEITclhXXEkF7ATmW6Bu_j04UjVAuApwey4ssn6RS6OghYYkuMqvH84sLAtesXLk5mQ__9GnCVo3y6kDpkZS9qxdkDdb-K6hEesDhFilXXKkobClw_Y-vBr2iXa5_hS_ISEiYFicb8iqmL-9vRqWE9No6ohnzyw-QVUb3ntCrs-eT7WYjLoMQE3fO8wAPc1WDOqm-rfxCK9dDXsB2PFehpNsGYsAlEOomPGuZq_D_XCuaoQBvCrPpyqq-RUGi4R1-M1Tw6hbyziAbNwRCZmEroeLUJR218Jw4Sk38G0cDvPt9Eietm4k3RlRuOfftNf_O4mvYWP0SYe4uPcz85BjBcKKliEOh-M_MquJsCvxePbMXJ2QKT4SkOOfUWe3RBg_eWgsWBe8dTljCZFMnGCsVH69zQ3mtBZhqESHA-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5207abdcf.mp4?token=aLrffZhamksttiSZzsZCVqujJJvrmpXaU9a_P0nVI6EFHK0NGJkXVDLib8agPAUsHziEq1DI8K6I_fQXvwc2EAj_u4KfGPsTkqd7stDaxqkhaMmqukWf9lu8oj00Yjhf8s-RGOHtYtKLF-wnGnb7Fk-iRKHJLB4ihjt_TfMOPPlD7ylBAEDCKVLAiIgPjylCOsUSXx_oaMyWdSFIzh-eE1AwV-uM267H7xTIsgxA4iTNP7tgg3y3OYCgKqz38Ebxssy7NEITclhXXEkF7ATmW6Bu_j04UjVAuApwey4ssn6RS6OghYYkuMqvH84sLAtesXLk5mQ__9GnCVo3y6kDpkZS9qxdkDdb-K6hEesDhFilXXKkobClw_Y-vBr2iXa5_hS_ISEiYFicb8iqmL-9vRqWE9No6ohnzyw-QVUb3ntCrs-eT7WYjLoMQE3fO8wAPc1WDOqm-rfxCK9dDXsB2PFehpNsGYsAlEOomPGuZq_D_XCuaoQBvCrPpyqq-RUGi4R1-M1Tw6hbyziAbNwRCZmEroeLUJR218Jw4Sk38G0cDvPt9Eietm4k3RlRuOfftNf_O4mvYWP0SYe4uPcz85BjBcKKliEOh-M_MquJsCvxePbMXJ2QKT4SkOOfUWe3RBg_eWgsWBe8dTljCZFMnGCsVH69zQ3mtBZhqESHA-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از حواشی جالب تشییع پیکر رهبر شهید انقلاب در مشهد
🔹
طبق برآورد‌ها جمعیت حاضر در تشییع‌ امام شهید انقلاب در مشهد به بیش از ۸ میلیون نفر رسیده است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/669484" target="_blank">📅 15:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5a0f0c0d.mp4?token=hOhfQ5maCn9ESU6LZgzls2JQyiMcJJswkIQC-9a-w1CAlLRIhGuwb1naUGI4DEZScUS4AXX597kBLzERbSsQK4oXnzsEFIooLoCcx9ChGRwxbb4gsfF2Qf0OAV_uIpjGMRWzCoc21L15OHZQxglyuE-RWtVQN7ALyR7tV-hkSfXFa4YjeOgQLGLLfMCz6I3u6P0UjEq-zvQNcHsDIWxXxoEdtGCfpwJZwGopEgz_Kuahbuv4nGzo6Ht2qjGmQoasyD0EYHuEcUIyHh4FwucAHN2zg5hApLWAIdlXNakOKLa4miVzBHsMnPVKHtK-otPYerKPs1Q5IHmM30nLNR0wJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5a0f0c0d.mp4?token=hOhfQ5maCn9ESU6LZgzls2JQyiMcJJswkIQC-9a-w1CAlLRIhGuwb1naUGI4DEZScUS4AXX597kBLzERbSsQK4oXnzsEFIooLoCcx9ChGRwxbb4gsfF2Qf0OAV_uIpjGMRWzCoc21L15OHZQxglyuE-RWtVQN7ALyR7tV-hkSfXFa4YjeOgQLGLLfMCz6I3u6P0UjEq-zvQNcHsDIWxXxoEdtGCfpwJZwGopEgz_Kuahbuv4nGzo6Ht2qjGmQoasyD0EYHuEcUIyHh4FwucAHN2zg5hApLWAIdlXNakOKLa4miVzBHsMnPVKHtK-otPYerKPs1Q5IHmM30nLNR0wJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری مردم پشت در رواق دارالذکر، محل تدفین رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/669483" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669480">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tibp7psaxJkDZpJUNKLoOAV-F1DpI7bLPP5uL7ugibiIE-KvJZ_IoIrKgFSNQ_s3M5rdtirE89d_otAJ5J3SXVk34IyirVN7yOjMzCk4Cx_4pOqCmdwroGgljWJE60RtzRZCJEO6tUWJ6p1xeZpBchGtiKcLPD9ElwawniB-uH_bte8xAckoo3TrQ4NxCQJJZrRljCMbLeL0CeUzvWcfUeIFLkLaiEAtIrLfYTqaHh_X6-T0S1sIXeAKylZsDTB92cmuQDeYEG-Ls-udnNOYl2Lju-OpWs21fjnzjFkRHbQuU1ltR5s4RjC9URBqBBtknH1FTJMktPUZLxifudW7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRUbInVWvR0CYF0ETRFCiIQAwC_AVHDOMpo2FDu33T3wHrB3ew5bN-cw-MaMERVb0Y53b233LveFHPboiojvWGk1AG1XuQhfwTii7jDvvahIBXlJP5eV-v2RaRGEws56fAIk36nM7xcP6nZ6IOdglyIOFmcMCn66kI0UQMtmNZfOVV_hbBoq-HK0qMv9CPZtFSmIliDUqNq-yUVR_nAhZEfJ5cJO8dgE2KcW84vsyffdzRaLtACa9Vb405gpd1xQIgkwoh1m2iHdD_EsYW6aEeab59MkYdOXoa_31mIGc3dg4bQ5CPOWOYfVUG0nWkyINaC1OCxJjnzdSKsK4cPLRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرچم‌های فلسطین در دست بازیکنان و اعضای کادر فنی مصر بعد از بازگشت از جام جهانی در خیابان‌های این کشور
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/669480" target="_blank">📅 15:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669479">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe53a547a.mp4?token=V97bF3oCvgbfLH4OSrp82LWaon1FeKYNSaa87MwwnQGAJzorH3EFmXjq8N0Lpix1t6DmuHwP346Q-s7eWDGd9Ow4V48ryqa4tJBipi82gM8xdZa4CPSaRVudMHIQstjhsucwHU77bIqXFgZf4_cpHgc2yLzkE7ZjucacPxpclLdWCqZYMoinhSAtJuEngrdDzUsO2oNSQ6ZE7LxXjZCxWtrsZeJBMrbv3ssdAIjSY2_XxDNftsO-H-QHCef3BCXymKKRVxzJ_dmyskXJGJCOM34w_yIDuu2hqFeJ0t1bVGk2iZbRYdKwrIGc7ceYH8rFjy5ydwRguEYp3lW6jyIoEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe53a547a.mp4?token=V97bF3oCvgbfLH4OSrp82LWaon1FeKYNSaa87MwwnQGAJzorH3EFmXjq8N0Lpix1t6DmuHwP346Q-s7eWDGd9Ow4V48ryqa4tJBipi82gM8xdZa4CPSaRVudMHIQstjhsucwHU77bIqXFgZf4_cpHgc2yLzkE7ZjucacPxpclLdWCqZYMoinhSAtJuEngrdDzUsO2oNSQ6ZE7LxXjZCxWtrsZeJBMrbv3ssdAIjSY2_XxDNftsO-H-QHCef3BCXymKKRVxzJ_dmyskXJGJCOM34w_yIDuu2hqFeJ0t1bVGk2iZbRYdKwrIGc7ceYH8rFjy5ydwRguEYp3lW6jyIoEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا ساعاتی دیگر مردم می‌توانند به محل دفن پیکر رهبر شهید انقلاب بروند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/669479" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a00699a2.mp4?token=hRPR0ehZ2GXSOgwNBsvyF7cgtaQFliPi6xYYYH3nTpnY0uUjHVANMhBdLqd5USYf7SidgsORmGsqz4AeZNmWB-pZiQdMV7fE-whJqyGbxqIFjfXYZD2AiI2ZRh7be7oxw-_KNT-n__KpL8SSFGus4VBPeNTNgSjYlLPQrSOFuSVu585rzOP0euQy3dva1Lm11CE9hGJx2__-qfF5x1OHgnI9lnj6CC5_rPUAIae1be_CgQ7vkA943bw1EORi-WhOXj_3s0cj_yu0G8ypQqWYhcp6mjkBaM8Lumz5HesgPmWXLC6ZjOAUUI-4vclP4SldkjOoBRdKmwHI9VgH82GfvQKv9tP7UfTCg9MfyqP9ySPjitYjHfZR4TbTh02qPY-COeR3FMOHtu-Q8sDXF6TvpWAM3Dx1r04lI0_RytMB_vsvwF6VeFkMzuHuffBOyk8uKK2pdSgb2vsVFjhGKQpch3mEm7e_Yd9ZnHSzsVBLjpcw94P8r76dQiPO4rPRVIyLdnzNLpblyFWFyEVe_mI-Q9BMnb8ALHirLAOodX1WArtzzCRPbjYGOmjHIU5dXTc3_VDM8bSAFK__o_QH24Wez_B4NjXKN5AUn1LIFI0dXTlf_O9UuRcj8tYJDULuWz3jbG3f708eZlXakYIy3QyXLazQwbc4meE9JSYVE3_4G1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a00699a2.mp4?token=hRPR0ehZ2GXSOgwNBsvyF7cgtaQFliPi6xYYYH3nTpnY0uUjHVANMhBdLqd5USYf7SidgsORmGsqz4AeZNmWB-pZiQdMV7fE-whJqyGbxqIFjfXYZD2AiI2ZRh7be7oxw-_KNT-n__KpL8SSFGus4VBPeNTNgSjYlLPQrSOFuSVu585rzOP0euQy3dva1Lm11CE9hGJx2__-qfF5x1OHgnI9lnj6CC5_rPUAIae1be_CgQ7vkA943bw1EORi-WhOXj_3s0cj_yu0G8ypQqWYhcp6mjkBaM8Lumz5HesgPmWXLC6ZjOAUUI-4vclP4SldkjOoBRdKmwHI9VgH82GfvQKv9tP7UfTCg9MfyqP9ySPjitYjHfZR4TbTh02qPY-COeR3FMOHtu-Q8sDXF6TvpWAM3Dx1r04lI0_RytMB_vsvwF6VeFkMzuHuffBOyk8uKK2pdSgb2vsVFjhGKQpch3mEm7e_Yd9ZnHSzsVBLjpcw94P8r76dQiPO4rPRVIyLdnzNLpblyFWFyEVe_mI-Q9BMnb8ALHirLAOodX1WArtzzCRPbjYGOmjHIU5dXTc3_VDM8bSAFK__o_QH24Wez_B4NjXKN5AUn1LIFI0dXTlf_O9UuRcj8tYJDULuWz3jbG3f708eZlXakYIy3QyXLazQwbc4meE9JSYVE3_4G1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال عراقی که نتوانست جلوی اشک‌هایش را بگیرد و به تابوت رهبر آزادگان جهان، سلام نظامی داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/669478" target="_blank">📅 15:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIx5YcuDZknmjOJgodZEj8240szG9nEjd09G2mJjKTx9l0BGZ-saVxkie0z57CrKgHrm1LaQ1M7gV2eMCPch6Yhnwt0D1Qr6f1vT_oesWLRoBTJyPrxv_5RvalGJ5j4NZDNIuc4l58jsk63VZvhmPZ4QZdAp5SPGasUbP7vCzyLoWJOnj0boPRBpGKBMDWHoefhZvH8XrkmUp85HbKQxptKHhRUOX0h5kc6cELdyVu2_9z7d7vwm4aQ3F9Zw2Z3w3J27B-Qa3ULMj3ly98eE_uhNfHa1x3UUqjh8d-gaVda4LlTXAr6D0TiyPec3rKtz1PPxi8hCuDMVZAvPajUvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انعکاس جهانی حضور ۴۳ میلیونی در تشییع رهبر شهید
🔹
الجزیره از مشارکت ۴۳ میلیون نفر در مراسم شش‌روزۀ تشییع و بزرگداشت رهبر شهید انقلاب خبر داد.
🔹
این حضور در رسانه‌ها به‌عنوان بزرگ‌ترین آیین تشییع در تاریخ جهان توصیف شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/669475" target="_blank">📅 14:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669472">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983bf3e3de.mp4?token=P_0oRftU2z89ZN1Yy4ugcK7F8fyDR899QEJTcLmTsyY6nl68VsDKu_A9KL6XxRvQ9PVq8H1lLFYOjsxYEqZsZ-BZya7J4-W_d3T1n60kqXK75IUjozZMF0wA90fALNQgBlkagpPhq-iw4Y_CCJw2MY7pYhyWDHLaHev1eci6zKiShnM4zGsi0DRT3QE7hEwGGlqgtO-kSCMkU3rUlPLrMq4GzR2DDAOz6q5MQB4z5BboJ6QoIW4udiUy2rLnE_hURCtjQstNTbmsg79CHI5GjFWl1Nw7VMsv23rL525mX09HRnIbqqk6oEUydCPwnOiziMbBgQtkVOB4vHM862rgrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983bf3e3de.mp4?token=P_0oRftU2z89ZN1Yy4ugcK7F8fyDR899QEJTcLmTsyY6nl68VsDKu_A9KL6XxRvQ9PVq8H1lLFYOjsxYEqZsZ-BZya7J4-W_d3T1n60kqXK75IUjozZMF0wA90fALNQgBlkagpPhq-iw4Y_CCJw2MY7pYhyWDHLaHev1eci6zKiShnM4zGsi0DRT3QE7hEwGGlqgtO-kSCMkU3rUlPLrMq4GzR2DDAOz6q5MQB4z5BboJ6QoIW4udiUy2rLnE_hURCtjQstNTbmsg79CHI5GjFWl1Nw7VMsv23rL525mX09HRnIbqqk6oEUydCPwnOiziMbBgQtkVOB4vHM862rgrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیگر از لحظات وداع و بدرقه با رهبر آزادی‌خواهان جهان در تشییع ۸ میلیونی مردم در مشهد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/669472" target="_blank">📅 14:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-Rs2Vf9BMAjaMC8C4npU_Uvd-ObQVn9hOWY4Lntjw9tAJxmiI-Kmln4PI5CVi5hNV1EqTqREvaujtZkQctepdXPgiLV_oSEnqLmLd8J15mXEurN3JTMjjtnrkUSHYtO1VXJkZobMkazMVhZDuSweroKs9twejTuN_EWFLaboAJ_78O7ENM_GXzq7BFFEAIaOufmO6QGXhKo0Rvq849Iv5zcK6ZPU_qZ6lxMfOWmL-nXUXJ_hYvHvYZZjo7lBksUmrtCl12dlVlGROlwTSU0XuRNcfjC8e64_NLJS8ILiQPpKWVnFIiLeQJp9p_TvVQN1df3Xiusl5JFTH3mEFSLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8ORk3vevkWrhGOusesA-0ZTO6hOmuXwjggEP6S09ChcTU0jlZlfricbyKOnE3e0aFtRK4FaLucnebvMxsVgIF9Fa_I7euWJhe39qS8wj7La9_x8SbNyVsFG7MJrHgdxwmxe-vFx3rv4iSnNDV9Mv0VrHw9ut6BrboJ1Hl_Lo9y4-NcqZ_nNJ9r3Qvm-7AywDe1oRTRAUYxb9H7srTZ37sMBnMdygC-dj1BR8k9N_PABg9f8MnByW4fLTXJr52qV_A9Fxz5xTaYvmH8CwisEMGsKVA6vhhWdVcNl2eftsheDyr-2GSrCfMraLoSoMr05VJSpNHgvE3SZ-um1WfnOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQIcwAwH1XNPeNBla7d9VrZqN5eYMqqyUZyF-A0-vHrblmy4q2fXte0uccqQUt5C6HF8FjP0eqWxVfSiQbH0V4NnvS9JoQuHRKMfsJmC9889jssCZJkaEv5Yb9h1gCRjDbpeHLo_36PWlSDgOo2Pprs__NI42bTHwVa_SCCpnqeNX1gez9XXYAPlBQIoyubBLo8qUZ2nI3zRWiIxfquo3O42Vv0NZ2HEqwBMdz6yXnnJ7ImIeXdIrLDo5Dx8cvlcMw6vGxCg8vxs3k5zxSPK0o8SliJESLW5Dc8XXmFz0Jur6-oOYZz_xYoSDn_oTE5Hvc3E5Cx54ACqHlLkK8Jmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auZzp8HdaR9ElTE77iVyBEyL3jxFXtxcbg3_1u6DiFRNDOHnCZ4VwfXTd03Fa78QnUOuXdRcVAApkArTsKDfVKiqQxTyOW-r4zuznX6I9g6JPpfyFLLwnmfQ4h_qwYyeEtoBFCuh804UkvnKSbCuKINUWcVEYmw4T36nU6deX1AtCiGs7NYBI7v5kMRlhDmArjhW1sa4tUZpShcrFxpPd-mthJvL6yVUsx-mOKPexsLijT1Y9bHknPXUCcmK2rjjeofeWzUgQWbRqbYSwTL_aFTwWJn7Oxn-jdVkIf1ON2BYMGr5JFXJvnpVgntjbLh3nOtCCwxgEwHeQP1Yxd7-WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نگاهی به جایگاه ایران در نظام سلامت جهانی
🔹
ایران با اختصاص ۲۲ درصد از بودجه دولت به سلامت، بالاتر از بسیاری از کشورهای منطقه از جمله اردن، عربستان و امارات قرار دارد.
🔹
از نظر تعداد پزشک، ایران با ۱.۸ پزشک به ازای هر هزار نفر پایین‌تر از کشورهایی مانند آلمان و روسیه قرار دارد.
🔹
پوشش بیمه سلامت در ایران طی ۷ سال گذشته بیشتر در محدوده ۸۳ تا ۸۵ درصد بوده و در سال ۱۴۰۲ به ۸۳.۵ درصد رسیده است.
@amarfact</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/669468" target="_blank">📅 14:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8a1c0ae.mp4?token=bcwuS6k9MrSowF7UIV2Iws-0ZKHOTP7m623hxKZEr-df5jP10M_YDGVZr6TEMwumKnaHeRtQjkBFzwEymtOEJat0CBJe9R9s2ImxvR2EICKt6fCdqkeLbfeZDqNyoSAk_lzgTaousbVEAQZumXQuQupLaJYFqpBtR88tnqvrZ7DgbWsJiyE_HQFsYoHcF9bP_ZS1LjoEukbnsNazXSm-Kg8Y8OCy2Udqaq_SO8CERT7gR3ZaraRD5kAx9jdFROXXycKm_81Ih9gsX-qOtTErf3-ljZ4tMRbJ_SBiEQaJcU5v-QsY66oI78CJoP194GFZpjJTznfsbtqBHMHIgcBeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8a1c0ae.mp4?token=bcwuS6k9MrSowF7UIV2Iws-0ZKHOTP7m623hxKZEr-df5jP10M_YDGVZr6TEMwumKnaHeRtQjkBFzwEymtOEJat0CBJe9R9s2ImxvR2EICKt6fCdqkeLbfeZDqNyoSAk_lzgTaousbVEAQZumXQuQupLaJYFqpBtR88tnqvrZ7DgbWsJiyE_HQFsYoHcF9bP_ZS1LjoEukbnsNazXSm-Kg8Y8OCy2Udqaq_SO8CERT7gR3ZaraRD5kAx9jdFROXXycKm_81Ih9gsX-qOtTErf3-ljZ4tMRbJ_SBiEQaJcU5v-QsY66oI78CJoP194GFZpjJTznfsbtqBHMHIgcBeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر آخرالزمانی از آتش سوزی جنگلی در اسپانیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/669467" target="_blank">📅 14:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SydzaVw1nDfKoo-ppz0CnZIJE4n0azhEwR0mU6eLNss21dPYdE3i018KfseBjI-isgjSFwhcLZCIzWcNjenng0Hj6eCBWNBAHjiVW8_XJfuctpEJAF_0JV3wtC2Ni-240K6w64FjKW9qMWPKyq5YbvKtXuwZI7ru2aUYP80l7az5I4KJJUPEAfcyzcwSCEyXRA85yz5ejLkxVcaoEctNmPj_52mR-EETxNuXaGcFKlLjQ2zliKTgsjqjKp04pFtvf8NkvalOxJUf33vEShClnUmuoY4R5zfmY3jY429kRkWQUSH8MMzaXz0SZRvS50xoubu9ByJ0eXfW2F-8B064Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری مهران غفوریان برای آقای شهید ایران: رواق دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/669462" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284857c6b2.mp4?token=RU-RoBx1vI4RAPoxgjKEtp4xYdXPjQr07HpCbl3xOD_JnawR4__lOV9--V9ma205A7jqF4FMnWCfJgfS6m4-j-6Q5ZNH_j7YpGdGyx9nhl7EQR6poKGtEzN1p7FysMsAFOAKBnYhec9SskCD7VAvofn31IG53usSZoCkM9sgyDtZVNmy8wgwxfI7kpeXqzJyJ_w04fTvHJSVabiJXADUsAuKpSoHJKQ03TiSPjbumnOitU0DWlDtF2_JiD3PMkIxpQ6v5c6wtkUr3BvHdrivbmY-_BhZZ19j7cBZmq8lhQ178nsVYICHoZWckGXxS15yexn7Jbx6xsNE1P0Uz6R9Oi-0wtw8G8veKBeEL_UoQS2pU6wQFmwNjZwjfVJ2qOWNHbxuG7De0E9dEosVJYpMWTUDJQjBMN5Od0LsoWXjPnnmF_1KO_Zgr42s5ghKYac6IxT95V52DfjPaDf8r2n3QPXL1_-qII2OvX-T1b4Npe3nRSYgDuOH_J_tZ0xqCSbqDF8wDHpqdxJsz9xkvtxg7aydXdndj3pjRMRQ8H5qvAlXCmoucjc4pu4TWpJt7axSB9F6hHeAo_bz8ab8xYafJITQ5DhJxBJm85rJdv6Ueg5C3EtvtwE4mHO0N-SMLuBr6utPFCT8IjKKQjmFCFXcn73KEsknOkA4AvwP-MRrMN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284857c6b2.mp4?token=RU-RoBx1vI4RAPoxgjKEtp4xYdXPjQr07HpCbl3xOD_JnawR4__lOV9--V9ma205A7jqF4FMnWCfJgfS6m4-j-6Q5ZNH_j7YpGdGyx9nhl7EQR6poKGtEzN1p7FysMsAFOAKBnYhec9SskCD7VAvofn31IG53usSZoCkM9sgyDtZVNmy8wgwxfI7kpeXqzJyJ_w04fTvHJSVabiJXADUsAuKpSoHJKQ03TiSPjbumnOitU0DWlDtF2_JiD3PMkIxpQ6v5c6wtkUr3BvHdrivbmY-_BhZZ19j7cBZmq8lhQ178nsVYICHoZWckGXxS15yexn7Jbx6xsNE1P0Uz6R9Oi-0wtw8G8veKBeEL_UoQS2pU6wQFmwNjZwjfVJ2qOWNHbxuG7De0E9dEosVJYpMWTUDJQjBMN5Od0LsoWXjPnnmF_1KO_Zgr42s5ghKYac6IxT95V52DfjPaDf8r2n3QPXL1_-qII2OvX-T1b4Npe3nRSYgDuOH_J_tZ0xqCSbqDF8wDHpqdxJsz9xkvtxg7aydXdndj3pjRMRQ8H5qvAlXCmoucjc4pu4TWpJt7axSB9F6hHeAo_bz8ab8xYafJITQ5DhJxBJm85rJdv6Ueg5C3EtvtwE4mHO0N-SMLuBr6utPFCT8IjKKQjmFCFXcn73KEsknOkA4AvwP-MRrMN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رسانه‌ها به تشییع ۸ میلیونی پیکر مطهر رهبر شهیدِ اُمت در مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/669461" target="_blank">📅 14:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3389298c0f.mp4?token=DFO7txZhiqukqrNvrh0-69xkogkW1aCmz7m494IpQeOuWEBleb0XOv7xu9W0yhCkfzwUFUmME05j7LCPWBFiAycMsVSK6asXQIEhwedAg8bmK5ldau4Im7_yE3dR1eQuW1Kg0s5PAuJn0gopSaRP_U6fHJBPOJh-CKJH00Uy6_QOR4jqSjGuqzPd6yFnxy-DioZ3R0RfgYfRQ7eaJfYipadLiI0XVpFwCSrrtqGI0lZoV5WzZGQ8HaBVBqFRoKzWAllsj75nsISmB2Txd6c0LkI1PkPOvx_lRSMRPkzO7ZENN8X3m5KzIe0bI0AwDXgnKJ3eEgiuAX50n3oroDUItQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3389298c0f.mp4?token=DFO7txZhiqukqrNvrh0-69xkogkW1aCmz7m494IpQeOuWEBleb0XOv7xu9W0yhCkfzwUFUmME05j7LCPWBFiAycMsVSK6asXQIEhwedAg8bmK5ldau4Im7_yE3dR1eQuW1Kg0s5PAuJn0gopSaRP_U6fHJBPOJh-CKJH00Uy6_QOR4jqSjGuqzPd6yFnxy-DioZ3R0RfgYfRQ7eaJfYipadLiI0XVpFwCSrrtqGI0lZoV5WzZGQ8HaBVBqFRoKzWAllsj75nsISmB2Txd6c0LkI1PkPOvx_lRSMRPkzO7ZENN8X3m5KzIe0bI0AwDXgnKJ3eEgiuAX50n3oroDUItQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع نمادین رهبر ازاده‌گان جهان در کارگیل ھند #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/669459" target="_blank">📅 14:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آخرین وضعیت از روند آماده‌سازی مزار مطهر امام شهید انقلاب در رواق دارالذکر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/669458" target="_blank">📅 14:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پیریت؛ هنرِ هندسی طبیعت در اسپانیا
🔹
بلورهای پیریت در معدن «ناواخون» اسپانیا به شکل مکعب‌های تقریباً کامل و طبیعی استخراج می‌شوند؛ از دیدگاه شیمی، این پدیده به دلیل ساختار بلوری مکعبی ترکیب آهن و گوگرد (FeS₂) رخ می‌دهد که یکی از شگفتی‌های زمین‌شناسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/669457" target="_blank">📅 14:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80716f39e.mp4?token=F3cG57m0yLA0r2SkXjqWyvRWVc8b7l97EG-KIXTLftAecXowB3pyJMuzQiteG-0oImvbFG8ETItI3QSa0yuGao4wAVODLsN4oNJ0R5mwnWaIAEtn-X2YBMQNGvygQEdm4l28zb2VfINipCXq9yCFVzeUBTfj-0jTvgyYOYCTd6xwnHVRzGNUD09bhd8lPmU3rKWOASXFQmnMMlAY1r82byb1vEOf5gHSGP5wJmb23DUipdfqfbJv2ye4mlZssaACdbvukKcI0bZQEd-zoS5nWWcdAupMo2EhxOltWOt92UAC5y-hnf5olU4GNpWsonwA-TmZrfjavtRmKCdX97VqIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80716f39e.mp4?token=F3cG57m0yLA0r2SkXjqWyvRWVc8b7l97EG-KIXTLftAecXowB3pyJMuzQiteG-0oImvbFG8ETItI3QSa0yuGao4wAVODLsN4oNJ0R5mwnWaIAEtn-X2YBMQNGvygQEdm4l28zb2VfINipCXq9yCFVzeUBTfj-0jTvgyYOYCTd6xwnHVRzGNUD09bhd8lPmU3rKWOASXFQmnMMlAY1r82byb1vEOf5gHSGP5wJmb23DUipdfqfbJv2ye4mlZssaACdbvukKcI0bZQEd-zoS5nWWcdAupMo2EhxOltWOt92UAC5y-hnf5olU4GNpWsonwA-TmZrfjavtRmKCdX97VqIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه‌آسای مسافر در پرواز رایان‌ایر
راشا‌تودی:
🔹
در پرواز یونان به آلمان شرکت «رایان‌ایر»، با جدا شدن پنل پنجره، یک مسافر تا نیمه به بیرون کشیده شد؛ همسر او با گرفتن پاهای وی، مانع سقوط و مرگ او شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/669456" target="_blank">📅 14:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669455">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
هشدار از سطح بالای تهدیدات امنیتی در تنگه هرمز
هیات عملیات دریایی بریتانیا:
🔹
سطح تهدیدات امنیتی در تنگه هرمز همچنان در بالاترین حد خطر قرار دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/669455" target="_blank">📅 14:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
آخرین وضعیت از روند آماده‌سازی مزار مطهر امام شهید انقلاب در رواق دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/669454" target="_blank">📅 14:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yxi3eY2hO_3VT3GjBmlkY2-2maRtu0Z3AD5ozF_xNptCAiurfusLgrnlCpAiGaMOFlH8tIZeFYqQC8mqjeVj18xc6Ac27Ehg2r8y463gF8q4jiTbhSI71dXpBbZxtjkfyTxEu8ZbZHgnAS34mV0znIAqW3B32-YwN_URIysfhAPTjbvQN7436CiMc2UG8m_sfuMjuWigjaPZ-fNYmkbGU21N4T08Go5LYjuSWOZj0dsOdhAylqraIxOxaIFk-Zr7cwOojxXKBeFxBpEx98M6AwU--DdSFL6gghqGebMBS0zgaCSY4FO7EBBESJ5E2xgtDmZ0IllSeT_GmjWLol8alw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nS39f-JvdTP-GuWKEgl4yESyIpRt9ze3iovt03jmbsvYqH16LxYrUgE8bFKkwoc1-hJoQ-yjCGAnaQkEOIScDkGO-Fnl2rOup05TfdUCp_GlQZQpjCpWgq9Kd0o_OK0Z-NnYn6JauaAgBRYVedCWAlmfxdRWERtEMNBgRWpcGmJlVkQSUCU5gX5II33hWh1aADJonM-bZrFL7msKvCJqikX0eUFmh_O-muJ4MSxCnVCZstK4HhYwKaZhFp-A9bqYNpxHMHSFIFUhpNwtsTJMAZQA942VDPSBDiXiSS3FwVoNh6GVxh1ID--9c2GRLTR9fFDzv-3mgBU_KyrlgHsnLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4tRbFBF4tBH2DlusVbrW8opFF3AbZmhQu0cm67DCREmTfbhSy8TX5enaLz5gfgYXKvLKg_Zg4N-e6juuzPsWvPjFlCLTmeTCWKYtxqmtvUsVxt-9u_2uZQ2R6rgofd6Y7KbcJ3w5G-j54K0fMHCm5JssDTkF2TAKyODeVvIs1tQY3BRV8iewQbnh9XZZ9u3ATxqjxXQN0RaRvBFEOlXe_3tbl3Pxfy1cXrrZFtQZRRCGBs3FG2111D2eC7Fq5KUc_amMTE3O-1WUTJvYoVE9G2cfxCnipws2hpAQt2I6DAC9FE-2nfl9pWBZ9bliKFw5ZB67dOBOIcDHi2vm_MTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgrWhnVMWMYJlOKMpylBFkt2JW-68Jhy6CFzFjoKeedyjnF8MFyfGf50At9pK5O4vIONkCcuU7CgJ_Nqa3zY0MhC4eeYtBdmMYdxIWEyzEhJgnG8jQwb3hNUEDxPe58EQhMNsNmjg1B6zbRrpbPc3C3h0-YnS6bSbb9bWOoLRzEwtMTAMx8Rok2Beq2lu19iaVWU7Y7ewkfQJsYWnFDvFbkB0-QQ0UoxXLRRfG11zNmGURYnLBJ11PkSmJJEtMgk6gmG3wSfW2gC2USGyKTc3SDg4Cki5g9E-RN_Yt--NadB88Rrh3v-LToHr47l-4yk61Wc8xnSxGOk3U4dgcn3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhGzv4yF1AURiQo69bARIEHfyJIB65TZ1EuIM5tOpn1mtY0ymHbX1__8FciDAsijnsgOBP07a4Bh4SnPwE4M4s0QeuvVP1wQfJFOYCgNnP9m0jM8YAo67R6FHOsU-af7I17S0JxAFQi2hqt1j4T4uJcXX931WYrDpl0nnzVeAGVJ7SBD8gwEZhRfXItIgGea7oAn0yfdT2gWjYNj0Mo8LCpxiP-3DKckvyECRnA41CQFWKc4jHIokZI2QQC_Aicbvzi48mqhMWl8fIJSrX4xeQi8kyEkTYesgt2v9VVLXgCybCPygT89LKW15uKEJJlUj2aJZf78DWB_Leg6by6VtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIpYSfwiByvNEhVClQq5bpEfOdR8uBhh9dsbRTy75h8epm5vXd0FulXSjghMZaZZrdvTU1s1BQByDeTB_xo906Bib8UrZW3EcvKa_moOOVDBxrubP7q5XCBFrpM5HorhJFa1pq_dU1aSEXRK8lu4YIUohicd3Gll0XbvvpJ7bB8iJ2nDUoTQ_DGuaKigEigPu7x7jGLC0bkHjQS7qa9fiF6hzDBMFypp-LlBWY1jM1sQsxVX67oWGf-B5InyHzdQICn-GlWZO3OiZKDOf-eLS3y31fko_DeySGXvfXe3sRqhSuh592hjDddWE0tPwWRaGO-CNq5YPAntgkoE0k19xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_NoS1rSLgLCB5eDRgYq_-gBnv3U1ZlzDVRH5iieXhs4r3ogTckqPKhxBOkeFXe8SO5N8N0VzrVKsI3sBRVunmVGPJUVjdaj9P02BX0ie6J4uV3MymGEH2dIyIx2Di3E44MtcQq4DaO6AUDDlAW7a7Qmqi7dfSeFNwNTjFPsyZ0VwKZ7-pDu2p66GRuI5fT2UfV4Y7oPlqCt9gcrg9nSQtCVyjpD3BVj_ROQHSH7M0MLxwJHXOwNF7SW4zb8FkaZZ3dCzAPZdsrmiB_nKGbVfs_J4fZgZIUTqgbVHpsNLFxymuBreijrga7u7np_d-2VfrWw9Gju2Dc-56DEAGufZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JW7zqPmCgW8L8acXp2jzI1_E-GbwbyFVkRDHlgWU1Cx1yNrfqBxt3vCXzPpdPNwr_pwEE-0N0r3apkD8vLCJVA5-GSn6Bfpq3md7aHiDDzYDgYKPhaD8-HNcHG_E4dC_qFhDNVo9y4c2y6FfuFyZ4OOd4qdeTMiwIPhmYqGfrYHJD_x8qJ_DYvd4iSBkpH52a4Gsj7tlLwmBMTIRN9Y5WGlrRDVAKVyy-O63v628f-HSSivTHcogw7eTOGESkR_7YbTaQ4r8ZFdBed_ak7JH-d_hafWxeJempceBi1czZ-dDv0A5rfmWJGaiTEcK8qQCSCwJ5uC6MgL7Xn3HxQeCOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
روایت تصویری مخاطبان خبرفوری از لحظات وداع و بدرقه با رهبر شهید
▪️
اگر شما هم تصاویر یا ویدیوهایی از این لحظات ثبت کرده‌اید، آن‌ها را با شناسه زیر برای ما ارسال کنید.
👇
#بدرقه_یار
@badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/669446" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c410869c1.mp4?token=EenC0iL0nlJnGKrsgvmZlYvCVTuRBWvKldWEzXdZVILj-RIaAFEBjC5h7GERUbgreRpwsmX6EZ5GeVFWGka_Gg11EdT6fDkeeXC_uUnn6LnVdpIfgVNRLxjVAsoOUbHmfRRTma6vIFKvTnf7yU5mmCe6WR2EeEURMdZG9Vmw_XOhLdOtox0sUAzkHd4ja16q2dDbUkArmxKW1tFaw0cnVngGuBhAmRXBkUqrCunXiSkFxfdKUa3EjtMo0eO4kfswktnQfpB0oHIt2FHuKXF0LpH1U6nHGSbJ-M-PbLNMcEhWV4_5qrxtIb8D4S8LiDNkY9NCCtr8pqiVbk6cRDs3hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c410869c1.mp4?token=EenC0iL0nlJnGKrsgvmZlYvCVTuRBWvKldWEzXdZVILj-RIaAFEBjC5h7GERUbgreRpwsmX6EZ5GeVFWGka_Gg11EdT6fDkeeXC_uUnn6LnVdpIfgVNRLxjVAsoOUbHmfRRTma6vIFKvTnf7yU5mmCe6WR2EeEURMdZG9Vmw_XOhLdOtox0sUAzkHd4ja16q2dDbUkArmxKW1tFaw0cnVngGuBhAmRXBkUqrCunXiSkFxfdKUa3EjtMo0eO4kfswktnQfpB0oHIt2FHuKXF0LpH1U6nHGSbJ-M-PbLNMcEhWV4_5qrxtIb8D4S8LiDNkY9NCCtr8pqiVbk6cRDs3hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: انتقام از دشمنان، حق ملت و وظیفه مسئولان است
🔹
ما در مقطعی حساس هستیم که آنچه فرجام این رویارویی را رقم می‌زند، میزان تاب‌آوری جبهه حق در این جنگ است.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/669445" target="_blank">📅 13:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKL3N5y0glfbB3pYPDDI9mJfvAMfhrcvetyAeGJrCWVl0iWB2YbZRiJYlH4WFB1ZUaUCyzYIqKQJ14wWtRH1rHhrweFW9t3PtkzMh2G4Gx2qr07kr_V5nwyxQ_8dfwtEJnSju-UkCOt67mH9fNXIifVSLh7fLfSChf0BC8AQdSu_cUp3rsOJsing5XsjUYtqrP1L6JYCfc4KEf1ktri31eEdtEqIj1Y07uYM1sh53v7pjmBM_alUqD3IejfKFL1Mqh7m11RQnjiJfXRXICJhDlJkunUNJ-sl55d1CCT60fdlfLPSURZo_dkz-odnrFA1WZow9iIpvyx34VxCkGzbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpUOQWvucjToy0gG-qVax3rOixm2Djii34pCSyUV1CNj--nertPb_HTEdAOQqwm505s6KJQT7pkX8IMUty7fTDL9SWjICrgy34bIsvajk09FoA05cyWhlSGJ5TBU2ABkKd6BJScA80gFQi9dF0ks0wCnOYqiEsL4xqRyrf4CH0nFqJ3mtIUIvNC7mAX7lqoiADKNbVhuoz0uQ9SSJBdw-voNPUpeXsD2IZBDcVeyWAodqYW35EDk4uTRc3_OVc6r5Rw6XQb1Glq5r9JNXMMLOurf6s0CwImV3PwP4tOXukpBH2LYf9KGYSd8O2mObbiOZjC2XXqbhk0cdazT4Ufqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRmVzCBPR1kB8UOqK22VfPcbsEtjzs3CiAUwwHRphb4ERUYIQoOwmWbtxxlHBOmyt7Q3Ku7CHJv5uuhGyyz_x34eKGxVTuHtM8mApvzCx-6xemzeDDe25l1wmGtb3Gv_oZPhng0pOaMU4_mNXqKMY-HZFxjclMXAvc7RGCf1baRCrflRGM9FBTSbS0COufoOnUx6JgyEOPVl9aGJALx8tCu7Thhsh_pLchFOkqVWLx_b8QN7OWj7GVxWW5DbyqWX2431t50uWRabtVhag7lK63aD3S87YM2fZ6lc3Q-hUwd2XSsvf14cgLSKlojitJrh-O-nb44eHEGhMSW10X6_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbkk-oJNdYqfR9I9B5QE-AQ6Mn-wV1WTx-V9MKf2LTDMndjkMQy2d6uuFVVctYREcdSYfUWZ65eHWP9yND86M5MLZvQbtFa2JiIDFkavOTVrVOtBtD1M1noKdKNjRcGsw0GY7jqii1eRJhQKgGtPJKGaTrPSzBxprZr_jNMyXKkl8_mxxX3lQ-Lo6o4zArkCi3hjkY_RZx5AWUPBJgdpcQKu38i46tvFpThsvy6MXuz2BqRDQ-JjGMb-tGFS18tnL-ndGA9wJRZhavoIFOxAWKceauGNNDt4KWx6P6kjlmjcHVhgEf5Y2DirUXJDjSigzw_Dw0vlu5XmKK9tFc5Myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGJIoxudl48t8DUtn6u9AEC3blDoF0631cUBRe6snPXoEzRFLUkVXk8s0T6LfkVqQBvIqZoMMNJ-HQQtC00mdkw0aM_UKORm6p1v8QEA4hn8s0Cl0dTczsOldCnkaWafaShzX7yCIwIpz2K3GNlTxq48WVR8amPhiQNGo29ZVgNrQj0M5V_hYESCqYRrTctI7hsjpkBW24BijhHUm7j63jgu_-sc4UzXguSH2A-LD9I7UrwgAmxUooY-gW5CIoIBULn_FTsMqYwIEHTwbvSff8vROqcVLKyKyn3t4zR8eWgPvWCSkJHmrsIF2M7Dc160UPTqkrXEzjUaPDt-4BtD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1xcmdoVFguVBsSoshOJV-fPuAkMgt3kzBtwKWbrlxlSpCP1lM8cz7dAthIJ4MQwcjmJXMufrryoa8Fi0y7ZqYHGkn1L9Oo28vqcHbv_wpm6x18bEJ5xShwH_gBl6XPdfQkXKoJidJyzG6jkhyagNED0NkWhAjPSkv45UOTSZx6e0dRFiMc4cfeIx6-PpRmXcHbb8VE2sVp_MlIqaevxZijPYwszvZBUuDWxjNDbIbsWm-vikP_TiXet01VS8kRfxrY-x-5pkPNFFNyloB5WUZJBnaVSulebKk62wQa4tm4_ZADKABRNva6qXr5ekhqbZ749wZprGzCqNDbZJwIfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8kHB5n6ODQax8hT0UCPG2XQG1W3nNurxjo8ScRfcS03Mb6_GN9dMqKfeAgtfAtrEK5G4ChQ342TbczjmBxMz3dq6gFoAL5Ucqf8lfM3ewN7Fz0xQUyFjq-HOCXeLpv69BkxJyWu2ysFkE6_8AdxS6v6y7JQfpGvjqiWavb13dtFI64HFuvD4BiILXD6qw645pDE2CzY98eRiyjrpA_oTYrkcnVFxKfmldr_1uY1If_obcuR7FDz8-UF_p_Ei77tKC0iU4olCd7zX3hbb7Dil7G7BDl3XhS4A0Y7aRINkHwKynN7YBeC5EPULG1hPEnsj0fTLSM71-0NAV1CIhmbEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دسر‌های ساده که می‌تونی با بیسکویت اماده‌شون کنی
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/669437" target="_blank">📅 13:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsY-0AcBXufeGJvAFe6Grw6dY7_cfTALNXEH8WjiowH_cofALMWEeV9i_hqajx78Kckg2T8On-omTMqxGj37IC-e9wMBMxfQ2_sbgJ8W6Hc56snAeHRrAgBHJ8BAOnMsZXh4KE2adRk051pGcKCJzwwfvcKlWnvmHhgqU85cDGxEgWFxxdwgiHhv9wTGLTK_T8Ot3l6NJCsaZiJYBogv1B-oCtaYdbl_m7ZAgTB3NNqU3mb6fMxK-Eo4yZNckB-PTDV13OZb2ALX5k31ogZgtHy-1X1P4pUz_225HFFvkM4Xs87DwOUecueJFQn2GiZs0SN1fv61_EUpZP3Fo6U7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ شهر ایران در میان ۱۵ شهر گرم جهان؛ بندر دیر گرم‌ترین شهر دنیا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/669436" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f13f441b0.mp4?token=SdtdeUlZtNPxvjE_tbmfWCnqE_JA_r2d5mnq4kTBF5q7n3U4iH4y1wZWtoML6ZM_8baoGzisy46u10w5O84Qnz264LFFTpAYLqgsJ-uZKGqs_YJBMdbwH699uaDRWHr_zazONQ0FFhR0QE7p4TwM0Olvuywrd2xx2Cs52Mgnxlp-HfR9MqDQI-KK2XPBFsCQZyhhK3eiYAcVW3gS6s8tfL0nAvLOyEd0mKERqlIHoS_0NgzEFF91PeClOVFuEKk9dBTV_OJn5pQ20EwGtsuFvBX--gY8PLaSpJc3qhFDsGiyLG2wgky9TZW6GVXfyYORAc7SGwdBG4hG5mAAC67YgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f13f441b0.mp4?token=SdtdeUlZtNPxvjE_tbmfWCnqE_JA_r2d5mnq4kTBF5q7n3U4iH4y1wZWtoML6ZM_8baoGzisy46u10w5O84Qnz264LFFTpAYLqgsJ-uZKGqs_YJBMdbwH699uaDRWHr_zazONQ0FFhR0QE7p4TwM0Olvuywrd2xx2Cs52Mgnxlp-HfR9MqDQI-KK2XPBFsCQZyhhK3eiYAcVW3gS6s8tfL0nAvLOyEd0mKERqlIHoS_0NgzEFF91PeClOVFuEKk9dBTV_OJn5pQ20EwGtsuFvBX--gY8PLaSpJc3qhFDsGiyLG2wgky9TZW6GVXfyYORAc7SGwdBG4hG5mAAC67YgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای این دقایق روضه منوره و حرم مطهر امام رضا(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/669435" target="_blank">📅 13:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fd9b7e8d.mp4?token=G4Q2BpWioKFKnFidY-5FUPR3CWMNSzvm1TfHGAXc4bKG-z-3LbM__gHDDBdfp1048DLyZWCCCIiLkXKp53vnsPb5qa0Fb1Pdz_CmtOg08RlESbuKGGUhSYx6HB5O9p1UxnVklCeeDxX_VHkaQLNEbF0f0up3wWlmBhregspB69TTmyDYQE0UwfkWaBgwJUiEKHj9pDeoC-ivOs_4_4pe14had_SuDD1ksKiF8QxrA_Qy48tTwPnIyRyILe5N1Rd5keV16WVMsh7--oppJvuBdoWq5EFqxTaj_zYeiaPYpZYtQm0YfEm7UpcejZTrLxuhbcVkw0hDhT81z9s9FRTkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fd9b7e8d.mp4?token=G4Q2BpWioKFKnFidY-5FUPR3CWMNSzvm1TfHGAXc4bKG-z-3LbM__gHDDBdfp1048DLyZWCCCIiLkXKp53vnsPb5qa0Fb1Pdz_CmtOg08RlESbuKGGUhSYx6HB5O9p1UxnVklCeeDxX_VHkaQLNEbF0f0up3wWlmBhregspB69TTmyDYQE0UwfkWaBgwJUiEKHj9pDeoC-ivOs_4_4pe14had_SuDD1ksKiF8QxrA_Qy48tTwPnIyRyILe5N1Rd5keV16WVMsh7--oppJvuBdoWq5EFqxTaj_zYeiaPYpZYtQm0YfEm7UpcejZTrLxuhbcVkw0hDhT81z9s9FRTkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مجری عرب به تشییع میلیونی رهبر شهید: آیا حاکمی در جهان عرب، حتی یک نفر وجود دارد که مردم برایش چنین کاری کنند؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/669433" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
این بار روایت مشهد را یک مهمان تعریف می‌کند...
🔹
شخصی که از کشوری دیگر برای حضور در مراسم تشییع به مشهد آمده، از نظم و پاکیزگی شهر شگفت‌زده شده و از آنچه دیده، فیلم گرفته است.
🔹
گاهی قضاوت یک مهمان، از هر تعریفی شنیدنی‌تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/669431" target="_blank">📅 13:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669429">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhijqSnYxqL3P8V3c6JkI_M7p0CP5O2T8jfC-_dRYi04lrucsNsZmvGf1qbNTpa8wlcI7maXUtN8nd9W5Vb2_dlDXU8JK58lYYmPifj1d8dwD45J4hW4VXJuFjQRrd9efTZxELVBCHKFpTNTQCx3xdIXB8P2HxHIdEyPrazft_5u1W9_JR03R1OTYM8jbgFctZdQbT1nhyl3TED9qPnmXlKBYZ_QdHq7VBHeHM9xvjFV7RBS0zbhPL0YvIxfHpxCHqxN2YessLMyoGrtGhC2corIe2eYw5r6V-x7AHrGz7XFamzNrN0svyYk4jkP5os-LVrA6_dh6X_4MRvKA2RbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشورهای دارای بزرگ‌ترین ذخایر ارزی جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/669429" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بیمه دانا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imWgaFKj7JTSYYE6D1qO8thA907b9TIO0r1uCj3AW0Po-gGXxjU7s-PAENBa19DPUdQP21aoE98UwHVXJZbb1ZKoENGVLaB0RslAgyupVEJIHZen-4KCHE_rSccpY7h8MOyOcYz1KW8Dpewe7ICZZvLAC72CfT7LdbBlGgabpRpSF9CaTNsrbpsI2rOPXv6vIpn6_nbdZuwS4DFtaMtiyNnrQtrpg893qsNKezg66c_jGEii77wtPbkmNizeh0y0Vm4-da2-HBlm5QYPMYL-GOoRjze6E7W0-tqeDXe61kCP8g8lvF-rttHWq_lviJYm-YxtUDX-Roczi7L3fhnzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
حضور همکاران در ایام تشییع رهبر و آقای شهید ایران ؛
ارائه خدمات خسارت سیار بیمه دانا در سراسر کشور
🔺
همزمان با برگزاری آیین بدرقه، وداع و تشییع رهبر شهید انقلاب، شرکت بیمه دانا با هدف تسهیل خدمات‌رسانی به هموطنان و زائران، خودروهای خسارت سیار خود را در شهرها و مسیرهای منتهی به محل برگزاری مراسم مستقر نموده است.
🔺
به گزارش روابط‌عمومی بیمه دانا، خودروهای خسارت سیار شعب منتخب این شرکت در استان‌ها و شهرهای واقع در مسیر تردد زائران، به‌ویژه در مبادی ورودی و خروجی شهرها، مستقر شدند تا خدمات ارزیابی، تشکیل پرونده و رسیدگی به خسارت خودروها را در کوتاه‌ترین زمان ممکن به بیمه‌گذاران ارائه کنند.
🔺
این اقدام با هدف تسریع در فرآیند رسیدگی به خسارت‌ها، کاهش دغدغه هموطنان و تسهیل تردد زائران انجام می‌شود و بیمه دانا با بهره‌گیری از ظرفیت شعب و تیم‌های خسارت سیار خود، آمادگی کامل دارد تا در تمام ایام برگزاری مراسم، خدمات مورد نیاز بیمه‌گذاران را به‌صورت میدانی و در سریع‌ترین زمان ممکن ارائه دهد.
🏴
بدرقه آقای شهید ایران
#یالثارات_الحسین
(ع)
#باید_برخاست
☂️
بیمه دانا
📞
02182468
🔰
@dana24_insurance</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/669426" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آ
مریکا: همچنان به تفاهم نامه با ایران متعهدیم
🔹
۱۵۰ نقطه ایران زده شده
🔹
بیش از ده‌ها قایق مردم نابود شده
🔹
چند ده شهید هم داریم
🔹
برج چابهار و راه‌آهن اق قلا تخریب شده
🔹
پول هاتونم که ندادیم
🔹
ولی طبق تفاهم تنگه هرمز باز باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/669422" target="_blank">📅 12:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgalDsfXT1Ii05hFcEQa2Cw6DxQBNXh6UKloCBVywPfX3hu1_Ctfkj6J16oZDRjjzXhpR0gXtDs26_YrUnrK20FcP4sV02Q5-PNdr6DzOv-q5bzZ7_FRnPSt-VjR-IFh04XIdY50VHUlixpppnWYNv_Xo90MjFHet1AyTBl4joDK8Xk5DrMVdr6eIpvWWIyF1GAgCm2GAzoW5JR2MGlqDYOxvRJk7CR72P44B9OtoKNeDsY1Hqs9RGNfXsiWXh96sV74eGy1-FOu8486iwsXFEgT59WhCv4t3ZyFz_7FzY7Viq-QgBGRlei2odmR5HjcIUdMfQzS4cVhBzXDaPhmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت عضو تیم مذاکره‌کننده: تفاهم خوب بود و شیوه اجرای آن هم تا الان خوب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/669421" target="_blank">📅 12:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669419">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sezTbtO0DehCHDfdrANd_9f0k2-PimfaJIna9a4mjsrUAKW4YbqtEX64rvQiSATPp-si7Xk7M0B4IbjMjxcvdDyPoT0jZvTHB_6f4M5i9BRs_HScdhdFxUwvReiGSuZ-J0dA5Z0C6YlYeznbtdh5PAWe8soy3-ufxA3QokZr7iPbTCAydIOhbG4GzobNBCCd_o25QdFRliLLy5BQQ3RgT1eiQ06vseyTI8Lh0ckHUW1f7cbfAQ_4Un1TD6j7SqWYB1-fumT-Wv8_JVOaERnT3amZqkuFTBYT6EgmuRjV4Fw9HSVo8JAkGR55FqeRAOjoJMPYtd4eeivlqtyLaKt5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت جدید اینستاگرام؛ اجازه ندهید از عکس‌هایتان برای هوش مصنوعی استفاده شود
🔹
اینستاگرام در اقدامی عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند.
🔹
اگر اکانت‌تان پابلیک می‌باشد، این قابلیت به‌ صورت پیش‌فرض فعال است؛ به این‌صورت آن را خاموش کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/669419" target="_blank">📅 12:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669418">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0393983043.mp4?token=Iczr-aMAbPphsPm2vQMCV3q-WE6zeITdgUfz5rxystuoa91VrK6_Rnn6dV8k17KMvt0I0BkzBp9k2epSm1kIQV3bIMYTgLSoxP3EciSaUpwGlVCsFQFI5gsXKaTfLYwv5RisOXoXEQZKihDVEfbA-rsPiKlGMcOocQOm3uwN2xW8lXnz548Wih0NHl9x1rJe06TMWNiuJnRdoynYECUeFYe0Rmz5QqSXboYTxDvbdBoKEZEfn67_oh-yIbHm5ypS7ehoW47Sx79YDORoeYAK_Bs8BqGPxeTzqYwRhUk49At-MhoZi4bxiOTJYlXEixZHMSQ_AuoOSGwBsSgx4hDjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0393983043.mp4?token=Iczr-aMAbPphsPm2vQMCV3q-WE6zeITdgUfz5rxystuoa91VrK6_Rnn6dV8k17KMvt0I0BkzBp9k2epSm1kIQV3bIMYTgLSoxP3EciSaUpwGlVCsFQFI5gsXKaTfLYwv5RisOXoXEQZKihDVEfbA-rsPiKlGMcOocQOm3uwN2xW8lXnz548Wih0NHl9x1rJe06TMWNiuJnRdoynYECUeFYe0Rmz5QqSXboYTxDvbdBoKEZEfn67_oh-yIbHm5ypS7ehoW47Sx79YDORoeYAK_Bs8BqGPxeTzqYwRhUk49At-MhoZi4bxiOTJYlXEixZHMSQ_AuoOSGwBsSgx4hDjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اندازه‌گیری دقیق پا برای خرید آنلاین کفش
👠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/669418" target="_blank">📅 12:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669415">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu6qoXjSQ3wTiECPobijiIJgQtL1C1_AJHW64XwJ3sqPMbIexhv-Bdv1Bgb5_sC30pxouw7OwC-hS2NH3mkUKNCxWYpFXrDBinewl3MEz0OsOJOjOIgLCDAndBuKSfUO-Y0pHR1b31yGPpi4CTzpwC4ERbUH_kArDM5Fcxg6e7gWFxCwMNQkJ24zwN3Udfo1kwi2KRXdE9_No5okGvt1Jm_wSlgdIKvQM25ULG_hsiWmGmgxuTQJFSpR-c_KzMFl21mPkElnMsLYdc3jH2gHZG_cLSWCMeWAjJlrpGhMGjslFWYtLdRH8_cZwJhnh6Jaa0p1PZ9ymVvJ6NAwz3q1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز درباره ادامه مذاکرات آمریکا و ایران
🔹
خبرنگار شبکه «فاکس نیوز» امروز به نقل از یک مقام کاخ سفید گزارش داد که گفتگوهای فنی درباره برنامه هسته‌ای ایران در هفته پیش رو ادامه خواهند یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/669415" target="_blank">📅 11:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669414">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwe1Qz3mrqt2vGYm_09Y0zW5qs66votVxDqlBD-0e-tTsZvbF76XiQSlKAlE_nX0VK0I9s1gzKEsh0rwr8zFy_LtvdkheITIMRXymCwyh406JPkwQubALG837puyuXO_88F0X95TVZaOLzP7bO8YiZcpGFM0dWR4v7nhYRDmTg87mQe4wkExr-Kx784YjyKbGVroxdty8bnaSHiIgMTtz1JTImTAySo_Yq9A-jlzncYbIdCI68NK0ZBo5ZVuUSwvkw5L3bqcBAIW33S85jzb3VJ0V4BTGFfHfcFnGBb8U6IFOMchEdlz9J1n8mXSirvwZ9Knr_FuocZjn5fKGtQ1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجره‌نامه نورانیِ رهبر شهید
رهبر شهید انقلاب آیت‌الله سیدعلی خامنه‌ای با ۳۵ واسطه فرزندِ
امام سجّاد(ع)
می‌باشند که در شبِ شهادت جدش در جوار امام رئوف آرام گرفتند.
السَّلَامُ عَلَيْكَ يَا زَيْنَ الْعَابِدِينَ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/669414" target="_blank">📅 11:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669412">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27582de67.mp4?token=ClnucxG8FvJtJrDlDqHxwedfdABJcxwGIrCbrO4XtPDHy8MDhCyIvAGMLKe-X7ObI0A_AunZ2GYrI2mhxGxJYUWGt8YV7cJo-ZzKkIo6Grfke-Sbji56cMWmLMz_uFXpukIug1wA4W37lv4xNQFS8OyYJZI0V0tWjT-FFcfwPRJRoFBNBhGs5yUr3wxweBWtqMQcb_mgldJtPfsxG9Ded2QY5JWIvfXpfZMJl7JJcD0UQKV6VaMmxgJKzzsBg67whLHpQh11wp_lAsWF8_4AWrxvLxkXxg6j6KyY9_RaY5ulSTYz_QbXk83U6cBpHNm4oQxvtbNpQ6Cng4npaP9PkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27582de67.mp4?token=ClnucxG8FvJtJrDlDqHxwedfdABJcxwGIrCbrO4XtPDHy8MDhCyIvAGMLKe-X7ObI0A_AunZ2GYrI2mhxGxJYUWGt8YV7cJo-ZzKkIo6Grfke-Sbji56cMWmLMz_uFXpukIug1wA4W37lv4xNQFS8OyYJZI0V0tWjT-FFcfwPRJRoFBNBhGs5yUr3wxweBWtqMQcb_mgldJtPfsxG9Ded2QY5JWIvfXpfZMJl7JJcD0UQKV6VaMmxgJKzzsBg67whLHpQh11wp_lAsWF8_4AWrxvLxkXxg6j6KyY9_RaY5ulSTYz_QbXk83U6cBpHNm4oQxvtbNpQ6Cng4npaP9PkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش تشخیص ۵۰۰ هزار تومانی اصلی از تقلبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/669412" target="_blank">📅 11:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669410">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d613292d3.mp4?token=gN45s2ReL9-dJhKeofPlrny5sPCE0ogvY6RICXhlu6UPZDlUA5N3L37hdD2OFPVMcu7uruGlsacxFZ2XOJiIrO2pod7PcQzAHFJNvToiLvJzLLJZqxKleJyZcfHzcTadSDi4-symnHO0pN2GpBmQQzP9bxvbM3q-9a6V1xW6uHlJyz-li3wFkX7GcuoXkHjaikFlTbpAocZouiyUtJ2fmiJJH8y4jrA9dHTZYCsw2mBte9QTe1cXzulD1o67e3cDG40kdViLRjfFEy12vPzkt3WY2muxQttGfq9cPAcOUiRg9DbLSLhJ4pAcKYIGb-N0Bxsacu2WU2BkZZuvE2bERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d613292d3.mp4?token=gN45s2ReL9-dJhKeofPlrny5sPCE0ogvY6RICXhlu6UPZDlUA5N3L37hdD2OFPVMcu7uruGlsacxFZ2XOJiIrO2pod7PcQzAHFJNvToiLvJzLLJZqxKleJyZcfHzcTadSDi4-symnHO0pN2GpBmQQzP9bxvbM3q-9a6V1xW6uHlJyz-li3wFkX7GcuoXkHjaikFlTbpAocZouiyUtJ2fmiJJH8y4jrA9dHTZYCsw2mBte9QTe1cXzulD1o67e3cDG40kdViLRjfFEy12vPzkt3WY2muxQttGfq9cPAcOUiRg9DbLSLhJ4pAcKYIGb-N0Bxsacu2WU2BkZZuvE2bERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بله آقا! حق با شما بود
💔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/669410" target="_blank">📅 11:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669409">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOSFjsYBupejngVLExjDmfX48x_CalHy1WsIF4dQezJx8xf-wgd8nFxCQDO1ZwgjN9DfK-26WyCbb7Ynj5tfHRYtjbc_r6tHtcK1nK4AQup1oKjpO0Bazm30ALxnW3PH4dkfP0FJN-Ki-iO8ZVqDNImBpX_L8pNYptTGpA96pTepUg24TTJ6pg-y7TpgM9GcwrMDX1A0PLXeA-r0WJWvDDQep9gyG1BYLCiFQwAFOa-CUPpdvwbmSSf72zQZnqm_AgEJOOXGcmRI3lu9zaoeoyfSlonHsOSUMc7J6pC3zkjNXNLwo06mrafJ-Mchj-Ap6Im4OeaqkgP3bxQBmDZOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی ویژه از طواف پیکر آقای شهید ایران بر گرد ضریح مطهر امام رضا علیه‌السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/669409" target="_blank">📅 11:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669408">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmWIDQutLLgjC5dGhIhBRfiqrtTWQZm_uQSv9k0odRAFTNFZoOj8YtPP9czO4qDQgQtgr_301DYGauRXPG7Qrlgzb2HSUSOJd0-G-w2tUDhrPjmPZx4FX785DWFqLSe55tYH3N37eXI3dpBNRLLogHgh1DnBbFITFEdCiaRssU-I7eAxq-KfHRUpy0eghRlWZtWaIqnKCBc1RR64pYG75eL7xqMo75LPooivY_e32HzwXoKC56l0zR1ncHIw234_QA5gp6nrUiZ_7AOsDArEJgwjjAJunXIKABNaJ0mkK2W2MkMJplwupiJFU8d1vLxzsU19pnVNPLkUdmzGB3J0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاتالوگ کامل انواع مدل خودروهای آلمانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/669408" target="_blank">📅 11:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669407">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آغاز پیش‌ثبت‌نام حج ۱۴۰۶ از ۲۱ تیر
سازمان حج و زیارت:
🔹
پیش‌ثبت‌نام حج تمتع ۱۴۰۶ از ۲۱ تیر آغاز می‌شود. در مرحله نخست، اولویت با ثبت‌نام‌نشدگان اعزام حج ۱۴۰۵ است و سپس سایر دارندگان قبوض ودیعه براساس اولویت فراخوان می‌شوند. پیش‌ثبت‌نام رایگان بوده و از طریق سامانه‌های «پنجره واحد» و «حج من» انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/669407" target="_blank">📅 11:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669406">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
وزارت آموزش و پرورش:
🔹
آزمون‌های نهایی بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
🔹
دانش‌آموزان می‌توانند برای دریافت کارت ورود به جلسه آزمون‌های نهایی، حداکثر تا ۲۰ تیرماه از طریق مدرسه محل تحصیل یا با مراجعه به پنجره واحد خدمات الکترونیک وزارت آموزش و پرورش اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/669406" target="_blank">📅 11:00 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
