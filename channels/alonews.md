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
<img src="https://cdn4.telesco.pe/file/NaDwbfPmI2EfXR5CuA6pz9kb3wddb3RksZ7gpIj7a4dYGBm3Ma9tBqYcm_OrtAavKcwfAww8OqdhPlccBb7xxL6P4ygm5fS2F7PAgJIQBnodV9WFxudUBO4yXTFNU1ElUaQzt0kbPsOI2hSRyxhkqKOmfJja9TBCbJnUY_mRu2PBdyYHNPY0X34yNIkSBP8Z2L5drA4nk2IuSSkFw-zzINcdYVLAXMuWp4pC1ikMSklWMfM34tI_8_NlR1dESRd2sDFD2_7Tsx3QUyC4d2bCIkg8kogrgc22QGLc7UXA95Kt9-3i92UMKullQjKqdSiam3M9PC6b0hCCW6OJiWM1QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 16:07:16</div>
<hr>

<div class="tg-post" id="msg-121770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/alonews/121770" target="_blank">📅 16:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121769">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRnZjsHK5cn0phUylHCyNhjygSpoLw3M3V33magZ-fXj-KP33BETvBbtuh0JVKWQvjba1nuYs1iNqTpaagVv-U_e8HOUAeq6NnE6XrftFMc6Vr2ibNTM8I4zLYCODlWEpl-wKA078eYyK6YWTvJ1iMjRnvtO-HRgCU264L_awP11jo98IsFXwHq_uhYIacmr3NYuxL_L0a62wFdbgIEf0kTvXJNLfuHC9uENFyce2IPOzH2YZHIVu1KvWAKKqsOA4nsT-H-m87WUypiaa6dAsMStAY2GXSt5KpFJyuXDUAPX3prSflRWxGr0tVw2L4uVUcRGIRH0vS-m0vVm-WOvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه منوتو دوباره خدافظی کرد و از پایان پخش و اتمام فعالیتش خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/alonews/121769" target="_blank">📅 15:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121768">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری/الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/alonews/121768" target="_blank">📅 15:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121767">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پاکستان: سفر عاصم منیر به ایران را تأیید یا تکذیب نمی‌کنیم
🔴
سخنگوی وزارت خارجه پاکستان درباره گزارش‌ها مربوط به سفر فرمانده ارتش این کشور به ایران سکوت کرد.
وی در پاسخ به پرسشی درباره سفر فیلد مارشال عاصم منیر، رئیس نیروهای دفاعی و رئیس ستاد ارتش پاکستان به ایران گفت:
🔴
ما نه می‌توانیم این گزارش‌ها را تأیید کنیم و نه رد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/alonews/121767" target="_blank">📅 15:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121766">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/elo7HH1e6viYjdLK3uTiIZsWcgTIB8Pia5BMIn93dhcxgjtH013nciR8gYJDm8EK6RohuYWLrdGOqerLsN9R6MHlmf0pLsq2Jn986_yjVQeihEXAqRfrMmCl-r4h_XlyTd1tVJ3U8b7312_7opwPclELW1RkC1eSc6-yviOEp7KLBMOnomY0OJdDbGl-GT5aV9bYtx0aDgqa0DvNVcXoT-3o39G6vcGz1EvfptTttabM3JcSYXzlz9uPXtV-2-x7ixdMMLYvQr73daiKBYVGCIEMkec29t7BM5qkczNYQCwr0sIO5-3JH_CT2Uj44S564B-zREDTYBYUX8ERyL4qaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت تلخ:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/alonews/121766" target="_blank">📅 15:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121765">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
صداوسیما:
حکم قالیباف رئیس هیئت مذاکره کننده
🔴
اسماعیل بقایی سخنگوی وزارت خارجه، سخنگوی هیئت مذاکراتی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/alonews/121765" target="_blank">📅 15:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121764">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzm9h27xNNij-dSCIJ94WTSyR4ADj8hO7cqd7cu1KXSvW_qvxBF8p5Ecu-J82qrmIxaoVge0UJx7WN9HHZGWrztbhR7SnGxiK8dOqgeV_ztoIlGMLH1bmrsfaOqztMmnv2_xu2Lk0Ip5XnWMVhJKErprhWU75odqmQP4lMPoadOt0F0padZpflHdISaTxsyu8Wpr4rPKR6HatRJctQdzlKL-gqSqRS2dPoZCc-fo2NcE4HQA4gAkq4euW4drmh80XtP1OYhU7ajChJnQ-A0wsfdZ5rUpy6lEOYicP-XV0Zbv3TLSSQgeWr2_ZzzmDn3nzdjbxQ9R8EIzb2fgA_KvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/121764" target="_blank">📅 15:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121763">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e9244fd77.mp4?token=QhvjILqjcDlRUB61vzCbE6T75oiRCR5yerAVEuaLp7cAqhvpWXvS1r8eyRFlq5b_Li5kIhAcMg_rHnvTB6qz_IsOsn5C4UsQsvfgzDX40VjoVdKANmV2J7KSJ_pu6bJppV6K2f4jAnift83GyprTUke7yYCLp0VGtd6IPp28jCUkwOvHciKM0l0EoSZjQFCK0YgZ7yXcB73Ks3-ZVxTqZzcUdMbZRo37kpt1MzNbmesoOcaXZnesXo0w6-PJLwJZ_bo7eZ_cIiQVI91XnfWsrFTDMPLCrBw0sD4jLqLfKFzbiUsVKAIQj4-EUEmLF0v-tivrEgymvxCKC_vPOfgwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e9244fd77.mp4?token=QhvjILqjcDlRUB61vzCbE6T75oiRCR5yerAVEuaLp7cAqhvpWXvS1r8eyRFlq5b_Li5kIhAcMg_rHnvTB6qz_IsOsn5C4UsQsvfgzDX40VjoVdKANmV2J7KSJ_pu6bJppV6K2f4jAnift83GyprTUke7yYCLp0VGtd6IPp28jCUkwOvHciKM0l0EoSZjQFCK0YgZ7yXcB73Ks3-ZVxTqZzcUdMbZRo37kpt1MzNbmesoOcaXZnesXo0w6-PJLwJZ_bo7eZ_cIiQVI91XnfWsrFTDMPLCrBw0sD4jLqLfKFzbiUsVKAIQj4-EUEmLF0v-tivrEgymvxCKC_vPOfgwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعال آلمانی حاضر در ناوگان «صمود»:
در زمان بازداشت هر روز من را کتک میزدند و آب و غذا نمیدادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/alonews/121763" target="_blank">📅 15:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121762">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeC6B1IVR_HMSnpPhhcpz-ED0ySOV5pL1dLdrDw6LwQziLA_xTlKBl71sXLfYmGWvhfpszJVXYElzraOjAM2u0MwW6-gayEW51Etiq9BssvngaFtR8IS_diDijXnAOzo6FrDfQt3KGfkZJRs-tfKJxsI-C30pbfLJYFb-18JIec9XxHvhCW1rX1tIQHNHiXexCDj7ubzHdJ4sn6gdc17Jh6RRGIsu1fL1sonOkcTZnlaL-E2R2HNPfOd5a1bNMBNcOltrXMB1V70rK6LJcpqigDxjWHMSae_v3TgPPOFuuuVku_Sh2Qp-H7BzBcdDAXPsDF2aGRpTONfeltJKhZa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پس از اطلاع از لغو برنامه چرخش نیروها به لهستان توسط پنتاگون، از وزیر جنگ پیت هگستث سوال کرد، طبق گزارش WSJ.
🔴
ترامپ در تماس اخیر به هگستث گفت که ایالات متحده نباید به لهستان به دلیل رابطه نزدیکش با کاخ سفید بدرفتاری کند.
🔴
این اقدام برخی مقامات را شگفت‌زده کرد زیرا این آلمان بود، نه لهستان، که رویکرد آمریکا در جنگ با ایران را نقد کرده بود.
🔴
کمی بعد، ترامپ برنامه‌هایی برای اعزام ۵۰۰۰ نیروی اضافی آمریکایی به لهستان اعلام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/121762" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ شخصا خواستار اعزام نیروهای بیشتر به لهستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/121761" target="_blank">📅 15:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: مذاکرات بین ایالات متحده و ایران همچنان در جریان است، با نشانه‌هایی از خوش‌بینی محتاطانه که هر دو طرف ممکن است در نهایت به توافق برسند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/121760" target="_blank">📅 15:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaAQ423A_uu4DX4yXNEtwc5YKo71WZQUqJSSXt1-Xz2ikvb-WTjealrvKOFSRVsaohe0nLlX5uM1MRHVMYRQ6HB6H_ZWkYZNO_jqOPs22Qfpfyl_aO5Y872Ud5q_8LcAccrdZJOOrc2wE00IFxCvCxJ00dchl7kuhSyy2fvTRfV0f9pjaF6RqUYLi0jUAGNx8YEhpSopvwnqU4vDLBiURaNEJEi2xNo4M9Q2wajfV5Sx4dWMaU02J_ONQCUGviI13Z7AJ6-pIXcACkiF8ZU_FxDek6t4HuMtkv1fNkS_8CRspXgz4FBOkuH_qvJLoB4LhUSIhSvY2-SBnDclLpxWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین، کویت، قطر، عربستان و امارات تو یه بیانیه مشترک گفتن کنترل ایران روی تنگه هرمز رو قبول نداریم
🔴
محکومش میکنیم و از کشتی‌ها میخوایم با «سازمان تنگه خلیج فارس» تماس نگیرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/121759" target="_blank">📅 15:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121758">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c194f6c50.mp4?token=iZ_CyOKpv-1t04To2x50tyoC1cGXbYVFtpMpUT6AduHqqOdMpQ0MxaXdd4iVBHNAYYO2B6vIHr3XJCdgdR8Me-z1LlRzpBDVOrz6wNVtKhp8iUrpljf0O3s2UjGXFmMn7bcS4SDKkt6HkiUo6sjRXWtOIDz9VFNzci3DpCdtj0y2kiJwyF_eiZWOCN5QVc-JzU82hV3waEzi8a448-4xVRFIQ5x_wr57UTtqp85m3OLzDHES9JrkaTRiHMnKYzBZdo52cgpZ3HJHlt3ER_z4E2tRGdxjRp3cI0D2GgUd9nECPr190kpGlPpQjR8NbG4wYug4iLhTunLOcxNZquNrKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c194f6c50.mp4?token=iZ_CyOKpv-1t04To2x50tyoC1cGXbYVFtpMpUT6AduHqqOdMpQ0MxaXdd4iVBHNAYYO2B6vIHr3XJCdgdR8Me-z1LlRzpBDVOrz6wNVtKhp8iUrpljf0O3s2UjGXFmMn7bcS4SDKkt6HkiUo6sjRXWtOIDz9VFNzci3DpCdtj0y2kiJwyF_eiZWOCN5QVc-JzU82hV3waEzi8a448-4xVRFIQ5x_wr57UTtqp85m3OLzDHES9JrkaTRiHMnKYzBZdo52cgpZ3HJHlt3ER_z4E2tRGdxjRp3cI0D2GgUd9nECPr190kpGlPpQjR8NbG4wYug4iLhTunLOcxNZquNrKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل اعلام کرد دیروز تیپ ۵۵۱ که تحت فرماندهی لشکر ۱۴۶ در جنوب لبنان فعالیت می‌کند، پنج مبارز حزب‌الله را که وارد ساختمانی در شهر منصوری شده بودند، شناسایی کرد.
🔴
این مبارزان سپس توسط حملات هوایی اسرائیل کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/121758" target="_blank">📅 14:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121757">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حسنعلی امیری عضو مجلس: طرح جایزه برای کشتن ترامپ در حال تصویبه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/121757" target="_blank">📅 14:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بلومبرگ: تداوم مسدودی هرمز، رکودی مشابه بحران ۲۰۰۸ را ممکن است ایجاد کند
🔴
تنش بین ترامپ و ایران بر سر ذخایر اورانیوم و تنگه هرمز پیامدهای خطرناکی ایجاد کرده است. این پیامدها شامل قیمت نفت می شود و خطر رکودی مشابه رکود ۲۰۰۸ را تهدید می کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/alonews/121756" target="_blank">📅 14:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
امیرحسین ثابتی: دور جدید جنگ در پیش است؛ شاید هم شروع حمله از سوی ایران باشد
🔴
گر از همین فردا بخواهیم به دشمن حمله کنیم و در حین جنگ نیز هیچ موشک و پهپاد جدیدی نسازیم، تا دو سال به صورت شبانه روز میتوانیم آنها را بمباران کنیم و هیچ مشکلی از این جهت وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/121755" target="_blank">📅 14:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به دیر قانون النهر در جنوب لبنان شش نفر را کشت، از جمله دو امدادگر و یک دختر، در حالی که شش نفر دیگر زخمی شدند که در میان آنها سه امدادگر و یک زن بودند، طبق گزارش خبرگزاری ملی لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/121754" target="_blank">📅 14:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وریر خارجه انگلیس: از مذاکراتی که ایالات متحده در حال حاضر با ایران انجام می‌دهد، حمایت می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/121753" target="_blank">📅 14:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121752">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اتحادیه اروپا : به خاطر بستن تنگه هرمز توسط ایران، یه بسته تحریمی جدید علیه تهران اعمال کردیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121752" target="_blank">📅 14:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دانشگاه پیام نور از تصمیم قبلی خود برای برگزاری آزمون‌های حضوری عقب‌نشینی و اعلام کرد: آزمون‌های نیم‌سال جاری (سال ۱۴۰۵) به صورت غیرحضوری برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121751" target="_blank">📅 14:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121750">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: جمهوری اسلامی در خصوص خروج اورانیوم از ایران هیچ مصالحه‌ای انجام نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121750" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121749">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gue9Z-7iFJjYdpex2cDQJzA1x9LRdGnvmfX0hlaCo4Kc_ezrGG9HpNPBf8DHIhX5c3Ay9EpPPe0i307wjWBs7yq-DWiylOFC3dnCCA1rpi8B8pTd8nBoIbA5IK4sD5uiAcrkAdYSTqn2Vjt-MUAvbahqqe1cFDSJpbEE1qHfFGxR54XnI4yQlCldC-gtrjLysp-yt-Z7IEKhNbExcrznhfZGxZWId-iymRbWXfiwWh5YoYAcOwcf_ZQqPDfNkpjmdb8OQuDFxS3aDILjDxm1ffsXUDSc9TnQQncr5su5kPn9G-BDAn-LetPHxPAaLN_52x82HgsuZ87ELAA4Bqv8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: کولبرت بالاخره در CBS تمام شد. شگفت‌آور است که این همه دوام آورد! هیچ استعدادی، هیچ رتبه‌ای، هیچ زندگی‌ای نداشت. او مثل یک مرده بود.
🔴
می‌توانستید هر کسی را از خیابان بردارید و بهتر از این آدم بی‌ادب باشد. خدا را شکر که بالاخره رفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/121749" target="_blank">📅 14:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121748">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=qa_kLSrAzdOfp6hBcMXnCZfqxJck11-5AtrHmmy9kF5n1nZ0kCajOCSdSX-96htNk-BZtQl6GyDF2AXSKzvBpYXpox2cn-VgWQpwMVt8Xrs3QN50Uir7QSsFKnQqJpcfVhH0mDYyFiOoL_LeB_nAlfcfz0Zpk1-si46tt9mT7tOxE31h9EbOEoZCDxx6j4W4saqmkr0wvNRIqQi25mmUFJ3qbyf7OuFiDK1TFEyEYZeP5B1xJON9ReC5hgJaMNhgOt0Tfz5byL5kKCsoqHUTroX7G-KT384_g_hFKQVvvNUxuYAo6gaRDb5NPc6k0HGPXmrlh9xqkm_W9hpQASXuBlcNCth-gRPGZ6kcmg6vGBbX1aeJTdzx6UiG3TursSOAK4JeNKG1zFVSZZJwsTJAI_hPRfnxAPquwc7zT-qCSyXa0BIdiGhZO3TENIwK-qId1haXzgMbl1T5sb0gd6AK7LruqcskOuWXbDA1MPUjuuiz7La_PLUq4bZjxaJGgmpQYmf2cPiuO1U8Zex_srbGRAeeVNDJgl1LWntuSaVQfORyAnPNK9bZwD_DrTxJBkcyuFK9Mxio3zThJijbDLqLHNDOVzHn6QrWOICLeq5NtLUMKLpQk5ZxBpxp7klkzpBTJdUdnNGLpO4pBjq2RYntQZ4XLWSwvuFaskAbWz3Gch0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029e0d7a1d.mp4?token=qa_kLSrAzdOfp6hBcMXnCZfqxJck11-5AtrHmmy9kF5n1nZ0kCajOCSdSX-96htNk-BZtQl6GyDF2AXSKzvBpYXpox2cn-VgWQpwMVt8Xrs3QN50Uir7QSsFKnQqJpcfVhH0mDYyFiOoL_LeB_nAlfcfz0Zpk1-si46tt9mT7tOxE31h9EbOEoZCDxx6j4W4saqmkr0wvNRIqQi25mmUFJ3qbyf7OuFiDK1TFEyEYZeP5B1xJON9ReC5hgJaMNhgOt0Tfz5byL5kKCsoqHUTroX7G-KT384_g_hFKQVvvNUxuYAo6gaRDb5NPc6k0HGPXmrlh9xqkm_W9hpQASXuBlcNCth-gRPGZ6kcmg6vGBbX1aeJTdzx6UiG3TursSOAK4JeNKG1zFVSZZJwsTJAI_hPRfnxAPquwc7zT-qCSyXa0BIdiGhZO3TENIwK-qId1haXzgMbl1T5sb0gd6AK7LruqcskOuWXbDA1MPUjuuiz7La_PLUq4bZjxaJGgmpQYmf2cPiuO1U8Zex_srbGRAeeVNDJgl1LWntuSaVQfORyAnPNK9bZwD_DrTxJBkcyuFK9Mxio3zThJijbDLqLHNDOVzHn6QrWOICLeq5NtLUMKLpQk5ZxBpxp7klkzpBTJdUdnNGLpO4pBjq2RYntQZ4XLWSwvuFaskAbWz3Gch0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از آخرین وضعیت تنگهٔ هرمز و کنترل آن توسط ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/121748" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121747">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
طبق داده‌های دولتی ژاپن، صادرات خودروهای ژاپنی به خاورمیانه در آوریل به دلیل اختلال در مسیرهای کشتیرانی ناشی از جنگ علیه ایران، بیش از ۹۰ درصد کاهش یافته و تقریباً به صفر رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/121747" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121746">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اتحادیه اروپا : به خاطر بستن تنگه هرمز توسط ایران، یه بسته تحریمی جدید علیه تهران اعمال کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/121746" target="_blank">📅 14:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121745">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روبیو: برخی از واکنش‌های متحدان ناتو ما به عملیات‌های ما در خاورمیانه به خوبی مستند شده‌اند و باید به آنها رسیدگی شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/121745" target="_blank">📅 13:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121744">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6f8a0346.mp4?token=NweTeTHopUVZdOSMi_aqPY2d_DgH_ExXdRpJcBRLtg9XAykcxOkKSLIO3JSUn_eqISve_Tt3dHCl454ov1S2p0Mw2j_BK4YmvpZjvAxq7bu9ZtOP1xWWJ9ITP03eNP8_Dx4YC9LBp2r1IhwIIxefnkZWnGgKcUjgBYgzIaDQqe1ogLZmlHfVixSAWGenXIkJixZgIQna0Vf-hemBu4vLyh1j-x6jRzzfmnAoxeQv4OUII0nymwRzFxVOFoBDGkSzEYliPnX4BSRwJCmNNdgok7A1ErCFedycyiR6ChpUZsWRYLYpkqAGGhL6eBfwddS4oq_nqjb7WGfGLL6e4q3z3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6f8a0346.mp4?token=NweTeTHopUVZdOSMi_aqPY2d_DgH_ExXdRpJcBRLtg9XAykcxOkKSLIO3JSUn_eqISve_Tt3dHCl454ov1S2p0Mw2j_BK4YmvpZjvAxq7bu9ZtOP1xWWJ9ITP03eNP8_Dx4YC9LBp2r1IhwIIxefnkZWnGgKcUjgBYgzIaDQqe1ogLZmlHfVixSAWGenXIkJixZgIQna0Vf-hemBu4vLyh1j-x6jRzzfmnAoxeQv4OUII0nymwRzFxVOFoBDGkSzEYliPnX4BSRwJCmNNdgok7A1ErCFedycyiR6ChpUZsWRYLYpkqAGGhL6eBfwddS4oq_nqjb7WGfGLL6e4q3z3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه ویدیو از خرابی‌های بعد حمله‌ ارتش اسرائیل به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/121744" target="_blank">📅 13:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121743">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سی‌ان‌ان: آمریکا نگران موشک‌های کروز ساحلی ایران است، زیرا این موشک‌ها می‌توانند کشتی‌رانی در تنگه هرمز را تهدید کنند؛ ارزیابی‌های اطلاعاتی نشان می‌دهد که حدود دو سوم لانچرهای موشکی و بخش بزرگی از موشک‌های کروز ساحلی ایران همچنان فعال هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/121743" target="_blank">📅 13:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121742">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
اسلام‌آباد به شدت روی چین حساب باز کرده است تا به پیشبرد توافق احتمالی آمریکا و ایران کمک کند، و انتظار می‌رود نخست‌وزیر پاکستان، شہباز شریف، در مرحله‌ای بعدی به چین سفر کند، طبق گزارش العربیه که به منبعی پاکستانی استناد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121742" target="_blank">📅 13:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121741">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر نیرو: با وجود بارش‌های خوب امسال، استان مرکزی و استان تهران در وضعیت ضعیف آب قرار دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121741" target="_blank">📅 13:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع پاکستانی:
هیچ جایگزینی برای توافق موقت بین واشنگتن و تهران وجود ندارد
🔴
کاهش فاصله‌ها آسان نیست زیرا هر طرف سقف بالایی از خواسته‌ها دارد
🔴
مسائل بزرگ در توافق به بازه زمانی طولانی در مذاکره نیاز دارند
🔴
آمریکا و ایران بر مواضع خود درباره اورانیوم پایبند هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121740" target="_blank">📅 13:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121739">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbeee07e55.mp4?token=ISDDhwiWZWm-S95QNd0N076ODS3iMxm-9uFcftBssMV2lpTMKJ-aCeBbGjUr0_K9_E_UeECUKB77hxsN_saSMh_A5MiLC9JkqmSJLgEGsFoJAhVn2L2evQqvay7H6ZOCeceTIyAigsAZHxV4TiTWr550_FmyCuxPMeriiZEWMwKIAVL9k_sK9MsjlYRG1CcZybHmzFs7bGIe569U2fpECiAswA1CSGjMY3wvkZ1_WvyklQ_Me3r1L7nyR9MZHydnXufUxlwN8FqDWYrGS388FtOhjX0BYn1R7HQvhXtGNLyNva5iu_piZRqKfyHwgeoABCp2QQAcdRFRah9Go7JvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbeee07e55.mp4?token=ISDDhwiWZWm-S95QNd0N076ODS3iMxm-9uFcftBssMV2lpTMKJ-aCeBbGjUr0_K9_E_UeECUKB77hxsN_saSMh_A5MiLC9JkqmSJLgEGsFoJAhVn2L2evQqvay7H6ZOCeceTIyAigsAZHxV4TiTWr550_FmyCuxPMeriiZEWMwKIAVL9k_sK9MsjlYRG1CcZybHmzFs7bGIe569U2fpECiAswA1CSGjMY3wvkZ1_WvyklQ_Me3r1L7nyR9MZHydnXufUxlwN8FqDWYrGS388FtOhjX0BYn1R7HQvhXtGNLyNva5iu_piZRqKfyHwgeoABCp2QQAcdRFRah9Go7JvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: "درحال حاضر، در سازمان ملل متحد، قطعنامه‌ای داریم که توسط بحرین ارائه شده است. ما بسیار درگیر آن بوده‌ایم. این قطعنامه بالاترین تعداد همکاران ارائه‌دهنده را در تاریخ هر قطعنامه‌ای در شورای امنیت داشته است. متأسفانه، چند کشور در شورای امنیت به وتوی آن فکر می‌کنند که این امر تأسف‌بار خواهد بود."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121739" target="_blank">📅 13:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121738">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نیروی دریایی سپاه: طی شبانه روز گذشته ۳۵ فروند کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121738" target="_blank">📅 13:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121737">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عربستان: با هرگونه تلاش برای سیاسی‌کردن حج با قاطعیت برخورد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/121737" target="_blank">📅 13:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121736">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c641e7ef.mp4?token=bQBTpiE3OrQo57UzipZ5SK_NKZHa25hDIhWUKQAP_CKU3fU9ft-o12Gkm1DZF7AjhWpxBpGaHoj9-Bzmfvy-3szcgqwCk_MYYh-Td5SLVFNiH4tG6DqRJScxEdi3zTS_F5sj2EREVQud_pKnPNHl9iGJ3hM_Z3OPbVqzXKtbdKy8bUiJ_jg_kXPP-R-iLXNDpMnh1HVS7b0rcLRBO0ft7rVlAysIDqFVamCrNzVnE__fic8StLaxRy2AFtpLJuRZYMz6t1rXgOxCkEy7ESPCHurqz4qmgLhx5_fVJWb-aKel__JqrklTkjvIMF6GxMBd1z3gpDTnFFeuap14jQr47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c641e7ef.mp4?token=bQBTpiE3OrQo57UzipZ5SK_NKZHa25hDIhWUKQAP_CKU3fU9ft-o12Gkm1DZF7AjhWpxBpGaHoj9-Bzmfvy-3szcgqwCk_MYYh-Td5SLVFNiH4tG6DqRJScxEdi3zTS_F5sj2EREVQud_pKnPNHl9iGJ3hM_Z3OPbVqzXKtbdKy8bUiJ_jg_kXPP-R-iLXNDpMnh1HVS7b0rcLRBO0ft7rVlAysIDqFVamCrNzVnE__fic8StLaxRy2AFtpLJuRZYMz6t1rXgOxCkEy7ESPCHurqz4qmgLhx5_fVJWb-aKel__JqrklTkjvIMF6GxMBd1z3gpDTnFFeuap14jQr47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو :  اینکه آمریکا داره توان هسته‌ای و موشک‌های دوربرد ایران رو تضعیف می‌کنه
🔴
برای خاورمیانه، اروپا و کل دنیا خیلی مهمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121736" target="_blank">📅 13:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121735">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انور قرقاش، مشاور رئیس امارات: دور دیگری از درگیری میان آمریکا و ایران فقط مسائل را پیچیده‌تر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121735" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121734">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
زلنسکی : یه پالایشگاه نفت روسیه تو یاروسلاول رو زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121734" target="_blank">📅 12:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CShAIR_hgOfAssz3ywOuayPFyCuvE5Ig9--1U-m8rDiQwkAY80zpOzizGMXVrtWlT3au_pjptggs6M6qiCfuKHIclZOoUlTU3JZ9EQ17kZoyAynG9aUjpKyjs9hVMMkxsqva4EupJZAwAajBNF1ikp48S-KaTEiXIyJQN0MsV5sIJHd61nHdi2PSE_byim7oxbEetsUU4e9DYcZ8RF3I19RtJVuI4FV4DtzLy3OztVGL33R5WOBIbtLhjl9_3s3Za_OC3AwJ7QDT8_WVnLzqp0_Gdgbie1gJwFiE7Emj8HZf4leRH2bIj4RZvOHvNGsZD2MtlIbgDu-gIzr1paQw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای فارن افرز:
«رهبران خلیج فارس از قبل، شروع به تنوع بخشیدن به تأمین‌کنندگان سلاح و مشارکت‌های امنیتی خود کرده‌اند.
🔴
برای اینکه بتوانند در مورد آنچه برایشان اتفاق می‌افتد، حرف بیشتری برای گفتن داشته باشند، باید هماهنگی بهتری بین خود، چه از نظر نظامی و چه از نظر دیپلماتیک، برقرار کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121733" target="_blank">📅 12:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQlio8AMeR_zeG0Oa3IWFmL4MiQF4c3Vq85c1aZm47gHY1_CFr91MgWEXJO9VWvK1D_Mpy46cs7Mej2g_yRVNq6cOaOym2hEkm7JkjTbIDN79IjnoK-N0SfKObc1K8D87wORoNxhJnl1pB_6whCRlY75FD9PdF0CtA6rvyjNnDxTydlsWhQjWkShAUcbtghJiuBaJctFPPYDGdguLCGEUbazVi_5Fk5d5mFDL05PRb7RkOjRqNv3yePOP6oxoPWnb8vxhxl5aWsnDAyWVtJDwXEGlWyUgqvpxE9UhtLSN8C5TXReju-qvQY2Sd-zLL5FdTJSQ3A2aiBuOsEcmac7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ox6IHJQ23zDG18BqkgavFxXKVxziS4eBxfdyoJr665vBsGxgLpfTYpMncXy6UAMueOlP7xOOEueNikvXGBZkgdN7DuiYShqI8D5OIS-d5E2yjh5s76mcZJ1IzgPj3bHC1X6ANz81qlqrE49GhPje9HdTQZ0wXoBZ-P9f-dgNS1YUAkM94JMYf6g2yUuglcvAvB-tt1bjBOXNGaeBcpmNOUF2cuyEyv2i8TIoS1QqHk3JQyR_AUIyzm5z_ctXdAVrhAWS6ctOgDRIw0QUTV3nqgOoHMMau1JZ-_Rwtrvx0Z445kFXxELSEvL273touOxJyOTRihHDv74XNzkbYS4wsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل به "میفدون" لبنان حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121731" target="_blank">📅 12:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
تلگراف: قرار بود ترامپ با اتخاذ موضعی سختگیرانه‌ تر در قبال چین به پیشرفت هند کمک کند.
🔴
در عوض، جنگ‌ها و غیرقابل‌پیش‌بینی بودن او به جاه‌طلبی‌های نارندرا مودی برای تبدیل هند به یک ابرقدرت جهانی آسیب می‌رساند.
🔴
درگیری در ایران به هند ضربه سختی وارد کرده است. این کشور به نفت وارداتی متکی است که بخش عمده آن از طریق تنگه هرمز وارد می‌شود، بنابراین افزایش قیمت انرژی باعث تضعیف رشد، افزایش تورم و ترساندن سرمایه‌گذاران می‌شود.
🔴
مودیز در حال حاضر پیش‌بینی رشد هند را به ۶ درصد کاهش داده است - بسیار کمتر از ۸ درصدی که مودی می‌گوید برای تبدیل هند به یک کشور توسعه‌یافته تا سال ۲۰۴۷ لازم است.
🔴
در عین حال، ترامپ به چین و پاکستان، دو رقیب اصلی هند، نزدیک‌تر شده است و سال‌ها تلاش مودی برای ایجاد روابط قوی‌تر با واشنگتن را تضعیف می‌کند.
🔴
مودی اکنون در تلاش است تا با جستجوی قراردادهای جدید انرژی در خارج از کشور، کاهش فشارهای هزینه‌ای در داخل و حتی منصرف کردن هندی‌ها از خرید طلا و سفر به خارج از کشور، آسیب‌ها را محدود کند.
🔴
این بحران مشکل عمیق‌تری را آشکار کرده است: با وجود رشد سریع، هند هنوز فاقد قدرت تولید، زیرساخت‌ها و نفوذ اقتصادی لازم برای رقابت با چین است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121730" target="_blank">📅 12:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا مدعی شد که فکر نمی‌کنم هیچ کشوری موافقت کند که برای عبور از تنگه هرمز هزینه پرداخت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121729" target="_blank">📅 12:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ادعای وزیر امور خارجه بریتانیا: ما با عزم ایالات متحده برای بازگشایی تنگه هرمز به روی کشتیرانی موافقیم
🔴
شرم‌آور است که ایران با مسدود کردن کشتیرانی بین‌المللی سعی در ربودن کل اقتصاد جهانی دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121728" target="_blank">📅 12:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121727">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b97475f3.mp4?token=HXXzPLnuA7D3yhJEfNHD2o6RQS7QEPuz281Ohkp9JUaPstM8I0hK5AdW6dcUpePLSM1SRqIVpnQ329okPR8UskoYgDbqPQy3WcgGoeoZxnFOUDta1Y30zfsBY5OG7L6yk5EjdXa-QQVsYlRGdsTd5OULOf-REGXyAhLT5TC__jBa6oILqhPoYnBL43uzxgfFj0wICRkaWJOdpYcD8FhlNeFJtjFVTu93TgIGgSVbaBzbSBpzbVNRSsMEfmZjj0AJ5cF1N143B-Dy94Mkunrq3cZdaA15-TmzQZs6O20XRmCdo4Z5cLmKO4LjQ62V8bK5iNJWONBUcKhZKmp3nIu-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b97475f3.mp4?token=HXXzPLnuA7D3yhJEfNHD2o6RQS7QEPuz281Ohkp9JUaPstM8I0hK5AdW6dcUpePLSM1SRqIVpnQ329okPR8UskoYgDbqPQy3WcgGoeoZxnFOUDta1Y30zfsBY5OG7L6yk5EjdXa-QQVsYlRGdsTd5OULOf-REGXyAhLT5TC__jBa6oILqhPoYnBL43uzxgfFj0wICRkaWJOdpYcD8FhlNeFJtjFVTu93TgIGgSVbaBzbSBpzbVNRSsMEfmZjj0AJ5cF1N143B-Dy94Mkunrq3cZdaA15-TmzQZs6O20XRmCdo4Z5cLmKO4LjQ62V8bK5iNJWONBUcKhZKmp3nIu-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو می‌گوید تصمیمات در مورد نیروهای نظامی ایالات متحده در اروپا «تنبیهی» نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121727" target="_blank">📅 12:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121726">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ادعای منبع پاکستانی به الجزیره: اصرار آمریکا و ایران بر بالا بردن سقف خواسته‌هایشان درباره اورانیوم و تنگه هرمز، به بن‌بست در مذاکرات انجامیده
🔴
اسلام‌آباد همچنان نسبت به امکان دستیابی به یک توافق موقت بین واشنگتن و تهران خوش‌بین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/121726" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121725">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: نخست‌وزیر پاکستان در سفر فردای خود به چین درباره ابتکاری مشترک برای پایان دادن به جنگ گفت‌وگو خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121725" target="_blank">📅 12:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121724">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر امور خارجه آلمان: ما در حال آماده شدن برای مشارکت در تأمین امنیت تنگه هرمز تحت رهبری بریتانیا هستیم، اما انتظار ماموریتی مشابه ناتو را ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121724" target="_blank">📅 12:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121723">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری / وزیر امور خارجه آمریکا: در مذاکرات با ایران پیشرفت‌هایی حاصل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121723" target="_blank">📅 11:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121722">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز: وقتی که ترامپ گفت «تمدن ایران امشب خواهد مرد» مقامات آسیایی و اروپایی نگران بمباران اتمی ایران شدند که می‌توانست منجر به تشدید تنش هسته‌ای در اوکراین نیز بشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121722" target="_blank">📅 11:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121721">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0874c8216.mp4?token=SKhbo05ucEzgif-PB2sftCXRRKHd9Umb7MMmsjjub9AQ2RDTwgVeIuP5aSaQ-y51DBAYSLMqdcQMSfToElHJAj_8_1chqi1-IP1PC11JN1P-dckf8FTgANMxEIQ4UExv07vEtVe8BI1AS8nLDhxou-rU0UYbZ5G03qpJgA8tiYsuo7Y9J3MTwu2EHy4641ylXmiDeNIP3aEdCDnnDclypGagUZX1ZIE7nCxlm2zNu5KAR7rfgBz4weFo6-tTgmw6Gg1qeY9sLOB2uoIaxV91mQjxfMT26jnqLkLbucdNMGIUPn6EszZIHbRb_UasAZKKT0Sg1gWmCC_JZlj--fhc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0874c8216.mp4?token=SKhbo05ucEzgif-PB2sftCXRRKHd9Umb7MMmsjjub9AQ2RDTwgVeIuP5aSaQ-y51DBAYSLMqdcQMSfToElHJAj_8_1chqi1-IP1PC11JN1P-dckf8FTgANMxEIQ4UExv07vEtVe8BI1AS8nLDhxou-rU0UYbZ5G03qpJgA8tiYsuo7Y9J3MTwu2EHy4641ylXmiDeNIP3aEdCDnnDclypGagUZX1ZIE7nCxlm2zNu5KAR7rfgBz4weFo6-tTgmw6Gg1qeY9sLOB2uoIaxV91mQjxfMT26jnqLkLbucdNMGIUPn6EszZIHbRb_UasAZKKT0Sg1gWmCC_JZlj--fhc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله با پهپاد انتحاری، یکی از باتری‌های گنبد آهنین اسرائیل رو زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121721" target="_blank">📅 11:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121720">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گزارش در وال استریت ژورنال: ایران از غول تجارت رمزارز بایننس برای فرار از تحریم‌ها و انتقال میلیاردها دلار برای تامین مالی ارتش خود در طول سال‌ها استفاده کرده است - از جمله انتقال رمزارز که این ماه انجام شده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121720" target="_blank">📅 11:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121719">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: وزارت دادگستری آمریکا تحقیقات خود را درباره استفاده ایران از صرافی بایننس برای  دور زدن تحریم‌ها آغاز کرده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121719" target="_blank">📅 11:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121718">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بلومبرگ: پوتین می‌خواهد جنگ اوکراین را تا پایان امسال به پایان برساند، اما فقط با شرایطی که روسیه بتواند آن‌ها را به عنوان پیروزی معرفی کند.
🔴
این شرایط شامل کنترل کامل منطقه دونباس و تضمین‌های امنیتی گسترده‌تر از اروپا است که به طور موثر کسب‌های ارضی روسیه در اوکراین را به رسمیت می‌شناسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/121718" target="_blank">📅 11:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121717">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68a8a3dcb3.mp4?token=q2jZeAQjS1oVhX9O4eCMwVCb_9gPgP_iYiEj3lR1c4YA47VKDhFwAuSGG7mE43YQ87WNckYOBaoYD4aBkQ2tY44FdgXmuxke-pRLsA0GzeG-7TCLjY6ZrkMbBwlm9i8bftRbEJ3Yt-bbvEBKcds6ajKJjqCEC_rHY_4oDma0_TfFhzvTZve8T8PKjT5KRwHzCjZ7PPL5EmyQHBFC_uIu5JF1sSNVVx_Nl83OR55pbrSG6DLYCkzC5IHJNEnSJvVU3eHeYHvm-CmuY5_eF0r8lTo6jDZYhKhz7w36sw8OG5xzh0TKmJ-TzgZktd4W2RIpMTlWu5SdkIVcbv9-l87InA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68a8a3dcb3.mp4?token=q2jZeAQjS1oVhX9O4eCMwVCb_9gPgP_iYiEj3lR1c4YA47VKDhFwAuSGG7mE43YQ87WNckYOBaoYD4aBkQ2tY44FdgXmuxke-pRLsA0GzeG-7TCLjY6ZrkMbBwlm9i8bftRbEJ3Yt-bbvEBKcds6ajKJjqCEC_rHY_4oDma0_TfFhzvTZve8T8PKjT5KRwHzCjZ7PPL5EmyQHBFC_uIu5JF1sSNVVx_Nl83OR55pbrSG6DLYCkzC5IHJNEnSJvVU3eHeYHvm-CmuY5_eF0r8lTo6jDZYhKhz7w36sw8OG5xzh0TKmJ-TzgZktd4W2RIpMTlWu5SdkIVcbv9-l87InA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: تفاوت ما با چین و روسیه این است که یک نفر همه تصمیم‌ها را نمیگیرد
🔴
مارک روته، دبیرکل ناتو، اعلام کرد: «ناتو یک ائتلاف سیاسی و نظامی است. تفاوت بزرگ ما با چین یا روسیه این است که در آن کشورها در نهایت یک نفر همه تصمیم‌ها را میگیرد.»
🔴
او افزود: «ما یک ائتلاف دموکراتیک و نظامی هستیم و به همین دلیل تصمیم‌ها همیشه بر اساس ملاحظات سیاسی و نظامی گرفته میشوند. ساختار ناتو این‌گونه عمل میکند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121717" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121716">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9d60253b.mp4?token=dzfvwL7EoYAeITMvZUG_jY-EXi_2TFd5w_hgca2oIE4VsVFCYiXmA92a45vdd-2RYHcPL0kPw6Lb5jIAXETAYtuAY6OEu5PkCilVch-8xZB0r8ztQv1BRLxzNlPd0uxa4RB1X1gWCOE_QJfGYlGGNmKurcckDYEmqmG-C189UBiM6fqF_tKZQhLy2Hm4PTkKkXoICHMP2XBLODAOfIHBZG7NzLC4_mwGc1vwDvMyTUOYZY3jTWXxW0lhTrCh1XzFlIsTEHnlLnQvx2g6LJ-rKx079ZGXaVmSa96HnKe6J8-5KapSX6LfD0nSK_Imz_oSQd9KKlGDSf5oTHqgorfDxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9d60253b.mp4?token=dzfvwL7EoYAeITMvZUG_jY-EXi_2TFd5w_hgca2oIE4VsVFCYiXmA92a45vdd-2RYHcPL0kPw6Lb5jIAXETAYtuAY6OEu5PkCilVch-8xZB0r8ztQv1BRLxzNlPd0uxa4RB1X1gWCOE_QJfGYlGGNmKurcckDYEmqmG-C189UBiM6fqF_tKZQhLy2Hm4PTkKkXoICHMP2XBLODAOfIHBZG7NzLC4_mwGc1vwDvMyTUOYZY3jTWXxW0lhTrCh1XzFlIsTEHnlLnQvx2g6LJ-rKx079ZGXaVmSa96HnKe6J8-5KapSX6LfD0nSK_Imz_oSQd9KKlGDSf5oTHqgorfDxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دولت ترامپ فروش ۱۴ میلیارد دلاری سلاح به تایوان رو متوقف کرد
🔴
تا مهمات آمریکا برای جنگ ایران رو حفظ کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121716" target="_blank">📅 11:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121715">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmE7UQrr5Ic6J9j_SI5ryrD_YBTdf0PYbUHWupZRbsqzV8ZSsUWJL1Vo1uCmOnXWQyVJHPlk8EoLSDak5MQPYNEAGiF7dU4xDBf8LJz-Y_8lXH1iU71NeWA3RPK6_UWHLqkiaVa1WqaRC1_mETiihFooefw2s34QnMSzOsdDRlJR35WftsCFO5TD73_Sy0kyZEzxujlGDWGTOWu5QErvt7WlvGMPzOdAzelHTFWF0lD1S1QOVD3KT-77csPn6VSkELj6LPC7J3LWJI10Q7-I9HbJOJblRHa7smVl5NekyVNdIo-VLtNl_2BuU6iJe_UZ1DwSaf11Jpm0pIOLOAyhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ناو هواپیمابر آبراهام لینکلن در بالاترین سطح آمادگی عملیاتی قرار دارد
🔴
ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، با انتشار تصاویری از پرواز جنگنده‌های نیروی دریایی آمریکا از ناو هواپیمابر «یواس‌اس آبراهام لینکلن» در دریای عرب اعلام کرد گروه رزمی این ناو در «بالاترین سطح آمادگی عملیاتی» قرار دارد.
طبق بیانیه سنتکام، این ناو همزمان در اجرای محاصره دریایی آمریکا علیه بنادر ایران مشارکت دارد. فرماندهی مرکزی ایالات متحده همچنین اعلام کرده در جریان این محاصره دریایی، ۹۴ کشتی تجاری تغییر مسیر داده‌اند و چهار کشتی دیگر نیز «زمین‌گیر و مجبور به توقف» شده‌اند.
🔴
سنتکام پیشتر ویدیویی از ورود نیروهای آمریکایی به یکی از کشتی‌هایی که قصد عبور از خط محاصره را داشت منتشر کرده بود. واشنگتن میگوید هدف از این فشارها، وادار کردن تهران به توافق برای پایان دادن به جنگ و کاهش تنش است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/121715" target="_blank">📅 11:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121714">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سپاه : خنثی‌سازی مهمات عمل‌نکرده در خرم‌آباد(فردا)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121714" target="_blank">📅 11:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دبیرکل ناتو: تعدادی از کشورهای اروپایی تمایل خود را برای مشارکت در تلاش‌ها جهت بازگشایی تنگه هرمز ابراز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121713" target="_blank">📅 11:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
الجزیره: مقامات دریایی بریتانیا مدعی گزارشی از وقوع حادثه‌ای در ۹۸ مایل دریایی شمال سقطری، یمن شدند
🔴
عملیات تجارت دریایی بریتانیا: کشتی نزدیک شدن یک قایق کوچک با ۵ سرنشین را تأیید کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121712" target="_blank">📅 11:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
الجزیره: مقامات دریایی بریتانیا مدعی گزارشی از وقوع حادثه‌ای در ۹۸ مایل دریایی شمال سقطری، یمن شدند
🔴
عملیات تجارت دریایی بریتانیا: کشتی نزدیک شدن یک قایق کوچک با ۵ سرنشین را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121711" target="_blank">📅 11:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر امور خارجه کانادا: ما به محض دستیابی به آتش‌بس دائمی، در مین‌زدایی و حمایت از آزادی دریانوردی در تنگه هرمز مشارکت خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121710" target="_blank">📅 11:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2joucx_niQLkKox2QlOKn8J4-YrtDn3kRI6XcaPXkDYFKtG8SADT0JSPaZCnxGjNKJbcd1D3utJHQ9PZcebx3NUs--NHY0GrdR1h4lxztk848MYFrLBllGwkF0vMKQA2bETSYFkVAmL7aKiMCFERXXzRVeZVDXxCNHcIRfxn1CYR2L_59mh3AEhpcg0UCiAc1mMVGGn01tnr6myA8q1H-T94sTd91Cq1KLdJf-XGBtkJRb6ISzMTGPTC604Ht2VJPEnuCr2y9awOrF1Um9tMWG1145NYM6Zxc-KQKn7eZyJ50w-HsBd-6TA4_sCq0J6uTWQ74StLVh-3vMLWCnmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: موشک‌ها را برای مذاکره با شیطان بفرستید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121709" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
میدل ایست نیوز نوشت: کشور سوریه در یک جلسه پشت درهای بسته با حضور وزرای دارایی و رؤسای بانک‌های مرکزی کشورهای عضو گروه هفت در پاریس شرکت خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121708" target="_blank">📅 10:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال: وزارت دادگستری آمریکا تحقیقات خود را درباره استفاده ایران از صرافی بایننس برای  دور زدن تحریم‌ها آغاز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121707" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN7jgY6W8vvW2rxB52Wa-GKjeVKdcuwRw7unSJwtswci0FxlngB5H8nj0uN0_JNokHuLrDSP88w6Qjsi5mG9vi_UqAgNYW6VlnC-FC3XsIesnrAYZLFZyphlnq-GHifasRWDwmukRMmRopaOPu0mUrPkji79Fb3JIKVxkzlUxwEUUgh9_QoOBXZqoxFd3J2xvSLGaFojPoFiPBsKpVK7Ya3S0x1CK6elR-A71YluzXwXDTGjU0KsDiPbsw8k4dLDj5XqbKM_SfE1105qvzddCcgHAdHn_u449m5zJI0NB45ROK0PJ0yRmZh4auTXJ8j8T2lBLtopkIkiUDYn71215Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه CNN: ترامپ پس از اینکه در ایران برای تغییر نظام شکست خورد، به دنبال جبران در کوبا است
🔴
ترامپ در کوبا به دنبال چیزی است که در ایران از دستش رفته است. اما هرگونه اقدام ارتش آمریکا تحت فشار کاخ سفید، با خطرات سیاسی و نظامی بالایی همراه خواهد بود.
🔴
اعلام جرم دولت آمریکا علیه رائول کاسترو (رئیس‌جمهور سابق ۹۴ ساله کوبا) یک چرخش قابل‌توجه در رویارویی نزدیک به ۷۰ ساله آمریکا با این جزیره است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121706" target="_blank">📅 10:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
چین از تلاش‌های میانجی‌گرانه ما حمایت می‌کند و در همکاری با ما ابتکاری ۵ ماده‌ای ارائه داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121705" target="_blank">📅 10:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ادعای رویترز به نقل از یک منبع پاکستانی: نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121704" target="_blank">📅 10:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
جروزالم پست: مقامات اطلاعاتی اسرائیل هشدار دادند که ایران ممکن است در حال برنامه‌ریزی برای حمله موشکی و پهپادی غافلگیرکننده علیه اسرائیل و کشورهای خلیج فارس باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121703" target="_blank">📅 10:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121702">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtX7uQfqv-Sfa0bJWznK9rUSsorTgEgx5-KePSoONSULYAmo94Y6GdQO-LWGKTkcob7bi5NYEQTFI72Aqzglv6B4ICnC9g89TEcyg6oXYROPJML1gqiuldkZz3qExC9sganMR1-kF1WwGj9p5xLxgXT3fvfGJ7vBouf9j2YdodajFZmTllKiqS48hFFd_Kwtdk-spzybx11RBKa8FkaPAkYPSBbIiOB7q_TFbssBhOS9TKErrvs0NZI5HtlbJOIkMyCYtwniqH9x1gRRJUM4AtLd36dgQ37I5xsUlfzKzk9ZJp2_ibzytr8AYKK4KSy38lVm9uVPPnJwFRvHF76AYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوجه‌کباب میلیونی شد ....
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121702" target="_blank">📅 10:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121701">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کانال ۱۳ عبری به نقل از مقام آمریکایی: ایرانی‌ها در سرعت بهبودی از حملات، از تمام جدول‌های زمانی پیشی گرفته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/121701" target="_blank">📅 10:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121700">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وزیر خارجه سوئد: ما متعهد به افزایش هزینه‌های دفاعی در ناتو و همچنین حمایت از اوکراین هستیم.
🔴
ما آماده ایم در تضمین آزادی کشتیرانی در تنگه هرمز مشارکت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121700" target="_blank">📅 10:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
منابع عربی: انفجار در ابوظبی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/121699" target="_blank">📅 10:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntUpWUGQLQrumVr4vR65uNIL9PnBl0VzGbQNbV1uUcHlb6adyBr3lMMDT7qEk4TStfN0nxNDCubckA63vKYJGyRJvI5nrplCW5kQnbKCTDGpApbPT_qXogHEdwT74cXAyzSQbONRwUih-sg9zXHIm7nJn33B1IDpDeCPThWLqpjkoum6RhFKHB_zNhbg5qwUfEUjpS7HYi2BWejgezk5DXwj81p2g6cKEbf9BztoNEMjW8HX_P635a0TMBchDVhLwxbnqJKVbMXuxAK1hlwZ_DIGU5iHADITdC_QLgnZjcxI4HP0FJeGtxfQ9DIcmIKy917qNDdJ1l7zCoHRfctTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز نوشت: ایران با ایجاد ایست‌های بازرسی جزیره‌ای، توافق‌های دیپلماتیک و گاهی دریافت «هزینه عبور»، در حال تثبیت کنترل خود بر تنگه هرمز است
🔴
در حالی که کشورها تلاش می‌کنند ذخایر انرژی رو به کاهش خود را که در پی جنگ مختل شده، دوباره تأمین کنند، ایران یک سازوکار چندلایه برای عبور کشتی‌ها از تنگه هرمز اجرا می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/121698" target="_blank">📅 09:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ثبات انس جهانی طلا در محدوده ۴۵۰۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121697" target="_blank">📅 09:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxKu96SVDZjdnUyIK4xkLDgFq8_aOV8W_pPgwWt_fGkWjcJ1xs3BEtph3eilwLk-ZMf-aV7DfwT4BTLKhun-fQInIjRViVxRIfCX8KmWv3VMUdTVIIerfQQsrbDVDmw82aQjkSehd3-AV61SQCOnP-J62hAt8kdUZjQEnxl05a96OmTAOTnXR68YVYnkaEHCe_z0zU03fx4vEKuhPSQWozA5jMy9_LJ7dsFCq8zjlhRVitRQanrhg-lzs2gUoowrYazTDZAVRDnDVdxI58ztFk_TsJ-P8y37jdQhi2fS-OJHrIxgg-i_-Nz44uqiSXo8CnKXNYPT13-pTEoVLFYUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعلام وضعیت اضطراری بین‌المللی در پی شیوع ابولای بوندیبوگیو
🔴
سازمان جهانی بهداشت شیوع ابولای بوندیبوگیو در کنگو و اوگاندا را وضعیت اضطراری بین‌المللی اعلام کرد. این سویه که واکسنی برای آن وجود ندارد، از طریق تماس مستقیم با خون یا مایعات آلوده منتقل می‌شود و نرخ مرگ‌ومیر آن ۳۰ تا ۵۰ درصد گزارش شده است.
🔴
دوره نهفتگی این بیماری ۲ تا ۲۱ روز است که با علائم اولیه تب، سردرد و گلودرد آغاز شده و در مراحل پیشرفته به استفراغ، اسهال، اختلال عملکرد کلیه و کبد و خونریزی‌های داخلی و خارجی منجر می‌شود. در حال حاضر درمان این بیماری تنها محدود به آبرسانی حمایتی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/121696" target="_blank">📅 09:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نظرسنجی نیویورک تایمز: ۹۵ درصد رأی‌دهندگان دموکرات با جنگ آمریکا و اسرائیل علیه ایران مخالف هستند
🔴
سه‌چهارم آنها نیز مخالف کمک به اسرائیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121695" target="_blank">📅 09:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
استولتنبرگ، وزیر دارایی نروژ و دبیرکل پیشین ناتو:   ناتو بدون آمریکا دوام نخواهد آورد، اتحادیه اروپا باید در مسائل امنیت جمعی و تضمین‌های دفاعی جایگزین ناتو شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121694" target="_blank">📅 09:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نخست‌وزیر عراق: دستور بررسی ابعاد حملات به عربستان و امارات صادر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/121693" target="_blank">📅 09:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121692">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بزرگ‌ترین شرکت انرژی آمریکا، اکسون موبیل، در حال مذاکره با دولت ونزوئلا برای بازپس‌گیری حقوق تولید نفت در ونزوئلا است، پس از اینکه تقریباً ۲۰ سال پیش زمانی که هوگو چاوز، رئیس‌جمهور وقت، صنعت نفت ونزوئلا را ملی کرد، از این کشور اخراج شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/121692" target="_blank">📅 09:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
کمیسیون اروپا پیش‌بینی قیمت نفت در سال ۲۰۲۶ را نسبت به تخمین‌های پیشین، ۴۶ درصد افزایش داد.
🔴
کمیسیون اروپا در گزارش «چشم‌انداز اقتصادی بهار ۲۰۲۶» خود تأکید کرده است که شوک انرژی ناشی از جنگ در خاورمیانه و بسته شدن عملی تنگهٔ هرمز، مهم‌ترین عامل این بازنگری صعودی در قیمت‌های نفت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121691" target="_blank">📅 09:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121690">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عربستان سعودی قراردادهای جدید با شرکت‌های مشاوره غربی را متوقف کرده و برخی پرداخت‌ها را به تعویق انداخته است، زیرا این پادشاهی با کسری بودجه فزاینده و تأثیرات اقتصادی جنگ با ایران مواجه است، گزارش فایننشال تایمز.
🔴
این پادشاهی در چارچوب طرح چشم‌انداز ۲۰۳۰ خود، هزینه‌ها را محدود می‌کند و به وزارتخانه‌های سعودی دستور داده شده است که بدون مجوز ویژه از وزارت دارایی، قراردادهای مشاوره جدید را تأیید نکنند، در حالی که برخی پرداخت‌های فاکتور حداقل تا ژوئیه به تعویق افتاده‌اند.
🔴
عربستان سعودی قبلاً پروژه‌های عظیم و پرهزینه‌ای مانند نئوم را کاهش داده یا به تعویق انداخته است، در حالی که نگرانی‌ها درباره هزینه‌های بیش از حد افزایش یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121690" target="_blank">📅 09:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121689">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دیدار مجدد وزیر کشور پاکستان با عراقچی برای بررسی پیشنهادات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121689" target="_blank">📅 09:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فایننشال‌تایمز به نقل از وزیر دارایی فرانسه:  ما نمی‌توانیم ذخایر نفت بیشتری را بدون دانستن اینکه این درگیری چقدر طول خواهد کشید، آزاد کنیم.
🔴
حتی پس از بازگشایی تنگه هرمز، چندین هفته طول خواهد کشید تا منابع نفتی به اروپا و آسیا برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121688" target="_blank">📅 09:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بلومبرگ: ادامه بسته ماندن تنگه هرمز تا ماه اوت، خطر رکود اقتصادی نزدیک به رکود سال ۲۰۰۸ را افزایش می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121687" target="_blank">📅 09:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فاکس نیوز اعلام کرد که جمهوری خواهان در مجلس نمایندگان آمریکا رأی‌گیری درباره قطعنامه اختیارات جنگی رئیس‌جمهور این کشور را به تعویق انداختند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121686" target="_blank">📅 08:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121685">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU2CjU6jnI5WUt_OErBp3aAblK1Go9AtbxLBKYPf1JX_lqqg7QZGQL5m_9zfuLAQXRCywjvJEdlUv8CD4aZ4XsH31R62K1Exb2opqBIPbBKuZrJnPC5_9IUKOFPLq8OS9D6HcRNHz1XldRSGyP-c6XdpMitw9buhomTXudJNUS52WMxzxQOMJ0BtfvmHMFziAi9xHj6V8ieUpBIx69y9KlmMLxzOMWwKyyewt8v0YHw6oLMet-OO82ypKCGETB1hUihVcQ9bW1vwxvte4XsMgrz47cdG96QxBZ9Lv4OKWUI27rWTm9OzuNNKz3lTtDNGoYg1jMQVziXfdL-KE6_REQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کپلر: احتمالا هزینه واردات LNG ژاپن از حدود ۱۰.۷۴ دلار به ازای ۲۸ مترمکعب گاز طبیعی در مارس به حدود ۱۷.۵ دلار در ژوئیه برسد.
🔴
این افزایش تحت تاثیر تاخیر در انتقال و رشد قیمت گاز در آسیا رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121685" target="_blank">📅 08:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121684">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قیمت نفت برنت با افزایش ۲.۳۸ دلاری (۲.۳ درصد) به ۱۰۴.۹۶ دلار در هر بشکه رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121684" target="_blank">📅 08:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121683">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بلومبرگ: ایران حدود یک میلیارد دلار به توان پهپادی واشنگتن خسارت‌ وارد کرده
🔴
ایران از آغاز جنگ بیش از ۲۰ فروند پهپاد MQ-9 Reaper متعلق به نیروهای آمریکایی را منهدم کرده که حدود ۲۰ درصد از موجودی پیش از جنگ پنتاگون را شامل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/121683" target="_blank">📅 08:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سرپرست وزارت نیروی دریایی آمریکا میگوید ایالات متحده ارسال محموله‌های تسلیحاتی به تایوان را به منظور حفظ مهمات مورد نیاز برای جنگ با ایران متوقف کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/121682" target="_blank">📅 08:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عمان، متحد ایالات متحده، پیش از این علناً همکاری با ایران در مورد تنگه هرمز را رد کرده بود، اما اکنون در حال مذاکره در مورد دریافت بخشی از درآمد است. دیروز، ترامپ ایده پرداخت هزینه عبور از تنگه را رد کرد: "ما می‌خواهیم رایگان باشد، عوارض نمی‌خواهیم. این یک آبراه بین‌المللی است."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/121681" target="_blank">📅 08:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
لبنیات از امروز 20% گرون شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/121680" target="_blank">📅 01:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AO2mn9U1ZURPSRU6fEyUBJreOOf7jQtwKhg9IsStcVNj_0U2jI9KToeHk_ok1QOb-OAiDivQ0xkV2ZnZqF1DakRz6RaNc7L7AXiQEfdgXcvb-AZK62ueiD1uLl31ohaGN98ZG8lOFrPYjOnHGokRM1HCzHijaSnJO562robnh_lSsGm7YaHEpmsyTd_yB6iqoO-XH1GWgTi_HhJlo6AQ-PXqPNRAFCGqRaBwP5bOgzC3V9qt6y3yvnNBhZyj-2s4__mWXCwVZ5HzhwJCs_Mw368Ajm-QqtEjVOxxonaTsO0zgmmd5M20qUQ4iMB0q1jj-sx6S4_z0vwao4JGDOzx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بسته چیپس ساده شده 525 هزار تومن!!!
هر دونه چیپسی که میخورین 3 هزار تومن ناقابل.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/alonews/121679" target="_blank">📅 01:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/288e58579d.mp4?token=XJG_C-uks9JwV6XHCHuQ0UFg0VpURnbhenKy9vFz6UbZoBuFwGqS7SRHxfyodrlk3DgumP1fnGmNsiJtvH5YLAXxVNZva_xX4DncWeU9nmRkXzSdx3q5iQzC5BbhM7w-oBZ_SvOxikFNegRoW7ulswOTVjZqmpl6SCa5fpefTv8H1DVdQDR2vCdOji3QGvYXXNYjqwSOG8QcVd702VOX-umctHK_XbB5D0QposbXAmMhsT2AlYCFt9z7Nak_RjOhg78wqP16zINPctZXyozOJfu6Q41iT0YYVjrOF-9INeGFUJJ4wbT28WQU84z2IhxBGB1CCDVdqJ09yklDpUZSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/288e58579d.mp4?token=XJG_C-uks9JwV6XHCHuQ0UFg0VpURnbhenKy9vFz6UbZoBuFwGqS7SRHxfyodrlk3DgumP1fnGmNsiJtvH5YLAXxVNZva_xX4DncWeU9nmRkXzSdx3q5iQzC5BbhM7w-oBZ_SvOxikFNegRoW7ulswOTVjZqmpl6SCa5fpefTv8H1DVdQDR2vCdOji3QGvYXXNYjqwSOG8QcVd702VOX-umctHK_XbB5D0QposbXAmMhsT2AlYCFt9z7Nak_RjOhg78wqP16zINPctZXyozOJfu6Q41iT0YYVjrOF-9INeGFUJJ4wbT28WQU84z2IhxBGB1CCDVdqJ09yklDpUZSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرمله در صدا و سیما: دلم واستون میسوزه ولی دوستون دارم، اما این‌بار بزارین فراخوان بدن ببینیم کت تن کیه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/alonews/121678" target="_blank">📅 01:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGkotWEIlxR-vy-c5zTOZtDzyp8OdKyRZEADGcIbunsT_FHefXEc9VdJA8SS-OhXDyTHyFQZdoSceg1sziujvgtqrCMPlDLQ4UZbsegeOqxQhh4TCFMUwGd3YQouz_xzjZkmY_n06_VInoIW9b-9kXwierkA7-iKwEkmzregU2VJ3Hb4PBE7HUSkx-3we_mqloGCAcUnQd67o5BswJKIEphoqjYft4EqDJoIe_gPS5946NfoPYQW3wuU6WGpqZDwBGFBo0oQCy2-YSiQ2MG2HkdBBIsqA7ZJOxZqcy8j8tH7_ucG3jFBxbKcA3hyKX9erJoSF6zONrqKAc0olk-AxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱ خرداد تولد ترامپ هست
🔴
بفرست برا خردادی‌های مودی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/121677" target="_blank">📅 01:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای انفجارهای مهیب در دیرالزور سوریه خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/alonews/121676" target="_blank">📅 01:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ایسنا: منابع پاکستانی به برخی رسانه های مستقر در اسلام آباد اعلام کردند در صورت به نتیجه رسیدن گفت وگوهای وزیر کشور در تهران، فیلد مارشال عاصم منیر فرمانده ارتش این کشور به تهران سفر خواهد کرد اما
آخرین خبرها تا پنجشنبه شب حاکی از آن است که رایزنی ها بر سر معدود اختلافات هنوز نهایی نشده است.
🔴
منابع پاکستانی اعلام کردند
سفر فرمانده ارتش پاکستان در صورت نهایی شدن چارچوب مورد نظر میان دو طرف انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/121675" target="_blank">📅 00:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e48e83426.mp4?token=UNFw2Vt7zcgKRYglyYRFSjGZdk2nHenhDtOwW3Z8F_yO3nQpTeMmV2PhbZlfcvGRXOw-KViFGMnrITn_b_kKiew5kg4QMWXXBlOMrJftDRVa69OdNOY4AQWoN0Vg44Vf3t2SKwMuREybV28wSh9_wb2dUuydM7Z8SFeloC7u6mVxlAd3amL6-0tQ69547BkIa6ZEok8nvJP5ht7T8G2byz6qguauEfw6K0sbjlKKRPAMGlBThZS7bIlte5B1Iq0nbMVxoYjheC-aUDMcDqNab1DCKr0pjYTcIJJp1IDsHKj246uu4HmvLkEBiNGi2usEfnI_6SbLlvs9cGjoaVM9Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e48e83426.mp4?token=UNFw2Vt7zcgKRYglyYRFSjGZdk2nHenhDtOwW3Z8F_yO3nQpTeMmV2PhbZlfcvGRXOw-KViFGMnrITn_b_kKiew5kg4QMWXXBlOMrJftDRVa69OdNOY4AQWoN0Vg44Vf3t2SKwMuREybV28wSh9_wb2dUuydM7Z8SFeloC7u6mVxlAd3amL6-0tQ69547BkIa6ZEok8nvJP5ht7T8G2byz6qguauEfw6K0sbjlKKRPAMGlBThZS7bIlte5B1Iq0nbMVxoYjheC-aUDMcDqNab1DCKr0pjYTcIJJp1IDsHKj246uu4HmvLkEBiNGi2usEfnI_6SbLlvs9cGjoaVM9Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوتی بزرگ در صدا و سیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/121674" target="_blank">📅 00:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf33652fc9.mp4?token=QbIYR2znkqKn9sfcJ0DgUsY30qd9Af-kjNHcLTgEj7_cYYHdbx0N9ARKvxsIq8ra0_tBY3UjQnhXoU_8WP39XgWuFaCiE3hQr7sOVuAMLHQh8_1mu4LWAUCr_Wa6X1qYJHsFaV_TTvjShnUZper4ABs7Z3toawz6bJ-OSnD9PJUwPAU2OEk6XB3V7cvHPVZgd_iTLpsB69k7RTf-xuJ6aAztEC7KK2-sZxydViOw_BSgDzXV3CP9PJKdb28ju7VZ2Wods3U-P-08vOMBRil2we2I8qvp_-BktkWNgsOwFzxeZu4hMfD_qoYrPmCWS8JEZJnyVxfTWrkQA3i00AQ1aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf33652fc9.mp4?token=QbIYR2znkqKn9sfcJ0DgUsY30qd9Af-kjNHcLTgEj7_cYYHdbx0N9ARKvxsIq8ra0_tBY3UjQnhXoU_8WP39XgWuFaCiE3hQr7sOVuAMLHQh8_1mu4LWAUCr_Wa6X1qYJHsFaV_TTvjShnUZper4ABs7Z3toawz6bJ-OSnD9PJUwPAU2OEk6XB3V7cvHPVZgd_iTLpsB69k7RTf-xuJ6aAztEC7KK2-sZxydViOw_BSgDzXV3CP9PJKdb28ju7VZ2Wods3U-P-08vOMBRil2we2I8qvp_-BktkWNgsOwFzxeZu4hMfD_qoYrPmCWS8JEZJnyVxfTWrkQA3i00AQ1aTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه ماریا زاخاروا: زلنسکی به احتمال اقدام اجباری علیه ترانس‌نیستریا اشاره کرده است.
🔴
او به کل جهان تهدید می‌کند، نه تنها ساکنان ترانس‌نیستریا بلکه فضای اوراسیا را نیز. او فکر می‌کند که شیطان را از شاخ‌ها گرفته و محکم نگه داشته است.
🔴
او قصد دارد با ترانس‌نیستریا برخورد کند — هرگونه تجاوز به هموطنان ما در ترانس‌نیستریا بلافاصله و به طور مناسب پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/121673" target="_blank">📅 00:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121672">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964a3a806a.mp4?token=FNG6n1YsElJhQdpF89OxMO2EGXgn44aU_Vjaer59lSoo5SKzsd0H5m6gV7YG-_PL8g6y-qk-VzeBgLUD_Ta2_d-tN23xYfNjE3fWToXwNcKBW_-j0N9-prCIg8pSsQmo6c1TC-g_Pwuoz45u1w7O799vA6estleBlwa4qhdgeRae8xWvn0XFBMoTt4Je3BgXWlZBXWapKkWbi6IS8TcSm37ou6stKBPVR15Fz-ZKc4KDQQKs_M5nDdGLUWtbx0-PKssjL8zZKEXhy9GG-iozu-TX7i6ThuBWSV-HuxjnsunDcN5K311DR-6rUaGwv2f50xFVP6nxzy0Ibfi7ycjq5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964a3a806a.mp4?token=FNG6n1YsElJhQdpF89OxMO2EGXgn44aU_Vjaer59lSoo5SKzsd0H5m6gV7YG-_PL8g6y-qk-VzeBgLUD_Ta2_d-tN23xYfNjE3fWToXwNcKBW_-j0N9-prCIg8pSsQmo6c1TC-g_Pwuoz45u1w7O799vA6estleBlwa4qhdgeRae8xWvn0XFBMoTt4Je3BgXWlZBXWapKkWbi6IS8TcSm37ou6stKBPVR15Fz-ZKc4KDQQKs_M5nDdGLUWtbx0-PKssjL8zZKEXhy9GG-iozu-TX7i6ThuBWSV-HuxjnsunDcN5K311DR-6rUaGwv2f50xFVP6nxzy0Ibfi7ycjq5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس دفتر کاخ سفید در امور سیاست، استیون میلر: تقسیم سیاسی اصلی در آمریکا امروز بین دیدگاهی از آمریکا به عنوان یک کشور جهان اول و دیدگاهی از آمریکا به عنوان یک کشور جهان سوم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/121672" target="_blank">📅 00:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d5f964b2.mp4?token=YmYbkPLBj5pQMLe_AhdZmKvsHjOkGL-9UdpN0GKVcGBTxOUU5W63de6T4Z9oa0o-jakGi2j1v2qiqsB7jpa-_asG62SZyLjF3TU190sBJVJSgaqHj4TGVBjB8LfIr6DHubUp1huYG7o5s1gU-BfyHul2sP7pTXz6v6aY1tqs37qFG9v1oNCkFWmfGU89y953U5ObAIhOxmcb3mEMxN4CdaW9L8RmoMAVSjW4b98Vu3WEeV29c0UiTXUiH7aMeZmW3aj1Yjmt9hTQkWbot9NgibRKu8uDm4bGWf8XTySUwKGOooSDKrA3hvPdpVq4LnBpoGk1ORbdG1cg_u068lmMeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d5f964b2.mp4?token=YmYbkPLBj5pQMLe_AhdZmKvsHjOkGL-9UdpN0GKVcGBTxOUU5W63de6T4Z9oa0o-jakGi2j1v2qiqsB7jpa-_asG62SZyLjF3TU190sBJVJSgaqHj4TGVBjB8LfIr6DHubUp1huYG7o5s1gU-BfyHul2sP7pTXz6v6aY1tqs37qFG9v1oNCkFWmfGU89y953U5ObAIhOxmcb3mEMxN4CdaW9L8RmoMAVSjW4b98Vu3WEeV29c0UiTXUiH7aMeZmW3aj1Yjmt9hTQkWbot9NgibRKu8uDm4bGWf8XTySUwKGOooSDKrA3hvPdpVq4LnBpoGk1ORbdG1cg_u068lmMeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مخبر : اروپایی‌ها چپو راست برای عبور از تنگه هرمز به ما پیام میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/121671" target="_blank">📅 00:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آسوشیتدپرس: احمد وحیدی، فرمانده سپاه پاسداران، به یکی از چهره‌های اصلی در مذاکرات تبدیل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/121670" target="_blank">📅 00:32 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
