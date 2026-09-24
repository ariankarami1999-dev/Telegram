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
<img src="https://cdn4.telesco.pe/file/JzTTUbvcODRElHB6mqxVtr5M-zb0m6b2628DqRrHgBUIyveZQ2muFMyUOvjzm5YUF4kCm0ZiTNvhdt7IZLfUsUI1h2TWuTF5qarq7hRqmPCUJ_g4w6-NAOQ-5q0_RVRrAqTLRkiOXjudy1WCSfsXsKtVRIOyXCfRaqQxX7yUJjd8fU6fEtgQRVLHb_Zs3WXgRX12ag8JfJgyqPFKNPRrhALBCQPK_S4ZqYWPaxeJaRu70xJOL6J0IHJd6ROvAUtqJJmJSR4AYdnmN0acNzlRQXMfm3z38DjQarkm9xI2zBHAkO0HbsoloYZSVxQ0Ws2tzcZQ8M1nUF3Z2RkeMeV92Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 451K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfq6OhzvSw8wTS4qomGjeFtXQnYzDujszurUXsz0QexeHTJR-NU-F_KkjLxAKS0Fiec3V0OH3FICMLPcZI6yl8dTWbdvWZqIj6jJPdHkv4gamSIgggA50JceMClAimOt0jQGOGWnRuCrptaVXncZ8btUBzsAKjahX9aoBwYBm6Z2MxhNEzMsW32XIo0G4yY_vynF3PpXzvh0yjL2fitmwUVxjkUsHbKYX-vlIXtBLt6Cgiibyo9yRPnQ6ucSjSC9X-OwxBPpPUOZc54MIwp3_H-oHIU9xstvka-RdZUIxU2otO3MtIzVdjn9nERVv5jPVu_cUunYVqhWLHI_Wapg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LV-DIeZPX9Qr0xselYuAV4kMBEjc75UF15kLwmIKZhat4xmafsA8dGQ3ZfXM3sKhbF_VO1VaTFF70EWc4rSNCxfozQG4T5TB1A-CxSoFG8XvVHoK_m6BMYeFcjUUr3JvptBEHzXVnk_bz4psoRzg48JHbcDMTLSOB-RQsOqwqsa0rx__J0Z9lY3-8vR8ZwDdyJis5XRrdMMpu5a5otyhSDHFccWGpbT0rle2zmXOyM8xdpJomqzD9YIWkXrVGIfst7RrUmuRt7lwE3zjKtAPze0x6vUVCRKlMF1qzcvtNRaO2ywHl-lg125RAcJrk9d0fymiX_E-Xkt2a21KK1PxNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LV-DIeZPX9Qr0xselYuAV4kMBEjc75UF15kLwmIKZhat4xmafsA8dGQ3ZfXM3sKhbF_VO1VaTFF70EWc4rSNCxfozQG4T5TB1A-CxSoFG8XvVHoK_m6BMYeFcjUUr3JvptBEHzXVnk_bz4psoRzg48JHbcDMTLSOB-RQsOqwqsa0rx__J0Z9lY3-8vR8ZwDdyJis5XRrdMMpu5a5otyhSDHFccWGpbT0rle2zmXOyM8xdpJomqzD9YIWkXrVGIfst7RrUmuRt7lwE3zjKtAPze0x6vUVCRKlMF1qzcvtNRaO2ywHl-lg125RAcJrk9d0fymiX_E-Xkt2a21KK1PxNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgR7HrGbpOejtW7ZD6tf-UxRZ6NMzd-n6_cpioPbT-yH09vZtihfxi1D6EafhiaJKrx1caaZfvlxGn88ViSg36GRX3ojhcaHVicqOqxpF6qTUQiSQGmvaULbI95JGb9AkHY320wmSG8xNuTfD4zmiEA-wQsoASzfARvHu_5d5xFM3jE9ppuc5SthrHnE7BxQvBU8pzbKc2j3ky2mwCvMEMUvTHn8zv_gHE9ONRCaiYdLwC2iduZ7VzKV8tsytGi9wckFO0fmVqmui3Q5BlKRZWA_GHSn0LmzAj86r13XOndh-CyCxf0Qu9ZG9Ksl3s2spM3qdPgDiUMIl5iucakWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmNq1WxsIrt4QZu5ffQy0rtbKtWNCOLaAISLd-LNGhxQGS6Oq7zB_hdTEkDUbnmVX7ctfos5Bq1-KvTaSy6e6Qn7-aMw-_T75x1F-kByK4u2d5qkWHxyVeHUk8jMSJMotTMzo6-Z3hOSkgYMjb9I4fNmKuW03xoFmkWI3QtHTY90Yt0S5CVYPu-Ov14lP9ghKOak3oHazhYCK3bbyplOQrN3NSPovEQweTtZI_hJvJ-f0P8SY85dGK_kbvUuDeuFdqDf6FaCt93MdgpU5aCc0jlA5tkWZn_TXZqCtD08WTsTonOLVZ9uumW-MrGy6gN5MhY9GKBjK-wZYjedUJx9vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebtVD3PLOh8JjVuwgv2_Wl65R0EP1IJc1OZVs_pbLbhZGsz6a2f2KzffaFZD7aGAXdi01Ay3dKg95YF01qfxEoW-_fuNsn2oTZEGw7l83W1LN147_wzlKPrVLo6JEHKXZRd8KB6deTMT5uvDVrNKLCPNPLZm_ETseufHET8NfBz0xtpzRnCt6viLCdmk9rL_Ox-QtU8SolrOs10ubEUWCbcM4Q9ePF8wRtLSL45oL86CjDlxYHkWzT0yH_KyZxFsH_oig5m5KsJgv9KkpigK0QZvNFDkjVZHfgtMkL9X6zi7KFB6PGF1r6BiFfI9JgLeyQf6JDppCLAqk1z1YqFRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-E0Wx1YjQxEd5bS-juW7W_Anvz8So-yVbMgZQ4K0Gx8cGLz_BOUMqzsQGE1TSY7aOrekiry31CgS6y_nSQdT4tw9LAZrLHy7Q3O0rFZ6OAUupqsyV8OlQjfJhXUypDm_3k7fyw33wRgVuqAGqX83XP55y3AXr-nBqKBsm7sRKFVowgTmlfL5nxb05ZvFLNM2DNa9xpfiFz-KuyFY81KguXp4MYLvN-UvjAr__rVIv62EZFivH3t8Cg8QVcj88ybtlN5SClBTnYQx86cJu8U0f_MPMY8dHwyrOtmdpxsDihmxTqv7i3DdqqN_hUAOIbVp3aEwjH1lcelpNci8Ol9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30370">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
گل‌های تیم ملی ازبکستان در بازی امشب مقابل تیم‌ایران به این شکل زده شد؛
گل اول روی پاس گل دیدنی احسان‌ حاج‌صفی37ساله، گل‌دوم پنالتی دادن بیرانوند34ساله، گل سوم فضای خالی شجاع خلیل زاده 37 ساله به بازیکنان تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/30370" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30369">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlWiI0FId_ShYZTKuxLfVdUalazaHyncb__aXci6Jdnus7Irwprmewx36DafzgsJSWkRjL6HCHLBbrsa7gSHNG-0hm-tAFvSd7Hwm5gXaA86wnX3TFN0TZrF0ijVXc_vC30Cmg73FygI12rCxgakKku1yCR66oxR7AhDan7Bii3KNc38hBZoNUuJXydseY6t2DxxpuKCGcj2zmj8E75eKjhtDy37KrJA_0PzlTu_LftFoxdRK8T0vtXJ7nvy1xgm5HK3FRabBadAfPfnj5TNEtuuQHl-Q_L9E6cx0ZSWJC5YSBh1ImqLEA2JczqojlRVHz62kyv2ywPGdhC5hIWJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در روز پیروزی ژاپن و کره مقابل حریفان خود؛ شاگردان قلعه سه تا از ازبکستان خوردند. این نتایج بازی‌های دوستانه تاثیر زیادی رو رنکینگ بندی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30369" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30368">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30368" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30367">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bl62C0F0IwQN6Nzu6XY6zJbSQ0ihIL41QNHSS7nsu6Dy8_lgMHJ0Y0dAMZsx04LF-3ZpmaSYWn0rRkK6Yxfthj86a28k-Dw928F0DvKSGfvNH2D04NUNrBhCt9wSeZIo5ZZODiWFJvv404CpTgLA-v86IYIYoiwe0Oq2UaPraNNA_n8ha9643rNs_qHq_PQPZn7sqohqzFdUTNwQVEuzyaqW23yPD4IqEdGWJdRckaBQc44TlfB9rcOGB4Cp40fkJD49sEHY7nyAEqCVF1Yd9saaA4SmaLHQSy_bTM6TaDjpEaZgjxD5TEAz9XsHf_ezLL-ZntDii2M-uAFP48k7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/30367" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyDkcHjDveWSBHp8V35pJwld7VVpKBn0yKdhhNCw4pHqQ4v_XuztKmcOWNboKqICwgZzLXVZ7ruaHi-6X9dqqcF4ilDxmBsILCdwkyhEC1NtbczElJqQkh_cr04576ZIsoskcOS1PEatVEYbdwtu5fniQpW7SoaY1D2mGuYtg3bQSVUqqMOTT8TmX16exuO6oabounmOFOtEzX8P5VtzmN1xaLdYGkgbRJII45jHA5VTTayl2OTEIISHcpY3boOe9rKhEKnmWUtqJu1sDZtWOoh7YlT3TpdHgHWWn8CewXx16nHOPrINtdeDk-hFaOp0gcxH73CXqAxs1MwxedoXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/30366" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CahFP-Efb--p4qAR6W5QU-3o5oOiuEuMnRAq1J5E010f2IKs2j-0lGbwy1zbEvFrak7vxrz9o5MqoCdZmpVzg5K8DX-nUaaJIf10CfB2i2pxMzz7g4PO2tyfBukBy35zJIbkccI_j5EUC8v2u_0bcISh98LsWp3ahOCAtSfNg2CXRwj-OzIedd0tpwP2yr2SgGFeh08WL2S-Co1m6jovi-MhxV4Wk0LNs5-7E7rKuWYXbfFQLkigu-GrEd7rkZunGOMBBTRvToWDyyfEeMgAeGv6rd2-29ksdb3C9f0tNRdtCjik6fHdayom-iPMYF0RoY7hdpWaDdUw6GdPOo3Y_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g2
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/30365" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfGYeMqI3Z-mL4n6gGlY1cWR-FatlXr0oSCf3J31QOfiv3bZ6-FtqPwoGr-hD3yHLMIKh5AeoZ2cGPmInRGw3LIAQJ9doBaoZbwMnWGsvOM8O5XDLuEIRZ5kuB3IQHtG_ntSHgO85iRaINnaSf5tuzhx79IZRuV_-1aB0_LLganFncHg18LIhxd6-NbipiJwso7XxrPAkvtVOo29-EGc7NIDZQW-HnKSPmQt7zkpFCZaDBAgM5IurnkolD0YBrSySaM2lANlh_B4wEOyE47XEwscq-6v3t54SfMFHPMizGUYJxwSgzarnCNGKoxaayz6xDWYMiDr6pyeBdD6Anedqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
حسرت ژنرال در پیروزی برابر ازبک‌ها؛ گل سوم ازبکستان به ایران توسط نورچائف در دقیقه 95
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/30364" target="_blank">📅 19:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=pLECY5iY8C57fdU-jzb6Ls1WPSjQhjfu_uPO9atYVyvMm1lUJcSVODCz-kN0rYuDvBeXV_iTrfTz2b0hmihcQLVKAricHR2y7_RiNWf8WBTnAB1tBanuY0bLEOrYl1ghHp5Qb-H7s3Kurww8uT3rh7zAkW4PRH6QC9qkPhruQKTQv0bvG1LDYseD3rpN5NV5RkL4QZCLp-nV74MrcBWftVQ9yQN-vT-w7OLUQ7RD5_Y3BBN5Kv9PQVxyL3RQtEwCRQYD59peFGi-flTCsUEhDLtWEEpIaFW_nMBfm5BB4jFjvBPcmuZ7c53DYNpnp2X-m2ObRNEfeFcXqbcxtCWUsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=pLECY5iY8C57fdU-jzb6Ls1WPSjQhjfu_uPO9atYVyvMm1lUJcSVODCz-kN0rYuDvBeXV_iTrfTz2b0hmihcQLVKAricHR2y7_RiNWf8WBTnAB1tBanuY0bLEOrYl1ghHp5Qb-H7s3Kurww8uT3rh7zAkW4PRH6QC9qkPhruQKTQv0bvG1LDYseD3rpN5NV5RkL4QZCLp-nV74MrcBWftVQ9yQN-vT-w7OLUQ7RD5_Y3BBN5Kv9PQVxyL3RQtEwCRQYD59peFGi-flTCsUEhDLtWEEpIaFW_nMBfm5BB4jFjvBPcmuZ7c53DYNpnp2X-m2ObRNEfeFcXqbcxtCWUsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
🇺🇿
شاگردان قلعه نویی دومی رو خوردند؛ گل دوم ایران به ازبکستان شومورودوف در دقیقه 58
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/30363" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30362">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8DmfS0p1e0eqDAjX6f3L3PbzGbQWm0DCHQw3lYHJQfYaZU-EL2LK6bfsQBzwq277nM6WMTMmXqUVz1DJI71w_CVeWWLW1v9HeE0IUlCJqdTwCgji-n1isQGLrI9dyTQTjSYi8Yin8QpfIImaJFyd7X2D5sWEn-PvxEruTI-MYTlJ4OflJoNdJoLGeLEAKFmP8FPOsl-sMBwGpz0_No5dDGi7clo6oF1s03X97M3nRjYeRqd1W24EDp1nZyQRfuyogONK0H23qgLSzI7B4ckgHuSB7UgsbraLND_rcFz1frhMjeTlY9QVxnT-NG-e8Ye3Kr0n9c-FuPFTjjVOlo54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/30362" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=GdEE62e6LyayvXVG4SycWIuGSTt_tfufq9q6j_mnFxiVxCWPuce0ht6gGHHHlMq1INn0IrWmnA-IIrEi8iJ1ZqqnQ9KKZWDjFqWfpP2ONXKQiZnxDs7qN6hnkj8aWnR0o7hw2RKpQrhCYUrwfe3235UYD46cJLJgQz-NdEHpBv8W1ajRAL2p__777a_1CRELQVT00ZUyTVO7unU0Va3kACF4ay07iRhYGNaMP1Lr33AE1ZJx3Cpy7LSStnhUd45AuMy4YAsHhmixsmre0CAeEh3Mokry85TuVG_I35BW3n-C4olRZ7Pz-mA6UBdqKZXl4wyHCS7XDzzb5eS69jO54g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=GdEE62e6LyayvXVG4SycWIuGSTt_tfufq9q6j_mnFxiVxCWPuce0ht6gGHHHlMq1INn0IrWmnA-IIrEi8iJ1ZqqnQ9KKZWDjFqWfpP2ONXKQiZnxDs7qN6hnkj8aWnR0o7hw2RKpQrhCYUrwfe3235UYD46cJLJgQz-NdEHpBv8W1ajRAL2p__777a_1CRELQVT00ZUyTVO7unU0Va3kACF4ay07iRhYGNaMP1Lr33AE1ZJx3Cpy7LSStnhUd45AuMy4YAsHhmixsmre0CAeEh3Mokry85TuVG_I35BW3n-C4olRZ7Pz-mA6UBdqKZXl4wyHCS7XDzzb5eS69jO54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=H67f-grpHFTMQ6NFgSYypc55L--t-i3vX2MQVa2qZpNbEXQ7MF8jjiDBPHrOXt2p9CYbZa6Al-u6W8mLozsA7LL1BU343GOsncDe14rOkMLescVum6J6ltrQRfkgEfQ1UoFHUEWbHgpL4Y8n5jDySL3Mdk0BqXbzoAy1PJkuNAb6h_zh01lVGywNUDprlDZQXiDxKFIZTzYYrew3bRWX0SIFkis9Dht2HSHbllrmGM0v0Vw46jhPtlB-vwuxbPpSldXASq9Xme5PTyUb5Zo_r-vnKkLineXiXU3S_YYYwhkUs76xr8ol57BvKCuoLsB6hTgu3UfSlywePo1-Psk5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=H67f-grpHFTMQ6NFgSYypc55L--t-i3vX2MQVa2qZpNbEXQ7MF8jjiDBPHrOXt2p9CYbZa6Al-u6W8mLozsA7LL1BU343GOsncDe14rOkMLescVum6J6ltrQRfkgEfQ1UoFHUEWbHgpL4Y8n5jDySL3Mdk0BqXbzoAy1PJkuNAb6h_zh01lVGywNUDprlDZQXiDxKFIZTzYYrew3bRWX0SIFkis9Dht2HSHbllrmGM0v0Vw46jhPtlB-vwuxbPpSldXASq9Xme5PTyUb5Zo_r-vnKkLineXiXU3S_YYYwhkUs76xr8ol57BvKCuoLsB6hTgu3UfSlywePo1-Psk5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK6Bqorp6N8pAgRrmFcvh4vWCBLada4WVbX-EKnmYFVdClBrGM3opnRuwGT6XLBQijgwz63-t_9DzAw2C2pCLenpaCQ9H8lblpMdyc6CLNMYK74baHYFPHJznbCcYOFTHMEPcm1RHY2-c52y-i9UtjFj8SRcTG1NWqAfcDGLoIbWWLhLc_8ydJCyoNBR2eT4mZYc0Fk9HK01YWD338yRkSlo5unqq-DrwCUEz3LASDhZR82F89we94AiNEEkotxGCCCNSLEzQzuRsUwyq2BsmykNaGKBQHnjyksA10wzpegiQdoD9hG9mMYxebB2shAfj06hGgf-yVTcdiBbbaSnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=XoiNzG29mhNLH9IJ-sgM6pVNNWRQiOsi2vW4qY4ZAUEDAuSh_dtM6bSrQzdY461hn9OoEMAsiNHXMzUJEmUq2r0u_7uWSO5o1EfnQkMieRL66kpDmh0chPtSHWmK9Ky7F1AYs0Ejwmgxq7Ds-HvypNOi-8IS4xlytBolt1i38jyFBijXlxxwIV2mfpv558UCnw9Nw92LUb_f1F_Y8fUgM0ckkUcZltG4xTP4zaVU-yimOgYyeVN0Re-NeO3XUEVPuxE4o5-3mjVYzGQX0INXcMY_HlsniMSW8mdPSw3O5dtlYwHfTdRGPyOa5NwVFUYPczU2x8qB20pD-rTeceEAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=XoiNzG29mhNLH9IJ-sgM6pVNNWRQiOsi2vW4qY4ZAUEDAuSh_dtM6bSrQzdY461hn9OoEMAsiNHXMzUJEmUq2r0u_7uWSO5o1EfnQkMieRL66kpDmh0chPtSHWmK9Ky7F1AYs0Ejwmgxq7Ds-HvypNOi-8IS4xlytBolt1i38jyFBijXlxxwIV2mfpv558UCnw9Nw92LUb_f1F_Y8fUgM0ckkUcZltG4xTP4zaVU-yimOgYyeVN0Re-NeO3XUEVPuxE4o5-3mjVYzGQX0INXcMY_HlsniMSW8mdPSw3O5dtlYwHfTdRGPyOa5NwVFUYPczU2x8qB20pD-rTeceEAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KwrZdLPbTe4H1SUYd--K-WQ66Fq_ktRFZiZxD6O_SWOJBmBCSfZ1SzfyzqN37C27tcuSpbTKdrEJfjQheZZWegZxhsI3BRkfTQqO8Y0f8KT59jFZjNgTENFMhBt9ummVodr96wK1YC9lwXrQg3ty55IUp5FLo1nbGZzl_ntvA20hjgW9lZsz_1XfMYIlnyPX6qLMoTvj3Jk73PJDRCbBFRw__1dRuNtdwiKnqw9ScfU01IbdlbCOAHvWrGzUVqyCH4ExhqSppGkX3OZnefT4mdCWzbJkg9oG4rMruWdQPfthawZh96kTw2TDfEDE8tv4MxIOLO1MWs2Tz9yc7zZY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=KwrZdLPbTe4H1SUYd--K-WQ66Fq_ktRFZiZxD6O_SWOJBmBCSfZ1SzfyzqN37C27tcuSpbTKdrEJfjQheZZWegZxhsI3BRkfTQqO8Y0f8KT59jFZjNgTENFMhBt9ummVodr96wK1YC9lwXrQg3ty55IUp5FLo1nbGZzl_ntvA20hjgW9lZsz_1XfMYIlnyPX6qLMoTvj3Jk73PJDRCbBFRw__1dRuNtdwiKnqw9ScfU01IbdlbCOAHvWrGzUVqyCH4ExhqSppGkX3OZnefT4mdCWzbJkg9oG4rMruWdQPfthawZh96kTw2TDfEDE8tv4MxIOLO1MWs2Tz9yc7zZY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC7VuNo2YjuJOh7E_NCUOWTrKj-at4lL6zbEaU0tMJ1sPINdbHD8qz7dMHmvyuBs4T1BIYTj5RHrzbJuNMorSWbMDjYlWUDcEPQ1m_2Dg3RaWRkQwCzVW7Pe46U40irvNTIT7ZbEfjsrcVCL4mXYMP2uLxaHd7UJsa16Ye56L2hh41VAP-Ud1Fg3BjsOTkDfXfV7AVPH3uQZ4WVYbmPfe1YsfaKrmm1mJvpplRCx6UNem0bjUBi5RgRtITTwgZy25oVWH3HVYx-_Hzz1nh7HjNVTB9vYv1v71ba_Gj6AqLe1taecAAJWN9H8yDjdnOWO3QuXfQP5U3kD7Wmdpfot-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9LmcpZun5H_AE9mzqVR2p2Uo1LL0AP5dNcKWfUQRUxnox5pc4x0xpekNeKP99XLiKfuN1MBGpRxn0aJFLsBBdrQ0f-0dTHJlBjaiR9ZqPWmPv4EUT2XjLWL6kUmraTEMweAUkMydIx5jnTfl74opRO9755S7hEL5oMMuwEY-rJBOsxnPnqhlDfSmVlt6KjPPL2U0W7CWUAP_01pZRER18eRrPCNqtCZUjKCCD3-PJRxKqxJ64aGy5hICIQ4ZV6rWMCHrnf13o4CzWY3etDjgsLa24Qz3eErbAB832bDO0KM8y8dpwu8iPxtxVp-Br3VND_O5QwrkBRxJnDu75VP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=VF8R1kcwF80K-L4aITLTEASqRMEcRmxUhnGm3IdvCyKKW9YFArv4hGVcer91ptrh7fwqDywkJU-zIIOD6AFELZ_hpMIsp09Wmlm1vcm27dXcYBVZqnBf6TWW_MXrgvlmmjTZGy6N2xZao5b_DNOhnBMmYE3UyAwiPxlZQ6IsLFsQZ-0B35e9PeLuOka9Gx9LFLC6BUSpp7aZDNh4vgnzb4yNRNZMAswPdXZomuaKEdRLl8aYGJPFE-hMZX-JPrfgxwwTzAmZdlFTED5BUENML_K5heOJJG8UstGwn3BbtbfUmf5V8iRTw4yUNBb0YLAgTf2jGGvgOLZ-BBU9vY5D2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=VF8R1kcwF80K-L4aITLTEASqRMEcRmxUhnGm3IdvCyKKW9YFArv4hGVcer91ptrh7fwqDywkJU-zIIOD6AFELZ_hpMIsp09Wmlm1vcm27dXcYBVZqnBf6TWW_MXrgvlmmjTZGy6N2xZao5b_DNOhnBMmYE3UyAwiPxlZQ6IsLFsQZ-0B35e9PeLuOka9Gx9LFLC6BUSpp7aZDNh4vgnzb4yNRNZMAswPdXZomuaKEdRLl8aYGJPFE-hMZX-JPrfgxwwTzAmZdlFTED5BUENML_K5heOJJG8UstGwn3BbtbfUmf5V8iRTw4yUNBb0YLAgTf2jGGvgOLZ-BBU9vY5D2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30352">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogSbrcjZh5Sy-QJwC5RyA72NA9_0n3UOPj-SZyiUmv7tiXZAa2OCeCH3cOpB-iF_mX0rFTY1Xie8tmiESW2jW6rUs3AQMBxGt229zrHLYqiZRFxBZksihqcYy2CdKxRJ5ju52jZcqZ5pGIc3sWOcD1Z2Fch6YG4NtegLFLJ7qRbQrD0IFkeoBqePo_aFwJuBHXyQyyOAdWe09N-Tkgp74XwcY5gM7or0Tvi_E4U4XQNeKyAFiBF-MsTzXnz9O3_9tQwWcqF-ZkISySUF3Z3VSORLcbusNJM0Iamq6LxoaJfV5Ba8Td_Br-i2yHOUezocGfXwCg7wUMWvvEZ8hMG5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30352" target="_blank">📅 16:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCpapDqbWBQJeiraQc2tH-hAAVRuX4YzANYL5OPazFzhaQ3SrivIYA9pdQ8WzSVh0ckSURuT5hkoSOOiUgD0g6ZOJHD838EONBHl5CbSgtQQuTBnHvIcsiW5dc1TQnQntUiXE7U3hYbjP_ruQN29vV8vFh39MhV6sUAgHJ8YC67leQtTX3mnDtuQmgoIMaUPUYXYjzPaHvLDOVvGXahQZFBH05SDLCSaTomO64doHfHtGqwmJjpDhou840K0PN08f04EK5zWIG4GLx8xW5cl_3LQR3oVFfgyxz6D0Ye_uxN53QNjCy5KlklEVzPKB5CMryvB3OvYrv4_q7nLxJMq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره:
من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم منطقی به نظر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/30351" target="_blank">📅 15:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A57RYLGqEV-MX9eKoGVxSBBgTwYpHWZbgXHcGcOxqwKzP-1JYlP_MMSussjaXRkicd7p1-HCBsN0sfPUxRAtmsp5S1zY7kdOn3tNFH_faxFaaB3SRzCJxDS1it0oN91ijIw4ZfOazOhXfw37C61q0LEVCPXDyULD9SNPY5Q58RZpc-ObZjgDO4maTtfMYI3Q884UXZgg-C7o5nNOU1B68WF-GVHDFb0EUZ4e4Qwp15VnaVgrTI7C-aKYs0Ie6IbWm42GJH-ovUjiYq4cEbSy3wnH-M4zF3MRUFx0ghSUij6chuUMAGWjVINpKir8CbNTQxKx_oR4wK0NWGd0G4z9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گروه‌بندی‌ فصل‌ جدید لیگ ملت‌های اروپا که از امشب استارت خواهدشد. این فیفادی با فیفادی های قبلی خیلی‌فرق‌میکنه. تقابل‌های جذاب یورگن کلوپ، زین زیدان، توماس توخل در پیش خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30350" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30349">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPGPTlRPbLFRvQeLY6Ig9HCjbsmokBJlneRWLliF2VvcomPL0nsA5JotEp_jyyqWIRnnM-lImLd2mb5XhBjmaCLuCqdvolPWy6wjuuuO6asjbMssqaVV5XqKdSx7qkWH_1jO51XgjbBZc0ppepxvBSOcE_6oioNmWuU8IKvP3kl9eZDrjo5Zru3FRkjYdcss_zvcTx0Vspb48gRQdwhjwgmLSlkDByraMQWYV9BIBGtgIUh4Yo1uglhEf6fNl9Ret6ts92BiHOqsBUwcvLRVfcYMk4rArBdDubRXztIKx6J23aT27knMi6s4xGHRiF1mJ9nWKrSgNnF1OWZLvek4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/30349" target="_blank">📅 15:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30348">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Qr9r0m6tf5g0lvcZVcyFKsFkK1YTcQOs_oYbGlT5EvK-tySPFaPsgBullrduVlvTAXIoyUpnLP66_3PyoGoSawNc7t_3Jnx4JG0pgIagilAePXCbS2X6mLwR5fZOcY0Dn_GkQ2-5C8Y0KY1MSIwTlH8mN0OzyjB6WDIa1kv0IMBm6U335eKILnEjycNRuYbSkCiSL8qT0A2AzcElxMKCEZ-Ukas8EhnCb4yfQlFlgcFinBt7_qPnD9dX7WUkg2K9bF8wHIJI09PEZpSXd41lvTMAs796ntjJpbyd66ON8plLndVUGWQUlls8S0O1VtNQkRiJSXonuiGGc7_pH9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30348" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30347">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAIfCOoi8v61TLDooYVAiwbdCW_v9-swBonw86EhMl-HADh08aVSeJqOfewT0-QxRCnbnQ_z8qdgIi1Kh7ixgceg1Uu6e1UdP6-LNV9TLRhIa_5O1KyB7wfWac611XltiidpJO9gAlRzwWYxG1jwZaym-d3yyFpG9lP6VsBUziW2_76uXOpAnnql49Xn__e96n9ei_iB9rWnfDjdO1a-9Y8VG4WW2jCbTx3-Z_gWd4OKxdZ3DcKb697m3UL5RPZ70GLUl9nPCpqvKPdebjMEXo_jJlBGUhF9oPHapNS1PwudHm4d5c5wIHcVkMDa5vy4T-YwFOBfnLUc7MMYCiThdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کم‌تر از دو ساعت مونده تا شروع بازی ایران و ازبکستان
؛ ایران توپنج‌بازی آخرش با ازبکستان بردی نداشته و ۴ بازی‌از۵بازی‌قبل ایران و ازبکستان‌مساوی شده. الان‌بیشترین ضریب روتساوی بازی داره که اگه ۱ میلیون روش شرط ببندی ۳ میلیون برنده می‌شی! احتمالات هم میگه تساوی ممکن‌ترین نتیجه هست با توجه به اینکه قلعه‌نویی‌هم‌بعد انتقادات سعی میکنه محافظه‌کارانه بازی کنه. توی سایت زیر در عرض ۳۰ ثانیه ثبت نام کن و در صورت برنده شدن به صورت آنی برداشت بزن:
لینک ورود به سایت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30347" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30346">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3LIYguDFK42BRzU5TlwvXXLuC3Tz3P1UCNNE-Jo_vAIurQHuFh-kmhyf7tJs4XjAzzDKQilXEGav3E1Pl0qWQsaa2FqTMI97ROmB0Vp33ohAEzi2pMwzvGXzyPo_YWLBi4htmdIuD7xkG9ZCw_pBQvtRTBi-EnAasxhXmkQqRopmi1nXLqUL-3mDgLVdk0hvu96LLyL-asZZ0-wPXNyCxpcFWZIf2tMnK1t13ZO9C9682RY3WVOeI34ciT6MZwhB3T8JeGkUfcYOfdcjaRHsvjIBBcgRxoqh4kUc9mznQakrgP5BSOJ3arrYsAa0QoMBeYwf4_sS6ETykJmGgrzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره‌کننده‌وفوق‌العاده کریس رونالدو در سن 32 سالگی‌مقابل‌تیم‌های‌اروپایی در چمپیوکزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/30346" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft67o6_JyNJBVqq81AYE38__37wKcw99jiP_O3QUBAYp4sqDVoxHRD-ty6NGQWe_o5TCBsT0vhGa3LcSRVmS7-4q-rCukcr0eSHMYyHyCblHBcfr2mS-eB0_BojY_tBjEY4oLeT99hWdxCZaXEyUy7SaHXyFgBFkcbRv6_4MGP6PvF_lKn2YaWx2_nm49kVUAim4JFR8NifnIhfYNmc9W6t7B2_rM-qDyXpTz5rC2L5n2mHP62pkw41jJJU4EsTYalsyA8BvAysxuQxp3a3TfyxSp6JpNdWTOOUEnk7HkC92Aq_1pgJocmI0WwRBYKS5CoT4guYr_bnu2eqdIbETfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kImhB8l5yhIB5xhx22Uyw1-rETSup4beDHGq-tTGxi7_idLQagCQv1oSV3oAiqtGYw_wPp4nIJZ4NUAiux5MpbwpN4j7I_ksLFfTyUOGXl0JaC-a-VPlQyQIFVa0TrurlvB_kZPZW_I_eEbbJxbzqKTZ6b0HRHITZIm2-v-8vF4TZqp_HZHD8KoZeaslePywsrLxTD_Huwxx3_iKjkB9d9PbNNi_YUayOq8Iu1a9xcDRQ71rALr0KZKsiuhwhdstEtPVlQiUER1M6nfUps82AOQklMKdan-btdJpb2s9aj4k28IvHLP8C5bfC35nLhKe1Knf_qpnHyKatO9VCQGZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxNxfVuH0Z3MhzY9OTu9HQfWt_ft_tIxj4aDw-GElXjq0rpLrme5ko_Ce6p133U239tDLPZV2pnYBTZymB-Rlb7CU-d_NtBil8SCZo2DxecZ-XVDxz_Pe9afwaKD8nq6KYflm0LMWzNbA3TV13TZbzJnvOkQRYEVLsujBPtQM-7cY5WJ5AjIHxDSFI0Ze84r8Yg5lk-zlv11Oi_-PEPnNKM_0md1tiMWJiliN0hdRHGb7FT8nCoqj6AqMIUxdNtz7ECqKbJkr2k80OjOBHvCuVgZ4-IWRVLx9oiIt_ALRf43WS9kwgSpf2UNLnnuwKj_RvFkaQwqXcEh2Pm-1Pwq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHQI3rwzIVntOE2VYiT9qfmG_nSOYt88_ZLwh78t2A2BstfV_PGwe-CnJhwQCP2dsZdnPKwHEsYb4L0Pdc4NyGypZcKFjZvZOZWHdme5NWFOTnKrHA_zPPsd9hkPXYpmBs44XIZTXVsXdiUnrCwRQZWcMD3AH9kAgyOEISOcUZnR46czSB6z8-e9oqQDfnuQoX3TUcEcdR06TbrBpS7xCH1PZ1BES3QlF_lQnPErd4OaPvDPS7u8Uwd3MMtWpteGNgKU83F0WKwDdJiJEMRv8DdRffjAoVY9-y7q12sxLQgZ7iYBFhNBD18i_2tx32C-u5y69Rg856W3re4nvI4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30341">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdp4qWhbV19fq0xJqzGD5KrnJ_dEbWmBV-yAq2R2TzRrmu7GJ-bkrqNgZ9HJ_5K5bgfDoIT5zGV-ZmKhOXr0gXfdIaMe3Dz1vBSnr047K29pnMm42caBt89jTzTfWSYYgq6l_oHxn0dC6HSk2BBxzYwU30PDfgGtjG_TlQPCI6MORfuXbqL5f8IN8cfnvYqRkrC1jWs21X67EvgAfNDz4u4eh6S3ZVzmmC-PXB4cwT_HmnAfipgbqqpwbWgjI7k6GRnXOmCFxQA3pRqzkYM3-g2TP4TxFeujBnO-PjOzbg2Tz156lnVvSXz65ebaHV3Qe8LUO4NJN7eqF9_9gmFCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئالیا:
چهارتا مربی عوض کردیم این همه بازیکن جذب کردیم پس‌مشکل تیم چیه چرا نتیجه نمیگیره. مشکل تیم از نگاه کارشناسان و پیشکسوتان رئال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30341" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30339">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvL0fVMbd3rBp8i0S6p50QEWfiEwZypOfGu54OKyuNoSetYSrxH15CI_xG2LsueuBwAsiwBf0t3gSjSsBlLtQ0WQO6mWZk0WSuDb9cXgmo7Gbt-aw-wkkIPK6JGXFNZ7ZkNzcT44hQLzj2ZUdPUsfxge6QjCeO7bSkL8Y4KzsBK715WYsJ6JOaKA8r4t0mmc-MWcAwUYZi9Z9Iw_5sjLHLHlL83EblTFMwhkW1cT1uZ-f62kuVUAUvUf49E1GODeEdGtRW-aysG9amQa8TiGMe1X9OI59Yrq4lOKsJgKa5WpbSpiaRkkxdjKYUa4GtbqjvrDHiXdWzM7ftIpIT7kNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛ تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30339" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30338">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-8gQYirwy62f_37GxM_Oe1JRtjCMDj2fM5yyovrfxDPTrTf6Xnm6cPCLg5kQc3EFRTYBgKwu0vDWa56BSbo5eoBOCkAJ3l0kGjMekAvhz_MvFyZTZ8P5uLCl9JRaNjhV1H8wWr8WfgXqimUApmagSNeQ0BweDRQsrcihqiF50PjLj2k2vNlQ1sMtjp9FSyX_vwSwrPDCWqzebKMjuaP53Ed6h2rFEefXsNIwsS1oD3KI2-h-71jS91KJ1spd3zqmfccJ2CfmgRrfSQcMMwEq63wnuQli6sgYEGx1KhYsO9WBsmn8Z6nUc6gtiM6kq1Ss5hjchKJFCfMBEdelUcOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛
تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30338" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30337">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P24_0pES5NMJNJboSXm57oWSzXIo8eCyfjjvWAS_Ar-ogSqgA8kTfsuvvtpWEIaA_EoW24OUvdl-UL4gBhNwulBWS-1FdHfUfsYpFGKta-Au9OK1tjYSo6jowcVndbRuyKQ-Tu36yPcSi7HqxVUHO7IkxzkwcYqJFJ2qtNvhp6FZd6sOqgIVdy_UtGKb5JHH0H3I3jmZCmcR8DjyI90syzFBANDYfBbFxbR5WsrjpJiGeXwPqK8HmOxR5KpLb1sYb4366iqKnV21Tyo2CetNhivddBhrHgIvnx2AaW9wT1qHoa6dkTkv1O4s-XNhMGj-YH0n-OyyfmkUcblc8yFTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رونالدو 101 بازی بعنوان کاپیتان تیم رئال بازی‌کرد که رئال هیچکدوم ازون بازیا رو نباخت‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30337" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30336">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPvIfhgN8voHYeKwT1VVnIxyhHiv6w3UzCgDrZugUmduLl6rKOIi36l4ee8HInKPYvw9SgJ2hegSxkybe5xTlNxe9XZ2ssg-YP31BeFGNT1fz2xgKbW61Hfvch924daqCvRI0ghrQyv7TcP4X4atk-wthPdpWVUzCsx7H6dV1HxOmCmH0WLCSktpzklAKW7kcQfFDYVZ5Hof-L0lnjCPgmysDugsGwEmvRwmhypK7ugcaOfu7_D6vGdCQtujoaZh95YhbcOFOVwUzXubIn0YqHUMqPnXJqYsdXfcFpl3y2sqr5cQghZNCZ97Dwt_RlNzxe3ghU0qqzeMqWwbHUx07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
میدونی تو این اوضاع بد اقتصادی تنها راه رسیدن به آرزوهات چیه
💵
💵
💵
🔥
سریع تو کانال زیر عضو شو تا با استفاده از
فرمهای آنالیز شده توسط یه تیم کاملا حرفه ای
یه قدم به آرزوهات نزدیکتر بشی
🔥
⚠️
توجه داشته باشید که تو این کانال به
اعضای خودشون همیشه‌هدیه‌ی جبران
خسارت به صورت کاملا رایگان داده میشه
⚠️
✔️
پس سریع عضو بشین چون عضویت
محدود میباشد
⬇️
⬇️
⬇️
⬇️
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30336" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30335">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw2DgXT2vSL2XfM6E1HlRrsOQhKdFkRye9SgNANgO5Az3a7LM0OgpYmmmccgp7MHypNI-U7MryHhXnIF4pogkqTYa_3QU8VBQqP0eE5fzioDMe04kfPXB1IHImnkfwp9k6Q1D2MYLbsnLbDe5GsyEi4EimaIur4jysghTXupGAimvX7z7M8DTzI_1CzsrdwnkZ1Mbjms_llsadG5-MtXzrTsROyZJL0Y4FrdfcTIBKiOJJ1-l4D8r-TWoRd_DljRF4-S9zXHQnZJsCrB5h1XrH-LkTaWXQbOWg3z0i7R90Smu9-n2UF_ChRhXr8etsdED6T3patXtVWtYq6nShxRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سابق سپهر حیدری: من زیاد اهل فوتبال دنبال کردن نیستم اما در حال حاضر بهترین بازیکن ایران چه ازنظرفنی چه شخصیتی رامین رضاییانه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30335" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30334">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBydeWceUXqW-5Hw_wKD3hyhCqasWTkBa4BSPSLjtuNVuhz0vP3k9TwF1zJNMvm0CymLK0HQq_OoX7m-0n3BX-mIDq_sv0NtwpsaCvlJDReihrUlNqblIK5yhHZz7-vyyexcWrSDDr0-YwnwIm2wTT3gUdblZXY7swU4pNedTZnl0B97TAJCVZ5xSqs7gqXmrVJPOq7IqISn27XblSBjM4D9WTOftWp28IpnLCV_1jUAyrPN-Q6s2zECdwN3pFqtI3e5dYO_tkzQ8Y5wvH9AmyFh1ih0kqwjTn-1kSrmAnB42tO1cPnQktc4XgSQdEMkOZi31Rpx_hgQgd4Lugkxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعد از عدم علاقه مدیریت باشگاه استقلال به برگردوندن دیدیه اندونگ به جمع آبی‌ها بخاطر مدیر برنامه پر حاشیه اش؛ حالا از تبریز خبر میرسه که ایجنت اندونگ این بازیکن 32 ساله رو به مدیریت و کادر فنی باشگاه تراکتور پیشنهاد داده تا درصورت توافق با این باشگاه…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30334" target="_blank">📅 11:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30333">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=BUUl3gelzyRu1uzbScPkIcnR9SqIy7GICiL0Vx_iFX1PZfgk1M_ks_XPXeVTNYl5h9g6FAkNkWUBPIDXY8QZUlzP9ZIsCtaCvoo2E79OS1SNY3p2f7ug5c7v0zeKxFWY0f1qmxAmfQ0G0gmiOhuEychSrm1qy2pCYXH1d-36EEp-edMWdlU-US0Im2JKGKNbnXKwQVweArbRUCLzS67FQ94QrRl_Sqf5ZkCJo552eEk1qsqu0uGDcvt6_-BpOdstxe7sea58ZAJovrb5DEcdGoplZC9NTq9rBSeIdKpYB0qx9GfHmoOhZUL3Hu0-ZTZMXjxizoHLwhAZNKPxhxkB5LIOmXxN_6zOgrP72LM8dkFNXLNyGXoVGibRl8_K8BVa-V-KLg2QAEW0ecg-uGgNeZ4v5CacP-Oi7_rApcpmSIXk5YHXR5CfA6Rm1qBBbFH9B7TU4XWFPfInBCKOgGLgLFrro8BZuoR-kuOmIvYGaZNGnB1ciVLVw1_xLSqy_z8MbuBkmSxziHcBMHKEzZDMMg0FRchgpWyhTiomvUoBQTje7WtIQ25gVU-zS9gEf9_tx2-t9-ht7t9MVrKMifYD_dEhYIGNT1ZFadkLbgPVSOjv-0lAbT2A5ifGZGfxdElnZ2wOl2YhX3buLJhAHCYfVJmi2QQap0pi-EoWRI3L5mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=BUUl3gelzyRu1uzbScPkIcnR9SqIy7GICiL0Vx_iFX1PZfgk1M_ks_XPXeVTNYl5h9g6FAkNkWUBPIDXY8QZUlzP9ZIsCtaCvoo2E79OS1SNY3p2f7ug5c7v0zeKxFWY0f1qmxAmfQ0G0gmiOhuEychSrm1qy2pCYXH1d-36EEp-edMWdlU-US0Im2JKGKNbnXKwQVweArbRUCLzS67FQ94QrRl_Sqf5ZkCJo552eEk1qsqu0uGDcvt6_-BpOdstxe7sea58ZAJovrb5DEcdGoplZC9NTq9rBSeIdKpYB0qx9GfHmoOhZUL3Hu0-ZTZMXjxizoHLwhAZNKPxhxkB5LIOmXxN_6zOgrP72LM8dkFNXLNyGXoVGibRl8_K8BVa-V-KLg2QAEW0ecg-uGgNeZ4v5CacP-Oi7_rApcpmSIXk5YHXR5CfA6Rm1qBBbFH9B7TU4XWFPfInBCKOgGLgLFrro8BZuoR-kuOmIvYGaZNGnB1ciVLVw1_xLSqy_z8MbuBkmSxziHcBMHKEzZDMMg0FRchgpWyhTiomvUoBQTje7WtIQ25gVU-zS9gEf9_tx2-t9-ht7t9MVrKMifYD_dEhYIGNT1ZFadkLbgPVSOjv-0lAbT2A5ifGZGfxdElnZ2wOl2YhX3buLJhAHCYfVJmi2QQap0pi-EoWRI3L5mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری درخصوص دعوت‌نشدن برخی از ستار‌ه های ایرانی به اردوی تیم‌ملی توسط امیر قلعه نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30333" target="_blank">📅 10:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqUB42ZUqAaLJWfniMMMt66DqGZTMJ5ZHJWHn7WU-gq1r7lg8-hjyxxmP-L89fKPtFep2rCh4bN2z78i9lyYax1KOoURs0dio-aMSwaN0rTL6cO39W5IuH4SPRxy32IoUGRqMq4Qj1UEt-KkKpGkAlShk-qjWLEwdN0oQwJN6Lp6V2ZNERjHiOnBlsEvK6N8NQik7BAwA5DHC0nUZjcS00Z4CONLBNWrQ6fXx-EtR7IYsl4gNl2EDVF4klvegH9kcmlY0wMEKjl7ti7eTbS6W1fI7Wanpm7ygWk7rNvKvGEA6m7NCs6TjQM5NmcnEn_YBmLtvSSlIldFva8P8Ytd_ge0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqUB42ZUqAaLJWfniMMMt66DqGZTMJ5ZHJWHn7WU-gq1r7lg8-hjyxxmP-L89fKPtFep2rCh4bN2z78i9lyYax1KOoURs0dio-aMSwaN0rTL6cO39W5IuH4SPRxy32IoUGRqMq4Qj1UEt-KkKpGkAlShk-qjWLEwdN0oQwJN6Lp6V2ZNERjHiOnBlsEvK6N8NQik7BAwA5DHC0nUZjcS00Z4CONLBNWrQ6fXx-EtR7IYsl4gNl2EDVF4klvegH9kcmlY0wMEKjl7ti7eTbS6W1fI7Wanpm7ygWk7rNvKvGEA6m7NCs6TjQM5NmcnEn_YBmLtvSSlIldFva8P8Ytd_ge0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های محمد احمدزاده سرمربی‌سابق ملوان درباره سختی‌های عجیبی که در زندگی‌اش کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30332" target="_blank">📅 10:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30330">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYXAL_o8U0U2lNcnXN4JX_D623pxaLWxIWnMtqnCyfh4o2T4mcj5LkIMM0ozpx9jdUI_2bH3G9S61C1WccDn2P77M9kzkaQz6pPVEy1sAwiKgrbZBSHXh7neyU7r3G_Jp7xP0MnnKSXIcATTpBSHT04wR2xVNlnsjK90xz5mrzMhpOCXeBcdywP_dOzTqp0GOF56AoMMv1j0jwRbu91EYekdRNh2A7VNqY5tMnoG8dBWp5YpcVCBOeKiSmxqIkluFfBxPSurBHVQrpzXMyzCvSoV1BxG6RD6n2xkPmJTDQLnUPqKAQW_rCDMAmTzVGt4zMTgXhfS_vzT5NDD7suw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8OsJzMexfPTsP990pKMSZ9sUIztK7u-xbDXG-kAV5-vT0SVYKczaEHXyQgZOBOvN1UKGpPPpHr54hzqWqzldM-z-K34WYGbiHrBU12NSqRiB0n36caquLrepNsEZL82l_jU7-OpgkzprBDo2h9g-tLMpvZjJ_myUiFcesNP7gsBpS6F6V-q436CS01iTg63MC8vN4cUPw6jgAKLOZKhHO4_8H5J1QqTSux3xoMI1zYRwBDhqQCYH4z2cH6ef0qKw1z-p2Ith8qO8PQpqg5dypChJKV9KNE9V_qkUMH2UkxvuUw6RTu9vHBmDhUcSUnNxOFZfXuPVrCT16qrs__z8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
فلش بک به سال 2012 زمانی که:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد 85 گل به ثمر رسوند.
🔵
پی اس جی 86 گل به ثمر رسوند.
🔵
چلسی 87 گل به ثمر رسوند.
🟡
دورتموند 88 گل به ثمر رسوند.
🇦🇷
مسی به تنهایی 91 گل به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30330" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30329">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=akwDeo9SKfnPnGLeGRT7qKAUnTN_LJwS88txxdS2NlTUc_3Nc1p1ImqrTTHDzufOe8V5Apk0FTVfmXsiewoZYZ2MxmlGIIuGO8DqdY7RRi_F4DHg7Ir7v4LqQJNc3jad2EQ6Ay9EQPxVdMP9uQCiIZd2eMLoIGt1TSu_Ai4xlGyESiUJ8mxhq0bDlYhfScXs6u9uB2mse64PGV3N_ofT0DfBMjCZpYQ1z-0VH_LpdI269IZ0ktrLmc00carXNIGmK-QGMyjYmajL_zTY_aB84B_m0bOp9YSbLaUWTOWXS6Lhoq6ir1CcthgybuWR4X3_SWeQK0IS7OB4W-OzRLTTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=akwDeo9SKfnPnGLeGRT7qKAUnTN_LJwS88txxdS2NlTUc_3Nc1p1ImqrTTHDzufOe8V5Apk0FTVfmXsiewoZYZ2MxmlGIIuGO8DqdY7RRi_F4DHg7Ir7v4LqQJNc3jad2EQ6Ay9EQPxVdMP9uQCiIZd2eMLoIGt1TSu_Ai4xlGyESiUJ8mxhq0bDlYhfScXs6u9uB2mse64PGV3N_ofT0DfBMjCZpYQ1z-0VH_LpdI269IZ0ktrLmc00carXNIGmK-QGMyjYmajL_zTY_aB84B_m0bOp9YSbLaUWTOWXS6Lhoq6ir1CcthgybuWR4X3_SWeQK0IS7OB4W-OzRLTTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30329" target="_blank">📅 09:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30328">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUYL-tURJK8aa-EqW3dVXCX2Mce_fmOxo__vJlE7OCO3AikIL1vKTpauqnqZbzJRq3bE84pqQlCHaLJwmlRZzB_5toD83wHlSqYixYGsMlSaPPrL904vN_UFheps3dVOBMOh11nUAOhilK-lm5Yey7pBPOQstd4Un23mCMoP1rvoWLykaHo04kEFZhbcWKsJM8V2rgv8kBKFRGyQ-LAWXtCoExOonhiilSinucgFDKvYtJwvor40K66QNz4QNAHdcrP--HsHSquaO4-H3DLkrbFmc-YdhqTtcBa871VRcsLP2Czmj95EqwkFrV8p7068p4Q7mJMo6HjDKG2g2LQx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب ستاره‌هایی که علی رغم درخشش خیره کننده در دوران حرفه ای خود توپ طلا نبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30328" target="_blank">📅 09:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK1tqY83ERrWlrGZb2KaTNvN8qcEdwrC-nDb9LMMiW3gWBqIaf32AcpyMzrqbKJfRpk6mriNPQR2UXKgnFK8acieKxOsuWnruxMmtsorMl1jfmJCOGfO8N6Od4UG926PA8yc2CqVIYf80ehgpCJ2mfB34CHC4190ReuG8-loZJZFxYDuwNwc7-9FOCkr9qlZIbDEMhZ6qje4OG8P09Gi26zOSR5jQxZ7buu8L1a0AGMh9C2JC_yFZ21W-JszDUCoJLFjHKv1EJqoMg52Df9GiByHk4TgolyW1QhPDKses8EwG8OQv4qujRdwXdHQxw-jMqnCjqPnbVWwr_9iFrn_6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30327" target="_blank">📅 01:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30325">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMb_pjXCdZZ7fgN86uazWQsNWV6-yN-AMtLPv7hRC-GeZVYWVujXwFFQB39qZrJ73uAs0sm47H_MPLV2LwsDtwkLFDZTHyRsudcZHdlJDdd4ss_4dIWOWqjRgsyAd996W0PlO3NNvloEPEcjvHb8gxXxG26illxVQRQgBmGaHAW7d9nyUcTQbA7IjsaOOk1_L0BuRP8eTrm9fGB0sLVTN0svXeSjHuvLEI4BPpvl8-axgXy-2Ixp01guWZjFTHuCnzef-DC_buB1cQ3xhNoD8BdwMAeRvlyqeShfla_2l1gs3oy__UqzwestYJgbKMVGYoVQa9sPeLK93Kj-21Wnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTuP0QmXIt63tw9n-UhkoaR_grQKi35Y6hyxXyJHfASLyjDpHCoYzWYKh8hJvBhuGjv32IFB3IF26dZFx7reOdPUmLH_sof_VovCUKVboC3xxI8XFObiE6OPZmVsPFuempsPdAQi2pY8GtnkrMlh7iVrl0JWbR61nv0xqifKrbNVNwrgjYOnS9qhJTpEDPknSyp5zC0Wsu_doeJ5-UrlSaD0HMEKRvw-lCFbllZN9eCrmXovZS2gPDkm06fojrZXVxQsckdMecwqtgkCC0nPrsjCfT2Qzuc-vOd1cx7seYdesvJ9n1_nqT6lc47T7x8G5rJuRmk5RUCA_9rjXQHvxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آخرین رنکینگ بندی تیم‌ های ملی پیش از شروع مسابقات‌فیفادی؛ اسپانیا بر دنیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30325" target="_blank">📅 01:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30324">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=gQtpVaUKMAXEvA4oBWADlzF-4kpMDyS17A6UQEvYnocBkrVVq_bH6krtjM8TsiL8iT4rJ1GOWuuuJpj_ArzvR__taAakdPFv1Bcj_hE4dpGnwQKECISZ5bMg6freWXEIItNX2S6MOiG9ndGVfBOS6BBcZFSs0N-jFCccXbVfC1abz77XkwLeN8jrVi_vX-BaeoiPYtU1-Y3IIIGv8trTWrYngu1GwFUxggpOYaoY9CupHGX2_ludVXZJR-Z8kffDxZfswJl9-ppZXeCspITmUdbyY5A4kJHNp0j38LPIFIydN-m-j6lqRy_nkiBHpFMLE3rodbhp4sRRqY9Gx7myJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=gQtpVaUKMAXEvA4oBWADlzF-4kpMDyS17A6UQEvYnocBkrVVq_bH6krtjM8TsiL8iT4rJ1GOWuuuJpj_ArzvR__taAakdPFv1Bcj_hE4dpGnwQKECISZ5bMg6freWXEIItNX2S6MOiG9ndGVfBOS6BBcZFSs0N-jFCccXbVfC1abz77XkwLeN8jrVi_vX-BaeoiPYtU1-Y3IIIGv8trTWrYngu1GwFUxggpOYaoY9CupHGX2_ludVXZJR-Z8kffDxZfswJl9-ppZXeCspITmUdbyY5A4kJHNp0j38LPIFIydN-m-j6lqRy_nkiBHpFMLE3rodbhp4sRRqY9Gx7myJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل فردوسی درباره زندگی سخت یان دیومانده ستاره 19 ساله رئال مادرید در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30324" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30323">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=c4hwvVbZ0Zo1hkDoO6DBnhwJ8v0jWr4GW0lxRrKFlezpIfgU3NAJr-wxOnRRUK2jYwmoH9i5LIHlueRwdaR-HHfye-5W8FKlQgAB0hrBPLi1pQPcAt_E4duHHfmVdkoay79d9sbh2wCeer5qO0EUB5mFeWP8pdmv9KFW8_MaU020czHtQfUAcA3jv_Mu7l-6upbfVez48wrIFQ0kpktjOC2OK28vzjfxM8EVX4NzJz1oaETFWZ7Wwgv1-hQibba6XZEVve4UAnktFsWykk1lzN867rGAbzTecqfpsXtBdo0OdV5UTMbgKPdiSTfs1fCz7oacKYCXHHLZo8sogXOMwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=c4hwvVbZ0Zo1hkDoO6DBnhwJ8v0jWr4GW0lxRrKFlezpIfgU3NAJr-wxOnRRUK2jYwmoH9i5LIHlueRwdaR-HHfye-5W8FKlQgAB0hrBPLi1pQPcAt_E4duHHfmVdkoay79d9sbh2wCeer5qO0EUB5mFeWP8pdmv9KFW8_MaU020czHtQfUAcA3jv_Mu7l-6upbfVez48wrIFQ0kpktjOC2OK28vzjfxM8EVX4NzJz1oaETFWZ7Wwgv1-hQibba6XZEVve4UAnktFsWykk1lzN867rGAbzTecqfpsXtBdo0OdV5UTMbgKPdiSTfs1fCz7oacKYCXHHLZo8sogXOMwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چالش‌عجیب‌وغریب‌امیرحسین‌قیاسی در قسمت دوم برنامه جدیدش با خوردن آبلیمو با غلظت بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30323" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30321">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbLo_M58Cqx9m4M16DuQ905KK-suvZrTnZrnN8RS7UJcwpQ8G3FbOBGQLqtpIKx-ZaWbqQhPyqIncin663QT0x8fVpQRREZIMIcdtN8wUbycs7RjgcvUmOoyL2KgYF1MwWobZ4Z5pQiVasa1YTKFffkFWqw-s1CQQ86HPnvmaU4MXqQU3gQ49gcz0KYbxulDC74RCS5qTs_8Cygt0jfO-oohstfrhl-KtieGRxyFKiDLT2gMBu2GDvTarXxkAnvLvpApGO__nXLanvcErQMx3e4NpG3ifEQrvMuRo3kmsqUPDNu1LveNCFEQowsT24LB0RBOnIZ-NZqAj_wqGS0KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30321" target="_blank">📅 00:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30319">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY37bJT0LjFJWQEvaCJkMefm0IjdiFDbWpehMKdrtZ36DzP9s160-0vQ8rqXRAAJv132J3cWmYsY74UgtiArcRnG-IXflAKwabRRUc7XnqjOD0KOnjWEzMyCTnZsAIiTfgvlCwTKbJwn_fhoLmojImoq9RbFlcEJer-kink-eOo9qQiSkFcZ7UZ4MuOzb9dMNlMoYz1ZCkk2UQU3hlYaOAvfX8njzf8RC8-F7jPUJXseoKbwcO2m4ZJZWhjQp7Qs4N8qkCk0wutkk6UtPlq7PDlwwQrNLY4Efl6WcXd8XtchmxB6K_5a2Wvb1s_ZOYzdRwYaO6ED7n1llJw8NH96OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30319" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30318">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVV5ah4U6zJvqQdWDJnU41kguy5Z_phXp5qgyp2JWlPKVquwsXDRkTTV8TALDKLg5x2kvKDqHtMSmKQfiil2vzNlq1bxDQw7spBUt0XHk104maJcgx2q8EHeUxWpn9Eq8bGE8tkqB_OQXF2xHR-X7V6vJhQR68uib79XzBSXGIKyJdaLZEnzMMEogpySbdkauBT3Q_FdAaxFeg4rd4hDMt_2mLcEcY7MSaepex2ldN8LxZt3DoiGrecUZY9oRY2AR4UkRiUdRY4qIlFbeD-30yjy_A6UX81XQl9UmSE11SIZHknKcqaF-xQLnI_YWVGGi-OmzQ99uRXg0iRPUsR0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌‌‌‌‌‌تنهادیداردیروز؛
شکست‌مفتضحانه تیم امید مقابل کره و حذف درمرحله‌گروهی بازی‌های آسیایی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30318" target="_blank">📅 00:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30317">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LokFhtquPtQMszmLQHdu1I8GiidrscJtpTfSnuSh-SJDZtqropWejTCNeFGt6f7fcMRBSgLyFlYfWeHBQDg-ktpZ0GYZG4cVDRzJVM3qn0fuPtVHWsytUCDyyvxZaP9qXEZjpClf7FZ6kU2AkGPi-cgqoU9YLSi0losvRrRNiOOMrbWeKdDmON5-mFZ_KCgnBKHY1imbkyEMji_9gcyiX_Qbjm0ubPifXsPp6dibk3X2V7g_AVegQdAL8VU1LprY1RHfaaAeuzvBne7HSb-PZFvbz8H69tQl2eg9qS9qAjfVzP4MtkWea_t50QSuDuBvTmVENrvJhGzXBCWTzQgiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30317" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30316">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=Wf7_EvS8FAxYbyK2Te6sfktyjcY9V05Xt2S6V8ZRb9tqJcEAm9mbU1KiiMIMVDO-fsBEi83SB0FqDDW_9UH-VIdgKnJ0h-IymYPfY50T7blpQl0r9A2_vAAoIMnyDgX2eYu6ch3bQZ5iocdlLamVMd0j7gjhhgGy7Hk27RsEr27U3HNhuYQZ0_n4i1r3naQy432Jhgu19WubkjJzPyNeQhGa1CszkGLu6DsOPOCFZSHY0BxK1IvhOQ5Rd2HP5DA-gmoaLmJEYfzdswMusg58xjRA6pZQ4IfqWYCFmIml1cIP3PhdDpX1EAXYtwNe0shlb4HDpRkCwvzv8jlMqqj0-yB4f5AV0o7DwR6NWv-WD3_YoF3J1QadO8IkZPpUiSAC37K0pMQLrjEwq1OY_nv1deGscXJr_RKMjkw3vkUvtnRWhiiis383G3Ncss4oNaW1K8F78VKJ5qFYEw-m5cVHsZmaw-9Ke5S_Tw7Yc2H6UujTCeZjXWWqmXHIa9dhKUHT3hUadhnxTgsqOcYZjdPawhtMISglsuaW2OeasG0hS1Fx31fAiNubRR4eHNw4sACDrrh-XHtX7bDcup8wGoS2kKKtegzT9D7WgP3EtD-d0zoHhSkP9C7SOegOuKCbyqoIALNFEDCXZpFwUYqNTBpCEC1zXajsfiXql-S8yu929jM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=Wf7_EvS8FAxYbyK2Te6sfktyjcY9V05Xt2S6V8ZRb9tqJcEAm9mbU1KiiMIMVDO-fsBEi83SB0FqDDW_9UH-VIdgKnJ0h-IymYPfY50T7blpQl0r9A2_vAAoIMnyDgX2eYu6ch3bQZ5iocdlLamVMd0j7gjhhgGy7Hk27RsEr27U3HNhuYQZ0_n4i1r3naQy432Jhgu19WubkjJzPyNeQhGa1CszkGLu6DsOPOCFZSHY0BxK1IvhOQ5Rd2HP5DA-gmoaLmJEYfzdswMusg58xjRA6pZQ4IfqWYCFmIml1cIP3PhdDpX1EAXYtwNe0shlb4HDpRkCwvzv8jlMqqj0-yB4f5AV0o7DwR6NWv-WD3_YoF3J1QadO8IkZPpUiSAC37K0pMQLrjEwq1OY_nv1deGscXJr_RKMjkw3vkUvtnRWhiiis383G3Ncss4oNaW1K8F78VKJ5qFYEw-m5cVHsZmaw-9Ke5S_Tw7Yc2H6UujTCeZjXWWqmXHIa9dhKUHT3hUadhnxTgsqOcYZjdPawhtMISglsuaW2OeasG0hS1Fx31fAiNubRR4eHNw4sACDrrh-XHtX7bDcup8wGoS2kKKtegzT9D7WgP3EtD-d0zoHhSkP9C7SOegOuKCbyqoIALNFEDCXZpFwUYqNTBpCEC1zXajsfiXql-S8yu929jM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برای اولین بار در 47 سال اخیر، یک ژیمناستیک‌ کار زن ایرانی درمسابقات‌آسیایی شرکت کرد. هنگامه هادیانی؛ ایشون درمسابقات رتبه خوب 13 ام گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30316" target="_blank">📅 23:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30315">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrpwzYriOlkC9FD8pZXK2Sup_8-jB_ZGbX54dIeI9NDY8DqbkOIZDKp-2OU3nsTREx9J-1hiUJDfOElX026ljR952se9yWuKDqXlhBdczBYOyvpoaGwMsROiVZVkrXojQ1OS1JZgssvBhMICx3pgVV4oJZFWXhp0GU7780eae9La_DC1xQ89vAYZfcn7qf6S4j5WIDfvFxS0rJgVnGmD58bZql8P77xDyCwxLH1Std2fuYSzzalEy30V7Olq8nivs6Br03BnoHqnAv7xMiFB1N0V9KLujiyRv8N1pSW-EIQVlB301Ag-YBekKbPBzAXE-Yjid0hrk-Dl7YF6gYdSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
صحبت‌های کریس‌رونالدو کاپیتان پرتغالی النصر درباره زدن هزار گل زده در کل دوران فوتبالی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30315" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30314">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq-LfDkvQq-2Cu_KTXq8KlE8icZpqx6_caujndJ3gcwihbIB9S8i9kYNUYSxA8yzZzHJjGBWZUGouDBbHWTDQn9FwmyeecHoIbnCWAEcMD3cvMyirXtp_O4SN6riidL_HnK8DBCFEXltHdsT_RpQOMljMLu60AZOBhwtgykt_Oa2QYyPg88K3bYtDbVACi4UbVaZufJ9HjDWY7SKMV8WzZcKpJeQ084UDH43MgonkWeIEtUBGIJOXevBCAycWMoe0PtRb45W2A0woPiSeIF9gjakDaDYRcihaywhw7Ja8f80sipIoNWM6y-LFt5jMv7vfQT2kh8bJpLTMbrynIWs-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30314" target="_blank">📅 23:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30312">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUbgVc1uQciIUKXjvoeQDI-bEsMombxOf7CFdjvCVUS2IhVC8YoTxMgIF1d1an2poqCso2InQnXhIoOPSOx7z9aquIhMMxV1u-Cm6Txlh2xyp2b406ZxCHftqzJoAgE-XtcMh8-ywLsd_2iB4dhyWvYzs3EcB03Rc2IWu0ps1lpWCvwRPXSPZZtBsLzeYkbvGAbTQh-XezedRmt2lFLoy_sOQWdEXdMWNw9EqRA4GUb5STB4WNONGjUEGybYvZ6qlza9uLXSvujgtaxL5LbS6na4Q36NncT9TXcamNa72HqMZMWqaggeCYdF2Hhzgha1jJ2qTutgfcyEm1hJhW62yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال: باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30312" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD_7PGtPn5yKViFN3MjHr23mhgP5TIJqQ5lwuQTmFwS-k9lL8PLGLfhf_Gv5aW9YGZhqv4tK_SUmkVf_DLG3OUNe2y6TlRwwT8I-tLsEkl_b4Q2ni_R4Qb2k3hw70DI5aTawVBYgevN1paaRIt9XVGZU126Ze6jamqgZfw7bWfO6x8EJkIeTycYeVKXkgPKlkKReK2i_gb5F3qy8zGYmJCY0SR70EFRx2GP47O1xSu94uWKVAXZ-VZ9oTHM5rDj-fo-Qq6qt2AbY8iDFFvVxbLdn4S-E23QDk7gpsXZkJK9TcX3bsWd3nPrNPE-m0bM8FCjTHesgLNaWTbk59v6i4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30311" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=Pfhq10y1TpriEQP5042ybyfZHZ3fYnd15c_hKnvbtipaMEfUDoGL5ngMo_-bkhLXH2HIeCxp2LInYVzWuQ5jE988ANE42WOqhGj1lqC4lFX9OLZJRscHfXzxLTK1t9rNuL_a2gbaIxiZJX4LGNiMPzGxakmQsehoSOGqOa7zp5bI-eBHhEEHVtgUJqEEgDFgSVlEOZwIHktdE7goPl-piHTa8_nEx37F-LTMeMmnHYR54RZTkCmvOQ4YPiLRY2WMNI_32ncoXpbF8RetxlhbQJplMzIEja0nKoGlnU62y5R6rpjbtB5quO5S8bKXZG6iqpmmxkQgwki5A0Hq5NLvljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=Pfhq10y1TpriEQP5042ybyfZHZ3fYnd15c_hKnvbtipaMEfUDoGL5ngMo_-bkhLXH2HIeCxp2LInYVzWuQ5jE988ANE42WOqhGj1lqC4lFX9OLZJRscHfXzxLTK1t9rNuL_a2gbaIxiZJX4LGNiMPzGxakmQsehoSOGqOa7zp5bI-eBHhEEHVtgUJqEEgDFgSVlEOZwIHktdE7goPl-piHTa8_nEx37F-LTMeMmnHYR54RZTkCmvOQ4YPiLRY2WMNI_32ncoXpbF8RetxlhbQJplMzIEja0nKoGlnU62y5R6rpjbtB5quO5S8bKXZG6iqpmmxkQgwki5A0Hq5NLvljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های خسرو حیدری کاپیتان‌سابق تیم ملی و باشگاه استقلال درباره حضورش در سریال پژمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30310" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTKKrDWsdbggG9JUu85pYDgsjLWwP8wV_jWI9u4_epxOeYWUirj-YChde89Mk2Lqtr7MgpLe1Skow1AGMQUEuvclZHGVXOV6DEL9gR7Hkl4I4hgFgmAKoaqXs-thsqKhb8QPBxkNukz7-voZscqySFxEShy0qX8U7ZDPALcO8NdFGALQ1VmM7toXyMM_EX_n24vXjA8i9Dc6VU6BQWOdcNhUmkqO-3vbpVjaYSMaNbemeGpp9A_n7HtigQ-Q-V_1EtDtGk31xRFhFtONN7KfmSsCbZ41OgwizvyZlUXwC8A6Bs-PfbSsOsL4C14ilzy5DNETlrNaQv6wvK3OChxtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرامریک‌اوبامیانگ‌مهاجم37ساله‌لاکرونیا امشب به‌این‌ شکل گل پنجم خود را در فصل جدید لالیگا به ثمر رساند. انگیزه‌وچارچوب شناسی‌اش‌خیلی قویه. این 414 ام گل کل دوران حرفه‌ای اوبامیانگ یود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30308" target="_blank">📅 21:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=C8Orfail8WEKKJnGdX4HTDTzXnSQEUkfeuQTwCwTEEiRGat3_Ud13FdgoGRhUHaFvmDT0EiBFhI2WdJN0TeTrbK7S6zfunFz4It8Ooao0pq58RHL5DTLYDMra2_WlLpbUHQlgGysuoTEqrue9Qel4jd-Dco8QumSEr8yghWl1uivcsPTjAPt0lj-W1K_wbmllv8TMBgX_AcynR7pCueSit_YmpCCn7dJ4U46z0Jr8f5wn6lUFCzG3WpqkloZY0cbibNTyZO6wqHAUes4GR1FffLMhjnXmkXm3oHmQkVdrxDSJTndqD8U4PMyXmkKfZr4UMQymxuJbujCFZ2i3lAPSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=C8Orfail8WEKKJnGdX4HTDTzXnSQEUkfeuQTwCwTEEiRGat3_Ud13FdgoGRhUHaFvmDT0EiBFhI2WdJN0TeTrbK7S6zfunFz4It8Ooao0pq58RHL5DTLYDMra2_WlLpbUHQlgGysuoTEqrue9Qel4jd-Dco8QumSEr8yghWl1uivcsPTjAPt0lj-W1K_wbmllv8TMBgX_AcynR7pCueSit_YmpCCn7dJ4U46z0Jr8f5wn6lUFCzG3WpqkloZY0cbibNTyZO6wqHAUes4GR1FffLMhjnXmkXm3oHmQkVdrxDSJTndqD8U4PMyXmkKfZr4UMQymxuJbujCFZ2i3lAPSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس رونالدو: ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30307" target="_blank">📅 21:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keccrBnqCTDN0QlD0JqdhzrUVRtEISQtJ-gkV-ZdrmLfJorw49H4LvXAPSMI-rmeH-wdhO81NeHZyWSDp3pbJy68su0LT1FELUEJZrbZHZyNLANcf4ptcsB5Ai267qIPkzE0U5Q0xFhNEtbArdP9sKiGM5HTYKtBZLpmF2kcsZ5g5B7EWlUb6M6Ag8qPiwfahF2gDYKeBVfxu_-O1DNqzU3MliguwCSC5UvawoKZYkSpSkchW2ejfX9RZNyUq3PJdeVnef5vcS3O74u36x_Hu1uWf83-h6SPAhiwVusYRGUegHuxfMlQffFNzcwt1e1sgfo-kn1PYhTzGP_YdvLX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بهترین شروع مهاجمان بارسا در تاریخ؛ رافینیا با ثبت ۱۴ گل و ۳ پاس‌گل مجموع ۱۷ مشارکت در گل درفصل ۲۰۲۶ یکی‌ازخفن‌ترین شروع‌های تاریخ بارسا روبه نام خود ثبت کرده و مستقیماً پشت سر شاهکار لئو مسی در فصل ۲۰۱۱ با ۱۸ مشارکت ایستاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30306" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWofEGwDN9FWNSDUMjq_VgmljMR7Tq541jbrY0VD5LZkzL6Asn9US4mSamSrMZ9T0VHkVbdBNVVfvzhpbpuVRdAwBItIYyZMRpQc8TFxJOwIiTflFMzlKRR38vWxWfugjM87K-jsAnlSJhNiDKE-en7ETc3oH3wxWSWNutQIPDV-_eK3efWDA4rze4YqZjlD3976VtrFn9mmb_AM7YB5_1AKrkWyeZpwZtSj-uPe8I3cQNcD0JNgki7tVEQPdH04KMY0zM9m8VPSCm9N39soNrz7sDhS35K5WyfmtnhA9TZO7L4kt04YD4u4t0uOrpdlcOAoYROxJkbIu3sxepy0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو:
ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30305" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
موزیک‌ویدیوجدید ابوطالب حسینی با بیت کاگان منتشر شد. خیلی‌خوب‌میخونه لامصب حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30304" target="_blank">📅 20:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=U2zJAN6e4_eMyn6bDDccbksFJGSyFFUzNQm84ey53QU05nMrwCaoOsAvj57Umgna3fxnPppVbbVnOW_h3y6sgpAH_vg8nvXmKdxxqKdUk--1AvrNLyD58G8FNlRUpFOMibd7wxTrrQ-LVDr-t8YdWRPav4zPEFsAtrXJoDUKoQ15nA14Ab69I4qSTLNciW6Dln59Rj18wvRPPcJRz4yPYsbIRLMhDWtcPc4layH-06p8vG9CWWjjjqkYPfF3v7-8F9gtht_mkeBs9wzDkvmW51-Ej8RrtLrXkdZMyOUKXpOMDshjRjFgwunA7pmgljKH2mey2CzjvoTtgtuyffGwSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=U2zJAN6e4_eMyn6bDDccbksFJGSyFFUzNQm84ey53QU05nMrwCaoOsAvj57Umgna3fxnPppVbbVnOW_h3y6sgpAH_vg8nvXmKdxxqKdUk--1AvrNLyD58G8FNlRUpFOMibd7wxTrrQ-LVDr-t8YdWRPav4zPEFsAtrXJoDUKoQ15nA14Ab69I4qSTLNciW6Dln59Rj18wvRPPcJRz4yPYsbIRLMhDWtcPc4layH-06p8vG9CWWjjjqkYPfF3v7-8F9gtht_mkeBs9wzDkvmW51-Ej8RrtLrXkdZMyOUKXpOMDshjRjFgwunA7pmgljKH2mey2CzjvoTtgtuyffGwSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30303" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=KuySZlCIc57gFohtbaKDL6l19VVJhNFcSpn4xYsWw6z0y2-AxbGuaPwmI9_y57RwW4DVUp4w3MY4D-2yjG7xs1Zg6Nuuw9nGYO5ruLZROmuHJeHsHmWbYDOiH5f7eWn6Y93a839JJ1qiWamXP9pRRnIOD7q3SOJjTlxAjywUWv-_K3FDGBJyBoe0gzMy-soa7KcHt3jFCscDk3a_H9LjNBJZ_KvdQy2kBdRdGvZtPKijfibefI4XJKKyqvU4GYZXLXQvylIVdCBvtGBS7nd9OPz8n_REcoRuW-8RiCfOXhXWM6ZWfWbwdJX-peWmbXxgic24LB1EN28UG0z1cXtIFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=KuySZlCIc57gFohtbaKDL6l19VVJhNFcSpn4xYsWw6z0y2-AxbGuaPwmI9_y57RwW4DVUp4w3MY4D-2yjG7xs1Zg6Nuuw9nGYO5ruLZROmuHJeHsHmWbYDOiH5f7eWn6Y93a839JJ1qiWamXP9pRRnIOD7q3SOJjTlxAjywUWv-_K3FDGBJyBoe0gzMy-soa7KcHt3jFCscDk3a_H9LjNBJZ_KvdQy2kBdRdGvZtPKijfibefI4XJKKyqvU4GYZXLXQvylIVdCBvtGBS7nd9OPz8n_REcoRuW-8RiCfOXhXWM6ZWfWbwdJX-peWmbXxgic24LB1EN28UG0z1cXtIFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره مهدی مهدوی کیا از قرارداد یک میلیون پوندی اش با تاتنهام که بخاطر سربازی او لغو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30302" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=IDlpA9hUxk0tvs9JtjHVJd38IjKmSaYzgqgL6ybWYBz0oz6s1pCcn6pvOFKTIpwrywtru3cYeAehBqefsc5lV_U7tC0HRbp6Q6LCDZ2z18ZC4G4FnxUrkOhTs5A3ZrxnuXtR21_Yyx2UnPkCtN_UXq-rYFS5mY7ODb9SJB2qNGUQIQIWT8jh_u0hfOzR3VgMWNfmvBS8Q7cB_Kw6VApK6_PQtcSx695e1h2oceTlax4J-G_jvP3roedbx1dJi8oo1zgZpwpsTZgXgttlK6B6n-g_MbVmKjBOFe4_19xSp0W_vy-PCN40KwdnA75qZQIUMxSh8hSmWmuqkG9sKYeZjr-YHeVhWm5dzLDUlOtriU1nxFcw9_z6ub8xHBp8osZBVE3hn-e-d6enoYtMxmjRwofiDv5ulD7V-n0fmY8amL2nzi8cOtCXxaWkJtt8m51Fdz5ONznBLjWKUV6gmII4QykmbP24dFTp-YbG3VLBdxi1mZEEVJb0cEV-UqWAlseHasA89eqC6BK-5jGGfpIOKyGoPW6siR-IxG1Fbpu2E-SiNwaIwULd4XKNrKquvE93rgmZJUXUh8tElK7Co_kSJagpolZfYNlz4buzMuMNmtDs8GzSO1gWVFym39kUvNrtxjHMsIwzdj98ZYvMeXPFmQFU5QaOs8ybb57GzBa_M_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=IDlpA9hUxk0tvs9JtjHVJd38IjKmSaYzgqgL6ybWYBz0oz6s1pCcn6pvOFKTIpwrywtru3cYeAehBqefsc5lV_U7tC0HRbp6Q6LCDZ2z18ZC4G4FnxUrkOhTs5A3ZrxnuXtR21_Yyx2UnPkCtN_UXq-rYFS5mY7ODb9SJB2qNGUQIQIWT8jh_u0hfOzR3VgMWNfmvBS8Q7cB_Kw6VApK6_PQtcSx695e1h2oceTlax4J-G_jvP3roedbx1dJi8oo1zgZpwpsTZgXgttlK6B6n-g_MbVmKjBOFe4_19xSp0W_vy-PCN40KwdnA75qZQIUMxSh8hSmWmuqkG9sKYeZjr-YHeVhWm5dzLDUlOtriU1nxFcw9_z6ub8xHBp8osZBVE3hn-e-d6enoYtMxmjRwofiDv5ulD7V-n0fmY8amL2nzi8cOtCXxaWkJtt8m51Fdz5ONznBLjWKUV6gmII4QykmbP24dFTp-YbG3VLBdxi1mZEEVJb0cEV-UqWAlseHasA89eqC6BK-5jGGfpIOKyGoPW6siR-IxG1Fbpu2E-SiNwaIwULd4XKNrKquvE93rgmZJUXUh8tElK7Co_kSJagpolZfYNlz4buzMuMNmtDs8GzSO1gWVFym39kUvNrtxjHMsIwzdj98ZYvMeXPFmQFU5QaOs8ybb57GzBa_M_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنالیز دیدار هفته‌قبل دوتیم اتلتیکومادرید و رئال مادرید؛ ژوزه مورینیو به‌این‌شکل‌بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30301" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErT_BvdxDy4T4zCijvgLXMKKb8VdbWEQlI-UC6GblNyARPmYdlpZAC6OBcTimRqutXuqqQGnzcCXbCjZcDZK2c-kpLw7mB6dTz5LOz_0jet-4G8Xx-xafjGSFGQF_IEPYhss6ddqoiotfVcALvZcJ4GQPZEsdAaboxS9h5wOMhA1JWfZOHvnW-km7OsEp33yPlapI2axjKFlnlJkegAD3IJXbi5fb1g2FdmlRMc4SXLsnqvwU4DEJmhpMx8rQwSgiC_A5U3Wj0lMKfJKjLGx4E54hqe9oesi6-_7-oBPeI92od2v6mT6OlQbB1PfgUeyNX4bHAZQb3IefpRV99Zdste0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErT_BvdxDy4T4zCijvgLXMKKb8VdbWEQlI-UC6GblNyARPmYdlpZAC6OBcTimRqutXuqqQGnzcCXbCjZcDZK2c-kpLw7mB6dTz5LOz_0jet-4G8Xx-xafjGSFGQF_IEPYhss6ddqoiotfVcALvZcJ4GQPZEsdAaboxS9h5wOMhA1JWfZOHvnW-km7OsEp33yPlapI2axjKFlnlJkegAD3IJXbi5fb1g2FdmlRMc4SXLsnqvwU4DEJmhpMx8rQwSgiC_A5U3Wj0lMKfJKjLGx4E54hqe9oesi6-_7-oBPeI92od2v6mT6OlQbB1PfgUeyNX4bHAZQb3IefpRV99Zdste0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 88 روز از این‌ویدیو تاریخی از خوشحالی مجریان شبکه دو روی آنتن زنده صداوسیما گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30300" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i63b9cPiexfT7TviD9q4ZsEUg6yzux1S3TXNBxrZFKXjDfqaDzcMmuzKJpc_F_Nnu_kO6d6PIKJF8V9qbanSPbu2lJgQXLQSCGwzA4cZZoCQPR2m2RawqI-fL8jGQkm5oZOP_ofolQceuj1yjlBnU-6NGg-W-bj-x6F2Rjoqc8ptAeDrA1sLeyj31tuNUCZodBoc2x1coE7IheTgY34DC8fVa321tBnMJjpu1Dtb_XnVKDNBHAK8DLRW21mk0WKADsnf77KvlKw05LaC2z6hs1Ijgpukk8gKlsD0RoFPmoP0XF-1nIT0r3PAZZK6yJeCJ3LhMY-tP-VMXNNyGXs8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادگل‌های کریس رونالدو و لیونل مسی قبل از جام جهانی 2026 با بعد از این جام تا به این لحظه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30298" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_nFM46FWfkmDf6leKwR-_AjmONSh7wdhvGI7W0exaawUOdw7Gha8MIEG5Zs77qBOfHbLCVu-9-DN5r0d970udXxnJ_46qyMJiM23WeiMGA7RaAT6brSV2GTfcd3LyPRALyGLx2qz9RGFFl4qIwhtoshmO4tPZt6Qin67gDlPYFpS_ccxEPE4zgNHdtWZ-TzxwRqb79c5lCodsTeKLyEw8v8brorOmcObqc76lg-RpPz1WLbCQrjRGExlTIcif-AA87LrKKtrnVdaKgw5y0PQ5RA8-SBmMBRmUL3kA0aTYa0ey27pFFE1ATZ1aDjDEn2t_-4VX99-O8QfdDNU4_8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30297" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30296">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZYOupFuLyJwB167TFG1kaEQXq_8XCdDGBvpLfKmsF0E7DPlkTfoz9a9x1oOmHVIEa-dwc-K7x3IYnrzwe0q3fpHaFpSbGm2-QPfgm8fOVyOrl4qnPpQjTvDTidz66xvQWQ0KacP5TVhIWsmY9BDkINVYhiqe4gGXyGJF-FRuGC50iPMHuiHhXNBSmEKZpt9MYBJdOlXlX8PMNnR0n44M6esjgLpMtTJuDhNrc3HgKD25UmvvMCRB2KXNsvd-FxDn3zSZ9MM409V2IIW9tUwauVbw3QHRQZlID0xA-kwhSe3967phggz86i_z0on0jaYhlL9cvUojkw-kxYhdcKYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30296" target="_blank">📅 18:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBdBbty351zo1eaECSadYz-uNNLjPklDov98Iksy86kQUPrcLafZk020CagfZ5nToPImE97h8G47bjkJ0Bv5GRfZd3cPfZ76tmUqRoa63aVi2D3iu9rkEant6DDPko1DYWaUkmGFjjhljOolyONy14BDGovVrBJDMSMEv7D-sluhgM8VYV30KED_ooRFrF37VGp7UaNENYGtQ5q2la6YbfZLaatBO1EZIYdlPdrQ7AZz2T-ia93U8MEloMQtA0Cad3fkm3eJ-sihogZSuyR52iQGylorwM-NEkQoFmQW2_x8BbuWJDO7spy1UClJmzHpC4QV41NdKMHaPaC6FRmgkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30295" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=e7O1jo__8VhX0AVDfj3HewGBQPnUfhOtMophq9J2-hDtThaPx6-JFOCkYGHwJaNC-jyiEfHTDo8231Sm259CsfUe_7mhgJWDspn2a5uhMUT25MLHI1Zg_MjODu1GchXJhLWiZEEzyz8k4EabIIjbEYxdfqL5MLULckN7vKI8OPKSLeTpyTtLt5ipv_BbTvRPwFWClJav68qNF-A6Z69F5T6b17AoEeQC6vh96ygGYr4Us6lK6HdPvZqSoM_jfcQ7qK71SjtqPIf3kBe8F_YOVFSSawKAeMPzsCjDF1oyFG0D2l46kHaPKjTTd-Yf2S4I8i6Ec0dTcmbJxMDKpGPSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=e7O1jo__8VhX0AVDfj3HewGBQPnUfhOtMophq9J2-hDtThaPx6-JFOCkYGHwJaNC-jyiEfHTDo8231Sm259CsfUe_7mhgJWDspn2a5uhMUT25MLHI1Zg_MjODu1GchXJhLWiZEEzyz8k4EabIIjbEYxdfqL5MLULckN7vKI8OPKSLeTpyTtLt5ipv_BbTvRPwFWClJav68qNF-A6Z69F5T6b17AoEeQC6vh96ygGYr4Us6lK6HdPvZqSoM_jfcQ7qK71SjtqPIf3kBe8F_YOVFSSawKAeMPzsCjDF1oyFG0D2l46kHaPKjTTd-Yf2S4I8i6Ec0dTcmbJxMDKpGPSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛
خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30294" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=GHxAx3gjXVUa6N1IKvB5EhaaZg5I1KJHkfZfLC5lDbZQRCmXm62QWW7jUXVjkTqGHGIatP_Gide2ex1M-8WgpOLXcZEnxAAgQVbWvBlpLQe-NuN9mEGWfKsklZx9ma5GkjoRcQdmpL26PXMkMAUW6350lVKuVvvR44D_9ceBOwKeyknwpBebTrEWH3upu4PsaFVChxfukCV2RnQrHevChToRSXigAV3FFkGISREuBY5HTPmNtW6QH5wooBgVL2lCRF02G01ZR0XnNHoKjd1O8NxZ_l_Eb5AVCRfb6k36Dynu0PQQ4Cb8MYL_NCVVwjdN6CvltNGhZE2IGMMNqrNs8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=GHxAx3gjXVUa6N1IKvB5EhaaZg5I1KJHkfZfLC5lDbZQRCmXm62QWW7jUXVjkTqGHGIatP_Gide2ex1M-8WgpOLXcZEnxAAgQVbWvBlpLQe-NuN9mEGWfKsklZx9ma5GkjoRcQdmpL26PXMkMAUW6350lVKuVvvR44D_9ceBOwKeyknwpBebTrEWH3upu4PsaFVChxfukCV2RnQrHevChToRSXigAV3FFkGISREuBY5HTPmNtW6QH5wooBgVL2lCRF02G01ZR0XnNHoKjd1O8NxZ_l_Eb5AVCRfb6k36Dynu0PQQ4Cb8MYL_NCVVwjdN6CvltNGhZE2IGMMNqrNs8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 3.5 سال از این‌گفتگوی تاریخی علی فتح الله زاده با محمدحسین میثاقی روآنتن زنده گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30293" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTCDjZpllSnw1BQLc0YJQR--FVUdJcOinXRyBx_cbI6TSaVVMQhyYLLWo7vjkRh9JtTae2MFFsfEojCvxiexeNp8848LbA2YCXKKccsMwVVQEZxMqRtHbTxcIsQsAq1vOeEqDVyBOpqeVd8AWejO-XftwYoACMCTYsO8kK5M3kyHNRoDOVDyl6ksIeV38VqTP37GLPgQ89yZj3gzNYtTPyzUBZXt1gjT6fQiTgxQw0IS0By_7dN3ZIuhbanDt_qKxpmiqEOUl7JBuY9uTcZNjKVK4WsX5AFGBNc7ZH82wtcisV4tRwNVDtCHxEEI0wPWVFRlR-SRFie4svXKGMR_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی، ستاره‌ی پاریس، با رد اتهام تجاوز، مدعی است که این پرونده یک سناریوی ساختگی و ارتباط آنها فقط در حد بوسیدن بوده‌ است. در حالی که شاکی بر ادعای خود پافشاری می‌کند، وکلای حکیمی می‌گویند امتناع او از انجام تست DNA و بررسی گوشی، نشان‌دهنده‌ی دروغین…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30292" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30291">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDbxbxmToqT6VqVqiYBDt_eo0PbpheD8BDIqrh9pMcyW1c_og-sP3KrausOPC-7flRKuVmUX21SRzmgNhLQhbUjIXdNDKhgzgEFBLDCb82XUmye3p-wIY4Dxkf8mRpPKgFDeDlsJ1cw1mTPMyWxON-kzmTm-soRlYNYRqQdkaMx9UpqWS7I7bTIOFheXNlL7x3ZSNgEFbsDQZwoARhmIti_sH-Funs3Qt7MzLhEwr4jc1nCrqjl4BcqndJYEotMAY7KRRcyJw5oBISPxwQcBnO_hJCOqtSIBE-yQPZXDRTjMS-mQX1Sm80Js0rsC7LoVKlRmzi2QwsutOZsUM6HiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30291" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esOih6OBxG_X-pl5Oh6Aa0cONZAVbap5SDeuzljkTVO_B7O3mvf-CjfJ9KfmUF9SKuPEoscR_Gj9XZ1Z0irmalERCp9NkCoFretrjB69PUWFyhL_AnImMGks9j7vhpj9D42fSeQIxBwyc3g4D9qDNHTLa3JsgUqjRfHdAXJFaEXhCwRlRfKptg-2D2STFa3xYtTlwwFiIrs1Ghr2DxfA87bVD9MXVt8d-X0Ia9dy6cngZ9rgNdD37y6f-xBpJNcQYmBwuVG4E41PMVmT6VPYsHO3ZVOUrJFKaBEgYV5BK9xqOkgXhuxTBUpG7T9fYB-HjNsAdmjqCfJeqVQmCqBxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ظرف24ساعت‌آتی رستم‌آشورماتف، جلال الدین ماشاریپوف و یاسر آسانی 3 بازیکن خارجی استقلال برای حضور در تمرینات آبی‌ها و دیدار حساس مقابل تیم تراکتور در هفته هشتم وارد ایران خواهند شد.
🔴
اوستون‌اورونوف و مارکوباکیچ دوبازیکن خارجی تیم پرسپولیس نیز تا پایان هفته وارد تهران میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30290" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu-rVc0tyCBNBQXVmjzW6wrV0ISjmat5wYLB3AyqaruVAL8vcJcj7Enp2Y_38aRzV9yr6wMju6ZyXPYQjQm0oGj1pKJXGspVy2hclVdBsT3_COxhqCWQaWBQ_9ch-iDQjm00s0Hwo2I_rtnRLIb7jJC75aMgiKRc1G9Ijiyn_7n2_WjlJYMKBDKMpSbadWKQ9Ef4ltsFnE6ZybcuU6MX-6u40BmT1b-p-ZXT_AoN_mLf8Fjjx87ox97LO2xTbZlCoXa3Z8RKWMArF_2sfyuFPkUlRs9No0bF8XyuUt-ojjoGHWa51tqySD3PqZZw9ER6xKD5DqNsYexPysi6ImbwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تیم پلی استیشن ایران در فینال بازی‌های آسیایی مالزی رو دو بر یک شکست داد و قهرمان شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30289" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30288">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hveivv0EuZX0Fazbk_aGUdZQyQiQJr8ulmpOwJtsHgttGdolGQlkYE1Gf9mNLJgqnonu1ikbJhfY6tOTggA-B0_aXMfsXGGaYDaX_ukSAlb57sawhs0buQLKXphpBCQmiDhdnQpNidUhqVPRXJknge4hXBKSfUW5PMg8ZmyLKARtIdOfuWhuYwacKMrTMi9Fe6REocgZhaOs4MTOi0KU08syL76y7A9VVTmgkMoyIqgtbCzJHKcF_6zoXdqxsMXpwcAgszqRFf-UhmsJSpPiz_j1IYiNiqz9TJtyvLeDSwl_9VREwCYtGYP1btDs6OGYSdY6HrGof_u3HnwHdCyjYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه.تعدادگل‌های‌کریس‌رونالدو با مجموع گل‌ های رافینیا،امباپه و هالند درکل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30288" target="_blank">📅 14:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30287">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQWmY1telovqKcmiPwy-V4JlTuJuVDSPe2TyW6qDFxeeuBKPfv6aOAxKWeX9KgH8gpzGmWN77n8lEGIGzI8-qb3kFOGsL184CS-qbPz0XUcxg8TZaReozNm1PGcjCocNdLqIJ0qv3C-CngtGAU8xy3asDk7TyoXa338n3zDD_JVn0oc0N9NmsMXBfBbFZjdbZq4jFTX5hooUGmco3_f0TLAdOS_tLHDIqqg8wxAzgXGWW136Z90v9sco5gXJjA_btOwSf_t9ZyF0pZ5XSNF7PDruP8Xe9rvpo_ll00lnBdi1UnYR4RDp-bDtGtNQfrPiwNv7b0zxhKIYRdbkGKD0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛ لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30287" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTRXSli2PniUJm0Y5pGFUnhxC8Wgz8CS0HsOnxVpWRQWuvoTRtunkpCZXQ--T59T1RVIdRYkO3FluDE_QnzBta15uMCOQ9hUnZYESUv7tPw4Nx-LYBchTw53sfzPXSlf_Ql3fDVDp4WI0HrIZtaZBnb9yrlkPko0HYgExpMOgNQ8dppyiPhIRk5-mGo6OM2XP2DNFHw7Sgc1eXDuIsNzywfUNoOP7LpUnLlo-T5x1EG3ViuAVhso_rKdd6nW4YhtizD63_-RdW3G-uiKg5r0nShop6IOuJ7D0esrFTBeZMburPuZcyt8OLyBg0i4wgCgeNa7Osh_yfA3fRDum2_mxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30286" target="_blank">📅 14:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeFXLrSqBW6cHIlj3HS-Zw0anE_AzGfhtGe1hP5tf8kAu7aQT2ciKzNEJUhRb4qA8QNngZiD2bS7zl0ckd11dBq-4c0IRcxOLa5DPV9bn91bF-vxi6BZtdOF28kOoB85EnskamuRJywMUlRpNZxYSOMR22ITzADHMG1kCxERyK1_ru3aV_1H_xvfBP4O8u4P57u8EDdMgYOTFS1AZpqnjkIh4bIzsLhdZPNrjPwuR3IVFd7gA2uRg7d7W268cL-qYsNxn70vUQ8SM4_wosQUIw1wi_XeXOj_FyrwltqtMdB3BPhBy4dGYd1QTvHtnfL9HuO5tnUXYXllJXlJupjhyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇳🇱
تیجانی ریندرز ستاره هلندی تیم القادسیه:
نمیخوام وقتی فوتبالم تموم بشه باز کار کنم به همین خاطر تصمیم گرفتم به عربستان بیایم در کنار کیفیت بالای لیگ این کشور آن‌ ها دستمزد بسیار بالایی رو به من دادند که زندگی خودم و کل خانواده ام رو تا آخر عمر تامین میکنه و نوه‌هام بی دغدغه میتونند بهترین زندگی داشته باشند. یک‌سوم‌رقمی که باشگاه محترم القادسیه به من پرداخت میکنه هیچ باشگاه اروپایی پرداخت نمیکنه. از انتخابم بسیار خوشحال هستم و میخواهم سال‌ها در لیگ حرفه‌ای عربستان باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30285" target="_blank">📅 14:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=k6kum2L9A8p7bjFxiYOlqr22njZP4_EDH076O21ofPuCDUHuyu_odBMNK3zIQR5zxu8pQfKxlOIq9xs2f9Lyp7tjZVAXXSINSjjqqtmQaRndHTqY505XfR2GjFGHSPYrWwoLvE8HtnAhet6mINfYS9jnvbCdY0R7IKnYmy-8u-vwnu2XYhT1mVomI7G-zedB1dFlqLen1WUBY-Pt09Dn9j3HTrTu5rLEguV2Oub5xUYPvWjitGrZiC1LKNoMzr-qnZZ55dfvxVF3t9Hdv4vDfYJbYh23sltT_9lfWFlkN_vx2mXgV4iNlJ9j0noyyzumVvDIErxd03ZFg3UUYvDnKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=k6kum2L9A8p7bjFxiYOlqr22njZP4_EDH076O21ofPuCDUHuyu_odBMNK3zIQR5zxu8pQfKxlOIq9xs2f9Lyp7tjZVAXXSINSjjqqtmQaRndHTqY505XfR2GjFGHSPYrWwoLvE8HtnAhet6mINfYS9jnvbCdY0R7IKnYmy-8u-vwnu2XYhT1mVomI7G-zedB1dFlqLen1WUBY-Pt09Dn9j3HTrTu5rLEguV2Oub5xUYPvWjitGrZiC1LKNoMzr-qnZZ55dfvxVF3t9Hdv4vDfYJbYh23sltT_9lfWFlkN_vx2mXgV4iNlJ9j0noyyzumVvDIErxd03ZFg3UUYvDnKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=NOH5lA7dprEJrrgKWJeABnhd7d-SgI4shM4kuwkZex_5_Klap8QBUhfJo7vaeruIqulije7bv279tX-l202OH9OKqQEzyP2EL4xaWe5w3ZgvhqqKJYan2ubERqYgVylcUylije8sP94R8BJDbfNW9fHMfhOY2RWe57lXJm5ifBWv6PcfPojsSavMZhWNq4lAPmYiQdkaDyV-1aDsvpNE7Hv9z8dvIZnoELxaGG5G5LacL1mbxQh6CSDYmDdbZLubPztvPBfF5SNHQZtYou58JMr4P0ZhEVPr02pbA8he7NfXgu0-fzAWqRh2gNpLXXaqzYC5Eiamh5d_s95njkNI9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=NOH5lA7dprEJrrgKWJeABnhd7d-SgI4shM4kuwkZex_5_Klap8QBUhfJo7vaeruIqulije7bv279tX-l202OH9OKqQEzyP2EL4xaWe5w3ZgvhqqKJYan2ubERqYgVylcUylije8sP94R8BJDbfNW9fHMfhOY2RWe57lXJm5ifBWv6PcfPojsSavMZhWNq4lAPmYiQdkaDyV-1aDsvpNE7Hv9z8dvIZnoELxaGG5G5LacL1mbxQh6CSDYmDdbZLubPztvPBfF5SNHQZtYou58JMr4P0ZhEVPr02pbA8he7NfXgu0-fzAWqRh2gNpLXXaqzYC5Eiamh5d_s95njkNI9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgytj80nDA_aJN_iWWBC_itAkuHjm_5ew7tulzkQicfq7L_O1oegNB4SF0xQ9n1ev-4aR-v5IAgq6WfKHkVPbErS5QShHt2JhukPvid1oEfgjSOM_jgdFDDXlknYzppE6pYpjgPzJq3ZEttUYgNtNla3VjkYVJUYD9IzNL0RabxlZm-6bSU6OYmnB9cjk8HBKMpaRK0QVIh8lsQT5pgpkKDOy48M6WimG0SJYbXD8gsQwAUZTbvd7SJ0TxNInC4UiPQdwjD1xO5r6bZIt5Cvd8ONA2smjFY3ujG9t17bsgoXOk4aPKO4gHarBdghMEcy7hk5IkvlJH-r7Ff3EEBSTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب بوکاجونیورز برای دیدار خدافظی کارلوس توز فوق ستاره آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30281" target="_blank">📅 12:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8Ms0Puxpps5zJfuePhr7VByCxMFHcS-O8URpDlZUsy-fxC6vDskb0EBafpPpEFuqGtthYLuRdszCpDwtMF9wupZHxRmiM835y6vzMuh7o6BZdqwfspSvTWqMX9RBf6hNyBNWz7y12SCnB8wr3DWE1bHSC62gpR7CXaAsEJdwawMbHyUABoITh8ZD4IR84IRskFHjQ81nIX7nXpNxtHOC_AH8YfYVPVLU7TREYMk6UljTT1o7W_k2GSYsZU7oiHUIALkhBzNMPgBUmdX0yfKWtsvF89hpFk1dwhPska5jQwgRIGP6j-CTJOz27vHil8mLWXRfj3mMnIZmg6-PQzlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناس شبکه CBS ترکیه:
«رافائل لیائو فکر می‌کنه برای‌تعطیلات‌اومده ترکیه. اون به دید حقارت به‌فوتبال ما نگا میکنه انگار ۵ بار توپ طلا رو برده.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30280" target="_blank">📅 12:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30279">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjqIL8TnhZIGY8RfdEyANBPwB5peexMFwYxm2dSVYYo1Wda55pu0AnXojXokLqMgEcPokQiaLNR9JcnmE2arA0sCBXYR8aDFMcQU-cWZ5TWtoYpz3M5gWVUYklQQ0aVeObWtWbb4D1T4_kE15EqwIJ0GqZhZUdEyMAgJS-uYi3_mYBIM7SIMaGSXCXex-w_FDhxMfeBRC-5vfH80Ga4-1xY1vxp1tZq8iYDUVIxZmMECQn9jGk6QHIaedzuxU-xf0mdqKoP2DWM7Bf2oFPaCPfUIrH3ZUWPtmYtjG06lkwBrQnKGLDXwP9MslleMpduTAlZGQTtb_JUdPMFquTw-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30279" target="_blank">📅 11:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30278">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYct-1jFSpp3nCBl2ZU3rNUwGyrTFZ88_5PQX66miaDh86DxXTBmnKWlfSoqdYdJ9qHpZKaMZcBqVEdzj0watG5QLMAjqkxTwyuIE5CdoC8l2MoxD9uwYB0-bt5Z5DoGfWtZfyHcRox8efEMlbGbBBQQBtGpksyWYm_sZDJrPWAyQAeM4Vb3D5d-514IFnnTMYcgFtPip78ibRq4xRLlSKEHflIs1xP1jTC7NFlbUFFho_FEecCS-l6dzk2ZM2kT2zJ5wlbXajtl0W73gcR2D2epPaFxYbF9gSY-JMZtuRiZWIN8wT79vUQ7UC_5LW8x3Qw4Z9k3rNapdN4Fjpxx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30278" target="_blank">📅 11:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30277">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMUVp1z31t6eu9qkc-b5hQs0ehsPgBTrsOjo3TypsfjcZx23rZPprO7KIy5srOzeJOctbNSjhjfQGembHFmfCuiKVb46_bm-hoycPF4av23aF7GDExbWJUkdV3F3uSwjpYEH9ClsXkLP6YMw-3j8EwsQznj4zy_POBcPgtJrXzrGcINjzug6ZjTyjQ48evIgA5hkj-nuFtUak-zbVqBBErubzAalAPlmoQpa5IYePjuv9n5fl6Bpy0d5tINWfg-HdJOiSPnwtwJ8BZtn_KeI87BnV6jUcdXd3Odm102Lxv30E009rm-ks5ovM-atT0eSWuJABjEKeUJ6I5AS-pkhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30277" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fjxi_Da0uzBZkZVmYjmDssJb6MT1eGKRV9b_AKtPOVOT9AYUuDQPq4_827nJ5ifabnNVCSPd4AEZYU89t5hqzCv7saSNA_t_fxJurCqNtke7av9XtOjBoefLrVCVy0itPpesq2XeDSMvt0pwIVtgPepVWwYarUTMd8stL9qyERU62CYCrWo0bne-ap4E_nhUrrNWJFNARjWtM_ycpunEla8Z0VZgL0p3EqcEWlwNum7F_LZATMNd8RcxSc6BwZBfntSn8j7qKdzT5O8w97X3KvEdtVCSid2SQA8QrHxbLUS6JlirCtDENVgXvMfWwhjC0fkTBHzKBBFmzamzK1BcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCASqmtYCePUSgHHeotOBZCQ6CUu8K6XKnHPHD9GrN73Df5bFkU14cr57d_kYe8xa-9tN1p4XgM-DZfeu4HI3_YD1qo1IB7unDpbBT95ck81ov9R4K-bQa6_Q8V2k5MGcv2MEzycByUcjU4h0m1vXgVWLq-pZbWFTa3-sJrFs7ScGj8evbQuYBGtt14zKFEp52tyTleXD5iqpNqaO5cdfK9wEgVMmmzO7maeKapB64Wz7IKTkyjp7YH8362JxPA5eAkqsmMpp1yBEgKAkMdCLK8z2JhR-OQOE8cCbSWgzVcDn2PQzoYSRVQYNtiNi6TmEHmNLPxODC21HFiOa3zDNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30275" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SP19LLcOpZ9TH1s7KvwF9BRkT2Iy4wfAMdIUJSCmaVbJ5-mO6TB8ChX5h0sAGmby4C_qrSwCO9b3h9VTmF2Vl2IEwmTEVB2TPMZ_K0l325t1I4oXc7L3Tj1EK2lAHgVfhMJSGsJCt04ilR1IJyMn5XdlVJ850YCsJp1iN38WyzzSBzEIyOtiJT9yE-n24cdKOHze99yCHeRNDJ16ICEPlYgzboAyEp2d9wU8Nq5E87aH4SZpGP969IMMEU1uEyK9LdPNiSSaq_y_i8zR_COhLISUHpQHz4IC_uMmmOnmfTQyH3KG_L4OUTgxY9GTAnEpZWk79bQDfpoN_pYgnoQdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30274" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30272">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBh2u4HHoajiiLYZckpvAdW5LRnyKJ-N4S-Nbf9ComOkDM-UD6_Acg8nTmhXKUWzg59qdCw2KNVI5o1E59ISorhzPgtpTk4f5pBTzYdIlWrOth1kl_xUIb-u0ylR2sdpTiBNsRwHgNV2nGnccOKzGSfwzfmyM2Wf_tLCZaevWwDWAlp7Sc_1x9FNlmArowfXSmqnZbDf3e1El21qov1O4fg6E4u_TqfltrrcXAc1i6vzGkbyZW_9VVWOVlRTezt2Eg2NUicFXwmVKutyWGcMEZjAqT9jPF-Y2IKTchTYTKKguR-Vwi-rSmb6MquN9JFsa0aFFHiR8jI5oN0j1-XTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مثلث خط حمله بوکاجونیورز در بازی دوستانه خداحافظی کارلوس توز آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30272" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=mkAnVadPdA7VxjHdtmDnPyWCje1fsUN7lCE1n8vQDWTCOYreME4oYzGPvtoeHRw30loLyhOuSXJaVrd814mZDE9OTLEhEk3nAFNcTl2BHYEdtm_93SHLg8iFrLSHZDC0PzSp2ze4rzTwQ4SIGvEpOeXTDVTXWwfmUQAvRGm3IB-4QpI_NtD4UOLeDdHqqQflLuvjqQ6u-_OV9qyZSJfRdZPx8cEX4tb1Yv0hyITW6aFEWYIuwRQI1HHEjP5vG-jb9J9gn_XySoGf5pnEHys2PWUFrY5buFz7sNnjqM6_Lra07JTlVNAjlCFpvgUzLj-vr6eLpKH3T7BlleFCt1I0ZoVgyyE-wZP6N_s1Fz_lrjt4YV-3S8jV927ZYYUDOpsDUTqVIaySimpOcxjuwEKcBxkwKPjJfcUhXoOcnCWjQ99VPnlbj3z4324bwXn3ibxvmv2hRBnNPKoJuGa2CbY9CRztSt8Klzd3yW-El3wPevp6b9zwMqqoTu77zS0fNEN5sHK1dS_0l-s2gHOBmCl0ZX1_p2_AVNNKN3c8mrfaEDSkaOQ9Ykp_kcjzqTrcWbx2BDWp1HEE8-6Bae-nIRu6W12Rq392xecObYozQP-ZMPEXzcCSL1vjNfml7WToTNJPRc5pRy0qLPkeA16QgPeYK1dMSR1pMTsjhMt55wweGF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=mkAnVadPdA7VxjHdtmDnPyWCje1fsUN7lCE1n8vQDWTCOYreME4oYzGPvtoeHRw30loLyhOuSXJaVrd814mZDE9OTLEhEk3nAFNcTl2BHYEdtm_93SHLg8iFrLSHZDC0PzSp2ze4rzTwQ4SIGvEpOeXTDVTXWwfmUQAvRGm3IB-4QpI_NtD4UOLeDdHqqQflLuvjqQ6u-_OV9qyZSJfRdZPx8cEX4tb1Yv0hyITW6aFEWYIuwRQI1HHEjP5vG-jb9J9gn_XySoGf5pnEHys2PWUFrY5buFz7sNnjqM6_Lra07JTlVNAjlCFpvgUzLj-vr6eLpKH3T7BlleFCt1I0ZoVgyyE-wZP6N_s1Fz_lrjt4YV-3S8jV927ZYYUDOpsDUTqVIaySimpOcxjuwEKcBxkwKPjJfcUhXoOcnCWjQ99VPnlbj3z4324bwXn3ibxvmv2hRBnNPKoJuGa2CbY9CRztSt8Klzd3yW-El3wPevp6b9zwMqqoTu77zS0fNEN5sHK1dS_0l-s2gHOBmCl0ZX1_p2_AVNNKN3c8mrfaEDSkaOQ9Ykp_kcjzqTrcWbx2BDWp1HEE8-6Bae-nIRu6W12Rq392xecObYozQP-ZMPEXzcCSL1vjNfml7WToTNJPRc5pRy0qLPkeA16QgPeYK1dMSR1pMTsjhMt55wweGF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛ مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30271" target="_blank">📅 10:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30270">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=tibcVC8b40kLU774yHzmsqwF_4KvQqKdb539bH4xkY9H_phEIZEHuGaCefAqsJ_oRkDh_3VI3kPlvb-MtLhbJ5q1fk3CoXKhJ2p5OjIhSgIt-xohWnB8Ki041Dm7gS-M8b75bM_8qrVBudO42DhBJ4D770iqEowU-MIvnZS4o_hMsxpjNJcpvR5p_yYFa0P6R4_guqIUNAap7y6RlIeNxY3Vx9TyuYIe3MmUawTS7Czgu2FCGvOX-sSB0Or7aqflGs5deaOwLezsdKGk6KWLzQhYbU5L1GR7aHIUvedt4yJD0nmPg_qx3N9zV6yEqYtBSyRaBaO8KXUaMXWIZ6827g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=tibcVC8b40kLU774yHzmsqwF_4KvQqKdb539bH4xkY9H_phEIZEHuGaCefAqsJ_oRkDh_3VI3kPlvb-MtLhbJ5q1fk3CoXKhJ2p5OjIhSgIt-xohWnB8Ki041Dm7gS-M8b75bM_8qrVBudO42DhBJ4D770iqEowU-MIvnZS4o_hMsxpjNJcpvR5p_yYFa0P6R4_guqIUNAap7y6RlIeNxY3Vx9TyuYIe3MmUawTS7Czgu2FCGvOX-sSB0Or7aqflGs5deaOwLezsdKGk6KWLzQhYbU5L1GR7aHIUvedt4yJD0nmPg_qx3N9zV6yEqYtBSyRaBaO8KXUaMXWIZ6827g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛
مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30270" target="_blank">📅 09:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Q5UwGGYXgI5nUqab5ImxthB6lGa2SC5KT0iHSHs236pPoc3FmoTrfxbdUP75tXvlXo6IymGHSTjgvKu2SwdL7RFylCpYxJCSeXLm5T63vHymcHeX2Nhb27p8OPoumOP71wApcfoDd5mW_3lXBj2WYyhIqtJh3Z8wc5zIGoDH40wMGOmXQnetDOhVUY6V5MtAV2NcvdNzbRac9XnG37mIsiijs9SqqgWRlCXDY-2CCSqMSk3LHCeOgidR66CBj44Av0TmYfYGNBRCce2dvhmdxEwoguqV1_SInnz1KTTu1Nfk1Bx8Sly-Q8XaF9QN3Qkt76jXLzU_-2187g2kQVMXvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=Q5UwGGYXgI5nUqab5ImxthB6lGa2SC5KT0iHSHs236pPoc3FmoTrfxbdUP75tXvlXo6IymGHSTjgvKu2SwdL7RFylCpYxJCSeXLm5T63vHymcHeX2Nhb27p8OPoumOP71wApcfoDd5mW_3lXBj2WYyhIqtJh3Z8wc5zIGoDH40wMGOmXQnetDOhVUY6V5MtAV2NcvdNzbRac9XnG37mIsiijs9SqqgWRlCXDY-2CCSqMSk3LHCeOgidR66CBj44Av0TmYfYGNBRCce2dvhmdxEwoguqV1_SInnz1KTTu1Nfk1Bx8Sly-Q8XaF9QN3Qkt76jXLzU_-2187g2kQVMXvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioGg8T50RxMt5kvoKRsWMXVMQJdsyCM_kRFf7MmjST2pRgouiIzxz3WE3DcFQLQEFtt0PmmYiBZLQbr72SbF5eUSv3lWRivJHV5Z8Q4KFPlrQeZqDI2lWkYV-_bT2N-GiO8HG-J9_7e0EXU4fQLOrZjj1iFjuzPCDEZOA9NmJcYmihD61Y0fiCeOBEQMH0nJ72lNXAxBMSOsjRvp1gdFx9KKCLMYMpC5FDFPmU3xwqX5qvNoBTtIMPvnY_IYtKpogkkj9l0upd3Xkfd03KBe_wWTkBSCHyeN1oCPQbZwqLhiIBwk67C2030Ux8P4JrPzuiusAq_3Sk4f-UTELG1gjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
