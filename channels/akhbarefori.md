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
<img src="https://cdn4.telesco.pe/file/hEaXEPqc5wZqFPvjE-PWQZLCCoG971HU_uIZWBgIUvSaPQjXfSfxd5voGELwPsmwWUBUcD2_qNDlDUMA_BVxF1d4_DapZzp3o4OHNIKClJlyO2oAa-lrDaEnQxxs6KP7mBd6_n6zsdadpu0RqxfdjlO1IbwABunwyIkzEw57FQu0F2s2-6gc3wTOMT0YF6MvT-H3kQUifopxsWE3qli7sjwn3-49C89Y1sxyBnbIY4qBcXW0yjOZUM6FSD3wmxIYsYmMwWdRaUhcA59ERwoyO2ArOAegUNk0O-oJ9JUSwA07KNuvdjDbaY2sEiyaGBC6shcGJ1m_eZ_EdSwHMTDKXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.11M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 23:44:28</div>
<hr>

<div class="tg-post" id="msg-677111">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9cudVq80xD-OzwZYhxZMXmaVyKYa7dAwOzBOEhRExr6UkS7cPuel74DuLs1jlZAVcVrZlsPiA65V6ypAaF12dcHXxDFZU_FtOPJ9PJMfwce3wYbgI9Rm4FwBPlle0SKu6nl7u9-uviVpatQ4vrtWtpaJLDqATPRHW3qK7h5d13hFFU5qC8lbxcOMKEY5_6p1FPcrQjLTqpvbV2LfbMMBFh_Px7XZsBZ7VsW0BsZHJWcIJtq89NY7IQJLWxtJFdZl6kIur7kdMFZIzKrZzqgA9TT1CQucRggENyp4aDR9lvqXgENFSTnlJ8n5BpPbHhO9DNlb7qH5KX_I9uDXzt7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
۱۰۰۱ سفر کربلا
✨
▫️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/677111" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677110">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acBll130bGO2lazDFo7CB4fKy7_Ex0VrwH_WZxjkvyuuLa3y6k2G6sl7c7HAU_xQkTJocNEikRCjuZlMdv0nnPBfBJO1maaSVjNj9b74_rm2ahRJGiAyaQ94jo0fJVuC2HM6AoBCZcV_7XtX-K3UxTYFO9f8DlHYcP--nPRMezgaWfXb0Sx55wqVC6lPtYCWakY0YvtfVN3-Dsi82AKzCg836MO6TTqekssyauIUT6Lf8UXlLG5itf07H_aFU_czniPaTM5w9dkMpCSbtPlr8ixFk-RQ7kgd7sQjzsbADLxLee2_FFN6LAjUmRGVAH0on1IwXejnOH7weqXHwW_H5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک پست: سنتکام طرح بمباران دو هفته‌ای ایران را آماده کرد
🔹
طرح شامل یک بمباران مداوم دو هفته‌ای است، نه حملات شبانه محدود که در دور قبلی درگیری‌ها دیده می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/677110" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677109">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/akhbarefori/677109" target="_blank">📅 23:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677108">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنوب کشور در جنگ ۵.۵ همت خسارت دید
هادی هاشم‌نیا، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
۲۰۰ قایق شخصی و ۵۰ لنج بر اثر حملات دشمن در جنوب نابود شده‌اند، چندین اسکله در سیریک و بندرعباس آسیب کلی و نسبی دیده‌اند و به‌ صورت کلی ۵.۵ همت خسارت وارد شده‌ است. خسارت‌ها بر اثر جنگ باید اولویت‌بندی شود و بین نهادهای متولی تقسیم شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/677108" target="_blank">📅 23:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677107">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آمریکا واردات از ۴۳ شرکت چینی را ممنوع کرد
وزارت امنیت داخلی آمریکا:
🔹
«وزارت امنیت داخلی، از طرف کارگروه اجرای قوانین کار اجباری، افزودن ۴۳ شرکت به فهرست نهادهای مشمول قانون پیشگیری از کار اجباری و همچنین به‌روزرسانی فنی اطلاعات دو نهاد موجود را اعلام می‌کند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/677107" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677106">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ساعت فعالیت دستگاه‌های اجرایی استان قم و ایلام روز شنبه ۱۰ مرداد ۱۴۰۵ از ساعت ۷ تا ۱۳ خواهد بود.
🔹
معاون ستاد ملی جمعیت: تا چند دهه دیگر، متوسط سن مردم ایران ۴۰ سال خواهد شد.
🔹
حزب‌الله: دولت لبنان باید کاری کند، وگرنه صبرمان لبریز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/677106" target="_blank">📅 23:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677105">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df730cd0b5.mp4?token=uuayB0sKJJwKMJbc1KaWpIE5Ec-SPyJawNecPOriHrJOd98HSl0nYWToN_ndVTNZ2SVKOqkMnw6ULCLx-Kt2VJDB2SGfeNe_qdYPOTRK2wYZBTIOUfxHdybd-izPhw3xdnV6fymteBscvGHi2sB6PYmJIyC80nksOC3DVYqd6-gd269fkf9D65-Wzx_ei9fPQn_dls5D7_2IALdqI749EZ7vg-WVimtcDtlv_yS8BlBMbk_blaoDl6ULhkmWMb8Qe3tQQc4jGp0z4B6hsFbeeJ-eTwpRVggCZ-uphdujEEv9Tw3cOHZ6dftZCWbxzt3SJCeqd3lfty6ar3pi784dWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df730cd0b5.mp4?token=uuayB0sKJJwKMJbc1KaWpIE5Ec-SPyJawNecPOriHrJOd98HSl0nYWToN_ndVTNZ2SVKOqkMnw6ULCLx-Kt2VJDB2SGfeNe_qdYPOTRK2wYZBTIOUfxHdybd-izPhw3xdnV6fymteBscvGHi2sB6PYmJIyC80nksOC3DVYqd6-gd269fkf9D65-Wzx_ei9fPQn_dls5D7_2IALdqI749EZ7vg-WVimtcDtlv_yS8BlBMbk_blaoDl6ULhkmWMb8Qe3tQQc4jGp0z4B6hsFbeeJ-eTwpRVggCZ-uphdujEEv9Tw3cOHZ6dftZCWbxzt3SJCeqd3lfty6ar3pi784dWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدا راه شکست را به سوی امتی که در برابر ظلم ایستادگی کردن، بسته است... #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/677105" target="_blank">📅 23:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677104">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سخنگوی فرمانده کل نیروهای مسلح عراق اعلام کرد که نخست‌وزیر و فرمانده کل نیروهای مسلح دستور افزایش سطح آماده‌باش در پادگان‌ها و پایگاه‌های نظامی را صادر کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677104" target="_blank">📅 23:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677103">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
الجزیره: قراردادهای آتی نفت خام برنت ۱.۲۲ درصد افزایش یافت و در زمان تسویه به ۹۰.۱۲ دلار در هر بشکه رسید./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677103" target="_blank">📅 23:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677102">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nky-uNatfgk3TvS4XJFzBciCdGuna9OCOeqptKTWXaeJERwd9-mn0V3nQxP4Wmxa3idu6L1jMHvtrjZj2HUrTaw1OfOWtOLuHRunVsJQlJSi0Q4_BQbc8ztqDnpfxOSUzcWE6cVnWCuuVElfuBMajQ_FICwDia3X7neyB1i21ekUlmEl8VqFdVSDJtuQutBpOd-Keh7c_hCCHfdsMQt_lFCWdxL6Q_VNup2giHom0ui5hUUYV09Um6fyS2IP3cUIhFKA9jYEeBPyCO5dxx3cKm_3MAqmv1FkjFF0TLd-rTeDqt3SNKstk0AN3ZkuS6LqcXokWSdBwE_pyyHu66GP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاوشگر کنجکاو ناسا دریاچه‌ای عجیب از الگوهای کندویی‌شکل در مریخ پیدا کرد
🔹
مریخ‌نورد ناسا در دهانه گیل، تصاویری از دشتی با الگوهای چندضلعی ۴ تا ۸ سانتی‌متری ثبت کرده که می‌توانند نشانه‌ای از وجود آب در مریخ باشند.
🔹
این ترک‌ها احتمالاً بر اثر انقباض و انبساط گِل ناشی از تغییرات دما یا خروج آب از رسوبات ایجاد شده‌اند. کنجکاوی پیش‌تر مولکول‌های ارگانیکی در خاک مریخ یافته بود که نشان‌دهنده شرایط مناسب برای حیات در گذشته این سیاره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677102" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677101">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHm14TI0KCCULVr5Lkv2lxuSzUP-wdqEICT_sSmbF6o9FHcnhSahVhDATus31uDR0CLCPCivLAXvqrftxeBTF202aJR8UsiUDFyj_HnSMyMQFe-z0Qop24ClWn6uWAmBBAMDLkIoLWHa6-rroUmJC9YuhsZypuHPJ-zss_oT12jom7jQQjlwWX-YbRVFYBbkZLu7KDvcCvgWzN9OqVIoqmbObh8-KdDinysYpURggX3datt-NcmLhMmZ1vO1nA5ju6ZYWc24tnE_qt67Ru8KJcmVtEMGWP8ukEnafEphCwKyBUvxwfkwHi7v_xo-wANJcYHKVKQSCuFdiyAnKHxmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
در راهِ حسین(ع)، بعضی‌ها فقط عبور نمی‌کنند؛ می‌مانند و خادمی می‌کنند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/677101" target="_blank">📅 23:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677100">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
فوربس: آذربایجان همزمان با جنگ ایران پدافند هوایی خود را تقویت کرد
ادعای فوربس:
🔹
آذربایجان در سایه جنگ ایران، پدافند هوایی خود را به طور قابل توجهی تقویت کرد. باکو اخیراً با خرید سیستم‌های زمینی دوربرد اضافی و جت‌های جنگنده نسل ۴.۵ که می‌توانند با طیف وسیعی از تهدیدات هوایی مقابله کنند، دفاع هوایی قابل توجه و متنوع خود را به طور پیوسته تقویت کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/677100" target="_blank">📅 23:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677099">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmRX2BdGDnzp5mahhovOvCvNqnxd94Ox2VFuJbSBArbhKaSLdH4JoIXcl555lWOAcfnrzlE84uU5gmUFdlPtMkX4PmBq44qGSeEqAJPvZUPh4KNG6MC5lBbq_yN-AslIgIQG0zzR9azdDyVQ174jaP5XCyudFOCI29hWjVDsw5y0Z8ICSPuEz3Xe0dHr67vfujzsZlsw8NjElBFfKL9BC0jxp1Oo-BInn1SuohPP9Rdu7AQp1EIhikb1ltsZk98ltVugCh6zibPvK4WQflvs_6szWPMyt33tRbd7p9XwnvVJvqZFW22eZ66WF3mijKs72uNo3AkU5BMtVGXQCwp_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری دانشگاه و صنعت؛ چرا ایران در رتبه ۱۱۷ جهان قرار دارد؟
🔹
بر اساس آمار، ایران با امتیاز ۱۷ از ۱۰۰ در شاخص همکاری دانشگاه‌ها و صنعت در تحقیق و توسعه (R&D)، رتبه ۱۱۷ جهان را کسب کرده است.
🔹
این شاخص نشان می‌دهد دانشگاه‌ها و شرکت‌ها تا چه اندازه در انجام پژوهش، توسعه فناوری و تبدیل ایده به محصول با یکدیگر همکاری می‌کنند.
🔹
کشورهایی که در این شاخص عملکرد بهتری دارند، معمولاً چند ویژگی مشترک دارند:
سرمایه‌گذاری گسترده در تحقیق و توسعه، ارتباط نزدیک دانشگاه با نیازهای صنعت، حضور شرکت‌های دانش‌بنیان، حمایت از تجاری‌سازی پژوهش‌ها و مشوق‌های مؤثر برای نوآوری.
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/677099" target="_blank">📅 22:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677098">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKwk6HJ3apdYZSG7tDOoM6vvgkMZllZ3s09tNSlX_TJpbHdf3HxJrYKZt78_DPXQaumDD8e7tL3ak6XfqmZy2_Q6xpkuxh-fzQ2jWairJZVyNkOS01R0YsbwAZTJzvkFYe5wejQ91bGHGIGzMCjZL8T7UCNrNkW7F88XH5OrIl4WRcfQClOQ_Vj6LmunFgil3pCmXYeHdB7YNRRoC4ocmPYRM_53nRF7mDihA2NvQOTsxvRQ1WsL8P0b6u7cFnPvBUmKvBITvQxGMSj_sAIj1rvQpiRR6ymsU5hjYua9FPeKMmvZaAvN8BTTduwKOhuzhydwLv7t58lQPSVm9YXqcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنفدراسیون فوتبال آسیا هم علیه فیفا شد
🔹
«ای‌اف‌سی» در محکومیت طرح پیشنهادی فیفا برای سرمایه‌گذاری خصوصی، به یوفا و کونکاکاف پیوست واعلام کرد نگران است که این طرح به نقطه‌ای رسیده باشد که «تحریم جام جهانی وارد گفتمان عمومی شده باشد».
🔹
با استعفای کارلوس کوردیرو، مشاور ارشد فیفا، ضربه‌ای مخرب به رئیس فیفا وارد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/677098" target="_blank">📅 22:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677097">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7264884e.mp4?token=feGEnwM94di3qTmf5qKRTK3nM1LBhhU7qXFR43TfUY-1NgUcWTZpib-kCW_mwMK8_2xqbwLavOvBHfTRnSbDP7shzj9XI2i8hJoBn6UIw4SjvLqVYQe11SZdAATm1ChBSqpe_k42HjnsTbaeagNLMOBzRYCHaMFsZRGCMnd9JpGTwedVTdVU5i53f-T79iNoK9gmmuX0bIx7TzM5tgIEDOPQm0VbGek7Xps53zYLaPc0aWLfagBIJ_23Tg36YQEkhQnf60OEX5fnCFrEoKRR0d4ObvzWCwu2BddcopFo3zKDfog-6jaer1Xu6Yr631i-smv01RuemJp7KIv4r6p9lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7264884e.mp4?token=feGEnwM94di3qTmf5qKRTK3nM1LBhhU7qXFR43TfUY-1NgUcWTZpib-kCW_mwMK8_2xqbwLavOvBHfTRnSbDP7shzj9XI2i8hJoBn6UIw4SjvLqVYQe11SZdAATm1ChBSqpe_k42HjnsTbaeagNLMOBzRYCHaMFsZRGCMnd9JpGTwedVTdVU5i53f-T79iNoK9gmmuX0bIx7TzM5tgIEDOPQm0VbGek7Xps53zYLaPc0aWLfagBIJ_23Tg36YQEkhQnf60OEX5fnCFrEoKRR0d4ObvzWCwu2BddcopFo3zKDfog-6jaer1Xu6Yr631i-smv01RuemJp7KIv4r6p9lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه آتش سوزی جنگلی در فرانسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/677097" target="_blank">📅 22:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677096">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581477b92b.mp4?token=BQLthWv4GyLY90PBWWNvyQYu8t0wsTLsZCYSvIETZerOU-C0-sgSLcluRoLHRVZP4j-DB04yye9bwLpV6uRvEgOFaeL1RxVFQj7LsvXcCZZ50627D0o5cfwo9wCNr6i5dU8nCLcrjM-Yr2qa3pLOSB5Q2lihTvPWY318xvAbJXLw2dt1SldNrmvlFwyZck0bBbjkIbs1hDEMbmx0YpiAWu2_0iYnWleesvipsgfLo_A8-Fpo7c9k00saTbEJ-W_knqNsk5Fepa4LZvU7MOq-yekePN6OkYNn-INNXWkuGzD1qW9oW1WLZHPp0N6wklF7tuRLvXXHzNH5PI78MPTIsp2qDuvR2Nrghts-ucmyWcB-kuhOf3U2lem-7QoPuQR3cuUIW1mYJijb8cR6V3do3kDD_UkKKhEiQH0CwSFP3wjNIGMwB0rgKaJz6mxAv72Yf1n3d0RIGxwSrfS9C4c6agGxA2TfnNvVe1AjxBvaT04wmfmZ-XTRtucPFIlQJaEsiEJKK_5gu-De5H4sVLSBzp3DMa1WG09wmz8S2qUywPSDSynGqJsQpdBvyWplWevJK1uy5QPHJ9lNC2tM9o0R1vrlq-OIvAsGnNgXxRf7Uy4LPi0UKWdp6aaWaoFFppFkmwuUrMCC-wzb_mA62d9HFtjsRlMwB673oqCCC2jfBTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581477b92b.mp4?token=BQLthWv4GyLY90PBWWNvyQYu8t0wsTLsZCYSvIETZerOU-C0-sgSLcluRoLHRVZP4j-DB04yye9bwLpV6uRvEgOFaeL1RxVFQj7LsvXcCZZ50627D0o5cfwo9wCNr6i5dU8nCLcrjM-Yr2qa3pLOSB5Q2lihTvPWY318xvAbJXLw2dt1SldNrmvlFwyZck0bBbjkIbs1hDEMbmx0YpiAWu2_0iYnWleesvipsgfLo_A8-Fpo7c9k00saTbEJ-W_knqNsk5Fepa4LZvU7MOq-yekePN6OkYNn-INNXWkuGzD1qW9oW1WLZHPp0N6wklF7tuRLvXXHzNH5PI78MPTIsp2qDuvR2Nrghts-ucmyWcB-kuhOf3U2lem-7QoPuQR3cuUIW1mYJijb8cR6V3do3kDD_UkKKhEiQH0CwSFP3wjNIGMwB0rgKaJz6mxAv72Yf1n3d0RIGxwSrfS9C4c6agGxA2TfnNvVe1AjxBvaT04wmfmZ-XTRtucPFIlQJaEsiEJKK_5gu-De5H4sVLSBzp3DMa1WG09wmz8S2qUywPSDSynGqJsQpdBvyWplWevJK1uy5QPHJ9lNC2tM9o0R1vrlq-OIvAsGnNgXxRf7Uy4LPi0UKWdp6aaWaoFFppFkmwuUrMCC-wzb_mA62d9HFtjsRlMwB673oqCCC2jfBTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اربعین امسال رنگ دیگری دارد؛ به نیابت از رهبر شهید راهی کربلا شدیم، اما داغ این فراق هنوز تازه است/تنها ظهور حضرت ولی‌عصر(عج) می‌تواند مرهم داغ دل شیعیان باشد
/ موکب رسانه‌ای یالثارات الحسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/677096" target="_blank">📅 22:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677095">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
مدیر دفتر الجزیره در تهران: اطلاعاتی به تهران رسیده که اگر گفت‌وگوهای ایران و عمان به گشایش تنگه هرمز بینجامد، واشنگتن محاصره دریایی و تحریم‌های نفتی را لغو خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/677095" target="_blank">📅 22:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677094">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eece875fa5.mp4?token=I-MgxsifSBn_xfP4Rr8r3AYERLOV--f7-uV7tZ7n4Pq8OqOqv_WE_Y6iRpVnfvR2HIb2jFbCZtWaj128OkQJuwWXot2XKmftAjTZTMqK_JOnXCpLJ1X9S40YdGvGdzF5rc0RSjc2O7U__d6K8QFxO_IE52884fz0bCNw70CoN8Dcbl9epCFg50OJhMkdfrJeS8y-ZogwK7xNluQ89pLSMb7L_O0n60eTuhak4Hsv8IyASzeOUnPZHQ4__aBpghgPisyhA6wXucgq3QdplRV2EAYMr15pR06fOMiOupQZCvqh2gLgpCLpPk8nXSaBE4PU-ti6J6f2IuRbHOPmgSzTL6IcAyLz5kc67purqwnpNjXDPBPdGMlCC6ZwPzDe7QTXfupHynB-9m4fUV2tQ99OyJK8aZs52OfWODKzDaEfIKwsGhiOw8SfLuiMJxY1z0I2q5fjrzitBJCWp6IQ6X7v0BB738TSwU1Rlz505lruPTp3TANB-_eKIOCRhYQzIkPiTCFidY4YgqhjBDWp5LcWQD4s6h3KiP9L6HTgcTqWb-pFmNa_XcSgvt00GAmjZdYJcQYMhhcBTwlqQaT8upkQDE0YfvMxDXdBSkEcewyrV9dFyEQc0g4ujiLHSawjD6NROClH_5WWTXWa0ayeuFhLeago3GOL5r3IS6VFZuhF7UU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eece875fa5.mp4?token=I-MgxsifSBn_xfP4Rr8r3AYERLOV--f7-uV7tZ7n4Pq8OqOqv_WE_Y6iRpVnfvR2HIb2jFbCZtWaj128OkQJuwWXot2XKmftAjTZTMqK_JOnXCpLJ1X9S40YdGvGdzF5rc0RSjc2O7U__d6K8QFxO_IE52884fz0bCNw70CoN8Dcbl9epCFg50OJhMkdfrJeS8y-ZogwK7xNluQ89pLSMb7L_O0n60eTuhak4Hsv8IyASzeOUnPZHQ4__aBpghgPisyhA6wXucgq3QdplRV2EAYMr15pR06fOMiOupQZCvqh2gLgpCLpPk8nXSaBE4PU-ti6J6f2IuRbHOPmgSzTL6IcAyLz5kc67purqwnpNjXDPBPdGMlCC6ZwPzDe7QTXfupHynB-9m4fUV2tQ99OyJK8aZs52OfWODKzDaEfIKwsGhiOw8SfLuiMJxY1z0I2q5fjrzitBJCWp6IQ6X7v0BB738TSwU1Rlz505lruPTp3TANB-_eKIOCRhYQzIkPiTCFidY4YgqhjBDWp5LcWQD4s6h3KiP9L6HTgcTqWb-pFmNa_XcSgvt00GAmjZdYJcQYMhhcBTwlqQaT8upkQDE0YfvMxDXdBSkEcewyrV9dFyEQc0g4ujiLHSawjD6NROClH_5WWTXWa0ayeuFhLeago3GOL5r3IS6VFZuhF7UU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظامیان اسپانیا مانع ورود مهاجران مراکشی به سئوتا می‌شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677094" target="_blank">📅 22:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677093">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بنزین ۱۰ هزار تومان شود، تورم چقدر بالا می‌رود؟
یوسف کاووسی، مدیرکل اسبق بازرسی بانک مرکزی در
#گفتگو
با خبرفوری:
🔹
در کنار سیاست‌های بانک مرکزی برای کنترل تورم، در دولت بحث افزایش قیمت بنزین از ۵ هزار تومان به ۱۰ هزار تومان مطرح است که می‌تواند اثر این سیاست‌ها را تضعیف کند.
🔹
برآوردها نشان می‌دهد این افزایش قیمت، حتی با وجود سهمیه‌ها، می‌تواند حدود ۵ واحد درصد به نرخ تورم اضافه کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677093" target="_blank">📅 22:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677092">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e63300c9.mp4?token=LrpulLivNoxA4LbJuMoXtItCCaJyytGmKzCK3dNTlSjGjASwnlDTVB6Gy8lgXJZu3kXBNruydPGpAQ0QkmRAi3JgSoyj0kwwV8GrXupvdQEIPfW4zUwlOLMwPGeXArOCCMlVMEpAyZG8DYe8aNIlWvcUWSpGHvxqQblaCIrnfteOPRkbbkmsGWk3Pgu7Bxpb62JOwwk_EDRtGi84lnVehUrHbXyE-R-6in0hTI51_vZQnkmSRVsVI3gsuCG8x8CF3DTcciuJBhoGCU57MIBmvHf9KPrKxmeydcoy0JkWAl3UOqZZVR03WX5q_uO1cATbfqahOVi1GAa51NYQnKLtlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e63300c9.mp4?token=LrpulLivNoxA4LbJuMoXtItCCaJyytGmKzCK3dNTlSjGjASwnlDTVB6Gy8lgXJZu3kXBNruydPGpAQ0QkmRAi3JgSoyj0kwwV8GrXupvdQEIPfW4zUwlOLMwPGeXArOCCMlVMEpAyZG8DYe8aNIlWvcUWSpGHvxqQblaCIrnfteOPRkbbkmsGWk3Pgu7Bxpb62JOwwk_EDRtGi84lnVehUrHbXyE-R-6in0hTI51_vZQnkmSRVsVI3gsuCG8x8CF3DTcciuJBhoGCU57MIBmvHf9KPrKxmeydcoy0JkWAl3UOqZZVR03WX5q_uO1cATbfqahOVi1GAa51NYQnKLtlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر سقوط اف-۳۵ آمریکایی در سن‌دیگو
🔹
بقایای این جنگندهٔ بیش از ۱۰۰ میلیون دلاری هنوز در آتش می‌سوزد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677092" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmvEMGRzj5UFP91sCOMj7dhtbxtThBmOiQVkk1skPHMxYe6YMpJVE4drufNZY3fwmADwwdNAYE36_hRss_PvL76jna9zDnwLdwMdpxjyfm4peY4QnK8tLUDK3j4CsVjxav8ruBRV1ij0cN3oyW-dmtBM-CrKaUiDnWRe5zPy_5LERyZqUhlEdn_AiYuhGTCFWQUnZ3GJs7e8Uqe9S4avy6Lbz8UYPEGw0EwtRBiei1HKaM4YAyxUTS5XPFHPx2Yb-P1HAe3_gmYfNaOCk9NQgJmKZsw9UP2OV_fd3PL5tR5MiW3db50Cu7s8ClOXaJ9iyRlrWUhs-P2dbxNcVMYW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ستایش سقف‌ها...
🔹
سقف ورودی کاروانسرای شاه‌عباسی؛ جایی که آجر، نور و هندسه در هم می‌آمیزند و شاهکاری ماندگار از معماری ایرانی را روایت می‌کنند.
🔹
حسین کریم زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/677091" target="_blank">📅 22:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677090">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نتانیاهو به‌دنبال عادی‌سازی روابط با عربستان پیش از انتخابات
روزنامه‌ هاآرتص:
🔹
نتانیاهو به چند تن از دستیارانش گفته است که پیش از انتخابات به «یک دستاورد بزرگ دیگر» نیاز دارد و منظور او توافق با ریاض است. نتانیاهو امیدوار است موفقیت حزب لیکود در انتخابات، زمینه‌ساز ادامه نخست‌وزیری او شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/677090" target="_blank">📅 22:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677089">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سنای آمریکا به طرح توقف جنگ علیه ایران رأی منفی داد
🔹
مجلس سنای آمریکا به طرحی که خواستار توقف هرگونه عملیات نظامی علیه ایران در صورت عدم دریافت مجوز از کنگره بود، رأی منفی داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/677089" target="_blank">📅 22:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677088">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNqMkFnxThQDncNCwE392XnYeeapDDY-Q5NsZJaffW2Z5JzIekDlrTyeHukgNU0pJFry2TEWunrsO93QK8wVUSOaG4h_EHuWh4vzJ4aYXUDEeVUeWlH6iC8vkwpMA40idOLnrv3TegXTj2DumSMi06HpiFPWCpeakUTLNlv2K47RGbgeUtGBFL3BnO-ptwfzF1ikPlWunMqx6FePAl9YEo3rGsFLLT8Pdb87ZVg1aelv-oNChjZJmFrg2gQt-6Aj7_KuqWJo9igYG4pHAwlr1CDgBnMeKgL3Gya06sqLLLvwu2fl6a7XSpAHcvB6B9WodXvmykVLlumZ8O8GQVP4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/677088" target="_blank">📅 22:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677086">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW91SAGC9C5ZZ5GueOfqFB2U3COLu4cJ_FE3t666k40Qxn1lGr6dOvhnB3dqQ69gRP0JVagtXSuqgEbFJoNlRjFJD4_7hR8FYI0riwcqrGcjE-2m_R5lVWg1S7LVazguFjCnruNkpEjSgP7s_Suy_aMEV8aSgiHezmCnHe6ecfeCdhZ1UBwCAWFMviHtY9278wRKzMUfLhAMIqfghPnTY1CNEFmGsOmPwKIg0ji-WGLkAPaal2kKLG-OsA2bw19cxynCiu5TeHy0fW2Kv3c7GwN9RFUrngfL3Vn7ZM3m7ncIBh0OQGERMFFrS_w-5rtQ3qFJEm7AJpYt1h7ZSp46sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳
جمهوری‌خواه در جنگ ایران، صف خود را از ترامپ جدا کردند
تایم:
🔹
۳ جمهوری‌خواه در تلاش برای محدود کردن اختیارات جنگی ترامپ علیه ایران، از صف خارج شدند. سنای آمریکا با اختلاف کمی تلاش عمدتاً نمادین برای محدود کردن اختیارات جنگی ترامپ علیه ایران را رد کرد.
🔹
رأی‌گیری ۴۹ به ۵۰ روز پنجشنبه عمدتاً در راستای خطوط حزبی بود. سه سناتور جمهوری‌خواه لیزا مورکوفسکی، رند پال و سوزان کالینز در تلاش برای مهار کمپین نظامی جدید دولت ترامپ از صف خارج شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/677086" target="_blank">📅 22:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677085">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVLwnDQG1nAfgNXo7V7b_wK8o7-G2du-rmA2kr1SWivCFOd68OjkqybVypARQTDHPdB8Z5mi3FVe25gCSjiE9ha7JblOnLQKnbMfS2xkOyTWLnytjo_BhJEnXfmZjZdPvOGIAjm1C_tkQm3gGuTWZowYoELv5bScV8P0VU5QzL0dDujK7vs68HLQm5sYLXeifr5QF5tlGH9TJcSfPeHn5pkbV57OF24-P6qVtqIPPG_s_1qHVJievD9z-SrycrHxtwYyuk6H0TF_sj1bYDwgBpsZeJGcVY0VpnHgNu8wR54Clj-oQMKgxjU6239ltm-wY1pjm6t1MUcaZEPU7ltz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
قبل از قدم گذاشتن در مسیر اربعین، خوب است چند نکته ساده را رعایت کنیم:
▫️
ما فقط زائر این مسیر نیستیم؛ در کنار برادران عراقی‌مان، بخشی از این میزبانی بزرگ هستیم.‌..
▫️
با استفاده از لیوان شخصی زباله پلاستیکی کمتری تولید کنیم
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/677085" target="_blank">📅 22:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677084">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184f60d6b5.mp4?token=rRWMaRu2e1W7U_4wecl1P72brgenx1m9ymNrdSBCx3gKMQMFjRlbJbchqkVoFhTmUwUpqiDBwQoYhqgE8fjpVqRmUiyAE-iqFvbRHghQurKoXcDJLQrOhBGladDJGDvxIsvX-f7fMzAlXTmDFbxZS7qzrwPYGz4_BTsS_9CRzinCKKHm6mOfjW3z_zPm_khDR3_CSMSam1eWOiZCPM8uXSArhW6lonNzbVvCABDfVqHu6aiT7YplUiKjIB2ciCnzAQmIeep9bev7ouFS04LdVXfeMTIAOzAMVAysTVT6FJTxDBQ8krnmHmDTdvW4s40brB71px3AfwjPckhm6EwnrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184f60d6b5.mp4?token=rRWMaRu2e1W7U_4wecl1P72brgenx1m9ymNrdSBCx3gKMQMFjRlbJbchqkVoFhTmUwUpqiDBwQoYhqgE8fjpVqRmUiyAE-iqFvbRHghQurKoXcDJLQrOhBGladDJGDvxIsvX-f7fMzAlXTmDFbxZS7qzrwPYGz4_BTsS_9CRzinCKKHm6mOfjW3z_zPm_khDR3_CSMSam1eWOiZCPM8uXSArhW6lonNzbVvCABDfVqHu6aiT7YplUiKjIB2ciCnzAQmIeep9bev7ouFS04LdVXfeMTIAOzAMVAysTVT6FJTxDBQ8krnmHmDTdvW4s40brB71px3AfwjPckhm6EwnrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش‌های ایرانی که حتما باید بشناسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/677084" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677083">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da87f3ea8a.mp4?token=b0jVHnjXtw3o5-TuEKgRudIDXsVzcecYKUhEUpgX-ONpdA9dgyaOzntTQpM6QvCeV1nm5KafPyCljaKTuunvzqNe9euXfQsa0-wl1ncvryvAHP3VbCaFj15_LX6F2VNQY1OmEYZj4BBtf8q_j2WLQZp2O1v_ExUvzGtNxLlgzke-8-kSw-afZEFxMhleJV79Qt5fDahNjBOZyG3hfItIdbkD5A48hTXSWfOMmeYNIFIYPobb0mHuAVPXLND9jvVGA6Orp0Cyq5vtCGni-QNbojAxx12nvo-FF8e0CJ6HuDByXiRd1ET1zdX5OMMr5Lq6PObVl3Y9vFU-eGhuuVHXHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da87f3ea8a.mp4?token=b0jVHnjXtw3o5-TuEKgRudIDXsVzcecYKUhEUpgX-ONpdA9dgyaOzntTQpM6QvCeV1nm5KafPyCljaKTuunvzqNe9euXfQsa0-wl1ncvryvAHP3VbCaFj15_LX6F2VNQY1OmEYZj4BBtf8q_j2WLQZp2O1v_ExUvzGtNxLlgzke-8-kSw-afZEFxMhleJV79Qt5fDahNjBOZyG3hfItIdbkD5A48hTXSWfOMmeYNIFIYPobb0mHuAVPXLND9jvVGA6Orp0Cyq5vtCGni-QNbojAxx12nvo-FF8e0CJ6HuDByXiRd1ET1zdX5OMMr5Lq6PObVl3Y9vFU-eGhuuVHXHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: یک جنگنده اف-۳۵ صبح روز جمعه در پایگاه هوایی نیروی تفنگداران دریایی در میرامارِ سن دیگو، سقوط کرد
🔹
دود غلیظی حدود ساعت ۱۰ صبح مشاهده گردید و تیم‌های امدادی در محل حادثه حاضر شدند. مقامات در حال بررسی علت این حادثه هستند و هنوز جزئیات…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/677083" target="_blank">📅 21:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677080">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ اشفع لنا فی الجنه</div>
  <div class="tg-doc-extra">محمد حسین پویانفر قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/677080" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
