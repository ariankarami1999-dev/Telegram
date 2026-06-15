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
<img src="https://cdn4.telesco.pe/file/uCVdvWSDkQODwAOmJb-g6QbP0m0HQFHmxtnM6sCoAA1bxKjjXG_8093pOXGRdESjfMyLPAkoII7rPicFnG47zm36b6gTLarRFlm7iR5yWABDvznaYOVpu5x_2nTR7zftdIO_xuuoC9laJM3mOXa2x8OTVsEzVlGQrz9GH2BIHJqNZVik2dmKNHlfJVHVgaRW6hY75H45lXh8Hl4g8M_M6WfKJOiJDxBsPAqLQrHDiXRW-MbYiHNJxKlXia4hr2FnVxOZwKqOPZzSsJ4Lr8qaTxiRe-l7WQZbVjGgcXNGS0zLQIlpAP7H6gqRk7Unwn4JBx_9Neo7Vg-G9UIlXGBBPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 06:22:01</div>
<hr>

<div class="tg-post" id="msg-128099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پرزیدنت پزشکیان: نظر یک گروه خاص(تندروها) مهم نیست و نظر همه مردم مهمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/128099" target="_blank">📅 03:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ: توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/128098" target="_blank">📅 03:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128097">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ حق غنی سازی ایران را پذیرفت
🔴
ترامپ در گفت و گو با نیویورک تایمز مدعی شد: ایران برای همیشه به غنی‌سازی در سطوح پایین که تحت هیچ شرایطی نمی‌تواند برای اهداف نظامی استفاده شود، محدود خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/alonews/128097" target="_blank">📅 03:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128096">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نیویورک تایمز: تهران نهایی کردن توافق را تا بعد از نیمه‌شب به وقت محلی به تعویق انداخت تا از همزمانی این لحظه تاریخی با تولد رئیس‌جمهور ترامپ در روز یکشنبه جلوگیری کند
🔴
اختلاف زمانی هفت و نیم ساعته به هر دو کشور ایران و آمریکا اجازه داد تا جدول زمانی مورد نظر خود را حفظ کنند، به طوری که ترامپ گفت توافق در روز یکشنبه نهایی شده در حالی که مقامات ایرانی تأکید داشتند که این توافق در روز بعد به پایان رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/128096" target="_blank">📅 03:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128095">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq2jzNm2gSkWFs-AZe3cftLbJeuXqxbL71BGVy6jSMxtnZD-OtnhOvfyk6ddBUAtSj0_dZx0fdSmBJVXuaVo6kwaG7kmlYOGhXq5KAvJ3YEIcP9iefjQ8jJ-tHLKW_IccF5pSnFpS2hifUygWrpOaiTL0s6JSwmfbRlphRUfjVd8LVQVToe0uI_wmlVDWBup9j_dVZNG1cl7EYWWXm4ac1ZdfpC4m_0fpqi7HM8GY9kH3aeLZ3X5RjG-seXvBXeEnDdawjDyP2uyPbysm9EjmmMs1WzV-dG63Qzk5A4fcxQhDbQirIQII92HWvUSnGsijWs0KeLS63r7Y7sn4DwF5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ به نیویورک تایمز:
نتانیاهو فرد بسیار نمک نشناسی است. او باید به شدت از ما بابت انجام این کار سپاسگزار باشد.
زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/128095" target="_blank">📅 02:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128094">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">غریب آبادی
انقدرخودکار دزدید
که تفاهم نامه رو الکترونیکی امضا میکنند
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/128094" target="_blank">📅 02:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128093">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea240da54.mp4?token=tv2YLlLto8usiMY5sE5h_yw0VUUp3OonsQII7hKF9wyHMU0VpfGWI1cyPTv4yaEHW5dlNDTD-AQAjUXKLuTentjlcAoeeUxlkn40CSGq8nU_cR70cvIClXrgK5OpVSaHxaUA0UaPfCZ7Sy4_iuUkWEOT0qCoVwhAAKTqwtLI9ccnQbKi0EiEU6RvxJ1r0q_5KbVvZztvymHYOl3303hmb3SHD_LXPFDQGv5Vzrs3JUVQetlkakBd3Z3QP7XLo0OybWyCxlS2eAxwtEZiWnRwtAKqDkqlP150PeI9AgftqroR6lt5yXQvuSjOyB5mPz3YJSZLA6_cJmtvAndk-H9Aog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea240da54.mp4?token=tv2YLlLto8usiMY5sE5h_yw0VUUp3OonsQII7hKF9wyHMU0VpfGWI1cyPTv4yaEHW5dlNDTD-AQAjUXKLuTentjlcAoeeUxlkn40CSGq8nU_cR70cvIClXrgK5OpVSaHxaUA0UaPfCZ7Sy4_iuUkWEOT0qCoVwhAAKTqwtLI9ccnQbKi0EiEU6RvxJ1r0q_5KbVvZztvymHYOl3303hmb3SHD_LXPFDQGv5Vzrs3JUVQetlkakBd3Z3QP7XLo0OybWyCxlS2eAxwtEZiWnRwtAKqDkqlP150PeI9AgftqroR6lt5yXQvuSjOyB5mPz3YJSZLA6_cJmtvAndk-H9Aog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/128093" target="_blank">📅 02:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
قالیباف
🤝
ونس در ژنو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128092" target="_blank">📅 02:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128088">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daLE-6DiG6oN7p9sMljlJmzBx7Oak8LFcyG1MEawqn9J83Uk_QgJOg_0cEInPH1yjJF5h0BneUnZU3PofbYlg-A4lClRkM-qiSJuT1GZyArWyPDVZyJCfYxKvMZKbbI_w5AqWwnMzUhgC914yH7X34oEq8fa1bAilU8WiCfdjr3Tc1Ksxiu2E_l7-21Q2uQir3gnDukpALlSJxs1jQ_lc8wkTQVxeTgFMKcFNVyGPb_2bzU740ndKhRvQlFS5-fVUPrUjPJX4vhs8w1742YEIAjxluyGwsPdzguoWc1A3hu41CUCWE0YASff814b_RuArGTnAwOIn4GOb4pi11fdUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5gkXV_uZBk-D3dDLaYtYXpRIoqALs9Iq_aHQvsIVyjqjh-AomcMEP809HWOk5BLFJRnV_43LEsGJ__a_vfZ8YQ2_FBEDsObAhu_MDhoxuRJmKxWwRHSXdCCrP6vh7yD6BGOlnd-L-UZVzDeePMWIusUG5qkIy67ZKZsHXHo1W1ZXXPh9aFa-CAPT0SyVt5J6AAtOP8pibhziH7tNIbAWAy5iBeX3pDCM_nCB2plUA7_gC_I9dE2doYyxBG6y7dm1JNHe0rshTvbjzqETO56car7Ud4byl60rF8gbdzDaSUf7tLku44c8OuMHQoSYiN5QQqDH-qGrsbJf_Mhfon0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tX7d7OlLn2PBteLVyDeAP56WcydEdszcgxhDdg_pFh9aUuba8MH1x5TZUcRsoKWFG4yY0jGm84wm8UzWdqQNeOXj8-YaxTSNlriMbxHaZsYLh1nr5-X5ZryRv7HIkpmi3p-wEZSVPz5JqJLpydMrizFcQWe1g5q0lNQ6R9Ao3yZ1pmkGiBFl1nXLFHL63e6AlZAY1fCMycwz84NkSIsVKLJPW6agabdinMZ_N1roXl5T4g2zGdKsfCXAx4ipI4OZndJJR0PDICpdXMguHTuDuDT5pWDROsuy-ai1uYLJIUz5SPTCgUP0ZXATg363oa7FPy9hiQgjR2ueqQQa0z_Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFYbeBzxmPfI6el5qQENM-Z2QAGlzBIly8ltEdIMcnkOCcy5DVjZKScMTM6rCIb6HelWF68CjFfHmbZqOVnWM7ikaHDWsnoNtShgm_iMz4mmUdhgO9IV3PCB44fBY2FuInHTFGnhj6JIXQpq3OBljDV6BcyFQHsaGWj0_ViSxfAnGlXF1kqHZBCmHmlErcPx68OP5v8HREQbkfBMUxJN1ZD0DX35IgEv_Zpy9x3I85SVX_VS1tW7YmOp_4bVOBbJpCKdK4KKd0IJOYMEv504mZEAHt6-XiWu_q709HTXbBRxZlqnpn2HWuNis2Qj_mUs63x3z_Qkn_QL64y0VsmuFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کانال تلگرامی اسرائیلی با بیش از ۱۸۰ هزار عضو در سوگ و خشم:
🔴
«خدا ترامپ را لعنت کند.»
🔴
«اولین جنگ در تاریخ اسرائیل که ما باختیم.»
🔴
«باید واقعیت را بپذیریم: ایرانیان به آمریکا درس دادند.»
🔴
«امیدوارم تا ده سال دیگر به احمق‌های آمریکایی وابسته نباشیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/128088" target="_blank">📅 02:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/alonews/128086" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری و رسمی/هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/alonews/128085" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
انگلیس، آلمان، فرانسه: آماده لغو تحریم های ایران هستیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/128084" target="_blank">📅 02:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بیانیه دبیرخانه شورای عالی امنیت ملی درباره توافق پایان جنگ
میان ایران و آمریکا
بسم الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
🔴
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانه رزمندگان اسلام، به دنبال یک دوره مذاکرات دشوار و فشرده چند ماهه، و بر اساس مصوبه شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه 24 خرداد ماه، نهایی کرد.
🔴
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان یافته و به علاوه، محاصره دریایی علیه ایران بلافاصله و به طور کامل خاتمه می‌یابد.
🔴
امضای این یادداشت تفاهم در روز جمعه 29 خرداد به طور رسمی انجام خواهد شد.
🔴
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
🔴
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/128083" target="_blank">📅 02:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
انگلیس، آلمان، فرانسه: آماده لغو تحریم های ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/128082" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jF1DiK9YfPwY_ymfhmzEGf3m-gSIPVroo6TaaePJvLb0tSwFMgf9UYI5y0rJA4ItIAThkQenhcxQAqfXNr_4DwF845RbpVW6JWQ0OG30AyiZ2ZL2_u9oK_S2x3DPLo42MWb3WusKN46MyI7fnqBrZ7bW4kl8yyzry2igOBDFvCBEKUJC7vUHaVsXWzmZ4nRLWHLtit6amyzDA_A5-5lnln0jlU3IN1_awkhZlTxk_pYJOiwbZa8X3dxhsMdqKzFd7dWVhfnuHaJ1HUIfsVJ6HjDWt63B6-Yy8zh1mNL9ysZgSDmzEtFqgIPa2_7CQaJGabBV4rEtPt6itIOdMZPlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏عایشه قذافی، دختر معمر قذافی در کتابش: به پدرم گفتن موشک و برنامه هسته‌ای رو بذار کنار تا درهای رفاه و آسایش به روی لیبی باز بشه.
🔴
پدرم همین کارو کرد، اما ناتو شروع به بمباران لیبی کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/128081" target="_blank">📅 02:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2af3a0e9b.mp4?token=r_r5yAb21sTCSsI4lmzpkiis7RbkUtCmn8T2KfUAxa0YjVtynh4Zbt30Q7S2UU-3y9Mvv8wt_MZYk_rRG7GL5nwQzEwwjYmc-9YQWooboGKEFwDDfkyFexjfqQSaulWaHUfdBXS7FcvJnECfaHZbz727sf_cpO6aSfyk3a5YalC-OYkSsGPQPfzroxB5m5ctXPFLyLJgGpavJNcUBvHx5ja1-zLQpNl4I_im0mRI1APGS4DoHlGme9uIxLyMWWWVx_plKvOCYHiCaQjNktb7ptU95Stg5uo3qUy4czHGE7AtGg6-BBHKevDExaCe_v5rrHirTR81uV6hiHj19wCF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2af3a0e9b.mp4?token=r_r5yAb21sTCSsI4lmzpkiis7RbkUtCmn8T2KfUAxa0YjVtynh4Zbt30Q7S2UU-3y9Mvv8wt_MZYk_rRG7GL5nwQzEwwjYmc-9YQWooboGKEFwDDfkyFexjfqQSaulWaHUfdBXS7FcvJnECfaHZbz727sf_cpO6aSfyk3a5YalC-OYkSsGPQPfzroxB5m5ctXPFLyLJgGpavJNcUBvHx5ja1-zLQpNl4I_im0mRI1APGS4DoHlGme9uIxLyMWWWVx_plKvOCYHiCaQjNktb7ptU95Stg5uo3qUy4czHGE7AtGg6-BBHKevDExaCe_v5rrHirTR81uV6hiHj19wCF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
بعد از حمله اسرائیلی‌ها به بیروت، ما شواهد زیادی دیدیم که نشان می‌داد ایرانی‌ها قصد دارند تعداد زیادی موشک به سمت اسرائیلی‌ها پرتاب کنند.
🔴
با ارتباطی که با آنها داشتیم...
آنها به ما اطمینان دادند که قرار نیست به اسرائیلی‌ها پاسخ دهند. آنها قرار است توافق‌نامه را امضا کنند و به صلح برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128080" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تسنیم:
تنگه هرمز را بازگشایی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/128079" target="_blank">📅 02:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23da8e0c62.mp4?token=TeRNsHUnjo7fnanJpHOYRqCIBW_lS0IUu5bWfyFLg0268NDsgFZQJzxmz2IqcQTaHOgL-Tf05sSAdQpkC_AGb_6lepLjyhsOaP50KTyKDKNRANdqqFdFLSqFYWUqTpP7Ge1xXM-whyhMrCtvwD2NYb3EBHx9QnOVFCup8VaNJ7HAkAHiJgur4SBEvR-7QdX5rH3acYpgAC7JQQWMgRKgYJBTGga76nutoDi5ix8BsU0hN0Np1gNpI8ffkBEAaCIcLv8XiSdKsPB1ff70gcpZ6a6XcfEwYOnGQmViG-bobZOvUqV66KDwYo4xxtHFVVG4Pkq_2fjINLHBt6SKrz8D7Sv1X4Pg-gEFzbXBJxQOxynGfwjCUskVpON9IZFDVYLyVMRqpuqk2YZElPh62KeSIzyDBWvF8iKFGbIR5qqn0ZPdImX-hWRedHxsgtX1JGM1twcyEyN7F6m81GU6o62r47KZsgT-2VXmvf8yOUEg48w0p8TpV3ljtp0I5_G5cDCydGFxeBpxnEvMbZ6I2sIom06ez1CdQriFxbjF11ASrxKjlitSCu1V0rVlhl6f_r4HzVjcqpWl31gCttUrq0S4pk6cKT8cJBZvDfyjqp5azWxivjAk8tnB-K4AbmWTmTTRTOPuE_Mi-jlxT8SyXu4SwBUCqW1h_nQpUeoFRCskIjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23da8e0c62.mp4?token=TeRNsHUnjo7fnanJpHOYRqCIBW_lS0IUu5bWfyFLg0268NDsgFZQJzxmz2IqcQTaHOgL-Tf05sSAdQpkC_AGb_6lepLjyhsOaP50KTyKDKNRANdqqFdFLSqFYWUqTpP7Ge1xXM-whyhMrCtvwD2NYb3EBHx9QnOVFCup8VaNJ7HAkAHiJgur4SBEvR-7QdX5rH3acYpgAC7JQQWMgRKgYJBTGga76nutoDi5ix8BsU0hN0Np1gNpI8ffkBEAaCIcLv8XiSdKsPB1ff70gcpZ6a6XcfEwYOnGQmViG-bobZOvUqV66KDwYo4xxtHFVVG4Pkq_2fjINLHBt6SKrz8D7Sv1X4Pg-gEFzbXBJxQOxynGfwjCUskVpON9IZFDVYLyVMRqpuqk2YZElPh62KeSIzyDBWvF8iKFGbIR5qqn0ZPdImX-hWRedHxsgtX1JGM1twcyEyN7F6m81GU6o62r47KZsgT-2VXmvf8yOUEg48w0p8TpV3ljtp0I5_G5cDCydGFxeBpxnEvMbZ6I2sIom06ez1CdQriFxbjF11ASrxKjlitSCu1V0rVlhl6f_r4HzVjcqpWl31gCttUrq0S4pk6cKT8cJBZvDfyjqp5azWxivjAk8tnB-K4AbmWTmTTRTOPuE_Mi-jlxT8SyXu4SwBUCqW1h_nQpUeoFRCskIjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما سرود پیروزی پخش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/128078" target="_blank">📅 02:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزییات این پیش‌نویس به شرح ذیل است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته ای و لغو کامل تحریم های اولیه، ثانویه، آمریکا و قطعنامه های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تکرار تعهد ایران در پیمان ان پی تی مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار پول های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق.
۱۳- توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل به تایید می رسد.
۱۴- مذاکره نهایی قبل از آزادسازی نیمی از پول های بلوکه شده ایران، تعلیق تحریم های نفتی ایران و رفع محاصره دریایی آغاز نمی شود و توافق نهایی صرفا در موضوع سرنوشت مواد غنی شده و غنی سازی، رفع تحریم ها، برنامه بازسازی اقتصاد ایران انجام می شود و بحث درباره برنامه موشکی ایران و حمایت از گروه های مقاومت به صورت قطعی از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/128077" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
جزئیاتی از یادداشت تفاهم ایران و آمریکا
🔴
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
🔴
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
🔴
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
🔴
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
🔴
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/128076" target="_blank">📅 02:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
توافق جمهوری اسلامی با پیمان ابراهیم رو پشت دست در نظر بگیرید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/128075" target="_blank">📅 02:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یک سوال از فروشندگان و واردکنندگان حلال خور و مسئولین با کفایت:
اجناس وارداتی که به بهانه محاصره قیمتشان تا سه برابر افزایش یافته بود به قیمت قبل باز خواهد گشت؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/128074" target="_blank">📅 02:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128073">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
طبق یادداشت تفاهم بین آمریکا و ایران، پس از توافق نهایی نیروهای آمریکایی باید از محیط پیرامونی ایران خارج شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/128073" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128072">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b2b37789.mp4?token=bLrFg5hoJ1Gwtpr0hpDhXLMAe6OfmhOJSiph_djm0OstOdFxl7wUCxQzueOvV4Y4H1tDsGWzgMExe40j9xPel9h7PT00ye7D74OUGweOgC_JUtfdMa9jbAZNWFLYQpFRRU0TmaVyvzGS0xj5as4rVg8LLmcmdWbZbuQhq-9HoNfmRxrhypVjTTTIHvzpEkT6y9F0wx26fVjBgMlZ_EnhRIaTOuS9ou_R4b_smkNoLFa5j3kTP-bbG-pl_tLuhgtBap5O5FcBbv5M-xP6m8qik8TEI4LAxnmJucwmkSWr3-QWKLVp02KkN4zIH6EWCzuFYqjxa3JwYPU6YBE-nuV-iIeF9liDiH4Q9CejK_TiT-08dVomSDkNtyeT9t_Tz9jMe3b01dIx8WAUmGL-7f-7K1yKsX1iKaMyi2W85EWxYBOaY53uQPZoacQVHNx9lYLKSkVo00EBpK5Hsmf8nkwzgq6KUqFp09erDy2sDVKRRqXofthuYHyRT06PvMquDLKNmmcI5ZNgNko1U6-Uh-uDOIwyRP-kVJSQtWQVq6zt2i2GqsmmpWZv0OJSXlUinQeS6wSX_kbIHurFAVSuD0KBKwtVkv4wWgpGLSiAUyiNH2LHNHZzNX54gArQN7XoFezY8oTN4P8o3dN2UmwVrrT8khfNOmYotN2owjXzt5ydkJ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b2b37789.mp4?token=bLrFg5hoJ1Gwtpr0hpDhXLMAe6OfmhOJSiph_djm0OstOdFxl7wUCxQzueOvV4Y4H1tDsGWzgMExe40j9xPel9h7PT00ye7D74OUGweOgC_JUtfdMa9jbAZNWFLYQpFRRU0TmaVyvzGS0xj5as4rVg8LLmcmdWbZbuQhq-9HoNfmRxrhypVjTTTIHvzpEkT6y9F0wx26fVjBgMlZ_EnhRIaTOuS9ou_R4b_smkNoLFa5j3kTP-bbG-pl_tLuhgtBap5O5FcBbv5M-xP6m8qik8TEI4LAxnmJucwmkSWr3-QWKLVp02KkN4zIH6EWCzuFYqjxa3JwYPU6YBE-nuV-iIeF9liDiH4Q9CejK_TiT-08dVomSDkNtyeT9t_Tz9jMe3b01dIx8WAUmGL-7f-7K1yKsX1iKaMyi2W85EWxYBOaY53uQPZoacQVHNx9lYLKSkVo00EBpK5Hsmf8nkwzgq6KUqFp09erDy2sDVKRRqXofthuYHyRT06PvMquDLKNmmcI5ZNgNko1U6-Uh-uDOIwyRP-kVJSQtWQVq6zt2i2GqsmmpWZv0OJSXlUinQeS6wSX_kbIHurFAVSuD0KBKwtVkv4wWgpGLSiAUyiNH2LHNHZzNX54gArQN7XoFezY8oTN4P8o3dN2UmwVrrT8khfNOmYotN2owjXzt5ydkJ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور:
اگر ایرانیان به این توافق پایبند باشند، این موضوع خاورمیانه را برای ۵۰ سال آینده به‌طور بنیادین دگرگون خواهد کرد.
این منطقه را برای سرمایه‌گذاری جذاب‌تر خواهد کرد. این منطقه از جهان در تمام طول زندگی من و حتی پیش از آن، وضعیت بسیار نابسامانی داشته است.
آنچه رئیس‌جمهور ترامپ واقعاً ما را به انجام آن واداشته است، قطعاً حذف تهدید هسته‌ای ایران است — که این کار انجام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/128072" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128071">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266e92cbb8.mp4?token=m-9uOak1c8w7j9lCPXIvPQMfccbHZyBdkuK-cQ1fB2Uliqjl2xh13KdYFxxn1dVOMtYmRP7znQARF42q_oiQq9cKqZ_kq3VvuPZhutnXdsNnhWTWmeX_gM9a6c-rceDENka4Pr6lBBrVNBtJfIU3PtvTzN0OAGVDnrc3kwfI3aBdDTO07rByvEOEY0VOHgE35haHHPMs2TUFbFII4mlZ2jVgYonlCRK9IulM329jIveMk75rrVCLMHWDVaChNyEKZ7KP_njs5hpdft3r3HSzFgDdZPKOyQY-LZrahPP1B5-4R5AFUfGTMxzUQv0QSc1TI4B4J7D5Tc1WmGTck_1usw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266e92cbb8.mp4?token=m-9uOak1c8w7j9lCPXIvPQMfccbHZyBdkuK-cQ1fB2Uliqjl2xh13KdYFxxn1dVOMtYmRP7znQARF42q_oiQq9cKqZ_kq3VvuPZhutnXdsNnhWTWmeX_gM9a6c-rceDENka4Pr6lBBrVNBtJfIU3PtvTzN0OAGVDnrc3kwfI3aBdDTO07rByvEOEY0VOHgE35haHHPMs2TUFbFII4mlZ2jVgYonlCRK9IulM329jIveMk75rrVCLMHWDVaChNyEKZ7KP_njs5hpdft3r3HSzFgDdZPKOyQY-LZrahPP1B5-4R5AFUfGTMxzUQv0QSc1TI4B4J7D5Tc1WmGTck_1usw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جشن آتش‌بس توسط مردم لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/128071" target="_blank">📅 02:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128070">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
آزاد سازی قدس دیگه کنسله
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128070" target="_blank">📅 02:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128069">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
طبق یک بند از یادداشت تفاهم بین ایران و آمریکا، پول های بلوک شده ایران طی ۶۰ روز باید آزاد شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/128069" target="_blank">📅 02:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128068">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9ip4WNBeyhMl3Qp8JzIkuKeMIbT4eoD4KMs6taPe3YF6uQOHibhk4AarVbKmXcyOGcS7jXbGIao2I7w_RhfE-fJrHchsfuGhrTvtfF0VEuzHG_hRR2kqvW4hoozj_6Yt9jveUFRltgQmwKXDaOzMc530kMBdh6soYNTIqW5pi648wVItNdqthChIyUp6xw0KcWSqpH7wYF06z-yepqLAi7-iiv6W7kp_M9erSmAtRQiO_JMiHl9AZkNLNxmiutUo4K_3SMXeI3wGfqMZivzqQ0_ayvBgYQYy1inF72P-Cwm9vDox47_dyTOimY9mwDQj7fmWt2oRn8d6jOL7qsw3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخاطب اینترنشنال:
آقای ترامپ ما کشته ندادیم که توافق کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/128068" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128067">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
شعار مرگ بر آمریکا دیگه کنسله
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/128067" target="_blank">📅 02:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128066">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4x9B-sz1ShhtzzGT2QPmWVD9tZauICKHr8t6EMIeG7gR3kbmqqiSXXnTf65hm1vZ7erG1dwFFm7t__CSwT5wR0g1PTGsGOT2qyg-K-jQ4NtZMCaS0PgtcGUW1jXatLhMiNVWHEojvRtjRcc4OzLZI_GSqxdiKZoQUb7evV_7XQAN_00TOuVOI4VANLyBmAx8jgJLa7UffClvZMjYPn0_LD1Lw9o9VSY3CeIf9PIHezDeFYiwNygi_RBV3WOccU39KFI6IrMKtP5cmCXOstLDDWCshk-SA9hHDJ75Bm9VE1yCbadTmJphKcO0x6KR3XvfFN9AiHgaoKLMDGorsT70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
این توافق بزرگ، صلح و امنیت رو برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردن با ایران صلح کنند، اما همگی پیش از من شکست خوردن.
🔴
رهبران منطقه برای نخستین بار، رئیس‌جمهوری رو یافتن که میتونه به آنان در دستیابی به صلحی واقعی کمک کنه. با بازگشایی تنگه هرمز پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/128066" target="_blank">📅 02:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128065">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
طبق یک بند از یادداشت تفاهم بین ایران و آمریکا، پول های بلوک شده ایران طی ۶۰ روز باید آزاد شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/128065" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128064">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpUOljnDl5T0-CsHt3HHbuaQqBqo5PnxXxZ6nwgfVtHglCntHvgaWsm3Sh3t7U9Za1dZUOGc1AXa3eDNei0A1jNmCwywmXm4ml8W2eK0nA8hlFeGhj6rOLU1wWUS9Kw5ES8pUSZ5OC_6kW0QloOUGCzdYvF9Z1NdFQ52kmfWOYuOq4WeszyLDBNBXS8twpBQrqQfARvakpmqH7A_ZZ__SID6b3urnQ0R5SvvnayeY-CUbBS5DZZ2uro8DTlu3ILDG7cTiORKUH1nr7G24DQBZSC0ZWYQo09xfLW8pZLzO9HJDKO6FUFka5PxX4g2nLtMaID9LEFFhseqL9R79IZrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتشر شده در ایتا و روبیکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/128064" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ادعای معاریو:
نتانیاهو به ترامپ گفت که اسرائیل خود را ملزم به رعایت بخش مربوط به لبنان در توافق پیشنهادی آمریکا و ایران نمی‌داند.
🔴
بر اساس منابع اسرائیلی، اسرائیل قصد دارد نیروهای خود را در لبنان نگه دارد، عملیات علیه حزب‌الله را ادامه دهد و در صورت نیاز به حملات پاسخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/128063" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128062">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEwCInHyiC97xoqT0Yz9JzZc-88WLhKloEAXQfhupCilWNdoYrgmtRby_fbqCUITsbS5R4PzdRSPD8pxpA5qvBX6LvDm-52b44akgBZtTXAqdrvE71eROCH037ZMu6GKK6pNebxUg6pZCPox93CUZlkn_Sd2xXkDCgLf1CqOSr4bX4Kl45M7hem36uU9cMJaKVqpZqdXx4WDxxf7m9ROYDzwxFpk0XXEukNRG2FWNWhDu-CxzDi7yE0HCyhpR-ydHrID1uO6Qagj4387--xwQzurIghEp9EuadPXPGJW3dm6cbddEZKRjdNByLhKVm7JcaJHNYeDWiZq-6qh1fMFzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا به جاهایی که غذا و نوشیدنی رایگان تو تجمعات میدادن گفتن جمع کنید برید مهمونی تعطیله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/128062" target="_blank">📅 01:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128061">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702066bd6d.mp4?token=nskLKZOYhujaYhE7Ap69EBwcc6NXxtApzGDgiZDsnXoHt-iQkN6SHW8BjcuiznMNy1tXzCgxnjDYocRw-2XMV2HgCr5FimJ3MWz93fVcb9IUdDUj6wQ6EFRXL4YnYRRHv4uHPzy3z1YWJYOIzRyu5HL2AN_JYHL75ezTgwXqipoehCJHYHuuZUt14jd02VpSg1ljteYiMr5yTqy2y07WYZWh0TF6mUS0mhUPFRBMuQGkl_-y6oLtieqBZbUkiulKGjXjtuQEb9UmhZMej5BWlgZqyPVonQCocivqMfLtssMXQxS9wV9WgsUX9i4ccUfIToLA_DczoLxBLdYk-4iKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702066bd6d.mp4?token=nskLKZOYhujaYhE7Ap69EBwcc6NXxtApzGDgiZDsnXoHt-iQkN6SHW8BjcuiznMNy1tXzCgxnjDYocRw-2XMV2HgCr5FimJ3MWz93fVcb9IUdDUj6wQ6EFRXL4YnYRRHv4uHPzy3z1YWJYOIzRyu5HL2AN_JYHL75ezTgwXqipoehCJHYHuuZUt14jd02VpSg1ljteYiMr5yTqy2y07WYZWh0TF6mUS0mhUPFRBMuQGkl_-y6oLtieqBZbUkiulKGjXjtuQEb9UmhZMej5BWlgZqyPVonQCocivqMfLtssMXQxS9wV9WgsUX9i4ccUfIToLA_DczoLxBLdYk-4iKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس جمهور جی دی ونس:
من قطعاً قصد دارم برای امضای توافق در سوئیس آنجا باشم، اما ممکن است خود رئیس جمهور ترامپ نیز آنجا باشد. ما این موضوع را حل خواهیم کرد.
🔴
فکر می‌کنم می‌توانیم با اطمینان بگوییم که ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔴
ما کارهای زیادی برای انجام دادن داریم، اما امشب یک پیروزی بزرگ به دست آوردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128061" target="_blank">📅 01:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128060">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt3nuM9FkRSbfvVTRnWsN_UGh5lcDAoEPA3FoV38YxkLSmQ0e1VTroPLNZUJeJE5dvqhsZJUQGDXfGHwGYcqxrZjcVVl_nzqd7XjI7R9wLl7MSgy6eqLDw1ZKMkM1pU2c2nUdtPp97P0jL3vy9BPJ3y_ICK_t1tGheAUJo9Y9guqpl9sXL3wdEJ9VUehrm_35FwkmeNWdiFClr2kyJJUReyxCNOe0CZMsCOWIbpzD8hNZfgCpAK3JUT15U358kdNp6GdEPX5gRj1hh5bAdCiZxMBhr3_fCKgIQam68YtEaFDMi_S87-0sscv4Pvkl4ZrvOXDwksUFuyYjDdMk8gCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت تتر که بعد از خبر توافق از ۱۷۵ به ۱۶۳ رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/128060" target="_blank">📅 01:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128059">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntebpOVgqiPz_1PVLRAO1xzhFBa0x2Fdo7AY_lOaFQHAWh1G0h6HpnGehRuPxAjzifsekHcGi6FqVNcC2vVRa5UEI6FtQwGxiKs-u98HA3fU_AP0W0FHEl5ndAv73l2iskLAlCQb6gimVIQGnOZYnOjRYgZmrqJoY9kNU_Y9YiI7THKzp_q89f2ejtu0UyTrjPRY8NQAKW5AwXFgtlolpaLbGq0KuAaRe-zU8RxuBrVMSslLeoiN2hS_1jW_fIFzF9kdpsO1-lRzpnzFWd9wTpyL46wxhKB2YCORFeU-KycvhA_BCn14UWSIpYuGMbCKkt0ICHVVMWoHmc6pfAW7uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شب‌های ایتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/128059" target="_blank">📅 01:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128058">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
توافقی که جمهوری اسلامی با دشمن 47 ساله خودش انجام داد، امضا سقوط خودش رو زد. بماند به یادگار
✅
@AloNews</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128058" target="_blank">📅 01:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128057">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLihr_F4b1e4TPOTjoe2JLjK0ziqpx6fV1uItYKRZhotU4-V5E3WfBr4_pA-AkhG_lDor5GxBT9Sq9Twd3A5kOwYQCl7A_T4Fq2I7Clde4xUmTvMOJN0-QDPgVk7qjOx5R0ngSZtoh8QxkNuCbcVLdLcWquYQiuIvpi86QRAIJI7O70_rKFlZFZ5CrjLIPqMTajRwknWAKt6V9zXGSoRlYYR75PDJTqE5rdmCDCfM6pEU2Q55YvI1m4q-VLIby4ObatjaH95M_UcmZ2PGa-dtrBF5yhMDSPEijCSyZ0FKjjS-80bwOQXIi2HR0YDo4ynedUkYq8RAl47YREHjemXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیافه مجری شبکه خبر هنگام اعلام توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128057" target="_blank">📅 01:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128056">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244bb5263b.mp4?token=U_Wg62zQGQiXCVuBaSr9jkqkrLWJlP1Ykk7wyxHaurpJV_F1y6vpvzPoOyrz_Zbgv1ke_qaZn87QGaQDOBZWYoGVnkjzl2ISoIMRhwxiqbmQVPgHF9Pd5-DRA_qM_kPx8vL3SxA0vdhlDLSi0ZWJhq7dfzRdPgx6VJqZIkG6pZQVw4lCvJtuEsnx7QZcDGRn7trxZzP6ooGp_BOAQj0Cf_wUN2v4G3ew_vIhFZ1FEGaYdOsBDnUkXqfwZDz8ug9iDG_SXYpL8sWV5HzorNz_VFaG2Ni2hIFPUrasnnIizAnc4xR7YAF9DxZ8Tkjr-Ty7lofm01MDueePEY4AEYEu3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244bb5263b.mp4?token=U_Wg62zQGQiXCVuBaSr9jkqkrLWJlP1Ykk7wyxHaurpJV_F1y6vpvzPoOyrz_Zbgv1ke_qaZn87QGaQDOBZWYoGVnkjzl2ISoIMRhwxiqbmQVPgHF9Pd5-DRA_qM_kPx8vL3SxA0vdhlDLSi0ZWJhq7dfzRdPgx6VJqZIkG6pZQVw4lCvJtuEsnx7QZcDGRn7trxZzP6ooGp_BOAQj0Cf_wUN2v4G3ew_vIhFZ1FEGaYdOsBDnUkXqfwZDz8ug9iDG_SXYpL8sWV5HzorNz_VFaG2Ni2hIFPUrasnnIizAnc4xR7YAF9DxZ8Tkjr-Ty7lofm01MDueePEY4AEYEu3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه ونس با فاکس‌نیوز پس از اعلام رسمی توافق ایران و آمریکا: حالا امیدواریم دوران جدیدی با ایرانی‌ها آغاز شود! این برای مردم آمریکا اتفاق بزرگی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/128056" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128055">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=l28j8bYFuXdBiO80rCGOD_xYdQt43QkOZWHtDhPqxUBEobGKy_Bvx-SdkIbfv-AZA-Wd4zB1n46kDNs95ozlHf7vWa7Oa0OnwDyvpUgBClSslR7RETnb6MGtewfAZVT8518yx4HYB1LhZsTWV1XpDMS1QqX_qTtRcH3sAHPpEBVxHZ5Xx3lP26qaB1ANbyZit53cOk4kh2tVf0nZ99jqnlCN1-aa1JEPVMo5EbMqs_iUWVpKogSpWz-WsU79qC4EpA7XWQdJhtjKPu7wRmVBvt_U63oKySUJojdJDcBejC8-2Fhv0jTlODOnL1Hr1rX7vwWef6jN0lZeapVjvgBhuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=l28j8bYFuXdBiO80rCGOD_xYdQt43QkOZWHtDhPqxUBEobGKy_Bvx-SdkIbfv-AZA-Wd4zB1n46kDNs95ozlHf7vWa7Oa0OnwDyvpUgBClSslR7RETnb6MGtewfAZVT8518yx4HYB1LhZsTWV1XpDMS1QqX_qTtRcH3sAHPpEBVxHZ5Xx3lP26qaB1ANbyZit53cOk4kh2tVf0nZ99jqnlCN1-aa1JEPVMo5EbMqs_iUWVpKogSpWz-WsU79qC4EpA7XWQdJhtjKPu7wRmVBvt_U63oKySUJojdJDcBejC8-2Fhv0jTlODOnL1Hr1rX7vwWef6jN0lZeapVjvgBhuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیت الله خامنه‌ای 11 روز قبل از ترور:
کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نمیکنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/128055" target="_blank">📅 01:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128054">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وضعیت عرزشیا هم اکنون
😂
[@AloTweet]</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/128054" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128053">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
جی‌دی ونس در مورد اینکه چه کسانی در مراسم امضای توافق صلح با ایران شرکت خواهند کرد:
«قطعاً برنامه دارم که آنجا باشم»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/128053" target="_blank">📅 01:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128052">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dw-s0mAHzLgsJfDwhVwSn4hPdscQKPi2u-EQRMjzU5X2rrOJVIQM1lHdR__rCKVv6URSZqPaGFcshIkbjd9AzxREBXMQFYrl114-wsh-HfpXyqo2r5Ss1b85iZcfIHr41f7oF_BPLxaOVEEUedJNTJL_oA2tTzNldZ0sl8ueO0gIpSmPSEtYfWfBFb3u0vZjZLu5b4-KRjqdmkbcZz-HmjgaeOsQScmwj0BZ8kvaKcEJ3yk_4-maFwlVMUAhDgshHa3_ZJJa-rQQgt3uvyIWfS2SocTUXP7rC_td__lOrul0lWv8czPdWyZO1nwThjptqaqkw3Wcm55nJJdxeKg7GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر عجیب همزمان با تیتر در شبکه خبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/128052" target="_blank">📅 01:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128051">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بصورت کلی یک پیروزی و یک شکست برای جمهوری اسلامی بود
🔴
اما چگونه؟ ترامپ یک تارگت بزرگ رو به همه نشون داد(رژیم‌چنج) اما صرفا یک تارگت کاذب بود و به هدف خودش یعنی اورانیوم‌ها رسید
🔴
اما چرا پیروزی برای جمهوری اسلامی؟ صرفا به همه میتونه بگه تارگت ترامپ یعنی رژیم‌ چنج موفق نشد
🔴
جمهوری اسلامی در این جنگ علاوه بر رهبران ارشد، اورانیوم‌ها داد و زیرساخت‌های اقتصادی به شدت آسیب دید
🔴
ترامپ صرفا دو تارگت معرفی کرد یکی بزرگتر از دیگری که از قضا همون بزرگه احتمالا کاذب بود تا کوچیکه راحتتر بدست بیاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/128051" target="_blank">📅 01:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128050">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c79ffcd9.mp4?token=UyTwgfNQw96hQIsgL8ZdC2pimHRtJFDg55sC0nx4lk0E7QKM21sVoqsFWOrr35UE4ihU6daw1V6ZVKxws6CE61ao2qDY1BHOAwh7_OtgI4tmGAeoVu0SzmOHclXSMI22k_14103IFnbS93SLsz5AltvnqRl5dBV96dgZj0hEMwYFQtSJVkfKPs_AU4DBcSLDHxD_5iG8Ske-vZza2vp1sthraGf6Na_4ES5K2Mp1VOawwrVsSuY59ZOhrs2BLSCbRuLAQKECTrFQjbuBGG3L7XuKpdFQqlFm_Iz9pIQna4apcfOfYxE6pQKW8IdN82U7w9gMUGN97anRB25I0G0HGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c79ffcd9.mp4?token=UyTwgfNQw96hQIsgL8ZdC2pimHRtJFDg55sC0nx4lk0E7QKM21sVoqsFWOrr35UE4ihU6daw1V6ZVKxws6CE61ao2qDY1BHOAwh7_OtgI4tmGAeoVu0SzmOHclXSMI22k_14103IFnbS93SLsz5AltvnqRl5dBV96dgZj0hEMwYFQtSJVkfKPs_AU4DBcSLDHxD_5iG8Ske-vZza2vp1sthraGf6Na_4ES5K2Mp1VOawwrVsSuY59ZOhrs2BLSCbRuLAQKECTrFQjbuBGG3L7XuKpdFQqlFm_Iz9pIQna4apcfOfYxE6pQKW8IdN82U7w9gMUGN97anRB25I0G0HGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخی کانالای انقلابی در ایتا نوشتند که این جام زهر نبود بلکه بشکه زهر بود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/128050" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128049">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a32b55890.mp4?token=XqfggPgx4ihN2LNA_XmQHmQgIT9NV9V_dBoefUihaznDz16kYSu1mQ_z7SQiv7qLwZF8kLVVWmjtlX0ZpJn3SYMgd66DkcbUCvUS6umWSePEtaZXOEi4lyB2Fnmde1mXJi6DpVnd-SWvw7mHQWoODuOxGNn4_deSz-_G9OJesLzAZhz6GMZIpwOGnApSuio9DYh-kKeB2K4cDxXY3eYRQhTx5aOIPxhLaf7Lu2-kJ2RTcGsSPLw-9abbKk-5OS4AAwrj_SsBuiUAJ8wpfSbJoaMm14Fl_3drNzFWKXyXR5Vfj7FPIARYoy2na5Nd3Nwi1GIS-aQ-meRSZfaoBqzW2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a32b55890.mp4?token=XqfggPgx4ihN2LNA_XmQHmQgIT9NV9V_dBoefUihaznDz16kYSu1mQ_z7SQiv7qLwZF8kLVVWmjtlX0ZpJn3SYMgd66DkcbUCvUS6umWSePEtaZXOEi4lyB2Fnmde1mXJi6DpVnd-SWvw7mHQWoODuOxGNn4_deSz-_G9OJesLzAZhz6GMZIpwOGnApSuio9DYh-kKeB2K4cDxXY3eYRQhTx5aOIPxhLaf7Lu2-kJ2RTcGsSPLw-9abbKk-5OS4AAwrj_SsBuiUAJ8wpfSbJoaMm14Fl_3drNzFWKXyXR5Vfj7FPIARYoy2na5Nd3Nwi1GIS-aQ-meRSZfaoBqzW2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/128049" target="_blank">📅 01:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128048">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر خارجه:
متن یادداشت تفاهم نهایی شده و امضای رسمی‌یادداشت تفاهم اسلام آباد روز جمعه در سوئیس انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/128048" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128047">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">«تو رستمِ تهمتنی»</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/alonews/128047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">😐
😐
😐
😐
😐
✏️
✏️
✏️
✏️
✏️</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/128047" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128046">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
برخی کانالای انقلابی در ایتا نوشتند که این جام زهر نبود بلکه بشکه زهر بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/128046" target="_blank">📅 01:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128045">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خیلیا میگن حالا چی میشه؟ هیچی ۶۰روز قراره سر مسئله هسته‌ای مذاکره کنن و احتمال قوی توافق بشه، چرا؟ چون اورانیوما قراره تحویل داده بشه فقط بحث نیابتی‌ها و رفع تحریما هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/128045" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128044">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIIh36E5Lcml2UK-nKKyZZkCVUkHrSe8-MYoSwN1d26CUZaU62EMTNypiX8NJLK1iK0YHARI7JluboV-O6qxFQfZj-yAk8g7PIhb4o5bMzjf_kUdJLBFnVO-I6-r-p0b615ilPacaTJj9ieLurT98psj0acaJ-i3BCQ7CdAKFO7r8baq3Wm1b5dEfeTuMkqff3pDL3R_PYWuQlrVk5MZHHYA5aPPJHoERXRpvEXB7CZB2CLleKNjenrkVydeN-cHqHMYlLztvofnRxNi48r6tDzJYuuOjAFQsXrqGwbx0gecMJ7xGXzEWpunHERDUi6yeagit-N1E2j-1xnwOHlj5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کریپتو و طلا صعودی شد/نفت کاهشی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/128044" target="_blank">📅 01:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTtG8vy6qgfO1imbvMp-bGHoDlayEPe45VScAZvj5fSvcB4Wv0dqA5q9K97oka53PU15NLl31Jg9ydq-sfDuJDc-ShysRw-z7O0072ecKgESpRYI14uocUnFEeCx8K4G3IfZ75MmljnCrzl6K7xtRkcj6EDVj1w5qtJEaKnFB_xD5ihyqQS0U6rUEgaEArimi8uDgauX941z1vJUETJmIOpS4PVKl2mvmTxHZvk8ubmg005a9SnH35ymB27jwZ7uZkaQkx_dxpxF-wmEr0wvropy-pZXyquBQcF9FvON_U_v1wOe3jA2mGa24rmUGMEx7GBBA6ht1OL2zX3m3Rpc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت گروه‌های انقلابی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/128043" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
به همه طرفداران جمهوری اسلامی، استعمار شدنتون رو توسط کشوری که 47 سال مرگ بهش فرستادین تبریک میگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/128042" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128040">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
منابع حکومتی: بعد از هشدار قالیباف، ترامپ ترسید و محاصره رو یکجا برداشت، برای همین انتقام حمله به لبنان رو ول کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/128040" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128039">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ_pJ2K8kUBsrAbfXHBGkOeBSmngJZl4UkOvl2iE5xxgWwZ2HdeS9cT9YeStKnrEJ6jmW7eS_rVT_DhoIsbXkyQG1W4i0tKbvle6jVGwOBlyR5R4SSB_y9j236CtNNdL8dH-C8igY1J--_blLTVqqwGr0SnvY6VH0QFU8BJ_RXMKjTNZbyIRhvEYISlcysPgasB8oEssGO9o3jqTl3jQiY8gnWQMIJZljRI87lcoH6BJeIKL5Y5Ivb0K0WlhBIUZoRvNzxzmYM1G0SBIIC-Kf9kHTft3ULHjYjCRgsysbBz48BOmW6seqsGzFGlNUMFa98FzA87hQu8O1NXmWTcgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما: عقب نشینی حقیرانه ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/128039" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128038">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=OebIQsGOSZwGvcVCjxhPK1Ylg5I3J2dzwENHMrJYv0rJxTbzUt7HsCemRt6ySg1i3_ADTZQftFOarBGfVw5CIbwh72eezzeruh90_lwvENJfgCb7TyX-tKjraMLp6WFHug7vkozXu2NIvBGiTzyD5tmfrX9qFD9yQDM2k-iZhFlnXecdTzW3p0156o2hOxMtDywJuMkqN9dnLLhTzMc8nZMyjWbQ2as3yXKNlciLE064dXMdOynPseneAFIfBKzYu_l-D-YuEeNHKvOQ7OVY2d9aBxM0ApSEM4Q1NF0qY4x4z4hj-7q1K-HcmxYmEMnOvbibIijSwL7bDBJEDrkStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=OebIQsGOSZwGvcVCjxhPK1Ylg5I3J2dzwENHMrJYv0rJxTbzUt7HsCemRt6ySg1i3_ADTZQftFOarBGfVw5CIbwh72eezzeruh90_lwvENJfgCb7TyX-tKjraMLp6WFHug7vkozXu2NIvBGiTzyD5tmfrX9qFD9yQDM2k-iZhFlnXecdTzW3p0156o2hOxMtDywJuMkqN9dnLLhTzMc8nZMyjWbQ2as3yXKNlciLE064dXMdOynPseneAFIfBKzYu_l-D-YuEeNHKvOQ7OVY2d9aBxM0ApSEM4Q1NF0qY4x4z4hj-7q1K-HcmxYmEMnOvbibIijSwL7bDBJEDrkStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/128038" target="_blank">📅 01:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128037">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فارس: مسئولان قراره بیان صحبت کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128037" target="_blank">📅 01:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128036">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
به همه طرفداران جمهوری اسلامی، استعمار شدنتون رو توسط کشوری که 47 سال مرگ بهش فرستادین تبریک میگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/128036" target="_blank">📅 01:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128035">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مجری صدا و سیما:
پیروزی رو به ملت تبریک میگم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/128035" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128034">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
راستی ۱ساعت قبل از اعلام رسمی، توافق توسط منابع الونیوز در کانال اعلام شد
🙂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/128034" target="_blank">📅 01:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128033">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmh357DrJvv-yAPE5YhcRk0f6FqLqeccI73x6_PnIpvAu70ouozr1aSU_9gNtzZ0HpuNbX7eK9h3Kz2wxmV0E0ixtym9spyy6Ebrpr924PqPwE-iVXY-VrXmgWNuXD6iyOHaE8MxvC_jB6hsndtvFV3oAwMwazdmMgz5EQA3YF13iE9K4j-A4kNvFP6mkBfqfNCd1iZlfp9fyYGGZeH6x2SjKVuROjwMtu6v_-NjTg95YMJcmgkzfgjHwV6UNCVeFiF1ktNp_BaIT1lDIlujfOh40T__BxBz2ss_8kPzUBCO4UdD7yGoObth4xnWRsrdioNdVeuAkIldTRghlqwiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاج حسین توام خسته نباشی
😘
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/128033" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128032">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfPMmq9qOSovcx7qbbmvwRm3TN_EW0uC25lOuugkjKTEd9Hh43cEg14-etSIU5JwFs2deVxs8JdJ2trPSXPLaLC3npemuO6DtX2ZM3EG5S-7TBELDLU-80l4wnfu37B0Z5Ji-g8n-ivhVjvxCcG6KBsVdgZdrICwT3VruULtt9grAMhOzca2aUK2_3UuHxGoYMu6D0bQwNdxVlo8wpcf6AxeG-P7yhMKWmL1206EQ9g6KkdD4V-ix49lWh1aD9eVJTQCv9_IlC2AtH3h2kqNmUG8hI33dZjkgg0liD09qfTu5snZntOmPvwargWUnMN8gRBmWtObbMkAHjpeZrF8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از همین تریبون به این عزیزان هم خسته نباشید میگیم
❤️
برید خونه حالا
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/128032" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128031">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0Q6wET1s7QtAFBqLSaKAW9AYudAC6-LCy4wb8ckqyjDHZR4nqGPOL5L9iSsKcW0gZDzYRTsAGFB6b1URiBQ4b2h_wCSWilv47mvNZ6_13X8mi4a-gzPKln16qChXAtOyEjvuI2seKDGo7nhXGzAiYPvhRO33jtaTEVC6EKR5uvrBpOnra1N5Dwa-DGkFqwuq6XWHGQGpf2Z6mYa7OMCWGS4iaHdbJ8LAftKtkbtM0ZHYitmOqGDOLYmcOT15MGAJL7w-C_Diuu_zwk9U9b2cajGV1E-NxDsSBMWvJG797yTbsNgVwOpWA5ot7Y0ZPHq9xqlIlG_ur_FpEjCwZW1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دکتر
ترامپ:
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم. کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/128031" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128030">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: توافق انجام شد، تبریک به همه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/128030" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128029">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKqt8N95ZWwSWNdbiryfBHj-Z7ocVxfDLCCNdeUVtxn07v7lge0iX6Ueb_PIl6F8XXAbpQ3gHmko2Ue2Tm-SjfOqxh8KpEwQYiYne8yrmgRX08YYyKDNelvtj9GuWiGjX2LLLCmWVc3dlsIJ--UY8IWBJGc-NQLUACP9yJpJ1G5nfu06f5E6mUSVwL5BixKyUH2f4U1i79_pIBIoj1u_5SN1GMHCfMVIbp5A8IHqSQkHaE3Ib1LAPs4HF2L2uy6kZt_J4bPirUN45-M2vPOwWBQuo_5KrF1-fePhJR5p3lY9RVx7Z7QeiNMKg4ZVSNPccXDVut4aeTrkiEG79_Aig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#انتقام_سخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/128029" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128028">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjCaBlj4vFq41cPc4gRcm_Go1wi0yFcRLSFYAacwzxJytsZsDlnU8jt9FOnnHjCkNTTWcB0g1hbxzwYa1X6ZcNL3jBOtoWEP68aJemem28L47Ir7gazoYmn_nIAxRTEpYyvoPxebk-_q1Hg6AL7-QZWre7r-tTfKXbhdmtoVkQ2aYxQ1EwgRVCnt4yBVQgB2uK8MbTg-T2GxVn1dzvkmxUDKyffY-S3oq4J_c8Vn0bDS-jIoNrrEqeTH6DWA-FA9ln0R8L_cd9C-74N7nzXksut5YA7tWT-BImQPtOEgO4RY_zsyqch6LPYmTs0dsLgXj1rd1WPSqZ89XSOGQE8S5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه خبر هم توافق پایان جنگ بین ایران و آمریکا رو زیرنویس کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/128028" target="_blank">📅 00:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128027">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
از صبح توئیت و .. که میزنیم میزنیم، نگو منظورشون امضا بود نه حمله
😂
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/128027" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128026">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رسایی: توافق با قاتل رهبر را
#نمی‌پذیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/128026" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128025">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خب حملات موشکی هم انجام نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/128025" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128024">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-5PqgBl62Kwi0jokWPK6EF4E6xwkASYmfuFn-QysXp4TYNO-Bq3Gt4BeGgniOKtnyhVmnUSkc35-3_UES25zLTwNVhQUFFyDejx9JTToJODy8xzrAwBsvw_w_A0TDDLAHRWoWzFTHT_Dqpz5S-U8jvTy_7rVjS8nczJy2p1100AKDpg0dOKDPb1TKcNga4MSTlPSgMuKllueg7TeeFtcPbcMpWP8euAsclprzCTZdGqqInAUJIHRwRPAkV05XtVdGqV1odkSL-dM2XIkKPDUY6C8l9fy9gbKgTRLJU9J2dCroaHnukcuOD627DW1R6gdrKmRSxHFBrBP7kSAAJ0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر پاکستان:
پس از گفت‌وگوهای فشرده،
خرسندیم اعلام کنیم که توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است
. هر دو طرف پایان فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله در لبنان را اعلام کرده‌اند.
🔴
مراسم رسمی امضای توافق روز جمعه، ۱۹ ژوئن در سوئیس برگزار خواهد شد.
🔴
ما از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای درگیری تشکر می‌کنیم. همچنین قدردانی صمیمانه خود را از برادرانمان در این تلاش میانجی‌گرانه، رهبری بزرگ دولت قطر، برای حمایتشان در دستیابی به این توافق ابراز می‌داریم. به‌ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه به خاطر کمک‌های عظیمشان در این زمینه سپاسگزارم.
🔴
اکنون که توافق امضا شده است
، میانجی‌گران مجموعه‌ای از جلسات را در این هفته تسهیل خواهند کرد. این گفت‌وگوهای پیش از اجرا، پایه‌گذار مذاکرات فنی و مراسم رسمی امضای توافق خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/128024" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128023">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فووووووووووری/توافق رسمی شد
🔴
پایان جنگ اعلام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/128023" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128022">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: ایران در توافق پول نمی گیرد اما احتمالا تحریم ها از آن برداشته می شود و خواهیم دید که آنها چگونه رفتار خواهند کرد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/128022" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128021">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: «بعداً مسائل هسته‌ای را حل می‌کنیم» و افزود که «هیچ عجله‌ای نیست» و می‌توان ظرف یک یا دو ماه آینده به آن پرداخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/128021" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128020">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: از دید آمریکا علی خامنه‌ای مانع توافق بود که حذف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/128020" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128019">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: رهبران فعلی ایران بسیار منطقی تر از رهبران قبلی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/128019" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128018">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: توافق ما شامل تعهد ایران به نداشتن سلاح اتمی و باز کردن تنگه هرمز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/128018" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128017">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/ترامپ: امضای توافق احتمالا توسط خودم انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/128017" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128016">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/ترامپ:
علاقه‌ای به تغییر رژیم در ایران نداشته و ندارم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/128016" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128015">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/ترامپ: بزودی یک بیانیه خواهم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/128015" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128014">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLKtisQELaAh3bwUo0P9CtVNGaL21zWXwyJRiNfbDZmlEAuDwPTTT8FS1zuPNvUVegovL9Bbcd6CGQI48kSUSCe6x4j-68RRQeA3pOR7wtmQfY154T1-NarsLwou_w3odeZiGrxmnqnm-x2ZGKRu_NPp40MqIe3mut9MSdRxOySNYjmiozUZJZGsl5cSHwLRo3AvS_ANMJpxOuS5TBkuVuvD2sHuUNmXrqgNT8Xej0MMitYiUD6922HHDv4cD9fe4fKOUjXuzI4CqE4glxTZH_8fAMbql9hnkaNJfcOOj8QTQBIcsjRi2uso1Isjfl_Ve3MNg4qVU_t_XG2PxAnWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت وزیر کشور پاکستان:
الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/128014" target="_blank">📅 00:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حسین پاک، خبرنگار صداوسیما در لبنان:
امشب به صورت همزمان ایران، یمن و حزب‌الله به حمله اسرائیل به ضاحیه پاسخ می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/128012" target="_blank">📅 00:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsR4SfTQF4fm0sd3iLSqpXtEvoP2GHdncG-fZotS7UGRoYHy2VjDvX347WJ1AWvDosJdL2qha74wHnP5cpd4ZS5MZj_TQvQFtllxWGrdBdp1tM8_jNvF7dh2a0Rcl6orwmnW5640Ni5YYrdhbFoZiPgfjccoTieMz_iM_Cghiehvll7Idj0LnBjxrPbbVlQPBeTuQYfFLP3JZ2p8KLHX4DJBuoS5FREtcTuFQcCQFmyQHToBUWxXVSMW-fhh9aP7W38CaqSHhLOuVpNf1MYj3o4ivOzNDntqbJGb1e6jivdllWW2nalp_tYydhRZGXzVuQDhOFFNH62f6I46RXiWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:ایران هرگز سلاح هسته ای نخواهد داشت و تنگه هرمز به زودی برای تجارت باز خواهد شد!!!‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/128011" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e23a8dc55d.mp4?token=pjU4kXC9dtjfvQj5s7GE49s_a0ELWv7cHfnjRRnRQcq9qTd0pCyWuqa0um_CAJANe2pwAI1uyiM-MmC46LGCrdXJ6ALMVYtu6_yRYDlhr20MMLzfN4p4luG5MEKfYC08rTZJAaBJFhAMACwncHSrGVfkCgU00nEDZ_FZcP0S9UPAtQA1hO9ROQRrHmX7jXCH6CrfmTbfBbD85wkI249Kpo81RrxQRDT6ADz_FkRiR1Wma2Euj3saLJZ4Cer_j5qluQGk97JOlCUEVZfrWSsNaGi9-h_rAjNI0vQKL7xR-BWVDsNJmAtNLVPCSS3cS4IOdox3Q9uPAJlafFRdgC3N8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e23a8dc55d.mp4?token=pjU4kXC9dtjfvQj5s7GE49s_a0ELWv7cHfnjRRnRQcq9qTd0pCyWuqa0um_CAJANe2pwAI1uyiM-MmC46LGCrdXJ6ALMVYtu6_yRYDlhr20MMLzfN4p4luG5MEKfYC08rTZJAaBJFhAMACwncHSrGVfkCgU00nEDZ_FZcP0S9UPAtQA1hO9ROQRrHmX7jXCH6CrfmTbfBbD85wkI249Kpo81RrxQRDT6ADz_FkRiR1Wma2Euj3saLJZ4Cer_j5qluQGk97JOlCUEVZfrWSsNaGi9-h_rAjNI0vQKL7xR-BWVDsNJmAtNLVPCSS3cS4IOdox3Q9uPAJlafFRdgC3N8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع ۲۰۰ ۳۰۰نفره امشب جلوی وزارت خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/128010" target="_blank">📅 00:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ot07Wv_X4i2Db-dkx3lAdtCKWDVYlUUktyFOLbJ9fFJoUfMX3bm0fQrWL7a_yuBJi1uIh5SLPMcOyEK-CAJZDXvmlQ69RDT4UqqRq5dDQzq37mD5pxV70HY7gyHKV55SbO0LtXwwSuQhZePP9tMadDrg8G35z8LhUmP1nkBNT75iPPSlKqkvZcAuxPDGIMGw-LZScNsc8GV07Ww1zueiI9rM_RZS-HOnvPsGXa3ERPVnxLtaNbcebJ6dkoF1TCgjAdLmFAHhqq1NtetbaYE99lWSPw3lIicVJbQIphMex2NYdWmz01eg6B5cmchQo5OmG1x9bnif8l9_L0Js6XKTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس:
دکمه جلیلی فعلا زده نشده و همچنان سرکاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/128009" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128008">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdH9rIoKtEvxYPWzhrg4xgVIqgcMhORLbapeyup_OerWMXnGROxOGcuiyreb1njUiU1iCBljANtdhHW4iThp5dL4E-C5h4nIML-g_i6Jc_OHE06PBhzjfpaua_SYvAzYGBwZA-O97Hw-vlTqbfZd0o48kNfC5HA_mwefmhVOEau6-HZX4JVrPFf1N30hzWB7Cq_cUyS2kP8L6vXvvCtl53G7Q82bdwKSTXcBpRU7eIlZHcxBPBZet97dqjgXys7pGGjakdK-dULQ0xOyZvv769UZ-IltlXxCvByPccenzOKNM_EI6ooFawme3uw02-FyxtyH84HirhjxNT3y9cnDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : جک رید، سناتور رود آیلند، گفته توافقی که الان بستیم از توافق زمان اوباما هم بدتره
-  به نظر من یا داره عمداً دروغ میگه یا اصلاً نمی‌فهمه موضوع چیه
- توافق اوباما عملاً راه رو برای رسیدن ایران به سلاح هسته‌ای باز می‌کرد و کلی پول هم بهشون می‌رسوند؛
- یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا حالا بسته بود
اما توافقی که ما الان انجام دادیم دقیقاً برعکسه؛ مثل یه دیوار محکم جلوی هرگونه دسترسی ایران به سلاح هسته‌ای رو می‌گیره
-  مقایسه کردن این دو تا اصلاً منطقی نیست. جک رید باید پاسخگو باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/128008" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128006">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سی‌ان‌ان: یک منبع اسرائیلی گفت: نتانیاهو به دنبال دیدار فوری با ترامپ است
🔴
این منبع افزود: نتانیاهو تلاش می‌کند پس از بازگشت ترامپ از نشست جی‌۷ در اروپا، آخر هفته آینده یا اندکی پس از آن، دیداری ترتیب دهد.
🔴
ترامپ روز یکشنبه پس از آنکه ارتش اسرائیل، بیروت را هدف قرار داد، به شدت اسرائیل را سرزنش کرد و گفت حمله به پایتخت لبنان «نباید اتفاق می‌افتاد».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/128006" target="_blank">📅 23:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128005">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
یک دیپلمات مطلع به سی‌ان‌ان گفت: مذاکره‌کنندگان قطری هنوز در تهران هستند تا اطمینان حاصل کنند که مذاکرات در مسیر خود باقی می‌ماند.
🔴
به گفته این منبع، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده در پایتخت ایران به سر می‌برند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/128005" target="_blank">📅 23:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128004">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
صدا و سیما: امشب رزمندگان اسلام، اسرائیل رو بمبارون میکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/128004" target="_blank">📅 23:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
یک منبع امنیتی اسرائیلی گفته است که نخست‌وزیر بنیامین نتانیاهو انتظار داشت حمله به بیروت باعث تشدید تنش‌ها و به شکست کشاندن دیپلماسی شود، اما مذاکرات با وجود این حادثه ادامه یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/128003" target="_blank">📅 23:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0466bd76.mp4?token=lAwKsan_lt1BDSIAYuZ44XYx3__u43ylkMBP0p5Lkmioqlk7H_845GamIAjFYdN4U71bLO_xE5mvbUKfYa9X7a5LlQqjJSTyedWG0ExhIxms4MS8evBqw5i4JMDd3QH0kuXExJ6hNpMJeYQTjxDATmhQXqRt9izddDKj3p6KJArTulhk6wKrqmc3jcOs_qp6hwc5c9aoExkPS9Kybrb3TV8KRhKOrrwe-OQO07ufEZsIw61L-zkpyrTXdFRUn37fWO6rTbfNSQA4RJGyB5exTMYGTk3Mg_NbRgNaSUF5jmcHWmOMiPaQimwr7bQyT2Rzlr67mWPuzczWhJvyF_0M-XON36_lHnzzU4TkJMKGtyQaNrrpqZav_XADOjlB6knz6AxJjHkndXLw3lWmDx6dP70SzeIt1mtDx7tLMohARvA4ystv3ZLHvvgrPti-DNzFm_-PedQWg-zpMQ-K4DIZM7P3wpkWF2EBPon-nHLVy8_75kkpKFc0sqLrnNAPEGuP0MVVG0Ip7-AwzqGdthS0qmIt0Q8ieOeRZvg7IAQhCZGL_IAlXsO7wnbLqxOpRu1aVbSO2qSlqe0fiiL1-UnoYrjVxco50qiZw6d86MeWCyHxgJ2PND9jsVkmjLftvMYH7iqh5NeZyVemu1wicxqWZs7iUYnLE27nJCHf9yKnEU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0466bd76.mp4?token=lAwKsan_lt1BDSIAYuZ44XYx3__u43ylkMBP0p5Lkmioqlk7H_845GamIAjFYdN4U71bLO_xE5mvbUKfYa9X7a5LlQqjJSTyedWG0ExhIxms4MS8evBqw5i4JMDd3QH0kuXExJ6hNpMJeYQTjxDATmhQXqRt9izddDKj3p6KJArTulhk6wKrqmc3jcOs_qp6hwc5c9aoExkPS9Kybrb3TV8KRhKOrrwe-OQO07ufEZsIw61L-zkpyrTXdFRUn37fWO6rTbfNSQA4RJGyB5exTMYGTk3Mg_NbRgNaSUF5jmcHWmOMiPaQimwr7bQyT2Rzlr67mWPuzczWhJvyF_0M-XON36_lHnzzU4TkJMKGtyQaNrrpqZav_XADOjlB6knz6AxJjHkndXLw3lWmDx6dP70SzeIt1mtDx7tLMohARvA4ystv3ZLHvvgrPti-DNzFm_-PedQWg-zpMQ-K4DIZM7P3wpkWF2EBPon-nHLVy8_75kkpKFc0sqLrnNAPEGuP0MVVG0Ip7-AwzqGdthS0qmIt0Q8ieOeRZvg7IAQhCZGL_IAlXsO7wnbLqxOpRu1aVbSO2qSlqe0fiiL1-UnoYrjVxco50qiZw6d86MeWCyHxgJ2PND9jsVkmjLftvMYH7iqh5NeZyVemu1wicxqWZs7iUYnLE27nJCHf9yKnEU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس شبکه افق: امام شهید ما خونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/128002" target="_blank">📅 23:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی: https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی: @exovpn_dl</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/128001" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crpeHZNiImB1FnbaGEax-0TmE67nLVUTjJL69dRtGymKa_c2RzuyfzZKBJi9Nt5D9m9zYEvc_LX6dDCi_s_GJiAm1_XKPtL4k6y8b9Rv5t_mWOKPUwcHgFEiCvLiGvh_vSIY4P2Vy_aQdeW-TNVKloZlCBKAlpUV15IiHJRV9dOzRb9R8_c0C5LkgHnT2XAslRJ1wUP6fiy181Jd21CMkbBLSlAgTXM9QXeLwYYpjOnDp1gxOHRhyd05UoMl1Y97il97wqwTBHoPrzkeuoioXA3uOVyUD-rcOO5eHlkSUg3n7rBGIZ3tV2E9_ZWpnyvH_QoM2oMFqp9mCawg85-zJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی:
https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی:
@exovpn_dl</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/128000" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اختلال گسترده در سامانه‌های جی‌پی‌اس سراسر اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127999" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
منابع میگن که جمهوری‌اسلامی قصد داشته حمله موشکی رو شب انجام بده، احتمالاً هم‌زمان با پخش اصلی تلویزیونی، اما اونو چندین بار پس از دریافت پیام‌های مستقیم از ترامپ به تعویق انداخته.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/127998" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq3HSaaKMylh_lypJUa9u31aUpbGnVb7AXuRF5_QqrRx-LZtn8Xg4cwbB4XUFx9bb6Yy73uLogkhP2bogndtPl_JjJk0UhsOsI05IbkVLXo31Re9Aym3-CCprlSZZUrzODD6B59IocGWctTxfyCEztqBIhJwt0bhOucQ6zfvZrVry-ND6kUXe8Zx-Q4KCyPgf3QAiCMu6_-PgiW88G1ybSZM40T8c3CvnLe8E3cSew79LBqi-nXTZzo9kRwt-MJYZDm4zZ6axroB3PLb2t-JhNGTVnWGFKNC9Jwkdu7Ol1L0-ion50SEr6-o-f3Ubml3__u-b-VyVKSijpwz1HB5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/127997" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a893cd483.mp4?token=bBA2ZjgFoBzHvo4XjzbZe7Y8ZGVVM161oZc1vJX_jfA-i_OIFP245d1JjaErtx-hQ_5Ys93F3CP6HzLIeGTYpX3HYGzoB-K1B7L914k2fmq81krDg6Qbkb8eMgnuASgrs1Pbwow-mZHZnH0-rlIxa3tWToPH6gIZWXkzPIDneMrEK1lWtj05ATRoK3SIFspWOXUl9VyRUwB6ugG6OT8eLK6onYuq-ht7XcjSTGurkVXB8nBJcWRuNwG7nY0DmFvTL5-Tq2292IzGcPFjHCr0X7gtDOmSo0FFQahkLICEtIDlk4Gof7-G3v7cyPE3lXrZ3QpDRIiPxV04vMGxlpjBQSNDZZbCYK0zBkHDyMnh59_ZDTj-C1T3IRmslTFRgB0JGVXBpZsWk3oaV6Z4IUPuJxVeUZPe1edRJ-5qJZAD-h7eqJQV1PfDP6VIZMq9wAKzHB5jSh25mhxHPmBJ4PyjQn-M5-KzaMYaBW_l39BABdLQBQt7xjszTwzK5zi8GkrDaM7f7j6KUYyoeu3CwVJ8CX1NqFVSmPab00VaUzdNsSK6DyZj4ZZCh9BFDfWBcRbBSRum0rl4CzBwLXfRJLQTIoGm6ufm2wXrSSBeIPHx3viBxMmLQrXmLYL93mU5NwtwXQiZ0t2yOQJyBEv2jVxZL_mp00BbEL62cU-6WfnlRQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a893cd483.mp4?token=bBA2ZjgFoBzHvo4XjzbZe7Y8ZGVVM161oZc1vJX_jfA-i_OIFP245d1JjaErtx-hQ_5Ys93F3CP6HzLIeGTYpX3HYGzoB-K1B7L914k2fmq81krDg6Qbkb8eMgnuASgrs1Pbwow-mZHZnH0-rlIxa3tWToPH6gIZWXkzPIDneMrEK1lWtj05ATRoK3SIFspWOXUl9VyRUwB6ugG6OT8eLK6onYuq-ht7XcjSTGurkVXB8nBJcWRuNwG7nY0DmFvTL5-Tq2292IzGcPFjHCr0X7gtDOmSo0FFQahkLICEtIDlk4Gof7-G3v7cyPE3lXrZ3QpDRIiPxV04vMGxlpjBQSNDZZbCYK0zBkHDyMnh59_ZDTj-C1T3IRmslTFRgB0JGVXBpZsWk3oaV6Z4IUPuJxVeUZPe1edRJ-5qJZAD-h7eqJQV1PfDP6VIZMq9wAKzHB5jSh25mhxHPmBJ4PyjQn-M5-KzaMYaBW_l39BABdLQBQt7xjszTwzK5zi8GkrDaM7f7j6KUYyoeu3CwVJ8CX1NqFVSmPab00VaUzdNsSK6DyZj4ZZCh9BFDfWBcRbBSRum0rl4CzBwLXfRJLQTIoGm6ufm2wXrSSBeIPHx3viBxMmLQrXmLYL93mU5NwtwXQiZ0t2yOQJyBEv2jVxZL_mp00BbEL62cU-6WfnlRQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا چپ ها از ‎شاه متنفر هستند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/127996" target="_blank">📅 23:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سه ساعت از زمانی که ترامپ گفت توافق ظرف دو ساعت دیگه انجام می‌شه گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/127995" target="_blank">📅 23:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سه انفجار مهیب در شهرک الطیری در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/127994" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127993">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وای نت: ممکن است ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایرانی به اسرائیل جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/127993" target="_blank">📅 23:29 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
