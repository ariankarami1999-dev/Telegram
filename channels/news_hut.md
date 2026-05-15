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
<img src="https://cdn4.telesco.pe/file/W7OXpp_XK8V_zTcTsVV9tessjLYI-OuuypJ4_5czJEQZCyjFf7MR0s4ukZFJthJ-j3D0HUvhN0DX-m0oPs1ameYkSN0DF1yZtTzAgZKzrZEa7sXk3Ge6QoJywCkLqH6ZH-SyDLO8yKIuThSHV5doLe1gjJpMT-kSWzHN0vspa1_qrgCnhUkxxptlDqsWJ225pTTASatr14Cwwh05y9jWgi_DDogruNx67VLtNp1y6iFNxl_aEFvJT5wBXadkcLPWRRkm1NE93k6xT8efzojwbKJYjNqoNjOe4JY-DM6-cg_BFNe2a7Ugi91hXq1S_qMcY_uOV9RnIlZKxYFvQffMbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 146K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 00:08:19</div>
<hr>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwXAi9GN87AdEr0ODN7Y2ALHNQrbhO08jCjD7Z5zDKbFoHTdW5Ep_ggOeNZ-YfWD7nqEU0EouC-khbKkFUHVxFkUt0sTJwOnzsph_LkKWoSrWiR2y2rFij1fcjviU5rrr1qUergSxBSwxeYNKFlsiFrBP9Bj5yCh67uOI_8htzSPTNj-fUHNffJM3qii5KhmK2e-b_ZfWURD-_u3rmRVjp9J9JbFoWw_JC3RLTS8PtumvJ2b1smmfE_Am93a9lIde8-WCFdzApxQ7q_2E8y94isWlgIr32E5qUcr672rn9sBsnvl6VZI8isfHHSVzDpV-wMZCCPCp4FP0d7ES_Rexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=p0cyJ3m0Gybuh-C4-kjnavNrdT6_OmH3rTnYkN7NpsR36mLiHDet_L3UgJto3eI3oCiY7ORu_vm-mclMj3NOxnjDFdHl3b_T6XgJaaCaQJ4J4kxqZyX9hnplMFUxNgHAvt9dkaIeynIju2pewbtzWRryAvY7H7LwvQGttbxFe9xO-V7s8zZP8cvr-blvTsakF0VT7e5vmPFFW-m3_v0gszIZM_6G2ZoOMABwKqqPZbrFQoouKUN_W7IP0gtTMi2yKCUhTNdxyf5JngtstCpNeCeFatIRRpFLYdS5Qrhf5d2w3omxXlL_7CG5ZA4LtRWR4mCQHemi7ILbvj8Tvmmfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=p0cyJ3m0Gybuh-C4-kjnavNrdT6_OmH3rTnYkN7NpsR36mLiHDet_L3UgJto3eI3oCiY7ORu_vm-mclMj3NOxnjDFdHl3b_T6XgJaaCaQJ4J4kxqZyX9hnplMFUxNgHAvt9dkaIeynIju2pewbtzWRryAvY7H7LwvQGttbxFe9xO-V7s8zZP8cvr-blvTsakF0VT7e5vmPFFW-m3_v0gszIZM_6G2ZoOMABwKqqPZbrFQoouKUN_W7IP0gtTMi2yKCUhTNdxyf5JngtstCpNeCeFatIRRpFLYdS5Qrhf5d2w3omxXlL_7CG5ZA4LtRWR4mCQHemi7ILbvj8Tvmmfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGUmfTsx06CEDlkqEgXz8yXiZEocV_-oE1Gg25XunwWumTOOHSD1dEonA2bKf_r0WNYoV93I2ciAFMZ4wMduw0LZpxTUosUZWtQP8SIcjofflhgAh_v9nK5Nx9ieNWCL7upl0h0lJ77BcyTmVRylcOtyLLVYyAPIVtG2NlmUpj7j8_GnSOMaUBT_NxSYYJYEH7i1C_z_JU_1oBNAyxbXLej27rClAhQ__QqV2npEJS3ihVoHJtixtRcp69wrp3DaEA770urK2tljHTcXY9ZH6s_80aZVUrCENQkn3G5fAaD7z8skZBLR2Fska4rGKd06rVjcosnhADUeS5GB_HqBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjk7COUTUHlHZYLLprftiuZ5s-dXv8Rmu0XIKxoDycRLqOPinhtv3QHmSJqSMqJTJHddgbSN0p2bFtGoXZ5hSlyqmee3FRAf8YH8o7wcn4IC7K_xrkcFCeo8zAHZpXMUtbPCDvQ6l7UkuDByePX1ttAfh5Eby1j6p-gdD8eH0cLCuV2wa2T00KWMh22grkJ6sPH036v0mrCKWtWDdM8Sy4wYFykTvPmNp0rp3mvsRg7efQxOlQPmVFFHSsjih6fMcJR6YikIbObKdgDKRgqXYVfi7Ry7UsEa8pFyun8To-pkCZ7RYmvBkFNj5mpliwQfhkE1JO3sU7ai11Jpqq0v4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4w6G-lswnuRC6bBj8RVNzmJeiGntwi0RhAUpkbl0TZvqp7j1-no1IdqQzB4IUKLClynwCJZOR6wRBg1U0FK2jDmLVBdSsJg5jNR6ryB0k90Sqyec6e0zpjFC14PJ69Jo77hohCaJs_wrFdF2Oas6Wx1cxZ5fO5pzZr9twkEiMXCO14t1xAbCFyb7tLWl_nTk0bwbDKhmdg-ltlMAxhQv1E1hODZzoqT3e7vnKGIFIaaNW45kj5-6rJMpB6oJsRf5xbe3SEXLdsFrZNUYE9hAm8pc2pdrwlq476XM1kOw9xRkHSzueJVSzcTQeztQMw3N3qaMau5WZMVTuJD4RPdbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVHNK1AiRWWEBsOLTMv0HmBXfB6f5YB_LfeQgQlZPxWCFXdylen5N2XlJs1n64bhh4hqkwnXT6ERU-P_mgSRSSREJeMVrC1fbT6g3paPyjxgHtCyac0fzBa1M7AStkIjMM92AzM5nWuZ-BHGOCiV6qbSvWqYGk2ajT87jsenphEXXAGw_I8A9lyiu94vj26d97pyCkmvlEyL0ElRoFbhY8lg7RoDat2IQl-ZpprIbdCJ-lJZKw3YSwvIKrDL5UjU5FESuAZ1QmVPNbiC6QwhTpXc7tWTeiDdPw80BufcIAnOdAily05Q7GeebbnE4Phc4QXZOHpc3ANimkdr2o0OfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaylE6p610F_0KuYOsMF3u2G0KtIbHt5mpqjTUy4hiZLhdLJKQV00UlWn1oLqCPJCCcETKMj_T6U_BABZzXmxHbeBhSCxOglsg8m1In9BCJqcOo2vQiVYSzFx9-yiq1t1BEh7Lai_VNx8UHmbFp2AyatJZkRUjX7Z0xQ0p-o14bPtezpLszvekcko9sRzGtB4hZ-Rf4vbzFQAeGUK9UGOUhsCvvYjok1xLEM9QK-LC-0vXj8O0oSKBmv3cP2KG1d62IOsU_843txDITyvA_u80RHV7FY3rKSxJe9vnIFnKvF5Gjrcenrf520P2FYZM4wzfla4PQ9MWObPu1lvGZP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Wu9sArMxTFavOUYZBcNFAoUf9EC0cXwa7z-PL6UzFKjnuCllxthjuXaWbhgkKpzXlWFylzrrIQdBMcNUS8JKJqtxKAvM5m-Gx6AB2NmhEy_c8R5evtVVkwxC6-DihaVKMU-8whXw4iA5ivyX0keeN9yI0VDBOVjW0N5QgMpB2hLQ3gU29zlaMIW2tRPh7nkQ-yux5vVZGzLpIQh7rLA96gbCjV0DeJRA9vA_XaSjMW1C3D0TkJjhS8BDyBMG0Ywpo4wN93gW2pOlbqatSkTokdJDDogIlO6_hm0vY8QGJweDWCos-Yiikp8KV2GLqS9hm9uAu_w_bLyTHdV9hg87KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Wu9sArMxTFavOUYZBcNFAoUf9EC0cXwa7z-PL6UzFKjnuCllxthjuXaWbhgkKpzXlWFylzrrIQdBMcNUS8JKJqtxKAvM5m-Gx6AB2NmhEy_c8R5evtVVkwxC6-DihaVKMU-8whXw4iA5ivyX0keeN9yI0VDBOVjW0N5QgMpB2hLQ3gU29zlaMIW2tRPh7nkQ-yux5vVZGzLpIQh7rLA96gbCjV0DeJRA9vA_XaSjMW1C3D0TkJjhS8BDyBMG0Ywpo4wN93gW2pOlbqatSkTokdJDDogIlO6_hm0vY8QGJweDWCos-Yiikp8KV2GLqS9hm9uAu_w_bLyTHdV9hg87KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Sw5xpicVoSG72tYYBau1hEdlBzSdGQtd1nyDjRUfowuB7JcO9AQhTJon5Xa29wBmFRZAskd0wXnOKc1fJT_DGpl9XQ1Bb9OTKH6qfAEfFvRy5wDys9MVPIdnDqV-Ym5KnoPHPu4QXoPyVyVfDUE38UbDbiy4NDaKAFEw-1arSRV3KMRGcQk7rQkc_neThau168sYiBeqL6hqsnXEO_4vGatn554ffktFwVl5nxppVH7jgDxS5qo424BGUqBGIWt9nH0FE2soup7l_6MUXFxmYw4mB0XmrrI1YEJIIPMpt7QuTjLj3UIDatnbwfKMnyoKCRGlEkgI21VmhEM7oVIWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdeuE8C8-6ZKKnyIsGz01bApiomihamZPyNFLVebgV6j0RRV0iaAcFfMuz-GgXB-opZNomQD3bhfgOAeIsCAF5oGUHlp9Gx3SNW-V12h1C9dn0Q7YZVscu-sqXOW4BzaGjtfDmW3SrOfuWpS-uf_k_2NQjysVRB3nEfXpm97XCL1thCqluixLNx-uG42wK65GsduI807dLuDUSrjphTridXMaYMnI_gougkKTxqEoKzi_zYp-WJLgxTSrR1532wWOAesBIZJj2movu-r-KtIASm_yb2BlPBbPoyPeFG-bPJQ9Mfom0wyTmB---NX8L6_c0AZnSkKGEqP8UZUtgU-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=jMasPhynyX-q2oSFp4HQdoFJuI-uwwLg1w-hMN7H5wDLg5qOmcRb6sXMTKBxBC1-Pd7ZY6MUdGh0av9ME8zZgBk0GZzhXFhURo9NsrUGVSHPhRH7qLQuAqxhoeUyrW-Da-06aN_BrEXGbXdkuNamNX65GZExhDYMX5JH1x3mU8z-R3sGndlKLN3g_bnJVyMV6cwrCicLNrqV-DHClnwdIkXcV5vZBaYNcY9JvvcGzVmFla0TswTPN3oefFGgwG2RGyvC7H6U8-FDkR0SkJQ-09Dj1cWiNLQrcx0UaXRUsaa2YYrruRXwqna3kt5sgBadU4WJFyKAj4KjvIv9jEb7dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=jMasPhynyX-q2oSFp4HQdoFJuI-uwwLg1w-hMN7H5wDLg5qOmcRb6sXMTKBxBC1-Pd7ZY6MUdGh0av9ME8zZgBk0GZzhXFhURo9NsrUGVSHPhRH7qLQuAqxhoeUyrW-Da-06aN_BrEXGbXdkuNamNX65GZExhDYMX5JH1x3mU8z-R3sGndlKLN3g_bnJVyMV6cwrCicLNrqV-DHClnwdIkXcV5vZBaYNcY9JvvcGzVmFla0TswTPN3oefFGgwG2RGyvC7H6U8-FDkR0SkJQ-09Dj1cWiNLQrcx0UaXRUsaa2YYrruRXwqna3kt5sgBadU4WJFyKAj4KjvIv9jEb7dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzD0m5nXfp-hae4r-47j2HdC1_f1Hwb2x6ItrmRyhQDI-vkSXq6vG-C4njtCO-vPmAGqvnjv1MWWmjktvJOVApWHwrGPoYPt2uARM-9gP_cVp9m-fAc3les1usjro5or33tz5mVGoRwAJ1F2YcclT-vK1lx1eTy_r07nffaFgT4FQ6B-XnokOgNF6s3toap-uGrgBwk2TKz56kaV9rI7hq1JPpnwpRQDJOnuCm0HTU5pfVP8Oni1KSFyTBndGtAsyIk0REhZi5tmuQJqg6lTUY2jiorlqR3ImS9OBoJUdy0MN3ifEnUzfEo4LpWzyRfCxqWBff78c7UW0Gl8ZojXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgQLcyVgDGzxlU5nu2bLlbbbAKNhm82z48ZUhWAcR0otayBNX-cFcJNsHR0zumeGQqVefovagSacGecrdzrSY7jInTAUoEIndgb8BoZOZ6srLuY7gWEymdrypxC0sAqujS9TbR0-70eJm-3kQH-oQD7I_gCqoqiB4cJMs2k3MJ9y4uki8IlhOYm_oJRFAIn5kZg_vu_CxyBYckbxjN4diG5cLn2J7qfs3TZQmdqxXOvYkh6cgIVguYvpR-eT6YxYdJ5Ay32kFgpzwG164FsLH2Mi3qMirWcQujvZ8o_AqQ-xijw7Zu7K17zgFm-KUNSfcTIkxCgAS6hv4NzQlii7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxQXBCPDwHXTLqZRNw8-qIAf4NmfkUS8q021OQLKPG3Lxea-jhbnNSpf-nv0X9Xg5FPFHxNglSXdPv1dEmEqkqN_q-tboqpyrvQ_J7790XKejrAKe8-Nn8vafTLdwByFhrcq8psoxROUjOPDPD7lzScnofFb1IUEeMpcrjknXm1PVFt95MvDWhUkn0heXXYAPMemDb0FiHEQYrIPDH3oly_3PHtHhleK95DYwAaZna4q02OMNB1wUs-NjARGLBv-qVNWo4rkE72SHk3XWO2LWmj0KekGORuEanKklOSq30eCfR_G3v0JRuayC58Cfx0upiRJdUo10Skehr4g6KXNaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=nQanVCsX0k6eJlsZD9bWw_ch0t2FtIFdRVpNMdoEeW_LRi--aZq0uZ1RzhtqjQFsrz-mdOgeA9Lye84VYku4rCpvs05rXHR14sNEz0ewHl4_qqj4VogA5EH7dOwG6IT6IfpoCBx0-iXYn6NTVOjBych0x5Asp9nwIN9h3y-yxwGeV8ywr__bJhU6y_43tsO-d9LeafXvMqeHGNrhGS65IvlGRLTXSM3L59_3W3s7JwR3C8BCTRD8h6GND--3dBS1JuSnFDl4rjNUzHPDqcDJ9s0jh0ehX-ZZphVvJlqn1e_AF0tnCvBzbRRTKqs642MLiW0r7bNYog_wDtUTBafBIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=nQanVCsX0k6eJlsZD9bWw_ch0t2FtIFdRVpNMdoEeW_LRi--aZq0uZ1RzhtqjQFsrz-mdOgeA9Lye84VYku4rCpvs05rXHR14sNEz0ewHl4_qqj4VogA5EH7dOwG6IT6IfpoCBx0-iXYn6NTVOjBych0x5Asp9nwIN9h3y-yxwGeV8ywr__bJhU6y_43tsO-d9LeafXvMqeHGNrhGS65IvlGRLTXSM3L59_3W3s7JwR3C8BCTRD8h6GND--3dBS1JuSnFDl4rjNUzHPDqcDJ9s0jh0ehX-ZZphVvJlqn1e_AF0tnCvBzbRRTKqs642MLiW0r7bNYog_wDtUTBafBIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XoI5lgRdGBULjG_iWk9ANCPwsaC4V5m-7A9GHuXao9SSa5maHcJa7hsfw0IZeNqjiyYe6sAl1O1WsaY8shfBloe0G3hZV1awrwhSJmmc1b15-WcRqrsK5ORKucuxZF6pFqXwR2qmJ-uQ3Zb6o596ovDCZYr-VlN5Oh4nrCt3Iiu0b0M7z400rNVBWCgvZy6T_Q8dufsHUidDyRpDzQ1SWoduKf4P_JTBraxysPrOpEL5c7FLDMBdDn8IJG5btG73dwgTL392QpCiniHMg8zBJysLWdtikc2zj1laOyqaq7Z_pCTVhLYgixrrNgAOSs-NS07rflggzIvi4vOkYRoqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ICkoUxQVHKDfhyqzG-WCrwiPrhc-3r-na5evd7wT2qmnRttBFhTl1MSox19denk2RlIdf0s1hEpYXD88kmrPjkUUgwY3aFpIcBTDJNxtiflBiNPTfjn01PUoRZnCVsX9rWRZuR1Jsb8bkaTDbTUNoY7pQ-9FwZXgtW0CVF_8d6tC-kYjYr5rRWkUH8FTwHWVzGRqTCWx5jVc5oMS5Nv5hFQPHkUgXbof85u73sOiMDsJOcCuJmtfDc_iDQdAfQNlfkEBAxWGM1vF4a1A_fCSgsnq8g292GZgAz4X5DE6DI6n1R6lFwTkSDpFfWYrNCG-kma44EHEghTVqrTj4ABVNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqbSNqiyR2qHauvI0nERvGViK5Oy2n4wxCbIeDtnDyO5YDIszlATeYOMdt8JpvvHhL5vz4S1m3vsgLEcbdovDGhcyiEh2FKyobVtM_YQdmIy_jnrpQ0anuFKqfrgky6m-c4EkQAyv4PgiCSteRHZ4TSKBqlIKRAo-0BBmBuzFkDw3ORXvW247QiqeATs_3cHk4zjbIPPrra95g-TNxOWlBIgCxA3xQ1sND7kJQZpO9OgvG-FgwuRYiuBEnNGELNty_GeXk2GKPorU504mbmJYCZBCvSfyr6eI3bAeETy4U9nGJNF7UH6Ol3jvPv3wpsSaHArrygqwUHIiiDBDsncZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Di4EKnZcmbeuzAUG78PokagA-JNEKDrOglIkLZAEKkNWz8lvqhI9MhRCXd9wBg3bnIZjJ75eEH7QuceSnykkLNMrxts6fzTXxw7TV43H4TqFhx_Puni9IFJx1ufs4BdP4HycrJWaU5JlxY3x-zQUSo5EBhK9cLC8d8OP5813NBiGgU6FV9CBsegu6bLKSnZMRajwvBYDnKOSV-KBdDBMuF-Q_CJAyI1v9c-5qfUikfLt2qHeqzqqtkzd_Lec_nGU8RRFPrNf62rWsyEICo0HU4ud44EOM6JiT4SnZd7q-bhtpY8hNFjlCj5jcMJU9Bc7bDviQ_puf4yMZzTtNK5LhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AiNrJdZtPdm-v2KooBHOX7ficmkqQHvJOFdYmw3iT_0kIOP0WE7fGPNEfWfN3pZxfitI1IwAc8JONNo90s4l6Rx5x1u5gcHS5lYI-VJ7D2XqrMzHdRWEvspeiZrV0QKw7-NEKxagsOgCtqfeh3RpARWES-3cMqAYDMuUtzzBuYS69rB-l6G0OtG_lrHNthYQhQszqfgILfvvBUSKn4pFMba351s4xQZDQ3dynb9iiuUHPm-ky1HkxmnD331gNWsJUUpOj2y5uRV_CbjbbhMySts3VSqJqR80SwenA44ZHLFq_qIMRRNDdq7O4jvN_iw3pGp1alNheD5LYNjrZ6dQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qpyz1QEKqwtd9ruFGI47LyRmdV_4wp3oJE0F-mMCu-iILhaaoKoWjMRmkOwzUBNUSXI7yxZhrBLsQUjKV7mKjMh995kOp4seoTudyckRkMkUjJ_x142183GhvH83527zrz08Crryw2-vPkVyXI0hh-26zBDRV6T1YtKkKNikKeKm8AqUyNOETTS73PQ8UQBI279-tK9IjyvZbH90KwdXqPpTL0ocn-LO8J4PmM5D5Adg-AYOB-Hkv2bVyT_Dpj4guEYJVdBa9n_kwrMnYcLv29LojN-HBhVNICNTMZdR3ZV9C3-Ix1pl8y_SGCOMNi8nceVBi66MabTgoU8tP6U7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=hPy8XbXn5j1_zJVNJYQsLPyGTtyXQpgzAVUfJ6jEgBjZUrDE2rMaxf7aq_YrDNkC2bxpIpyyPvgMJINLOdaw2fB2q5HwmoysWeo1Nz862A2b-11oWWwuf-dD6slM1LrBMs_Ht6UY_-FuuDzqnhTlNSDwNGG0R_CLkB347xr3uAJH13Qv-oJT8ntom_qnJYSRgQ4SbysRSU9WGNPyCJF8J5wRTz2K4NTHMPBOjjS1OYqMAn3cBv13OtgpZftljDOgmvmdl3d8C5_2A7u8VfdVfRiD2D5f8tJHkHuQ4wXsTiw1n4MtAmXIOU17rN1irBu-PKd19nijYzsj7xHMuCrmhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=hPy8XbXn5j1_zJVNJYQsLPyGTtyXQpgzAVUfJ6jEgBjZUrDE2rMaxf7aq_YrDNkC2bxpIpyyPvgMJINLOdaw2fB2q5HwmoysWeo1Nz862A2b-11oWWwuf-dD6slM1LrBMs_Ht6UY_-FuuDzqnhTlNSDwNGG0R_CLkB347xr3uAJH13Qv-oJT8ntom_qnJYSRgQ4SbysRSU9WGNPyCJF8J5wRTz2K4NTHMPBOjjS1OYqMAn3cBv13OtgpZftljDOgmvmdl3d8C5_2A7u8VfdVfRiD2D5f8tJHkHuQ4wXsTiw1n4MtAmXIOU17rN1irBu-PKd19nijYzsj7xHMuCrmhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyYyfWApTYEL5OeqbGoQa2I9UZ-8NfHKHWkctWT9z0x_QCmd5795UxSockv7WXnfmb9xAx9LneKDXen5iadlgE8oBa_XwEwcMT1hw9V71StsYU_kjjLiuAxQH0DPFkVhLWd5qrnpWd6TEhT7-t51VujTE-6u8t4c1Cpr7LRrDe7driDm7DN-mNSWf7zJRg7FBprUd-8A1-w_-8SwX_O8vPfzA-G5HFIX-Ygw1camshaIJBRWkIze5ROpGI7O-kxPCJlIMsg3zd1RtmPQb68WJF_xa7QleQfGkUv14E2K__EK3U8U8veuhllEx_l0s1DmApmtnKiPVYw12aSnF5NSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KpRwAuDBmKvKWcbWzg7_RNhl8cH6HEjf8Bn3ZwbVS-n9q6y20dUuW-lNqkiBH951huv_vTA-wLinApw3Nz3vhaSaczTXA8YWhpXBhVx-N0377At-zCmWUxpXDN9yRXhZkUqeRByX3QmL7qEm6f5t0JwlTfyqkrDjn4RGYZAh-mqJhMOLmCt2k4HO_8JZe43TjgpLEIZwQJOhkGS2c72hZlqcooJ59lT_6Hr4zFzMXdm3U1y6FUbS3t-CEsr_dB7NHa1bJUMmsY6_mgfrD3BZsyyF7RNk-IyhmqwtviQ4lLGNl7xIHmNEckLv6kCBA8iyo0DyoVf2YRGNlBGR3Xammw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxHss1r11t8AjvxDwe_CoicylL3yFVoMb2GGTXTEyIrqeDuehA9iD8gnG9cEJF5nskF8zepgPeARV0qIraE2obCiu9Th-9Tz0cc1HIUKnn9ydmOKaVF0haGRptpmoaqK2XtQUGGA5UR1c017AfqIUHsxERsvsFfPyQmVZXI6Zo1YWbWR4-hxZfeR6UdIM-n3GAUgzQP0GXFpDVN2hm7ySqp1CvO8-xnnxm6xZfySoap696n0MbcMHjXH9rEqrmEpHRQdHiuTVCa3p6oXmEKdkpQbMNmgQ4fTAP487akzAP4tzCV0z66IO0NdMcvZB_K4-lJEAdqU4w_JqM9Y8CEbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=UUMOu0_7uxa5fsdHEysU21gF3WariKyxNneC3xfd3-m8-702tZROmeKtmpKIo4l0TFX5m_lD9MncMh7A9Fdn9nWY7tWEyEPe-1zPNrEvAW7clid-AAGE85X1OrB5rxw7g7jYQrhJxaysa2XHIpUzD5KjCxVWhpwB2f7bcQkCjGCtr9dWnjNHfOdVNNMSTWei8XZ3wv2tAZnqfj_AgNOmt-qPyXq0Hfp3iNEpZ5mF2DHLl2KSuCxRiGw7Jg6_qJBfPDriQ40PO82KT8oJmAy3YvXZgppz6_U7Epgy6SqXYyK8BOK_hruIDMeHtGVhBWD4F51TiBof8LUne-hmCg3GFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=UUMOu0_7uxa5fsdHEysU21gF3WariKyxNneC3xfd3-m8-702tZROmeKtmpKIo4l0TFX5m_lD9MncMh7A9Fdn9nWY7tWEyEPe-1zPNrEvAW7clid-AAGE85X1OrB5rxw7g7jYQrhJxaysa2XHIpUzD5KjCxVWhpwB2f7bcQkCjGCtr9dWnjNHfOdVNNMSTWei8XZ3wv2tAZnqfj_AgNOmt-qPyXq0Hfp3iNEpZ5mF2DHLl2KSuCxRiGw7Jg6_qJBfPDriQ40PO82KT8oJmAy3YvXZgppz6_U7Epgy6SqXYyK8BOK_hruIDMeHtGVhBWD4F51TiBof8LUne-hmCg3GFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=GKx0wkLBUrR4Lk4DoXfYGoajTI5UDQTJTJ_3OK3o61nkExrpNVRwxPMJ4V2Qa82a9ZBXLLAPUrbxszRCGBffETcdyyHI8El3UCEasRk_Vd_4VWbXJz-3veu1hwQQ3JyawScagbXRXpbp9em56GzlzAn2IYhkRJBirkhFkDc-kxPIOF4twZZzXxlBUE3ARveNxYwepmsqQBJ6pXdYij3Fp5b-9PraGyGkDOZ_-iibJEFBFdPeCodmBiu9Y4Jc06SUK28g1lsfgPCvLRboahWr5On_zkEpqwHx5xD0lTkIKH2y2hb8tN76JzuuY4r04UWR0rcEoiNa23P43QgVen9jKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=GKx0wkLBUrR4Lk4DoXfYGoajTI5UDQTJTJ_3OK3o61nkExrpNVRwxPMJ4V2Qa82a9ZBXLLAPUrbxszRCGBffETcdyyHI8El3UCEasRk_Vd_4VWbXJz-3veu1hwQQ3JyawScagbXRXpbp9em56GzlzAn2IYhkRJBirkhFkDc-kxPIOF4twZZzXxlBUE3ARveNxYwepmsqQBJ6pXdYij3Fp5b-9PraGyGkDOZ_-iibJEFBFdPeCodmBiu9Y4Jc06SUK28g1lsfgPCvLRboahWr5On_zkEpqwHx5xD0lTkIKH2y2hb8tN76JzuuY4r04UWR0rcEoiNa23P43QgVen9jKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK9KBMnXiBAA1QvINjedtYuylEhA2IFUm85iiFdVbpLszgJoEXRfhAv7fmAC5qkJD6ydjM9vDfjemMSqjoVZGzi3kQnyutShpoTPwwJY321nAse3XFKJb29mmUaSQNHPSoIx9ISZ6KqHIRNTrHdh6gDN0TjJYoN8BAW3lNk8QcQ3cxm1xEuKWd6HlehTicqdzrn9koZwDKjRx8rKiQKv-sJacRidfUeR5_5A1O81lEHioeroT-VLHD8kJiEjQTgrmANuqkXtpoFptJBHz0tP37yG011PIS2i-S0nUFCzpU-lVjeMw1B683Hfp0YB9jZ9FKzP3rz92_S1-_66IFENzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fbqYvVnb-bm5neLEYtlIV9KXJyuFrDeATk1bjIz7SjqqHU5dObhegxhv2Ztnc2J0AiZswD4xYHhOskk9QnGJyK1m3wdN2lFU4TiUTjuhBOd30cYQ3HkY8DOO8i40am9u-iGqWp6rsps5gSi67LrLQRi6PiP5GaBVwzN4Y-cNIO1oxALGTAem6ErNBVFS5tED9HwYMUlTdwjufdbSW1zpN8dpekvrF7rXRsHawc8nCx44WF8ABW7X181UpznXM_EuCCHmFcx0AoFtxioLf3zJ2aDfHcN32x7ml-N6NmHywtvmo0Fhc6UsqtGfgzwM5fpNq8z35vccGS5H0Qe4-4oP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKp8NhwyE7ql4bZOO_sMPg80H-AGJ0BimFVE0FHL163STWa4NnXuPdsC6XQd9VUlmwWut1S1kbIEDCzcjTlJp9wMxRsATUaFXnP-fljXy5n8JW9rknyhhGOf3KGqB3hl06La5fjXE0I_fgLHTX5fZ22CfwbxiZHwBWqaHzfyFdvMHN3V4fPLRfSMh6QL-Mkg2yLDCGAAG0Fy2I7j6EKKe8_OkCIQtagv7IDVKTYex7W2etgGzkKgOHG07cYZfqNFY3evzOtTPG--hI7I6VSg1944JOwHCg_jeAqef758HanyO0C2PLcrUa96MKuaQuZPqpEz4hSCGnkmsL5RhQnBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEynUoWAVKSIfJYockkK4u5hc0_bZky5jy8kPJOTCqWBEVq1laFmViO4yomZZLyBgyvfcNO1WL-kjBboL1GZC_5Hge75tdqiH9ng_8Qx6XWv-YeAFXpn7G5LqEyaoXQMSnXSZ3Mfs_Yf-E8-dOrkAoajprQPwLro-vtSVIzdwOwoPt_-UDbZtFJxfnZvOahrkG0fmm2ar1LWVmC8ruFCCD-TryFZXH6njZBOxbksP_XwhnbqGWiIbU27K6FQS_kehkPTgc6y_7waxIzWmRvbgmqKeeIvzf7AHAstOznEfgyuO3O00CrxZsnqDi7fFjGeLYU7lm02I0UAvi3ICsUXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHlmOpnppomEIul3F0X5fXHdlnwWLOQiDKDcp23DglfsrvWvEIN5a3-8qVQcSYiSSWWnCVh51aRZkkkTcZsfiLX0lWMKc-AT7zOnYiUF_35sIQ__rnhOT4pIoeABJoB26F21Na1TjGVsYakpyxAoK2cXy4a3DMcziGUCLI0TYlzQ8o6P6YC2V9mdfTGs2ActPZ1Oum_xfNT0DSkdn8SuhwE1n3DCzibVMqwfV4VrUIrAcaUh38yf1bOL1KCILi07wucbjBqsPfRvNAoxSnnJdgknWHjdm20IYsHXJ25iXpKN_pyQhnFU3qs8ZAWlnNj4mwAugL28Gx3rGfS9UaW5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=GP4Rq7prjLGuyafunpgsYdBnLQYMmWkJBlaAkecG5hMJ6wssIsJ-kj_Vi25fbcqOQ8okeURbc95G0d4MBRtEOKesFOTyCycU1MzrLuSJOnwXqtv0ORSq4tKfQvd939AXw37wmrSWD0vtU8OJKDnfMo0FLfOS6_73pWVYs8Fq6_EPJvAINQ8TwzO6QScETq1JSZT4mf1F6qKQGWcMw2itjM0C3ZmyAQmNy47GgFBK5rI-hifdxB2HJA4Fmk0aBCyvs2a6wixLyLKnGfFPL1n-RKmbNJmOIYPzLdKHYT2T5yVeONtJoUM4K3ASOq-eb3T8VvBvmIewjjqku2KaimjWSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=GP4Rq7prjLGuyafunpgsYdBnLQYMmWkJBlaAkecG5hMJ6wssIsJ-kj_Vi25fbcqOQ8okeURbc95G0d4MBRtEOKesFOTyCycU1MzrLuSJOnwXqtv0ORSq4tKfQvd939AXw37wmrSWD0vtU8OJKDnfMo0FLfOS6_73pWVYs8Fq6_EPJvAINQ8TwzO6QScETq1JSZT4mf1F6qKQGWcMw2itjM0C3ZmyAQmNy47GgFBK5rI-hifdxB2HJA4Fmk0aBCyvs2a6wixLyLKnGfFPL1n-RKmbNJmOIYPzLdKHYT2T5yVeONtJoUM4K3ASOq-eb3T8VvBvmIewjjqku2KaimjWSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=ZAPnJvYLWUkd1prg8dsnzOMM7lJwGYt_YypdTQBDB0kEh9xE_VHHpVzJsde_rm2AZ65VzjAszEMgz62XlpFITKDSGIpy_GsZeiYL3ArU2eC0wScYkqiHNCPqRW8-JBp0fWes9fnQrQv7xf9KW7wmgjYkYyGl1tMPTQ6XWIwOGOEXRoi-JiEIeWzygW0IYctwKQM_0bTI_uXiSz-m0b5EeQI_fHt6GiOECiEnAZQ5PKfrILZLCGAEWJNckEGzf4AHYiLCRDS9RdSlE4CjZkO9TW1qjT7eEp9OsTJJh2q6mqUN8msqTgYWu8QzVJ6wwmlSHftUccuTOIeRGbKL4TcBLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=ZAPnJvYLWUkd1prg8dsnzOMM7lJwGYt_YypdTQBDB0kEh9xE_VHHpVzJsde_rm2AZ65VzjAszEMgz62XlpFITKDSGIpy_GsZeiYL3ArU2eC0wScYkqiHNCPqRW8-JBp0fWes9fnQrQv7xf9KW7wmgjYkYyGl1tMPTQ6XWIwOGOEXRoi-JiEIeWzygW0IYctwKQM_0bTI_uXiSz-m0b5EeQI_fHt6GiOECiEnAZQ5PKfrILZLCGAEWJNckEGzf4AHYiLCRDS9RdSlE4CjZkO9TW1qjT7eEp9OsTJJh2q6mqUN8msqTgYWu8QzVJ6wwmlSHftUccuTOIeRGbKL4TcBLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWyokqNl0jcI634fxWyFpIZDS2i4JvtOtkqxWja5evKXUjGF5X_piZ4-AhAodlIm7ggNdiZl3EtuzasTVEjCWJ13Z6d90kalM7ZRm9z5spermgdGeumqUi5q56JXpffRVyPUeIe5uEN1a7B9jag1-nDbDLiCXQoNK6aMr_hP69LMtHx2V1pHl_avMM7xSTBAL1JOSFidLv7kZZ3D-2K1PYXXNZCTMV64Hmy3twoOF1GpOxkeoT8iXXnA-Zdadp4sgNIFIYyvf3REWQfSS8Ri7ayrlwxzjdlqJxHd8gym1XFvvUa59uq680ss6rLYN53P1iXfHwi9Qw8Tz5rsiiLldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WZQbn6X5G7kz8M_7TiX9rFMejEANhWitOibS-R_49E5HJKaDA9W2NcVwNzyAYE9vhHW5W8KvzvRYeC6QyNr0qU9Obf0APWUpvjmrVMq_hZwofVHpoC1UeZbOK59QIpa1X__W1pgXCy2lTxaWiTPylKzGcV2gWP8Umb1Qy7OG7Pqp2C1VHls6SFwI8gYVDRlAWKbZL-yaAWkCeDXRu-_u0fF4d6QyH2u0Zi6sKQnkpSsfps7z8LjWF8zsJQU8gfEa-zbS5FAuxQtQYSfltAomBkt1JqcXL3uXPrXx9-Apc68V4axCjwl23F5x06OET4Nxr4Gj-gAx_asnsax5tkN6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKOH24YGL87thzla4gGr2Tpgeblz8jurId68xZvqd41264nrz3RK8BdrHa9-KRdmN1ZzVtd9gjvIHwnDyP-Kf8zqB6KRUHrIvcI0BT8JvqvmlsTq5IwXyFoJCdQY7u59xXfYBHNmQ4V3JPrvn6_G-oEJaXH_NsacRKxtwPdybbOsgN6-Qo9BgpfXos0ED6q7vFUV5N_KsEccGOtPOecwsZ78hGAT9ll446UFGK9pWEP4ahnjviR5TCLcqzOvQzGUVw79RI21uz0NfV-wmD9KMsSddG1eGhQE7H2cNwkTdQwtQ22UVqj9kdpFS_Pi0vMHJ3kShXA32QL24tUi7bJocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0BjvA9emWXgJc8UrGMbxtnkbn81GDvqt2h3688b8FKnJR2zSMH6j4ZtwJKAJgfRZsPt2qZ5GZ9KYDYGR9wNpSLW0osP4upELPXL1rztyozx__ZQbI6QNkBJFiKYCRo9U3aoIlAbzyM1ehWfvTerP-xJlarQwPF97X2RDFRcj4zNObxCtBjkKqCCIG8Fi97wW8uYjUgxrXv-3Jzneo8iPe9-wXOX_bxpeI4STe45zbVMAyIZGFNeIK-eegDwnMSzutht7obSIsJ2qOxWRPbHung6jCTVO_0-xtdMdDwVnBs95udJ8BFpUv2RAzA1Wjpo6e1QM0EwahpzcOd11qxD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=WxDM0Z3SGerOYKoWrTaxS0pr-eUxUL7xQC32GYzYU3etUepxHZOrkZ10dv7cHwA2PxXvDUin2ThlYQfFN3ccPrHOkU7p6e35KwVH91wf25GT3hVQXdcueKBZsQ2xlFC4lvnyp540p4RhWKyTb2UooKPzGP7vwjW_W_FPsOXCCoYjdCrkws4nT6_RVH0xx4voJ1lZsX6oNFu_1AtHWoVBK2CEb-iowQY25Vyuqvy3K3KwZ2qbjiuUoFbleSMHWLdl2xlpQblBVsYW-K7OIqzKLBkpZPpJxQe9GFcLbG4Ar0M3CXH2kDD50pO2JmfH-3-KoRtOXlBnIncBPa581nLOjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=WxDM0Z3SGerOYKoWrTaxS0pr-eUxUL7xQC32GYzYU3etUepxHZOrkZ10dv7cHwA2PxXvDUin2ThlYQfFN3ccPrHOkU7p6e35KwVH91wf25GT3hVQXdcueKBZsQ2xlFC4lvnyp540p4RhWKyTb2UooKPzGP7vwjW_W_FPsOXCCoYjdCrkws4nT6_RVH0xx4voJ1lZsX6oNFu_1AtHWoVBK2CEb-iowQY25Vyuqvy3K3KwZ2qbjiuUoFbleSMHWLdl2xlpQblBVsYW-K7OIqzKLBkpZPpJxQe9GFcLbG4Ar0M3CXH2kDD50pO2JmfH-3-KoRtOXlBnIncBPa581nLOjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_f9HXvA21tphAb2LXLgBAPPXWzAAy3z-ytNgfOGhY5uab5yiMZugaI5kEBmgkyi21_Q82XzILx__GI5DmyacYAAUMqve_FxQ6a1grKNfc3yn0jZrxngQKN0eXKTXGwF4ix08jMq084QzAJ5S03cFGvHEwvEaJtSS7WV0JtsrPC65isvDyIBvzu6OsUj02z5myTeLeLqaz1I9xC_-sgmhVBEsX7rqh1Wc-Ah8UScNXJziS-182DxuFOmpM58YKM7me6azFhVr-lgdjww5rRQNsSErLmAa0Dp3tkJEBjhxjzEZcMXLz1ZsNXMFt86jdM2q4LGbjufeHVdTOjY02dvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=vJRSK53pdj8BbMPjgswBL7iUk4SEmTQyt0MyD63ba8Q25w8Hczm_L3t9KBSxfxKQbZFkYyFr7lOae6-s9vtiYd38JwLETERC07Cf2HyXo4gzmjt6E9cckzvZF5WPRn8pCmACSQNUDr8oTDKBWfPL0Dc8Af2uHCNj6l6Q8QAmvqPhyVrNEJW8fciMUY28rK6YTk_Zagp-8zQUyXE8KmwMFzAe4ZJm8XdyIwXbZxGMZnLkJFiXx5FnuQQGJx5TbohjgxrLB12ZSv0ISyhygzfsT2WeIFmxlT7roPT_fBhcK-5JwHqz8wvVf1mj1XgPF8T4wShPUI5SgTlY-g83rPotwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=vJRSK53pdj8BbMPjgswBL7iUk4SEmTQyt0MyD63ba8Q25w8Hczm_L3t9KBSxfxKQbZFkYyFr7lOae6-s9vtiYd38JwLETERC07Cf2HyXo4gzmjt6E9cckzvZF5WPRn8pCmACSQNUDr8oTDKBWfPL0Dc8Af2uHCNj6l6Q8QAmvqPhyVrNEJW8fciMUY28rK6YTk_Zagp-8zQUyXE8KmwMFzAe4ZJm8XdyIwXbZxGMZnLkJFiXx5FnuQQGJx5TbohjgxrLB12ZSv0ISyhygzfsT2WeIFmxlT7roPT_fBhcK-5JwHqz8wvVf1mj1XgPF8T4wShPUI5SgTlY-g83rPotwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=u7FUIxK9ful0Ym4mAf0ml0wpyI-sGT8vrD4N9hWSi-jwp5q2XUWxGEnT7gxpVqd8KFBwzZvCTjPhO2T_Z65ajIQwh7b4y3T-MKa9Hm_SBTM5Lv8VwsB3owayyVEArAgbtRF76w05ZcB4I3kZvzIRXGjjaUz5wwTpGkoV92ROczDNIZXa83Diczn6R1sY3xs9H0HtH2bPJssUsCP8rFA0DPsj6WQ8XR1nrnZJQ71mkiOInA0HQAF2KsUlPPoJREPleT_2aivhNdXdwc-sp61563yyaoJq5iqXBvdthhYrtBddtbuA6KJsguKqLLc_hG5ccDaX2dqTak8NyCFTu0_qlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=u7FUIxK9ful0Ym4mAf0ml0wpyI-sGT8vrD4N9hWSi-jwp5q2XUWxGEnT7gxpVqd8KFBwzZvCTjPhO2T_Z65ajIQwh7b4y3T-MKa9Hm_SBTM5Lv8VwsB3owayyVEArAgbtRF76w05ZcB4I3kZvzIRXGjjaUz5wwTpGkoV92ROczDNIZXa83Diczn6R1sY3xs9H0HtH2bPJssUsCP8rFA0DPsj6WQ8XR1nrnZJQ71mkiOInA0HQAF2KsUlPPoJREPleT_2aivhNdXdwc-sp61563yyaoJq5iqXBvdthhYrtBddtbuA6KJsguKqLLc_hG5ccDaX2dqTak8NyCFTu0_qlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWARC_g434Qzlokth_cLhCMBaAf5tPzo1yyaBsXbkUO_KcMkMXhNihKWWv-939_CZGGeWbWtKqq8gyTFBWp8eOPAG74KWm-62_R4NFhgMwkUr0Ex4ljQ6zFe27S9A5crhFy0coYo6u9z1xm4tHn7XYfQe7kX0e2jsK6dyAYtQdM9jEMDNW1kGevC-0Z6rSrFK4kjmC7ON9E2H1h9k-uv3am8ho5LrrypujMEZ0viZIchFpGjP9RoB56O68XzHQI2qpN5C6i2ZTnpTahCVJ-3JEkPyJt8Ia7idB4CpAjyG_3lRFBaNp7DvGyzJLimMsBlozY20VuqcKD_-ODaWRy8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WnIkWZEiTqoLpML9lTRSDgWMKNTLxZJtoNAPv807wYERDTXiyN3oqnOl1fJj5vvGh5S_U3SEFBDl-EoBemIkeSufjyjfVCOwgWOyL18XPTJrXYBD52hm3Df6je2HOU24LVfTNyxJBn6zBS08RA7FYL8YkrrgSz9dz9k8LXzMeXTITLnJy6uE4DjDfHmkCYjW8ZiLN1V1tLlx2PSrzluuFXnR6kJnpu0SN1hDwosngWDe80Gi3XVwYauCsowQ005g1UoKnHnyudbQhT9v2mpa1p92K-T-RNAZCCrwXY06bKysRbAoH8c0k-C53s5WNPgrSFpv4EgULeHW_vz40GRBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=o1BaPejtk9TugoBHP0MDCEH0K_LGxqbRwKxPq8IYHRU0Xen4VHRdK20v1bSp3xA_EC1sgV3UJ8P8uRNy1jBff_IxG7dWwLFL4IteLbUGnfEgtRvo0xTsQNBYfMLdjceVPbTpLymZL_T2i97U4Kr94nQJgfaJ6ifojkqwXFmTcmEH7RfnmV7Mcx_KNoB3w32dCPvZ8Ajw7WY8claaIZjVBhiSTgECsi4Sj6rHE3tMO-a3BXY-eaY7sBs7bVtv0Iv-lisRyzUNlJUhRZLOqbYg0lll3SGhxZO-nm4zW8zw-b1z8x-iBYxK2hBT7tHdbnWy_kVDH2YDZaC4AdoQdKAfIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=o1BaPejtk9TugoBHP0MDCEH0K_LGxqbRwKxPq8IYHRU0Xen4VHRdK20v1bSp3xA_EC1sgV3UJ8P8uRNy1jBff_IxG7dWwLFL4IteLbUGnfEgtRvo0xTsQNBYfMLdjceVPbTpLymZL_T2i97U4Kr94nQJgfaJ6ifojkqwXFmTcmEH7RfnmV7Mcx_KNoB3w32dCPvZ8Ajw7WY8claaIZjVBhiSTgECsi4Sj6rHE3tMO-a3BXY-eaY7sBs7bVtv0Iv-lisRyzUNlJUhRZLOqbYg0lll3SGhxZO-nm4zW8zw-b1z8x-iBYxK2hBT7tHdbnWy_kVDH2YDZaC4AdoQdKAfIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=c4Bjaz5GFjVx38xcR0rYhEvrmM9pNJJYYvfsMvl_YQXWII4yBEm5U_9bcdzXu77062-UHVVToZ9cbR0aCwdJuKWV1tf_UjCw7qu33w7qjlrwFJRO_sOpUWZFt63Q6S3iF7mL3Q3s8vTzkQgBNBge2fZLk8zYxCYFAGG05mjWociQlPn2bwFsGzMlrb6EMqhY1BjI-IpEWkHsbjuQByuUqiSa5FTsE1hYP7wBSzRmazNnIMxEImIGqvGUHTSYEaHKsRTv8vVJlIVJBIGlYFfYH5f1rGMGcvbhAqYo2u2_x3ii8bAWU83TmKLKI1iGfRP0PJiVz1CuELK8crR69kFkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=c4Bjaz5GFjVx38xcR0rYhEvrmM9pNJJYYvfsMvl_YQXWII4yBEm5U_9bcdzXu77062-UHVVToZ9cbR0aCwdJuKWV1tf_UjCw7qu33w7qjlrwFJRO_sOpUWZFt63Q6S3iF7mL3Q3s8vTzkQgBNBge2fZLk8zYxCYFAGG05mjWociQlPn2bwFsGzMlrb6EMqhY1BjI-IpEWkHsbjuQByuUqiSa5FTsE1hYP7wBSzRmazNnIMxEImIGqvGUHTSYEaHKsRTv8vVJlIVJBIGlYFfYH5f1rGMGcvbhAqYo2u2_x3ii8bAWU83TmKLKI1iGfRP0PJiVz1CuELK8crR69kFkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpiuEDt77oDdQz5SLh3-EGar2rjkYMVG39FZUrVqCzUnHw6y1MmeN4tgmXx8fxLGPtQhpWnbUkf4UDVOJ_92eobBXBuXB1H-JSQnCgSer-MKq3CYQ9R5AB1iLDeiF1sxHc2JeJ12l3mZr54YJyBbRYk_3_EqDI62mOH5wwyF_EUgXjFnJoczed9ASaSbNalQ7O56oF7ebspcettpFM1Fz9OhNmPFy9uB2tUU6K2vGfyzdPDJ-sLpv9DlYInsvO3OajrLr6JGYKKfSGwfgGEDM0r3lOeZ2vcQSheI5YrvnC1cNSXyQCLx5vAVrd5YxAtIDYIqac9Yo43dU3XjLX5TJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JB9rQtGIUa6w1iz4ZPmuXb7t5DCLWoSkHq8FCyIfda8WatHyxSFS81bGPTaKLeVCfJ-gtjbJpl_BatqUivClzf1g_gWLWPwu4bqt50MCanHxv9EHbpKlZayLX1TyI6K1R3WvLp9Y3GR4W466EfTmKlSrxSlE8l08G2U1TuGohHL123FhMIEFJzYVpeG5vMe076NT5AwmH6WuaUbS5TDS_0ptmvsngoFQ8C_zBEBZyOSYpDNpVFHTbqNxk9dZEezORIf9v3c1_OBNqz26-VTamfSEhBZFqTk9Yh11G0PQVqVKzAyDRFbvYNxQdaQZCKGrYeD8UPyqs_hHdhcrnmQRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODaaitER7CONuXrRLAwIjAzoBIaOxYkatdCyt4jy-mElyL6LrnKDEboo7LFktqZzZCQ1WpwtjCDSeTpIG7She0CgQ2kBJtlo4LvHZg0TGTcfhMGsqvyKgExTud1c7nk-Tmoo4dzXAezGPt471CsR2rc0uTNrfrigDCXydzZiq0dePirInMepCc9zZTYLNU8xyNQcegm0JfQuuUmJ77fH_zATN8Ex_5peqfxpx22u5YujvpFCBpXr_ErZTDJr-p-PFAhF88CI-PQMHsyhLevKuF-sPx8sSGnoQBoezyRaLXkvwXJ9yQFJMdb3ivChsAHmqPnuygYOKltzss8HI7aBaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8mjDV30UKV1Ip2eUxvweQPEGjK4lonI0eYxihiVeaUd6HuOwrd3_VLoh5gZpRf1IDTXhnc44HCvZuAk6OSL3CgSns2qxcGr28X-7h07xy7gmqxzxv4m6mEtdKRH9M_v-J-uid6PcQbRf5YEMPiPtuBoGfV58w_FrnNbRN9OBRFvzNaboxTLcQteHGdD2K72alJxbiuiN5v34xweO7WatKl_kxcNAFROXaY-trlzExdIgs-6GB5dsdq4Q7h0Pdb2c7AM4OArWUthRkSRI0tB4FZTqSfkCxAmHIstl63CpMPrHaW8YOZVKbNa6bCyinVPfTQK8U0vaJLbLzeZJqz4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=kvuoCNY4HsB3gwytF2obHuJud1GQeFux4wulAMqwZKPvsKuQ2MKReb8JY3mD1HEqkLXsOhPKSkxTXv4d8nLa96tVUnMkKRAxkiKeSttf3Qb4YLVOR1RVqsDjt1CEQCFgwFXbZVFccArXZSgIWrGClhF99ssqbZYnmkTaUmwU8JZkdzMbU9gamLU5Fy7psliam5rzg7a2fPDT43ygYNr-zDZL3CJrK7NN9SbLwT7ae9UEXJjFWRGx9ZFBYJoB2cvxoNWzxnmCSl2E-d60ADL1sF_My-k8a4XQuXkNm59EmC1kv9yrbWMCiMNCSB0whjGyFzJvdke5yQs8rPBzrIPHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=kvuoCNY4HsB3gwytF2obHuJud1GQeFux4wulAMqwZKPvsKuQ2MKReb8JY3mD1HEqkLXsOhPKSkxTXv4d8nLa96tVUnMkKRAxkiKeSttf3Qb4YLVOR1RVqsDjt1CEQCFgwFXbZVFccArXZSgIWrGClhF99ssqbZYnmkTaUmwU8JZkdzMbU9gamLU5Fy7psliam5rzg7a2fPDT43ygYNr-zDZL3CJrK7NN9SbLwT7ae9UEXJjFWRGx9ZFBYJoB2cvxoNWzxnmCSl2E-d60ADL1sF_My-k8a4XQuXkNm59EmC1kv9yrbWMCiMNCSB0whjGyFzJvdke5yQs8rPBzrIPHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کشور عراق، تلگرام رو رفع فیلتر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64839" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏ترامپ: ۹ جنگ را به پایان بردم و در زیر دهمی زائیدم
@News_Hut
#Fun</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64838" target="_blank">📅 16:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-FzxQe3QJgxKZEjjFYfL-vOQit9-d20maTlcAfzTrmJfXMwf5cDk-0xYrPLKlib-sp5qLBCETiD0WmRE58iCzAW9aF6PT7ijieqvgEHaSd7Fu8SsDz-lWb66WfJAgu2rjRk9-4CuaeYPdy-MdYwbrBxy1Dejrvmg0oCeTjKNGjWihXkT7zD8nOIKZ4L61A0IAXG3AWtUHew2KQ6vR2uWSobwEfQ1lxqbp6Taa_Gq43J1GtXAqxwSBsGtahEpDZg1gpOoZ-Ph6FWStt2ktE4EfWkpaZQTWuhnSUlFc-lf-V-Cqk94uR9P-n54K5My-_QocxVGyLH0E3gyaKcXbojXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=AGmENGBSexeZGNKerpUJuN2lwksIjAckuTbddwvdACCH41rbB8_pASjKXHAb6p1PKZW22NgCSrg34nd_-Kolr0nXvvxTSng8mtUd4ETx3373Jo7vLzjTZWyUt-cLtGupGONG4GlQvz3o6Ilshd6dsc-FevRZ_uuATGQ2ZDHS2-H9you4YsCyK6Af0XilD6bnfTfz02eTVWGof3ILpSQLmGuZqLr3-j0RbrWg_WCVOfvarFWImWNx0TL4m8DSaTbWjslTy2hSNw08642fVHk7MZ8bRhXDYcWQDX0F_wJ99k9KSWoU1-ALMcBUHUnc1SOCzGv3Y6Mqq4pfaYbkvbMm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=AGmENGBSexeZGNKerpUJuN2lwksIjAckuTbddwvdACCH41rbB8_pASjKXHAb6p1PKZW22NgCSrg34nd_-Kolr0nXvvxTSng8mtUd4ETx3373Jo7vLzjTZWyUt-cLtGupGONG4GlQvz3o6Ilshd6dsc-FevRZ_uuATGQ2ZDHS2-H9you4YsCyK6Af0XilD6bnfTfz02eTVWGof3ILpSQLmGuZqLr3-j0RbrWg_WCVOfvarFWImWNx0TL4m8DSaTbWjslTy2hSNw08642fVHk7MZ8bRhXDYcWQDX0F_wJ99k9KSWoU1-ALMcBUHUnc1SOCzGv3Y6Mqq4pfaYbkvbMm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامپ: می‌خوام کل ماجرارو تموم کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
ترامپ: خواهیم دید چه می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64834" target="_blank">📅 03:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مارکو روبیو: متأسفانه، تندروهایی که دیدگاهی آخرالزمانی نسبت به آینده دارند، در ایران قدرت نهایی را در دست دارند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64833" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64831">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OY1IR6qET9-RrcjA_0mQuCgRi2dYRCOD-5-JufG1KR9o9sp3aBmHPzedxBzgHXW6r3e04AHoQqLWq-ShRuuEzCf0kVXjiMwGJ5FwPDP84dA7v0G_kLGamYbKl1u9jKeAQZAUrz9ZkGNbuLfj6P1M9r1SJdmQOHFO8PbW9aOV0teEq1g09LVIOMtSWMPWtI97Oq2_O9VcN9-J6-DJOo8_yhD_J2lPHjrRxu4PoWuzHokw2_OpBv7i6dMrUSRcDGi8cWlTGnmrWNP5kd9QdJYof-UH8oZvoWGczv0rZunX-VSpyO_QilGUNtWsMbaFXFnQFGJl-jyyCu2bmPnxoYX2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGjiu6xEryvqbcrawzTmQH2zz6Uk75C5L5bynYSt4Mqf6oecZNTNKT8PIeAVdv2NL2oq7xqXhmrg5CtzIHyVxx7THUOhMEq8JUTREbKgRzY4hvnKcs8lHpDq9n8rQrlOxl7XQFnxc_8LfRRZM1AYYSEGeQkvMUyQJgxVWz1Vw4yh9p206u78_dFg_JV963Xph1a-DV0CJEf5hvN0GwG_i6Pw-R-7x-TJc5p59xFPYhGYp118heDzU-ZKMBl4JFFp8hu5sqNjwcBsYFemixwUOW_bZ0Y2XhcVHz7H0rqW3VP5NLUDLDI_V9LepQKVRF8DIPj9POKbsl8K47FioQspww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbOTR3WKTi7K3yjO-ycowt3yJcvLI4s-gECoVMf68_I7ta5ItXW_Nv_6aowrjmibC2YqwhYjjUKU1K-mHwc6Ww4qr5HSDhV0Nq-ebpmOOujsuNbpgx46tQe_0wQQmGYpbIQUMlv8yQnLd9mD0vQBc96Zgd4jB2o03fpRSOTjpdUozCXyejlXRGYwn6Ne7pFDgWeuQKJ76Qiw7_dgd1Wm6Vpi2EqIpJ7VDDGpcz7L5gMwDDiLskk7ilcYH7jf4bMHEFMIoy5BwabxXrWIkNdcjrXDgoQlHBuDMBrui5AlMdpl6si37yWqgcD5kLq2Zo61Y6dzq3ylnnc_KzYq9uQyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn73njgU9bDO8oGLbUD5dg2aMwMTnD67mnCJUcTT9GKiXV97gsKj0cgt8V1gP_ZbmC-b8ioyaZ4u1Keuazio2YRWfLt1mgmsh3t2O6pbRskJzukZpMkAz6vwsTB97rn_3OHu-lCQnSdMgwB8CY7DwZ3jUhigFOtr2Ehc0kfgKSVIjBfF__XV0UoPk5L9EZsdhW8oNdFsbQ3M0pvNo0U_1wDc0cfHXfHLEHQotkQ_-9fSjSTnCiRbt8xPc4rc4gVG5nP1cIdWo8RZZM-AkOJhErCIGKc67t-oz0qxBZ_-3A1LuAYmRBaMNuE8vLJsu37W5nH6Brtguq22Fl9nYbIDQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فشار جنگ کم شه
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64828" target="_blank">📅 00:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=eGhLnnaD4M-Vzx8E6BauYkwf0HNk1I8lO88BS382eQdXXfRUqdjAIGSTZRjw5kaGlTabNBfzDsMdX26ATzQLtY7YE8GGLY2tyQsep_0izMXSioU9xkaY4Sa_7QBy2SU2sUXqS-Sr_fPHa-m60NufXD90xrkqoPffD9jN2e7oJGwsG2NcNG07mn3q9H1NKNV36Kxf3Br7ykOTyJH9-p0wPtGrAGw2v-kP-_C5MTp9Os0anRw6J9XZE66IC73CZFckPkYmT2JDUMzAsgWo3m_JGltN6BcUIrFoUQPD19NCl-zt4NNSshbjl9wrgKIYtH7fFs5gv5KKloRg19NLqstgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=eGhLnnaD4M-Vzx8E6BauYkwf0HNk1I8lO88BS382eQdXXfRUqdjAIGSTZRjw5kaGlTabNBfzDsMdX26ATzQLtY7YE8GGLY2tyQsep_0izMXSioU9xkaY4Sa_7QBy2SU2sUXqS-Sr_fPHa-m60NufXD90xrkqoPffD9jN2e7oJGwsG2NcNG07mn3q9H1NKNV36Kxf3Br7ykOTyJH9-p0wPtGrAGw2v-kP-_C5MTp9Os0anRw6J9XZE66IC73CZFckPkYmT2JDUMzAsgWo3m_JGltN6BcUIrFoUQPD19NCl-zt4NNSshbjl9wrgKIYtH7fFs5gv5KKloRg19NLqstgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی مسئول دفتر علی خامنه ایی درباره مجتبی خامنه‌ای:
خونه اقا مجتبی رو زدن ولی ایشون تو راه پله ها داشت میرفت طبقه بالا و فقط موج انفجار بهشون خورد و افتاد زمین.
فقط کشکک پاش و کمرش آسیب دیده که کمرش که خوب شده و یه خراشم پشت گوشش برداشته ولی الان خوب شده
مردم صبر کنید دشمن الان میخاد یه فیلم و عکس ازش بیرون بیاد که کارو تموم کنه به وقتش عاقا خودش میاد باهاتون حرف میزنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64827" target="_blank">📅 23:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhOJh1nz4lfIBMSChlUi3CPI1Swcl1kVIfLHPfFFqXQi3LLpNQ4rf2jNOw-Xodv19LiW1A6cTtW_HPILpHmIKeA_stRsXFJOQTkvgrRr3tfJRGT3BQLelPF31xYg90pyX8dzkiQLH0pTmqwOJR1IzOFF4--EAPSMiRXc0iVv1L-Tn9FUQTh3E1zaGSqtHYm18CAZ4wOItFC1MQuDyiAwiR_qwBPEMU3XINX_Hmag95keh9FVc1Qyspy7EiO6sJ8FVqmSMy2JwKAkJrCWEuJPatDPlWgGGWJCIHjhHd6C-_zLChXjplIlHkinQXQTZag6qAAh2rdrNSUOzbcXF_kx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ ۳ روز آتش‌بس بین روسیه و اوکراین اعلام کرد:
خوشحالم اعلام کنم که آتش‌بس سه روزه‌ای (۹، ۱۰ و ۱۱ مه) در جنگ بین روسیه و اوکراین برقرار خواهد شد. جشن در روسیه به مناسبت روز پیروزی است اما به همین ترتیب در اوکراین نیز، زیرا آن‌ها نیز بخش بزرگی از جنگ جهانی دوم بودند.
این آتش‌بس شامل تعلیق تمام فعالیت‌های نظامی و همچنین تبادل ۱۰۰۰ زندانی از هر کشور خواهد بود. این درخواست مستقیماً توسط من مطرح شده و از موافقت رئیس‌جمهور ولادیمیر پوتین و رئیس‌جمهور ولودیمیر زلنسکی بسیار قدردانی می‌کنم.
امیدوارم این آغاز پایان جنگی بسیار طولانی، مرگبار و سخت باشد. مذاکرات برای پایان دادن به این درگیری بزرگ، بزرگ‌ترین از زمان جنگ جهانی دوم، ادامه دارد و هر روز به هم نزدیک‌تر می‌شویم. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64826" target="_blank">📅 23:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXd8v-hnCUezUW_mLkO5319Pgvo1k33H9D8MWT5khfWMHniJSypBu0ju68uCemtE7dF6Mfa8OxEEOxOmq_RoItiLdpIQcRNQUaEpLZ3K_trxFaP6eSnSkKo98Dz3AQnnboIUAdSO0N4g3VxOKid_TlI5zzmjQ3p2exPCehWdqS-SlUI-BPIgg6xbpZJQzyO4ZhJG__SLvTQGolpkJec5voNKTFNWl9hbsJ8XOg_dZxrN_0FWmaQrg2_dYvePszOPXQoz1gN9dZGprv-Opd8oSCRGGbwnh4lcVHGoVBWkOtsf4uP4T68XWI3bI7V35VQ_pqPNsF3Ummms21URSBZM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
در مورد وعده من به شما، وزارت جنگ اولین دسته از پرونده‌های یوفو/یوآی پی را برای بررسی و مطالعه عمومی منتشر کرده است. در تلاش برای شفافیت کامل و حداکثری، افتخار داشتم که به دولت خود دستور دهم تا پرونده‌های دولتی مربوط به موجودات فضایی و حیات فرازمینی، پدیده‌های هوایی شناسایی‌نشده و اشیاء پروازی شناسایی‌نشده را شناسایی و ارائه دهد.
در حالی که دولت‌های قبلی در این موضوع و با این اسناد و ویدیوها شفاف نبوده‌اند، مردم می‌توانند خودشان تصمیم بگیرند که «دقیقاً چه خبر است؟» لذت ببرید و از آن لذت ببرید!
war.gov/UFO
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64825" target="_blank">📅 22:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
چندین تصویر افشا شده دولتی از اسناد بیگانه‌های فرازمینی، پدیده‌های هوایی ناشناس (UAP) و اشیاء پرنده‌ی ناشناس (UFO):</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64824" target="_blank">📅 22:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=nFqAOasdykWmWsFW54K0woiAD6vXRSjJg5E2eY1k7OtB6Y1sA9UlebjTDgikY0hVuZEjLnH8Sbc0m3qEbvbRmbv0sVYoPuZqVlZvorQB8an_4M8zn1LQU2P7D3bjRFQsl2MNJTeF8iJPgFDTjPqx162yIclGPj6Z-u7rVh8S9g2eHWxXkZWTfmDU5q9UNnXtg7oUX63uOKECfvpfZRcb88j6HwpKMdmYQTR-ER2dbsQGKo-2jhLFZ3tSW-pDMcJpOEzRoJp7aqLXvsgxJODXOrvufTL3dqnLJ2dbMYYCIE9s3UssWKCIDxtYatDSDUnra2BaZtDk0Z9lKLaAmXMhCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=nFqAOasdykWmWsFW54K0woiAD6vXRSjJg5E2eY1k7OtB6Y1sA9UlebjTDgikY0hVuZEjLnH8Sbc0m3qEbvbRmbv0sVYoPuZqVlZvorQB8an_4M8zn1LQU2P7D3bjRFQsl2MNJTeF8iJPgFDTjPqx162yIclGPj6Z-u7rVh8S9g2eHWxXkZWTfmDU5q9UNnXtg7oUX63uOKECfvpfZRcb88j6HwpKMdmYQTR-ER2dbsQGKo-2jhLFZ3tSW-pDMcJpOEzRoJp7aqLXvsgxJODXOrvufTL3dqnLJ2dbMYYCIE9s3UssWKCIDxtYatDSDUnra2BaZtDk0Z9lKLaAmXMhCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیو سنتکام از حمله نیرو دریایی آمریکا به دو نفتکش ایرانی M/T SEA STAR III و M/T Sevda که سعی داشتند از محاصره عبور کنند؛ این دو نفتکش پس ازحمله متوقف شدند.
این دو نفتکش تلاش می‌کردند در یک بندر ایرانی در خلیج عمان پهلو بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64822" target="_blank">📅 21:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64821">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
📰
فاکس نیوز به نقل از یک مسئول آمریکایی: ارتش آمریکا امروز به نفتکش‌های ایرانی که قصد شکستن محاصره را داشتند، حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64820">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: امروز پاسخ ایران را دریافت می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64820" target="_blank">📅 15:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64819">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2i9g0cex1PDgc3mP2XSazMDgiYVPp9QQNNAEhPvwBstIkb_ZEU1ee03Jz0OSpLfnK4-ofW8V5xSnHrn07CYI9LNq2bQ2DjffR-k_YqI4fDllX_vDEes6R47sjR_3A0VDgan4jNudn2IsHom9q0XNWk2dZAZlbu_nFxrywOby4cQPK2-Ww9hg5TF42gxlTcbZH_daLxWOWNS_XgSujiYOyLTDd0FN_tiwHplMYPWFhg46yGtejsUt0gwpUw_2TM-Ck1Gx25LlYuoRMy1h5oxuwGolbQbVUctDR5oqGtAPLrSN1_MF2OJGRLh_KfgCDsVE_Qt9rSrWSXFwIg-xVdrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات که نه، حتی اسرائیلو هم بزنن ترامپِ کاکولدزاده وارد جنگ نمی‌شه، چون سفر و دیدارش با اون کیری‌خانِ چینی براش مهم‌تره #hjAly‌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64819" target="_blank">📅 15:08 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