هر جایی گیر افتادم
حسین رو برگردوند از من نه
یا وجیها عندالله
حسین اشفع لنا فی الجنه
🎙
#محمد_حسین_پویانفر
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677080" target="_blank">📅 21:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677079">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd5c59a58.mp4?token=nulFSOiw7uzRB_yPNgQJtZJKv8724Pc_5hyzZv-SeoYkEv5bS7f79Z8qecIwL67Qg9SXjipMvHcSLCZ5IkMXPMB_YFOV5FbOWouKtiJ5yG2nd80Id1ZVJM__qAxggSZnYvEkOfrbY_ZRmFdOQ1sC3AdvSoGyFM538xKgpVdYQKg-eYhEfs3OEeckzhZogW4hpid__-NoUf9tntWK3hcaA-wz2JlB7G8joaiaAAYruQIosxr1PHzp6v0lkI9nQAuCCaW0LXKk6vPOV9zLKWGPR18x5zO4TDUOANB2-xHRxzeLES_lwKcyo5NvtLbVNhbPcm-I-BmL3Ng-HSteEsM7sjioyMvduJ4yms54XmIJDMasWrgSzYgbfBpc_KQot0_WgUSEpIjk9hX_sru9YxcJTdtP6QkhkqGjbqhRd8YApoSlbN9-x7MdMTyzQ6eGNDjCg5nExSXqDEcS2a5LOpoSAXVIqHKI86ggycIwCCb2yaeo6r8D5BAVbArhx4B8mwg_ok-3dSBNEIo0G_vsG8eauAhIaWSat_bs1A1L4eiBD4z2UL3yOMrdzsXV-DIk6vobTOhhbGL2GYffZGRmiFnFTGNyro0GIuPQynRHFpQplt1t44OS1g-2xTWn-jtrp7dW_U-Zm5F_jdlP0lW-WhqhOitKlRFObAwH6fWNOXw9HOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd5c59a58.mp4?token=nulFSOiw7uzRB_yPNgQJtZJKv8724Pc_5hyzZv-SeoYkEv5bS7f79Z8qecIwL67Qg9SXjipMvHcSLCZ5IkMXPMB_YFOV5FbOWouKtiJ5yG2nd80Id1ZVJM__qAxggSZnYvEkOfrbY_ZRmFdOQ1sC3AdvSoGyFM538xKgpVdYQKg-eYhEfs3OEeckzhZogW4hpid__-NoUf9tntWK3hcaA-wz2JlB7G8joaiaAAYruQIosxr1PHzp6v0lkI9nQAuCCaW0LXKk6vPOV9zLKWGPR18x5zO4TDUOANB2-xHRxzeLES_lwKcyo5NvtLbVNhbPcm-I-BmL3Ng-HSteEsM7sjioyMvduJ4yms54XmIJDMasWrgSzYgbfBpc_KQot0_WgUSEpIjk9hX_sru9YxcJTdtP6QkhkqGjbqhRd8YApoSlbN9-x7MdMTyzQ6eGNDjCg5nExSXqDEcS2a5LOpoSAXVIqHKI86ggycIwCCb2yaeo6r8D5BAVbArhx4B8mwg_ok-3dSBNEIo0G_vsG8eauAhIaWSat_bs1A1L4eiBD4z2UL3yOMrdzsXV-DIk6vobTOhhbGL2GYffZGRmiFnFTGNyro0GIuPQynRHFpQplt1t44OS1g-2xTWn-jtrp7dW_U-Zm5F_jdlP0lW-WhqhOitKlRFObAwH6fWNOXw9HOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان ارتش از لحظه‌ای می‌گوید که پایگاه آمریکا را بمباران کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/677079" target="_blank">📅 21:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
منابع رسانه‌ای از وقوع انفجارهایی در داخل یک پایگاه نظامی امریکا در کالیفرنیا خبر دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/677077" target="_blank">📅 21:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2339d551bf.mp4?token=BbX3A06WgFgbRM3aG0GLppko-7hh4y_Dq_pcdgO9RPTd9UfxxWI1sbBPBwbFvnuqhQh0tC_H90qmzRN0U9WLoAuuvsrwba59cqwuxB3pgSSQh-TOLTW2YYOwlultbHDVWDBFs382bTGpNt6-aBOy_kdy8g_6c3QmxtfSO7E-Awr7pMm1OUnUg-QbUSW7L1sS0Y5uTyPpw71mIsq3_87ZXl9AQC7mFsdiaqWFJX2fx6MUlp-5TebrajmbjuF_XnMwuZpBU0t9x9r3UAO1M6LyInlHa6oekhkBc9k9ocwLt2NJOvJMtAkUMylK_eBf6ou2Obtd_cE9QAYfX2Kd6aW3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2339d551bf.mp4?token=BbX3A06WgFgbRM3aG0GLppko-7hh4y_Dq_pcdgO9RPTd9UfxxWI1sbBPBwbFvnuqhQh0tC_H90qmzRN0U9WLoAuuvsrwba59cqwuxB3pgSSQh-TOLTW2YYOwlultbHDVWDBFs382bTGpNt6-aBOy_kdy8g_6c3QmxtfSO7E-Awr7pMm1OUnUg-QbUSW7L1sS0Y5uTyPpw71mIsq3_87ZXl9AQC7mFsdiaqWFJX2fx6MUlp-5TebrajmbjuF_XnMwuZpBU0t9x9r3UAO1M6LyInlHa6oekhkBc9k9ocwLt2NJOvJMtAkUMylK_eBf6ou2Obtd_cE9QAYfX2Kd6aW3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران فقط یک نقشه نیست؛ خانه‌ای است که ریشه‌های‌مان در آن جان گرفته و هویتمان به آن گره خورده است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/677076" target="_blank">📅 21:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
تعیین‌کنندگان «مُد» در ایران چه کسانی‌ هستند؟
🔹
در ایران کارگروهی تحت عنوان ساماندهی مد و لباس وجود دارد که یکی از وظایف آن بررسی پیشنهادهای پوششی است. در این کارگروه که ریاست آن بر عهده معاونت امور هنر وزیر ارشاد است، نمایندگان تام‌الاختیاری از وزارت صمت، آموزش‌وپرورش و سازمان صداوسیما حضور دارند.
🔹
همچنین سه نفر از نمایندگان صنوف طراحان و تولیدکنندگان پارچه و لباس و همچنین یکی از نمایندگان کمیسیون فرهنگی عضو این کارگروه هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/677075" target="_blank">📅 21:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
مرکز اطلاع رسانی فراجا: اتباع خارجی مقیم ایران و متقاضی سفر اربعین، پیش از عزیمت به مرزها، گذرنامه «سند خادم» را در محل سکونت دریافت کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/677074" target="_blank">📅 21:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNpi2WHMJiegNvgma1gzs-jCtuMm0Cnvm3-OeqPrQWRQvEZhsGG97ofnt54MD93sdKt9l386hw6P-nthOg4CWpExjkYAuwyXCYTZ8nmaZuz3yOJh4O4nw0isAp1yubB-bRr-464_N0q0ePoJnXwvoCCxVZ7dACgZa9eirgP_W4XunzRlWJqpmJRlHPeUZCIye__CpuCzsJfS24qVb2eXICMGw9Yrd8I7sVxjZkP0AN4LYlhSOKA-r4B7ao11HS_2K-aE5kl-mfK_vEltr9Q2Y30iVxh5-8d2bXc4jrca_I8zFnw9Y4Tc2BHCwAWbdp_guEqfN73-oE82feNgqlyEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عسل رو با چی بخوریم؟
🍯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/677073" target="_blank">📅 21:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2a99dfbcd.mp4?token=LiQ0NHchRtxzzx0Y_gOmO6LESC8Ll-QFHqqzGxpiL3CdVpDZp-VHG4OFgiCyp8ilhN_rMN4-CuNFJZdPTLqyr7p6jpUsNwSQXvGvdn-uRfFYTgfaw5N5LP0N83J-Zv7GZMZnjD82nLFOwxCz01HGN15ZGGdt7DgR1Qc2bcIDjgkeA_sLJ6bIcY6LH7jWhXqTD6TwkgfeewYvoOCfe6g7jBFvpg7I9yZuXnFyFd6xZdv8Ju3Wwkqu1YPefVaWdtp2hvsZw55GbXYLnOauKQ3gZZLx_gfD5Y2AEan32Kj1LaBbS90Kvl0km8TJku4KRU7Lh1FHj0cbMSjfh1xSKRe5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2a99dfbcd.mp4?token=LiQ0NHchRtxzzx0Y_gOmO6LESC8Ll-QFHqqzGxpiL3CdVpDZp-VHG4OFgiCyp8ilhN_rMN4-CuNFJZdPTLqyr7p6jpUsNwSQXvGvdn-uRfFYTgfaw5N5LP0N83J-Zv7GZMZnjD82nLFOwxCz01HGN15ZGGdt7DgR1Qc2bcIDjgkeA_sLJ6bIcY6LH7jWhXqTD6TwkgfeewYvoOCfe6g7jBFvpg7I9yZuXnFyFd6xZdv8Ju3Wwkqu1YPefVaWdtp2hvsZw55GbXYLnOauKQ3gZZLx_gfD5Y2AEan32Kj1LaBbS90Kvl0km8TJku4KRU7Lh1FHj0cbMSjfh1xSKRe5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع رسانه‌ای از وقوع انفجارهایی در داخل یک پایگاه نظامی امریکا در کالیفرنیا خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/677072" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
خبرگزاری فرانسه به نقل از وزیر خارجه ایتالیا: توافق شنگن با اسپانیا تعلیق شد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677071" target="_blank">📅 21:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
دستور آماده‌باش کامل در تمام پادگان‌ها و مقرهای حشد شعبی
🔹
سخنگوی فرمانده کل نیروهای مسلح عراق از دستور مستقیم نخست‌وزیر که فرماندهی کل نیروهای مسلح را برعهده دارد، برای ارتقای سطح آماده‌باش به حداکثر توان در تمامی پادگان‌ها، پایگاه‌ها و مقرهای رسمی حشد شعبی خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/677070" target="_blank">📅 21:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش ۱۵ درصدی مصرف روغن در کشور
شریفی، دبیر انجمن صنایع روغن نباتی ایران در
#گفتگو
با خبرفوری:
🔹
مجموع مطالبات ارزی واردکنندگان کالاهای اساسی بیش از ۴ میلیارد دلار است که بخش عمده آن، یعنی حدود یک میلیارد یورو، مربوط به واردکنندگان روغن است.
🔹
پیش از حذف ارز ترجیحی، مصرف سالانه روغن حدود ۲ میلیون و ۱۰۰ هزار تن بود اما پس از حذف ارز ترجیحی، پیش‌بینی می‌شود امسال مصرف کل روغن به کم‌تر از یک میلیون و ۸۰۰ هزار تن کاهش یابد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677069" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f349f12e5.mp4?token=WiRfgUl3Nf389v0fdvotXefvd1Qx9NBFP0KEsuqNwa8ZutOVL1g3EpKD7nw-zwI98WstZQuIEPhx99mhKLrBjZQAQC4jLz-4sKRM2snZDpedzrc0FnKi1iS0xWn458aVb-h2dOh4lfxj_MEm9hE1BzyUdaq5Ir2SEWNAINhBlLHRqNG4Wp3x42F2HNG4p6XeA-REH6FbXopLuMX9QTzm7Z-PrEcPVbJ_13ue9WrpQMeqJoF_grkIT34jCMN8kPz9XMdTKO6W5z-K5TMuI8PBl3bQXXB5bCB6P23-vfFZgJRm_V1OSqw8DkzNs1PsilaOSiNn6Z012kVdoPSFcwVtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f349f12e5.mp4?token=WiRfgUl3Nf389v0fdvotXefvd1Qx9NBFP0KEsuqNwa8ZutOVL1g3EpKD7nw-zwI98WstZQuIEPhx99mhKLrBjZQAQC4jLz-4sKRM2snZDpedzrc0FnKi1iS0xWn458aVb-h2dOh4lfxj_MEm9hE1BzyUdaq5Ir2SEWNAINhBlLHRqNG4Wp3x42F2HNG4p6XeA-REH6FbXopLuMX9QTzm7Z-PrEcPVbJ_13ue9WrpQMeqJoF_grkIT34jCMN8kPz9XMdTKO6W5z-K5TMuI8PBl3bQXXB5bCB6P23-vfFZgJRm_V1OSqw8DkzNs1PsilaOSiNn6Z012kVdoPSFcwVtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف خوک هار به کم آوردن در برابر مقاومت مردم ایران
رئیس جمهور تروریست آمریکا:
🔹
اکثر مردم هرجا اگر بودند تا الان تسلیم شده بودند. اما ایرانی‌ها تسلیم نشده‌اند.
🔹
بنابراین، من به آن‌ها اعتبار می‌دهم (تحسین می‌کنم).
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/677068" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac896a2c.mp4?token=qre9Ikha5JI1U7e9HRJyp1MWhMEt3v1110QoPNGJODDvxg-N4LFB-rc5zhieGpcruesajX_p18vbQvPU_0QPdG30BhvbJn2J6ffNUm2gR_g4xVrX8BH7O8ww6WSGt5S1ctxHXgf_2A13UnGixNShypTQBmYXKf6z4YFZYdP4-yJGXOlQSkmMMWq_wStYe1zLNeTrvMCIXiGqGMa1UhJZ7Gz6Fq10L5SVxiOBaszbV5MCGduFdhyfNIxCNxYQ_XEvBsDO16sZP_x9WXcgB_gIZGjhDTHMiXt_vEb1wiZZwDqbOdHjC5omlk6aLbmJVnuJeTKJhusQoy3v-woHbjilnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac896a2c.mp4?token=qre9Ikha5JI1U7e9HRJyp1MWhMEt3v1110QoPNGJODDvxg-N4LFB-rc5zhieGpcruesajX_p18vbQvPU_0QPdG30BhvbJn2J6ffNUm2gR_g4xVrX8BH7O8ww6WSGt5S1ctxHXgf_2A13UnGixNShypTQBmYXKf6z4YFZYdP4-yJGXOlQSkmMMWq_wStYe1zLNeTrvMCIXiGqGMa1UhJZ7Gz6Fq10L5SVxiOBaszbV5MCGduFdhyfNIxCNxYQ_XEvBsDO16sZP_x9WXcgB_gIZGjhDTHMiXt_vEb1wiZZwDqbOdHjC5omlk6aLbmJVnuJeTKJhusQoy3v-woHbjilnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
اما لذتِ خدمت برای حسین(ع) را فقط عاشق‌ها می‌فهمند...
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/677067" target="_blank">📅 20:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvNZqogJwY_UF-Nhgd_7cVLxZrVepay-q-DHIPzQTXCoHCQyf-2xnS8b6e5ba3xRWLoHtTbOrMkWbqLwcKqy259o3BBq_6rMoXLJ21G6wuHXomWubCtV5HWciJYFjl84p2JEkLBnmi_4LS3oZCAaxsQoZaPcGvm-NtHouR4uPf9Q-aolYDfwKqhz8nmF7b74L1MiQaTzeybvrUBKegKnfbwH_4aT2gf6QnodBLbgMkvLz-CByvstY4tTdkBOv809ZUsP9xSsyX6n5DDZZEtJNwYK0W4BOJ0HYy4eBYslZHcK6XhdG4xKXcwQ-HBA-kqEaA_--0CIK2VqzV0OeeOdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بیت‌کوین به زیر ۶۳,۰۰۰ دلار در پی مداخله‌ی آمریکا در بازار ین
🔹
بیت‌کوین در پی انتشار گزارش‌هایی از مداخله‌ی ایالات متحده در بازار ین، سقوطی ناگهانی را تجربه کرد و به زیر ۶۳,۰۰۰ دلار رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/677066" target="_blank">📅 20:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzrhKfJ1HosicNqqKycn-Cu16TCVGujl1m16Cos1bEWo-ao2SRjdFcfZGGqBmMmjc76p58P9CFBEChbg1OYdt95qA_lODtuKYnMpCkeI7jYEvc_qf2Jf1hDbRkyvdnOqsdoKYLRzf_gMpvXoZip-3Z1Pir0NAXF1sScGqUS3v2An7DU7E6j9Q28NBqwhunS7iSWbu6WJaUa5jERlv0ReaSsdsCKC1jG_6QYV94k-RVGMK1G64c7x7ojGTEOmAAnqQoCaVFV2maMikRulpO6Klm27i55lWP7v6E6B21rv8ohfIQFKZNOvWb6I5Pgv5ZpAtihMOmBAkWodX7oI6_RcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امانوئل مکرون، رئیس‌جمهور فرانسه: در پی بحران مهاجرت در منطقه سئوتای اسپانیا، نیروهای نظامی، هواپیماها و پهپادها در مرز با اسپانیا مستقر شدند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/677065" target="_blank">📅 20:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294f7820ea.mp4?token=rc3o66UXUw4oC2cKxRghKcwIt2Nb4tKVoLe12Od3YKrrnAIjmKmW8ciZHrd0c1C28B1IJgWe32A0LQbQkb7aFz8EKPGipZHUe-DhJrayX2YZrKtclaEK5Q1PzEMOfQLmt7xW_dswC5nqIay0xmXaX0QXBvv19VJcjwluIaOFJupTatETgjUxyHvOzAdhf9S-etTV6QyQVIckv5THuy-uaP5GrMlo6APfXb7LePHPcYvAPJS_XfbssSJhRc2tdiA8UZxAfxRQyeET9KEkXw6mnyOMJXuHhvtqdU5MMI-ePvUW82d_ucycJdSQgipUm-D1GfgVpyMVWDmgVKyxw_447g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294f7820ea.mp4?token=rc3o66UXUw4oC2cKxRghKcwIt2Nb4tKVoLe12Od3YKrrnAIjmKmW8ciZHrd0c1C28B1IJgWe32A0LQbQkb7aFz8EKPGipZHUe-DhJrayX2YZrKtclaEK5Q1PzEMOfQLmt7xW_dswC5nqIay0xmXaX0QXBvv19VJcjwluIaOFJupTatETgjUxyHvOzAdhf9S-etTV6QyQVIckv5THuy-uaP5GrMlo6APfXb7LePHPcYvAPJS_XfbssSJhRc2tdiA8UZxAfxRQyeET9KEkXw6mnyOMJXuHhvtqdU5MMI-ePvUW82d_ucycJdSQgipUm-D1GfgVpyMVWDmgVKyxw_447g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: میدونید موشک‌هایی که ایران به سمت‌مون میندازه رو چطوری رهگیری می‌کنیم؟! اینطوری: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/677064" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677063">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سیم خاردار بر بالکن‌های بارسلون؛ اجرای طرح آمریکایی-صهیونیستی برای آشوب در اسپانیا
🔹
تصاویر تازه از بارسلون نشان می‌دهد شهروندان اسپانیایی برای محافظت از خانه‌های خود در برابر مهاجران آفریقایی، بر بالکن‌ها سیم خاردار نصب می‌کنند. این موج مهاجرت هم‌زمان با…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/677063" target="_blank">📅 20:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پزشکان ناامید بودند؛ اما او با ۳ پیام مهم به زندگی برگشت
🔹
00:09:00 چگونگی جداشدن روح از بدن و تبدیل شدن به یک نگاه در کنج دیوار اتاق
🔹
00:28:50 التماس‌های عاجزانه مادر به زائرین حرم برای شفا یافتن پسرش
🔹
00:38:15 درخواست بازگشت از دستی با هاله‌ای سبز رنگ برای دلتنگی‌های مادر
🔹
00:42:05 گفتن یاعلی زیر باران و حاجت‌روایی
🔹
00:51:00 متولد شدن و آموختن دوباره الفبای زندگی بعد از کما
🔹
00:58:00 درخواست اهمیت دادن به مادر، خانواده، نماز، از من در هنگام بازگشت به دنیا
🔹
01:05:50 تغییرات بسیار زیاد تجربه‌گر بعد از تجربه
🔹
قسمت هفدهم (دوباره تولد)، فصل پنجم
🔹
#تجربه‌گر
: سیدسبحان حسینی‌نژاد
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/677061" target="_blank">📅 20:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677060">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای رسانه کویتی: ایران به ساختمان یک شرکت چینی در کویت حمله کرد
ادعای تایمزکویت:
🔹
حمله ایران، ساختمانی که متعلق به یک شرکت چینی در کویت بود را هدف قرار داد و منجر به مرگ یک نفر شد.
🔹
مائو سخنگوی وزارت خارجه چین گفت که این حمله به هیچ تبعه چینی آسیبی نرساند. سفارت چین در کویت پس از این حادثه از شهروندان خود خواست تا آگاهی خود را در مورد خطرات افزایش داده و اقدامات ایمنی را تقویت کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/677060" target="_blank">📅 20:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677059">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXBViHA-4dvH7_T8_ZOVN2hqT9yd_1w-Mik5sdGculd0bXZcHSxstpmh4caUh2S7RsypDHBfoy674o6BfTfBrWKgY65Z095CvqaiS9NCIGt9RNmdijlInRTiBM-f5fS8_byBsvLAvPGFTys0kAP_4czmCJpo89jZPImQgeJvwh6bYfcMzi1TSwbhh3AcpFHZMe8kam5snNSPGrXiTngsidyTldi42djGgVYaPMAPx-AA2G_1FXQ2SzHfcv9foEHT5Ko6sVqsT3PmJGmO8kQHvy7_-DxW9ftkxd6rCpe9U0Vhf_bV0lnrpBYHnLTNcMOdb8tXGwMjeMb8Vynuf9e67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کشورهایی از شر بیماری‌های واگیردار خلاص شده‌اند؟
🔹
ریشه‌کنی بیماری‌های واگیردار حاصل دهه‌ها واکسیناسیون، مراقبت مستمر و تقویت نظام سلامت است، اما بسیاری از کشورها هنوز با برخی بیماری‌ها درگیر هستند.
🔹
مقایسه روند حذف آبله، مالاریا، فلج اطفال و سرخک نشان می‌دهد موفقیت در کنترل بیماری‌ها نیازمند برنامه‌ریزی بلندمدت و تداوم اقدامات بهداشتی است.
@amarfact</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/677059" target="_blank">📅 20:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677054">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDdtGIIsTDbwugZEf4ScOCRoarQsyPPO2Vt4krh7ofXkPVHLPVFK8DRW0I3IWHkNC-jqvM-iCY-LsVbATmjOfLREovUjXfuguusvUHwCBS0OBQw_uJqG3uBxCDkBd4UNnIq29lkGjYzWmCmqfjwsDRSCXjnvEONHQ1kE5sHQ18pCbCIsirCw8TfeK__49LhaRQu13UrZielfA3dxLciUS-YDDCjyihKfuOurSeIGEVaspHdg9ha4v56yKQLAXT932pUGc-0qqr5hT8xNIVpxHxAEyNDQYiYyREyoVb4n9-g2u1DsQx_bjt4RnXPSzAw9DPDRRN54Kqh-F7DPK95kiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/677054" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677053">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb554c3360.mp4?token=lNgDm4_BX9oHXkdIHYOPbFwpRnDapw4VlT_OrAN3nKe2a5ZybIVerSEzVxBUV20ycLJeSo0_9Fn59OWU_8zL17djLGXeciogTVMyQ9VwokZDDk-B7H1pFO9Nf4tVjtl8Kq0K6FyxTG0S2ymwPOPWTqDvO9cNqo07c_LdA03wpD5xKeACz9VDBYSqUcsueBqhxEukuiNMwd2JU7IrgGvfFrVj0yYA3sAuMr5lXOMX-limoRgSDChn-3EBQTpG4XKlxQfFb1F6czJmyybZbBtNLGSDm_pn14WT0cVwUj3FG80A2t6Yl7sfnQbGGHe5o8hwdR57BYsnKI3Q9RiKZXqlWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb554c3360.mp4?token=lNgDm4_BX9oHXkdIHYOPbFwpRnDapw4VlT_OrAN3nKe2a5ZybIVerSEzVxBUV20ycLJeSo0_9Fn59OWU_8zL17djLGXeciogTVMyQ9VwokZDDk-B7H1pFO9Nf4tVjtl8Kq0K6FyxTG0S2ymwPOPWTqDvO9cNqo07c_LdA03wpD5xKeACz9VDBYSqUcsueBqhxEukuiNMwd2JU7IrgGvfFrVj0yYA3sAuMr5lXOMX-limoRgSDChn-3EBQTpG4XKlxQfFb1F6czJmyybZbBtNLGSDm_pn14WT0cVwUj3FG80A2t6Yl7sfnQbGGHe5o8hwdR57BYsnKI3Q9RiKZXqlWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: چه کسانی از دولت با ایران صحبت می‌کنند؟
🔹
ادعای ترامپ: ویتکاف، جرد کوشنر، جی‌دی ونس، مارکو روبیو.
🔹
خبرنگار: آنها می‌گویند که مذاکراتی در کار نیست.
🔹
ادعای ترامپ: آنها فقط مرا عصبانی می‌کنند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/677053" target="_blank">📅 20:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677052">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای رویترز: شبکه قمار غیرقانونی ایرانی به دور زدن تحریم‌های ۴ میلیارد دلاری کمک کرد
ادعای رویترز:
🔹
یک صرافی ارز دیجیتال مستقر در دبی به عنوان مرکزی برای جابجایی پول غیرقانونی ایران عمل می‌کند. این صرافی، شلبیت، یک شبکه قمار گسترده را به رهبری دو اینفلوئنسر جهانگرد، استخراج بیت‌کوین و بانک مرکزی ایران، متصل می‌کند.
🔹
شلبیت صدها میلیون دلار ارز دیجیتال را به بایننس، بزرگترین صرافی جهان، ارسال کرده است. شلبیت مرکز عملیات جابجایی پول ایران است که از طریق آن شبکه قمار، بانک مرکزی و سایر نهادهای تحریم شده ایرانی به بازارهای جهانی ارزهای دیجیتال دسترسی دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/677052" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677051">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b093f39759.mp4?token=ipJOhOF6M1RmfwseNM__mAyjau8KkNFxYeX14K1eHk1xHLaoiAmIjC1drXu-XMMWH54qMHTHz_oX1VtxCq31poS_Z_W37yWxRDKbdJL3Xmdmq30McixoQDENa6Dn5UXs1q3MyTrQpemgduv1vTKK3Bq-V0KMIYzEoUOXeq--7kV46ANPoSf0BeR8AZAIajYFA2X9iyGPgOgpXVaVzddiw0uVFpWWU-QiZ0LpuW6_S-6BPAkV8EcSvDGXfSIrttc2NR_a6zj3_80OPJ7_x0dcMPANcBpo946VoxCVutqlGuC8KC_kamRDcAeX6kcaIrkkdlTI3QJ3XlylD_kHoLkkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b093f39759.mp4?token=ipJOhOF6M1RmfwseNM__mAyjau8KkNFxYeX14K1eHk1xHLaoiAmIjC1drXu-XMMWH54qMHTHz_oX1VtxCq31poS_Z_W37yWxRDKbdJL3Xmdmq30McixoQDENa6Dn5UXs1q3MyTrQpemgduv1vTKK3Bq-V0KMIYzEoUOXeq--7kV46ANPoSf0BeR8AZAIajYFA2X9iyGPgOgpXVaVzddiw0uVFpWWU-QiZ0LpuW6_S-6BPAkV8EcSvDGXfSIrttc2NR_a6zj3_80OPJ7_x0dcMPANcBpo946VoxCVutqlGuC8KC_kamRDcAeX6kcaIrkkdlTI3QJ3XlylD_kHoLkkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌بس؟ نه فقط پیروزی
🔹
خبرنگار: چطور آتش‌بس را احیا می‌کنید؟
🔹
سگ زرد: ما فقط می‌خواهیم پیروز شویم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/677051" target="_blank">📅 19:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677046">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXot__K3VOUWQpMF7djQyaGG2Vx4LS8sTiLVU4BSDw9CV2ymY85cWOXd_6ungdeP-TjP0uisiaUaTAmo8BAJJ_dj39MdTnnwHVw-McNUcK3Ih0ShDHxQY_cN9iPlh6hUUO49nJZinKSDcDqpHIjLZiguSLbJ5uHr6xlyyCPzvPH8F_DkQN_0liBuweU2OYKNqOpg11wqhsIbcfnGt7mSEcWcgVYVRQXgpK3gtIQMxrq_pIaXQhTfaqnwynFxGj0DFi5oJ0n0wzxuoseUYi4WBEINBILR_vZ3f6lbQIiyZWLltKt8lO5Nml2qiRY8Y3FIm_b-ulEQlTWeIHQkQEfGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzYXtyI0ow3_T3oE4BCE0WYZ0-yMpaY5j_ecqTgK_nFOACzkTRZekSLX_gJ4D74rx__NO9w5f10yHIQVgugDBcdry4J09F0gtEIfn0FKkk9ea1kn1WOOLWUoo0QX-_Oh0tbky4FJNLxtXyKB61gN0oan_v_A3AWzqQo6eW8mcSXCd7qIOgn6sp7cklR3uw4ii8l_ShR_5fopEbIcoBYpW6oWo5kBZFUHHsyLTh1yd3u_G4sdKo0Oc2KZC6f_Q4tIvB5U20FNFIO4HHf8KdygEKMCkoCuHCJZMqI6SQ4yO0hESi4epWDLwHfzN9g4uyPHEOI7epSi07ucMBaaAD9RPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdYF_kkTPOiA6zodUBZ3QB5ZXLXF0VF2vAN0pk0rmwhYNUi5UR5LFicCfKhDhIpJD6CSLDtEgrFoCD_fXyBydRBko1Ee-ooykitbfDkikaJnkSKhmZVdW-3QomuikCsVWYBpHhHSG-4OSA_ms1a7-XM9yXZ8dovY-y3aFX48pr8lMrVrYEyj5cHGpq6WTZKPNMvsZnZDfVSwX7auTn2uMEOOUrsF35vYbVndIiXghXN2dAq32LURirIoERDhmnd0ZKI99UR3ACfYTOoRVaNTNl5-HzWFIH61-EQ_Sw8uKPmUyHgHFHLBdl78DrbPeT8PbEf3WsNdfnuGuYq-V0Ppfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQqwPokZ49Y2WTH8YBbJWGuX3fZtVhm3r0y1rufvkP6jeQduXx9O9RWV01SWH6t04wl7dScEbzM_XUJ_LUcQQyfPP-s-615-TfoSKDz7gGmCM3FFtv6IkWIg_HuhgrujQl78zdsUT_hZnkttyC7doWPhYg1Cb0ztr7nPGhNF3SCvYwin5AFCTUw3PfaPV0sF-3E4-pgODZsoBTI1iOFeVBXTjz8B03i1BD-TEWXbhxvG2XxhpnSB5a7y2wXFqPDC6jzSr9BBzDRl_a5Ds48vcIdu02Sx7KtTmAPoVOzL0rBMBrXQNBoqyjcat-mQhX_YIDC8EuFcPG0yg2Y9NF5hcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
حفظ منابع آب، از عادت‌های ساده و روزمره ما در خانه آغاز می‌شود.
🔸
آب شست‌وشوی میوه و سبزی را برای آبیاری گلدان‌ها استفاده می‌کنم.
🔸
شیر آب را بیشتر از نیاز باز نمی‌گذارم.
🔸
هنگام شستن ظرف‌ها، آب را بی‌وقفه باز نمی‌گذارم.
🔸
برای آبیاری باغچه از آبیاری قطره‌ای استفاده می‌کنم.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/677046" target="_blank">📅 19:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677041">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7952931be3.mp4?token=mmmnjt8uEtnmp_irjtfprYUJFD3lLLIExYuR4MS48CB6WUs0yi-AdB-gy2hUtP1E7PfTNZRp_xfawHbkKbmM22PCSKlaZbe2uyrErKYC8gX23Xk8c9LDeP77cEj41apCXFBAEOiAouA6WXOzDwDfbW9rfl9andS30XXHudd2i6_00P6i2wtoUx1A1w3RW50p5alrl988ioPPT-g6R9bO1h7xoSvE6azU3ius58mAmBXIrx1a1JXWSdfvmdJoLMQIe7TvfST9FUw_HcVZIlUIspboouMvpy0Z-Wnbr63h3tqw5IHkhsOWqYxrnsXaWO_ARWojNdbxt5BtdZCJpBj-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7952931be3.mp4?token=mmmnjt8uEtnmp_irjtfprYUJFD3lLLIExYuR4MS48CB6WUs0yi-AdB-gy2hUtP1E7PfTNZRp_xfawHbkKbmM22PCSKlaZbe2uyrErKYC8gX23Xk8c9LDeP77cEj41apCXFBAEOiAouA6WXOzDwDfbW9rfl9andS30XXHudd2i6_00P6i2wtoUx1A1w3RW50p5alrl988ioPPT-g6R9bO1h7xoSvE6azU3ius58mAmBXIrx1a1JXWSdfvmdJoLMQIe7TvfST9FUw_HcVZIlUIspboouMvpy0Z-Wnbr63h3tqw5IHkhsOWqYxrnsXaWO_ARWojNdbxt5BtdZCJpBj-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ دربارهٔ ایران: ما بسیار محکم به آنها ضربه خواهیم زد. در نقطه‌ای، آنها خواهند: «دیگر طاقت نداریم.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/677041" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677039">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65099aa8b3.mp4?token=XZDhsySjzEui4d9ZqzMERwXMIIwVVPMGsqK1-A8beqIWuErfTGJKs24J43Ti_3mvWhnlXB2we_79oi3YhqUibv-7Q-JU_p2FVUxj4QAjrVW1d7wmsOS3I0a-J-k-QN26cSw5t74roYJ2F0StH4ATOPnB4Ji4HyRbv-1deJrSPoz5qXpMRErFvH_z39X4nMNzG1jrmANsLpgXxLaE3UWVQGl61YmRfUkpW5D5SrLbHSWts6UN4L4gGbHKqtOEH01DxSADYkeTdD4TRq30MzdhzJAtJLuw8cxB5VZr7OujzDHQbFbDNdggTovSLO_90qD5ACpG7Yy7dM3Wr9b2-pLu2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65099aa8b3.mp4?token=XZDhsySjzEui4d9ZqzMERwXMIIwVVPMGsqK1-A8beqIWuErfTGJKs24J43Ti_3mvWhnlXB2we_79oi3YhqUibv-7Q-JU_p2FVUxj4QAjrVW1d7wmsOS3I0a-J-k-QN26cSw5t74roYJ2F0StH4ATOPnB4Ji4HyRbv-1deJrSPoz5qXpMRErFvH_z39X4nMNzG1jrmANsLpgXxLaE3UWVQGl61YmRfUkpW5D5SrLbHSWts6UN4L4gGbHKqtOEH01DxSADYkeTdD4TRq30MzdhzJAtJLuw8cxB5VZr7OujzDHQbFbDNdggTovSLO_90qD5ACpG7Yy7dM3Wr9b2-pLu2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوست تخم‌مرغ رو دور نریزید!
🥚
🔹
کاربردهایی داره که اصلاً فکرشو نمی‌کردید
♻️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/677039" target="_blank">📅 19:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677034">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای سگ‌زرد : شنیدیم در مینه‌سوتا یک حمله‌ سایبری رخ داده؛ آنها تقصیر را به گردن ایران انداختند؛ من اینطور فکر نمی‌کنم
🔹
من تقصیر را به گردن مینه‌سوتا و فرماندار فاسدش می‌اندازم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/677034" target="_blank">📅 19:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677033">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvCB5G2QP42lnNDnjMpf-Abs_VKBfmCGpWBNQLTNzzI-iokprnc2kkgGtBa4noll6p5gOZnUyQenK2G9Y4T1rkoet2aHm3GJ4udDAkUhDSEvUrYkyHgvLR6jEsaX4tryKjLhc8LhAvW4qdJQDiADMEfxU1jyjRLKkSPZHfSw7eQokTgmDfG2GKhieKx-erBPrr-o72oUmgL6APiLUmxHCmN-4Kr46oZW9QTbHgr2NHBHNqtZsfpMZRXaTO8r2-rtw7nLOPn0CYAlrrSuIMQ2TmbEy4BHwJhDYp3_Vo7GTEk_nwL1bpTPbDehf2djeK6AfKs36w_2TVAUSlkLrwxxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران در میان کشورهای با پایین‌ترین قدرت خرید مسکن
🔹
بر اساس تازه‌ترین گزارش ادعایی «شهرهای جهان» سازمان اسکان بشر ملل متحد (UN-Habitat) نسبت قیمت مسکن به درآمد خانوار در ایران به ۲۵.۱ رسیده است.
🔹
رقمی که بیش از دو برابر میانگین جهانی بوده و ایران را در زمره کشورهایی با کمترین استطاعت خرید مسکن قرار می‌دهد. ایران با ثبت شاخص ۲۵.۱، فاصله قابل توجهی با میانگین جهانی ۱۱.۲ دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/677033" target="_blank">📅 19:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677032">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3fb4494f8.mp4?token=p6CuGZi00Ubhv4J6tciRW58qoiHZvJKG2BgrAKpAt9XS3Wdnr0BjXHXpennTNcAWJfN8ldC77m6ZrL7EzIAaL22AHgMmrqW1UamVwsQzHSQuvgnN0db8-s0lthIGJ7Nb324vxeR-6H7kbJRgoomE7ugoWegcgtK8l2wIztHw9gnImHAObzyNs5B-KrU6Z6Y-6nL-cHcqBTLXDvtvybiO4hokYEVycylSo3b2zRCAyyyCXiAtN1hpl0jIxitOkc8j3thYe2wpSBsdopk2S6CeLTICx3Zu_LI3u5NPd_mmsgwfuXeA7cxJfbapc6qvyfk6aCtlqrU72OxWYudYiC8D9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3fb4494f8.mp4?token=p6CuGZi00Ubhv4J6tciRW58qoiHZvJKG2BgrAKpAt9XS3Wdnr0BjXHXpennTNcAWJfN8ldC77m6ZrL7EzIAaL22AHgMmrqW1UamVwsQzHSQuvgnN0db8-s0lthIGJ7Nb324vxeR-6H7kbJRgoomE7ugoWegcgtK8l2wIztHw9gnImHAObzyNs5B-KrU6Z6Y-6nL-cHcqBTLXDvtvybiO4hokYEVycylSo3b2zRCAyyyCXiAtN1hpl0jIxitOkc8j3thYe2wpSBsdopk2S6CeLTICx3Zu_LI3u5NPd_mmsgwfuXeA7cxJfbapc6qvyfk6aCtlqrU72OxWYudYiC8D9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواداران پهلوی این فیلم را نبینند!
🔹
یادبود کودکان شهید ایرانی در حملات آمریکا و اسرائیل در حاشیهٔ رویداد محرم‌شهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/677032" target="_blank">📅 19:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677031">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c087beb7d2.mp4?token=RYjjBO2GnyWTga62O44wEPV09YjIRajK3Vtjcf-aSo1oLaDi_SukzNYxbhDfY1u27O-QL4Im5AemaAjtXA3p6TL2dHLKRcapsrLNr8vymF0xFCz0nrVo20cKhEAi0WoF3pjFTtK95X7jeNCh_bPPQN3AffEYaQHLEWyB1YgFqRq8M_u48ZWbV6XUHn4AQh2NUbnlmi3k1rp7pxEdSpKbprJ1kTzcyKVHOfu2JNyqXlsWFfAAGHIDHEsAFMAV-6Pah0sEJu43-MNujS4MDEUY53TtceI2SngTqUEhf3Vg2J2U9n2P1xNUu3bqJySiSxLuxu_rcCg9B5JPOaFFhp_sSa9uEwKYHt0eY_G_xxU8tZF-JrJNeVnKqhEotySPJ1f-8k0_Ln-FojzSbKWwfBOQHdZUl1hOtPp3Zkgj2mJFfdAhQdFdRtn_mR6PkwpStHWHKt_DmJPG5Fk6ABqhLk5zeuVFGGF-vyqLyF8oJr_dtTyryVxhjNH8yAQcREa3L4gJnXDyL22CEHzvuHTf7CBgarhsLSnkT5MHOSx5DgX62gB3rSOFkWZWyY-UOi7wWt707Egj5z6PKzhu_fu6b74vTIRxMsMfdSlWc_7KtTlUMD1oFe2jKQpK5vc_zMUWlCw0sx9kLR63OO1sGB15xIrNbJCyoucgyEhCqCTWm9pMghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c087beb7d2.mp4?token=RYjjBO2GnyWTga62O44wEPV09YjIRajK3Vtjcf-aSo1oLaDi_SukzNYxbhDfY1u27O-QL4Im5AemaAjtXA3p6TL2dHLKRcapsrLNr8vymF0xFCz0nrVo20cKhEAi0WoF3pjFTtK95X7jeNCh_bPPQN3AffEYaQHLEWyB1YgFqRq8M_u48ZWbV6XUHn4AQh2NUbnlmi3k1rp7pxEdSpKbprJ1kTzcyKVHOfu2JNyqXlsWFfAAGHIDHEsAFMAV-6Pah0sEJu43-MNujS4MDEUY53TtceI2SngTqUEhf3Vg2J2U9n2P1xNUu3bqJySiSxLuxu_rcCg9B5JPOaFFhp_sSa9uEwKYHt0eY_G_xxU8tZF-JrJNeVnKqhEotySPJ1f-8k0_Ln-FojzSbKWwfBOQHdZUl1hOtPp3Zkgj2mJFfdAhQdFdRtn_mR6PkwpStHWHKt_DmJPG5Fk6ABqhLk5zeuVFGGF-vyqLyF8oJr_dtTyryVxhjNH8yAQcREa3L4gJnXDyL22CEHzvuHTf7CBgarhsLSnkT5MHOSx5DgX62gB3rSOFkWZWyY-UOi7wWt707Egj5z6PKzhu_fu6b74vTIRxMsMfdSlWc_7KtTlUMD1oFe2jKQpK5vc_zMUWlCw0sx9kLR63OO1sGB15xIrNbJCyoucgyEhCqCTWm9pMghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خانه خودمان شروع کنیم
🔹
هر اقدام کوچک ما، قدمی برای حفظ منابع و آینده ایران است. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/677031" target="_blank">📅 19:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677030">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e611bb25cf.mp4?token=fByaTUE8us2H4Vost_mGhpKS5uhBTvOEKxJLr5I6rtDUi2SIeh4gI-PL_p8TE0wO_pWKAm3fC1IrU8GRKlBgZiDF2PkMEEgyevWCyOIwQM0w8VbDyLNb1LhZEBo2H7lX7QHfM6-mfLlO5tOCliX0RMKsR-fr0It6HRJrzl5V3jiAmiOs1UmRssoM7WsjabiqGhdPvxWW43dbPqbvGHeEeM3r1P3pHzsXNI7SxnWuwo4eYu5cvYR1PbAu5lXP4c8NpH3npkXrFSF7f_f6grh4VdHAv0feBHlnYxQysKYvM6irP7ncZunJGm_xgn5LHMg7cWlb6S1IEIY4AHMbDSxHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e611bb25cf.mp4?token=fByaTUE8us2H4Vost_mGhpKS5uhBTvOEKxJLr5I6rtDUi2SIeh4gI-PL_p8TE0wO_pWKAm3fC1IrU8GRKlBgZiDF2PkMEEgyevWCyOIwQM0w8VbDyLNb1LhZEBo2H7lX7QHfM6-mfLlO5tOCliX0RMKsR-fr0It6HRJrzl5V3jiAmiOs1UmRssoM7WsjabiqGhdPvxWW43dbPqbvGHeEeM3r1P3pHzsXNI7SxnWuwo4eYu5cvYR1PbAu5lXP4c8NpH3npkXrFSF7f_f6grh4VdHAv0feBHlnYxQysKYvM6irP7ncZunJGm_xgn5LHMg7cWlb6S1IEIY4AHMbDSxHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای بین‌الحرمین در ایام باقی مانده به اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/677030" target="_blank">📅 19:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677029">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQE1Tol6quSA5AS43C8pOEk2kta0NUYTFXt1K7zjIY3RK6cTIZ2eoKVsN12--gixlL9xIPinJOvHvVnHpNVpvSRuqdSr3G5uAyo8mcHfcFgcSVZHCq_-oDBZgsK1FfGplGOchY5HAZFwBmm3bgKoGolcKFIq2XG_tiyrbB-r8tyP0v6QBNime2hY7gwkTgoJKyw3BlDcCMZVInQBWd6DoPCP90oYSzgY6j4g-9fVKnmF8YOwXHpsDT05uFyN_ejFQJHyMHiFterhoGgmMXoIgwNiw5DklJKB5YnGXmgeVQLJToYjuBqaUogiCMfpWn7J_VKIo4IZlr59CoXfdSWOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر موشک‌های رهگیر پاتریوت آمریکا در طول جنگ ایران حدود ۶۵ درصد کاهش یافت
ادعای ای‌بی‌سی نیوز:
🔹
ذخایر رهگیرهای پاتریوت آمریکا که پیش از این ۵۵ درصد کاهش یافته بود، حالا ۱۰ درصد دیگر هم کاهش یافته است.
🔹
طبق گزارش CSIS، آمریکا سالانه ۱۸۳ فروند از این موشک‌های رهگیر تولید می‌کند و حدود ۳.۵ سال از زمان می‌برد تا دوباره آنها را بسازد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677029" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RybMGNqpYhHxuFWxKrBjcZzr3QvwrDgaOFSEWXaJ8yS41mA8PaPoeFDoZY2XaXJ7OkHAn-K4V3myfTzby9n1_cdfr6AhgVJUb_5EE8B4zyNxliK1n5Kzr6lqfz0TsLlDwyZwXhwyHbaIJPR2xocLG4T5OqWRaKiYyAUNCwHtivEM0niegxfDYMt5DQP_Z0LiDhtqYYouLbYCB_3rMHaMOko-ndxGS63agozTwPO5VC-7WsEzdB8jAqWwCf0o5Ej8VNKxFdss8FEdLQUUO_Rre-1t-l8VRqxVbuZ8RFSdHG7tvucpcGTT5Mn-aqfcBbRZDiMu5mJzZjZBIqlyiuzXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmDSA_EQTkfUCXpOAGdQTCFl7CtslZf8dcyx9K3j3TnBpyE9RNPQMRtGqEzcvxNFnZU0M4AwaNPHq07bfFUz3-ZRZLKG2MMy3n24YwmpHg18EMg5M9wfwMQOMxBSi_o7DJoZEF34tsiPoWxwJpf-ilUIjispZpsAPGWhyHNqwW7xTjcGnbIvkGYPRicHG4cqDTVU9jTH2L6Dfue3l5f-otBxRUlIEGMvr5l4GwClDNavfuyhI574933IFNArXo_LguCGcd-XLnKAM7Prx4ulS4v7dPigQFhN8g4G909lqoYJofOgtCJJKsZT_fNNa2LF1y4f-GKnaUWNL-VZGfrwlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avk6PhC96YJ1_k1suQLPL6pGkOwbDMZCkDdrENBFliSZg-9Y4zARp2NqA_3n8L0Kfs8iUYD3Cw5Mgd7A-xYFY6YRbMFp2Rht5gApPgYiecxRaKsTBIB-ODfh32XoifqUjLTmgKqfbMOHcNUOMsh_Xwf-XG7VEZ2XPXPNZ-NmMCf_TCWH5aFCD2LOaZ4DBfooFo-Nhkpxgw68Ux0mK5wUqmbHbMdfkVXbc0_RADEA9bfsJeeLCP9RY6PK_uQ3QyKZZ2yyIIcpcpZMYTBjeveY8H7alrcHth8SMDJ6cP3n1Q8Glq_yUhuyLZrhuH2qCOGZ020afEGnEKnfmVnmZcHNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWMWFdQ0ZJ87EeLRLGaD2ACZG8hnFhkLEMoMwttslkERsCaN5-HoGJjdVEvd5bfOWupVevQ0kwljXVI26ikJqg46v2T4wLpXfg_5r45cfsJWAlvN9wRbNDuVeb-egcU3wE1QBtQnCEYGXX3O7aIwVc29CFBW0qRNmMzLQHH_u82xe5MOjWsDxS38X6R4D8T4epVqWYMXZfIj1xcFU5hTateGp-ynkJkm1VEOMVbXQOqwbghC09Y7YAZK-Oc8FqWqg5ELD4To51qXG6Cek5pShEDAid_EXyVIyLOE9cw5WxaUXC636e3gZIFbej3D-2Rwya4Rp_JvgGJaaxhq09wkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwzxEVIvxZfJEdmNfrUNz2dVbkjosN-HJ7EhDQfiOSy2tOO8DZH93p3WouUPY9kYxO-DkAjLrh_yJfQ7mPLXhZV6bmieL6iwYGSzUZ3hD4ctDs8Oa4SI20A64_-BR5LvA0EqPkLuydIt64hOjteiPresvD2qb6FxS3m6TfoWI9WEGx_SvFfWrxkuZxigW3iOVSpwZF5UA7-GXO5VN3_68Dh4YfpNvfOGEaunGELv7Ur7LY6z_cu-stsozTLJypL7N42MoPA8IQtb-SKDmWIn0jyuZe6xJ9WGNtSUvNn_WEh1xmPHeYazR3gomuxeZMNHDOx_wvPu79smOyJz8vQCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaRjVfNuGZ_whw3vGHxnYZzWvwqbNNzvxYoXzWP6LRzehZmFkEA3ywDy69LQr3v-HeDG4kWG03RHNvMGhFje2VLhTW5gNMnfRUzQnJIWkNJ8VW5FHmc3CoG5CtNhPTy51nFHfIdXxTcZwGU4tIOFjX_vaCmVZFYLPboCHNRWUMuH4QPbf6Td-CcfP44To7H55CD_drAWKaEGcugZhLQTDYW4YzIFCy1hkkO1RQGB1g2JK1zU5M1FKHyGOwV3PJzoU7553n7fA47XrgIrS-a87LmwrNxfCXYL8vAGKsR4r-yVLxrNyChYD9u2FZgAAOBBzo0Ypd1enYiWv87pNkkH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNpMXqKxIP1Ycpqz11CT-twQPmN2F2cjzLhyn7iwHOT6qf3rZABCmnfb6x5AkXugZEtG7tERo8eCDeG_ohUmKF6LIRUr9_q0Q_KFoRJGywq-NeSugmpVkPw6MpSHUdLDW1HhEtxsmUasNke8UIUfmFFrYmPj-hUOqasx8sY-jig2GWX8GV_deCnDuj1xQTe0gdNlr64zh-tq2jFTLq0dm-U-wQh8OQhdYWUJwnJt3e9vsuIURCBm55teDl_MQD8WoyqMfJ2RIRZmPy56v7Er-dCScONX_qNvQHL6oFiDR2dU6xC3y5f63x3wPR8Y8H4O6LaC7KJtiJADuVGg-FYCZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
اربعین یعنی کنار هم بودن…
یعنی حواسمان به آدم‌های اطرافمان هم باشد
یک قدم برای تمیزی مسیر، یک جرعه آب برای یک خسته، یک کمک کوچک برای یک زائر…
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/677021" target="_blank">📅 18:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اوکراین: علاقه‌ای به جنگ با ایران نداریم
اولگا استفانیشین سفیر اوکراین در آمریکا در گفتگو با یو‌اس‌ای تودی:
🔹
رهبران کیف با حمله پهپادی اخیر خود به یک کشتی ایرانی «شطرنج» بازی نمی‌کنند
ما هیچ علاقه‌ای به تبدیل مناقشه خود با روسیه به یک جنگ جهانی گسترده‌تر در خاورمیانه نداریم.
🔹
‌«رئیس‌جمهور من، فقط به توقف جنگ در کشورم اهمیت می‌دهد.»/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/677020" target="_blank">📅 18:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gp1dpDEXVWnnbMAa-MiJhi8hHmEKhJLoU670w8TPIcRwf0zGggYTxY2o6P0pBufL997A_UuAOwf0bi3cWTvR09Waa5Tf_61pXw2EKK9dc1wMI5nd8cI3iGO-7ftcjFEYmscBTrCAoTKalqlBH7hiGcbig0ATIJCmyznUB5AmGAbvfE2Te4tPEndofNYXd5eMwaVhQTjwqGqNAwTmte7nziD9ZPTE5l0TrguAzHGb10qMWoWSNMRFicVvDzIF1vLsRdSMdJEWHHZsMtxissTMMbGNGVDS0SYpgmB29VWALAH-9QxnCLLMnlWMlETfSqjnhsJwLuJI9oXRQCcFAiniWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCXDyIioQIueWjbEa-GjZEsVOBGecgl7TAWy6H1PSTgb4LxGFPrW7aO-oRyYzhJTXhJOsT7fKgfGHzLWAQaTgkvQsXMa4qzthsdiRKRq559zQ7e0Sz7VZOb1Likzh-Y8PpcUE7XxsTPg6eVqRebImPZUwGaTTBvxV9u3t-bDw9ESoDyrzj4f1N68Tk57TlluiSqy7lw-rBg5vQHAJay4W0p-jorEEfOo3Xd0s8QOD7T6ybRo_ygB3LlJCzX-u_m4eggkVwJ19hQ3iBse7O9QQKRg1n_upP-8YsEWGDFj_MtYAsTkYQx6HP2CA5hWMGRXyXQkwWRvXgNpkE2XCIqtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc9eu7m2dp_es4xKqnIENkxuOElzxElWBw0WVpiL3HuTrCHJMy9XU0rs8-Fj4g-JSF7nkLvZZP8Wv1S42Tcup1xRGK9PTa7TQUudX3N_eBydSR-06iSmRzgKPigcdvN95pblnEtSFunmhWevoLJhJbBb1fCnYoKk0lWDfIsj1jxkIk82H45Y5iJt1H3lpat_CpmIQVD6rpzrEHZjnxTyEhdM4p2G4HyecR4FXO7kaDHjXlb8cGTR9mPMqu-7bfZ_83FBOrlUeoejq33B1wXL32UA7aS0D1V825gdQY6lRuVcAm5Sv6XzzEn5LBtxaTT34SanUNDZTV7PiOnI0My8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkjnVqvFpp5-7E57b5L74iHGEbeXCRQNRAV7RyAaAhb36KXlHirddv9bRurhCCip1l2VMUVOORVpLXmSm_TmE0VAFrlzHpg34SMp__34RhuSKtvkI2mqgRt2f5L_92ht9ZrQImzed6_PYFvoj1LTne1vWGlvLhkaQnG73tUqFL3TGxVeCiT3L7t3wmEeMTOLmBmV2BFLWAewjhMtBTObVhaLrc3OuikiVp03BYobdWG766fWbY4wVxV8UaU7LgXvWDlG-BfDhzPU87MbPMdzqh0-3oVDpmUkrT8PEcLDT6LW1nRYwVgMYYQrLsW5kjWHwoAuD2yJpQbPg0bO46g92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBZEm3xoZGtYIpMh78Hbbbu_1peXkwMb0oCRRRTkFf53uQ7OOaPzoW4hd0ZJ8snpSliFfPiOkvFdHgi_NE1O0sPL-kc-mYASLc-Rq3r5hfHLXtngwS3D5k94jef28auOAXyAzR7Op1cHlZJxXXGZlGwEH1JAj4gsUjatJdOXRxLqojtKsSCQW_XT07U-o4Nt10lPv7-6QYxB66Sn7WAmJgCNC7a1q-dWSDI37SPmI_CCYGdWOiF7NwJsvk90j6rGbBCjecaR5WC19ntGmvbedyFLZ1NDLtEriDyQS3Rb9rIGRRkUZ_6pLr4ws25OchEcc9MZhFLMsw8SRyNehq94-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ نوع پاستیل خونگی و خوشمزه
🍡
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/677015" target="_blank">📅 18:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0efd09904.mp4?token=BL_hoPme2lwF86spVsghxKRAFZuzLBvjGEKnkFIVhWyVp7OwKc-tqip_2RBNSBlBF_t9HQhZX-ugXUuR26bXD4ldb1yksPkkFtsyCqOs15IXW_7gzlGEyvIhQGvvoThWLYINFCmDMLOfcgoBq6Emu2XINjLKzmyKOrXcw9qOKgrOYorvsSW8N--W6hQkoKLXfAi06L5eHOchsb5tLus_DiU4pBGz-egJpHIMf6Qf6_MnI8wYqEEotE6fQEtxqZKIkGzx4HwRlUAetJkyJll2guOBeoYwsDZWhw3ZUulFfkbqPj-1okWE7qHopqjQoyVWSK3LNJiK47P6qVv_HfWGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0efd09904.mp4?token=BL_hoPme2lwF86spVsghxKRAFZuzLBvjGEKnkFIVhWyVp7OwKc-tqip_2RBNSBlBF_t9HQhZX-ugXUuR26bXD4ldb1yksPkkFtsyCqOs15IXW_7gzlGEyvIhQGvvoThWLYINFCmDMLOfcgoBq6Emu2XINjLKzmyKOrXcw9qOKgrOYorvsSW8N--W6hQkoKLXfAi06L5eHOchsb5tLus_DiU4pBGz-egJpHIMf6Qf6_MnI8wYqEEotE6fQEtxqZKIkGzx4HwRlUAetJkyJll2guOBeoYwsDZWhw3ZUulFfkbqPj-1okWE7qHopqjQoyVWSK3LNJiK47P6qVv_HfWGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
ایمنی سفر زائران، از جاده آغاز می‌شود
🔹
در آستانه اربعین حسینی، راهداران کشور با اجرای عملیات گسترده بهسازی، نگهداری و پایش شبانه‌روزی محورهای مواصلاتی، مسیرهای منتهی به مرزهای اربعینی را برای تردد ایمن زائران آماده کرده‌اند.
🔹
این موشن گرافیک را ببینید و با دیگران به اشتراک بگذارید.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/677014" target="_blank">📅 18:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677010">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17770649ea.mp4?token=GuwZ360Ha5RcLEwFwnxg2Fp1IG0Mv0grDqJ4oOM_nools4FV-ff38mgSNDRu3FVbq8IMhrSde6vOjiy8A0-ETI8jHmNZOSB9po8XR2xRLMuQV1AMOSVfamT8aWvDxTBKTuURGuF72p72kIAPdQITWe0-CeriMGwIVXBMxslTn_21qikr-iuJ7-MrRTAJPZ9n-xt-QDZ6NvrUF0lfYsf4IcWvaiXNuARYkP0l_uE_8GlkrKnt-8JQoltO3CUA-nR1RWnMDg8KbqaBw2S3hn0rr_cq4xJC1qv3fLZeyGSv04D5D13qBnPQJyhsNGJGKtNjIZcieWmVq19ophbBQYoJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17770649ea.mp4?token=GuwZ360Ha5RcLEwFwnxg2Fp1IG0Mv0grDqJ4oOM_nools4FV-ff38mgSNDRu3FVbq8IMhrSde6vOjiy8A0-ETI8jHmNZOSB9po8XR2xRLMuQV1AMOSVfamT8aWvDxTBKTuURGuF72p72kIAPdQITWe0-CeriMGwIVXBMxslTn_21qikr-iuJ7-MrRTAJPZ9n-xt-QDZ6NvrUF0lfYsf4IcWvaiXNuARYkP0l_uE_8GlkrKnt-8JQoltO3CUA-nR1RWnMDg8KbqaBw2S3hn0rr_cq4xJC1qv3fLZeyGSv04D5D13qBnPQJyhsNGJGKtNjIZcieWmVq19ophbBQYoJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه شستن روغن و سینک از زبون خودشون
😀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/677010" target="_blank">📅 17:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677009">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نیویورک‌پست: ترامپ مایل به انجام مذاکرات در صورت موافقت ایران با آتش‌بس است
نیویورک‌پست به نقل از یک مقام آمریکایی:
🔹
دونالد ترامپ مایل است به روند مذاکرات فرصت دهد، به شرط آنکه ایران با آتش‌بس موافقت کند. این مقام افزوده که ترامپ خواهان توافق است، اما هشدار داده در صورت ادامه حملات ایران، هزینه‌هایی متوجه تهران خواهد بود.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/677009" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677005">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1efb3a2f0.mp4?token=B1yG8RgMorx6RDXqVgcuFG9vHkyNQH2Ef3xjNAYLzM4dKoTIAn8guCRhlMlPKc-2Z9CdvRgOkUp6hnZMvMDSjwZCa1htLXcyEFUL3RtupLi0rmzo_QclS72kH0BEoUlHt8ousO3KwYR7JKcM7YGbFGKuZwrUeo9Y0Lt-l-vD9nJ_hDrR-4FzQ5perWM6-uXs_4X_yPOTa6VAS6EOnufGBX9-Tc5Z8HGYS0R4Lk6FHN8J-uq47o1ZwkPTE9FatD8k3GQMVWNWmdhfzf6TgcDpB1LF-e7dKzQiPtrv7avOt2vS8gfF3A2_yRxtigrU2Uz9xwTSQJeoyiYdzVXWiU27Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1efb3a2f0.mp4?token=B1yG8RgMorx6RDXqVgcuFG9vHkyNQH2Ef3xjNAYLzM4dKoTIAn8guCRhlMlPKc-2Z9CdvRgOkUp6hnZMvMDSjwZCa1htLXcyEFUL3RtupLi0rmzo_QclS72kH0BEoUlHt8ousO3KwYR7JKcM7YGbFGKuZwrUeo9Y0Lt-l-vD9nJ_hDrR-4FzQ5perWM6-uXs_4X_yPOTa6VAS6EOnufGBX9-Tc5Z8HGYS0R4Lk6FHN8J-uq47o1ZwkPTE9FatD8k3GQMVWNWmdhfzf6TgcDpB1LF-e7dKzQiPtrv7avOt2vS8gfF3A2_yRxtigrU2Uz9xwTSQJeoyiYdzVXWiU27Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آئودی دیگر فقط ظاهر جذاب ندارد، بلکه حالا پیشرفت و کارایی هم به بخشی از هویت آن تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/677005" target="_blank">📅 17:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677003">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
استقرار تجهیزات هوایی ایتالیا در عربستان
اویشنیست:
🔹
جت‌های یوروفایتر، یک هواپیمای هشدار زودهنگام، سامانه‌های راداری و ضدپهپادی ایتالیا در عربستان و برخی کشورهای منطقه مستقر شده‌اند. همچنین ۷۰۰ نیروی ارتش ایتالیا در عربستان، کویت و بحرین حضور دارند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/677003" target="_blank">📅 17:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677002">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/677002" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677000">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_b39yhVg2EWaCYud-I1Ud88gG1pRDbJuxEUGYvaG6yZ08K3VXq4x6f9xAemsQZZimsSCFJQBknMv_T8jbFQbv4SEPB3CLR0GVABAz8tS_I6Pi1JEx4WA2Bmvmq8791y7kWw14C3V1G8o84rO3coG2DSuRW23nxY-FoKPWWajuJgCZjkrDUwK0wGK5tlrGy9gtQMpBmt9a3AKOHF53P05wUxiWkAcGLAeQE2lZZAfNPIdT2mxUbQbT7oSd65_m3sBJT5lMI82NHYZMOuH2x_RdZflcrbqoOYa24izdLDxog_NLz8SEbf4L7vHN9r1TJMgh9720fl4PaDWSyYpgRbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰ درصد برنج دنیا را این دو‌کشور تولید می‌کنند
🔹
بیش از نیمی از برنج جهان تنها در چین و هند تولید می‌شود؛ دو کشوری که نقش تعیین‌کننده‌ای در تأمین غذای میلیاردها نفر دارند.
🔹
برنج یکی از اصلی‌ترین مواد غذایی در حدود ۳۵ درصد کشورهای جهان است و غذای اصلی بیش از نیمی از جمعیت کره زمین به شمار می‌رود.
@amarfact</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/677000" target="_blank">📅 17:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676999">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سگ متوهم: حملات ادامه دارد و اوضاع به نفع ما پیش می‌رود
🔹
دونالد ترامپ درباره جنگ علیه ایران مدعی شد روند تحولات به نفع آمریکا پیش می‌رود و این کشور با ادامه حملات، طرف مقابل را تحت فشار قرار داده است؛ او همچنین گفت این روند ادامه خواهد یافت تا شرایط به نفع واشنگتن تغییر کند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/676999" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9d671d57.mp4?token=ia8H-_LPzYbMmS-FB6P1eb9Um4viqqwA2go_fgDycaxn7Iu9KhpEt0c0Ig2ofjS1PHkua0hceAUxnu3WCMYXIA0twh-gVR0eCeg-WIUwabclsGXB_rn2a8nvKvQn4fVoNajYpxwp6N9HM07yR5tO27tpVIEGayxrfYTOJMz9i1ZjPKF13Ja_0b2i9ntUZ0j5yVgL-03T2DpX0yKzBQpDuQ473g9ktSSaLbo-Dg6dcfsfKP_ghZi9YJ6EFU5kUNmf6cJ4d2QNVF9zU7VV8XdRg7JhPzh9USHO2lFRTcUmsPkCMOZeRECI3Xc3Gc4ZFedCRVSXsUCZq01DB5zKVReFww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9d671d57.mp4?token=ia8H-_LPzYbMmS-FB6P1eb9Um4viqqwA2go_fgDycaxn7Iu9KhpEt0c0Ig2ofjS1PHkua0hceAUxnu3WCMYXIA0twh-gVR0eCeg-WIUwabclsGXB_rn2a8nvKvQn4fVoNajYpxwp6N9HM07yR5tO27tpVIEGayxrfYTOJMz9i1ZjPKF13Ja_0b2i9ntUZ0j5yVgL-03T2DpX0yKzBQpDuQ473g9ktSSaLbo-Dg6dcfsfKP_ghZi9YJ6EFU5kUNmf6cJ4d2QNVF9zU7VV8XdRg7JhPzh9USHO2lFRTcUmsPkCMOZeRECI3Xc3Gc4ZFedCRVSXsUCZq01DB5zKVReFww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز قدرتی است که کم‌کم از بین می‌رود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/676997" target="_blank">📅 16:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7mTfXGq1QO_AHzNKHr3OMTEDsCuMyhnVLjm7Pix3E8FUk87fByiwiMNAi7r6Z1_Xd5YfbzN4zdbpVoE6DcbZksxl0GPnOeFIdWGL0Puu3CLsn6BqOZUTtKswEy3c91GPSC4jZQ6DUHom3JSDfbMf9Wf8lQSrFTuSO3aWEO6-Sn1SZaWJbHcs_oeIGQt8XC52wvfa6Hyl1An9rJXf4VCBH6frdK3yHkJ0_Q1U-gMjUhymp3H63TT9GkPMWycdXqxJBXZRTvj9-DxnWh9J88QmcQzvuI1-GPijNKhWlxWuS5ByiK3GPbsRFikV7Z3hedaWJmIY-dIHxnAX0_qjQ40KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به علت اقدامات تجاوزکارانه ایالات متحده، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد
نهاد مدیریت آبراهه خلیج فارس:
🔹
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/676996" target="_blank">📅 16:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gld0LvNdc07QBBF6MODKC9QE_4D8xaNb9XZI-DxcvhpL8rOhXN2s7Y6RPjUj4f0GhdE0QpHH53oFP6nKKx1r5kgTGVojLdUdzb8LxvzUb0g408PPyVuzTuC06QVgvpU-JbH3WJOEqL19Fi9jxpGL1i2luuXumJbAuzvAoDaUV9XUJ6s1ToWXThJgmivIF0N_Pcjhv1jvpV0-S3yU47KBfnhAJPmNLPmId0LkmdidttUimSZDsqmcTszl5aYsw-amwHYig_DqrB648n6sGBSMLrv8_g_bhj_kv1ACQcbc2Y9Ma534A2bSE3wNFnEMFdCjhYH0G0D-gTlmVPTtT1vYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت یک فعال رسانه درباره‌ تاثیر هوش مصنوعی بر کلاس‌های دانشگاه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/676994" target="_blank">📅 16:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb1198ee1.mp4?token=NfqAIh6rK-OoI4cl831zFX2DTTEWHJFjSyfKFrXuAghT9B11JvQLKPl32NJycaEKvqK52ebbCy8GsgkXVmGB0DQa4E5FG97j2ZCbk3yzgdcOx6zXfQQT3rzfy4ziwyfwKsP40LIeulSgLRjvoMfTpNOQ8b7ps2TQld7j24Q-9xJqlqH19b_DrNYOoy4FfFUL5pOUO6gLVs8h4MilAgDubwU6BdPIYMGHm_SvfHgb9ddncsD0_EAiKjpPvu5FfGkOCyBBope2SU0CL4VDhJK-9BACnuiCa11lq1yfbbLRNQE_F3ss8xQSfmbXndxGbstIm8zHHIihFlC01itC1o2TmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb1198ee1.mp4?token=NfqAIh6rK-OoI4cl831zFX2DTTEWHJFjSyfKFrXuAghT9B11JvQLKPl32NJycaEKvqK52ebbCy8GsgkXVmGB0DQa4E5FG97j2ZCbk3yzgdcOx6zXfQQT3rzfy4ziwyfwKsP40LIeulSgLRjvoMfTpNOQ8b7ps2TQld7j24Q-9xJqlqH19b_DrNYOoy4FfFUL5pOUO6gLVs8h4MilAgDubwU6BdPIYMGHm_SvfHgb9ddncsD0_EAiKjpPvu5FfGkOCyBBope2SU0CL4VDhJK-9BACnuiCa11lq1yfbbLRNQE_F3ss8xQSfmbXndxGbstIm8zHHIihFlC01itC1o2TmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراکش با هدایت مهاجران به مرز اسپانیا، سناریوی آمریکایی-صهیونیستی را اجرا می‌کند
🔹
ویدئویی بحث‌برانگیز از مرز اسپانیا منتشر شده که گفته می‌شود انتقال مهاجران از سوی مراکش را به تصویر می‌کشد و واکنش‌های گسترده‌ای به دنبال داشته است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/676993" target="_blank">📅 16:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تیزر قسمت هفدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید سبحان حسینی‌نژاد که در اثر سانحه‌ای ضربه مغزی شده و بخاطر شدت بسیار زیاد ضربه، امیدی به زنده ماندنش وجود نداشته اما ایشان بعد از مشاهدات اموری در برزخ و همراهی های مادر در هنگام دعا در حرم مطهر امام رضا(ع) توسط یک شخص سبزپوش در برزخ، ۳ نکته برای زندگی دنیایی آموخته و به دنیا بازگردانده می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید سبحان حسینی نژاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/676992" target="_blank">📅 16:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206c453fcd.mp4?token=wBD56B_oILE63rG2pcdC-hD7qFXAijvtmx3epwQx8AoIIuXBXzBQXtU24Kx-3HNFqiA-lYsFvlnVKEmawiuo_xddQ80Ow1A0DL7qy3V42mq1_nh6q1Rm63MHKKwxW5UftiYbd73b5Kv6S5VRO3v9JJa-HreT6XgkcLUlViI4CLpscHEHNG6nfpX0eAZhGuTZXI8LOpB9-oiGig31kXnNPcGfYK0dd-CXYHZsmO5YgOO7AdPR31HvjScfyjpWBBJz936Fu4lWshWp1gaS5WzIBOQcj02gtjqURZHOYc6K2DbVnv3tq9Q49ucmal4Tok4R5QaoOiS0wrLVdFEtNZzWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206c453fcd.mp4?token=wBD56B_oILE63rG2pcdC-hD7qFXAijvtmx3epwQx8AoIIuXBXzBQXtU24Kx-3HNFqiA-lYsFvlnVKEmawiuo_xddQ80Ow1A0DL7qy3V42mq1_nh6q1Rm63MHKKwxW5UftiYbd73b5Kv6S5VRO3v9JJa-HreT6XgkcLUlViI4CLpscHEHNG6nfpX0eAZhGuTZXI8LOpB9-oiGig31kXnNPcGfYK0dd-CXYHZsmO5YgOO7AdPR31HvjScfyjpWBBJz936Fu4lWshWp1gaS5WzIBOQcj02gtjqURZHOYc6K2DbVnv3tq9Q49ucmal4Tok4R5QaoOiS0wrLVdFEtNZzWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه تعاملی تلویزیون اینترنتی مدار آغاز به کار کرد
🔹
«شهروندمدار» عنوان برنامه تعاملی تلویزیون اینترنتی مدار است که هر روز به انعکاس پیام های مردم و پیگیری آن‌ها از مسئولان اختصاص دارد. دغدغه‌های معیشتی، گرانی، مسکن، اشتغال، حقوق کارگران، تولید، خدمات عمومی و مشکلات روزمره تا هر مطالبه‌ای که نیازمند پاسخگویی مسئولان است.
شهروندمدار و سایر برنامه ها را اینجا ببینید
👇
https://youtube.com/@madaar_tv?si=e1sVJ4219UwoCUzD
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/676991" target="_blank">📅 16:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676989">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY-oaMnKYekXWQ_HuYdwORVr5YK5KRUBWGFXknvN3X2WuVJo8Svu9cOMjq1kivQFT9Iy57iz67mpLbFXAeCaouZLefQMavCTmYPQU876zt5nIXZc_FJixtFTzrT5d1acVMxFoTXx69Fmhcl5mxPGi88C5QEfLdEVNgpCsw3Smz3YBrepEULPs6JqC9hv7Pj4UVQ_RHVCW0T1ZwepaGKDZQ76rJiF81mVr7hlVWlK46z7-3_T4H0YeZKVoLFRdHVVWiDCfM0RQKgZDHHIUOb3ZsjiY89JsRDBBXrhQ_b8rWREGtglHg1GuV0BK4ZoZqzLnVPDud5jdrYojtCcGf63fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آیا آماده‌اید تا به کربلا سفر کنید؟
✨
▫️
با پویش «زیارت به نیابت»، شما می‌توانید یکی از ۱۰۰۱ نفری باشید که به  کربلا سفر میکنند .فقط کافیست عدد ۲ را به ۳۰۰۰۱۱۵۲ پیامک کنید و در این راه نورانی شریک شوید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/676989" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676988">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
حماس: فقط سلاح‌های سنگین را تحویل می‌دهیم؛ آن هم با این شروط
🔹
حماس اعلام کرد با مرحله دوم چارچوب آتش‌بس موافق است، اما تأکید کرد تحویل سلاح‌های سنگین تنها در صورت خروج کامل اسرائیل از غزه، تشکیل کشور مستقل فلسطین، بازسازی غزه و پایان تجاوزها انجام خواهد شد./ صابرین‌نیوز
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/676988" target="_blank">📅 15:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8719c4f62a.mp4?token=pLEibZaRp8t3LaEeZW72sfnv313VLRQ1qP3Awk4HWiXNBdpw5mBc1G_FndMWeDWWchgbQ5AYjL6ggQbnPqyDMNrfjNrC9IlIlcrPrmdwmB8adLzT6mCqQVbfXU1mZQLkIpUDr6X66Xc5NO7fhuKGbPc3AffLD436N3e1uhlexVPeJ-w5A7PSPbwQohx24GkqbxELyrMRId2M9ZPbhi3yYb_greso1rx75TSG5wDGUF1NfpFlJCDZf56KURyGP6kbr9buE_t85vOr0faPayi-hBARVon9ElsBH1j7gNwbf_SdWc9SyvDqTWdPNBPN5qcZCXg1SAXFZ95T6SF91XobsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8719c4f62a.mp4?token=pLEibZaRp8t3LaEeZW72sfnv313VLRQ1qP3Awk4HWiXNBdpw5mBc1G_FndMWeDWWchgbQ5AYjL6ggQbnPqyDMNrfjNrC9IlIlcrPrmdwmB8adLzT6mCqQVbfXU1mZQLkIpUDr6X66Xc5NO7fhuKGbPc3AffLD436N3e1uhlexVPeJ-w5A7PSPbwQohx24GkqbxELyrMRId2M9ZPbhi3yYb_greso1rx75TSG5wDGUF1NfpFlJCDZf56KURyGP6kbr9buE_t85vOr0faPayi-hBARVon9ElsBH1j7gNwbf_SdWc9SyvDqTWdPNBPN5qcZCXg1SAXFZ95T6SF91XobsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران قدرتمند اتنا؛ شکاف جدید در کوه آتشفشانی
🔹
فوران قدرتمندی از کوه اتنا در ایتالیا طی شب آغاز شد و شکافی جدید در ارتفاع حدود ۲۷۰۰ متری این آتشفشان ایجاد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/676984" target="_blank">📅 15:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676983">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
لحظاتی منتشر نشده از دیدارهای صمیمانه خانواده‌های معظم شهدا با رهبر شهید مسلمانان جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/676983" target="_blank">📅 15:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676978">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc07cde495.mp4?token=Cqr19pd8rxCrzFCQKIIwm5Paz8x-PpOLzWVPps-EDmBK9Pj-ygun2zjoAORxvR4Nc4Q6L8riIayEhlycneKlBrM9_BTcEfm7_jkScuaYqieWwvt0rWO6XcteKT5iYmHDTOqXhA1QAs-1bInr7tIourkoVP4KM1BvhKtU_OTNP0Rlk3HNEI-PwisN3nJzj4buulArHg5YJZf-4H6aL7amqgKaPbxfLVcpBVhhspMCRrg-JYtdAeTLiBKYGQ6SkTdrkWpj8NF7EzDVJ_jZOYV5lrvhRm3BCh5v-rl8e_gvl4k71IYzeUrWPQNT3NQDGgTv9j68QcjPNIz3lpJ81xW9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc07cde495.mp4?token=Cqr19pd8rxCrzFCQKIIwm5Paz8x-PpOLzWVPps-EDmBK9Pj-ygun2zjoAORxvR4Nc4Q6L8riIayEhlycneKlBrM9_BTcEfm7_jkScuaYqieWwvt0rWO6XcteKT5iYmHDTOqXhA1QAs-1bInr7tIourkoVP4KM1BvhKtU_OTNP0Rlk3HNEI-PwisN3nJzj4buulArHg5YJZf-4H6aL7amqgKaPbxfLVcpBVhhspMCRrg-JYtdAeTLiBKYGQ6SkTdrkWpj8NF7EzDVJ_jZOYV5lrvhRm3BCh5v-rl8e_gvl4k71IYzeUrWPQNT3NQDGgTv9j68QcjPNIz3lpJ81xW9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدونستید پشه‌ها اینطوری به دنیا میان؟!
🔹
چرخه زندگی پشه چهار مرحله هست؛ تخم، لارو، شفیره و پشه بالغ که همه این مراحل ۷ تا ۱۴ روز طول میکشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/676978" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979329654.mp4?token=fxFsFiSusDt37IIClT9cGZdGIqTsNuXt8ErYBJBtZkdGDikBGcZSuxki3RnFE7cmrky9aiYrNW8KHq_qcUVrdkg7osojfGQ4qeYO4U6kbPeQtPEVprz6X73iTj9r3xf2lIH-LAgIYAZtUxrbhClQTiFClsacU0t03jHoH-5GwT5dyTXYGpciUPERTVG2zMdpmH6RZjOzoZxa-kmAiXVcrY0z1v1O-U0wYTAEq5O9aDjkJSRPXwEWplF-VUXpBYa9eMk36apNqdY751IPDmgSBg23wtWDSNixOT4_wTBP-2xmWqMn3PNCCO64rpuAYKPRL0kbt1Um5AAVWBjuN0TJAiwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979329654.mp4?token=fxFsFiSusDt37IIClT9cGZdGIqTsNuXt8ErYBJBtZkdGDikBGcZSuxki3RnFE7cmrky9aiYrNW8KHq_qcUVrdkg7osojfGQ4qeYO4U6kbPeQtPEVprz6X73iTj9r3xf2lIH-LAgIYAZtUxrbhClQTiFClsacU0t03jHoH-5GwT5dyTXYGpciUPERTVG2zMdpmH6RZjOzoZxa-kmAiXVcrY0z1v1O-U0wYTAEq5O9aDjkJSRPXwEWplF-VUXpBYa9eMk36apNqdY751IPDmgSBg23wtWDSNixOT4_wTBP-2xmWqMn3PNCCO64rpuAYKPRL0kbt1Um5AAVWBjuN0TJAiwrIAj43dQMee7JQKLfKfUOj4mgBQ2Mq8rl74j2hfpH6CZFDsy4h_ytVTMtZArBoXdKv41fYkWUcrK89YNET3moc_Vtt5dXZ4QKaSvvApM2Z2_d-sErEqH75SZTex-eareWfVPgHNpzdpESGYNIOrtmco5XXRSk38gLVxm-yHZ3S1b4GT97JSU6cqvLcCOQAsF3p29kvINjLKZtsxdd1RFcIj78fAFhKrDKG5r72hjlOvTvJlNfJXwOybhY5AoWt686zqWACejPaNvA08809MuO8MBbX8ksnxs6hfnW54Ws7ly2tWjSGr2hz8qJwe75P0HBb--hdWiRpcSz7NB-wf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منافق کسیه که پشت شعاراش قائم میشه!
🔹
بریده‌ای از فیلم سینمایی «لباس شخصی» که در سینماها به نمایش درآمده است</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/676977" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676976">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f935398a4c.mp4?token=QXVyA2E4WSfPGkeiMw8tLYTrnB1WJHuhmTYssF3crvbpjhGA_ys8CWurQjoEHd4C0YrRvC4NTYrlzoBVHdcObL79ixrOg0NDSUa2HujS2cp9SQqVQI37u-G8TrD2DgYQFetKRkwMyYtx3n3Bqsu4PyKsDjBRWqk2WnYg6dhQii02jBPL0hvx9vRawjyePSD1K7c1KNgkc-4tbklayxzkNh7imUcDKAM2np6sG91VhJ1rkLtpcmz-Eht1VTcCgj76mybhL15VHnKbxOKvJ3ROQqKAEc6Lljz2CWKUwFpzfryj8AJ1yPYiFk21qNOGYBn76cJlFGAgeGuJgbqo8hUArg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f935398a4c.mp4?token=QXVyA2E4WSfPGkeiMw8tLYTrnB1WJHuhmTYssF3crvbpjhGA_ys8CWurQjoEHd4C0YrRvC4NTYrlzoBVHdcObL79ixrOg0NDSUa2HujS2cp9SQqVQI37u-G8TrD2DgYQFetKRkwMyYtx3n3Bqsu4PyKsDjBRWqk2WnYg6dhQii02jBPL0hvx9vRawjyePSD1K7c1KNgkc-4tbklayxzkNh7imUcDKAM2np6sG91VhJ1rkLtpcmz-Eht1VTcCgj76mybhL15VHnKbxOKvJ3ROQqKAEc6Lljz2CWKUwFpzfryj8AJ1yPYiFk21qNOGYBn76cJlFGAgeGuJgbqo8hUArg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی تازه منتشرشده که گفته می‌شود مربوط به لحظه حملات پی‌درپی دشمن آمریکایی به دبستان شجره طیبه میناب
است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/676976" target="_blank">📅 15:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/676975" target="_blank">📅 15:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676974">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8225375f0.mp4?token=X_NVhdmJ2me-PmuRC5PfwM5TsulV4hh5ywokaYltwk_Qu_o6XK_vsJDLwYceoWSbFwvqEWC3Il7Xovw5LAS07Lw8jSt2k4_Crulb6EYPYyYFCC76sUNwswsqtg5tMFyL5irDtIftLXiU-Rkt9NfSWuyvLYOVXnfz5xS68mp4Fw2rYloh3Jfr8_SP3kBlR_YJG_USdVN7kYNnnQAwTTb1U1XPO5374TPNGB6PlexmlSRfPiSRQ__JVGZYs_CUfKMnFPBw8aKHQ8rzbe5xKUIyoCyQvRObUNpb0Cs1OOcyzoOp9ufQTbnSSgpDUcI-4QnmWF49N3a2fTryY6hAgQCf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8225375f0.mp4?token=X_NVhdmJ2me-PmuRC5PfwM5TsulV4hh5ywokaYltwk_Qu_o6XK_vsJDLwYceoWSbFwvqEWC3Il7Xovw5LAS07Lw8jSt2k4_Crulb6EYPYyYFCC76sUNwswsqtg5tMFyL5irDtIftLXiU-Rkt9NfSWuyvLYOVXnfz5xS68mp4Fw2rYloh3Jfr8_SP3kBlR_YJG_USdVN7kYNnnQAwTTb1U1XPO5374TPNGB6PlexmlSRfPiSRQ__JVGZYs_CUfKMnFPBw8aKHQ8rzbe5xKUIyoCyQvRObUNpb0Cs1OOcyzoOp9ufQTbnSSgpDUcI-4QnmWF49N3a2fTryY6hAgQCf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی روحانی عراقی به دلیل شباهت ظاهری به رهبر شهید آزادگان جهان در فضای مجازی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/676974" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/064113fb7c.mp4?token=pJ5a2d2IH9KxeL4oYYtASatjYO3McEXT19PoZqs40ufM9K1_UjHSCqZn6YDpmDAwPcZUOojIwfMmgbVJ_SF_OoMVpYEwhACdUwiMTRaXuAxrpVYPxLZ6DWXKaSS5jC4jMW5v5hnoYu3vTE3FQkRMKanf8pdqI-g42lh_6HrdSNn4vLABOfAt9vhjcEJNWYYqbwWpvCoNF0Bna1golnFPoAOYqRC_oq5YwzE-AJFOWG_vT1wqLjgdpXhgzMNDu2SESor6Q_QD9s7ZUaUq_FgmGwJ_Ozm1W5xb6274NQ26ZEWkRkicezzQ_ysWpwDaqA5TxCWD4HO_B7utqquBlU6o4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/064113fb7c.mp4?token=pJ5a2d2IH9KxeL4oYYtASatjYO3McEXT19PoZqs40ufM9K1_UjHSCqZn6YDpmDAwPcZUOojIwfMmgbVJ_SF_OoMVpYEwhACdUwiMTRaXuAxrpVYPxLZ6DWXKaSS5jC4jMW5v5hnoYu3vTE3FQkRMKanf8pdqI-g42lh_6HrdSNn4vLABOfAt9vhjcEJNWYYqbwWpvCoNF0Bna1golnFPoAOYqRC_oq5YwzE-AJFOWG_vT1wqLjgdpXhgzMNDu2SESor6Q_QD9s7ZUaUq_FgmGwJ_Ozm1W5xb6274NQ26ZEWkRkicezzQ_ysWpwDaqA5TxCWD4HO_B7utqquBlU6o4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار درباره یک سناریوی خطرناک/تلاش برای ایجاد جنگ میان ایران و کشورهای مسلمان
مایکل یان، عضو سابق ارتش آمریکا:
🔹
رژیم صهیونیستی با حملات پرچم دروغین به زیرساخت‌های کشورهای مسلمان خاورمیانه، به‌دنبال شعله‌ور کردن جنگ میان ایران و دیگر کشورهای مسلمان است.در لبنان هم سعی دارد جنگ فرقه ای ایجاد کند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/676973" target="_blank">📅 15:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676972">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb384c4485.mp4?token=hW2eMzD990EHuvvSvmNN5J660zmKICRBkWe6EExDT6U6qRcWWnX23dRKoQ5NlxpauJOMpJ2ZNpg1py4Ha16BtiOebTIRkN2xEyp6qnbyrR1xfp9-clvkgRvNoJl5P6DksK-YIffd1eOH86_N_5C09bQS1vjjtV3O7Q3xsooFty0uF4XBd_Pd4xevfjPp_nUOm_vCs5lPM3hAIDD46mIElBQr98H3W8lzeUbV966ALkNT06GFUB4z_5l9itFAs97wsrFRjWdOEr7Qfu1hCXfNw0zLt7cQDYj1tYpV8xaRzIG5KS4GwGdwlNYe9IYfbVhZichr6_2kCCQRh1qhMTMjLbmEIB34sfHE3L_ZhEwX5oX1gY6fufUrBUtzYHD_B9iu3UlQaaXo5AJsJeB_NWpnckPSPLLMb6BSsz1jBxamCPOtX0GDt0J4pW7AzDLA2h7K7BcoBsDzE0bJzO19wGZ0EsijV8kknVVcwNp0_uAzty9LhtANdd1DS6Utw-NtTVMHyKPsvgd7NWW1hq0iyHLD2cDKXuY0wkRVhnoCrneceRcFynVygSg-hQIc56hKXlhYsTH0xo_Ku768BF5ahbw37Vn-mBQIcS7661wJNHupkiPZcuiRjdcdzNoEF8jxQ6c-cRmXO7si1gaEJqJfHLb-NlluBreu2_fG8tBFNUuSb24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb384c4485.mp4?token=hW2eMzD990EHuvvSvmNN5J660zmKICRBkWe6EExDT6U6qRcWWnX23dRKoQ5NlxpauJOMpJ2ZNpg1py4Ha16BtiOebTIRkN2xEyp6qnbyrR1xfp9-clvkgRvNoJl5P6DksK-YIffd1eOH86_N_5C09bQS1vjjtV3O7Q3xsooFty0uF4XBd_Pd4xevfjPp_nUOm_vCs5lPM3hAIDD46mIElBQr98H3W8lzeUbV966ALkNT06GFUB4z_5l9itFAs97wsrFRjWdOEr7Qfu1hCXfNw0zLt7cQDYj1tYpV8xaRzIG5KS4GwGdwlNYe9IYfbVhZichr6_2kCCQRh1qhMTMjLbmEIB34sfHE3L_ZhEwX5oX1gY6fufUrBUtzYHD_B9iu3UlQaaXo5AJsJeB_NWpnckPSPLLMb6BSsz1jBxamCPOtX0GDt0J4pW7AzDLA2h7K7BcoBsDzE0bJzO19wGZ0EsijV8kknVVcwNp0_uAzty9LhtANdd1DS6Utw-NtTVMHyKPsvgd7NWW1hq0iyHLD2cDKXuY0wkRVhnoCrneceRcFynVygSg-hQIc56hKXlhYsTH0xo_Ku768BF5ahbw37Vn-mBQIcS7661wJNHupkiPZcuiRjdcdzNoEF8jxQ6c-cRmXO7si1gaEJqJfHLb-NlluBreu2_fG8tBFNUuSb24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید بشیر حسینی: آمریکا با ترور رهبری، پدر ایرانی‌ها را به شهادت رسانده و ما با آمریکایی‌ها پدر کشتگی داریم/ به کمتر از محو اسرائیل و آمریکا راضی نمی‌شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/676972" target="_blank">📅 15:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676970">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDydsd6GJhoEv7h_plC8tGhT4B0rCci3qQaRfZvCzyV4Oj_-oxFyvEWTzat49UfnODCdzQgipiTDiscj8RyA4VvbClfmRksvdUI2cKcfRrSzP2vs_Y6NgTnMhFf94GFo7hFKLftvZCCAQOj_orDZl-TrbQ58BEiBHp0arIveOII7wUbSRokCd5pATNNRcU5TOeHmS87aW1Q1-7PngDeQcxdU130U01Tykya9Lp94Q6uM7EIrxKsGnCYrorHKGHV-aZd5xb12FbWrCp7Jw-KiT2gkPqrtI0fMaPAjoNHir7fW4TgHKkfaef2Yg4y5U2CdlxYDlap9PpFJZWGt1SM1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن آماده رونالدو در ۴۱ سالگی؛ قاب پدر و پسری کریستیانو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/676970" target="_blank">📅 14:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676969">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuHq9e1ii8V2InJhjywdq94Pntz-GSbwANOXN_ryoDNgrJVBGU41vOFUhxI0psat2Rgz5qDjFMPqsl4frZkhRvXVuL7-X83prkfU9tdZc9EIM0YvTBnDVCSOJ78fIAcEGHES8VRDJB0n05A90k8f0thynJxYx22nOget9o0TUIv6TOmxWOL3vZZKffqn6EbSFSkK1xyn1ZmXpy8lQwlDqVRdZiMAXGFrYiufj81GQopmSEQj3pvazQzD-Iw9Brd4wG7_uog9PZhq84gMYlJPfuESVV_ckl2nevvRgg897vWfP__dErk3IVuJQMBJsqSuPpdpvAokOpJG0E54_SPB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محاصره زمینی ایران؛ طرح جدید آمریکا و رژیم صهیونیستی؟   تلگراف مدعی شد:
🔹
آمریکا و اسرائیل در حال بررسی طرحی برای محدودسازی مرزهای زمینی ایران با همکاری کشورهای همسایه و افزایش فشار اقتصادی بر تهران هستند. اجرای این طرح، به‌گفته تحلیلگران، با چالش‌های جدی…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/676969" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676968">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBJFcFJt3_L-mUEtZN3J-DhNRKDTu8mL4tPuMyCshsPTHUhl7tMjwi8NkXvAncQ6qjS6N1aykOmiVkuY4hiFbVmntq4SeTzjdYdR7UirhhZr_4Mw54ornj8JIbwady1-2zMDNoWdDvkITShbrKQZwmKAfl1Mg-kaVEUXrHqkjy10nvei5s442YrEKP9f_3CNFvQql4qXwUQQ5XpYV0urnPXUvMLfyyfQJ2fzIpCeP0EmwEPAHesN7dGm-LtZraBYgWkHSN8Ny10Q3Njp60UcLNO4ouLivX74ic3sujd16W_vOgBMxETZZBIqCgPaaqDTbcPRpBC_1kRqQG7ZnJ5ZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعی گسترده اینترنت در ترکیه
نت‌بلاکس:
🔹
داده‌های شبکه از وقوع یک اختلال سراسری در سرویس‌دهنده اینترنت «ترک‌نت» در ترکیه حکایت دارد؛ رخدادی که همزمان با گزارش‌های گسترده کاربران از قطع یا اختلال در دسترسی به اینترنت رخ داده است./ سیتنا
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان ترکی دنبال کنید
👇
@AkhbareFori_TR</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/676968" target="_blank">📅 14:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676966">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e0b93dc5.mp4?token=B_LdCewGuuTK61Hhwsut1D8ptvCYM0DQJqUrpCjiiTvKCCvbPqfMfhRB_C5RIyQygFJnlXn_9Y10HIwze0YFo5lnBgX6_HhbQOeUWKpzawsdK2dafyv1DNyEo8W5jrZrOr2shb7DTfUuD1BqPsP00sevKFaV_K9-PEu74bmeaTvnj2vj-xyZAAxHExcsM2BIEyTKjKjpuimD7bBGMI5I1c0bHjgMo8e1iqipoIZjjikCmNwYo4wsnzK25olfg-E7t70ADIcrojUafgp-DIpU2aWQ62ynhvghqtKlFhs52yLzzN18ckzHqmXBaGau30SJD2SYcLiE7W87CsS_w5I1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e0b93dc5.mp4?token=B_LdCewGuuTK61Hhwsut1D8ptvCYM0DQJqUrpCjiiTvKCCvbPqfMfhRB_C5RIyQygFJnlXn_9Y10HIwze0YFo5lnBgX6_HhbQOeUWKpzawsdK2dafyv1DNyEo8W5jrZrOr2shb7DTfUuD1BqPsP00sevKFaV_K9-PEu74bmeaTvnj2vj-xyZAAxHExcsM2BIEyTKjKjpuimD7bBGMI5I1c0bHjgMo8e1iqipoIZjjikCmNwYo4wsnzK25olfg-E7t70ADIcrojUafgp-DIpU2aWQ62ynhvghqtKlFhs52yLzzN18ckzHqmXBaGau30SJD2SYcLiE7W87CsS_w5I1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کامیون‌های حامل مهاجران در مرز اسپانیا؛ ژاندارمری مراکش فقط نظاره‌گر؟
🔹
ویدئویی منتشر شده که نیروهای ژاندارمری سلطنتی مراکش، در حال تخلیه کامیون‌های حامل مهاجران در نزدیکی مرز اسپانیا، تنها نظاره‌گرند.
🔹
اسپانیا هدف طرح صهیونیستی-آمریکایی به‌خاطر حمایت…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/676966" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676965">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvdrJCZRU0q25Cl7GeihXRIc2jVRB-FXumzAGnoXNGb-3I_u1xKdNxIEga3Q-jfqVbNIAXGgatt7Np0pumIg96-6UJqBqud2MScnv4aT6u864t3H5OC5iaFVvOl-Gp0eE7eby9jT_1l1f5Sk77ONhET3YqKUsFXB2g6ofQr-eDSC3KecWEjrYuHEb7GRz0fBBOBo3Hu7TDnXg5L4JalOgdBVdgHrsPrKFMavcsXB597EMLCM0SwSWFMufdELQkrVK3CijQtdcemEvMPFPIyKVaoh5UGwzGy65vu75cH4ADeKKuxWKV5UyIC1y6UgG8sybi82ZJsLQPDpRul8djVvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه ویژه و متفاوت شهرداری تهران برای اربعین/ از توسعه زیرساخت‌ها تا توجه به نیازهای فرهنگی و اجتماعی
توکلی‌زاده، رئیس ستاد اربعین شهرداری تهران:
🔹
برنامه‌ریزی امسال بر پایه مردمی‌سازی، توسعه فعالیت‌های فرهنگی و رسانه‌ای، ارتقای کیفیت خدمت‌رسانی، مدیریت هوشمند، تقویت مشارکت اجتماعی و حرکت از خدمات صرفاً زیرساختی به سمت تمدن‌سازی انجام شده و تمامی ظرفیت‌های مدیریت شهری برای خدمت به زائران حضرت اباعبدالله الحسین (ع) بسیج شده است.
🔹
امروز در کنار توسعه زیرساخت‌ها، توجه به نیاز‌های فرهنگی، معرفتی و اجتماعی زائران اهمیت بیشتری یافته است؛ از این رو، علاوه بر استمرار خدمات عمرانی و پشتیبانی، استقرار ایستگاه‌های فرهنگی و مذهبی، اجرای برنامه‌های معرفتی، تولید محتوای فرهنگی و پاسخ‌گویی به نیاز‌های نرم‌افزاری زائران نیز در دستور کار قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/676965" target="_blank">📅 14:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676962">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eacdd6360e.mp4?token=rR-dCuptc_Lkp2bp7g996BzLC5jdqIM9wuxtUf7BQxeBXc1LURWinust6HauS0ij5FA7u6V4aTfB4Qk1o_WPYS4AZeyPwla4NMz8kP26o0UaWyFORn3dhAaOci9x-ooAZhk74ZQv3Foyz5VOLpdnacXHnN1HQsJXEZYBmDo6h0FCehrrG9CWAHAGg_2LfLZX5VSvnqCikHp8V_hY64B-7bEhdIQEBvvKRs6ZEx5f8xglQuj29O221aPLTIqH82ETBqQ5aWCb1h9kmn1oYnF7RLZWNq5ULDQ_ow-NM6BpTAKchRuXgq9VcsLpOMZ-X03G6KI-eCWs2OrUmoA4BCiBhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eacdd6360e.mp4?token=rR-dCuptc_Lkp2bp7g996BzLC5jdqIM9wuxtUf7BQxeBXc1LURWinust6HauS0ij5FA7u6V4aTfB4Qk1o_WPYS4AZeyPwla4NMz8kP26o0UaWyFORn3dhAaOci9x-ooAZhk74ZQv3Foyz5VOLpdnacXHnN1HQsJXEZYBmDo6h0FCehrrG9CWAHAGg_2LfLZX5VSvnqCikHp8V_hY64B-7bEhdIQEBvvKRs6ZEx5f8xglQuj29O221aPLTIqH82ETBqQ5aWCb1h9kmn1oYnF7RLZWNq5ULDQ_ow-NM6BpTAKchRuXgq9VcsLpOMZ-X03G6KI-eCWs2OrUmoA4BCiBhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی متفاوت از اربعین با ابتکار یک زائر ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/676962" target="_blank">📅 14:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676960">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a00a5bc9.mp4?token=mx-26vQWY7ueRxQFDNIP9MfQyknHzGftzSvCQZ8Hy5urw8CrxBAIWkxD_dFI9QN1zn1B0-wPrF2QKOh_9b37nvI-a5shtRE34Vwg9mWUWT3WTZsHTYpwPfPOqRYmzm43m03dN6WRVVcboPau7dv5n57lkL83psUZf1HT9n0ocPbxb9xNMsVU8scVVhpdTWd5sGHIFV_E2RQ8EcgRI2n98Ook8WHvSpBvY1WLUXEjxz6ScoTGoyMOxduIjliapAKx8s4HQwwVaKKYbCQiAORske-NZP8j605RV6n_Pn99SXLX2TZc5Q-QeDT3V_Rp-vKV8uLbe2e8ut4ciXvDXxZagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a00a5bc9.mp4?token=mx-26vQWY7ueRxQFDNIP9MfQyknHzGftzSvCQZ8Hy5urw8CrxBAIWkxD_dFI9QN1zn1B0-wPrF2QKOh_9b37nvI-a5shtRE34Vwg9mWUWT3WTZsHTYpwPfPOqRYmzm43m03dN6WRVVcboPau7dv5n57lkL83psUZf1HT9n0ocPbxb9xNMsVU8scVVhpdTWd5sGHIFV_E2RQ8EcgRI2n98Ook8WHvSpBvY1WLUXEjxz6ScoTGoyMOxduIjliapAKx8s4HQwwVaKKYbCQiAORske-NZP8j605RV6n_Pn99SXLX2TZc5Q-QeDT3V_Rp-vKV8uLbe2e8ut4ciXvDXxZagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران محل تجمع نیروهای اوکراینی توسط روسیه
🔹
وزارت دفاع روسیه با انتشار ویدئویی از هدف قرار دادن محل تجمع نیروهای اوکراینی در مناطق زاپروژیا و دونتسک با استفاده از بمب‌های «فاب-۱۵۰۰» خبر داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان روسی دنبال کنید
👇
@AkhbareFori_RU</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/676960" target="_blank">📅 14:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad9a3c862.mp4?token=lwCK9m9UpZrjypdKXLU2IShOODp7mB_4BrNT2Xl85OD6U2pAS9zvXUkHECxUS0dP3crdU8CnCwejGyGNJyGJx_nV6KOZvnGa4MxxDz8MeHN61xFYHzkAUHddY9tt3GQJ1FiINSwlAbHt55GpWTZp8ORKPgTxCCwLepB1eejUuvTHJ_yiXcOhH0EUQmGpzUu7sa72gNeLY1knOY9rg2AycJSAS9A8TUeOSKVz1ZVDHvYy-iBJWj4-WZRNohkRagLUzONjzYIuEUid4rZz8H7BSMMWKms5G7zQNIJyoNwyQAnnkUkdNh9o9OhMji4zn2yk4hstHioFcZzQEadcGVb8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad9a3c862.mp4?token=lwCK9m9UpZrjypdKXLU2IShOODp7mB_4BrNT2Xl85OD6U2pAS9zvXUkHECxUS0dP3crdU8CnCwejGyGNJyGJx_nV6KOZvnGa4MxxDz8MeHN61xFYHzkAUHddY9tt3GQJ1FiINSwlAbHt55GpWTZp8ORKPgTxCCwLepB1eejUuvTHJ_yiXcOhH0EUQmGpzUu7sa72gNeLY1knOY9rg2AycJSAS9A8TUeOSKVz1ZVDHvYy-iBJWj4-WZRNohkRagLUzONjzYIuEUid4rZz8H7BSMMWKms5G7zQNIJyoNwyQAnnkUkdNh9o9OhMji4zn2yk4hstHioFcZzQEadcGVb8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوربین وایرلس مگنتی A9؛ کوچیک، کاربردی و همیشه همراه!
با این دوربین جمع‌وجور، هر زمان و هر جا که بخوای از طریق موبایل محیط رو زیر نظر داشته باش.
✅
اتصال وای‌فای و مشاهده آنلاین
✅
دید در شب
✅
تشخیص حرکت
✅
نصب آسان با مگنت قوی
✅
مناسب منزل، محل کار، خودرو و مراقبت از کودک یا حیوان خانگی
❌
قیمت قبل: 1,598
🔥
قیمت ویژه: 1,298
⏳
فرصت خرید با تخفیف محدود، قبل از اتمام موجودی سفارش خودت رو ثبت کن.
https://memarket24.ir/product/brief/35151/180124/</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/676959" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c52b50ba.mp4?token=jlEbegbKmXZZ20CIJErxj6CFKVQ8P0gJoQIWlfyuO1UNzFdbTa-cORyC202BYfqvgqH7LzKuntW1sGPT-b4CLbdsTwRHE4FBuulkclkLF6Efr6herLYNiHJlL9As8FBv0QclUq-rh8BbM0PMhPqnOCsXRA_nB9ZuVT1io4zp3Kl-2sTuoRkiNp8rQw_lP1SWPpTEPMJZ7bF2P26S3TToilnIc210-4w8p1adODoG9xbrkXUVmq-wLc8LAbUfTvxVYRxWD5xlPqq8lbyWGiwewk-pKrdb5BQ9alI2EZ5oweVb6LCmU6xV47ANXoy1FowWl7kXD4gaxxgvhCIuEclvlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c52b50ba.mp4?token=jlEbegbKmXZZ20CIJErxj6CFKVQ8P0gJoQIWlfyuO1UNzFdbTa-cORyC202BYfqvgqH7LzKuntW1sGPT-b4CLbdsTwRHE4FBuulkclkLF6Efr6herLYNiHJlL9As8FBv0QclUq-rh8BbM0PMhPqnOCsXRA_nB9ZuVT1io4zp3Kl-2sTuoRkiNp8rQw_lP1SWPpTEPMJZ7bF2P26S3TToilnIc210-4w8p1adODoG9xbrkXUVmq-wLc8LAbUfTvxVYRxWD5xlPqq8lbyWGiwewk-pKrdb5BQ9alI2EZ5oweVb6LCmU6xV47ANXoy1FowWl7kXD4gaxxgvhCIuEclvlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی میراث اشکانیان به دست امریکا نابود شد!
🔹
شهر باستانی هترا، یادگار دوره اشکانی، پس از قرن‌ها مقاومت در برابر جنگ‌ها، در سال ۲۰۱۵ به دست داعش آسیب دید.
داعشی که پیش.تر ترامپ نیز، اوباما و کلینتون را به نقش در شکل‌گیری داعش متهم کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/676958" target="_blank">📅 14:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77b8a7a73.mp4?token=DCiaKIAGZskF0QBDLr_ZMXL9KFwvxU4eneEII8C6hH9QemXle1yo_SLXk6K3TBdmkY2nMaWRs_LIPunpb5Zw3GKYs32nr7pUqV6coAlAb_yfBrtcZQjUW9jr0BoRVvCaOURzarADKHn9I6Wl53XbWGNVLho0pgb32cuUnIfDqpRvZ81FC204x5se6HXq7NvpQc43h_sx4X2P_ocUDxw5ccten0pGbf1dXy89uM5Zat4jtO6iNpUhb-zbd5HK_7lRuXvx5ackBSAGLs4T-kzf90zLx0dcZJfTmARxVqisjxBHuTXpcCQzMgaU3J7hqMnIpYZ5sAjfap789QpbwxWpUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77b8a7a73.mp4?token=DCiaKIAGZskF0QBDLr_ZMXL9KFwvxU4eneEII8C6hH9QemXle1yo_SLXk6K3TBdmkY2nMaWRs_LIPunpb5Zw3GKYs32nr7pUqV6coAlAb_yfBrtcZQjUW9jr0BoRVvCaOURzarADKHn9I6Wl53XbWGNVLho0pgb32cuUnIfDqpRvZ81FC204x5se6HXq7NvpQc43h_sx4X2P_ocUDxw5ccten0pGbf1dXy89uM5Zat4jtO6iNpUhb-zbd5HK_7lRuXvx5ackBSAGLs4T-kzf90zLx0dcZJfTmARxVqisjxBHuTXpcCQzMgaU3J7hqMnIpYZ5sAjfap789QpbwxWpUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روز دوم تهاجم مراکشی‌ها به اسپانیا
🔹
این ناآرامی‌ها بدلیل مواضع حمایتی دولت اسپانیا از فلسطین، لبنان، ایران و محور مقاومت بوده و این پروژه با هدایت صهیونیست‌ها در این کشور کلید خورده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/676957" target="_blank">📅 13:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676955">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
محاصره زمینی ایران؛ طرح جدید آمریکا و رژیم صهیونیستی؟
تلگراف مدعی شد:
🔹
آمریکا و اسرائیل در حال بررسی طرحی برای محدودسازی مرزهای زمینی ایران با همکاری کشورهای همسایه و افزایش فشار اقتصادی بر تهران هستند. اجرای این طرح، به‌گفته تحلیلگران، با چالش‌های جدی روبه‌رو است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/676955" target="_blank">📅 13:45 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
