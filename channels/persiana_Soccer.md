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
<img src="https://cdn4.telesco.pe/file/Yu8IiDtjtDBz6CJlqh-OZ8aUXrfjmQRoYRmSET3mXIxa2rCI167tw8Ef6aQF4UmU1-Bousy9mx0ZU1-PrzuNJAkTzUq-A9CajtVP_Mq-QOonHJ01_YfljT34rOWNUZ_KyNx3kUnx4jM6l3RpOcN48FkdxArvsoK-ipeebp6-Y5UI5DG4AFLVXX5d3f3yuRJSHQcedTjRGhOJa9VzW7NpFIt-ojkG2SKbcfNqfGfvGZcXcfuCysB-vEOdO-xe63Lr5-OBv_bSMfJW6ezwmxsB9c8om4gHeOqGMyfJOljS72rjNtlnN72TaCOKN9rlViywMmaaRIF0SNSV_OTREiDXTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 605K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 20:50:37</div>
<hr>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXRK09w_PkQlexQ71qs0ketq8WpEH-3ozHeP-Dg1zDDQbvoIUc-OjIGv8nvz6N2SoeIzRkER8IZ3wtxf7gKg_x9M1DVFdy9CPRmYrj2jrYsy_ijIeyKgqIAvMy6MLwgwvzt5nuHQSd_HJeWbHDvii6RWMs9dDJWyeNdRiZi7mSQA2zxEzhbVmSqssMGY0iH4E1zlqgkPQ-VsSqfjK0_h1HrzARFVP4T7MeVWJG2DD97ghx7eQkiZRa6MOphhc5Wpt9o7jBBONldKfHUwL93EU_VVKiHl4-pxS0VLS1fkiAiIYlPbO6UbHV7gp-cGg5qP6ntOxFPoBkL4TqWKS7QtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=GR0uohhauef2twzQMD4bsMiyneKa_W8xZrgyb3JQP7HjCHe4yQJHmXLkYhfN0OaqKLp-Kn9vDI95kbfpyLz7_wQj-1cwJXyglcIjaYUE61psfIfiAhzvDMgnh4vmuEh4NLbXQH7c2a9LtOteVWOFwm1Asqn84WC999I22t8Kco6t6j8HQY2TeLVD3kqjiXGVYYy5s6FO8V8FaHUWEtEAYMfAxCMPVwrZK3r5VuToTT3tcYTUOBetm_aJU_VfyG3sK0lZ_MozcGWT_MvGXqPcuCxcZxC6hjm02wC8tQcSW8YqtAOqwi6sbV8jczaFLppWerAlcDhU73PRvtAtq54HqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=GR0uohhauef2twzQMD4bsMiyneKa_W8xZrgyb3JQP7HjCHe4yQJHmXLkYhfN0OaqKLp-Kn9vDI95kbfpyLz7_wQj-1cwJXyglcIjaYUE61psfIfiAhzvDMgnh4vmuEh4NLbXQH7c2a9LtOteVWOFwm1Asqn84WC999I22t8Kco6t6j8HQY2TeLVD3kqjiXGVYYy5s6FO8V8FaHUWEtEAYMfAxCMPVwrZK3r5VuToTT3tcYTUOBetm_aJU_VfyG3sK0lZ_MozcGWT_MvGXqPcuCxcZxC6hjm02wC8tQcSW8YqtAOqwi6sbV8jczaFLppWerAlcDhU73PRvtAtq54HqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfLMr3CqfhseGB_zFmjbV2LuQX7z5aMVNn8orJdB1YuzcMFN2D91hNswVDGeaELq99ErmJLX_Cs33YoWT6UfOspyZsJR0xf6BM1wer-xEtr0QfMw5xS5KdG-6gmjCA2rE_6I9mmoIuvry60WPml3lvNhzKSwj8wd6k94mPRGZtAG2vzBZGCZ39hhlk9VIy_dAkq0Yc4bAEpBjhfYTnrH1qua8lLwgeKcCMUAnyMcLManfyufNX5U-1Fvmp_63WMxnby2B6UvHRv1FUcV3LLZScXnMNL-hH0iFUe6kyCBwz_J55d9mFO2Tvi6PeTAHG3_UPH9u7GCWikfn2G4UqZLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE5YjafaXq90Y9zhDdQCo3slCnI8IFB0zrgnydVCqII9oYueFpLGIgGRluuMgcyKWZMgKzpqmjZgoYn1jNGKF7TrE9nzALsVpPKVKl5RAD_RAVFufEMlQEAm8cTle_vQeJTcJpEhpMCNn7zpvBuolHWb8zBV3XEXOb9UjFTQkwRIFgITFFP23Lwjb_4Em7_FiZpZs-8b5DG-nGU-MFihQy7I5P5XcaXccgEvEwgU9UDO6wgBTSQtKocgUZyf7wmmNm89LxTl08yrDFe3LkkYcDqu4_XkUsrVLD59QsnkWjMsbvV4eANwK1FI1kNuijBU7RFh5pK2xhE7OVS9c5Dzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArvQwunyWzB-O-IoM9HHA8J25aHLfzKo6JRlZvCHIhyc5AEiJAMGZCv1TXzH4pmJO4GJtdh9lBDk2sRREyqI0HeYbFw0hVkZKbpGbgbUqfS5frdMiCmv_EbDHhlWvghbX1UEJIeBzVDk-ijIUusmZY63vuCSRvmFkzabduWRAM8px5yJKzRgEyIp63ZFwRfuwQwtPHL66SfEP3fO_BqHWT8Y7VhEDi_t7Q4L_EM9XmAEUEeJXHDhDjljMzw19YEVGn6lfjwenJmr40HofE7lTZjaW-ufKUm4bH2f38ZZU0_03P3KyS-zJoVCcYPrCpmKvcwcYZd4qSUAOiLNSnWx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPJU7NZX1brCgg8d6_-PZRmoaVNZgrZd4M_VW0V_VMyzPQLBwkaSKKBG_H2cgZoCoE8YuFjuRslrnBTKBWVHIz4W4Mi9xhWGe1wI-ZKJ_EXJh4SLQBfoNSxJxDEehzWJzDQuvVeVnSshzS3fh3f-2rEnaz5QsrNH5b9hIdjE5JcbKzQ21GDSk2x80W_hplV223AoYSLtoZXp641_YqZjZmYvAf9_ERbgytPFwfwBZT57S9PWOEKK77d_1b0g9-8g8IyIe-cZutKVyMAz1-oV1TPr85A0-GBxW3gkHBns9pB2ASPkD-QrPTMrjX3HDvHB1JFJr_mU85X9sheV4viFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv50TcRvy1Ccr016CSCW9LuwwVhCyzhR23zDXTeOvUb03v0OGnpAVrNnBU4zWiGeq9ZJF7sNlwGbvzN_LyXrpY_SnfxgRzBKqfXlt5QJrljR42QbVqjD_SudEuxCJdovShFqKumzTSgFF3JID_n0x-5hhTplhn945N7UE2LkwHh2EaM6IkLIwEXV4dpa3HoXZVl4yuTQkCzzIyQ74CbYPBLIEWmoQ-twgqK-SkdMJ5HkRcF4uHghl8IamKFvkV64QYqgY8A0unILdnww7p9QtYOM1btlEbeNKpZyQPU1YTNJbc-oKvwd_HMdQZQvRg9MNjxoJ-bRmegH08kG6TdkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26890">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚡
گل اول استقلال به   🄼 TAJ NEWZ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/26890" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5bZUij1esGCDgbfEaPt-S5rSyC9T_ZklJxkrcI3BmA6LAjouWUXNQluIga8j28ik83BGj3ro1PdP91-PXb7g_kTSS4r9QuI5q-qmxvPdnU6Nk7X6b9dsqlMXP0qMfOOJwWX5jCWaxEUToHHJsrQEyGcbssPfgIThCRVuFJUHYaVdnwqxH7XmrAq2fhcMljFq1NbJlm5qMWykeK2o1Cxd2WtW_T_flqYGUFPZRUSgwHbHrJJs-CXqAjjizXI_owMs7dVgg3rGvcxaSUV2c9n6heihK5lLBGnaUoECUNmzaxcBYpRmY36438WYMCobQsIW9_GqbjuF3jQWcXjUuYMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obkhzRifX4xqtgXeZKoZjgSyiNkgm3QETFg6MYELNmdS9VaCpwnxtbCR68hzmE8HnCMjBv-juozO4hsSHPn7hS1ZK0d8NY1TGFFZ5upsW5ZgvdBY-rT5RmRzya1CT9CxKqn02QwnQpJjY1HNkhbh1Qh2m-ymTidsmsdtDLCLhlY3KtWSeFi5qw-AosgTQ4ALlR07swRB_jkp_E1FNhGwda-7b_w23yFJJl4h5gL27d0gTGk5YqSAJQgFMDRDi6k3QHPQtvePHEl8TbisGfCh4YlH4fNzabg_egqjtrDunFOhbbi5xva5AunXRks197dAXzhj5QAlJqYnMqeSX_tSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRsXn0Thoirc1qME_j6azLanNC3JJIgOm53NF4e3g6H2seKZ8jzlZ68HPznQZxVHB_fvGMgVwPl_D8COugNNaltqeYvS-FE_J8J13BqcX1dDzKrkfuzcSHiW6W3lsrzw0l8R-QaSj99gmPoUguRKxf6dDLykiWuqbbb7PvLnBPgL-DPz6r8UkROFJIH0OfqysMFfHjaEu1-waRo6fswNqbulGpMi9Lu7e1WU309l80p2-PS_1xjcJqo2J0JO80wAZBdNG6wWXHeTCVPlFdDJhcjCKR-TRZ8oMMQOlNQQx-hyWBYGYRMs_ZJXEKsEB4wrFR4mD9pc_6x54j4rWzTpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se4weCwH7EoFuSTiz3q5Efmj4M5rc8_lLQ8grjdE0zee1hats2QzAlxjs_tlTJZMdBN0myItlDXVwDPfInwDI76fS-A_Aw2leBIwYrY5TDrGKOyCRFQBpNWM9hnO5mGY2Y9UIKflwxmj5H2wzyc0uUNZ6XEJhiXhVeoHr0mWrGqNoBefSbr0dyktBJCnI6pKw4ukyyQeTRJD3kfXHHmnCfqOTMMha8fM2UnEqBwxyxa24BGPJLkgse1bS4KS9-cyCPzqAQ4X3uBHsrabdNjW9pW5KApOE9DgVA0aUeeUuLxn5NMmYyPv1vp0P2y4UCBP1hJuNB_Frc6vmkOoSRwosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHVJExY66ALXLUAP_OjvS6dMXfygEe_CVOLw4O4nNFeXawMrqUAXR1S4X59rmKQ56v7g9Jo_Bgc1YP-eDsIlxjcr600VlHya3Grp0iGyBgGX9EvokOAkDnJsoGOJpiKMgayCNza8QWUgLrumCLVgbcAwJsR-mYm4L_eej3F6WxX3iEWGu_mUCBpS8hDK7dsLNmHonzbXVndHkxXWizUIZDufJHDxvnNHQIc7o5bHUBLzxF3oQztT8mg7MRys2u9OZIgA_6dqpoEubay3txaK8KSEnEpd8FeXIPFNrJkmpdSYun1I1COTk4RgK7C_AJJGeFUM2s2dvd-zax_58I401Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S36U-SXrmB4x52wxoHHpXMx7U82w5mh0zCyQ9hCillqQTN4RMZjh5Xa4wx57EGgr0UtgU91aeAGN1rwJnf-IRcdN9tqa8Epe8cDrOWiBthGFBNFpZkN-s6VHxl-r8LGbkuwEj9AzkTcrondwlwmkBVn20aGk0uZzMxCv89m3dkmINNRWw-8x3yA0xyRAlXq6O2MMWFnxYt9oqu2BjZaUuBav-9IsrhZMXWWdA1sSEyakJRakHBDWPzBnIc6SXSACV2gSMribwJ1zh9BSS4XMfbJC9D4ktoj8Yo8qo98L3JOTuGGe_wELL_JleZC9k5vcI0MpbeQQALA34ulLTddLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26883" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uICKIFQ1Ycfn1QXWIBmX07jXr-c8Hvp3Dz_XKj5yMXqx8wXfR9MlVyFjdnvrcWykVpiB1U93gcyjdcOBAJPJEtVPgyR7EF15Kbl2pgxFUotvsg9Fw8Lu8Lu2OkRSTiEjWxPgfW1QpXPsuzVEtjJzq92ibAWr2gqv1iLYobC2Y4qseqO0NHns_9pA_mlDLNFzjkKGaD567IOII_be4W34Lee_XDSzoZHaM-DT_ghq8ST4oOHq9fXNLGf9hoMO3ksQWe_iofOuKVItl3Umar0-sRqFa_n_hB7TlOlYvoCRtpaNTBLN5IoY2zfW12pJNUzduGXBawp0qWCrReteO0xi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2AVn02hpHWgYrWVaLGZjFDrEizLE7wYiAKV2s5wuOtbQE4mXMrDYCrx8zK1CjJd1IQhjlHb92aOytvGlgjBX9OvNMJDzhXZAc-1xlblsDKvnRxfP6gEZL1V_kWbLeQPuxpB57VXTtxrEl5d9T6ScM7g_MazIYRPYlvPMW7mNK-BStR7WNeAMhYpJHYoftRiLjDLqec_lUBfYlS-Ij9i8-CvYTr4olMS_BTrAbmO4RGAsLDeu-lqEbbzoYnct-KSwEQTlg0yfmL1LIjOxIbUI4Ba2nAZ-nqAPkjqxVBI5SA1VKbtoU_TOdlIjY9xmngdtWGJj1yoXA36FTjunhDk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbxdk8mnyaudSxvPPC37bGpX8cc7cmfDZjpPO4ObjEnqO0NsQ-0AVIpllseaVS-sWvxyvcCkMHem8BhiBMBETf3UCSOm9P8PEWJu-sQ6Xe7-NRNhnWgconb53usVhM_9i92skJglhzIRgOCsOiHH57SmGySlJ1Z9uD_3GcWxlgIlQaNHHywQHZ9a_5WVk7l-2h6hLXUVGQNAbe-5nlrxDzRc0C1aG42H3eVt3IKhv0R3QMfVCPDgRTinZm41cvl0DwWl1Q3kCyrUqeGSBuJMiU-c2igSCDGI5gtXwt9uf7juf5Thada1eXba4ZIOy70aSXtopil0B0mLPqSJziP8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=hUxtuggM9yKRrgxDBdNMz3_HlPmvPgXw0KYtrshL5PDRj8atdGVfcDYslbISAJ2AuZhewmHA-f2PK-OHVXh5cqtU9E7aqc1SuPgUcgw_PQKeCxgG0jpWpRKJ3lU9qRNyWFTUOjFZDXMBw4348yljuGZLlr_-yLZ87JA-WBA0tAd3y88K58ehLwvHc-ImLwS7pGaB_SWzdUUk3eENMIMmkP9eAGcu56gwBWhT7FmDUH8nrDuj8rwAhzulcR5-mAsWlr-us_HHLAnAFNb0xdgM7bBxuJAnqykgOzzgETZ6JntLLZrbEqHXeOPAP4wZrqzeYmJR77JPHUrEq9f5AYjSdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=hUxtuggM9yKRrgxDBdNMz3_HlPmvPgXw0KYtrshL5PDRj8atdGVfcDYslbISAJ2AuZhewmHA-f2PK-OHVXh5cqtU9E7aqc1SuPgUcgw_PQKeCxgG0jpWpRKJ3lU9qRNyWFTUOjFZDXMBw4348yljuGZLlr_-yLZ87JA-WBA0tAd3y88K58ehLwvHc-ImLwS7pGaB_SWzdUUk3eENMIMmkP9eAGcu56gwBWhT7FmDUH8nrDuj8rwAhzulcR5-mAsWlr-us_HHLAnAFNb0xdgM7bBxuJAnqykgOzzgETZ6JntLLZrbEqHXeOPAP4wZrqzeYmJR77JPHUrEq9f5AYjSdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=QWtXW4ckxMS_Z8LxcjzR6tOjnMTj3QAptbwYDD5_DcmqiyLcgtXEQ6sEPu0yqUFD2YilgV6E7Mrz-j62ubBbyF7PSEl-wAMC_l2_yn6jv1FJiGfKpL2T0PaA_uO2GBUTZwix4Uu3GdzM5zj3PcJX1v39b0ai4datnyHGvvm5OnsnoDX2gdJvzeEwbwQftggPiVrqp374inqbzVKpA1YFlhNphcD_KFfePWb5WPcOUMkHOLZW5MlgFfLF2x59uTo3ap-sx2TagrdBTgm9T21X36s1_WXAHx38MPXHpoA-36cC9kWqsbBA8HdoF-F_4zgj6oTSMLcfHeDqM_dxBIlbgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjkcygl8AV4TBXK66UHkx5XMnaQSTUR-ugJ8irgPfywmI_YhcQu96aqj0H-sM_f93Jo4lS2GowU6ALO4thz-Mfo586guwTc7HP9V4t3W2dhyOvBaOsxTc11ARvxjW3SfPqOvyjZ_C3aYpg-ahLBVBx0u9CsVWndXxRlmrx4Ly8UDosf3Q4Jiey0KqZen19aDXd-qKW8KRSpaHJmMkY2guOjB_zPpoBa7DygWRHqvkvdl9eVYwsHO2iUjmjLOhk8TKKSfOPmomajdMap2y5Ukhd9dmA-w1-evuaCZmz6S4BZM9zem-rFZRaZhhfhQgWZNESLHHMPwoR-OCWnfumN_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp9_ZXi--1k39GArbIrWmB085UNhO3q0un8a4hTWoREpaaosP5YFxl52MNBZnJ6sJ0duBHSHSL_t4OSbv-dpV6p3wgAQf4e0z39jMMeLE-E158_oQQmMe8Y3cx-Hz1x9zVRNq_NVlOT4JwGSKSfZ7--Y8C2he0h1mXTEXMkRQj73GzkzF5DHLCw-CnCSUVCBmCS33ZBri2uXSHz3tw7lhhB19MXwiWR7HiY7dGK8xpo8tfM_qS-MlxEh1OJZr6gk84Xlnq1toqmpPLTLHKZ9CCEDxeXCFzzgLWgS47_IK1U2gWJMJuIrf3FsKCaVKZjziVxaQMknta6FH_I9ChcEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=J4LGHYhb1eM6gDjGWgXEw-jh27vUYGMR4WC1IfwLUZDIv_JobhnVfCYC7CJiESltiMfNrKQ3t5SbftDzySNcBQj1H-pwzg0Y3ulnh8VpheeVUABb20etxqDDrFXDBJfN7h0HevIsxj0-J8l8GShGN8ra1Dh68QQmaZNVon0rC6ekt-kf9YA9EblOMThb65CRW883vXkg-u3AQWkTXEF85xtAtPM1e-_lpt-JbAg_BiQV0iwJZpaF3vnhLSCAX-V4E5ne48RoNVctewSvnQfmHiwS_40mzL4Il9Pk5AsvaHMfHd3UEmzPZYqnL0IAmPV-hxiPa6fOH6unYLL6oTGwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=J4LGHYhb1eM6gDjGWgXEw-jh27vUYGMR4WC1IfwLUZDIv_JobhnVfCYC7CJiESltiMfNrKQ3t5SbftDzySNcBQj1H-pwzg0Y3ulnh8VpheeVUABb20etxqDDrFXDBJfN7h0HevIsxj0-J8l8GShGN8ra1Dh68QQmaZNVon0rC6ekt-kf9YA9EblOMThb65CRW883vXkg-u3AQWkTXEF85xtAtPM1e-_lpt-JbAg_BiQV0iwJZpaF3vnhLSCAX-V4E5ne48RoNVctewSvnQfmHiwS_40mzL4Il9Pk5AsvaHMfHd3UEmzPZYqnL0IAmPV-hxiPa6fOH6unYLL6oTGwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESNnSo9XWyeJxAMsPfHHJfBJHbAt1OE4I8lTPF8ndQ_0IQC37gw3h5GMw90TeEuPTEyR9ImD_MHD8-3XeSRIcLqMb9FdFboDl-nQJwoXgIAZrXIEcRR8NGwYRNvzd4U4HaPpmtlJXzN8e8at5duLei2Uhhr1nuatljG0gJKPWigGal1t4Y9rOjs6ZkE67J-iqm0aJFPlsKLqbE80HvqmAoY44MtlG6WNsbCZeEi_H6j04cwvHPOJsKYcJgr55zHsYC36qy34UfPw_5Oc-39SuDz8dSYcPtQhy1meJPCun2JfVP6TVfHwsn4JgmrSVthuet7_R44rHKtUQZinAUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0molnG4jUPPGvf481j3SMYcg3D5BpYoPPtYu2_eUYhy1ojzPhW875Lxhu-E7Wm994kl8u9hE77Ev_AzppxgDmcdkFVZGFbRs-aGNbJb_lrinjFOrqHDjW4eR694OlbcaOaeLwq-h0Z9cJOjpAs_0otICIbwwPJn_okadG9xjVCuCpQ8kXhKhrTAJTsuQkqojLBVJnB_l1RdKK-jR9jyPjEp_fuI0SXp75WNJzwS9GID0njRzzNpOXd9-h--bkSVEOi_Ui04KxnE1TGTla1M9LOJQLs8kOjQr-DQSiPxxsnBY7LkctRmLZqT0aV43NR9UTRQyR9CtHOypJ6v3f4mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9k9j7dI6Xr1X-K4DlWcTPF02avDCMl5h3BRaAVPkoeWy6_Yn83KjcVayEP3hkCKL6s78gGDhGoKpmJ1QFwhVc9UbArWqgQhmkcTvnpnA-6njd7wRqSYGRJxeipkccypn6SF2PLWYqtUcJ-Po26aOnIDE9_e5-ut6j9fhcgVpL2Q1ZvoFYd3teboQY53L2U8e_Bz5xJsCh_rAx78UTBtURZP5zsiYPZFL1yHMa4tst8YITcsbdX0rlCybdGuuXsqui2OW-euVcJkKr-2DO_9ylaWXVFQbqdZDyNWkmKoZFmHPb9eqOgZzHH6kR-LisqZrS2as52hOPMS1SRDmJCqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFygl9nbpfW4LYY1SGGnIzGpnzZBNQ7lJG1o20GVJQ8pcVuGUwy44hfLsfiwn9d53tY6huk0oxnSdTZ9cwV1_7uXpTkipPoQAPFNolPO7Vlxy2YMWhREKCMLGJg0NNCZ76LpNMxrR0O13lMmIXEY6FBvDDzrjOvEg6XRoGheOZBWvNXwzr6ZY2RsUFK3lWxjXe0oSjJcl72KM3aDbGy8zvNtE-sUCpFRvAWt35Bo-DigEKQJJILIlK5ZAWt6dDzMa2gDNS4THztWh7l2qt2ExcKGfddDeMMiVzPONbe9wr2xYaaX_f_tj3_Un5saz_QHjjWKr5gPIVqRunFxqjxMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYgmzXrYKGo-xc4h7dGce0_8LmJBzJnVML8vDYyNxm3BaUoFLTt7Oi0L8F2V-9e9Mb9bwOuBPSSjGOrSQwuOLRWqsF8UhPZfP3mNNPXfctGFDp_bg_dCu1igrG1OZB8J5EjOV_R9d6XWELRaSYZ775e-gpcgVir_pvXRqhil6FigpEPnn_98Y76QccTdPC__6KjwiR7SzL7P0_oAWMqGmGgMJo6iBlmFFiGITJHulg3m8Schw9bj6e3neQuaxZ2PYdzwlPcjPOPtREe57oFLjO6FGG8itaZj-BAmdbkCRZ_KavYdDcsJg-Ibo_HLBAe4IjxOzq9X6hs6tEdpQ8OefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkPy9Qmkiw9O0_4VvXqD30pv8neCflQJ3ApPmkDr4V_sjJIy-nKhfIAzVflswhZsvNEwVNR4QCLEm9lstmCwbqJ_SX-LOwqNZflUKNigBM9Sz5nvJ32CL30Jf8JnDxSibj2NhkLG6W5mlH74yXweQ3oNfTOhZFkgaEXz3D9r6-oyEelAK0xMaP_-Nm5xZ4PCguwSUDhPxKbWHPs0WaWWLKnvNwSoNacQRQ0DIXivtfMwNHt0TnNM5veIwraCuXY7vuLc8lo_p4fO5POOlHlOINj0DVuJ9HkTtq2gOluHRhiLjZPR6xU5UcoVCGZ7qNl105YScCo_G2s1ykOkT8R2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh4GB6R2Zlb7JlGzXHBPoOwx8_onoa1Rn_UzlPi0E4YVLRGeXNj7j2D7sFNFjqw4rAOEgVFr7R2rDmch2nYaRBfG_2Ek8A270ISB1NJnpf1tWnSvVqcJjPrtP-tii1PCVYvpKcI8LYs0n81Stld4BVsIhfQ_Xl0y6GIdMcJY-sVHnQ9lBSlslLKPqMQ86OA9iJSANBbKTo-BljFHKwH-sCNQ9Ni7w-3yS0QSXqxTo0C65GDcVLeki511Jk1NIeSbU9lmpMXBeMajmseNGx9XkqRzloa8MIRX-v3kd26kEnbXzAmyeV3_RjSlMMREQ3iYbUaHbUPtOtn7Y8IccI7Lmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26866" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxOqHvNL7y2XtHohbs7HcT9loajHMotifeFJ056glTQLbtty7t6C4ankKL3tY5rbkeotrYe2bnsj_5MVXMUdBZQTc_X2S7G9_p25T0yG8w2acCMHR80grnncZwaf3gRwC0AgzK9LPbzizv5Opay9UvtDl4eXc_bzhaLSVsgaWlnOPt4um2K1zTDKeAAynkJ9hcynDRWhFgzYsV6wwV0Nb4yjEoHcXxa7PdRfnFx0OcuL5wnJg4AZyTT3xAdoi3E1hKFfzD9Q5s6hhVkTfNJV8aQ24wYPaJslRh0kqx1WN4Fpx38M1SXVrbfiRdYZQI4HNFoDOaqKAtiaWZSOR1RLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVdyl7m6SpLEj5-y9PvCseuYPXaBrE1hhr8i7s5poPfFUsh4BhuFL5NCgpSh9ZuYDIP-JXEbl5mbaEGfZ_ds-n8UMwNdJQmSfVinHaJEnsNbVJ9UHgjUIOt_u44todVpU4UuWiOyt8WTW0a4aL5Cpnhd0L5AIiQzbYFUqauDLX5dhjVSgSHQjSHwWdPN9h-j4KgQQHnKFKYUCLMIpDR4X81KnJPEafjj-rTyn4FuQJFyJwtztvNAO4WfOB60TAXE3H6rhVAxhA73Nro97daPQ-PGOWSyZ-8N7OQTN9J63Mg1ISxWCmQOYvGcCk361URcOByndYu4vBBw9TyLcwFg7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMilaqwP0FNTWeVxbZDo2HnSIpjv0D0dGI-wCMMUGO02JvL3Iq-9nFHa7kFRcWZUXFgWqa77Ynmu2qprIp1nZm7y8y4Z80noQc8jE5pe9IkSLOHDOLx1ibtKDJ9ddQB6Uie41oGJmLWl13JQoPFsgO-f1cIpdntdBqD6u9su_JFadBPL-t0XCj59QcPM0nlqpype1eUYAHe1RNY7z5h3U62SJTIYIXvaA-bMRac0U4IHnmNeF12R9RkMr3VbveOoVX9MB4EziVhyCuwirWmISOa31LstgUYvT4R7YDnpLVDwZjZnPHRbz2ZLNQWVH_tDO5IoG4_o-0xE6rWc8JyxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osr4opukbslAhN7-Tm2Od4GYVY-3dydjaowNodPiJD1F1MFQK_1f8mcZIuGiNlywV5JPpvhDMSnUvwkzpLJamUc12WLGJXwMYKgQfKxXj9YQooClH0Ereq1G-6aoMTXpMItQjb-6r46KqppE2AeAz6sMhjZ5pifBBrwrIu8cIf5YVksbJIFok4Eu5849sWSM48uGwIOVG1jw4JMZvnb_mPtTcrR5O_UR10U6wodKNnbS4ofyupcbVSof47FBM7QJC6KUIRTS0XWgh8o56wBngXZTXpLuXrWAMPgwOUjjcfvrKZoNPlSFvex7R5QsQJi4jYqG5Oz1k1Pz4-TrfoltSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=qAVq_xdYn_rY3kVZVEsMbwNjHYNnO9fNjZ1gnrtLw50eyRwOh_1A38g3CkBn_Y0us1rF7m1kD9chgw64YbfsHBu4vat_m6aimjJ00hSHzSfhuSa-YxssYqdTAT9Go00vBGdFzk_5jh4hBkbD3q8Ec7rGpqoWHKqFK1D9FWKSeMKhV6pBuW74Dyg-re2YiLTW46vvKyR9Dnv78KusnBWdqTaSMzVNh3fK9d3zpF-PMiWaLec_3X8yNqhP1dhlvetXDbvH46Tk71fGOVSxEqRf9akt0jLlJP0849dgjShbm5saSYk1rFDElQycknMCQubgIGhI5C3_SnTe8GZHj2feiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=qAVq_xdYn_rY3kVZVEsMbwNjHYNnO9fNjZ1gnrtLw50eyRwOh_1A38g3CkBn_Y0us1rF7m1kD9chgw64YbfsHBu4vat_m6aimjJ00hSHzSfhuSa-YxssYqdTAT9Go00vBGdFzk_5jh4hBkbD3q8Ec7rGpqoWHKqFK1D9FWKSeMKhV6pBuW74Dyg-re2YiLTW46vvKyR9Dnv78KusnBWdqTaSMzVNh3fK9d3zpF-PMiWaLec_3X8yNqhP1dhlvetXDbvH46Tk71fGOVSxEqRf9akt0jLlJP0849dgjShbm5saSYk1rFDElQycknMCQubgIGhI5C3_SnTe8GZHj2feiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jenlfORIZweTyG0jxt-V_sP8y1O9XCMm7ETKTq0o-ovgU8wCeujWQZUkYTJX20deGs97IxQee8owf6x1V4GPcj6mhWcdkYw7VganrbEYhpBtg09oJ1Wp1Iiygzi8f8A2sMjjTwNZHbj5O3JeNNwUUelM-BHRDaUwc1I7q7YXK0Qh2pf8cQ80bGO4vWbKtlywa2t010aWrGAp33_nmPDOTVYXsND61tSzmQQ0tG5eA6ZqbFeAV2eHSILU1DLvUqVro9rvgvEZ6pB2GjALC5E5DmMtB8zZpn8gbnsSXVwHS7nPQPKha5EiAVKOJh6rOFhG0mdr1oI3LKnWH_uhBk_M-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG5hV857KoOedEvkzI1yvLGN-iILAWLGJdaTrSQ5K_vU3bzFtqoCf00V0tEQat1KebQ75SegotjL4TY0GGrdr1It1zcs0RvzUf53tZrRLocg8Xdw4S1SsSr4OC3n811ziJpLNjxE_ol7wlEmmredSX1_DjqzFTYtHH1NfsIPKq4z6uzbemmuBNBnt_8OqPPJM2nGK8PwYFxi1pYHowWGYBsJPCBitHha3y0S6-HMsDMvkrXPUmSgfselmSB-wtvDEYjrdjyA3Ku4pkvAW5UDzWQk3DJ67c5nZvJ7k6A5qp71-WDjM9lklBqRGVOHYH-dtonAD996UbWSZvmYlP21BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW8pJUAL4kHmyNMRtkmd8NMnDJunTcuM3E-VrzUznhWBF1t7H6Scspao2oogAoTehI72CG1gmkyZ5bwdfVTNsqEC1AaNf_eNeMiNarSoeSJ3kE5hKBm0FzsHVBWaNTNcG0MezyVVenaEaCElj573KjPDJmQQox8Nu_FBBC1aC6GM8hlfCUgmufI7IDeGwhkBpSw2v-83l1Z9VFs-00gZjwNYjYDxwHU9kax657X6TJvwtt03cHdBk_9dU16saSd-aksU5UVjS8pwv78wvVnfJ--DzHirFegMEYheu_004_S_Uy5klRooSFhtnby0GxqoQ49R1Jzt3UX3v_sc_cyhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwkwWC2yiwhagxAy06y6IzBCOf9MmKJqsQBUqLb3iZtxY_cQYrSkOJ8GEGCdgHduPxMuJyW5fESUldPHhfT2XJpUTvzUUe1kX9EZ3Yz-gSBq9AAijYJPXLICHv08Yp5XXv6HeHx1hlTVP5pgUJgFe6Ac1ujkAptBFVB3xTH_ZAWCRPJaTaQJTPXq1owGec8itSVCxhxdQYX-O6YtPnRYLsCyN2gr71CL4b_yId7a0h77kGdvc2sISFb2LUjlAn0idF_PZEt4JvqJxux6h_xggjZsKWfWtTk3_m4z-MO4M17b1xt3alTPf4X7QusBtYkaIp-ZKdrfqwqsytmsZnzsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqBsn2ifAwbcDpxZhQzjLgokss9CZaLu79B7pw1yEkhx2_kARG0-8uJMhvLeo2B14bvLfMa3X_U-VW6IaGVSKlGJloTjHVU1NqXlcNslkWGYGUp9Vls1UDtAtlPDORGG4nekaGx6GRSt1SRuLgQC73WdEc5QGvcYFEdeeQyDSuy5WKxZ5xH2gcgvMob4a__ewVIHC2L6F1TTqJy8W0C_ltGzZTXcCvw2UNQksSgEn2MNSRliLZUG81_j2zQU4QBg8fVnp2_s69ln3JLNQiqfnFHYY3EUkc2e1l41eMdQyzwFF7C-_hoYWaOt3U_MBJh6tPBYP4Kfs-YWyFqZs8X6SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYs7az8zlIDEVyKNDkC7ZWb0RnCBvbia86TzrYHf6oQ2CEZL89Dm0w96uvijzuhjf1YwOdkuCjQYqjAMkldz6cp_q-oI3xWvmM9zyC9KbK_eg3JMID2lfYGE0K805aV7fxiZLaBP0kEszr6mill2un7PDOp6M7hsWiNJwXSryQWSXP5_0-MjNzfQ5y2dJe0HfqWl1OPLepeoF9iMkCM4V8DZ5mEzSAgmxob0IDjGCGG7tJvA7vxLd2T5668wXrdQs6x5Mk7GrCWlVtLbCj-Wo157S4wvQqhSbH2WbMGzYl7X49K0yTVkAu9Odfv9mWaUPGDunttbUTSKEvH1dVT-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haS3ya7I5HHXhMlT8TS4xRZKPjWwLLVFtw6m6aoyVHwqh4snQHeRK3xizZp3dGa-BgKav18lhg-V2IW8At_4Si2XFqMXecCwOroqPsYPzTnZEi5G-JRehcPljuFHtLRZlFyJarvqZQURUg2LmtcDDeCqILvIwqGDqMbIaoHPmDdrelb5vtrczozo_CTKUfZOlTQzz5dvqmEo-eeSZeI7SOVWyDWBCiUQjYYnVCmMr2iMHtzguD_s0bWRlrgl8qoOdfvdmaMWIRM9BPz_XdamfN1DGz4XjOwsR2Lg5iRS7VrB2M-EJtpMXIdSJCrd-YjC5IYjHowqZgcIwg5i7Oc0uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDDOARo2AP39jmtgjtVup18Z3q1YvBVwhfhvUDWuYQQVCOs6n3Dz0zYTJfKE47cho1gND7w5x9JJeN8s1lQDPTBc_XYTMSNt9tMovtJMXD7fOADj1nW0sH319CDJ9YII48dNW7hdFoRb_BeKqRxvWe0TAFWSI-3j9PB0YyWpunsQmAmArEaNyd41TztVxdnrcIqLqyzP1UzQHWg2MM36FT04vIn_WjDGU8qkh2wqZBpI8MFRgLcoJs7KARvNcVoAoqIBrbY11LYauoj7ySZItyy5fffZRZnCpEz_t4GVS2K19iHOmDSu13zlSLxqM9ooyQCrnfNFqwm15m0Kp6jZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvbnzfXN0bUZAGJSVGKjvgQZdWabAybzd5VYlsLIcoGJrqpyqkSgU0l4FLhaNy5zQxbVyEV2KoNJ5iH50RVcsdGf_Fd7iK2JX0NQ7O5drD9MAF2dh17BfSG9NHfT4E8TUHPXZikwT6O5yNp1MNFXH8TMRmSpyAuGddTN0P02RQnV50HRX2XGieqMQp1QGKOirpFK9FMylKaGcprSFunoPOoUGh1UTRbJxG6Zvf63nlJUGbJRm4GHPBO7TQbshiq92dfpaqpq4g6fr7z1EC7EusiNRgvwM7fb94w71RLSYTLIWDJts9zg_SBtm31MdUES78DCGi2NoxZ-y9CL9SMsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxamEPao61lM247jZ5bekG4UoVCMZakYB6pq2vxNG3RT-GumTU8O-wj3xg-8zQN9zR1lwVWSnZTysSv_pS7l3TY29ke4Cr7k19EJvkQ_gJZGDbT2qvcCyPR44_J1wGGHii37ZgJ1xcCXCaIDFETTOGMgPfvPfoq4l-OWF9ZW2STyTw8qEjlqIFKJNHJfjXEsO3UcsmtIJOQbItaE7EBllmyfAC2vyUl2MTjGXyEBCbhhhCaYcKCOtTHl26Q-Ode_Itt5uyclWzhnwpHLYDV-VFivUA6LvVc8o40tc7HHuy06yW4OOtK2vPUc4uHEvrQoVov7xN6vlZRbcBSR_Qmddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wdVlnjAPu5DKE0wrz3qPgTCtZjU2zyWlpmeJw8-J82KNk6488t2dIlbpRBLsQmqYeLFqFjmy3jT7dQDotW-MWOAJrhgl47M8LiLO23bewvx_V_XwqokNvzD8vS__G7LIUw883wXuGRPmlOYorHgomGllWjiOvt0NrmvAvZwyG9hpjJer8yhSHiAo5v4ll9Kh-oTv29x0RQGH6A6U3T9Hv5uXvEHm-zRdpw7_oJSuArwF8wUwR-iR7Wl46MdpNlPORSHkHLBGGfCsEEFODdXz65OdsOpe3DMDcm8DE3CbK3Vw5Hz5mk4FKRoIdWm8PFd6-V8VELhqA5g9q3XV2mN1vE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wdVlnjAPu5DKE0wrz3qPgTCtZjU2zyWlpmeJw8-J82KNk6488t2dIlbpRBLsQmqYeLFqFjmy3jT7dQDotW-MWOAJrhgl47M8LiLO23bewvx_V_XwqokNvzD8vS__G7LIUw883wXuGRPmlOYorHgomGllWjiOvt0NrmvAvZwyG9hpjJer8yhSHiAo5v4ll9Kh-oTv29x0RQGH6A6U3T9Hv5uXvEHm-zRdpw7_oJSuArwF8wUwR-iR7Wl46MdpNlPORSHkHLBGGfCsEEFODdXz65OdsOpe3DMDcm8DE3CbK3Vw5Hz5mk4FKRoIdWm8PFd6-V8VELhqA5g9q3XV2mN1vE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaJzU149LtZJ5XQI5_T_DoBRiVGpUtsRHyCOF0qVps6CO9aRm1oeoqYAZicH8HxcHv67U2Pjaf30L8tOC6kktvRZt0FVZyBIuc8otLr2PGt7o2mufXD_029MJZmKfr5opGRFQ1kT_dDp5IpqrH46eD0AYWcuKiTsCjaMxJuuummmb_bN0MjBNivy9iSyRsvsqRJqLOjKQxKUhP_vhGia3KyvQ5b86_URFX08bbJsrxJFd-8UM-gpG6mLdAH94b5wimietjAPNOHqPmBUZclgL2ev1MGDYQF9XekMRW2P8aHF_VhyV8cjMmPU7ZlznNHHvAtN-F8e13jwoXwsRsPleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl2DB16141yiteYCM5HGTH7Z7ml7lPP9YkRkSxEfTckEi6Y5eDKULHr-8Zvb7FWYuIPcGVRC5Iv0wKsZpryrACYopmo6ykUEpaW1K3NMSiKl8lV9OWKRAE6y9R6PgCZXyQPgrARscnbdrr1DgHNJ_hyd0oiDOCVYhfGm40EetT1Crrxdc7DZTYd0bOZen2Qx21mse1S1OL3otUKWyll3If1LVQRUTJomYHCe_15vEWr9lMhywDziKeqnMcmf8saPIwSj5YVSR8JmI5QnEVfB9QoR2zoWNYQYVA46K6sVlGZt7WkXde3OoFTomRnR1gtnKTq_e8Kjz940dgkmty_khw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoSDZ0uDxOkARe6_37a5rrlbslTb45_FG-1pJJ8jjBtMKEAUmtyIY2T8QOD1F0PiXqdGP9h9aK-l5B234UGZimOmm4IT2fPqf5p6RAeJMTRQ19eA9DiMJTwaFDQjFsy9_3TqX2VLnWzFqv_n08kf0VF6u7skGO6Woq8rn1Qxa-ZHkCWsaENu1veNTygtWJ4TrLffcmKigxtVFxpqIajf7FkxKMRJYwZ1aW7_nvMUIn6VHMUMO6riC1JGA08Y-KmiV8ZBEQ8nOWwYwhoPnAqjLhBfiHrY2-L-eoJo1LNvVPB9rQvsTI8LsP4A43Kn9pFShhV4yJ06_996OAi_SB9zHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyQ5ucjluxBWi59VuqCxakAzGOWPnZ_kBJKzOgCorTEO97OjbeePDUNqsU4HDE4kdwDko1IF5XIEfuvTY3GZWtEECpPYiRgQzbNv5QK2nBWDM40mvEI2fMPqC45UYQ2-e1kEk-wDljCGA5An3qhtgHNODLF7U77SC4PTgriO5mTBBjoQKw260svWGUKcUUogDXr5v5KpiWcybh5uncwlDVRLqVhUiZJkBHqeJBVolTCvomqexBXxFbNEXa1aULbgLoahJ4eWmxBUXNfKdIrfbEjnyntzqbqUKlCJWo5FI5Ehaohcw7CoDNTNFwXJGlnbL7LbJvgFadR8fpbVOmjh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB4nLMyq-tGrY2xJB1M4PMq5phyl7FEpVO7z1SxpmB2uFvBpuQX04xdJf9k9CkrZgwlNBW5Wg9ymoyQcRLG7gRUsHcsYcMRGQg_RKFqL4KE5X3KD9KOMQcQvhCrvhgRG98TkB-X0460ZZMaZscOlqAwgGLeCaFdgVctGv0RvrBRKLGqS2we7_4QpVdTRYe4zVP1IQk2VcBHURmSBxTrvl3P1kaqsfXl2EuRi_7PlaexltVSZlB5JWM3ArOoXXDxGdKWjbTHMA1irxPFZuzSk8uBfiRNYqVK-KaAx9MRFwLW5xyxx0RrhXSNfGGx5U-inu4jFWLMKpeJ-1J7P0jlHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzO0sHdLCPTm-0zoKJ27EhAvdZFTTU8vo56_izrOnmqf2dSOowH5SDgE1AqWLwV6nDsIV12domhCtiuP4WXghoJk4i58dIX7X29_VQh5AH1wmELAJX238OG9YAOnhQ2n36uiZmWUgXSlwReOEORMDzf3Sk6hXsgxQZc5KHl-QSSUaOh92zYDyEXQuyHDCxcmRwKyPf8bMfYnVw2NVUFSnSVkIpwd2-4H2YYz1pg-2ddGo1wOsS9ltz3jEbobT1nwqpVJl7Ne9UI0XeiQLM0AjFVXelcJJsXAuTvw4GOOBKCdFBZniRYjBi-sbfMkyz_sT8mKFDzzEWFqe77EbDVqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfwiVBMe2EVFYdzGY46A_8XXene1xpxRzS83K-nf5ts2wnSkOKr0lAN2byaIx2g6PdUJ7j9Re-Z6D_f0vQiju8IKfuHXN1Jn5E12vQRDYXwXxGWxtTAiRRGNrABOzxJK7wSOnBQUyK5Bupdy_0arCsa9IfxiH9rdg6ZAn-GwaTt_vKnBlqO9yEuoRr1k8oQgrukwSMvcgQsJ4wOsYVp_XoK-DaI-7A1kpPjVGYYLlFWdW0TF38kTh6_jILQVPK_ZCiS36gOZghvV6XmHyGVt8NhsqD3Nsxx0WRBJZ3NAp6HafbjelsOLl-jLKfPQWjfqzcG5Tezqa8twDY2anaROyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKxEBAS_5ichLcNLmxdE7Wbc5o9ftTnzN1FaGkyxaIs4vvHl4Rsh8cA8urPgtL5le7EbLcehwxEWH3XB3JGksf6wQyJwYP3RYv7DTfFbxoq_yT_94XjgsPF-h7DeYD6foQfE9lkQ-qz_cFQW4o5Gq-A77VEsFMQXBPy4VsTMA4ZtK6rQLJRZla-48GJbcpjGMpyaNIClKF4zQBpvlqpWkg9PUTOjFLvNWuEEAQRLMlIKuy-7f-7km1WFibJSOdAb41Gxg_plOH9TXBTk_QcRdqcTuUFBov5OwyIfsBVBYHSohr5pSkwl_urr-ta6JNY-gsqtYUYbXMC42FDE5RHiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNsCnzUKYyWJEpytetB14pzwCmRQ2mTZVNT-g8OAPscOG-JtICMCcytprjI3ygNx59nQuHxH5DAKtLP1mdOjLz9M2MMxQE58wVO3yNcXXQJ5NQPJKjAJv-RF5ye0OozapwEwHGMsYwF4xsU6UnJZdRMeMHRLIBgzkPq2cnuKO-n_nAAioKSHKq4u7srcLWWlrw7JgYvfE4agMLzjU7mnjzF4atyCtPjrDSwIDcT5lKL0M_nn93zB1M7b0cYnuy028Tv0WWtTiw_l9GJu_3-bS-M4WZ8mNdqbJoYBuVwxG-g6zoU7VvapS02tjl0voZedeBhfamndXxCUp9lZ6jeS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frECECBTk1LYUnXUGXgoQgacnfWq1tYkIKSmPzeqVkXMhNR-S3aeOw1_UXwbjTNel_xpdu8IdeA8xeo308F8lHmFDUUzJ2VOmReARUvJgerGZqAWvojKp-sVLyDSdD-Uq7MB4QVqZXfdE6uJFRv5BEzzPZzuduD4Z45vhXFcMMR8igA7FfVi_b2r09Q-XdMtTe8ZahiWJHCzN9IqWg3h7fqlYeVqXmS2i1JoUoPb9olCfRiQNk-PrOem1Dw4H3dChvm7nNLyitnFfSe2hSkv1m6uHnOrewY_C0MjT4rlUsnE_TyaDnZ487V1xseOHYU6y_sTkbCPXTtzskoEXKB7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6tNQGUF5MpDU34S09NEx2yJA3TZRzpEojHDRHKK4bHH8HY09WnbZ_esNvK99Jr7mec6aEx1Bf4P6LpdA1aGQxHJsLoY5KDhDkPqUxFjmDY7BPa4FfgnNVYhDjfeoYoDaHCmwBTu4vlZ5X0KN0clxRPqOi0UJu2fMlGrHdhw4__Ce3FACf7wv-py-eQauWmqEL6g492s605k94sbQ-AWGhPntGzy03kUPyvvMX3IUL09K3fRDhoeqdn2X-0-nqAO0-xcXo7gZ5e_PxcLPzcf9KjdWINaOR0PYOgWln5WU0WsMIEZtQYC2qQTyrHJ5Me84keqm4hE5aFa916UnXMlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=JZv52I6wZZFUB4Hei_4-ahkbZX8M2BYm5bI0_g7I1lPXvnmAeUiF0rfooUu632CUT0VFeaMs-RGqi_kDyDQ4dZziFO8M7HOMh3tsns_fCSRygobni4WW9QyhAfjvMEcQmC5rkJdH4fnu1aFcu48zBQLVtHeI6TZpUnmetms2k2jUhI5lrRg5-4iHIxIhrxAQabYOr5X-nMSH5agsLkUVsGS3HWtBdtIuYlLFcFI74P4eoTxqpJQjmMBmGFu0rX2gm4B-MKad5jdhEB-T99RqJef97TWv0a5U3r52_dvqyORiNt0QDGYh1tr_OHAMAfCYHDaETGJlmliVxQwS5YOZCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=JZv52I6wZZFUB4Hei_4-ahkbZX8M2BYm5bI0_g7I1lPXvnmAeUiF0rfooUu632CUT0VFeaMs-RGqi_kDyDQ4dZziFO8M7HOMh3tsns_fCSRygobni4WW9QyhAfjvMEcQmC5rkJdH4fnu1aFcu48zBQLVtHeI6TZpUnmetms2k2jUhI5lrRg5-4iHIxIhrxAQabYOr5X-nMSH5agsLkUVsGS3HWtBdtIuYlLFcFI74P4eoTxqpJQjmMBmGFu0rX2gm4B-MKad5jdhEB-T99RqJef97TWv0a5U3r52_dvqyORiNt0QDGYh1tr_OHAMAfCYHDaETGJlmliVxQwS5YOZCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW6x89aYFA4imt57_HmPQZDD-JysklotFLQDpluUJvogXgkyJiqfAkQLZkO-gja09WlNcycLl5WP_XwLfSHxk4H0m6bmHhDLe3i90Hnhsb0uKkA17sd6PB4HUoBgozsnMEogolitHg-ZjdOFgSWhp-M_DLRicGI_v41p9bevgNn7yFwb9IyixpjzNlGrChP9wp3bmuRPcQnE6ofruPs42ofXDipJ6mhPwNj3gR5l1TVv_Hggs87KAX7JhEhf_531VVLodFIpY0j4UXcSYAmq1CzfqaBQkRHb99cAVup2VIhfzMR-fNJThHUzOeqLydwWKwnoigMmX_h1d6EzxHqa6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUz8TdzqV_3ljvbGzOysHDa7jBX5xieN217UcYHg1eQNWaYBu-4gxGmr-jvzH9i14XWEee4jO7X-Rk-ZVhyLdCPxiFAHCzOJwnRm9ipCOWT3Jy8AH7MQOR8OE-ZeG50mcLOzAnLYRzb_Nb0y6H-EmVhbxO0d_yZx0U0lJwGR3IwdpgIYZQyoi1Gviutx3AZplpxd6ZYx04cQKYPvwzdubmMOyRom8M7PPRdFzUC3aplLkX6aVXz68fCX810Et-XK9_XYvDOLuWe8rT9bD_FvNA43uhrFARuzYUXQVkYsuOYNrwcE9nEDOvj_68QBX9jOwNjVHO58crLABls_THHCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNcCbjiXQSUQPssHIEl5BmU73fDPjyK8vudNZAwjYxyIQonoUFqhY1LskRl_Iq6F7ZjZ_1wy0m-97u2la3XBOuGYkDXuPOnKVTkeBKgOuKlC99ZsUfn88lHu0MA8jADyazc3FQkJF4qSIQwXIMjJS_Fap-86G8avns6lsRgQmZLZ4AJHXuXFGzsLdgMGrad5nvla1Ejaw92hcZ9Z3vxH0G3_5IdWpAHOXRWSYJ1ZTODOuRsVCRC-W8s_hZyz29JwsJqsguKwb4-5kchiVR2riCiF26iUpxtiQT9zxqrXDX7VDBbslBGlSPljZh5NX3S6f3sPr7j3jRzjsCrDNVl8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jbsG7XzPXaJVoaDbDw96f_HV4AE5It2mvpXOmv8faoasQhiby1neiRhDDBHU9ZNJSxdP9tyIZJdbwDauNdyEhRblgCbdCo1ZC07yRds5ut7hn4OOWbZ_UfqdRjdy3UYm3FMeeXMmoQyEAdR5YuCflfwyzAC0lFU7mUHtqJy5-Vx1CWOF5RnuKVJDOBASCgoRgJ-ACkWTGu9nIqD5MIY2ciKNf_50KinsF3TuKdTL2U2K_DYxwvtxbHMjm5sjMM6g-hAp5Z_xAWOECuyPoloxVGEzow3-A6XSyovORMM5oUnztTS5pRUDoRLFo8mdhZSmDP5_amwJR8LyUOTh1LH1Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jbsG7XzPXaJVoaDbDw96f_HV4AE5It2mvpXOmv8faoasQhiby1neiRhDDBHU9ZNJSxdP9tyIZJdbwDauNdyEhRblgCbdCo1ZC07yRds5ut7hn4OOWbZ_UfqdRjdy3UYm3FMeeXMmoQyEAdR5YuCflfwyzAC0lFU7mUHtqJy5-Vx1CWOF5RnuKVJDOBASCgoRgJ-ACkWTGu9nIqD5MIY2ciKNf_50KinsF3TuKdTL2U2K_DYxwvtxbHMjm5sjMM6g-hAp5Z_xAWOECuyPoloxVGEzow3-A6XSyovORMM5oUnztTS5pRUDoRLFo8mdhZSmDP5_amwJR8LyUOTh1LH1Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIM6DmqX6SBt3FDVDCAOfCq_-Hu6p1imwe6pFROh2-0JynxzwbE_WwqitEFIgre42Q-oTex0CWGYBkcwiNPSBNOz9Hpk-udSVq5ke98DQdZa2ApyPFloSpyYLVSdcCFhXd1gakqWJnXFiDTXtCW3KE1uvH7s4M3iNlUUxgGCvn1wnkq1tKx6IJKE-CTKi6FcRE5DmatPvAH57Zad9DYP1fb9QCYeggbS5wNBQSavs5VK_vHSjp0fVTIUxyIXNGyhffJIc-H9LzM35klmo5_oWAWolsyXr6W1jm8-5hJcMNzzORn7kNNVlCv1I7kbh1IFewMVuf3cW5x68p8Mx98Oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOq2JNs8eSg2_E6gpS3GjeCtkRI13azy4bjgUwah_eG_DcKwYpinxY3rKWt-fsnUQb8tsubf2394PqpPEhsbG3X3nyuVtXbGLGvGGlqf8i6Foid12V92AAWeHkynZLe7_xV2YRkHTAvo5cfBZczhIWrwL6TJy6ZH8SigJNvGjZNkP_qIoJquqxKjyAsBtIxtQNI_zxla2GRPOMJ-GOoFcqBwMNuSqPZ-kkkS6a7IxtgZ1ZEgiuFQa2tTPopaybTop0Xkj1VwKPe_-3J72jZpnIqY4wNQHSemKpInRkqPGdfy4sP-uxYKNH0TXfovFIcYEthGrYuHdkmurwUgt4jULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW23PRRngvuItsyPTTc4xLpi4ykpWLh2tI3wRYOjToW709-9Rt9xK9vOSUUdlkD0Q0J0TOWJbjEdOe8tp2rH816hBNkXHG4YXCRESL8J6Xpx0cj7k3sWS4ytRelQFfXs0VW5smQ6tXSsGLtJrUtZTK3E6K1Tus_IFoLRNdG00kgNdb-JlMDAkZULjvWW4x5OrR2gvWyuHvwDb2u4WrVg-DxkY97WbG3JNyYT4HM7OMAdP-G5lIkwjjYM5kOUhxXYrCjWCpDVlaxpk2CVIwskxPUg7TK5GhK7yUFHYI4OpUL2y86b0ObAzQzY0EQAWtDTzwFaFWUMn3s9Hf1CvyE_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=dhjS1I2GDFdHcPyn57j6r6bLPI3oEAUAIA5GgtZRfcCND5u0ShbDlTpo3SrAxgUoCFNQz7BYQQeucVWxDpTD0BQxPO_u_qoJ5MVxV0Ps-H06pZnNm0U81VXnshO86Eh5YHumVHMe6av_i6grnZai3gYv1AYgkbwXXgnYK9zOFw48BjzpBeUQQ6XGgnOzXsgNMmhp3ahpK6kfe8i85FMX8M7L3H4wZirI-MGUixJsAiVj9o6IqGSo0hu5OcjmH3skuBNTYR16TiKM4YL_Xpvp6C2iybIEwsnMV9dqVAyaIambuEDgGsjrPjxIF1lA0NgJMc3TNJukhDsQO38LIO67sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=dhjS1I2GDFdHcPyn57j6r6bLPI3oEAUAIA5GgtZRfcCND5u0ShbDlTpo3SrAxgUoCFNQz7BYQQeucVWxDpTD0BQxPO_u_qoJ5MVxV0Ps-H06pZnNm0U81VXnshO86Eh5YHumVHMe6av_i6grnZai3gYv1AYgkbwXXgnYK9zOFw48BjzpBeUQQ6XGgnOzXsgNMmhp3ahpK6kfe8i85FMX8M7L3H4wZirI-MGUixJsAiVj9o6IqGSo0hu5OcjmH3skuBNTYR16TiKM4YL_Xpvp6C2iybIEwsnMV9dqVAyaIambuEDgGsjrPjxIF1lA0NgJMc3TNJukhDsQO38LIO67sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG_9_kvwyfYb7yfb6KDHDhuguag9xthBUDExsaKEuEdekiZRBJo5STwbXxBd1je_4UwreK0cYPX1cWvCDBcZpVDUz4CccFArxtUn6Bi0Qw2P3KaNnnd80Bct-uxx-YINAETCZldjg-VfdGB_Jmh63NTB9JxtEYAum_x604N_93Mw9Ik7vQ_kfxfEdo3A30L53RefTEW3oQ1vxlZHpnrawpsXBuXZywkQB7yfjHPY5-Tx-5tbjivdtXJmkv_kpSgsqbz76mJWPc1kY2igp5Yahhbl7xM2zT3rNZ_cHoMCYMDqv8Pjap4j6qElLoAqRwAqOhhjyJjOCS_5qtGNqd6FKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=dUosBqHL-gZ-4iVVD5ny5dFQtVCtwZuUAkOLvgghnr8Vn0b65HZT8PIKw9hTyF2mB57BU0ry7frCgQ-M-nzlZnGP869kGFNEonIcolHPHtfPvySUi1Ircac34OMznq5ADMT20Nw5SIOtT1yxEa_uxkT0-1YcOdbIYb_G-4scwTkajKCIxOGtxKdx0MVjSTPY31pK5bdP0vL1KiaGWoFH5La1pZFBxsKyMO2Mnf6BBey0zKoJR51KRusLFtEzRLiScJKlhZoHYWhDP-8xzxQEdlcneLwyhumyo1WsGOJci25F5uSyGez69k7C0zTOUyu0KBdyAXC1wIHLxUren2UdqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=dUosBqHL-gZ-4iVVD5ny5dFQtVCtwZuUAkOLvgghnr8Vn0b65HZT8PIKw9hTyF2mB57BU0ry7frCgQ-M-nzlZnGP869kGFNEonIcolHPHtfPvySUi1Ircac34OMznq5ADMT20Nw5SIOtT1yxEa_uxkT0-1YcOdbIYb_G-4scwTkajKCIxOGtxKdx0MVjSTPY31pK5bdP0vL1KiaGWoFH5La1pZFBxsKyMO2Mnf6BBey0zKoJR51KRusLFtEzRLiScJKlhZoHYWhDP-8xzxQEdlcneLwyhumyo1WsGOJci25F5uSyGez69k7C0zTOUyu0KBdyAXC1wIHLxUren2UdqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATZmHBM0fQSWFlWmuYEw_V55WeJBlTa-D1NLrjy47KbOI8K-tX7H_Lmd5xQFmlfCVD37CsaOVfvXvJJaCnjIzSjjC586PAxRt9-mbD8_z-MW3st4tKVQWr-b6NhaVV0vzH6DNmaW8xG7fPyHIo9rp0wbpcCip-vPiDHFp6503s_S5YbhXHitQNpL35HooGUyAsblDMx6HKzbKUAIQAj6cHu2QQpmU33yQS0flETfqsTb3duze1dSexn0KYrlpnLFvtw9fAD0Z-AcGppHW5oCEYSllNhgsdnw7j4GeTekwQUxZH7NAz5F-Im6bh7wU_YDsoYGaKAvm0woU4BjcI8FEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Deffa2CeIb1V-TvX4FDlZjnLDPJRcWh7W1udBKwnB9od7LCdm2Hb1snemovMO1sYK39wcnH3Kl5F80dlDh8ixRL3PF5CqJ6Ohg0oJlVIbvOjtfJD0hrHChdmPWewpWvp3FVmi1JhrLkkQmpsdhmMO-8Q0MIqyVZwmwqtcYiFbq9eC2CiJa_hSbOEsGKpbVoVAnf7Mj6Lw6fVZPjwfWYs1RMTQNl0dEJ88c7t1MnK_lQlVDDHgNtHPpPmLYkzlTWeQuGS5YelFPnfY9SAznexJ-uy8OvjfkXc0f-kzhDxxJriLKG-RG0B8fuKKi2VsBONa5WAXlkD2BlPMkXSbjM7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=Nx4a2JN_XcezHefDqUE7iAoHXWQpuMmWwcrP3rVYIA1l_omGyP5QTRTKu3SzMeilphUdCZba1aaEQEHmxEhe_j7MguczsLEXUoEqAQmipuAl0Wj2qzn_X8o1tCc-9-IMaL519vTyt2gjeisnVlOmNNpKKtnrceOmdKtdvRJkJZLu4Hs9-W-V3cp0vB3RPc0-rI-Z-DeqBSTEp72SgaNRMpMd46TNtjDtamfRsg9Lv--W893_c8WQ1mhn085vw1btXNd-l0Nvh0jgVVG7XdBevpD7frvOvzhTRKi_8qB3qdoJbSfmqGjFMEfgtu5UVOItHLtOaqT7gBUnmReCntJ8g41N8gGtD0sJS8czMvRL_tidMvqHX6rdAB7vKONMI_Qv_j7R5DalJyLMX0ywMg5etrRiiAuBt9dn5wHecNYCwuNFWQJJGtNUuHsxqMoS727Hniuji7Us8wMd3cU5oAWBz1NavqFFjsymsgELq-rLbOUnqXcWO79RJ3NmQ9kICZ2hmNN4oj8fRBHk1rVz5os1EB8eHyzsAVn33J8EknByXZMPtQU-04SBtCncgQMOZhginel91qc4PgdfkSj1usvg3gTBk2YbiwsQ3cOUc3wbP6fdwx2Q-t6wgSMSJq5kCvnF2YboYC6kX6JvPGBtqLrok8o207JzzhDQ8xJcYTxmJMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=Nx4a2JN_XcezHefDqUE7iAoHXWQpuMmWwcrP3rVYIA1l_omGyP5QTRTKu3SzMeilphUdCZba1aaEQEHmxEhe_j7MguczsLEXUoEqAQmipuAl0Wj2qzn_X8o1tCc-9-IMaL519vTyt2gjeisnVlOmNNpKKtnrceOmdKtdvRJkJZLu4Hs9-W-V3cp0vB3RPc0-rI-Z-DeqBSTEp72SgaNRMpMd46TNtjDtamfRsg9Lv--W893_c8WQ1mhn085vw1btXNd-l0Nvh0jgVVG7XdBevpD7frvOvzhTRKi_8qB3qdoJbSfmqGjFMEfgtu5UVOItHLtOaqT7gBUnmReCntJ8g41N8gGtD0sJS8czMvRL_tidMvqHX6rdAB7vKONMI_Qv_j7R5DalJyLMX0ywMg5etrRiiAuBt9dn5wHecNYCwuNFWQJJGtNUuHsxqMoS727Hniuji7Us8wMd3cU5oAWBz1NavqFFjsymsgELq-rLbOUnqXcWO79RJ3NmQ9kICZ2hmNN4oj8fRBHk1rVz5os1EB8eHyzsAVn33J8EknByXZMPtQU-04SBtCncgQMOZhginel91qc4PgdfkSj1usvg3gTBk2YbiwsQ3cOUc3wbP6fdwx2Q-t6wgSMSJq5kCvnF2YboYC6kX6JvPGBtqLrok8o207JzzhDQ8xJcYTxmJMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=CAz9qdr3HXtt1NYOyp33_1V-IijH8zW7TmUbc-wBOVIjfHUD00YcUAHMmHF53uDwB4b5fhfeN4iJxNDbeIGf6C5LWj7gld6oyHNbVBa36f-t3qgaWHOYbSYttNC1b4CIBzItuVdELys4RARfCYPtsW6shneUYrNePRx5-2-JSUFogU0sqqJdS6LjvwXEDbSUt5cV6lhYHSlkCLa10KAQ7mh7inM3BQwtZvGdmDyKAektyUSwwZx2zd5HqBEdG7WfstDfpTAjNBQ5KTChhyUhtc56WRpAJi_BuSEUjw1bze01wsmjMVIMj29ZP8xJaW589Gd-EFq7UbdJoRsv1LGnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=CAz9qdr3HXtt1NYOyp33_1V-IijH8zW7TmUbc-wBOVIjfHUD00YcUAHMmHF53uDwB4b5fhfeN4iJxNDbeIGf6C5LWj7gld6oyHNbVBa36f-t3qgaWHOYbSYttNC1b4CIBzItuVdELys4RARfCYPtsW6shneUYrNePRx5-2-JSUFogU0sqqJdS6LjvwXEDbSUt5cV6lhYHSlkCLa10KAQ7mh7inM3BQwtZvGdmDyKAektyUSwwZx2zd5HqBEdG7WfstDfpTAjNBQ5KTChhyUhtc56WRpAJi_BuSEUjw1bze01wsmjMVIMj29ZP8xJaW589Gd-EFq7UbdJoRsv1LGnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5l3keg_7cnj7S-qCgIIaldVufoTGZ0Ad0rX0KeqD1zjvVcSfmod6FonskDH2Yvm-ZZrXe8BWBv2be5Y-bIMEjqeso1PkKbk33p6OP22fnmfwNfUEID1dlJENIXiz5FwfahAvfFVzYG3IOKLmA0DaTLxPeLWov9vt202b2qXTPVMJoHJPYNCCaYFzxNrHVnIxLX_8g8AOiPLwacdFKPtO0As49eQINFM5qAs5NTQKR1lK3ZvdW0Ily3-YPKIplKi-GLUl8uYCIxOycDtJimklVmvdV5qljYEkRETiORysvSbKFgYqOt6qPkWqT1CA5nA4lI_TcHKdLZ6ltCRu3ZE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ngfz3_YyeeL3dXbfZeq_2pAXdAQKFLKPUjOtQ0e1sxYaUcjJNQ7DaH60AFFKziDtB0sVsavhojZ-A1qv39IypWZ-DHVBFA_eawa5OkvByQrPWZbmOv74fLQOTXwmPHDZ4ZTsPPvCRCgF8cWGhpQks8WbEXiOQTmxjgKz0CtIXChO9jfCgnqpbyjyFri8BgSBns_b8hXgN8fY5CdDShHYWeYXdwCQvN_rOBdq9Khi722sqU0i-vFmGeMleLwlPFrg_DKR8ols4nIXv1MVBIxZzKgpFF9tE6WzuyJI3xokEYHE7vAS1LwAOA7yaVyTaNY7vK2pe6xo15K4UBF1e7_V9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaZ8m2P3PrqMC8flhQlkKoJRISxNhv-Uvjl28qXIC87HUGkC-UuWxjZJ9MjyV_aCIPmQaaNRP3jaL-M8PentQ7gP1b0wq8zg3NEr5qf6gToYrp3T5eRk5BMQpcO5yFZ9wIqITlYgF-UMnMn_Ozc5kIDDgz4qrQxAHEM7pWExHPL4AGQTH4F-yVyM2QHCTfGPCxMyeg7p_GnQc1jluil_9YL1IZuqNex8N2AhDgakIE07UnYVoP-wMvtAsu_cmz_pjRKS1OQDG4LKpBPaJoEfa11H6v83w2TObUM4J5oHbfSfMiS_t0bB8rZKbOoWFupBXUzFykngmkqa-z6E987IPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS5l8Zm-I7hMg1KA1aV_CSIL6CCQ0V2re_D1SOUe4X-40CsqMxLYnokuXsknqIvuSwHS4ZcEg0uBUWAre2f66u4A5geKm8_9IExHeaB3afNRuffsbGiv1aFsFeEi92wNYd7SEYYNKOLbNyRWyeu9TOw1DYy1sarW9hb-S_Sf9NgJhR5MMKL_IDuwuvtRvHfDldbONgMDrrveRqBmfDLwQA2OL4N0ROB0aMDqd0bEpkdDUKNEgIwhJHjRMRY3uWJtGoQxv1VJ6AAaVlF9txC_ZziUs8Cpie4nXOXXqRPynw79vcDNSqikpW3WfCBmVen5tDv_Z7uEwT8QzCmaECqHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGMGiUaDIhFxw5wDwyJpYAQzftoM85OxBaukyd7aPp_uV6W54PD83BaOXo4eN08ioa4s8ywcOCNZBLMeG_Z-Tvd8NuQ8aUrfKbX8ay1uN5BIhM24cPMHr1zSdwRzEDkNuaH1ypPJKSJYl6p5qytw0IXgOzuFbiJ7rX_CqEDk1x0gJV418P96XIuvPJ5sxZ842TYLGiu_2mME4ZJ9BgViZLa_GhZLpm4I3okIgDPAdZIiwv8yiz2aE20L47gaZn45ryzCh_PV2bNQheMbeGLV8_dXkzxARIcNxhsSr_AIWDE1Rrdg2csMIZ8t6UQ1dEZaYQcH5cC8-1iZdhOZQi80zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_JXPZE56CnMWhMDyufE8vsqxgOfJ4nibq9-UwsGQJlp0jmVO07CllUcOP7ktzdsHN7wXiDnhD3n-cpvQ0cT_cfdzyBpq660dgSDGfBTs-FhxErH7d78TmSv0dw2qZq1-MGHvIUG0O0IwaweEWSgMJsZ8_39vO1SiRkQiKrdNCYPgh-co7XoJv9_7x1Kcvsrhxo-oJe-foAtpyME4_cKNan_OIukwWuewIwBhMUzHqF8HY9Uz5raz3-NDKy_ZWue1KDwZnOTRnBIY5KJXMjsDAPQLIO6u6sRrbLgnIN_OsgawPq3zZl1r7HLwljR3q2rFSOrMmnBEdQ_IOIcqjCWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSh87wdhpfad3ttwA5wt7yTH-mfx75IJYugClMK-e9yr9CziLJ6K3MYBr0kMPard4S9a1Kfm6kfL1aWY8tLe37tVnrJVZOKeWzuEom2IXl6D1-a-ZoRne8J8ZFg5S466ceaqb8Z9XBMWG0n7ShoRtkBmoqLZOS6_iEDhFMmjPztvvKR1kF-iMW4_L_r9qho-gWLI-0sg5z5bWsY9PnPSYZ_8ya47n7jw5oZO9pe2TcHYfSXwqECyhYCJtyG-qO8A4EAJR5uO5T7VrEiNC-_-lfzm1oEtHpUOIChkhe4qSKI82lu7_Z_hClJBWFRu9sQfgSiIteiobnZOQBqvLk-i3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El3y9_LGen3WNDNN5oT0WiF8ZIo7q_tHlAo68wGoMOnqcOl4-PSIatjKby-E5-TfuUMrsUIDx5rYk_YCx8QxTr5-aayxSvh4zO8jRvGeS_m9ZaO88y0gm__ctCGWOQ1ZZW8FTHLwVYHrxdcyhL1T-XIF-R0uFnDkAm9Su3W4JIgk1eiZO8jcr5TkdqLVUZluXVtq7zfdpS9rJIYENGfrf9xJ1Xev3Rt-oTR48LszE6e2If3nwQTf_XyP1XGGJWbI6XKqTHzlRZr1HQItvRM-gZrMsG1zmKU0adUd0_llsu3yems3be0s0ArVlWfy85GcbBPjtx_3jkrXu_TI7GqqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul0oHkQ1LRDwq3bN1Sj_OnMrZ1lsF50_XHqwTH2E22-YpzK7Sryq8iwNwgr3Qio6QEtA1uTz88QM7Z1pbJDCWU1Ew8-pUjx2lJxBmKNcXpdi-cV8WmFs87Zk0-64D0ankahIrVfjHn9i2oYAfyPxoxeOZVfipvZVBElHmLSz5Qc3kZnyztl3DEB0_n5_0ODzz3tIV72zgy2BL6oUilVAdiPJAHy0uoCNKMHLcspeW1W-IECJQfctWXXN-HYVnoSx7c3Qy5mHVUwcWTj0VMK2gY4tL9VZxwyD44wB95VPoRfTc0gwW57BPXkZrYljP1dAQOag_kSU3g4f4hJh3-mx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwMAfiLY0MGCidjXIGmEa_ofApeh2seKvPEv3h5218nJXzADztwwFszZOJK3gfoa-tndOsJIHoczNGAEIO8Kmso-0ftYvC1-np5KOYZwvcemaHINW-aLjWUFi6jIcyzWtm3kWe1tWSH3vB4xqHcpMejZit8nEUV4GpRr-qUSHmyf_vVcQ3Qx7y3SHIoj4g3Rbm7SLcB6QQiHXozo4zGemTYo5ac8fM8sC9l97N73-8kSGcQf1xDCsFTV38XixmxNyiM7d0GqQLxrwZttcXgDgtV4thJZFAIQk3gGHpvM5nwudH-meLtHQ1HKPhk7hxpYGrJX9sQONg9Kg3jBBagFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdOOxhNGNVXvm_ji3DhvBUhgc2Ac6iJZ-gm2aemMQqmX6Xvd_1z2azTviIK9bercUJBnKuHqKWhqZl_VDyZ0mfxwa_nxU4simk8vS1Z-8YePGPz-m2Tfvxj-3ftQ28iwhPcOE7D4EVF78y7z50Jxjqyem8fQN24OsQh5H75rhopWh2yT88BDCpdt1KtIz-40WvDVbg5c_iRuCdz2I3yt6N1EFafMvFPFHOHzm7h--J1j4Z3DgvHXidThiCgtn8ZVRSGmZbLFgn8A6oyWXvtLL_Rh2vshILJ6Zoj_WSdxt1WnRsoYpoaxhQ4TfIamy3-lkjfXxhzmfLiB1LO8ZPRxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=KrozEzo041vCE4-BVxJ8aurnpL_VQ-RxP8yt75FEdgzIf1WSW4vvo6c7H2kKhp4CwH-b09YGGOqy81I8eMiOvHzwmR5SW5yA-zu3mXabBvItesiYEdt_4eq3IrdjD0BrVjHKe5IfQONH5gtPaZp-AOiyUchH2ViocGbvWLG4yiFG9ATrSFNWgnR0gtx7NTL--ftw1XI3VduilyU1pu5dGGtH7GzQOmFWLCtRyvMwLhWeEa0qXCcq5tkqmEMkvuHTwQcqfM3Th1OXmbCclB37VQrkUqYPA_NIfm7cAEQHNSvxMoT3K4QeU59HVQITHKrmSeMD82X8Fosa0yHwABtpBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=KrozEzo041vCE4-BVxJ8aurnpL_VQ-RxP8yt75FEdgzIf1WSW4vvo6c7H2kKhp4CwH-b09YGGOqy81I8eMiOvHzwmR5SW5yA-zu3mXabBvItesiYEdt_4eq3IrdjD0BrVjHKe5IfQONH5gtPaZp-AOiyUchH2ViocGbvWLG4yiFG9ATrSFNWgnR0gtx7NTL--ftw1XI3VduilyU1pu5dGGtH7GzQOmFWLCtRyvMwLhWeEa0qXCcq5tkqmEMkvuHTwQcqfM3Th1OXmbCclB37VQrkUqYPA_NIfm7cAEQHNSvxMoT3K4QeU59HVQITHKrmSeMD82X8Fosa0yHwABtpBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXAZGy5DJHWjZtWbOM7K8IHNwFM4nefln7O0UQbNi895CLLmgBBMboMliTwXJ9rTL0VoqapZENyfG1klKVOdTzW6JHerNXblL1ac_IkiRC5drWeAtBmbJs_mm29vwHZ3ARw6_KqDRF6ABqC5Jn0YuhcS4KM0ZbxZTQvSdKcU39XvCCnNDJSGaStpMWBtWLZtbJekPYJF6oKgokvXTdetN2XsR1jEkoSKa0wPOLvM_-ISKLWKcFOWQ8AP4vpjn1OuWRZYtL3TMyAd8khAZRIxkjISk3bknL5cpdGhF34ozBPzVL2yDnzITs49FobHDYvp4LO11emyfKxPMNZzvIX0WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLQZcU5SVi_KIIczJs-6eTY1S_sL2FIwP3DmgRffw_qngZKljN0xXhmdN_tRtm_0AUPemiMkscM7tgas1A0sjlyphhzMSBSqLMVVcS7zkKO-IfOZbkoTZUPcQg9fKMALUAaGQAVAu-scRhOId1EcJ9KmnAClEmBWcowIyDcm0JLo2rW-vuEuy6FWwer49Yb2ywPj5ZGb4p2J0LiR8ySaSLRoZaPJv7EG0_W6fP9LiVpZisWogbP5M4_1GsAeHPpIYtDap31V2ouNW1jetv814-x6hrj-m76F-6u7jjVn5Wu6fsn_Z8ykx69sc14YvYbIn3rL5P346eTlKkoX-nXNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czo4d1FgpaW_a3Dc0whey0fnpoyedSAe8_qPufGf1QspgWyzqdOIjnGP8tzgYwXYlK4EP6N6A3aeuFaQam5lQkNcC-bqGzmI07igChii4cK2NkXPAzW3r31aIxAgos8vGSkxonqtD639Ryw7gRtIOQ0TeoFew4begkZkJ6F8T_jZMyaXoRAodviQhU26XZsArGIo6AuV1XOwJQxD7SPp0z6Z_ziiXAm7tbLAbW3DLF3s97qD0S80XQPoJmO-PeAPaSEQzjDDxezfScq8FGBXZEH4CWaZF466V_KWEGWAwx3b5KcMNRgRki0bcBpdCCaAoq_g9H6Cvnf0YZXu-ju-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=TFCL8X3kyZlBGrqzoEtZLBfvqviITSx2b5J6VUrljRQk5POR0lGYiUkyv1ciD6_H6UsbHe-OHfOy72MprOvPL7v2Gn2MJ7en59Fn734LgioopsHkhl6aKGmHtEMHNdAMs2xEPX4fVryPOQuOPlg3Y3Aa_Ndtu2c2g3Wc4gcVRCQxDZPr69BYfYsLvex6b8mcAUnwG-HcEHeMKi_Bfxtf9jBUTnqSLht4WqezVecAEf4_OVj2rLJ7DbfyLouwwQFfr1svB6EAFpLrldo6eiwbNgscRdjnrtWbwUyRBlBWqSyBDvO00t0d2XkjZ4MayQpm_jY1PItHu17JVHmXG-K_JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=TFCL8X3kyZlBGrqzoEtZLBfvqviITSx2b5J6VUrljRQk5POR0lGYiUkyv1ciD6_H6UsbHe-OHfOy72MprOvPL7v2Gn2MJ7en59Fn734LgioopsHkhl6aKGmHtEMHNdAMs2xEPX4fVryPOQuOPlg3Y3Aa_Ndtu2c2g3Wc4gcVRCQxDZPr69BYfYsLvex6b8mcAUnwG-HcEHeMKi_Bfxtf9jBUTnqSLht4WqezVecAEf4_OVj2rLJ7DbfyLouwwQFfr1svB6EAFpLrldo6eiwbNgscRdjnrtWbwUyRBlBWqSyBDvO00t0d2XkjZ4MayQpm_jY1PItHu17JVHmXG-K_JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRvEd7N_j0jc4uMRFLIpKl3eX2zDm3DvZ9xtsRuwIDXwKhezmhh5F2r9DXjD9-n_qESSoDz5B_exeo0WoxHMzNkzWiqb7QJQVl4xf1Y886ZW9f7QuvUV1cefZluZiYpTEuMzjSTXjp-uJg7d8DnN6yCag4d8TgyaKUIljphrzxiyC5HcF6EcDtJEk_h5jcMHYiibYVYd1HFEmMTwk64IGS2Jc2RttelnmB0n7N42hPgn-VjRc_qcbLB3IVEmutqAos6J5D6CXVCJukaTfVdZbteXQ1Qopf4JXQxZSXV38ODXfpuADzZ75PHgsmojbHsAlC4dNEDeIDf4Mp6i0el_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpskFG1uMrzCLZDWtWmwVgxG0refQnFWM9l3G6xO1aoFeIZ7DeIBBMPV2VFIs1s4BP5Eqwa6obXyvPlYxs3GwpIxEZYrI4hGFyUXx4JpUbqgp0AhnpRcZFBtQnPHS6s2p1IDvVGJIl5Fl6yTFmdh9HDduIlmNDfFyo_h4dBn9KWQFj8Fzp1XFFE8NYi71e0Rv4M_WiXzI6ofZkCpYmFSiE8vv6a7Fcv-QJZaehU04kSk-SjDX_3-MuFbM1ZcIgBbpR5rRxj5K5Z8s7JZOgNJqreIn4ec4hAt76GGneunmFpMRgjQmPDeJpk0K6xExY9cTv4bSvzN-PJWdluuUC6aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt3GMV3Ygkw469giDovOEF4ijL0bkUxY-K_DkzJYMF_qwU9cmc3zjXacsstA9HGRyG7ROIyQQhFyflfUFeH6iOoAh-l2mkecSZo3L1avEpJ3WNYAHVpd8xnqt2muMRmZvJGUbkO5AQ_Nu6pjbi2r8yUZ5wQjdKAjbFQiVXncs57jZcDSP4ZBtAIJ_ea1h32fexyhiSfWI0RaBV-ZExYZX9xWS0FkZyNW5qpAJj5QnlvrArcro8CqheQNWKSy_JVSDrsWrMzI_EACesn1S4FjekfctEiopay_FUHWXekCh7udledta4ZlvhpfnfMcAx_vCdkWxeyAntFZWxNFKYLRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=tKnjtpFpr51R2WJ9XujaLapSqA8ECPjhEaiqM6yrkm2onhG73-Qg7LN2dUq6nsxNkTMmicc-0N3Bq0jI6lOp4_tPXAniwAK_fJe1UzVvbczm5revoQW-ipO1eym_4AKsB34-S0XK6-HTme8hZ3HLPzaut5islwOwzWKBHoYAWPcr7qAlN7aXhzivSbegG5Ew2cLWezJuoH1FopbWMSNgPvK8kAbKXVHt9Q39tRldGWBL6c8Uf2CUO9HGIDy1s891jJPTMhwqn-MaH_9aJAYHNom3Br2yNonQVzJkR6Y64Y0peGesH4f4LT6p8J8-k6KqJdEvSpxx9k5A-JKDV8d0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=tKnjtpFpr51R2WJ9XujaLapSqA8ECPjhEaiqM6yrkm2onhG73-Qg7LN2dUq6nsxNkTMmicc-0N3Bq0jI6lOp4_tPXAniwAK_fJe1UzVvbczm5revoQW-ipO1eym_4AKsB34-S0XK6-HTme8hZ3HLPzaut5islwOwzWKBHoYAWPcr7qAlN7aXhzivSbegG5Ew2cLWezJuoH1FopbWMSNgPvK8kAbKXVHt9Q39tRldGWBL6c8Uf2CUO9HGIDy1s891jJPTMhwqn-MaH_9aJAYHNom3Br2yNonQVzJkR6Y64Y0peGesH4f4LT6p8J8-k6KqJdEvSpxx9k5A-JKDV8d0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwdG2goumjFmTWvp6Rd-SWxuQ_J50_6TuHAMHEBh2hLiHqfcPeFhwDzxI9uqSwZbX8P1Io650mvXqH5bKpz2cE6Y5P_anBLz4fWFojC3R90CkBbOyUVXBLouOSQx_GvM_x97faRXs3yQmwGfEvOJKq7S-Ye_jcDA9AvKwvUjfzFLxGrNx38Qw4Rnh4ETrtq4-dRc6driimnQlWqEOcxYm0GVoyV01KTF8MKr9vVpX_41fRJAmU_oPVOc7DVYGbE5_jpODucIa4Yru8IcnJkGSvIcpZNC5k8XKQKUKblIuEmShlQxtCPmmXym5zdlduQDjSAnSBvup4DVKYID7gY0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1jyxPftelZJfRug0CrtjaTZtQwjDiVTYM9wE3RA2VjZ7NhQFRNj1alUsO-oU-DNE07znEFSujFcwb_MgXTEj4voF1S24c6RpkymKadHZGkzBBHQl_JEAdhkeqq1yGs3J5kQ4ArbPcPwzlyWgigBTl3dkRCfHnvIZi6jfqmil7siCnXDGluOepVchHynkKTNwlYdoOE_m84_qb1dGNXmT45WrNEez4y81VoI6Yrj71fYS8p67kL-jcO2wWjAuPbz8Yca2vptL-JfmXxoeBjWLqIIFhqhRjIOWyxOx2uVxGMelB-78W_dfYHi48pZjcFZT_Zt034GghUOE0SjUH4aLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDiVi6EI8DuS0k6Qh6lAOf__sVB95vk-vf44_dyhU69Bz2T87crCBz5qAA3RoUONtwBdzXUOjwXZqk_2nf0lClLL-FZwSn6quhth66VCV5_CJXs1VVOEbsK4tA8NlpcwuVTCE8mWGhjcUNfK_TGULsaxTCJxLTIW3ULKroxV4iWPqfzj3Ge9owil0719t1AwyZvTsis0CAEFUXBMb_3j7iEInGFDieXSDKe6IJ44N2006WRaLFg9sVeAH9u7Dk4jGWHhmfY93Z6OYWsDVs81Rbn5Bm8R38drEHI-xaoiaAJhAN5hBrd8wR1bM4mGOeF8bUfvrSMecVkCh3JPjPJgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAqQUljzxJQtK3w8gsEBPkQWLMqXbILepQSBNpS2xR71oKLg7M4n3jgBchJloVsI_HzfpQXHLp1F_NFPN0BbNEJwTwGfvw5IX1r2gRFv9ziFWDmlG8gw9tAG6uOqBi3km5wohPKzy94nY82-owQ7yIQpTPMajCFyRXMRY9WjD-4hT5eIcTs9fmge4b0FYEjArlHoTjVbO7RHKvm4wA94CDhQpH_AmyRE0H77dhYnxB0T2w7XYc7CF3uPfuYlTZPCBnGIvYFxnQ6klP-PsnJFxF5U7rqt9VhaV0S1u7swVpnMl6bUrAIGWNtJngqjMn2heixajpUSB_GS4oASBaTm8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=Ne5wbalxJ8peBHGZeR7w4pNbf2mGpb1zaqjbZ4ajdQkIa5CT7Yp19gP7ohVjjcXOhJbRXx2yTijcyzLtDrshyOab644-aZ5lANie92RcFxXOsZhkWdu_Rt6T62t7urTW2XQ7YgS_wkp3xcS-kRCGzABnWWe1eZnAHPhetopN1lwCMg3gy5vkvsf9IwidwgtCOZ2woyH87ZP6TSMgv88CgMHWN1hCjly5id4oEmRCWXYGYnzmGz6tN29uZ7iPgN1iICfy_CleR0tNpDmi4QdcXUYK7U_4u-W68i2-6s9v8iv7QMyhI5Ec2uaN85GLO8lD4mpMZC1t-ZFNJA11SKShsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=Ne5wbalxJ8peBHGZeR7w4pNbf2mGpb1zaqjbZ4ajdQkIa5CT7Yp19gP7ohVjjcXOhJbRXx2yTijcyzLtDrshyOab644-aZ5lANie92RcFxXOsZhkWdu_Rt6T62t7urTW2XQ7YgS_wkp3xcS-kRCGzABnWWe1eZnAHPhetopN1lwCMg3gy5vkvsf9IwidwgtCOZ2woyH87ZP6TSMgv88CgMHWN1hCjly5id4oEmRCWXYGYnzmGz6tN29uZ7iPgN1iICfy_CleR0tNpDmi4QdcXUYK7U_4u-W68i2-6s9v8iv7QMyhI5Ec2uaN85GLO8lD4mpMZC1t-ZFNJA11SKShsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=SU0RhvQyymIkzVjQJ8EARU7Onjmyp-zLwVCO_7_7hK6osdwiBBTsTQwh45Kbe8FK40LPM7m_SbH4RCX2XXmgSRbZL3X3PkrLEt1rzATIACB0HUi_lPSvzKHnlHTHNYaDQmP_kLHuUNqMF8y1KooMTYsSUPo--EzHxkAMyTLnferdLT3JED5oqCYo0Ic9n1xOlwo1cw1JF7YhCZ28Cau2mP27vcZJx6xCSTS24lD2ivATe5hHSJX1p-9U5uGAeVj7qegqgX7UtH7RoZSg5Jcbgiw70uXBCFANsc3WT0Ndom5Vh5YPpDhAzIaSZgZRnc1GinP4O0K7uyTnLsMMbwkfhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=SU0RhvQyymIkzVjQJ8EARU7Onjmyp-zLwVCO_7_7hK6osdwiBBTsTQwh45Kbe8FK40LPM7m_SbH4RCX2XXmgSRbZL3X3PkrLEt1rzATIACB0HUi_lPSvzKHnlHTHNYaDQmP_kLHuUNqMF8y1KooMTYsSUPo--EzHxkAMyTLnferdLT3JED5oqCYo0Ic9n1xOlwo1cw1JF7YhCZ28Cau2mP27vcZJx6xCSTS24lD2ivATe5hHSJX1p-9U5uGAeVj7qegqgX7UtH7RoZSg5Jcbgiw70uXBCFANsc3WT0Ndom5Vh5YPpDhAzIaSZgZRnc1GinP4O0K7uyTnLsMMbwkfhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW6dAlxeLvWHfGPgKE38lTIjB1totgfGh45jdW2ByhQ6q0GjdX1poPw0vE5dc5ES1KM4e0BC_GgghaeK7U9rT-0Wq0ChRqAhj6Uqtt8WmYOtcM5hdzNDpwnCHsYeobsySvgTwRiAvbhxAeirG8R-gqPPZJG-iOUgNCwwIVCLTWLN4uTOJ7XdM82EfP_wwAptLqVPBF06u3_ROjwWOW3-as5bhBsSYeBHwQAkvthAfOsWgMKdJmYuVsZKjhv9-mvSZMR7AShSs1lIR86atQppDC_8NmHBJUFVWwLrFavbYKUI1zsBqZIRU4OsbAJKlznhUa1oWF65Av_gfu-Bb2gqGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
