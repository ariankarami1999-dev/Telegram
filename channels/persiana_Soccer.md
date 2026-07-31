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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 22:19:56</div>
<hr>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfAAYoSdIp3tME2ggTDuDhBd_Zj7UZuCiBuXaATYXYZaVC3MjDAQyuqvnlcVbH-A7Z2HiLOwcYKH9XiVyv7iN7zWSJcuzpDZaBhoZMLk-ptbY3medJ1ZrducDhFVOs7HOtmlL0xMaxD0NVs-SJp_eY8gcXcqYIxYFoYnxG8u83kpN4aZl7RTnb-V32HdQgHhWlfA3F2-ZXMbkmxCj6OOKlVckp2YzrQNiMdDp8h9UzhR5C4OB0JLeEhFpC5-lZPviI8duBE6o7sfRKkztbetq1sBNf_iuapzbRkOzGimRpIJOzL2KXzshwO5D7YPUbYPkQ12tyl-iEnfrzirqxDLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDHPhcQueMPYBEc2I3MO5_j5ukORb837hEYI81CQoIcmVt0HZ74JE5FivLOLp9K8urFTcWc4E496wfUo0QUd1KeykkjD7h59Qhn1wdJpZLBcQe6biXefmbNfZ-McDarNdBk1djsE-AXDJdIA-TcMK1ppZlOH4OC7rfZKaeiVlrjbrOroOz6Txs6lqOBAHQ0IcP0KL5NDLZ185fUIIfWJZEL75edPoipChM86v6zNCQX9RO1JRxhXOQ9DSMZbE0gbs1aUT7lgouJCUeURYrvv9Dn_uyRFA6ABcoH6OhJ16HsOHm9ljC3ZcnRiOkTucx-OSGMpTBRAbumdDK7Smt8FbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzm5m7dK8V6tganEY3x-l1AfAqIizPLtFZ1986aGdqixA1UR0Zhp0ZfpcoCPuQj7rv4iCo0HiYFI2tqY43h8hkDYVbf8G7IiMVYW5gMMkY5xs6U3aeshWjxqHKsHrYwXDns3VSTid1TqYAVmFfTfuShMSccCoasHcP5iKa6vICbci4n-JLpc1z2H4gpwl8OYH0F9wQ_nDDue_oGGgJKEELqGPAhRqM7GiiZZ01s4YoFT6_lUDnOkc7UM3Hskv0NhZa5ty3cDemrGuhtf8Vp5PD8JGg94voynRwWZF4xq-9vnvSQYaV9ZKx9hMyyhNc1dFAFgxhOLzJ0XTdT7Qbszkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfUBmioy9-K-Xi-ZqisNuFJg6c4BFfvzyn64lW6an0cHWgb0N7eLNmnvc0dXlb0OzLxqjcu1nHXGhqbm0SURT2Cvar7py0wtHxjepwVIdoxk4vgwMCykroBFJ_1ueAgXrnqSSPblqSJK4IE-P3zXUvQZEYmaZC9E3mMr2CyBiL8UbXhvmF7YYF8EqROnL1zyZn0SagN51b5DrfPEuY9to_P6egmQSwgphFpeKJAgduU1FXBTd7msNYuqD7LVB_v2Ht8j8-C5ku8QXrRp7g3tgMcNvX121T2HUBvAvBitbCnpZT_IKy_bfJ-JounnC6_D5Me4JcWECQZocZEJwQb82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXRK09w_PkQlexQ71qs0ketq8WpEH-3ozHeP-Dg1zDDQbvoIUc-OjIGv8nvz6N2SoeIzRkER8IZ3wtxf7gKg_x9M1DVFdy9CPRmYrj2jrYsy_ijIeyKgqIAvMy6MLwgwvzt5nuHQSd_HJeWbHDvii6RWMs9dDJWyeNdRiZi7mSQA2zxEzhbVmSqssMGY0iH4E1zlqgkPQ-VsSqfjK0_h1HrzARFVP4T7MeVWJG2DD97ghx7eQkiZRa6MOphhc5Wpt9o7jBBONldKfHUwL93EU_VVKiHl4-pxS0VLS1fkiAiIYlPbO6UbHV7gp-cGg5qP6ntOxFPoBkL4TqWKS7QtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfLMr3CqfhseGB_zFmjbV2LuQX7z5aMVNn8orJdB1YuzcMFN2D91hNswVDGeaELq99ErmJLX_Cs33YoWT6UfOspyZsJR0xf6BM1wer-xEtr0QfMw5xS5KdG-6gmjCA2rE_6I9mmoIuvry60WPml3lvNhzKSwj8wd6k94mPRGZtAG2vzBZGCZ39hhlk9VIy_dAkq0Yc4bAEpBjhfYTnrH1qua8lLwgeKcCMUAnyMcLManfyufNX5U-1Fvmp_63WMxnby2B6UvHRv1FUcV3LLZScXnMNL-hH0iFUe6kyCBwz_J55d9mFO2Tvi6PeTAHG3_UPH9u7GCWikfn2G4UqZLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE5YjafaXq90Y9zhDdQCo3slCnI8IFB0zrgnydVCqII9oYueFpLGIgGRluuMgcyKWZMgKzpqmjZgoYn1jNGKF7TrE9nzALsVpPKVKl5RAD_RAVFufEMlQEAm8cTle_vQeJTcJpEhpMCNn7zpvBuolHWb8zBV3XEXOb9UjFTQkwRIFgITFFP23Lwjb_4Em7_FiZpZs-8b5DG-nGU-MFihQy7I5P5XcaXccgEvEwgU9UDO6wgBTSQtKocgUZyf7wmmNm89LxTl08yrDFe3LkkYcDqu4_XkUsrVLD59QsnkWjMsbvV4eANwK1FI1kNuijBU7RFh5pK2xhE7OVS9c5Dzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArvQwunyWzB-O-IoM9HHA8J25aHLfzKo6JRlZvCHIhyc5AEiJAMGZCv1TXzH4pmJO4GJtdh9lBDk2sRREyqI0HeYbFw0hVkZKbpGbgbUqfS5frdMiCmv_EbDHhlWvghbX1UEJIeBzVDk-ijIUusmZY63vuCSRvmFkzabduWRAM8px5yJKzRgEyIp63ZFwRfuwQwtPHL66SfEP3fO_BqHWT8Y7VhEDi_t7Q4L_EM9XmAEUEeJXHDhDjljMzw19YEVGn6lfjwenJmr40HofE7lTZjaW-ufKUm4bH2f38ZZU0_03P3KyS-zJoVCcYPrCpmKvcwcYZd4qSUAOiLNSnWx9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPJU7NZX1brCgg8d6_-PZRmoaVNZgrZd4M_VW0V_VMyzPQLBwkaSKKBG_H2cgZoCoE8YuFjuRslrnBTKBWVHIz4W4Mi9xhWGe1wI-ZKJ_EXJh4SLQBfoNSxJxDEehzWJzDQuvVeVnSshzS3fh3f-2rEnaz5QsrNH5b9hIdjE5JcbKzQ21GDSk2x80W_hplV223AoYSLtoZXp641_YqZjZmYvAf9_ERbgytPFwfwBZT57S9PWOEKK77d_1b0g9-8g8IyIe-cZutKVyMAz1-oV1TPr85A0-GBxW3gkHBns9pB2ASPkD-QrPTMrjX3HDvHB1JFJr_mU85X9sheV4viFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv50TcRvy1Ccr016CSCW9LuwwVhCyzhR23zDXTeOvUb03v0OGnpAVrNnBU4zWiGeq9ZJF7sNlwGbvzN_LyXrpY_SnfxgRzBKqfXlt5QJrljR42QbVqjD_SudEuxCJdovShFqKumzTSgFF3JID_n0x-5hhTplhn945N7UE2LkwHh2EaM6IkLIwEXV4dpa3HoXZVl4yuTQkCzzIyQ74CbYPBLIEWmoQ-twgqK-SkdMJ5HkRcF4uHghl8IamKFvkV64QYqgY8A0unILdnww7p9QtYOM1btlEbeNKpZyQPU1YTNJbc-oKvwd_HMdQZQvRg9MNjxoJ-bRmegH08kG6TdkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26890">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚡
گل اول استقلال به   🄼 TAJ NEWZ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/26890" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5bZUij1esGCDgbfEaPt-S5rSyC9T_ZklJxkrcI3BmA6LAjouWUXNQluIga8j28ik83BGj3ro1PdP91-PXb7g_kTSS4r9QuI5q-qmxvPdnU6Nk7X6b9dsqlMXP0qMfOOJwWX5jCWaxEUToHHJsrQEyGcbssPfgIThCRVuFJUHYaVdnwqxH7XmrAq2fhcMljFq1NbJlm5qMWykeK2o1Cxd2WtW_T_flqYGUFPZRUSgwHbHrJJs-CXqAjjizXI_owMs7dVgg3rGvcxaSUV2c9n6heihK5lLBGnaUoECUNmzaxcBYpRmY36438WYMCobQsIW9_GqbjuF3jQWcXjUuYMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obkhzRifX4xqtgXeZKoZjgSyiNkgm3QETFg6MYELNmdS9VaCpwnxtbCR68hzmE8HnCMjBv-juozO4hsSHPn7hS1ZK0d8NY1TGFFZ5upsW5ZgvdBY-rT5RmRzya1CT9CxKqn02QwnQpJjY1HNkhbh1Qh2m-ymTidsmsdtDLCLhlY3KtWSeFi5qw-AosgTQ4ALlR07swRB_jkp_E1FNhGwda-7b_w23yFJJl4h5gL27d0gTGk5YqSAJQgFMDRDi6k3QHPQtvePHEl8TbisGfCh4YlH4fNzabg_egqjtrDunFOhbbi5xva5AunXRks197dAXzhj5QAlJqYnMqeSX_tSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRsXn0Thoirc1qME_j6azLanNC3JJIgOm53NF4e3g6H2seKZ8jzlZ68HPznQZxVHB_fvGMgVwPl_D8COugNNaltqeYvS-FE_J8J13BqcX1dDzKrkfuzcSHiW6W3lsrzw0l8R-QaSj99gmPoUguRKxf6dDLykiWuqbbb7PvLnBPgL-DPz6r8UkROFJIH0OfqysMFfHjaEu1-waRo6fswNqbulGpMi9Lu7e1WU309l80p2-PS_1xjcJqo2J0JO80wAZBdNG6wWXHeTCVPlFdDJhcjCKR-TRZ8oMMQOlNQQx-hyWBYGYRMs_ZJXEKsEB4wrFR4mD9pc_6x54j4rWzTpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Se4weCwH7EoFuSTiz3q5Efmj4M5rc8_lLQ8grjdE0zee1hats2QzAlxjs_tlTJZMdBN0myItlDXVwDPfInwDI76fS-A_Aw2leBIwYrY5TDrGKOyCRFQBpNWM9hnO5mGY2Y9UIKflwxmj5H2wzyc0uUNZ6XEJhiXhVeoHr0mWrGqNoBefSbr0dyktBJCnI6pKw4ukyyQeTRJD3kfXHHmnCfqOTMMha8fM2UnEqBwxyxa24BGPJLkgse1bS4KS9-cyCPzqAQ4X3uBHsrabdNjW9pW5KApOE9DgVA0aUeeUuLxn5NMmYyPv1vp0P2y4UCBP1hJuNB_Frc6vmkOoSRwosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHVJExY66ALXLUAP_OjvS6dMXfygEe_CVOLw4O4nNFeXawMrqUAXR1S4X59rmKQ56v7g9Jo_Bgc1YP-eDsIlxjcr600VlHya3Grp0iGyBgGX9EvokOAkDnJsoGOJpiKMgayCNza8QWUgLrumCLVgbcAwJsR-mYm4L_eej3F6WxX3iEWGu_mUCBpS8hDK7dsLNmHonzbXVndHkxXWizUIZDufJHDxvnNHQIc7o5bHUBLzxF3oQztT8mg7MRys2u9OZIgA_6dqpoEubay3txaK8KSEnEpd8FeXIPFNrJkmpdSYun1I1COTk4RgK7C_AJJGeFUM2s2dvd-zax_58I401Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26883">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26883" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uICKIFQ1Ycfn1QXWIBmX07jXr-c8Hvp3Dz_XKj5yMXqx8wXfR9MlVyFjdnvrcWykVpiB1U93gcyjdcOBAJPJEtVPgyR7EF15Kbl2pgxFUotvsg9Fw8Lu8Lu2OkRSTiEjWxPgfW1QpXPsuzVEtjJzq92ibAWr2gqv1iLYobC2Y4qseqO0NHns_9pA_mlDLNFzjkKGaD567IOII_be4W34Lee_XDSzoZHaM-DT_ghq8ST4oOHq9fXNLGf9hoMO3ksQWe_iofOuKVItl3Umar0-sRqFa_n_hB7TlOlYvoCRtpaNTBLN5IoY2zfW12pJNUzduGXBawp0qWCrReteO0xi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2AVn02hpHWgYrWVaLGZjFDrEizLE7wYiAKV2s5wuOtbQE4mXMrDYCrx8zK1CjJd1IQhjlHb92aOytvGlgjBX9OvNMJDzhXZAc-1xlblsDKvnRxfP6gEZL1V_kWbLeQPuxpB57VXTtxrEl5d9T6ScM7g_MazIYRPYlvPMW7mNK-BStR7WNeAMhYpJHYoftRiLjDLqec_lUBfYlS-Ij9i8-CvYTr4olMS_BTrAbmO4RGAsLDeu-lqEbbzoYnct-KSwEQTlg0yfmL1LIjOxIbUI4Ba2nAZ-nqAPkjqxVBI5SA1VKbtoU_TOdlIjY9xmngdtWGJj1yoXA36FTjunhDk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbxdk8mnyaudSxvPPC37bGpX8cc7cmfDZjpPO4ObjEnqO0NsQ-0AVIpllseaVS-sWvxyvcCkMHem8BhiBMBETf3UCSOm9P8PEWJu-sQ6Xe7-NRNhnWgconb53usVhM_9i92skJglhzIRgOCsOiHH57SmGySlJ1Z9uD_3GcWxlgIlQaNHHywQHZ9a_5WVk7l-2h6hLXUVGQNAbe-5nlrxDzRc0C1aG42H3eVt3IKhv0R3QMfVCPDgRTinZm41cvl0DwWl1Q3kCyrUqeGSBuJMiU-c2igSCDGI5gtXwt9uf7juf5Thada1eXba4ZIOy70aSXtopil0B0mLPqSJziP8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjkcygl8AV4TBXK66UHkx5XMnaQSTUR-ugJ8irgPfywmI_YhcQu96aqj0H-sM_f93Jo4lS2GowU6ALO4thz-Mfo586guwTc7HP9V4t3W2dhyOvBaOsxTc11ARvxjW3SfPqOvyjZ_C3aYpg-ahLBVBx0u9CsVWndXxRlmrx4Ly8UDosf3Q4Jiey0KqZen19aDXd-qKW8KRSpaHJmMkY2guOjB_zPpoBa7DygWRHqvkvdl9eVYwsHO2iUjmjLOhk8TKKSfOPmomajdMap2y5Ukhd9dmA-w1-evuaCZmz6S4BZM9zem-rFZRaZhhfhQgWZNESLHHMPwoR-OCWnfumN_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp9_ZXi--1k39GArbIrWmB085UNhO3q0un8a4hTWoREpaaosP5YFxl52MNBZnJ6sJ0duBHSHSL_t4OSbv-dpV6p3wgAQf4e0z39jMMeLE-E158_oQQmMe8Y3cx-Hz1x9zVRNq_NVlOT4JwGSKSfZ7--Y8C2he0h1mXTEXMkRQj73GzkzF5DHLCw-CnCSUVCBmCS33ZBri2uXSHz3tw7lhhB19MXwiWR7HiY7dGK8xpo8tfM_qS-MlxEh1OJZr6gk84Xlnq1toqmpPLTLHKZ9CCEDxeXCFzzgLWgS47_IK1U2gWJMJuIrf3FsKCaVKZjziVxaQMknta6FH_I9ChcEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESNnSo9XWyeJxAMsPfHHJfBJHbAt1OE4I8lTPF8ndQ_0IQC37gw3h5GMw90TeEuPTEyR9ImD_MHD8-3XeSRIcLqMb9FdFboDl-nQJwoXgIAZrXIEcRR8NGwYRNvzd4U4HaPpmtlJXzN8e8at5duLei2Uhhr1nuatljG0gJKPWigGal1t4Y9rOjs6ZkE67J-iqm0aJFPlsKLqbE80HvqmAoY44MtlG6WNsbCZeEi_H6j04cwvHPOJsKYcJgr55zHsYC36qy34UfPw_5Oc-39SuDz8dSYcPtQhy1meJPCun2JfVP6TVfHwsn4JgmrSVthuet7_R44rHKtUQZinAUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0molnG4jUPPGvf481j3SMYcg3D5BpYoPPtYu2_eUYhy1ojzPhW875Lxhu-E7Wm994kl8u9hE77Ev_AzppxgDmcdkFVZGFbRs-aGNbJb_lrinjFOrqHDjW4eR694OlbcaOaeLwq-h0Z9cJOjpAs_0otICIbwwPJn_okadG9xjVCuCpQ8kXhKhrTAJTsuQkqojLBVJnB_l1RdKK-jR9jyPjEp_fuI0SXp75WNJzwS9GID0njRzzNpOXd9-h--bkSVEOi_Ui04KxnE1TGTla1M9LOJQLs8kOjQr-DQSiPxxsnBY7LkctRmLZqT0aV43NR9UTRQyR9CtHOypJ6v3f4mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9k9j7dI6Xr1X-K4DlWcTPF02avDCMl5h3BRaAVPkoeWy6_Yn83KjcVayEP3hkCKL6s78gGDhGoKpmJ1QFwhVc9UbArWqgQhmkcTvnpnA-6njd7wRqSYGRJxeipkccypn6SF2PLWYqtUcJ-Po26aOnIDE9_e5-ut6j9fhcgVpL2Q1ZvoFYd3teboQY53L2U8e_Bz5xJsCh_rAx78UTBtURZP5zsiYPZFL1yHMa4tst8YITcsbdX0rlCybdGuuXsqui2OW-euVcJkKr-2DO_9ylaWXVFQbqdZDyNWkmKoZFmHPb9eqOgZzHH6kR-LisqZrS2as52hOPMS1SRDmJCqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFygl9nbpfW4LYY1SGGnIzGpnzZBNQ7lJG1o20GVJQ8pcVuGUwy44hfLsfiwn9d53tY6huk0oxnSdTZ9cwV1_7uXpTkipPoQAPFNolPO7Vlxy2YMWhREKCMLGJg0NNCZ76LpNMxrR0O13lMmIXEY6FBvDDzrjOvEg6XRoGheOZBWvNXwzr6ZY2RsUFK3lWxjXe0oSjJcl72KM3aDbGy8zvNtE-sUCpFRvAWt35Bo-DigEKQJJILIlK5ZAWt6dDzMa2gDNS4THztWh7l2qt2ExcKGfddDeMMiVzPONbe9wr2xYaaX_f_tj3_Un5saz_QHjjWKr5gPIVqRunFxqjxMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYgmzXrYKGo-xc4h7dGce0_8LmJBzJnVML8vDYyNxm3BaUoFLTt7Oi0L8F2V-9e9Mb9bwOuBPSSjGOrSQwuOLRWqsF8UhPZfP3mNNPXfctGFDp_bg_dCu1igrG1OZB8J5EjOV_R9d6XWELRaSYZ775e-gpcgVir_pvXRqhil6FigpEPnn_98Y76QccTdPC__6KjwiR7SzL7P0_oAWMqGmGgMJo6iBlmFFiGITJHulg3m8Schw9bj6e3neQuaxZ2PYdzwlPcjPOPtREe57oFLjO6FGG8itaZj-BAmdbkCRZ_KavYdDcsJg-Ibo_HLBAe4IjxOzq9X6hs6tEdpQ8OefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkPy9Qmkiw9O0_4VvXqD30pv8neCflQJ3ApPmkDr4V_sjJIy-nKhfIAzVflswhZsvNEwVNR4QCLEm9lstmCwbqJ_SX-LOwqNZflUKNigBM9Sz5nvJ32CL30Jf8JnDxSibj2NhkLG6W5mlH74yXweQ3oNfTOhZFkgaEXz3D9r6-oyEelAK0xMaP_-Nm5xZ4PCguwSUDhPxKbWHPs0WaWWLKnvNwSoNacQRQ0DIXivtfMwNHt0TnNM5veIwraCuXY7vuLc8lo_p4fO5POOlHlOINj0DVuJ9HkTtq2gOluHRhiLjZPR6xU5UcoVCGZ7qNl105YScCo_G2s1ykOkT8R2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26866">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26866" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxOqHvNL7y2XtHohbs7HcT9loajHMotifeFJ056glTQLbtty7t6C4ankKL3tY5rbkeotrYe2bnsj_5MVXMUdBZQTc_X2S7G9_p25T0yG8w2acCMHR80grnncZwaf3gRwC0AgzK9LPbzizv5Opay9UvtDl4eXc_bzhaLSVsgaWlnOPt4um2K1zTDKeAAynkJ9hcynDRWhFgzYsV6wwV0Nb4yjEoHcXxa7PdRfnFx0OcuL5wnJg4AZyTT3xAdoi3E1hKFfzD9Q5s6hhVkTfNJV8aQ24wYPaJslRh0kqx1WN4Fpx38M1SXVrbfiRdYZQI4HNFoDOaqKAtiaWZSOR1RLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVdyl7m6SpLEj5-y9PvCseuYPXaBrE1hhr8i7s5poPfFUsh4BhuFL5NCgpSh9ZuYDIP-JXEbl5mbaEGfZ_ds-n8UMwNdJQmSfVinHaJEnsNbVJ9UHgjUIOt_u44todVpU4UuWiOyt8WTW0a4aL5Cpnhd0L5AIiQzbYFUqauDLX5dhjVSgSHQjSHwWdPN9h-j4KgQQHnKFKYUCLMIpDR4X81KnJPEafjj-rTyn4FuQJFyJwtztvNAO4WfOB60TAXE3H6rhVAxhA73Nro97daPQ-PGOWSyZ-8N7OQTN9J63Mg1ISxWCmQOYvGcCk361URcOByndYu4vBBw9TyLcwFg7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMilaqwP0FNTWeVxbZDo2HnSIpjv0D0dGI-wCMMUGO02JvL3Iq-9nFHa7kFRcWZUXFgWqa77Ynmu2qprIp1nZm7y8y4Z80noQc8jE5pe9IkSLOHDOLx1ibtKDJ9ddQB6Uie41oGJmLWl13JQoPFsgO-f1cIpdntdBqD6u9su_JFadBPL-t0XCj59QcPM0nlqpype1eUYAHe1RNY7z5h3U62SJTIYIXvaA-bMRac0U4IHnmNeF12R9RkMr3VbveOoVX9MB4EziVhyCuwirWmISOa31LstgUYvT4R7YDnpLVDwZjZnPHRbz2ZLNQWVH_tDO5IoG4_o-0xE6rWc8JyxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osr4opukbslAhN7-Tm2Od4GYVY-3dydjaowNodPiJD1F1MFQK_1f8mcZIuGiNlywV5JPpvhDMSnUvwkzpLJamUc12WLGJXwMYKgQfKxXj9YQooClH0Ereq1G-6aoMTXpMItQjb-6r46KqppE2AeAz6sMhjZ5pifBBrwrIu8cIf5YVksbJIFok4Eu5849sWSM48uGwIOVG1jw4JMZvnb_mPtTcrR5O_UR10U6wodKNnbS4ofyupcbVSof47FBM7QJC6KUIRTS0XWgh8o56wBngXZTXpLuXrWAMPgwOUjjcfvrKZoNPlSFvex7R5QsQJi4jYqG5Oz1k1Pz4-TrfoltSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jenlfORIZweTyG0jxt-V_sP8y1O9XCMm7ETKTq0o-ovgU8wCeujWQZUkYTJX20deGs97IxQee8owf6x1V4GPcj6mhWcdkYw7VganrbEYhpBtg09oJ1Wp1Iiygzi8f8A2sMjjTwNZHbj5O3JeNNwUUelM-BHRDaUwc1I7q7YXK0Qh2pf8cQ80bGO4vWbKtlywa2t010aWrGAp33_nmPDOTVYXsND61tSzmQQ0tG5eA6ZqbFeAV2eHSILU1DLvUqVro9rvgvEZ6pB2GjALC5E5DmMtB8zZpn8gbnsSXVwHS7nPQPKha5EiAVKOJh6rOFhG0mdr1oI3LKnWH_uhBk_M-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG5hV857KoOedEvkzI1yvLGN-iILAWLGJdaTrSQ5K_vU3bzFtqoCf00V0tEQat1KebQ75SegotjL4TY0GGrdr1It1zcs0RvzUf53tZrRLocg8Xdw4S1SsSr4OC3n811ziJpLNjxE_ol7wlEmmredSX1_DjqzFTYtHH1NfsIPKq4z6uzbemmuBNBnt_8OqPPJM2nGK8PwYFxi1pYHowWGYBsJPCBitHha3y0S6-HMsDMvkrXPUmSgfselmSB-wtvDEYjrdjyA3Ku4pkvAW5UDzWQk3DJ67c5nZvJ7k6A5qp71-WDjM9lklBqRGVOHYH-dtonAD996UbWSZvmYlP21BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbX5S94cxm2I5gUBW3cso8nvCDOmKuUG-WfPBNfMiOFlGKBCm5udACeF7Uf4KUmSK3UnCL1Nk93OfGQO88GSToW3YNPgBQpthV4cJNiqblByIm_jaFm1538B9JZxN673WCSk0OYzjYTFacDB63rCTsPZusnFCFkWSQdIe9M-odBdU1xkEDFFRkHdHvcmVUw9pRN0sNCfj17yRxrv09pmjC8H2Tu9ECowmcpEQSJhoNu3_db-C7SRkHprVv6Tfc47vba4xX5uFhYWkjo51YpunJw9ZeMrSE8vd0s5BrhgHV3dCTDw_pC6cC5kpnwFeI715ePtCCmG8zQdJzM63mX4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNkd7jJeRVTrmrhQbqCmPy1l9jZdBjZUgZU8PqGh7M16Vxlx6tlFZMdLTh1_lnxcNo7AGBKXkzd3YTSih7bMhZdKvfPahYqrBe3XeMtszx9lgNYJMkmbo7VNhQ6NqBoxm9d1ZO4m6ZowAIcnXWVbCpAPW_ibHgCbCd_ByLQ8ml1HOOW--CEhSmB3fkRHmgQS-tJuw_NIwALrW1DuBNEgAC0Yg3xyXU8xZK4KSvkUr2WLR0CYCAVMg2qQK7dcVpPK2baDhRx3hmmP_q56MJ9HrVN7tFkmGZoT0J0Uh1Lo86FosaEHUHvBOFQBhLqeB4bxzeXzQhvQrZg-Hzs3kJXAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY6Yolu_zSkFqK4aCRboTnNrRNYXf1raZVwWA__IWhVuQJL1U13hHKHtafSWOnELmipaM166RH7vUgdo71zgleAMnz9IDBoB9kwaLwcgkLkiR5kc3mCBj-uIfAfGO2Ywlq2KZsEeDi0jbxmeCvlfsTsEM9S15E4vEOh8e9OqDqwuguO1DDd5ZLzXay2MRDkv61U5TiiPeaW-QVrIk0AZ2SHpsX-Vr36j5PQXNfZyeiJaCtxt8FthWFyJFu4BeqAKJtbygJJtjUbzlWoyCia6c_BES0FgNmmLWoEIOAgkm9Oz-cJgnes_CeYTyZfJkTeIr7sa5xk2GEqa32VCfQdkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0ke0Id6LJytKfiji-sHW4CYThCEt6h4CqqJByZ7eSSNtXiASX8ttsjNqyODPUyW8Z-yo-gy-Fe2irMdIthE5ky-KQTYRcxWloCpywnaGiNrrrLbGqcO1bGEBx-TCpHnTyD-VmivlzHSjk2lR6XHqutsqRsBctIRcAbbhKcsKMXaRmC9Pqojj6c13EqeIiLY_NLUnlOzio2LSMDS-uFnIGMWAB2pOKLAshoql6ozAqub5JWZe_EjVu1sMZx55S7-NfGLWbRmdVSGeEAeul2fkT0Fv7eyTyaZUCQmYE8CTUYJq6uzluX1sOyJRvI7VZh7HlAgUE3faOUKTyVg6RSyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXdfnCWV5Bgk5UcEAw9zsY4_NXxpxZl7PQAYuLqPCNOoL_O_lo_7nYxbBQ-pgOtJd1Vfgy56ca2rxkbaUPqMJgTAZkFQqzRlS3G6m_7adptCQK1ImBUYhItMG9Y_9s7dRYWFXeY63tA03a9Ll1d1sIOK4poy6UVxMVhvLcbPP3tBqQaUtXr5psLjjL56SUvtLv0ZwVmr2Ain7gQ9HbBLFPapMTcC9ZSqATiWiC-abZH-1dSlOEG_OVMGEZKAWIw6q603fQS4i_3HkokhO7c84skCQQ8G0hQ_7MMT9-3lOdHz1aOpfvrEfOqAvTB7DwKvPKERd1otXfdO3wfc-fN4GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbijYllHYfhvsh3N-JsG2Lcb99uaes7Doqy4hQ7Jta66VGnygtMk7fvk5uZab91QQwWToo5iVfUaxPw6eJU1I9HKroB5kmy7QoWwN4BSRKZw29U532uHgdbqjhzJdYbrf3b6sqbycsY8_AaQURJbJyw9fvC6uorGG3M23lvVn1CUY8o9si4PqnnufEHvm7dF6BVVB0CpgSKIgKNV0bh0ZpfZ3bT_8hi9yche0d-RDeEm6ATIbAt88gUpJNNf_lNFcePQ0EGXgzgdy3Zd92zQrhMN_ElUe-Bo5uK9qW97UzQbkf5G44WvHZF-pzbrhgJllqa02mZLD-u4QRNUYEO1dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSDsaZOm8VXOVYsoYXjFC-U03RAsUvo9Xp4nHUhKgk-mUnLph2ybyKT2Kt2NKb2iIvh-V7ZubdzGqLtX4LbGYXZ34v1xnBxR2duoKh-1XEFx6xL3n_J_6dZgvAa8mfOT_TiOZVTtLWLfLL8zi_fHrEZfKTpN4ar3DniVs7FO0okreiQCKDFxLbeQj8TqBFkooKFZ7NOkMkfBViCbrpGgoKRH0h3Gtx7V6wCW3TzB8eCdAeE9vSQXlJgv_grSWCcPSrI3lg-CGH1AATttlb7r5641ng4JdkXU0vwP4cu0KadkWH6c8G3Qe-zv1QwyA9ivFW8bOl4Zs4da0MRBqdsI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5sit6oVvERS2K3DfiLSpi9G0InuT8z2faeL9CsoTW5QJ63luvEvBvZuYBr1S787zgWoykVB_TEyh6k_k9Nk81k4XJCE9VMcDE2zZB02aCsY3KFUOR8W1vTTJjwaWc3OzaKx9P7t7ziSPymqjXmuJSHO-Fv0nWd27I_JuhuCmND_69RVoo0rakseupC5obaemDtnDV3x9qtTFh8IMpMHgGL_z2bwVjVmor20XIfgK8GmzO_bgSE25bDzghKjmlrzMSyPDghw0CWm6DW2DQwNF9PtI5XAjV2qu61ZJSs4f5mJMFN_Anydnao91eGJ2MivLbZJKDMJEKIwnfo6nyTRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t85AYpx38dtmRF1Fd-69PAa8MFC7LkHdRIIs-5d3XK8NSlu0VVcreu2Fav05Vcmwmd1cmTdXDGCegO2CkaOc4v3XBYzvmu4msUvvaULUuVhA6GO3qTsbKQEsMtFXPz8wbSlq24CbqAI3ChOhy_UG_kS9YKnfyFs6IJIG3J8ZdkiczIUeGPU6pptzG7mTmOXDHsUof6w24NoelIk2O6-wEHQ3_LxOnu93etavgbpXalNxYqvrHxWTRsLvL6kE5bFCa0f_YAgbL00C1PsshDTGCvCv3dsM2etWfNpveh0--UhIa3cwcUSs36wHrUcc2fMyh7VGdCev80xb-7bFkWEMsthI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t85AYpx38dtmRF1Fd-69PAa8MFC7LkHdRIIs-5d3XK8NSlu0VVcreu2Fav05Vcmwmd1cmTdXDGCegO2CkaOc4v3XBYzvmu4msUvvaULUuVhA6GO3qTsbKQEsMtFXPz8wbSlq24CbqAI3ChOhy_UG_kS9YKnfyFs6IJIG3J8ZdkiczIUeGPU6pptzG7mTmOXDHsUof6w24NoelIk2O6-wEHQ3_LxOnu93etavgbpXalNxYqvrHxWTRsLvL6kE5bFCa0f_YAgbL00C1PsshDTGCvCv3dsM2etWfNpveh0--UhIa3cwcUSs36wHrUcc2fMyh7VGdCev80xb-7bFkWEMsthI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdjAFO-M_aZO6jXjwEVmK7hfjuomq2yixDLWkbCqkeYgFiQadlGf7m_CZy_MYPFett9Gpjo8BEVU_05IlSmtznp0iFazaTKejSUg7jwO1P-liGbqN_KKUj_WqS2TRg9T5AhGiR9xG3gsRYwzksX9I3ldwFIgVSe9QAY59Yz_Wl4Cp517aiqkxlDmIeUuRAFaK9tSgKsk2crVYtqL-TCFh2TGYuxFfSuDYhxfVMMITuDymOerA0XSYQPp4r7hLm90iM5-CqM-gLyMcG-At9xVZqssarLDWWR_cvpE8OpchSKuDnqJePQxGoxGwo5qR7W8r_f57bM3Rd8lTAmjZC7LUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9FLd_o20Pk2uvxC2ZdMn7UzajO-Ugtzek6gnri6Y5XsSqxQsGmdfIV7UZd7uCmnpramU9UqqbvpTSUsh6hTGGlD1nAnTrqNdXz49efXpEmZAx6ZXzRQQvZxU_pINMpyFRc5Woas0JNYyKW-PDo4AjQ4m9HMis2G6J7m5RQUVk6Iq9cFcmzdn76pECB2nJWndzfNr9QopgKO4g4yn8shD6cGiiJSpH3HckBUtAA5BU850mdy506vsGHraK2t5zUAj3Y7BQGq3mzeNFZU8_B02w4FNgzhzdM7WE-0W8zGobOCIz2NfR_N5hSmUq4vTGvWsmAzo22SxU56oG5ymeTb5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7S_BT4oHjk_ZfCTYxrs5lofuZvEPgFShfjSgbEf93bJi1rCcMFYPjeONxGxDxzym4BA9QXDb-bWrR3I0_nODccWWuk8ByfBJf_RegUlkEF4nrGf8weByQDwvv5w5BBdMDZzvmr9X9aEiuMK6d5RALfnB5k-nyYVhzzMTiLATJj9wDNA23p_LWwxIfjr4po3ZOQolFhK7p9FY0PPENKFRBnho6ZTCnuc8fJkvRZ5zTTbt9zxl9TenbBODUfFCkKswMi898GJSCGB358iW-5FMJsu3XVxFETcPBzO2GQ7UvxJkn95ZtTWdauuE6DjQkHmDe6mHrFJeT2ElczVBBnl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eegXSRjFqnFr11YdTBKcJaWf6NCjmInkbym0wwpvpm4sap46mRfIQVswkQtPxYhjMurJuMmF1zKIV14Nv3zZYKYeD1z7AkSCm7hWX0kjhRGi985ABNNA-UJgb2WX8YD_3SNHiI1LCxonzeM8iFsjemc8Z5KeZP_laa-kU7Jn9nx86pT4g26AaKNI71UuifIyBaqnfPXpalcClKTIeM_ZKhjlK4vK0VHfaJg91LoSqT7_PKHGxmEup0yey_vETSQlEG0_1eL-h8OME0w6MCRXMGBiiyIMkGUW6GlCSF49gier_Ba5_oOVC3SMWCxGmir8yphfp4WjTOxFXsYAHc3qjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuENYisu1ubMazYta6szm4q9pDSQ0aKhb6EoUtPsb7tPvwGC9hysNkYbluy8HZkKsrrP-5a5fFfX98QxyXIPz5vLgPgy9-N32Sj0ZSl2WLg-vnefffCla54AfsRISaRW4b79ky25APALquQ06-IQnfFot-Ajsw3QPZ_CLARJwDwTii4QnkXRN0CtdcAf0e9ewuYAtfK5lDMNN1DPeuLWt2ep3NhXGhEtH6I6W1bITL2FiGSXkKNmpxIQ2vFIcF79bIcgeTfIQ147SzDIl6Gj1V182BdlS31ErSCXrKvHIhTCYsS2NsZJCN_E4bpKrM8Wzp1TGNjLEyRycU_F-0-Qfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSt4SKYRi0F12fKKFcBzA0uRa9rGZT9y98Yds-FSIKeITkYTAHE56VHtowHch0FPSCxI6n7EnG3VuGjTkLgdtek0ehgcY8kOxzEQG0ltLJOTAs0PSRa0IUPPgzvRFEuRuVE6JALAVTqu5c582BPfUAnpy35-bnw-levKlpNUbzXLxRDNnSE0bUfXYBPlVBHcKSYIFsI4vnZ8RCGS3aGW4pR5k_ExUz1Q5WxnT8W1KypOBwYXtFZhyTcbEfxQhpFGiPV5fAYb2KBvcQEqtofkAORieCCucEhovJL5wRuGeugwhjycLHs0Sm5jp7ynGqJaTr555q5_nWRES69AuS5_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYLTrabtvahMkNZVQ9H0AML7B-fYYY10qAHNSsXf7V58pDpT3JZdTZi_B07ysfkbs-8pr8XX797oGgQA8iIh_f7QSJtaQLZ97jdxWsHnrS67rEXQ6nmm7vREwtkNN9L5cvqKXo43lXa_snE0lvu8e2R5tcBABPdswgSK3zI4xiGj76cSaaRseNtP0rid6U45GTi9elucYgBHlyPjU-JREOfjH1BcJzxgrKx3ePOwhO7bN7tMuBzvswv6PSYVuAzztt_fxdJWujSLUYjvb-EtSudAiAPSFJ6tWuFPlCO3qIvCHytokJR7vi2HdXxMYOfLt4z4IwONdbHOt3jpez4gGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOIb52Ulqa1znYwgj-DTqYi3gTZwVvr5aSemPMb2BEh2jb2RxB1sB1bz5kofYMW3wwa_VuORDbPuAYBKiicds4yJtmt34_hP2k278hTXq1mK-qbMcicQWzCLbt10OyU8KrZuPuSk-XBsyeXDYpAGK3aERn_WsIzZFP3heQvWi2IWM6GAHbNb9Ydhr5gE76MrKstPhqlfD6KiRx0cPb6HD_iNtn0y0mH4tGjKlGObRFbnmHKR21vXvBXwRmRcqFYL1lRIBJA6Grg9nmOyRRdiHyoEmR9miUC6XDT9zcvdsvv6BlPXQYBgbrD2w3E5OALWl5VWETpgeMkdWLCk_1NX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVwX2M0R3mKen9yaMihI7ago8VKy9rp_S9sD_I2VZ3kP-9jUA67h5R_4nH3srNqVYl-6txV85RVXxaF-ZGyRUEvArt69MAdrHqQOJUiCuoMugaCaTVW9xB4zz1VTkhuG0MnQqvd1vuOonq5zF16Y1dAPyHjIIRj60vuI1QfT0oq267xcNeh1OGtQnYy_k7drFCPFYNdWe0TdKFo-0wjhc0qCXKpaRaQPkXwJ-I-MU2gaSQ_044_A1Em9stLV5_Tw6L1PgUYQAOB244PwLR3o_LS_YhYbXNL-EGGKbpjUpJ4kwd6t4YwzIHVXTn69QNymwy726mg8UPSTjBzC7kxJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_3__sxDyXWT06aNb7m56hIEegGvt8fFwBrfRYETIcUMxdn6nJ5YbEn-jNS0Icp5uebx-HJra2VxMy3oU85pOTJPHN1aMfhg2irNdmEbnB0iP1feqmZ6j1cmCmaZiT_t_SCpd2VVT1Gsx0Y2b9s4n1QylHqdmWNOgMmNcyFPGYgIIO-jDxbBS-tCKwX34bJD_Js7Kdw9z09-4K7taXyegn6KZ8Y_qPtnWwY-9XBn5WWZ5FiZr3wgib4KfFRryGsY4VZB9Qlf5-m5u1JVFN1nWopPfjBSkYnKGDtKNTLOqf8T_8utUh9W4gXpph4fMgGBeZ-Dqofwbr4jrWGYmflvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO092Lr3x6wsyF9FtjDB_xhBrl7QZEAwnuIgjWPPYIanHsK03JI7EP1h0miOib7FnUxCVwl8uYzKFPt0czpuX-1VwvuIF0JmfHsrvmvClXgr3Lt9s_2czLC9g29WQpoG3t370jFlR3wLiPY1IT0TIBdyon5ErwK6P40UzwvvIDJUl4v1h7SlyUR0a8Ye8J3VCmzQilFCPcWFRc1u5uzVtyTm7n7d3tK4P8AvJsbbeupc9a3mbdjED1L_sqMPgljnxZVcAc_ih2-5GGdFHXDhmq3z-bntl6PTPN4XnaOJGbD4SgGZxil1bpa4G9NewvSiBWCu45sZXxV0gIbcVmhTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=tZubeV5MbZysLkDHUguwXiVKdfYP8GDUVAYVlM-EcNQ7SVUrBpAB8hixxSmouJ_E3ZrehFChZdK0y8whhEpDtx4xaCHkmkQh9-Edm6luTK0PqxvVFzFxHviN4JpccQVYzORzGz4a8xVg-34w-xijwkXos1EP345VF_UiCizkyx9_KjfOKlcTIBDLrv2zYrJySLWcWKlMKdptG82XMF-u-agPGnXWzXjbxWYGkSQBHb5wswsdGdJNwemx-9Y3Wlpiwt9K0Gk3h8PdrK7fKLKQ8foYUbJSWPllNBM3Wwl9pt7JH7vbLgl4UUBVKiT4EhOI1jsqHnxUmIwuBfsKDaASnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=tZubeV5MbZysLkDHUguwXiVKdfYP8GDUVAYVlM-EcNQ7SVUrBpAB8hixxSmouJ_E3ZrehFChZdK0y8whhEpDtx4xaCHkmkQh9-Edm6luTK0PqxvVFzFxHviN4JpccQVYzORzGz4a8xVg-34w-xijwkXos1EP345VF_UiCizkyx9_KjfOKlcTIBDLrv2zYrJySLWcWKlMKdptG82XMF-u-agPGnXWzXjbxWYGkSQBHb5wswsdGdJNwemx-9Y3Wlpiwt9K0Gk3h8PdrK7fKLKQ8foYUbJSWPllNBM3Wwl9pt7JH7vbLgl4UUBVKiT4EhOI1jsqHnxUmIwuBfsKDaASnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUZY6vJ-V0pBIIhTpeLC1Ofnpiwj_fMNw52KisMS56P9LvtyWXTDe5cukRmSzLhyListUTOQhdhyyj4r3YzBn2UJn4Jbttg-O_jU8lgjBiIuQoZNtA2UCfXgwEOGb1Ij2TSrsD52kd6JeVtHb1waNIQrQea1wX4ktLqZgv935B7CLM1GAl7xKInVBQAZIbBnGBMedkjWXLfSu1L7aDrnTEJM6Ec-qaRRuOEqfHmPDgDGFgzu4lKVZFtODUePv97TnTEAnjBIidaP1jz95wGEUMHs9yIjIyPXfvLICF136AOeZywdpYGM-2a4hnJiKSWOmFcNufiuaqWk1QIDCxJUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq_X4kOaiiU0vJz8fYJE-D5Y18oG_0zEc3Fl9H7i9RkUyKK8NPIT_ruqQSyQHbNYHXe2xVzSsmUsH1p7K-WCnaazooUQn3-Hu9gtMtXphLnnSTBmZTGuKEuUCsYw45HbJDE6vJ23UCO_yT0sddIgiU8nELXsBWG-m2hQMi0XpgezzcvXDYnMH0CJ3PIl_w0J67ABQzIKUPjZvEJoLU9FrewOvbCZIuwUij9b2Ki4gSFMBDKENV_ZHQ1VyNZzjz50uTkhGwxDP3momhLoJsSSnhDJrQKcxMwscU6PGQvYIudDHnmQ8I3O0CnhEakWgvWfQ8pAGQ5B7qvH530PfukuMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6YagF3yihLdxgFt-pBsulugT8lKk5C4Ti62LehOga_NTuaIrT0lAF7xnM2eT-B7En-zy1B_d1DxXKoe7QGpJhUh40UJY4aHuXW9up6JJLI1U3mg760GwrdGDaUSMaLasoOWbo4g0W1qAWSFIkwmtk7jU3qFww1tHIt6k7hlHfn5BRzLtkR9zsHm1R6o3RUNtZIxvtbFRG-vaQFL5Zl9pvCu6So9TTDqG5L4e5_U-GedLNAsqPfNiBHvLCbbfprENB5nQ79Nq2b59IWLQY6Q9aMzX0PiqMIFMt-nTOfupTDrHcZaLf9rnheK94zRhXdSMXeZmekTgHLBfMtLqDRGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=Bu4F2f4YSWI6swdbV3KddhwqF04FQsy5mPohDSDahK1U8xmT8esXnk6gVdjEp0lAyt3IN7-rAZq3mSE5msBmOZF3ukeeyTFJ3LqaH4jFa8bly8yJFVsRqHJdcJ90H9UdjdkUEmU-SpjnZoS81PHk66CaIsbBz4sP84Vlrq1M8Q9DNfPgT9uTz2qZ01d9pVG0pn4GZeihKHcpLPvci4KA22jT1vzYrBalgtGHdOjxUXZh9eu4jr8ZFe60RP9KRvD-asL4NpfwQEfpIybyAqIvr77pJBLueh3KseU862HQR6MPbVP6m-rO5WVdiFVrF8BBiu_aWPtvy-oUjWu-myUq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=Bu4F2f4YSWI6swdbV3KddhwqF04FQsy5mPohDSDahK1U8xmT8esXnk6gVdjEp0lAyt3IN7-rAZq3mSE5msBmOZF3ukeeyTFJ3LqaH4jFa8bly8yJFVsRqHJdcJ90H9UdjdkUEmU-SpjnZoS81PHk66CaIsbBz4sP84Vlrq1M8Q9DNfPgT9uTz2qZ01d9pVG0pn4GZeihKHcpLPvci4KA22jT1vzYrBalgtGHdOjxUXZh9eu4jr8ZFe60RP9KRvD-asL4NpfwQEfpIybyAqIvr77pJBLueh3KseU862HQR6MPbVP6m-rO5WVdiFVrF8BBiu_aWPtvy-oUjWu-myUq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWad7r2rx0OilRLHtIsHI9i59Q-1PMKls1q4J9eQkMcvHM4mLscAb7sN1m6LyGhaZSt7_3anJ5RSXyG-uQDlI4dKvdBiqkwEi42BnEbLnrs5c4AtdW4akNO5hudDEfRCoaAqR_WUJKa6DYVA-QNHSyTYWwhoTYCccWQK-IcOkZMuyb9md6ulvyV6rY8mXLya7ebjBWwcyQwgWPWF06c28LZDPKLFeNVjlDveTBed957rSl8XQNmtiMkr3ZiSwJ2rBxb2gPA7JIx8PVbda8xtqldl2ikl0rHsVz6eMy8HTrxLlfr5QE1-h7UlDf5WNhVYR802gAa9uMxTqvzid8WLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1u2KH03zyD6DDmzKfuyyBzS-SvdPePOLghMD8-oCuvcEzUCT9Fq-6Ip-EzaIREdLM7R1v9YVrC9pSeidssLuCHlPo1j04l45YqC8z4I1OSrtNaHIgahpuoNX6Hx7Do2Cc83DUFTJwtCrtA7uKAF7Q1RS8ZawczuEY1fAWDJrF80T6FK_jgOCEnhiKiZJIvYbMT5J0VrDC2jJa6vZg8-qL4Uw3tZ52HFaa8P92yD2fHs4weORMBwOy_mXELdIAzqYik-XZWH-nPbwFC5Qi6NEhzyueQiYrSil0j3BdthNcmQr0I0u2UEQ0PeRQ_K9q1m4T0cEt8ASGLZ_4v8Pn-bZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFSyNdih_aANNKechioynLnfYd4ztywRGY15752Mf4g4vr7UtqQdGKAUuN2on0T48INHDrMy58bo-Pn4hiKXCVV0FwAa2JZRxcOTnlHtHbWBeY7Z6iIfrd5rpW18EisgHdMN4mdwCB0LeStQiJ3i81tlgvitHRKvFoVLAOWPB2HM68pSxK7IwmYw7nOCvy1Bd7KeO5Rhg9BOdqZkUJyH_65hAjTQQNtdGWyhcP5Ug9jRi8vMmrzWFg85OmK9FXl2e3pL4tUOkgCgkn11EWUqHBK9DtZsSWiLgywaRwJQnpu2kDjyXf0NME4mlCOUH1_-WUNumbuTIA3AVSkuglNqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=LiVO1hPv9vq6u_9v3QkhnjHLZm4s9X4b89gdO9crjWMZAAjmbsoH6IhQl2broeDNMKjsFMkDuyDQSelHx7xRMmjcS7ttJt6zvEle-eXt3PybKp0a5dYDPdAhhdyAgOoyA4R-fb9Hf2ncXLDjytzcrivZuRWPvjNg_Rt04PzGyYiGfYlBQtYiwl5bA6JwIjoXXBp_q5HRr72v8lVY1OPmDaub7NwsCp7dJoHmqtv_cpFMXNQteMNVoUmDg4ZirfTKD_-9GDU-l05CwOmXZCCLpDfXAnjzuvsQHq_FSBz4ELxT76wvbPmjZc0xH_Sm6lYC2pcbBGshMTo0BfzIWarJkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=LiVO1hPv9vq6u_9v3QkhnjHLZm4s9X4b89gdO9crjWMZAAjmbsoH6IhQl2broeDNMKjsFMkDuyDQSelHx7xRMmjcS7ttJt6zvEle-eXt3PybKp0a5dYDPdAhhdyAgOoyA4R-fb9Hf2ncXLDjytzcrivZuRWPvjNg_Rt04PzGyYiGfYlBQtYiwl5bA6JwIjoXXBp_q5HRr72v8lVY1OPmDaub7NwsCp7dJoHmqtv_cpFMXNQteMNVoUmDg4ZirfTKD_-9GDU-l05CwOmXZCCLpDfXAnjzuvsQHq_FSBz4ELxT76wvbPmjZc0xH_Sm6lYC2pcbBGshMTo0BfzIWarJkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQAz8711pmJTObNpetsgcl0fN-6IdDCyFDtQ-p_oL39HsC8J0q_4GYIcPPQOJE3b-YtrpexUn_9io2lkwULKBFRVAWTAf2iQuOAuGOqh4QJYrEezeRwQoGBf8URg-zoWY1GyBD3FNEg6rTop_RYiqRhUJasaDtDtaW5GmFJaNagTun93FV3oXcSQLy3l72LX1mYGebb0OZIy9G7Nz1iOZhQA3RA84iDCNqi-9Sczmwjc9kUI-usihDeWF80VR6oAsW36Ss0FpcUFsPblNcphw2xMCgmfMM-EUo8N3ReSCOr7Bvu_hja88abXASE6rRdIv6Op8kfKAJyK-HhbjCKOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=i_5NI2D2s7H5AUPxv0yEcpWLug92qtJ8q26o0RrYZlV4KP-VKUc-AC6z5NSOepAZyTBWopdswJ501R1WWXlj1Q0AQa2B4WV2crIeBzNSC9jlvXy9iMB7ef5ceCQ_322rFJ-degu-OLiVeSMXqjlIWYlSiVSsUWVnLoakNSXJ-VC6M4Z1W-m3PUSSlsjYxnt03Th8f-t8OKMGrglSG91TFUIe_IpzutqVDP4KjxiwVsBnniftTvypwSDDq64EXRkDMfyiL4uWUkQGomppWfIj-fMROiMriruoZg4Ni4x_CP0ze7VC0CT8-1f-sa0HppHdna1gxB6dOHx6okpVvm9v7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=i_5NI2D2s7H5AUPxv0yEcpWLug92qtJ8q26o0RrYZlV4KP-VKUc-AC6z5NSOepAZyTBWopdswJ501R1WWXlj1Q0AQa2B4WV2crIeBzNSC9jlvXy9iMB7ef5ceCQ_322rFJ-degu-OLiVeSMXqjlIWYlSiVSsUWVnLoakNSXJ-VC6M4Z1W-m3PUSSlsjYxnt03Th8f-t8OKMGrglSG91TFUIe_IpzutqVDP4KjxiwVsBnniftTvypwSDDq64EXRkDMfyiL4uWUkQGomppWfIj-fMROiMriruoZg4Ni4x_CP0ze7VC0CT8-1f-sa0HppHdna1gxB6dOHx6okpVvm9v7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMf_68lSMzErmtxqQ19Rh_BgP3miXb5qZO30EiZOhr8SxdSshNyddltSgC4Ctpjk-HjysbtP1719SrPwMJjUms15h1QXU12Cg1pD2vl876jMgCllgWpjRWneTUiSwjtEat60Yli4ReWoIOEbHioB-RuAB8AeMlTiUKx8XCtoYQgrRHRgshfNtMcKw2meYlPZeGTknhnY7hU_MZeS3Qipn1QjQvMjkyIiPB4RECClzqzHH4FuySqRgT_R_3BypYj25tKafVO2JanEdFpu8SOB2W4A9vB9saglRkvQJBBzeYGnN_7Y7uFMuylCJySOQSeC8fFdL5cQwgpHMBGaHJ3rSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po3vTVrTALTfW0EAzyXmZDyza_ZJNHQ5tYCmR2NnmjoDZCoB23A3dUN_GY8r3QJs40ONIqlozok137hX9rpyVX29_VpAmZNs2jdVsi64wzz29_uVjegC0xv1T-lMVnXqXO4Qcw4TBMT4QhLaX0wPdXq_ciK-szdINOHPFYaO54Tohhjtx_cqzP7ofhZ-QBIGBOoUX1ok1OIrhF5jQyVP4NhQWyhnCuDu6HaV8DRVeCKLTZwNMx4J91Z14yfBH4RM8UYMyH1cmJkUuCAgFx9b908E0I6n-nfSeNmcI0P_qk6jYbX2CROz5URh8MOyjgNA93Tlwv9g94cJDddJTBIjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=sBUKUCYrgjeudFQ8qhvG_Ffiqy2ysWmonQu9pM42h2nQqGC6iyQVa2Z09UbfUpUB6Z9YTeqLUQcrTvVHRa69t9Xrq1_gToQd0cUf4EqMmdFKMBM9As-yGwdfRlPVBjsPr8jaB4OWT3F7smaBue0zB5UKUVxYG1SwEVJvDJ_m-n9Ne1n_wMJt23GADBaQVNO7WX4aARepf0SLD5sShRqi2hxhLZWoVJ7C-yLHBGW15HG9WXaaZFxy88ki0qpVTVXkhgZg-tCK0ak9LFK5EaFHLIPOjVYqdZgDDlm8xSAXjFpzasP6koyVx_OFl8eZl4rPTKz0efHyOrnWegIZf1Vg8y5ImrGGVGFIotwZUKGmCUXXEu7ZPMKzpdMvEuhVRAFVggIiR8NFJXuwX4u6fv_a9AJPsKPo-61Ezoccn---K0vGEVuHKrHmavhc9GmCOytgF1VJ2j-OoH5KbbkBUDLYvPU8cp3uAt_8IV87wsTAV0P-ezLkcSnP0_Od0kwLkcp9WgeGtfY_4wXKDaW8UoRM-_c-upvTmGTYCuWZbtwq6TXEfRSW_281zwXCNcSppLSqqWxg4vSUEqm1eN7k_6wMg5Jt1gLkURgiTtgcqcpB3XFyepWLpRz4mRa9EKt5hLoMtfL0Jf2fjn-GH80jWveAU8nGnXfDTt7m_X1Yor_XLk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=sBUKUCYrgjeudFQ8qhvG_Ffiqy2ysWmonQu9pM42h2nQqGC6iyQVa2Z09UbfUpUB6Z9YTeqLUQcrTvVHRa69t9Xrq1_gToQd0cUf4EqMmdFKMBM9As-yGwdfRlPVBjsPr8jaB4OWT3F7smaBue0zB5UKUVxYG1SwEVJvDJ_m-n9Ne1n_wMJt23GADBaQVNO7WX4aARepf0SLD5sShRqi2hxhLZWoVJ7C-yLHBGW15HG9WXaaZFxy88ki0qpVTVXkhgZg-tCK0ak9LFK5EaFHLIPOjVYqdZgDDlm8xSAXjFpzasP6koyVx_OFl8eZl4rPTKz0efHyOrnWegIZf1Vg8y5ImrGGVGFIotwZUKGmCUXXEu7ZPMKzpdMvEuhVRAFVggIiR8NFJXuwX4u6fv_a9AJPsKPo-61Ezoccn---K0vGEVuHKrHmavhc9GmCOytgF1VJ2j-OoH5KbbkBUDLYvPU8cp3uAt_8IV87wsTAV0P-ezLkcSnP0_Od0kwLkcp9WgeGtfY_4wXKDaW8UoRM-_c-upvTmGTYCuWZbtwq6TXEfRSW_281zwXCNcSppLSqqWxg4vSUEqm1eN7k_6wMg5Jt1gLkURgiTtgcqcpB3XFyepWLpRz4mRa9EKt5hLoMtfL0Jf2fjn-GH80jWveAU8nGnXfDTt7m_X1Yor_XLk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=S4jgUa0IzLNaD7IazSlI1K4oOcmJ_F0j_JpszaW4IKjXbFu07Xj9HQeDrAu9RHEOeS5b8Cc9vJ9n6rIVLJ0GJIAplnBZFOPeCEA6uCAMvoeVuPgSPXHz2hOxoApx-7gLKdchvfZa6XDcEKzZwzAiUB0ou4KzbVsCSAiDAr-RAWUZk9n8Jf5FhkVuM5h1CbcVlJzZ2EO_2qczcytkBVyapQPUNnm4OUB9eUI14hqxi0CYtFbPG5b06BOXYEGYZCxue9Dd2fnHxdYnPrQgF3TiYDCl-k-B8WpO8gonKAOCCTBs2NYTkzbMvcl8ezT1euAeujf-mO38B9vcnOPd1DG58w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=S4jgUa0IzLNaD7IazSlI1K4oOcmJ_F0j_JpszaW4IKjXbFu07Xj9HQeDrAu9RHEOeS5b8Cc9vJ9n6rIVLJ0GJIAplnBZFOPeCEA6uCAMvoeVuPgSPXHz2hOxoApx-7gLKdchvfZa6XDcEKzZwzAiUB0ou4KzbVsCSAiDAr-RAWUZk9n8Jf5FhkVuM5h1CbcVlJzZ2EO_2qczcytkBVyapQPUNnm4OUB9eUI14hqxi0CYtFbPG5b06BOXYEGYZCxue9Dd2fnHxdYnPrQgF3TiYDCl-k-B8WpO8gonKAOCCTBs2NYTkzbMvcl8ezT1euAeujf-mO38B9vcnOPd1DG58w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIRjkQyp8oUIhKVpXBMIdUSOUsPQMFGQvgzCjVTAHtuTqWy3bnNjOVgPo482VjwfTDxya50VUjyOi3T9b_fsHE5150NphDGXGTFzx6k4ge5kw9ZtyT03o8zQvMu2fIF7SiS4Y1Y7h6cmunEeV0p-ctIPZ29Qg8OHTEydPtWdS3SuPL3N8F1Rs-O1PSpL5fC0scstd5kNlDMDjTjp62h2tHatjcdcip9PiBjDJpZ9aWgsCf0v53aO1gSlNLRVb73iBPHNJ8raBQ4UeHi665BwuNXeLTDiLaaRV64FkMMVQAarNMBvI7_8DByWSkSlPES0k08pjPJSpMnvRoE0COIykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD42CcEmsCNHdNDAKAg5xS90BdiqWFp_j-3ss-nCObljxZKEIwmYBXx-T2mE1P7ArXMjgw8RCaTmf6_MbssJSTq6f-Tmw9xoB9Xs3aX3lqLCS_yET2EBvHKUnT85PZn4C8WHyoNW4Zp6e9ndk1sOtoOfHZcWqRqjgZnPOCsnIAREVz_CO76uieJZRJnJ1ctgSVkE2eeWDCV1fPKCKaQ1sep7tZ8CQRU6o4A0P3lLrJudgoWD7J-KbXqmHAAmzUUseYa82h5QQVgZOGFKR5dpyrQcB5QCL5sNaT9cbsVvEWFIAIysIejGUF3ZLi13-r1Vc4UcRZHEfkRcYIGUiGiLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSqI29h6R7aVWRf1ZOx067WDWdtgaLHQfk4bVKTBiKza8__xfVwgith9DM-kYO2Khfw5FL8sWzJ9rQZLg4TnL2MqX7ODcQD3VYv418tLFGtz8i8Hl4GojIcR2_qZws_ZtfOkz-3qIx85r_GFK5kwgyDy9iJ3DIfCO1uYcomiS9mT_y6tU7Q4pVgrioQwb4DRVpwZtK5hp05QgGNchfZmlf0T3cSwyBTCxHFkRMecZzu3JWEtW_GuIxgPEQGFeIUrc5FCj_JatuYt4FQwuILwItM8hug1Y6am0fUss5bbb_wfVATgjX6jbE81G0RsZHsIRo_ZOm-nvcaXPJiMJQNG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8nqHt9ou0D7mhDxDomt9hZPUCyQOpanQqqtL0nAQaGySatGBABE_56-VR4RN-4kBoTM_DcSW_gZ0JHSM6BakBTBGlOam6ljFn9DiV5JTcoUBQqMx3JaeEo5u7R0tZD8l3hRfCjakD2SCKVl9hhRsWmpI1tU5XIIXuHb-b7Dcf4usu3dE_uXTgZTgJkiiL45ttx0IMCOt8tE7gv2lGp6pf7e4eTJUW0q_aynQrCXhNMnM7jUCokCYjQFVO0M8RCvAlYslYmyPBBmvV2kgayH_bVfkhXrBFPp2MjUBCrmqud7c3roFtDjcRBLAU_pdoP7rlSGBSWj-cqq0j6FrzNW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D39BehD2iFfVfGUkjBBpQjLyA29hbcBldsM_v7z6Vq3Ubru2tIX2_kl2warjnUG4CzlQOkIFWBKcSxk2nhbCRtN8sYQkeboBN7mZJxDMLrsWK5X-a1fNwY3644fgZKDvqLyI5Yc1WhoAiGrkB-fqvq1oYKbHDr3QCz7GFajWIZOGxzxwmuu88Z_IQwyFqMalcpfLycMg7VLVHKldbEBuzhTQEgqR5KzeULaggFflOUITx_fahrX9sa0hkaOo4ROAdrzlgc8gLIVI8dmtBKVpiAGXN8-5ODl4xAX2t11CWaqbJE4KCs3iSiKcCMeS8IDIWRh_lygXpHEvZRxJH72iKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-u--fE57wA3apCEvcIq9W9YqnqG2uViOPVylvKp2tYJdhHTj69YW6aRemLVtGAknwNFh2GzAsgWvfoSzxN-LsQ7nMR--W9QhxX_Bf46s1Abawkoy5lcn_fYZWn1Wa0vLC9vhDnvsdUPT3QsrDtsMK_BGaZgJW9drog_r4znVPgWsS84I7SXndJ4DC7VcPNhtjnbayJLgt9ba756rHO46mSIBEVpL8SzfKy-KgYjXnYwqZMg4nFajqEMsOkuEYg_69BtgRq_E9WEpfaBQF-YCP9LjHU55YVKwOqwfxC3GaDSbp5kymBiSaLTK0wknBkiIKR0SeDyBhfqOpXObKCzZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehj8sYkbF09qpS_1A6jEklgmlhZp5TeteKB3BTwJND06xUQg_dDfNHvC80NtSj7q98_O10LFRgMWyuYTqvzkxee2swLpmkbdARz1kIZ_l2asm3YZfR0ZWqjYx7iXpgUqw5QoUdNtGXKs7K71VZfvzP6XBnEbyk-lInNiKmn62lyfZQEQ04s9xZfD8Jdw0tTspEJLSQuNHK-rVMnONb-EeQlOk_j6BSBYlzcEPPcj0FdrGruytJ-HYknr346mExtpuZyjAJuAqpqMjEFx5xj9YKNURrguP_IyioiUbIPwv_bmm8n7kgksayB_GaXrGGSODvytVqT1Gv5gb8FoKedJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sT77yHRbf9i4VVIie6L10F3ZvepQPjlLEtNIZuXg04ex5xDq0BQCoveVVuhpQnXlmkO7i2At1yMzkTxqrhKQVSaEnuP4z94Wtsj2pVAerJ7LPbeSNuybntqTOE-x9ao-M4NhCUOGLv58IyVwUz50R2Zu0DwIbX2Y-kJo2ojHDPkLy99RJwDjcf4TdyBo9o3EeJ2AW_qTEltuFXoMM_o6sF3rZTdANBwVWSaKmQlcYwBPSgfGG31giuVhjtfBB2yjjun16RGNPjJsl3l9VpBXQSIgjQSit51Gcc9DhdEAvI4CjVs7WE_hHaoBscazlF_W179SBfYDu5Rh_1pBne60Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2Vatkx3oGcyQEgYaIuLonNUvoo71NA7h0AOYwewkOxkAeWqUjVmc2WM884HBQwPDWGoh4-uw8UK6jLr66Vty3ptHJvfY_Rjtzkfo9fj-Yy7IosFNeRCa8ItJ_NzRaw-wpLvfNxAHWSoe0mVk4KDLynQD6GjfCPVBZK7RWbyF0s--LtoSIMVphKQt2L0fClRSADoDzw23K3VNhJoJbXhFIOa_DmRj5c_8WtuRsP0fTn2w-rGzlEdiqbxZFG417N3qklUNj6sjP3CJwxnK7b_A1Hz0OXGZ76D7rKFiwTeZoezOZbnGdc72PuRDO7UJB5zI9-K6ASjRK42J_31fOiGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4BCMklfRQtKbdQnQriGI6pSX6PVZGzpSH9POXdTycYvSLAts759irUgRiGfn7YEgL9VH1_5bpCZEyvu2tFuVFxurP65EthYVrQY1f23LnF0lig5jDomixcGPdsMec9F2q9-vJU3qnnKxqykwR-W8JPNBOI0y5DeRGYiBrsyjyHdqwF5_kVTKOMbQE2P5thccGX1cDOIx2T9fTRSSZcDOI4X6NIQmIoewMB4z2GimemXPY27244RM39TEocJZhA3MZOvKpwqRUmRhzEPrDyi0KiFmSqFsbBIwPjrPRoDsVU6nPPSRA4NsHxralPbJQDEonOymSfG8coAvW3Jbt2p_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muFMXYHd8M4QR-4C-1lpUE1xFQGf860U0CDPofiICx-4aYPQ-PWpYTfaArdnQIDH0ZtQp41CWQaxlcNQ5oup_7kgdOESJG2ScOydzdwiPe9zljYQz8aoNrISr1TyfVcgrjRYB6WeTZ6DmSGZjrYn2eMs03I7igvhiG_sARHSF64sMYkKuwvohsIiVIT8M0uO0f8FWMLpNT27ztxIXCwL_ssf7n44cRLFAfKfwzzIdYNDm4kCsDHGE3J3II6IJXtt0RSH0cUlKqVO1694XrV9rTt13eudFEFfRbpKxDPM5Mxh1cPSo3aF4Q3FHsuD68eKzimFYXfxJo1dLrMv41sfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=qR-G34qgM9a6J8xm9mgE-alzs87ptSJxCrbg03EZnuaTIiLAWtyu8cPE6EfY_9nR2cNFT_b4IhiiweErrPZgxgyZZD-zq_7eU2bNePioqTYWj2-wWeCilkmqE5nkzlxu2gB564o0xO0Q-RsjPVGNvJrcwzGc5zeIRIVfBagzj4igJXQS5AIjHV_-yQUpgW0fPpdHz5rcn_sa1n3Lls12H_IEkjqzSmxzVnPDwfcg7GvL7_RQhivFBESTNoSWWeG29OwSugkNLs66rjfu-qaLU-6OtrG2b4fvwuz6bUtNbN0Tm56mtimK0Vmb7Tk1gRPf4sHGNfoY4D96U57hz0sJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=qR-G34qgM9a6J8xm9mgE-alzs87ptSJxCrbg03EZnuaTIiLAWtyu8cPE6EfY_9nR2cNFT_b4IhiiweErrPZgxgyZZD-zq_7eU2bNePioqTYWj2-wWeCilkmqE5nkzlxu2gB564o0xO0Q-RsjPVGNvJrcwzGc5zeIRIVfBagzj4igJXQS5AIjHV_-yQUpgW0fPpdHz5rcn_sa1n3Lls12H_IEkjqzSmxzVnPDwfcg7GvL7_RQhivFBESTNoSWWeG29OwSugkNLs66rjfu-qaLU-6OtrG2b4fvwuz6bUtNbN0Tm56mtimK0Vmb7Tk1gRPf4sHGNfoY4D96U57hz0sJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY8gYdhEubc-1IlLK2rCqlDej7spbOX2EsN1D6oume1zIW0TXdht6jbVVeS0wYF69pHdZbSWTkaa26mLLnnhefoxpffQ19DLr0JBqPvmezmKm8uhmcKQekAQ_yQnau1gQeWfK_LZZO-LexZY0q8wlbN6akmk41MM1EprfeAiDySDp5e1Nc37MAuMAbX7S2mHyPNzmmK8XoG127hb6vyxoSJ5cOHAHw_w-NzJBm1NWn8jfrUweXNcRkkeLGT54u40KM1dsKGKkucGRdbB3BKt0peltKAdlvM8ESGg__ywDo0e3bXETM72mqt80ycoaD06bhMfGD0FqdrSv2lium8YFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVwsSLx2Wn7OYMrcuFTDGyyRBsKGVv7oKOl4Cg9D5r_8vHOj6sHTd5qBlmijuEm10oGKBrtpjYuw3vqXiaRCyeqwYTkgS_VUv6Z5Y4Dv23VNFocnF-d7hikj9pLAao7glub9M-quYHo-6Ra5j2G0l9v0RWJI7Lf8l2INrVU-tXmrFDk-SAJB_-xOqBPZEozq33jb1gZYLn4IMuqgPQWHBKXy4CQzj5zp_cqKRjK68xi-zmzf3EjbVn0RNaF38tKJtYDARlBXduDd0iFyVsvLJoXQ3fzu_Ys36P1DvuEtAp2VIBv2V1Es6OXgf3e8v0WcHnmF9I7KH3VM-Il1_GYxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8te5OvO-OonAlkKolwgC5-5uaxDUkYp-h3I7NYNyD9M7ETgET0FbMAiW2HiYPm4UyUgb4K4HfJqKM-TIpzqcWg3KRohP5Yr0FiiodjZGlALGjI3fpl7zVfbYrytZTurRieSCaz17i_3JjwBRpmMAbej7f5pE2KMZo6vATaPFaNUap1xgJZXG_nCL0pupvLvGFgAX37FJXyMyJdLrImgXvcb3f5BIPHCkycpiVTNOZ3G66mXINtKliqz407PVoBhERSeHw_abAqPBzE9ZvoxY2wLbf9XxO1JfPV97Gvz_x-gDxBatnldyNWp5UFf9pMfXGOe1f1Bmw-Il01W_lQw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=OkyBaNhO9RVL4Xw_6CfYj6oxzrRWCxwzjdaqRbIbAXhOBKzmlFuAAfviOcYaacL0yQ05RSUTCHill37xZyhTfp_7-vQhdUuxIY4UnLRN4A9KaiTtS5puxACcg5dqDecJ4McZ8yNBFrQO-rPrGmSjq8GEwivWuwPpLuw0XX2zDlOCvs-1fWyAypSriyXSGpcCn1i_hqGezAev7BdT6DnsiS7C1g-390EJs_7dtHq1QR2p4aX8npG2smHkBomG3IO3-g4aJCnXzIPeo1qC1rFaRwTeUJqIcRezbYocAIzJsyLkFBT4ZZNyShxDhg2q5Xc3WMLWk3Yq1HLm7K1U-OjEPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=OkyBaNhO9RVL4Xw_6CfYj6oxzrRWCxwzjdaqRbIbAXhOBKzmlFuAAfviOcYaacL0yQ05RSUTCHill37xZyhTfp_7-vQhdUuxIY4UnLRN4A9KaiTtS5puxACcg5dqDecJ4McZ8yNBFrQO-rPrGmSjq8GEwivWuwPpLuw0XX2zDlOCvs-1fWyAypSriyXSGpcCn1i_hqGezAev7BdT6DnsiS7C1g-390EJs_7dtHq1QR2p4aX8npG2smHkBomG3IO3-g4aJCnXzIPeo1qC1rFaRwTeUJqIcRezbYocAIzJsyLkFBT4ZZNyShxDhg2q5Xc3WMLWk3Yq1HLm7K1U-OjEPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3XJ_UbgyJH_ZLZPhSB8hxeMWENX7lRQzNTVpvqV9qJqZi_PoM7SOlYr-n6oBlAqXWkVkUzCy7QeQYZXh_tehAxf-iA0pYWYdFjMP-5x1m3UjXB-beirBKY4tagXGlVfXvTNIauvo156RXLJTeffky_IG0e3UOz44vxXeN3rKWS5Uk_m-1hld6edr3B__YFhm9ic8xpEAcH-go4wauZilLPLluUg89htwJc0cZLSeny2CVp-c3rzesP7RkYJ6de3itsgHUwemH8ucLUFk6c0NiM9gpfEcf1_9qMf8Xi0wau3XzYubc0njutULSLEn_wzEnkEo8RNHiqOi2xW5s-QWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoagfBrGxrC9GiYaffQj8yUEac93MpHQS753nBoCBtYZYJtMsfCPFZVBoVq_ewVXOrqtz2tbM6qntvk9Z_bLlJ5hmPqhCDCkY3G6lbItYEObylDdUfzlP2Wv3NevDqFJKOwGh1dSaaHkzWYcEKFexCnBBvaPjh2V4UYsepUkBGIIIgh6sxqJhYrkK498SeN-3GXJd7ZWp5FG69I91zVSvlRqxSvICCIktmp08AOH1NiGsf6rPKEvSa42WQqruZkbtUaFm5eyobQRZBFv4I9qhZ-tp5LplBQK5A9GuaRaOovMFm40Szuf3PoFqg-Eq8ZvS_vBWvm_pL2SJSakrI0lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tH6FoNCa1rdcmwqkB9QjiZate2hmT-DPInfkJENq3M3dEHawN1khoRFMXimLEArXu_lO9JqcA3Ep54SmTVo-EB1gP8NGBZ0zAM4qjK3FLGv8m6W4TTsYjOOZwSNUahY8z0qN-GHjz0vkmvPsrDgDZEfFsNgoh9nWcV1KeFCJmeoH5-yJCcd6bahCO0CfWCEjMxbtu83dkyoM8ERPZLow1GoStFEdE8mqUbg498FD3OzDjFO-9fsM3w1T6dEN4T7xqeW2pD5H-aEs_HE9FhsQOdup4jnP40nRaPHfEcmV5ivwqPrKeboiJ6gv_j8YXiwbTW0AYjJ28vVFmUQOj08lrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=kPLbFgI4WrV4QX8qXVJq_sFedw8G-4pdcQVUqbTEpX-sJWq_bH32YdDYJPjLpF9J-6Nv-wsTPnoff4mzlGxh6K1qvzHI-dN5eGMBj81kCBGxpfQHMbZtoLZNlrV7lbNkVFQEF_VCN_7DxxYXw3qhnEqWsLCtUs7Fc02wWecN7mNzdwXQXVri7oX9OUJcCjJonibgT6czdnThQDQxN1Tlg-dZ3WIkcZ6RkmdjkGcztdQ0IxHGxORg-kvJS_pwOAxUO9BRiodOzogs807whvMSzcl50cwx_uKnnhQQPuZhpKNp5by3_Slov4z3OlBWlHj5HXN6Jy3gFiZfQ3Qo1L0qWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=kPLbFgI4WrV4QX8qXVJq_sFedw8G-4pdcQVUqbTEpX-sJWq_bH32YdDYJPjLpF9J-6Nv-wsTPnoff4mzlGxh6K1qvzHI-dN5eGMBj81kCBGxpfQHMbZtoLZNlrV7lbNkVFQEF_VCN_7DxxYXw3qhnEqWsLCtUs7Fc02wWecN7mNzdwXQXVri7oX9OUJcCjJonibgT6czdnThQDQxN1Tlg-dZ3WIkcZ6RkmdjkGcztdQ0IxHGxORg-kvJS_pwOAxUO9BRiodOzogs807whvMSzcl50cwx_uKnnhQQPuZhpKNp5by3_Slov4z3OlBWlHj5HXN6Jy3gFiZfQ3Qo1L0qWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stn7DzVv-uKTZawswDSIWe_11QALVh_8OmfVAN2Dsoadm_yi38CY1cDZ9vf68aPT--POXJSfOmUtfe-D1BdV9c0tJhD-WfV0FttpJPnkpv9Cu9mEZksgLTP1Fbo_Fdy2684dMlH9A-wXepooDvYdR_A6pCEcY5u4yKkSz9SPv79b_iVo5Z4QBHuYVFrh8NJoI-K47XPUaj_tK6HWrEGDkXU4C_9nzVybytbapqDttndbHn6zlX0hL_FxyfEYFLQe5_aVqGOptRNea_wGtScrEUDcpdSv1XuL53VhQfnOunLapyjFDdUAUeOpZkiz7fvxanorO3WgrCGJdTLTaewSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4h7USeo-sVAw4OuahRaiUmtgSunMmySf8ifxfz4yHF6izqHPskrbaYVQOJt2Q5SKJkshASQW3ne3AahLKcfGQxes3eCQ1Ynqn0RLQUKPLccdmO0nFRxQq77YuT4cIbOyeO-XeoXpvgkcSFA0MNb0h7d3m_BjHd4WewXZ9IkPTF7SYtnVZ1D9aKn7buDb0ilJ5hsC3SgSx9rARgFAfKdussLqcF_wlvzE925vWWBRy1RsCLDn1tqw7GfNB9L-VHmtJIFSXlZ8Qxm_BCtDzSiESMU9kpbyjZLnNrQh3piaRQEUUPFXJqxasFnW2_LeJfH_5dj6c517jKMqy1BBBZpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
