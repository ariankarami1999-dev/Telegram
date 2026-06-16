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
<img src="https://cdn4.telesco.pe/file/bEiDHH-8iQI9KCUJeW3glFQxnGg2Wfgu71d4xPcJa19CSCtgAQwVcrSfciJL7bbmq2e2dezjtafjh9qrnjmPXLhVhQk2P4cXVOf_h8uJ8bnzlzQ3vg5PyF2xv-xc_OE4vf_bdwOVOlv2LbdPI4flKC6oG2xdYULSeZu-vf2WFMTF1kZNKYC1Sk-Yifhbj4TBlfuVxHjeQ5SMAxlXOSXSkcoUSJQvvFYmPttnbtDvOZP2wxKvrHb_Fbf8RjQBTfX6HeScnHt6jem9zgrnQHAqq4tbztiMtoOint3srtpjF-k-z-4sGH4Ux-IKcP2lIU6ahTQzNsqMmux3oQfDS38d7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-15032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عراقچی: هرگونه حمله نظامی اسرائیل به لبنان ، نقض یادداشت تفاهم محسوب می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/withyashar/15032" target="_blank">📅 12:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کیهان: معنای سکوت رهبری درباره هسته‌ای این است که دیگر مذاکره‌ای در کار نیست
@withyashar
روزنامه کیهان وابسته به اصولگرایان تندرو نزدیک به بیت رهبری است و مدیر مسئول آن مستقیماً توسط علی خامنه‌ای انتخاب شده .</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/15031" target="_blank">📅 11:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15030">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=DoL-WPuS9iT9dhuCkujjV4YdDuXXuC8OAghEszLCrdPobPcwrjgRYkO8qC7OZuIrmgf0Misw2HBs7YTVCa__PrVgt4HEkIV_c3mCUuP9VfUcWvKANZ3HcOkS20GcbcaYRNk7sV295Lw65gsxMHSClDDL4S6nUDDi7jXzDx6XT3FqOA-4WSppyWxZmqYlKTkXrcMAsGIZx5h9NPOyJtoBhIW3Dxs74TSGuECvw5_1hFmDQlHnnusz5_WT_DYPlFUWn0tePUg3ndlKMWQytrcPbs1TkidFAw6UiouP6OvaBXp9LKyoTgVFMdIe7-i5nnTfNQbOGqwjYx6rmrsr8cK31A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bf6e0591.mp4?token=DoL-WPuS9iT9dhuCkujjV4YdDuXXuC8OAghEszLCrdPobPcwrjgRYkO8qC7OZuIrmgf0Misw2HBs7YTVCa__PrVgt4HEkIV_c3mCUuP9VfUcWvKANZ3HcOkS20GcbcaYRNk7sV295Lw65gsxMHSClDDL4S6nUDDi7jXzDx6XT3FqOA-4WSppyWxZmqYlKTkXrcMAsGIZx5h9NPOyJtoBhIW3Dxs74TSGuECvw5_1hFmDQlHnnusz5_WT_DYPlFUWn0tePUg3ndlKMWQytrcPbs1TkidFAw6UiouP6OvaBXp9LKyoTgVFMdIe7-i5nnTfNQbOGqwjYx6rmrsr8cK31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبی بعد از  زدن گل دوم، با نشان دادن اسلحه و شلیک نمادین به تماشاگران نشون داد این تیم مزدوران حکومتیه نه مردم ایران
این نفهمی او واکنشمنفی‌ در‌
رسانه های جهان داشته
@withyashar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/withyashar/15030" target="_blank">📅 11:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دونالد ترامپ در گفتگو با CBS در واکنش به سفر کاروان تیم فوتبال ایران به آمریکا گفت:
"افتخار میزبانی کاروان تیم فوتبال ایران را داریم. آنها تیمی بزرگ هستند.
به قلعه نوعی گفتم اگر اینجا جایی نداری شب بمانی به منزل ما بیا. شاید قبول کرد. شاید هم نکرد. باید ببینیم چه می‌شود"
@withyashar
.
😂
شوخیه</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/15029" target="_blank">📅 10:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ویزای مهدی ترابی باطل شد
در حالی که برای بازیکنان تیم ملی برای سفر به آمریکا روادید «چند بار ورود» صادر شده است اما ویزای مهدی ترابی تنها برای یک بار ورود اعتبار داشت و پس از سفر تیم ملی به لس آنجلس جهت دیدار برابر نیوزیلند و پایان این بازی، اکنون ویزای این بازیکن منقضی شده است.
فدراسیون فوتبال ایران برای اخذ مجدد ویزای ترابی اقدام کرده تا این بازیکن بتواند در دیدارهای آتی تیم ملی را همراهی کند.
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/15028" target="_blank">📅 10:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.    جزئیات تلفات هنوز گزارش نشده است. @withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/15027" target="_blank">📅 10:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15026">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ونس: ترامپ ممکن است که پیش از روز جمعه، جزئیات توافق با ایران را فاش کند
جی‌دی ونس، معاون رئیس‌جمهور آمریکا اظهار داشت که رئیس‌جمهور دونالد ترامپ ممکن است تصمیم بگیرد پیش از روز جمعه جزئیات توافق با ایران را منتشر کند
@withyashar</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/15026" target="_blank">📅 09:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15025">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امکان پلاک‌گذاری خودروهای بالای ۲۵۰۰ سی‌سی در مناطق آزاد فراهم شد
معاونت حقوقی ریاست‌جمهوری در نامه‌ای به دبیر شورای عالی مناطق آزاد از امکان شماره‌گذاری ملی خودروهای وارداتی بالای ۲۵۰۰ سی‌سی موجود از قبل در این مناطق خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/15025" target="_blank">📅 09:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15024">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Feb-BcFQr3mdZNT8KDJQtj_WuR8ILus-L9BA_r8CUCC3CIEUm_JrR8-lEGiH2ie9PRhKGwCh6ypMoF7pmdWDtRSIlSTxJR4RmuNqCtxfRsDB_rlxgJ3UDXeULm38MWfXoROinhj2k7stOtPC_3DpyWL5fEQuZNXMXGqRSF4IMuAZGcM1gRw66jqyfOL7W9Zi9TIbzUU1jbh2K6eBCn3g4KnP4S82YKG12RL9BMgUeAWAMRxdQmpXL5JuVJ7wDmB0wKRUlh1jtK5z8An2aYMyoxJfyuV5S5cHwOsJwLMFdUS6o2k8PDdkPysbAlk5eYLQtp2AGJj-14e-2Smt9qhSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندین بار در جریان بازی مسابقه امروز تیم نیوزلند و تیم ملی در صدا و سیما پرچم شیر و خورشید به نمایش درآمد.
کارگردان فیفا تا حد ممکن در حال سانسور صدا و تصویر (شامل هو کردن و پرچم شیر و خورشید) بود. از طرفی تعدادی از پرچم‌ها هم با نزدیک شدن به پایان بازی توسط نیروهای امنیتی جمع‌‌آوری شدند.
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/15024" target="_blank">📅 09:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=MDsFAd1BQjAf5CH5qGFZnl35DwKrEFfO_vtX_2o1ru-8-Bpu_PSBMeLZceuSu2R3Qg4DEY-t4X62kzzmcfRc5mNhT76ho4x1PrmRqMztFl4tus3iND8pn_L7LCyO3ZgXCFPcwpNk1LYUtpSxoZ_oW1u8qcYM64LUicqTT2C2XE_5ODgnav-MeWF7d0Cc9btc_O40Vv65iXh8Lkl8Tu8QxHKS6FmjEHpN3N7Ean9dfn-jY3gG6DM4OITSngwnldU6LcrUVKWOxi6DneycBGx-yOXWg_zXShOv0-nHdpnq3cp6lHjlItKUwiicIf5f3KPV_lHCsX7e--4MlGrnkwV8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a672a698ff.mp4?token=MDsFAd1BQjAf5CH5qGFZnl35DwKrEFfO_vtX_2o1ru-8-Bpu_PSBMeLZceuSu2R3Qg4DEY-t4X62kzzmcfRc5mNhT76ho4x1PrmRqMztFl4tus3iND8pn_L7LCyO3ZgXCFPcwpNk1LYUtpSxoZ_oW1u8qcYM64LUicqTT2C2XE_5ODgnav-MeWF7d0Cc9btc_O40Vv65iXh8Lkl8Tu8QxHKS6FmjEHpN3N7Ean9dfn-jY3gG6DM4OITSngwnldU6LcrUVKWOxi6DneycBGx-yOXWg_zXShOv0-nHdpnq3cp6lHjlItKUwiicIf5f3KPV_lHCsX7e--4MlGrnkwV8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">7’—Iran 0-1 New Zealand
32’—Iran 1-1 New Zealand
54’—Iran 1-2 New Zealand
64’—Iran 2-2 New Zealand
گلهای بازی و تساوی ۲-۲
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/15023" target="_blank">📅 09:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=UvX2cHOkS0nJ4SgD2l0eKcvy268nyelWD-sjxTRmYw_XU4suwZSugi-pg9XTd3JG2nGucG4mWQNtTsRmSYgs6jkzpUYPKoaayx9nBxQZrxbD6WVdQTbwgBnNyDNVidsWKTMbyYFUbXPCRwOgnO__Mr4inRSeRao_WxuC6jGCO9-SpjywFEGctLpD9ikTM6g2smRVWmmj1NbtlZ5I7MbtgHDEg9JYjueE96fHt97ajXOAlg92YpvjRV2rNWNRQ-ePQB6gxG3seHRXU3810fAIdVo09EEC3wKg6JcWQtzh-9VFROWMF1lJxOYrdrfqtia8PpT_H9VqA3Z3xmTs8a9Ncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ecb9fedcf.mp4?token=UvX2cHOkS0nJ4SgD2l0eKcvy268nyelWD-sjxTRmYw_XU4suwZSugi-pg9XTd3JG2nGucG4mWQNtTsRmSYgs6jkzpUYPKoaayx9nBxQZrxbD6WVdQTbwgBnNyDNVidsWKTMbyYFUbXPCRwOgnO__Mr4inRSeRao_WxuC6jGCO9-SpjywFEGctLpD9ikTM6g2smRVWmmj1NbtlZ5I7MbtgHDEg9JYjueE96fHt97ajXOAlg92YpvjRV2rNWNRQ-ePQB6gxG3seHRXU3810fAIdVo09EEC3wKg6JcWQtzh-9VFROWMF1lJxOYrdrfqtia8PpT_H9VqA3Z3xmTs8a9Ncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج مکزیکی بازی ایران نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/15022" target="_blank">📅 09:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLg7IleMcnLdSesLOFhnUs-8cK47n_UEXJkPUvtsWWXTjr6nC4U8anBhHZOGzeCZzZRSbz2D-o6lrjh4kzmeIHNR_87MHpyEMPXz3gDog5-wdpmEmjoJV0bwmLIkxCV37TmfB0JesWfr3NfOow093RIuL7dLt8WZv8Ce5UTIV0Y9wTbUf3hq3rhcO83Ckzp5bjCuHM6JsaxuT_mwnOktmmsAaB_wokcihLhGboJoNbmjhL9MWRDSXZiQEOiE278O2-5cxEAxEs2bx2Wb9gyQLQsm9i37C1v-qF7rfvCNslLgyqz_WpI3527BuIfZnH5l4z5zMbleF9f012t8Bsho6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین داستان اینکه آمریکا به ایران ۳۰۰ میلیون دلار می‌پردازد، خبری جعلی است که توسط دموکرات‌ها منتشر می‌شود!!! رئیس‌جمهور دونالد ج. ترامپ
@withyashar
فقط این ۳۰۰ میلیارد بود که میلیون نوشته</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/15020" target="_blank">📅 09:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769eece9da.mp4?token=PT6p-fM7vqWPmBPQQe9sUYfY3ub4lDn5pKGmqUFX8q4kDJ5VYdrUksiErRyldl8QKVn3jcSOzNeCIWqmjSF7-4QWP8xH-l3JRPSH839ZYbojqwpgCqOfC7ZiN-cPlXP6nDQI9le1Oz8KFyO4UKtFf2ORTyGslvoilKStit4lZO-_CKGz8CtgPaU1T11C7lOiVHf7LF4DTiupMo3al-EC6un2PydsvdHbU_UiORi-LSGhdCaE6oHvUlseuCzQZxJ5RmCmMuqwrifVWErRJTFBREPxZ5Ikd9oVeR6c-Dz-ZrVfClbT7t6BZbPlYxJxUNR5Zb18IunTleu4GNl_mhFBIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769eece9da.mp4?token=PT6p-fM7vqWPmBPQQe9sUYfY3ub4lDn5pKGmqUFX8q4kDJ5VYdrUksiErRyldl8QKVn3jcSOzNeCIWqmjSF7-4QWP8xH-l3JRPSH839ZYbojqwpgCqOfC7ZiN-cPlXP6nDQI9le1Oz8KFyO4UKtFf2ORTyGslvoilKStit4lZO-_CKGz8CtgPaU1T11C7lOiVHf7LF4DTiupMo3al-EC6un2PydsvdHbU_UiORi-LSGhdCaE6oHvUlseuCzQZxJ5RmCmMuqwrifVWErRJTFBREPxZ5Ikd9oVeR6c-Dz-ZrVfClbT7t6BZbPlYxJxUNR5Zb18IunTleu4GNl_mhFBIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس : هیچ دلار تخفیف تحریمی یا پول بلوکه‌شده‌ای، نه از آمریکا و نه از هیچ‌کدوم از متحدای ما تو خلیج، آزاد نشده
این امتیاز فقط وقتی بهشون داده میشه که به تعهداتشون تو توافق عمل کنن
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15019" target="_blank">📅 01:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پرس تی وی: ۳ نفتکش و ۲ کشتی با کالای ایران از محاصره دریایی عبور کرد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15018" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">@withyashar
تحلیل وضعیت</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/15017" target="_blank">📅 00:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCk13Ml3gh-O2A0qWa2JIJYRKPotzZRH5cbbvzthUZGLd5uJJhP2v8DcvojqMmJ9DAvugX15VbyCvpP7dpbIeNsDY0RnOG9puouGDLM17npfkEspPSJKIVIohaunMh_-lAX6Ia1XlaBRMHTcic0jaUItC7W0VR4zHlcdumMdMIFrvWJWJVIeu51mU_W6pyEi-mmPpvtzb9SlwbhxQqEsf7GO3q1Y0EJZLaEFBIu2ZSrYqSjNNZ0JBBCjyM9NmWoOvKQbjdYva4gGO0KLgT7ON72O0arree67v8Kdp112-vbz5gXJy2eUyCWSGXA9gIY7k2sqzTDGqdXyAn-gyrlbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشم  سمت سوزا همین الان خیابون اصلی
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/15016" target="_blank">📅 00:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صدای توافق از قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/15015" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzx5-f7FSHtSinG5XunIZiRAwdqnJTlVuZG3Dpsq_elQbBWFlStBtE0tLrCsiCYpMvLZng4gQ42ecNU9sdK4QAEwv9GleERu80Hb5jO8EGruBmZP4OOX0DU1eloizbKo0Zig6pPBrfTWx1zbE7Bpo_fyYRodhwYAqD_9YXH_myhqxsIp8Z8LNMbN7K2qYvJ0aPqR38aIpc_rJfJkvysrHBF-SkO64ZUpQySFy9V8QmGO69SbKhgfAPI8h_XMfXbMqX1CmFQ6TEFonPzX--Ahr6TjH1MkzrY0YPgSv6dK16YLeWraPxiXMyqhkH6ieE9TxzGzlj6G1fiTwAbT3Q_p7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
توافق یا عملیات فریب برای حمله وحشتناک امریکا و اسرائیل!
⭕️
مشاهده تحلیل
🇮🇱
🇺🇸
🇮🇷
👇
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/15014" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15013" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال ۱۴ اسرائیل: تعجب جامعه اسرائیل از این بود که مقامات ایران قبل از دفن علی خامنه‌ای با قاتلینش توافق کردند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15012" target="_blank">📅 23:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15011" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15010">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عراقچی: جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15010" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15009">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیویورک تایمز گزارش داد که ممنوعیت ورود پرچم‌های شیروخورشید ایران به جام جهانی که از سوی فیفا اعمال شده بود، پس از برگزاری یک جلسه اضطراری دادگاه در لس‌آنجلس در روز دوشنبه تایید شد و قاضی کرتیس ای. کین حکم داد که این ممنوعیت به قوت خود باقی بماند.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15009" target="_blank">📅 23:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15008">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76cd0f1e71.mp4?token=U6XOhoDdakbDBNi8AbfAJIq9Is9Aih7FAB0RnOKoLt1GvoZh8rrZcPoGKzZNrYTPmUVp84ltFiXPpyi_SJq_w_Wzf6ylQoIYH7u7gWY9gmkyqePlq213ZLu54RyCSq8trNVSAtE_khrwxJ00dlLyrieAEa26-Kan5u02yJjKczIr8FhCg3qq-QmakQ9yvqLi9zH1_aS1gJw_0i164GosEN0mLezYNIkciP_AUFQ9nqPY2_0l-t37ujBrQVzfwMGJaQe6VCp7aKm-ZMdH_tS9HLaHcslAnqPXCYVgTETI1cKzZztz-9YnS-Z3Ky6LnIDwCKZ1VpTuMDBW4CtM8BkueQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76cd0f1e71.mp4?token=U6XOhoDdakbDBNi8AbfAJIq9Is9Aih7FAB0RnOKoLt1GvoZh8rrZcPoGKzZNrYTPmUVp84ltFiXPpyi_SJq_w_Wzf6ylQoIYH7u7gWY9gmkyqePlq213ZLu54RyCSq8trNVSAtE_khrwxJ00dlLyrieAEa26-Kan5u02yJjKczIr8FhCg3qq-QmakQ9yvqLi9zH1_aS1gJw_0i164GosEN0mLezYNIkciP_AUFQ9nqPY2_0l-t37ujBrQVzfwMGJaQe6VCp7aKm-ZMdH_tS9HLaHcslAnqPXCYVgTETI1cKzZztz-9YnS-Z3Ky6LnIDwCKZ1VpTuMDBW4CtM8BkueQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از محل سقوط بمب‌افکن استراتژیک B-۵۲ آمریکا در کالیفرنیا
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15008" target="_blank">📅 23:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbiRISAR4cgVvHP0s-4y4bU8klF65a2_PbpMlBjcW-G6FICvG7Is5EGWw5seoNC2kUT-_78B1O95ipRX8OEp7kOAC6IVxTQbV0njiKQosgtFXTwiyI3tondKf2QGkQWK36VezDsWNPNEMnGHLjzcookcLBjE6aEonAPo1ipfuNqJTsN0B_lkMvk6JtqzMRJqyeagQCIdcGPXDk8isbMCCUn4rR-ilHnr7PodkMTElgjmYDG4OOH99JPvZcYWuVNlEeZpJwi_Yh5rJH18fs68Fyf4GmhMWjZ0KUYCP-ce9YxbEsewin3QHumz3xyPlr9Kp6apxNXfz3tqyNhAiTjGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.
جزئیات تلفات هنوز گزارش نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/15007" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoji pers</strong></div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15006" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به ارتفاعات علی‌الطاهر در نبطیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15005" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15004" target="_blank">📅 22:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پست جدید که در اون هنرنمایی هم کردم براتون کلیک کنید و حتماً کارهای اداریش رو انجام بدید.
https://www.instagram.com/reel/DZngOTKRtYt/?igsh=MWwzcTZmaW9oZndxcQ==
⁨ اتاق جنگ با یاشار : سفر قاهره «ملودیک»⁩</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15003" target="_blank">📅 22:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو: از موارد مورد توافق بین ایران و آمریکا مطمئن نیستم ولی قطعا در انتخابات پیروز خواهم شد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15002" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSMPGHtKuoVggtPrrnefCQxcUoknwx1nCu9dz7p1JcXiv3BThtqGeBGYAn_rD8g9yPxVGDPEfJFMjUzhF3mGPM1ik1OYVM7LdrI01wa8-KCZMsV5eaZLZyBJFrSIk9cfIkv3H5PC8KPfCZ0WUcqu0Q95OgCDccNZ3_BnXz0gwzM0ZAiTFyDE_zs9OPKA5GL49aJ9wEGjx5gkgnK0nHEq4jyv6RPHEDro8xXrM7t4PmS-w02pFOgs9V7BkaCPJm6VGp8iAL3L61BJA9w63oNrFiPp-_PzzPkz5PdDHq1nxE-MxgsPozsB3yg8f2MAJkAPS6G10iTaCexJRqzHHwsy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/15001" target="_blank">📅 22:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: تا خلع سلاح حزب‌الله، اسرائیل از منطقه امنیتی جنوب لبنان خارج نخواهد شد.
همون کاری با غزه کردیم، با جنوب لبنان هم خواهیم کرد؛ همونطور که غزه دیگر تهدید جدی‌ای برای اسرائیل نیست، حزب‌الله هم در آینده نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/15000" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو: توافق با ایران توسط ترامپ منعقد شد، این تصمیم اوست و ما منافع خود را داریم‌‌
ترامپ رئیس‌جمهور آمریکاست و من نخست‌وزیر اسرائیل؛ من از منافع کشور خودم دفاع می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/14999" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو: من نگفتم هدف ما سرنگونی رژیم ایرانه، گفتم میخواهیم به مردم ایران برای انجام این کار کمک کنیم
@withyashar
یاشار : توجه کن این جمله بار حقوقی داره با این حال بنیامین نتانیاهو بارها این حرف رو زده</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/14998" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14997">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتانیاهو
: مبارزه تمام نشده است. ما باید همچنان هوشیار، قوی و مصمم باشیم تا از خود تا حد امکان دفاع کنیم. این نه تنها در مورد ایران، بلکه در مورد بازوهای تروریستی ایران نیز صادق است. ما به شیوه‌ای بی‌سابقه به آنها ضربه زدیم. ما این کار را در غزه، لبنان، سوریه، یمن، اردوگاه‌های پناهندگان در یهودا و سامره و همه جا انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/14997" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14996">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو: من با ترامپ موافق نیستم،
بنابراین، اسرائیل هر کاری که لازم باشد در برابر ایران انجام خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/14996" target="_blank">📅 21:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14995">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شبکه ۱۳ اسرائیل به نقل از یک منبع:
تل‌آویو و واشینگتن بر سر عدم عقب‌نشینی کامل اسرائیل از لبنان به توافق رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/14995" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14994">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=Otn_TqZI3NN1qSQzT2sjweoDOcWkswXDJfCDmtQagjptaLvLjmi6N-Nhdez6FnVSu3Kesz7SDL99TWqm3Gc5e9e_-vJ8fO1Ex0tRXt0TsFPdNm2LV6EKWEvSw3qmN-zryAN95v0JX398j-cjPDdsBD9ym82XuNxke0hCoS3_1gHXJsZVk6BOM-FeV33FtKScggsb3WpGStjhxZ5FzGaPAd-8Axie5JPQtlNwyuAWgksLHgS0E4-gizMFBqnTXFQ4V4EYjLG_lmqWd9ZtWNRoqp-Kft141A-Q74SSWNGhX9ZfyNGOWdQSdkyoqE8F-wQmldbHQEDSADlaOvvhWwGRmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbac886c1.mp4?token=Otn_TqZI3NN1qSQzT2sjweoDOcWkswXDJfCDmtQagjptaLvLjmi6N-Nhdez6FnVSu3Kesz7SDL99TWqm3Gc5e9e_-vJ8fO1Ex0tRXt0TsFPdNm2LV6EKWEvSw3qmN-zryAN95v0JX398j-cjPDdsBD9ym82XuNxke0hCoS3_1gHXJsZVk6BOM-FeV33FtKScggsb3WpGStjhxZ5FzGaPAd-8Axie5JPQtlNwyuAWgksLHgS0E4-gizMFBqnTXFQ4V4EYjLG_lmqWd9ZtWNRoqp-Kft141A-Q74SSWNGhX9ZfyNGOWdQSdkyoqE8F-wQmldbHQEDSADlaOvvhWwGRmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:  ما در لبنان خواهیم ماند. کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/14994" target="_blank">📅 21:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14993">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو: ما خسارات عظیمی به ایرانی‌ها وارد کردیم و اسرائیل را از خطر نابودی هسته‌ای نجات دادیم.
اگر ما به سرعت برای حمله به ایران اقدام نمی‌کردیم، این کشور به بمب هسته‌ای دست پیدا می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14993" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14992">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو: «اسرائیل تا هر زمان که لازم باشد در “مناطق امنیتی” باقی خواهد ماند.»
«ما شراکت‌های جدیدی را در سراسر منطقه و فراتر از آن شکل خواهیم داد، در حالی که توانایی اسرائیل برای تولید و تأمین مستقل تسلیحات خود را تضمین می‌کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/14992" target="_blank">📅 21:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14991">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/14991" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14989">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مقامات آمریکایی اعلام کردن حتی با وجود توافق قصد عقب نشینی از منطقه را نخواهیم داشت و نیروهای آمریکایی در منطقه خواهند ماند.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/14989" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14988">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/14988" target="_blank">📅 21:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14987">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما از لبنان عقب‌نشینی نخواهیم کرد، اما از این پس هر عملیات نظامی قابل بررسی خواهد بود.
ما برای دستیابی به توافق بین واشنگتن و تهران قربانی شدیم.
معاون رئیس جمهور آمریکا از نتانیاهو خواسته است تا حضور اسرائیل در لبنان را کاهش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14987" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14986">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو: می‌توانید طناب را با آمریکایی‌ها بکشید، اما نباید آن را پاره کنید.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14986" target="_blank">📅 21:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14985">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۳ اسرائیل به نقل از منابع:
گفتگوی پرتنشی بین نتانیاهو و معاون رئیس جمهور آمریکا در مورد حضور اسرائیل در لبنان صورت گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/14985" target="_blank">📅 20:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14984">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرنگار : آیا قصد دارید در تشییع قائد امت، حضرت آیت‌الله عظما جانشین امام زمان علی خامنه‌ای شرکت کنید؟  ترامپ: بله @withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14984" target="_blank">📅 20:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14983">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار : آیا قصد دارید در تشییع قائد امت، حضرت آیت‌الله عظما جانشین امام زمان علی خامنه‌ای شرکت کنید؟
ترامپ: بله
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14983" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14982">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fba57ac4d.mp4?token=DP3kl88fU9gievQuLldaUumNC9YN3G7DV_vI8Kn-BtgGJLan17vMs5xNMYtD2Kfc5f9m_o-YudH4Z70I6WXe0MuF1S8mt2C38_S2q8jZHjHeZlEmRppYz25WwYV4R9qpBMVOC_SNSgPdUawCWVC2clCoVf7o0n3FkBRbaqeXgu2Zu-QG1PgcTXq2a-HPIr5Vj4BbCuJyq0q4E_7BFJxi2vyzNn0JFUMA1PWSaPP1WnZe1CPBuaOIiOk6HuEgy-16Q0vDdEAT-F4sDyHtopTcST6LFfWJP_3AU6c5Cfna8Z9JjX75yFKrw4Q-QqAuv4ANkGDe4Z_xHO5CbHuD__XxJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fba57ac4d.mp4?token=DP3kl88fU9gievQuLldaUumNC9YN3G7DV_vI8Kn-BtgGJLan17vMs5xNMYtD2Kfc5f9m_o-YudH4Z70I6WXe0MuF1S8mt2C38_S2q8jZHjHeZlEmRppYz25WwYV4R9qpBMVOC_SNSgPdUawCWVC2clCoVf7o0n3FkBRbaqeXgu2Zu-QG1PgcTXq2a-HPIr5Vj4BbCuJyq0q4E_7BFJxi2vyzNn0JFUMA1PWSaPP1WnZe1CPBuaOIiOk6HuEgy-16Q0vDdEAT-F4sDyHtopTcST6LFfWJP_3AU6c5Cfna8Z9JjX75yFKrw4Q-QqAuv4ANkGDe4Z_xHO5CbHuD__XxJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار به ترامپ : آقای رئیس‌ جمهور، آیا این توافق شامل لغو زودهنگام بخشی از تحریم‌ های ایران میشود؟ این موضوع از چه زمانی اجرایی خواهد شد؟
ترامپ: نه، چنین چیزی در توافق وجود ندارد، این توافق بیشتر به رفتار طرف مقابل مربوط میشود
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/14982" target="_blank">📅 20:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14981">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: احتمال دارد جمعه حضور داشته باشم و با ایرانی ها دیدار کنم
از اینکه مجبور شدیم دو شب دیگر به حمله ادامه دهیم، احساس بدی داشتم. و فکر می‌کردم برای بار سوم هم همینطور، اما ما قبل از آن توافق را انجام دادیم.
فکر می‌کنم اتفاقات خیلی خوبی قرار است در خاورمیانه رخ دهد.
قیمت نفت در حال سقوط است و بازار سهام مثل موشک در حال افزایش است
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14981" target="_blank">📅 19:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ: می‌خواهم یادداشت تفاهم با ایران را منتشر کنم زیرا سندی مهم و قدرتمند است و ما به زودی آن را منتشر خواهیم کرد
تنگه هرمز پس از جمع‌آوری مین‌ها به‌طور کامل‌ بدون عوارض باز خواهد شد
کاهش تحریم‌های ایران به رفتار این کشور بستگی دارد
اکنون ما می‌خواهیم ببینیم چگونه می‌توانیم مناقشه در لبنان را حل کنیم و باید در این مورد با اسرائیل صحبت کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/14980" target="_blank">📅 19:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14979">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: توافقی که اوباما با ایران انجام داد، این کشور را قادر به ساخت سلاح هسته‌ای می‌کرد
ما خواهان روابط خوب با ایران هستیم و اگر این امر محقق نشود، به جنگ باز خواهیم گشت و امیدوارم این اتفاق نیفتد
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/14979" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14978">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: ما با ایران تفاهم‌نامه‌ای امضا کردیم و تنگه هرمز تا حدی بازگشایی شده است
تنگه هرمز روز جمعه به طور کامل باز خواهد شد
: توافق با ایران به نفع منطقه خاورمیانه خواهد بود
ایران سلاح هسته‌ای نخواهد داشت و من با این موضوع موافقت کردم. این اصل موضوع مناقشه بود
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/14978" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14977">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فوری: اولین سخنرانی مجتبی بعد از پایان جنگ و توافق با آمریکا.
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14977" target="_blank">📅 19:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14976">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a81cca2afa.mp4?token=XpaZhaXWHK5HtZ6orlcCD-DNFERFCEaZoGMWjnvEI7omGcnnznpz2i9bHIPF0LpSCgJ1Rm5_UdCRMTDpBUhXsIFeQwWCBhkbIHpMmlbLJM5iI-eQ5I720-kEVfv-NN6AVyuPYwjHYY78a8EYSxfcZBZXmluQ5YK2tpUmpKL7_Kkw9R02KRf8Yr6FGF3lYPM-HX15G2f0V0xAXZDVnbDuc2pG4-_EWy1FIOUb73SmRQfyTXVtFTMr4GarJ8uZLFRaPE5kzUQrykBUEjcabtSLuUQQnaixmDBZ3O4NRd6LGzjeF46atN1lABuTycqZfIr9e7UH-o0fVmWjT8dmjGVnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a81cca2afa.mp4?token=XpaZhaXWHK5HtZ6orlcCD-DNFERFCEaZoGMWjnvEI7omGcnnznpz2i9bHIPF0LpSCgJ1Rm5_UdCRMTDpBUhXsIFeQwWCBhkbIHpMmlbLJM5iI-eQ5I720-kEVfv-NN6AVyuPYwjHYY78a8EYSxfcZBZXmluQ5YK2tpUmpKL7_Kkw9R02KRf8Yr6FGF3lYPM-HX15G2f0V0xAXZDVnbDuc2pG4-_EWy1FIOUb73SmRQfyTXVtFTMr4GarJ8uZLFRaPE5kzUQrykBUEjcabtSLuUQQnaixmDBZ3O4NRd6LGzjeF46atN1lABuTycqZfIr9e7UH-o0fVmWjT8dmjGVnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، برای شرکت در نشست سران گروه هفت (G7) وارد شهر اویان له‌بن در فرانسه شد
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14976" target="_blank">📅 19:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14975">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDpZ3WGOCebdd9IBHEp4uk3mPh1LJwWjXwhKFGJn1T-qDFi0I4boiCl9udhIRUUo2yevubZtZOPRn_cXpy51IPHUeCrkHXeU-3uboMaq0-OW2--Uey6WHmw7F80f6eWdMkAGXdvLyFITQLPKKPcafTq7FeJOUO3YmxFOm3MM1R9hULH4W4b_P5K6IF23MK1aWODM8ss6vn6w0iYDFk4Xcy26_4jQy5_iWbtAwAX-8pnOvlY5Rt-j-6ujcshMyr1s8AljbBFgL0Mq1k-Tx3-MfaRFpLPi5K2eXTdObJhDFjk1ostH4oXxQxY9HSKOwEfIuEoVtnnw_HP_KkoxlCz5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر ماهشهر همین الان
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/14975" target="_blank">📅 19:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14974">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
به وضعیت کاملاً غیرقابل قبولی رسیده ایم که ایران در مورد آزادی عمل ما در لبنان «حق وتو» دارد و این یک واقعیت پوچ و غیرقابل قبول است.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/14974" target="_blank">📅 19:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14973">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/14973" target="_blank">📅 18:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14972">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADH6aKDt4MZDAY2b3jAMb7yxPiun7L-D9XpoEVRRZmxitciwo1OvrbiK21Zwu8BvfKRWUPFmKMI1k6Hy-4lnlm5PkT_jNXoo71LMlXKX-omsAasruLiHb2Gw-L3Ct_CDXx1FkBSv1cCBCz6fjVd32xycpzPNRiE6Kh-Vu9l1AAAoSXzgjfu4fis221ZwWUx-Ondj5UDL-h2Ee2HkyXLgNNIs7ZYXJHOW25twpp01UQ26dZdkG4BcGX4BfHMsWfMj2ceS1HxdeWMu8FBnH0Rcy4N4kGRyMWOn5GdpvDjugrC8RvFA5yJFvcOtSMs1tH2JnM2PRnF_WcyKX2zgAPAjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرجنگی عمل نکرده موشک کروز تاماهاوک در ورامین
این حمله چند شب پیش انجام شد و ده ها سایت راداری در سراسر ایران اعم از کرج و تهران و چند سایت قزوین و جنوب کشور توسط ۴۹ موشک تاماهاوک منهدم شد ( به جز یک موشک تاماهاوک )
موشک های تاماهاوک بار دیگر نشان دادند از دقت فوق العاده ای در زدن اهدافشان برخوردار هستند.
@withyashat</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/14972" target="_blank">📅 18:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14971">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نتانیاهو تا چند ساعت دیگر سخنرانی خواهد کرد و این اولین واکنش رسمی او به اعلام توافق پس از ساعت‌ها سکوت است
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/14971" target="_blank">📅 18:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14970" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/14969" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جزئیات دیگری از یک اتفاق قابل توجه درباره ساختار تفاهم اسلام‌آباد
یک منبع نزدیک به تیم مذاکرات در گفتگو با خبرنگار تسنیم، جزئیاتی از یک اتفاق قابل توجه در روز آخر مذاکرات مطرح کرد : بند 13 تفاهم‌نامه مربوط به این موضوع است که تا زمانی که برخی بندهای دیگر تفاهم‌نامه عملیاتی نشده، مذاکرات درباره توافق نهایی یعنی موضوع هسته‌ای صورت نمی‌گیرد.
وی خاطرنشان کرد: تا پیش از روز آخر مذاکرات، بند 13 شامل بندهای 4 و 5 و 10 و 11 بود؛ بند 4 مربوط به رفع محاصره دریایی، بند 5 مربوط به آغاز بازگشایی تنگه هرمز، بند 10 مربوط به اسقاطیه تحریم‌های مربوط به فروش نفت، پتروشیمی و مشتقات ایران و همچنین بند 11 مربوط به آغاز آزادسازی اموال بلوکه شده ایران است.
بنابراین بند 13 به این اشاره داشت که اگر این 4 بند گفته شده (4 و 5 و 10 و 11) انجام نشود، مذاکرات توافق نهایی آغاز نمی‌شود.
این منبع مطلع تاکید کرد: اتفاق مهمی که روز آخر مذاکرات به وقوع پیوست این بود که با پیگیری ایران، بند 1 نیز به بند 13 اضافه شد.
به گفته این منبع آگاه، معنای مهم این اتفاق آن است که اگر جنگ و هرگونه عملیات نظامی، از قبیل ترور و ... در ایران یا جبهه مقاومت از جمله لبنان اتفاق بیفتد، طبق تفاهم هیچگونه مذاکراتی برای توافق نهایی صورت نمی‌گیرد و طبیعتا اجرای تفاهم‌نامه (از جمله بازگشایی تنگه هرمز) از لحاظ ماده ۱۳ متوقف خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14968" target="_blank">📅 18:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراقچی: جمعه تفاهمنامه ایران و آمریکا امضا می‌شود
اقتصاد ما نباید خود را متکی و موکول به این قبیل توافقات اقتصادی از طریق مذاکره با آمریکا بکند
در راستای منافع کشور، نیمی دیگر از راه مانده که باید طی کنیم که نیمه سختی خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/14967" target="_blank">📅 18:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14966">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Acr4F_srQWZ97N-uZbwlS7TigaYG5i0lhFnxNmhUWc1MRk273r2d_KiYp6jDA3KtqD1bV4sv45OpLVVn7y0owSVIF5NJ9YtAUqiAfeeRuj33ZVBQY8jfLfKvJCk7bg-8WRS92wluMzRLpc778S5GZND2YRfZstwlvCvMxwa_vrXkBbFnou3DnxwXXwM3Akmn1-sIlVpiOg6r1JMEe5GcF6x_jXrZsrf4V41qppgwy0REGEUY__SqIzMZFjuP_C3gRkfktE1zLUD4ob4gr3FTg1nu5Cb-3qOyCiulwaBJJznC-nXxD7vIQ8GFSNxS_0dDlqWvgWmdcpI2oQoprBig8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث: متأسفانه، اگر افراد را از کشورهای جهان سوم وارد کنید، به سرعت خودتان تبدیل به یک کشور جهان سوم می‌شوید و هیچ کاری نمی‌توانید در این باره انجام دهید
آمریکا را دوباره بزرگ کنیم!
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14966" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ادعای جی‌دی ونس درباره ایران: ما دیروز به صورت دیجیتالی پیش توافق را امضا کردیم
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/14965" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=ld4lMRNRcu2ulgmmnfOxAwqWVvihtncy6FVl-Nu6jyTSYw-k-u9_nKqWLtNJ-xCzR2emuQjgSwyOk_k0EOGiz8ptfL1e-16o1oys8NpOG5PaesHv-CUEvODdBXbcUcmOsXGII7lYTC78b_-5Kg84faD4ELTwsNoHJfuWBCeLmxnPayoZB187-HkytOxdr792tg4E7X66z6VSib6Oqb8OZhX1m77dO-1btadJdAWmlDLDjeckNACo4gMjekz7u9GNHUh4mzE3fAnXrnAXnyoyDE22lCzFipjobZg1L2nI3W5yDTDmppUlrMuckfZ4C-DZgIF_8Omja_YG-u5FKw0o8BN3Flu5v7ZaVja7YlIIuVqkFSBNZWpHF5HNxJS5ktZhFuFp4JdYnEkurgm-We46llUXFZJR9IIB8gRt3Qpj9x4MNCyqsZsRXkqXi5RHb-TK8Nmn80WzTY4xzNVDU0SRv_n1L-LneuPsw47T3lsOYorXDA5stNaFYPRFz-ftMHyB4lSd5J0i9Prt0S6hsguOJrxNnfasaQru6Oxo6GkGbvUPP7taSKTUEW8EjAsBoDPM0toOkqPv4vM5rvAIQjO4GVbZCbclCWRFTBLyvItclDetmRIQbI4ODFEa1xtL1brHq-ltBLf1rcq3316Ft2VEuz_JG9OHSyAy6gR6fyrTeKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=ld4lMRNRcu2ulgmmnfOxAwqWVvihtncy6FVl-Nu6jyTSYw-k-u9_nKqWLtNJ-xCzR2emuQjgSwyOk_k0EOGiz8ptfL1e-16o1oys8NpOG5PaesHv-CUEvODdBXbcUcmOsXGII7lYTC78b_-5Kg84faD4ELTwsNoHJfuWBCeLmxnPayoZB187-HkytOxdr792tg4E7X66z6VSib6Oqb8OZhX1m77dO-1btadJdAWmlDLDjeckNACo4gMjekz7u9GNHUh4mzE3fAnXrnAXnyoyDE22lCzFipjobZg1L2nI3W5yDTDmppUlrMuckfZ4C-DZgIF_8Omja_YG-u5FKw0o8BN3Flu5v7ZaVja7YlIIuVqkFSBNZWpHF5HNxJS5ktZhFuFp4JdYnEkurgm-We46llUXFZJR9IIB8gRt3Qpj9x4MNCyqsZsRXkqXi5RHb-TK8Nmn80WzTY4xzNVDU0SRv_n1L-LneuPsw47T3lsOYorXDA5stNaFYPRFz-ftMHyB4lSd5J0i9Prt0S6hsguOJrxNnfasaQru6Oxo6GkGbvUPP7taSKTUEW8EjAsBoDPM0toOkqPv4vM5rvAIQjO4GVbZCbclCWRFTBLyvItclDetmRIQbI4ODFEa1xtL1brHq-ltBLf1rcq3316Ft2VEuz_JG9OHSyAy6gR6fyrTeKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: ایرانی‌ها می‌گویند قرار است به یک صندوق ۳۰۰ میلیارد دلاری برای بازسازی دسترسی داشته باشند. درست است یا نادرست؟
جی‌دی ونس: چنین چیزی می‌تواند در دسترس آن‌ها قرار بگیرد، مشروط بر اینکه به تعهدات خود در این توافق پایبند باشند.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14964" target="_blank">📅 17:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2bosxPh5PAe16wMOWAPzYEN6nmKy44h6f_cOMg4BGlLFQALmHORUcRCumKRVnc8c-sNiRPv22YB3sw2ZHNDdGTxFKBU9fqQbN-9DDSUh6r1cyC-9sJg1YiWH-GsGj6iD77wMSVuPxqX68wgSldcaAlbCYAE5J_codLn9_PPIXE9jiSzDRAPITN545XnlSCi0OMv-Sjrhq7YncOdY_2a0vHQJYjOCHEt4GltZvZoYsYoFbVDb97vQubhcH-VGnlxq4_D0_4q7UexNxhgaF0vFGdor16pdEWRI3r4cKq3N3OEsi0smASoBa1LrxSmMXkzxN8TJVL1NXPPqNcx_x33zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند.
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً ایمن، مطمئن و بکر است. مناطق دیگری برای سفر نیز وجود دارد!!!
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14963" target="_blank">📅 16:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مکرون:  پرداختن به برنامه موشک‌های بالستیک ایران در مذاکرات آینده مهم است.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14962" target="_blank">📅 16:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تسنیم: یک منبع آگاه در گفتگو با خبرگزاری تسنیم، درباره وضعیت نیروهای آمریکایی در منطقه طبق تفاهم اسلام ‌آباد گفت: بر اساس ماده 4 تفاهمنامه، 30 روز پس از توافق نهایی، نیروهای رزمی آمریکایی باید از محیط پیرامونی ایران خارج شوند.
همچنین بر اساس بند 9 تفاهمنامه، در طول 60 روز مذاکرات برای توافق نهایی، نیروی جدید آمریکا در منطقه اضافه نمی‌شود و ایران نیز در این بازه اقدام هسته‌ای انجام نمی‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14961" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مقام ارشد کاخ سفید به آکسیوس:
هیچ دارایی مسدود شده ایران پس از امضای یادداشت تفاهم نامه در روز جمعه میان ایران و آمریکا آزاد نخواهد شد، همچنین هیچ کاهش تحریمی نیز برای ایران اعمال نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14960" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ونس درباره توافق: جزئیات زیادی هنوز برای حل شدن باقی مانده است!
انتظار می‌رود طیف کاملی از نمایندگان ایران در مراسم امضای روز جمعه حضور داشته باشند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14959" target="_blank">📅 16:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بقائی: ایران و عمان امنیت تردد در تنگه هرمز را تأمین می‌کنند هزینه‌های خدمات ناوبری و بیمه کشتی‌ها طراحی و دریافت می‌شود
مذاکرات هسته‌ای و رفع تحریم‌ها ظرف ۶۰ روز آغاز می‌شود
به اسرائیل اصلاً اعتمادی نیست همون‌طور که به آمریکا هم اعتماد نداریم تجربه هم نشون داده اینها در عمل به تعهداتشان هیچ‌وقت صداقت نداشتند
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14958" target="_blank">📅 16:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صدا و سیما: تنگه هرمز تا اطلاع ثانوی بسته است و بیش از ۹۶ ساعت است نیروی دریایی سپاه اجازه عبور هیچ شناوری را نداده است
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14957" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14956" target="_blank">📅 14:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253e5fb18.mp4?token=Oy1NYHwhf2qJ0CBammSbnI-BjLeDtQINZdzfPOSMxfNfmix1UnOS2uZQAqQyToBewP0NVK6LaiHnnFFsxSB2Im3AJI2rj_v0yj1HDoevEbyGqqoYPSiLguD6QFCqfG1SMO5SCwhcQXjQ7eTRGpXo3sSbwFKmsZ-ANklyjWy1XwiH1L_8piXvF757bYNIjPO3_CLk9cwjgTDyHnLZ5I20VUKM0sSoYJ1XNH9uwKgn86GAAyDRO7qsX58I2iM4dMVThGREWTjGLGSzHhbB4xrYhP8oymz629t0RHIcC9z3M2jMBxxErStWWWZZGFRfeQ7Gs6rW4DjVOXsEyBJu_pMuUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253e5fb18.mp4?token=Oy1NYHwhf2qJ0CBammSbnI-BjLeDtQINZdzfPOSMxfNfmix1UnOS2uZQAqQyToBewP0NVK6LaiHnnFFsxSB2Im3AJI2rj_v0yj1HDoevEbyGqqoYPSiLguD6QFCqfG1SMO5SCwhcQXjQ7eTRGpXo3sSbwFKmsZ-ANklyjWy1XwiH1L_8piXvF757bYNIjPO3_CLk9cwjgTDyHnLZ5I20VUKM0sSoYJ1XNH9uwKgn86GAAyDRO7qsX58I2iM4dMVThGREWTjGLGSzHhbB4xrYhP8oymz629t0RHIcC9z3M2jMBxxErStWWWZZGFRfeQ7Gs6rW4DjVOXsEyBJu_pMuUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای شرکت تو اجلاس گروه ۷ به فرانسه پرواز کرد
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14955" target="_blank">📅 14:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">والانیوز عبری: تاکنون هیچ درخواستی از جانب امریکا برای خروج اسرائیل از لبنان وجود ندارد!
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14954" target="_blank">📅 13:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرگزاری واس: شاهزاده فیصل بن فرحان، شاهزاده سعودی در گفت‌وگو با عراقچی اعلام کرد سعودی از توافق برای پایان دادن به عملیات نظامی استقبال می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14953" target="_blank">📅 13:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f0a7cffc.mp4?token=m9HsVOGl1t848e35wuhgBA1411CjASqRasALGdxBR8cRQDCu8uU65MlQgALti4J0EmsDw-kiZ_FrlYdwOJuz2tam-u2UKEot8TQF57fND0i-Nex0weJ7MrcJHu6DWHiy0vZWAWJlcyHcA5O4nB3ne11uPbIFq37zB4L-CxjCFF-YXSb3sMFabJb47nwuhbp32e0kK2yM3gV88V-W7D37mBlLM5wGYXnGRv4_hbSF10N9Jl2DwkQCx7tJUZRrqC3kJ6yraoYOE0dYZyHtSylIAplhYB_024K5fbvd5UeyjRdzOeg5znVWN2BpreqrQKR4q_vRuRLEF2b5Pql3eU18wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f0a7cffc.mp4?token=m9HsVOGl1t848e35wuhgBA1411CjASqRasALGdxBR8cRQDCu8uU65MlQgALti4J0EmsDw-kiZ_FrlYdwOJuz2tam-u2UKEot8TQF57fND0i-Nex0weJ7MrcJHu6DWHiy0vZWAWJlcyHcA5O4nB3ne11uPbIFq37zB4L-CxjCFF-YXSb3sMFabJb47nwuhbp32e0kK2yM3gV88V-W7D37mBlLM5wGYXnGRv4_hbSF10N9Jl2DwkQCx7tJUZRrqC3kJ6yraoYOE0dYZyHtSylIAplhYB_024K5fbvd5UeyjRdzOeg5znVWN2BpreqrQKR4q_vRuRLEF2b5Pql3eU18wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون امام علی نزدیک خیابون دماوند
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14952" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تتر ۱۶۳.۵۰۰ تومان
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14951" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14950">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کانال ۱۲ اسرائیل: حدود ۱۰ ساعت از اعلام توافق بین واشنگتن و تهران می‌گذرد اما نتانیاهو هنوز در سکوت به سر می برد
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14950" target="_blank">📅 11:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14949">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نشست سران گروه هفت (G7) امروز در شهر اویان-له-بن فرانسه برگزار می‌شود؛ جایی که رهبران کشورهای صنعتی جهان درباره‌ی مجموعه‌ای از بحران‌های جهانی گفت‌وگو خواهند کرد.
گروه G7 یک گروه متشکل از هفت اقتصاد بزرگ جهان شامل آمریکا، بریتانیا، کانادا، فرانسه، آلمان، ایتالیا و ژاپن است که از دهه‌ی ۱۹۷۰ و پس از بحران نفتی اوپک شکل گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14949" target="_blank">📅 11:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایران فعلا در تنگه هرمز پولی دریافت نخواهد کرد
ایسنا: براساس جزئیات تفاهم‌نامه، ایران تنگه هرمز را مدیریت خواهد کرد و عوارض را «در تاریخ بعدی» دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14948" target="_blank">📅 11:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">️ترامپ به نیویورک تایمز:
«کنار آمدن با نتانیاهو فوق‌العاده دشوار است و او باید از ما بسیار سپاسگزار باشد، زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل وجود نداشت.»
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14947" target="_blank">📅 11:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر دفاع اسرائیل: همراه با نتانیاهو سیاستی روشن را دنبال میکنم که بر اساس آن، ارتش در مناطق امنیتی در لبنان، سوریه و غزه باقی خواهد ماند
با وجود تمام فشارهای فعلی و آینده، خروج ارتش اسرائیل از لبنان را نمیپذیریم
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14946" target="_blank">📅 10:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=eOQeyDnyBZQihfbFGfxIVaDwlbsHxUCp9m-eXT7Buvaz7WcMLrTg8KX3tmR3S28rKeBkWVx-5N_2LjHZNkjxcL8pznnajNOkgl9k7OCDaM2FR_jsH8lwvXN3xZqcvF4aQZk-Rsmy9t4rnpJHLrUjES9NILs13Gfiys-H4jhWlXxtoNJc0zfeMiSqQV01ofluFlqXBnm5H1IAxxFtXIRC7Rd_Do1EUjcl_B4ycDxafqaVdeha2BqDOc6OGkJXxBMTivJJFZFWxgJpSle_tsgBONwz53kO28uD8NJqI4XrQKF_dyx8lznG1pemwQawk_fxE3uFB2MfCrdqtzyMR_jNQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=eOQeyDnyBZQihfbFGfxIVaDwlbsHxUCp9m-eXT7Buvaz7WcMLrTg8KX3tmR3S28rKeBkWVx-5N_2LjHZNkjxcL8pznnajNOkgl9k7OCDaM2FR_jsH8lwvXN3xZqcvF4aQZk-Rsmy9t4rnpJHLrUjES9NILs13Gfiys-H4jhWlXxtoNJc0zfeMiSqQV01ofluFlqXBnm5H1IAxxFtXIRC7Rd_Do1EUjcl_B4ycDxafqaVdeha2BqDOc6OGkJXxBMTivJJFZFWxgJpSle_tsgBONwz53kO28uD8NJqI4XrQKF_dyx8lznG1pemwQawk_fxE3uFB2MfCrdqtzyMR_jNQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین شناوری که پس از اعلام توافق صلح میان ایالات متحده و جمهوری اسلامی ایران از تنگه هرمز عبور کرد، نفتکش گاز طبیعی مایع (LNG) با پرچم مالت به نام “دیشا” (Disha) است که از طرح تفکیک ترافیک دریایی ایران استفاده کرد
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14945" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حمله اسرائیل به الخیام جنوب لبنان!
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14944" target="_blank">📅 10:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14943">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کانال ۱۳ اسرائیل به‌نقل از یه مقام ارشد:
توافقی که داره صورت میگیره فاجعه‌بارترین توافق تاریخه. از نخست وزیر گرفته تا رئیس ستاد ارتش کل غیر از این فکر نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14943" target="_blank">📅 10:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14942">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reRomA4-qgSaA0JPhFQC7yfKwKyp5A7zAEY_lbJc0-ZK489KelScZbgHZuYpD_3q8pXNY3z7IPdVa0yo8-hvPraYkd9n56QoO1jCyCFPQRPsqIYrq7th-sXY-2RXCL475-PsAaXRJqRm0EFAUIFcYHPsXR9z6akpEOy_OcSJtfVbmrUKfxzyFhFxzKWjaVfXTsNdsg9yBc0rYLhKQq1OI8j7f-Y_XbPZG70cJmYfOBKuEqWM8jqktvrHsDel1qhUtAg3AjYRWS59qzF2hqcX7n3-TB-K1yT2gU6cSlFA0RX8AfjZge0b9C6AoBmvAVofG5KGqyamyJ64uXvwRUK0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق خوب، توافقی است که هیچ یک از طرفین راضی نباشند
-کتاب قدرت مذاکره جلد سوم صفحه ۲۳۶
یه توافقی بستم که هم ایران ناراضیه هم ملت ناراضی هستن هم براندازا ناراضی هستن هم آمریکا ناراضیه هم اسراییل ناراضیه
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/14942" target="_blank">📅 03:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14941">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نیویورک تایمز: تهران نهایی کردن توافق را تا بعد از نیمه‌شب به وقت محلی به تعویق انداخت تا از همزمانی این لحظه تاریخی با تولد رئیس‌جمهور ترامپ در روز یکشنبه جلوگیری کند
اختلاف زمانی هفت و نیم ساعته به هر دو کشور ایران و آمریکا اجازه داد تا جدول زمانی مورد نظر خود را حفظ کنند، به طوری که ترامپ گفت توافق در روز یکشنبه نهایی شده در حالی که مقامات ایرانی تأکید داشتند که این توافق در روز بعد به پایان رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/14941" target="_blank">📅 03:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14940">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ به نیویورک تایمز: نتانیاهو فرد بسیار نمک نشناسی است. او باید به شدت از ما بابت انجام این کار سپاسگزار باشد.
زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/14940" target="_blank">📅 03:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14939">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پرزیدنت ترامپ به نیویورک تایمز گفت که در صورت شکست مذاکرات برای دستیابی به توافق هسته ای نهایی، حملات نظامی خود را علیه ایران از سر خواهد گرفت.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/14939" target="_blank">📅 02:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14938" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">@withyashar
khatme kalam</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14937" target="_blank">📅 02:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14936" target="_blank">📅 02:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نیویورک تایمز
:  محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14935" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14934" target="_blank">📅 02:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14933" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14932" target="_blank">📅 02:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14931">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14931" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
