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
<img src="https://cdn4.telesco.pe/file/b1otcCp1sULTBo2-csJQRVs_GMm3wWBWqbddtmCZsf9fKA3byITnSqeNaqSt_dVSqe3dw4_d3uEVueh1EJVI_dlDySM_hLuFxnT7V-HCpF6gvYKIDcO_3en9w2Sr1fcuLHAk07NcaoEEMfBFfQX5B-XovXrBDx-19V3SeMUYQGf0uD3ZXVzYo8Hpk1nRIXRluUiiA2Jlf_UTFsLj24qdsGfQtDZZTGFD_6QFAPkN9yzkEAuoT77K5cciUupzqFdC81Wqub7s_rcM-Ym_i2wn1hz9TLDWmmP_agEVIbk7RubWB5kmLurv8pWxMoFeqN_TdBucgczYnzMgtxYWHpD-EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 263K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 00:42:31</div>
<hr>

<div class="tg-post" id="msg-11521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ به کانال ۱۳ اسرائیل:
فکر می‌کنم ایرانی‌ها باید از اون اتفاقی که الان در حال رخ دادنه بترسن.
@withyashar</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/withyashar/11521" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هم اکنون گزارش CNN:
ترامپ تیم امنیت ملی ارشد خود را برای بحث در مورد ایران فراخواند
@withyashar</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/withyashar/11520" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پست ترامپ از تیر اندازی  به پرچم در تلویزیون ایران فیک است !( این کار  انجام شده ولی ترامپ چنین پستی منتشر نکرده ! اکانت فیک ترامپ در X منشع این خبر است</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/withyashar/11519" target="_blank">📅 00:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339423bcdd.mp4?token=MNqvyYaIjuw7diJR1HGGr0ZNek85InQ1pXxqj5GTya_P9YLSCGtyJ9PZ7oy-zk6QCNJAQ_ZnS1gQ3hSUD8ibKRfHDnw9OWlitkVQFsLW11S5-CrbQ5irQU9qHZxKDPZQ6Rf3xZLaBqZ4W_VIxlm0pZU2_rbpjd-FTrd2MbpYGF_JiwDBhM0BeZ7yLYI2_RkpPH3XpqwAo5VGd1ra73q_bK8_SFkaIFCotM5iW6fLHbUaE3rggv4z9OvtvDIMumD57DAwmdp-RQ45BESCIutOM-5IrcQPDJaQ1sB_ktHT6w4KxQwYMXyabOaBcN-UthkNytuRuzK_rfdSiSY6d-xtzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339423bcdd.mp4?token=MNqvyYaIjuw7diJR1HGGr0ZNek85InQ1pXxqj5GTya_P9YLSCGtyJ9PZ7oy-zk6QCNJAQ_ZnS1gQ3hSUD8ibKRfHDnw9OWlitkVQFsLW11S5-CrbQ5irQU9qHZxKDPZQ6Rf3xZLaBqZ4W_VIxlm0pZU2_rbpjd-FTrd2MbpYGF_JiwDBhM0BeZ7yLYI2_RkpPH3XpqwAo5VGd1ra73q_bK8_SFkaIFCotM5iW6fLHbUaE3rggv4z9OvtvDIMumD57DAwmdp-RQ45BESCIutOM-5IrcQPDJaQ1sB_ktHT6w4KxQwYMXyabOaBcN-UthkNytuRuzK_rfdSiSY6d-xtzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
دلیل توقف پروژه آزادی به درخواست پاکستان بود. پاکستانی‌ها گفتند: «اگر شما پروژه آزادی را متوقف کنید، فکر می‌کنیم می‌توانیم به توافق برسیم.»
ما پیش رفتیم و موافقت کردیم که آن را متوقف کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/11518" target="_blank">📅 00:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ادعای فارس
: ترامپ با آزادسازی دارایی‌های بلوکه شده مخالفت کرد!
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/11517" target="_blank">📅 23:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صدای پدافند در اهواز
@withyashar</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/withyashar/11516" target="_blank">📅 23:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاخ سفید: ترامپ و رئیس جمهور چین به توافق رسیدند که ایران نباید به سلاح هسته‌ای دست یابد و توافق کردند هیچ کشوری نباید برای تنگه هرمز عوارض دریافت کند
@withyashar</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/11515" target="_blank">📅 23:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اکانت رسمی اسرائیل به فارسی: شایدم اصلا چیزی ( جنازه خامنه ای) برای دفن کردن باقی نمونده...
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/11514" target="_blank">📅 22:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f212f792.mp4?token=CuHbveCkVA_sd5TGkLvLiKAXWgnWd4EHK3lwkU4abSo97AeiqbnngEIJ6pRQdHnh8FlQqgyPhEmktTwhs-NCpKqz06UqeqBUPwRwogNry1NIRIyYk8-jUweLCSeteqJHnenZhXlY9mf7gDm6TDUAG-SKuxQQHeG7iD1rXewkHLWijYCmuvYtIVu9kV6Ba_ZP6HboQ0vRpqOjyb4LKnVBJ_feRCMesNDuIObkvhCBY2e7mqDdY8HC4qNLBnNmh_ViVH0UdphQfAQWWoG9A6d_KpygJiofz7ch4U_HekCREF9eH0Ul4lcSasBkYtwUD5dyI77SfZK6Q16t7TMVd70A1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f212f792.mp4?token=CuHbveCkVA_sd5TGkLvLiKAXWgnWd4EHK3lwkU4abSo97AeiqbnngEIJ6pRQdHnh8FlQqgyPhEmktTwhs-NCpKqz06UqeqBUPwRwogNry1NIRIyYk8-jUweLCSeteqJHnenZhXlY9mf7gDm6TDUAG-SKuxQQHeG7iD1rXewkHLWijYCmuvYtIVu9kV6Ba_ZP6HboQ0vRpqOjyb4LKnVBJ_feRCMesNDuIObkvhCBY2e7mqDdY8HC4qNLBnNmh_ViVH0UdphQfAQWWoG9A6d_KpygJiofz7ch4U_HekCREF9eH0Ul4lcSasBkYtwUD5dyI77SfZK6Q16t7TMVd70A1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11513" target="_blank">📅 21:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ: ما می‌خواهیم توافق کنیم. آن‌ها جایی که ما می‌خواهیم نیستند؛ باید به آن نقطه برسند، وگرنه ضربه سختی خواهند خورد، و آنها این را نمی‌خواهند
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11511" target="_blank">📅 21:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11510" target="_blank">📅 21:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یاشار فک میکنم عرزشی ها هم منبع معتبر خبریشون تویی
😂
با این حجم ری اکشن هاشون</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11509" target="_blank">📅 21:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoo</strong></div>
<div class="tg-text">یاشار فک میکنم عرزشی ها هم منبع معتبر خبریشون تویی
😂
با این حجم ری اکشن هاشون</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/11508" target="_blank">📅 21:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رسانه‌های اسرائیلی به نقل از منابعی گزارش دادند حملات به ایران پس از چراغ سبز ترامپ به‌صورت مشترک با آمریکا انجام خواهد شد و بانک اهداف در ایران شامل زیرساخت‌های انرژی است.
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/11507" target="_blank">📅 21:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی:
انتظار میره ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کنه تا گزینه‌های اقدام نظامی علیه ایران رو بررسی کنه.
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11506" target="_blank">📅 21:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ:  زمان برای ایران در حال اتمام است   بهتر است خیلی سریع اقدام کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. وقت بسیار حیاتی است!  @withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11505" target="_blank">📅 21:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11503">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8925f5731b.mp4?token=SWatEbOJSY2bBZ0DTa8zXtLUZTPDvr79MLXTKwlLBmJn_g8tIo9RLdF9x83a4EEop-8Xx7sab1nsSjo7mk7dtgi1nmOc9fwlEEtfGh5888-0wTgAB7AgkmCxjZK9pmGnTBZ_bqa-lD4bxryo_FdKsJP3rg_Lj8-k54IaKPTXPfg64qXQtMqN4BF3B13Pzu-CvphMsD3N6DQKQA6t_HBswvawxur-_6Tuzh6TuzRxDAJQlOvTOr5pgT-s7lSWWYS-Z9SQ1xpSpEpQJDQHIsG__07izYPVIYByUvXUj3MGUYBntVRcokTdFo_OGj2UJesXZ8mHHJpb7y2_FIN7gN7g4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8925f5731b.mp4?token=SWatEbOJSY2bBZ0DTa8zXtLUZTPDvr79MLXTKwlLBmJn_g8tIo9RLdF9x83a4EEop-8Xx7sab1nsSjo7mk7dtgi1nmOc9fwlEEtfGh5888-0wTgAB7AgkmCxjZK9pmGnTBZ_bqa-lD4bxryo_FdKsJP3rg_Lj8-k54IaKPTXPfg64qXQtMqN4BF3B13Pzu-CvphMsD3N6DQKQA6t_HBswvawxur-_6Tuzh6TuzRxDAJQlOvTOr5pgT-s7lSWWYS-Z9SQ1xpSpEpQJDQHIsG__07izYPVIYByUvXUj3MGUYBntVRcokTdFo_OGj2UJesXZ8mHHJpb7y2_FIN7gN7g4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعر امشب
😬
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/11503" target="_blank">📅 20:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مقامات آمریکایی به اکسیوس گفتند:
مذاکرات با ایران به بن‌بست رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/withyashar/11502" target="_blank">📅 20:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
ما منتظر یه پیشنهاد دیگه از طرف ایران هستیم؛ اگه این کار رو نکنن، با شدتی بی‌سابقه هدف حمله قرار میگیرن.
@withyashar</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/11501" target="_blank">📅 20:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/11500" target="_blank">📅 20:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گوگوش در پیامی در اینستاگرام اعلام کرد مدال افتخار سال 2026 «جزیره الیس» را دریافت کرده و این جایزه را با «عشق و احترام» به مردم ایران تقدیم می‌کند. @withyashar</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/11499" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گوگوش در پیامی در اینستاگرام اعلام کرد مدال افتخار سال 2026 «جزیره الیس» را دریافت کرده و این جایزه را با «عشق و احترام» به مردم ایران تقدیم می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/11498" target="_blank">📅 20:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:  زمان برای ایران در حال اتمام است   بهتر است خیلی سریع اقدام کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. وقت بسیار حیاتی است!  @withyashar</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/11497" target="_blank">📅 20:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/es3cbmM37iBvxhCwMxGq-KDxutzK6Z0CZOH8J7nE5IlmiqKajHZzTUEP8qJxV2ASB62dUm_gxJQFynhjsNP6togJdisLhdMFWN4EN6mnHRyOJq4bpBUQ0b5a8i2DNUpLeJ-tolUZ8otw6PzJoM4T33Qm3Xjo09GVGz8JYAfkdhn6PFHddiRH_W1iD00W1eCyI5aNZk_ie6JZ6wgCuQpf4I3_9ah7RnxtYYIN0MqpUWW6jooM5G7JeLa-yAoufrxCpt5o-qppyEtOX0mcyIKcohc7UIRFWH9E2Vv1_JgdSutb6LTru0bU8Phmc4dF_m4gnoMF9IhIfaQnqKv73Szozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  زمان برای ایران در حال اتمام است
بهتر است خیلی سریع اقدام کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند.
وقت بسیار حیاتی است!
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11496" target="_blank">📅 20:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c29a07582.webm?token=FgxDmoroBdaLCikvMFtZReiI3lcsSWaiJ14xvdCJg9qBll_wVdVzvqBmFS1Bk-TTyahWIdzL3DF10mXb8Y6JmdqHd4ga3f4ULDjhNhR7aWvq7j4pmzGOYnKTNTmrH10U6DDqBCXKuLofN_8rP1VuUdrkWCSgYWgEw_eUXA2_4A4gDhfCQ88atpngJN8NuBgvqf6eWmX27rPIvbFIaAb5fO98PQdrjwEmi9B8LAz4CkNGYb4wvNdPWsywMgsSZ16IiiCVUZfz-95W7JpzxJKiPTJuYJlvBW73lLlqKcUpfNeuUjYgljJBTSAL8RhJUa6uTqh2sId8aW0aaeJCCy6x5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c29a07582.webm?token=FgxDmoroBdaLCikvMFtZReiI3lcsSWaiJ14xvdCJg9qBll_wVdVzvqBmFS1Bk-TTyahWIdzL3DF10mXb8Y6JmdqHd4ga3f4ULDjhNhR7aWvq7j4pmzGOYnKTNTmrH10U6DDqBCXKuLofN_8rP1VuUdrkWCSgYWgEw_eUXA2_4A4gDhfCQ88atpngJN8NuBgvqf6eWmX27rPIvbFIaAb5fO98PQdrjwEmi9B8LAz4CkNGYb4wvNdPWsywMgsSZ16IiiCVUZfz-95W7JpzxJKiPTJuYJlvBW73lLlqKcUpfNeuUjYgljJBTSAL8RhJUa6uTqh2sId8aW0aaeJCCy6x5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11495" target="_blank">📅 20:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اتحاد باید شکل بگیره ! حتی بچه هیئتی ! تغییر رژیم شکل میگیره ولی تغییر عقیده کار یک شبه نیست و باید هر دو سمت شل کنند ! من خودم کافرم ولی تیم باید تکمیل باشه ! آس پیک شخص شاهزاده رضا پهلوی تنها هستش ! ترامپم مارو میره قاهره شک نکنید !</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/withyashar/11494" target="_blank">📅 20:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محمد پروین دوست خوبمه امیدوارم با تغییر جهت به سمت مردم برگردند</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/11493" target="_blank">📅 20:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72df07c21c.webm?token=sqJplB3ulBqg-5d8SU7T9vsM16vg6FeuG8uXAmMtC39nrtWpKOe6jXFA-pp98vVIrOc5vOvnAfqewaCdFv3mxVhOOWv96jjByYfOndxTaJv4hdscuVZjeI9lL23lLXorGG9iwDAn5NxlSWr9A-qhwCkia-fom2-wzPWBxtOCck7SYhgN70X2u9f_RtGT2GAdgQ8yfTApvQqEWjWoDC3sRRIgEAvNRFiD78D3zjMWej8hChWCMVSuQp-6qnCTF5d-WuhSf8bg7vhb4ToaW5mlwi-TzqYocvuteLc14rGwgPMVuZ7DT6Dnrcu-TZ7Sb2ZXnFe09_vI_NpXuP2CRYakgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72df07c21c.webm?token=sqJplB3ulBqg-5d8SU7T9vsM16vg6FeuG8uXAmMtC39nrtWpKOe6jXFA-pp98vVIrOc5vOvnAfqewaCdFv3mxVhOOWv96jjByYfOndxTaJv4hdscuVZjeI9lL23lLXorGG9iwDAn5NxlSWr9A-qhwCkia-fom2-wzPWBxtOCck7SYhgN70X2u9f_RtGT2GAdgQ8yfTApvQqEWjWoDC3sRRIgEAvNRFiD78D3zjMWej8hChWCMVSuQp-6qnCTF5d-WuhSf8bg7vhb4ToaW5mlwi-TzqYocvuteLc14rGwgPMVuZ7DT6Dnrcu-TZ7Sb2ZXnFe09_vI_NpXuP2CRYakgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی پروین در بیمارستان بستری شد  علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.  پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/11492" target="_blank">📅 20:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">علی پروین در بیمارستان بستری شد
علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.
پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده از بیمارستان مرخص می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/11491" target="_blank">📅 20:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شبکه عبری کان: نتانیاهو و ترامپ، بیش از نیم ساعت با یکدیگر تلفنی گفت‌وگو کردند و در مورد امکان از سرگیری درگیری‌ها در ایران و همچنین سفر ترامپ به چین بحث و تبادل نظر نمودند
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11490" target="_blank">📅 19:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝕭.𝕽</strong></div>
<div class="tg-text">کلاه شیر و خورشیدمو الان باد برد تو آب های خلیج فارس…
🥹
❤️‍🩹</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/withyashar/11489" target="_blank">📅 19:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11488">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWsC3t1yhAqe6iMznKxtm-kKjAHG60gZkxIkFGQUonRKhdHYUOJ0Zl4KYu6IlVB47XKLN8mUVRLFeR79sdnvBWGGQzLRbxNo9GGXjVZvPJUt3C4hlUxYhmyVmvUq4LsZgZrelRbSQI60acb5PL-TScT4Dwwgb8PFWF8B0TZD0ZYx8M8ztJtZgJSP9WA3V6bztj44XVdDPlOeQe8lA71ylm9_ObyW8YI5iD4yovjXNKAiUATuzHp10umMMwVLjVIbdqnkC5LSoypoZOK_pRh36GD4wEhdSDTDt1xLiVPQbzKxrZY2vESPW7S3fcPs0Iyysa0OiPPKKOUjoqxysFNkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاه شیر و خورشیدمو الان باد برد تو آب های خلیج فارس…
🥹
❤️‍🩹</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/11488" target="_blank">📅 19:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11487">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زیرنویس شبکه العربیه:
قرارگاه خاتم الانبیا به یگان های موشکی اعلام آماده باش فوق العاده صادر کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/11487" target="_blank">📅 19:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زیرنویس
شبکه خبر: هشدار درباره عملیات غیرموجه علیه کشورهای منطقه و انتساب آن به ایران
یک مقام آگاه نظامی: ایران همه کشورهای منطقه را از افتادن در این دام رژیم صهیونیستی برحذر می‌دارد.
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11486" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سناتور لیندسی گراهام در مورد ایران:
طبق تحلیل من، هیچ نشانه‌ای وجود ندارد که افراد مسئول فعلی با گذشته تفاوتی داشته باشند - آنها هنوز می‌خواهند جهان را به وحشت بیندازند، اسرائیل را نابود کنند و به دنبال ما بیایند.
بنابراین شما آنها را بیشتر تضعیف می‌کنید. کاری که رئیس جمهور ترامپ انجام داده از نظر نظامی شگفت‌انگیز بوده است. زیرساخت‌های انرژی، نقطه ضعف آنهاست. برگردیم به بحث جنگ، من انرژی را در صدر فهرست قرار می‌دهم.
من خواستار آسیب رساندن به این رژیم هستم. بیشتر به آنها آسیب بزنید، شاید آنها به توافق برسند. اما در حال حاضر فکر می‌کنم آنها سعی می‌کنند منتظر بمانند و بازی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/11485" target="_blank">📅 18:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کیهان لندن : آماده باشید که احتمالا آمریکا و اسرائیل به زودی حمله می‌کنن
@withyashat</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11484" target="_blank">📅 18:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حریق در یک ساختمان تجاری در خیابان جمهوری تهران
سخنگوی سازمان آتش‌نشان:
ساعت ۱۷:۱۴ دقیقه یک مورد حادثه آتش سوزی در یک ساختمان تجاری به آدرس خیابان جمهوری بعد از خیابان شیخ هادی به سامانه ۱۲۵ اعلام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11483" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mehmooni (iG @yashar)</div>
  <div class="tg-doc-extra">Amir Tataloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/11482" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/11482" target="_blank">📅 18:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd18535cb9.mp4?token=RlmY1yipUYtQD7U4Ygoppo6STOW5GSNWajTw90Zn4PXCsyTOEaA1fltxvFxR-Z_2XWggdbTsMpDxmz4VvWM3RqxyapC5AIh8IxClGri_K7_VHJ3vLW8lUTKx79M85BK4NgeizuXHyQME5mcFrjBIZ_wzTr10b98a4y7Owb0ZFwjje69DOWrZEPifhtvw_mF_k0DVyTUrmCNjABE3quP3SysuqJSckvVbdySu-2ghMPAfudceh1fhguGTI_OZHogoFbOi0FFGUAV5C3zGUICVVNUFW003HIpEyLzRBYzTlEsIILAOQzpxlNGVwNLIPXx-qxrVqLJkMf0t47WH2dR5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd18535cb9.mp4?token=RlmY1yipUYtQD7U4Ygoppo6STOW5GSNWajTw90Zn4PXCsyTOEaA1fltxvFxR-Z_2XWggdbTsMpDxmz4VvWM3RqxyapC5AIh8IxClGri_K7_VHJ3vLW8lUTKx79M85BK4NgeizuXHyQME5mcFrjBIZ_wzTr10b98a4y7Owb0ZFwjje69DOWrZEPifhtvw_mF_k0DVyTUrmCNjABE3quP3SysuqJSckvVbdySu-2ghMPAfudceh1fhguGTI_OZHogoFbOi0FFGUAV5C3zGUICVVNUFW003HIpEyLzRBYzTlEsIILAOQzpxlNGVwNLIPXx-qxrVqLJkMf0t47WH2dR5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11481" target="_blank">📅 18:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نمیدونم چطوری اطلاعات بدردبخور رو‌انتقال بدم  نمیدونم اجازه میدی به وقتش واسه خودت بفرستم و تو یه کاری بکنی؟</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11480" target="_blank">📅 17:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA i</strong></div>
<div class="tg-text">نمیدونم چطوری اطلاعات بدردبخور رو‌انتقال بدم
نمیدونم اجازه میدی به وقتش واسه خودت بفرستم و تو یه کاری بکنی؟</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11479" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شاهزاده رضا پهلوی : جمهوری اسلامی را نمی‌توان تغییر داد همانگونه که یک گرگ را نمیتوان تبدیل به میش کرد
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11478" target="_blank">📅 15:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9e1343f7.mp4?token=CX3gfTylUMTdQmrcgL-ZX7149OTNiIra5G0KpMqjKI8r2a1htn-1I4KPnB3jqBF8whZbTSIVbGszCv2-61tZUzXqQhKeK0Xg4KTQGtdMUi3MqiFqoQA6bU_epwMNCuWS8ZCkMSpK66YmL2Vd4l4W0qftIKksJBoXNY7E-PPWQemgoHUNtDaGxZzi8bnHtuO_WBTU5bRyEioHLdQGC1gX_G3oROWHxhu3bTbAtdzxsLkTaWi75vBhWC488ooanq_S4WFCboBwYTvBakzeKy2MZZ9L9Ztt0bNFNGuG2-YCzZC4Q61Ch3M8twh3kYHsb1urTCbt9tE2j3umfZjKdSDvWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9e1343f7.mp4?token=CX3gfTylUMTdQmrcgL-ZX7149OTNiIra5G0KpMqjKI8r2a1htn-1I4KPnB3jqBF8whZbTSIVbGszCv2-61tZUzXqQhKeK0Xg4KTQGtdMUi3MqiFqoQA6bU_epwMNCuWS8ZCkMSpK66YmL2Vd4l4W0qftIKksJBoXNY7E-PPWQemgoHUNtDaGxZzi8bnHtuO_WBTU5bRyEioHLdQGC1gX_G3oROWHxhu3bTbAtdzxsLkTaWi75vBhWC488ooanq_S4WFCboBwYTvBakzeKy2MZZ9L9Ztt0bNFNGuG2-YCzZC4Q61Ch3M8twh3kYHsb1urTCbt9tE2j3umfZjKdSDvWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما:   با اعلام مدیر کل آموزش و پرورش تهران؛ دانش آموزان پایه های هفتم تا دهم دیگه امتحان خرداد ندارن و با توجه به عملکرد علمی یکساله سنجیده میشن.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/11477" target="_blank">📅 15:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک‌تایمز:  آمریکا به عراق دستور داده بود که طی دو عملیات داخل ایران، سیستم‌های راداری خود را خاموش کند و عراق این کار را انجام داد
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/11476" target="_blank">📅 15:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو: امروز با رئیس‌جمهور ترامپ حرف میزنم،چشممون روی ایران بازه، برای هر موقعیتی آماده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11475" target="_blank">📅 15:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFpyYxYfNgx5Ea81epOvADl3EKzFKiJgM0N8P1rZeop4H-IRfbBa_8oav7XmhRDhMj1hmEIPs8BwSVi2M847oj_0xCrCApHi40n3ZhGviyRrFPxeJ8bmVbXsTmESN1qMTpU_n9XYXtzoYeibaJqlQ3NBpTgLYFXKyaCrDUxVVvHsjvjWhNgLLq1BpcXZu_JKHqMWI1FZlAwybRyg4VsDbOcAdW09gHhdB3ZzWWq3dEgW_i9Y3IcIBlWl3y1cAD-5P1R285H8tdLkW0pFfJZXxvu3a6mIqB2BdknqrqBPhADqJOlsCJypL6tqQD6iXbU4Gp7_1t0l__vzoii3EQ30Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: یه کشتی اسرائیلی تو خلیج فارس توقیف کردیم که خدمه‌ش عکس علی خامنه‌ای و مجتبی خامنه‌ای رو روی دیواراش نصب کرده بودن.
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/11474" target="_blank">📅 15:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11473">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو: ما در غزه اکنون چیزی را در اختیار داریم، دیگر ۵۰٪ نیست... اکنون ۶۰٪ است. این وضعیت امروز است.
ماموریت ما یکی است: اطمینان حاصل کنیم که غزه دیگر تهدیدی برای اسرائیل نخواهد بود.
ما محدودیت بودجه نداریم. هر چقدر هزینه داشته باشد مهم نیست، شک ندارم که اسرائیل اولین کشوری خواهد بود که راه‌حلی کامل برای حملات پهپادی ارائه می‌دهد
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/11473" target="_blank">📅 14:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11472">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو با ترامپ تلفنی گفتگو می‌کند
رسانه‌های عبری: نتانیاهو امروز با توجه به تحولات و تنش‌های منطقه با ترامپ صحبت خواهد کرد.
@withyashar
امروز همچنین اسرائیل جلسه امنیتی برگزار میکند</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/11472" target="_blank">📅 14:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تایمز:  انگلیس برای جنگ آماده می‌شود
این رسانه انگلیسی از افزایش بودجه دفاعی انگلیس خبر داد و هدف از آن را آماده شدن برای جنگ های آینده اعلام کرد
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/11471" target="_blank">📅 14:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مشاور سابق پنتاگون:تحرکات سطح بالای نیروی هوایی آمریکا در خاورمیانه شدت گرفته آماده باشید
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/11470" target="_blank">📅 13:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11469">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دارم میرم یات تولد ، شاید دایرکت ها رو درست نبینم کم اختلال داریم ولی من هستم
😬
🙌🏾</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/11469" target="_blank">📅 12:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11468">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سی‌ان‌ان: ایران به کابل‌های اینترنتی تنگه هرمز چشم دوخته
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11468" target="_blank">📅 12:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11467">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/11467" target="_blank">📅 12:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-text">داداش شما رئیس سواک میشی شک نکن</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11466" target="_blank">📅 12:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم ساواک روزی که برگرده باید اول به من بگه دادچ آرشیوتو بیار
🤣</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/11465" target="_blank">📅 12:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1faf363e.mp4?token=Zc9bnsqwzxM8SCODszsA0xcIXuV8VFwBoPalRJzAzrQd0uCBd0SV-X6pYBDW70dsRhl8TvmpXrCkL_A4QMukKoIWNu8PNXtjgx9uhYebNvrUfLV8iMhHV5cq9XI94D2fge0kxrGQ9qbCsGheQuTk1GyZdQ5muLEcD4SbnS8hAz663jJ0-3Ds_otQAmk0KzbJ7gwL0sD0p8H2dTADnlmEfmf4hU0_L47x2g7oJhznSR9pD8cU6qN0WAka3pv_zso5i1ORlbmuMvxHAyQL39QI4PqIm-rsQ3s776nkXsUUM1jpcNxxTetMQ4GmcvkRgWDOP9B2L_Ftr3ywuUMzDtVt6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1faf363e.mp4?token=Zc9bnsqwzxM8SCODszsA0xcIXuV8VFwBoPalRJzAzrQd0uCBd0SV-X6pYBDW70dsRhl8TvmpXrCkL_A4QMukKoIWNu8PNXtjgx9uhYebNvrUfLV8iMhHV5cq9XI94D2fge0kxrGQ9qbCsGheQuTk1GyZdQ5muLEcD4SbnS8hAz663jJ0-3Ds_otQAmk0KzbJ7gwL0sD0p8H2dTADnlmEfmf4hU0_L47x2g7oJhznSR9pD8cU6qN0WAka3pv_zso5i1ORlbmuMvxHAyQL39QI4PqIm-rsQ3s776nkXsUUM1jpcNxxTetMQ4GmcvkRgWDOP9B2L_Ftr3ywuUMzDtVt6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان بحث داغه دیدن این ویدیو شاهین نجفی هم که در اوایل شروع ‌به کارش برام فرستاد خالی از‌ لطف نیست ، من امید وارم همه با هم متحد باشن و مشکلات تموم بشه
@withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/11464" target="_blank">📅 12:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ac4f62eb.mp4?token=Ra7U7wnm-Comh8MEt4VwLczbWGJYmXgjc58c2j17RMk3092r2mA5E2IkO04LqXtAggQZiL4Gc4nuFKCOtnPdhlwy6DZbWgmklsQyaKYA1CBvdZEEDH6En95RJFGrsHDgYdB8TPpFLGP6r4BPIQXjMMFau4yDitIIERU__Jo08C-19-12daNrvXc2qeFf6Ed0txmzScu3r2yZpyHdyHyv2mCfb4z4NfMGqXUL75Sc_OhdBjk6LaCnlUjhWIeAKBf22MZ0-09Hdx1LY5XWXFkQvCQikNBxm9V0fgKR0rC_OfG9QnEIHQaptLVDQCFOxQ_46mAmT_3n07cfkkWK4Q7oMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ac4f62eb.mp4?token=Ra7U7wnm-Comh8MEt4VwLczbWGJYmXgjc58c2j17RMk3092r2mA5E2IkO04LqXtAggQZiL4Gc4nuFKCOtnPdhlwy6DZbWgmklsQyaKYA1CBvdZEEDH6En95RJFGrsHDgYdB8TPpFLGP6r4BPIQXjMMFau4yDitIIERU__Jo08C-19-12daNrvXc2qeFf6Ed0txmzScu3r2yZpyHdyHyv2mCfb4z4NfMGqXUL75Sc_OhdBjk6LaCnlUjhWIeAKBf22MZ0-09Hdx1LY5XWXFkQvCQikNBxm9V0fgKR0rC_OfG9QnEIHQaptLVDQCFOxQ_46mAmT_3n07cfkkWK4Q7oMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا همش به تاریخ پیوست…
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/11463" target="_blank">📅 11:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/11462" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عباس عراقچی، اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/11461" target="_blank">📅 11:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11460" target="_blank">📅 11:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.A</strong></div>
<div class="tg-text">تو اين مدت هر وقت كه ولنجك رد ميشم ياد شما ميافتم، هميشه و هميشه و هميشه
اين ويديو رو براى شما گرفتم و صميم قلبم آرزو كردم به زودى خود شمارو تو ايران ببينيم
🌸</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/11459" target="_blank">📅 11:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11458" target="_blank">📅 11:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11457" target="_blank">📅 10:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11456" target="_blank">📅 10:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11455" target="_blank">📅 10:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11454" target="_blank">📅 10:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEu9aRip1OZW1_pHaRHYTiSAjwc92IsM3buNmkZs2s1tm4R-j-I3PIytlWAUVM0200Lvu6hBJ1K3FwgF5rzx7rjq1RF0yd8UgBXrL5KCmumeUyRwMNdm69n_8uWQ6OwvkfVN5Hmx0Mhb5cb-WqL9bKN_qCeZ3w8Xr167FvsFJ0Sd-CV4Hj4TwZmCIgDG0N4DGoi6B3rdEGu_RK807k2xGXZHbvISgqntq3CB-DJm3ic1gx9lOQ7N247PE0la4URVRwYK2NpHAe-k5ehygg5cmF5K6-D3xqwu_ciOni_5wL5Nkfj19DGS-bLEwF-Cq6rviyADC5NpdSVwzp95M2CQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11453" target="_blank">📅 10:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11452" target="_blank">📅 10:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11451" target="_blank">📅 10:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/11450" target="_blank">📅 10:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYas</strong></div>
<div class="tg-text">عجب جمله ای: اهدافت رو از ملی به مالی تغییر میده. رحمت به شیری که تو خوردی یاشار
🙏
💪
💚
🤍
❤️</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11449" target="_blank">📅 10:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr_ACE</strong></div>
<div class="tg-text">این لحنم نبود
🤣
🤣
🤣
🤣
بد گذاشتی ک</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11448" target="_blank">📅 10:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ولت براچی گذاشتی تو</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11447" target="_blank">📅 10:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr_ACE</strong></div>
<div class="tg-text">ولت براچی گذاشتی تو</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11446" target="_blank">📅 10:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/11445" target="_blank">📅 10:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پدرم در اومد رسیدم تلگرام چرا روبیکا خبر نمیزاری یاشار</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11444" target="_blank">📅 10:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froms.r.s</strong></div>
<div class="tg-text">پدرم در اومد رسیدم تلگرام چرا روبیکا خبر نمیزاری یاشار</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11443" target="_blank">📅 10:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">معاون وزیر خارجه روسیه دقایقی پیش از قریب‌الوقوع بودن حمله آمریکا و اسرائیل به ایران خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11442" target="_blank">📅 10:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11441">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تاج: فیفا برای هر ۱۰ شرط ما برای حضور در جام جهانی راه‌حل ارائه داده
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11441" target="_blank">📅 10:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11440">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/11440" target="_blank">📅 10:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11439">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAhmadreza</strong></div>
<div class="tg-text">نظرت راجب فرستاده پاکستان چیه؟ بنظرت احتمالش هست بتونه کانکت کنه و جنگ مجدد درصدش کم بشه ؟</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11439" target="_blank">📅 10:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11438">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/11438" target="_blank">📅 10:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11437">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEnrique Batista</strong></div>
<div class="tg-text">داداش یاشار
خیلی از کانالا دارن میگن که هواپیماهای c17 آمریکا دارن خاورمیانه رو ترک میکنن .
این یعنی چی؟</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/11437" target="_blank">📅 09:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11436">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلام وقتت بخیر با توجه به اینکه این اتاق‌ جنگ اسرائیل تیک زرد داره هنوزم فیکه؟  چون تیک زرد خریدنی نیست تا جایی که من خوندم</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/11436" target="_blank">📅 09:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11435">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdyar</strong></div>
<div class="tg-text">سلام وقتت بخیر
با توجه به اینکه این اتاق‌ جنگ اسرائیل تیک زرد داره هنوزم فیکه؟
چون تیک زرد خریدنی نیست تا جایی که من خوندم</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/11435" target="_blank">📅 09:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11434">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">باز این اتاق جنگ فیک اسراییل توییت گذاشت الان همه میفرستن میگن یا خدا
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/11434" target="_blank">📅 09:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11433">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af61de15c.mp4?token=SBPmzutnOlL6iV0aZJW1te9bcEg15zpCALrFO51IDIRAP2PW4Yo_1r7xnSIjhvYqUeTlrZm0NiZ2qCnnMMl5AJKF0WrutVLa2lq0sI4AgL3QLskVEa84GuQaqOxDVauE0VY4WKiumcThLI2ImUrKthpb4bf72IHrUwLuS7TTD-2Mq6ZZN8e-bTzQVeu0HpWi3gtF0kwR36yQlAMXm2hUBPJfCAJY_iqAvdm3051ZdgTtStEO4ZxPpT_lhvGSCeQQ5Sp6QWH4MYmJ5k9JBOSp0iZAGU1QAzViydDbXkIteMNt6VmtJQzJHpS5YNa2wZDeJrUd9f431cLWQ6KKv-dnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af61de15c.mp4?token=SBPmzutnOlL6iV0aZJW1te9bcEg15zpCALrFO51IDIRAP2PW4Yo_1r7xnSIjhvYqUeTlrZm0NiZ2qCnnMMl5AJKF0WrutVLa2lq0sI4AgL3QLskVEa84GuQaqOxDVauE0VY4WKiumcThLI2ImUrKthpb4bf72IHrUwLuS7TTD-2Mq6ZZN8e-bTzQVeu0HpWi3gtF0kwR36yQlAMXm2hUBPJfCAJY_iqAvdm3051ZdgTtStEO4ZxPpT_lhvGSCeQQ5Sp6QWH4MYmJ5k9JBOSp0iZAGU1QAzViydDbXkIteMNt6VmtJQzJHpS5YNa2wZDeJrUd9f431cLWQ6KKv-dnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنته هرکسی که توخالی باشد بالاخره معلوم میشود
@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/11433" target="_blank">📅 02:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11432">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc37be173.mp4?token=kLsHwF_QILKCl_wOPzgbOZsfokGNtIzs_MBO_yYJHLeEKvA0gyolF0V-JkQUwFsklQjPiuK3c2kE1kZuYnzFQta3wo8KgjsuTFN6BpJy6Rj3mly5QqQkfFXh5_l6ykFzkaSp8Y62EeT0etW3jbdSOM6Bt0xPoGJvj2VtEA9UIqDwANk_oJ16Qhg0iKmy4VP21AFokhBpBXKlOHa1JGXWIt0lSRnnGJJM8_WzrPllFQDnKTcoWOuIioVcB672CeikK8fjg4f_3eGKC2LlEE8eKtCCPJyDmnw0ETjzpAoOQ1Oy_M-1apfKgIHHphSSvSy_Szi991-Y0l7DvrRSSB70tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc37be173.mp4?token=kLsHwF_QILKCl_wOPzgbOZsfokGNtIzs_MBO_yYJHLeEKvA0gyolF0V-JkQUwFsklQjPiuK3c2kE1kZuYnzFQta3wo8KgjsuTFN6BpJy6Rj3mly5QqQkfFXh5_l6ykFzkaSp8Y62EeT0etW3jbdSOM6Bt0xPoGJvj2VtEA9UIqDwANk_oJ16Qhg0iKmy4VP21AFokhBpBXKlOHa1JGXWIt0lSRnnGJJM8_WzrPllFQDnKTcoWOuIioVcB672CeikK8fjg4f_3eGKC2LlEE8eKtCCPJyDmnw0ETjzpAoOQ1Oy_M-1apfKgIHHphSSvSy_Szi991-Y0l7DvrRSSB70tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/11432" target="_blank">📅 01:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11431">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایران به عبری ی توییت زد ک  پیام روشن بود لفاظی نکنید... המסר היה ברור: אל תהיו רטוריים... یعنی کار ایران بوده؟ مث ک کلاهک اتمی اسراییل اونجا نگهداری میشده</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/11431" target="_blank">📅 01:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11430">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoul</strong></div>
<div class="tg-text">ایران به عبری ی توییت زد ک
پیام روشن بود لفاظی نکنید...
המסר היה ברור: אל תהיו רטוריים...
یعنی کار ایران بوده؟
مث ک کلاهک اتمی اسراییل اونجا نگهداری میشده</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/11430" target="_blank">📅 01:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5a8240dd.mp4?token=G2aB3D9zhtybpt_nGx25SrvHey9lQxkE2GY941pODpOUvrrmUWkAFmXZZjgqSpMjfKVTkX9MyVGe5vhNy_oTX6Zm7B_ntjUXiZXmmsWMRLqRtBlaXTm8HKWg9TqiTbVT999qmThXf9LaeoHAqu49JqX7m_9uflmKP_sW2-klrA0TjFKIVmcggrjAG492aIH918-Gwzzck6E_iXdlwS0oUPPJbGGlMNAnhm1yM_m1o9jrEkh25UocJZHJhDWjUdBcfN_KQwr2r1Kx0HiuKyQsNTQr-SMXfYLauI1pRzkt1honnQSclSEQglX9YbwGyhB6okpesqVzNgz9E_SvLx8uxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5a8240dd.mp4?token=G2aB3D9zhtybpt_nGx25SrvHey9lQxkE2GY941pODpOUvrrmUWkAFmXZZjgqSpMjfKVTkX9MyVGe5vhNy_oTX6Zm7B_ntjUXiZXmmsWMRLqRtBlaXTm8HKWg9TqiTbVT999qmThXf9LaeoHAqu49JqX7m_9uflmKP_sW2-klrA0TjFKIVmcggrjAG492aIH918-Gwzzck6E_iXdlwS0oUPPJbGGlMNAnhm1yM_m1o9jrEkh25UocJZHJhDWjUdBcfN_KQwr2r1Kx0HiuKyQsNTQr-SMXfYLauI1pRzkt1honnQSclSEQglX9YbwGyhB6okpesqVzNgz9E_SvLx8uxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو هواپیمابر جرالد فورد به خانه بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/11429" target="_blank">📅 01:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63af08e0ad.mp4?token=ZVuwptOOWg21Xpuwld5MggPmWPHcuOzbZBKPC4WH9EP39MtfnY6DLpOljvnq9QOXEBBv6RREKJHpA8ZS0Cidum2txRW7GkRfDBvjEfImpUupBHbdWfcmyt-gdA9xN0epXYpo71lWOWfUijEQtVEjl3Lqi7vk5Pn7Mof3OD0J53voGwm_TNyKpbDFeBidLJfbEkixK1lBVmJ4Sz47QkcsXzj_cquFNd5ZJUH7W8SvdZjXRoGnMa-euf0d1xUokDuYU8B36JJ1MPFuHaZ4xae_zEi3Av_RBojxxsnnOj6Ls3e9cCu3RpHWiG5WLvNkyHb6VQgtzDqr75EQHW2J-qXYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63af08e0ad.mp4?token=ZVuwptOOWg21Xpuwld5MggPmWPHcuOzbZBKPC4WH9EP39MtfnY6DLpOljvnq9QOXEBBv6RREKJHpA8ZS0Cidum2txRW7GkRfDBvjEfImpUupBHbdWfcmyt-gdA9xN0epXYpo71lWOWfUijEQtVEjl3Lqi7vk5Pn7Mof3OD0J53voGwm_TNyKpbDFeBidLJfbEkixK1lBVmJ4Sz47QkcsXzj_cquFNd5ZJUH7W8SvdZjXRoGnMa-euf0d1xUokDuYU8B36JJ1MPFuHaZ4xae_zEi3Av_RBojxxsnnOj6Ls3e9cCu3RpHWiG5WLvNkyHb6VQgtzDqr75EQHW2J-qXYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سنگین در بیت شمش اسرائیل و دیده شدن ابر قارچی گزارش شده که در کارخانه شرکت تومر رخ داد. این شرکت موتورهای موشک سنگین و سبک، از جمله موتورهای پیشران موشک‌های ارو ۲ و ارو ۳، موتور موشک هدف سیلور انکر، موتورهای ماهواره هورایزن و موتورهای موشک باراک ۸ و باراک ام‌ایکس را توسعه و تولید می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/11428" target="_blank">📅 01:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/11427" target="_blank">📅 01:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8cf2c560.mp4?token=Z_1LIJa31LHKRw3Q1dYWpbHv8vx6KHJonT33nxa4IQOONCMdYUZEJ_492WZjllmn705VyXiNSKeCeffdeajy7pVB5pBpCDB-qrRQxs_i2BH4LbQb9_YrLj1SBb05-OgJVx-A1ritDtIf0Qhn5PJfxEJe3jv2gyBkCRar-OJ24AQ_RkTDKZYr1FTHSp1bpZ8wPSRtx4UeK5eD7eKmcUEvy0RTxx1a8YEx2hXdPO7n3bQVlTdI0iHsWAqYhWNFZMaXlQJcZVfPs1YqruwXY4iR6MWe5HT0k34Pq1o4f8p4F8z2jJVUwEhmBj5OM0HhezJS23XPOt9BPIMF5t9--WBF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8cf2c560.mp4?token=Z_1LIJa31LHKRw3Q1dYWpbHv8vx6KHJonT33nxa4IQOONCMdYUZEJ_492WZjllmn705VyXiNSKeCeffdeajy7pVB5pBpCDB-qrRQxs_i2BH4LbQb9_YrLj1SBb05-OgJVx-A1ritDtIf0Qhn5PJfxEJe3jv2gyBkCRar-OJ24AQ_RkTDKZYr1FTHSp1bpZ8wPSRtx4UeK5eD7eKmcUEvy0RTxx1a8YEx2hXdPO7n3bQVlTdI0iHsWAqYhWNFZMaXlQJcZVfPs1YqruwXY4iR6MWe5HT0k34Pq1o4f8p4F8z2jJVUwEhmBj5OM0HhezJS23XPOt9BPIMF5t9--WBF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب بیداریم !
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/11426" target="_blank">📅 00:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏ جیمی دیمون، مدیرعامل جی‌پی‌مورگان چیس، درباره ایران:
‏آنها ۴۷ سال است که تجاوز، قتل و کشتار می‌کنند. دنیای غرب اجازه جنگ‌های نیابتی را داد.
‏ما درس عبرت گرفتیم - باید سال‌ها پیش به سراغ سر مار می‌رفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/11424" target="_blank">📅 00:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11423">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3D0QCkX6H6GMICmqd87sTYCojyH3O-D8Eydtnll49lEjlqOKNQnXGyf989wuaWIIZt0trwvam9df64fUsTTDVdgB7pvi_bCbwS9fkzpr3q0PS4yrHUeyCch-4rO792leWVyC4Q2rbdwPHFK8hdrsday3IHZxArBoyJ6mdIHPQA9yOLmNgseOc1UpYU2McKM6il1x-e4ikN6QJVbctWtx1c3jVkihVU9dpq9RTZ47dajcjkj7g6OApZ0C3fwuhAJdKooS7mDttNd_GHCDm6I1vF330mySWtGXEi_lBXGv7WgQzu4IiVdJMHYH7vBMrOoLoRIBlgFI-s0g2R2z05JiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد امین صابرکار، دانش‌آموز ۱۷ ساله بسیجی بوشهری،‌ حین انجام تمرینات تیراندازی اشتباها با آتش خودی(فرندلی فایر
😬
) کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/11423" target="_blank">📅 00:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">@withyashar
فرهنگ ما همیشه غالب میشه</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/11422" target="_blank">📅 00:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42c743cc72.mp4?token=cnAxx16KQW-fZxetRCt-7TZe0jmWMsyrFBOs3IV4_Oib3kprrg6vfOnp8tWZWI5uzbIB2hD34AQJwfqt6AMQ-I1KMGf8uTGzQxDx23YJ4rxbHx4vYGv-XcjQepd-gaHwdfG8R3hB_OsT3xtwnI1V312xsPo5bQgrxYj9rE5lk3hPLoLuOMcxqep5VIWaivc-lcr3h972hBp67j3H3D61fCLkgVIkB6i3pNlMpY-ifzIIW1SeDClturVmvY3JFj1pKTBJqUu-H-zk_eHo1VbZbXW-IsH7WRLVmZIlN7hEcnKdZjXfnqhlYu83QwBLEKn1qt4R5G057fhCxHOTXt6dCIz3JMWKDHiltTs8utsfQC0uvxhC7uOXYU20BY2TPH3OBmGwqdiCxn6R5f6kvKbyYdrc8mpOEvz6plV2eSVdIytLPyZqJT57S0HqGQg41n70pj5NQf-HRvoTj57eejIKTRGp47bQjUS-F4BPOzIycyH2FAiK4ioavR1-FcOWNxhJ4b4UCAJ6L8oXNx15HWR8QQ5FPIor5Egu1JD-mPlyfwFLBmLOYpg8niSmqvkC3wDHmj9cON34CD-Cqs7kM2dDxokJ4CvhlT1jFFgAAMQUNvWTNRMZmW2mkvr4xrbxsEG3vDXKzF8VzFxXPv0L3I_t7FtQ_X_Z2nqB84TNM_UZACQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42c743cc72.mp4?token=cnAxx16KQW-fZxetRCt-7TZe0jmWMsyrFBOs3IV4_Oib3kprrg6vfOnp8tWZWI5uzbIB2hD34AQJwfqt6AMQ-I1KMGf8uTGzQxDx23YJ4rxbHx4vYGv-XcjQepd-gaHwdfG8R3hB_OsT3xtwnI1V312xsPo5bQgrxYj9rE5lk3hPLoLuOMcxqep5VIWaivc-lcr3h972hBp67j3H3D61fCLkgVIkB6i3pNlMpY-ifzIIW1SeDClturVmvY3JFj1pKTBJqUu-H-zk_eHo1VbZbXW-IsH7WRLVmZIlN7hEcnKdZjXfnqhlYu83QwBLEKn1qt4R5G057fhCxHOTXt6dCIz3JMWKDHiltTs8utsfQC0uvxhC7uOXYU20BY2TPH3OBmGwqdiCxn6R5f6kvKbyYdrc8mpOEvz6plV2eSVdIytLPyZqJT57S0HqGQg41n70pj5NQf-HRvoTj57eejIKTRGp47bQjUS-F4BPOzIycyH2FAiK4ioavR1-FcOWNxhJ4b4UCAJ6L8oXNx15HWR8QQ5FPIor5Egu1JD-mPlyfwFLBmLOYpg8niSmqvkC3wDHmj9cON34CD-Cqs7kM2dDxokJ4CvhlT1jFFgAAMQUNvWTNRMZmW2mkvr4xrbxsEG3vDXKzF8VzFxXPv0L3I_t7FtQ_X_Z2nqB84TNM_UZACQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوش جان میسپریم به فریدون عزیز تا من موتورم رو گرم کنم ویس بزارم
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/11421" target="_blank">📅 23:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11420">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF7IVVcUjm-kDqRBHtMs7TPP0YgHNmGpXfstiwqi7_OWmBdYDRAiwbaQI4g4q7p2qGJ4ylsZCnX5ISlAyRYJkvJCLNB42hqY255J8JajD1sdZMBRyLZcWj8lYKqZYvwaglDbxdKYTlLKrK7XNfvEfIreN9V9A02YeBlEPYO3F5olTpuVytkwKpNmiMLshp0LZlnDKVn4DDmUMw_TaOu_XGgkQgaCvSFa54Sah_4y2lK_fQCoaXqAcMCi-_wqCU_twExkgAKa31zbIQ1b2qV4juOn-d5WCDKO6E2PRDlgVtRwc4QnOAD-EL4Ck5Kccv5P555GuvdopKDMkcdGOUh4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : آرامش فبل از طوفان
قایق تندرو با پرچم جمهوری اسلامی دیده میشود …
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/11420" target="_blank">📅 23:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11419">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/11419" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
