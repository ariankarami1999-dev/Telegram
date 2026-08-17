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
<img src="https://cdn4.telesco.pe/file/DglKu2MKBPRGxrPo1lOlfAsttA1y2jDYXKZOTmWm1AyQMc6b-GU9AnS_IFJXz0jPoEJEA_xJp07d9YueqW_Fw-KuIKMeg3AGgd8xjSNAfR8imPqCYmQzVvrK9Ta2WrfcjWF-KdBDBQAllJbre9ibXT8iI7kjHSoCFdH79MNeygau35F3qWtddf3aJUfSVh-o1l4KsnRmtPEAkioBP9VMJEpCFUwG7yVQcKIvO5_w7eTykrVBlBRRZsvAJBstjg7RLOpyl4GBJE8M17Cr6tH4sXfPXo11USI_RVrZ8j9ZCl7FNoPH3VaQmbTaW401V272latSiU-OxC3tagkasKvMHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 13:01:27</div>
<hr>

<div class="tg-post" id="msg-681932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnK3nmba4pgJQM5IoCiZj075u4u1_NnrpOqSnW-6Xd5pKM3K9KR80yEwqLGRkqaMZ1JeS9JMQ4pLEwe5tsyzeIc7MW6TQ8PFGHjoQHj3VscvIMSzIr2ByfduxKmtW3pxfAjEvsAdq6mbf4LLFdNYtp2-o0zh77L5xKt1cBYzRrouztQmx1SV-7CtksrisGTWX5dFdg8zjl-YAQbnTkdwSHGjdAuApnsXc_AcxtSno2k2leeqbpGZMUzbLzV4zlIi3ViIZUN747HE2_j5ou5-QP9RENL6j6T06IOsFFRbkz11HirPRTVTi8j1_kYQP13bvDtZTlHUsp7DnTxr0AJ60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: امروز خانواده آمریکایی، هزینه قمار سردمدارانش را نقداً می‌دهد
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/681932" target="_blank">📅 13:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch8y43Nge8g36iVmrpOKCukFyLDAvnT2a3KaKZgJdeLjsx0StXQBobdTdD5iCHoOX0p5f8-64LhGf_m9hD1mbyLEllAV7i8S7_vg8g_S5P3_-ptJwnGYccKvpJysTanuxQk2LzGmg1dvBr5cC-0um_N8jKjebezPiRFs250mBV_24ecxxJorFnzCc72HDaVYMhlYGwTjgv7dU9mtDDyEIjfJl8vKiY-BAoIjaJ6x7fASEfqkhyL8rluev8P7rbWGh2-5tTPQ5S2Ew484zlPzh-BqFkhuI7exSlvPF37BE_xxZNaX3NtYo6pjmHSgLKnqf3z3iJheN7_slxAWFNJmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۶ مرداد ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
دلار امروز بدون تغییر روی ۱۸۶ هزار تومان ماند و پایان آتش‌بس ۶۰ روزه ایران و آمریکا هم واکنشی در بازار ایجاد نکرد.
🔹
تحلیلگران این بی‌تفاوتی را نتیجه آن می‌دانند که در دوران آتش‌بس نیز درگیری‌ها کاملاً متوقف نشده بود و عملاً آتش‌بس واقعی برقرار نبود؛ به همین دلیل پایان آن هم نتوانست نگاه معامله‌گران را تغییر دهد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/akhbarefori/681931" target="_blank">📅 12:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af73a7afe.mp4?token=LqEMezyrOvC3RhaFW2NUxRt9Qj5B73MhYEbMpr7wO1lBLt-r4cjv7HKhkC77CfDBf1I8V9hbEnHBICYGCS_oTvqKeE2XpRDUrgyl4oWd1dvTnB5yU2aptGf0YYAv1V2C2Mgs0UwfrwiitDt5kILP_GwCMwIc3FJAujk_tllmVyXENchZXbg86p3JkgJn6pjQgnKdxRNtfE5AEYZx1GWRw-GVskc4JPsCcS-52b9xcXX9XMIfWBqTDjGisjr4NX5JhwnhaXiLKQtHQJWZjks7QNh3zmRY4GyE89K8obDWMU2YFI6k8aVfa4pN663uMnHTiqjPhu1up64aipc4zRZsvAMjmhpGOopMpHl5_-TretbEKEWMSgVCtyY0n4twvB_HwBlK8UWSAaSy0joC60IqCGOz3kCruWCAcFuDmBZpbREuj4RiveKD8Bmp-pQCkFZQxz6G8sWehMr22OqWh-AmgKq3ovqs3aQQUHlSApplmUWK02MJQdhr_IMkIpbIcOCLIOYd71GAcIemTwxrhEXUbM0AHnhTOw5ukMOXPPEEe3zIg_3tY8PlgrEGpH_rjvemanH-V5DVaQrl0V6988yw23oi6jdfmqzquR4u9seoEkB6MPNQFbjns9yB9rAK6ZjYkxRObdxJ0T4OMon3pH7P3PMprIRQN9Gnjub4pNGc0KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستور پخت کنسرو خانگی آمیش‌ها؛ روشی از سال ۱۹۳۴ برای روزهای سخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/akhbarefori/681930" target="_blank">📅 12:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPvKLtTAWSn-edE4E6o4InOlcsPjpDu7V1c9H0qH7Sxo5PpXAthKJeXCf98BV-RwjEMpvVzSGzR5rb8KyMp1pcRiEcuCzIK10rSQ4vfM8NOv3xadAmloK5hLz0bSxcpGoJzSOjOrwm6cA513RuwnrK1qZHxHkmIMN6NPcOhgYzaKQY6G-pdKMKuFEBmbyyD58BGslKtn2Cnou2lEFgQ3vYuv2amZRQLBU1A0l2r2_cErVA1uygN15UTl1vY6YfNYES_QpCLllypuB3pmR2_2z0UgI7Im5jOMf1TCB1TIcMgHfScOsFg1p009MfQdZOmjf_ovh7YBAQNuvJPpQf4ZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد جدید بورس در مرز ۵ میلیون و ۹۰۰ هزار واحد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۲ هزار واحدی به ۵ میلیون و ۸۹۸ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/akhbarefori/681929" target="_blank">📅 12:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeNjQv60XlKuEcEGIFwShpSe2WdiwsK1aFyORnNMTNFAXxxiAqhBGX2zqD5juEDznXf-eNN8Lu7fvGVy0-ADv6RXEFb5Jfv803zs5ssCoiarfPNKET8rdRLE1xnx4X-ykwsshpWY1b9bI4Meij1mRHM2sbGbLqBfjU5Pu3POOXKLfJcYItv4NqatK_zgvwBa29On28aU88WtjE7ZideNekyTdLuXsZ5zClu1ZE4ipPz08ohhHkM8vp02_wfv8by4BvbUQQF3K-11WxWa9SNLzFzXfkBAPFhf8Zux4PXhsvaAtU1ZNYHpCsrcw1OK3rv5OKfLulTAb7oopImmRnwEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراحل ثبت شکایت در خطاهای پزشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/681928" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d313518a9.mp4?token=Yu3ig4MbO8YhrZ9rvdII6hm4If64LOhAPA_hLsaMOg8lJcXNhMISSJjXJzp56oaLN1_jW4Uhm5bZ_362BG_mkzCbEp2Zb_E3pN6A_T4io4J1rTVr1V3WQYorMrHZUhLYPKKg7JSGmXOfEEwbUIj2Aroe9cZeiEZXvEu_3v9vwmPT3GwWPQ9s5liXYPyXInuo-WyP8s-lXg_IUoSecCxWXqweSXqDriVHLkh6ssAwDZ49TRdkOPVDoZAfJM1RRe0w6fj5rShHT7N5vZesdRwq1vko-15omzxVd-w5Qp3ppP1ZMdtvQnB3GrVc3iOkgFSjZ9M3WEViVH3D_0ncMyVHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهین به ترامپ جنایتکار؛ مستقیم از فاکس‌نیوز
🔹
نماینده دموکرات ایالت ماساچوست و نظامی سابق تفنگداران دریایی آمریکا، در گفتگویی با فاکس‌نیوز حمله‌ای تند به ترامپ به دلیل عملکرد دولت او در جنگ با ایران داشت.
🔹
ترامپ فاکس را تماشا می‌کند، بنابراین اینجا مستقیماً به او می‌گویم: آقای ترامپ، تو تنها رئیس‌جمهور تاریخ آمریکا هستی که یک جنگ را خودت آغاز کردی و خودت هم باختی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/681927" target="_blank">📅 12:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/akhbarefori/681926" target="_blank">📅 12:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6209fb52.mp4?token=MWA8YHy6LA2XQLroTjEzXaKOrXbzU0uausO0D2faLXhBl44IB34Loi6rlWilDamaniRjwuvRNIgXimdCuGWsTwOKKH8G-6ayGtpSTB8Rgw--fnIydSLrVlo6C9h30orB2IbETPg-JJkHDpK4rerH-5cz9Gbs29Clk6h8NeaGKg9Az_w4Sp1rzrHBnWscJavAZy2aZ_hPo1PPBTMXyJI7f6QIQV5Q0cWeT0TUMlKM8FjavsKh1QoBD2FSLG94AVamyY3u_OKl1XDPy8RN-GklY76pnQtd-ol0X6jkLVl5H_-RT-HwdEM9jlIL-imsri39OWILvV8ISA9TbT5Gne66PFS8aXc765SJ8rii6zG8QzgiNDE3mSvP4JM9Om0tApzwAtjQjIwSOpNmr9ME4_MKrekopE17z2z6U567coQj9rQ4jdx1dUCyYwse3oOhF2sLNL1XVHjYxaZ23JSQDKohkFsYU9Cj2QxvaxSQdJ6E_okW-PpAaGOI_9ZXicGbjR5mUedIhhaMfO96PVWQPvOuxGzuRQmru0PyJr007xMzdEbNVeRjfDZ9Dc4_v4Nnf-2LRVwZsljWsI2RVlYb4WAdAt-BOOR5rRWFiqQGR1_99C2h5S5lWhjB7uAAOQyw2eX3XBscbwq7i_bfDoCNWkV4dep-R0TD2TxgegU2QbYjPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی MSI؛ گران‌ترین کارت گرافیک RTX ۵۰۹۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/681925" target="_blank">📅 12:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7885178bb9.mp4?token=T4KozM7gTj4lJv6d8sHz6MmCso45dU4rmDeILVwe3eZTqyYfTl1YoMe5XToaaiFej7qfz6dpgQJvsCub3y8x0uaycQ3-kE3L8JM35ZmwhcXLP-ZslT3iFKmS0GPoXkul_1dyvktZlCU78LtW33F0FBftnbb3KgCClfZwoasuUnEMqMgd5IY-4vnMxTeSL2WUda2XbmdOJiUwDD55D7oQm1EXLGSWgb4qC_VNNq_VpZg0G8Akr_HZIJZzNllOhrZHOwLwruqsljPM6jIIlAHGuExTEEeX0tpk1GyDBtH7awWRBzq70-qpvmwwQLKjmAXgTMUApivQyYmdcYQ0F_iYWYoiwyF08lACPEBiKFE1OHr7rwTT-YKPkqmwEBGIUckkI-ipD4VBZmC4jjSNtUtU2V5HtAjpy4mSh9yB7mWH8iwkoisJGPN1_RskGX9cijfS4IIlBvaE3nHX9xWsuf8z4scEtH9MXGOGpgGz_96avxN-XWgMVXWmZ53zUvtszvjmj1h3ymglSJMbGlh1OdSMzaUc9YTrD3mrsiOy__10TOkTLlr_gHUxrwkjDIhoNr42E8NwcMQSu4mXllvcc8c0IisSyUP_pdh0vF8S-tg2x8EVpcxLSpP5vMDZp38W3TiiaseUzrcxt_BFxawNdLAKv5j7r6UsdCwcpUUNUU2S2bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7885178bb9.mp4?token=T4KozM7gTj4lJv6d8sHz6MmCso45dU4rmDeILVwe3eZTqyYfTl1YoMe5XToaaiFej7qfz6dpgQJvsCub3y8x0uaycQ3-kE3L8JM35ZmwhcXLP-ZslT3iFKmS0GPoXkul_1dyvktZlCU78LtW33F0FBftnbb3KgCClfZwoasuUnEMqMgd5IY-4vnMxTeSL2WUda2XbmdOJiUwDD55D7oQm1EXLGSWgb4qC_VNNq_VpZg0G8Akr_HZIJZzNllOhrZHOwLwruqsljPM6jIIlAHGuExTEEeX0tpk1GyDBtH7awWRBzq70-qpvmwwQLKjmAXgTMUApivQyYmdcYQ0F_iYWYoiwyF08lACPEBiKFE1OHr7rwTT-YKPkqmwEBGIUckkI-ipD4VBZmC4jjSNtUtU2V5HtAjpy4mSh9yB7mWH8iwkoisJGPN1_RskGX9cijfS4IIlBvaE3nHX9xWsuf8z4scEtH9MXGOGpgGz_96avxN-XWgMVXWmZ53zUvtszvjmj1h3ymglSJMbGlh1OdSMzaUc9YTrD3mrsiOy__10TOkTLlr_gHUxrwkjDIhoNr42E8NwcMQSu4mXllvcc8c0IisSyUP_pdh0vF8S-tg2x8EVpcxLSpP5vMDZp38W3TiiaseUzrcxt_BFxawNdLAKv5j7r6UsdCwcpUUNUU2S2bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: خسارت هایی که به محیط زیست و دریای عمان وارد شده مربوط به دوره اخیر نبوده است بلکه به دلیل حضور نظامی ۵ دهه گذشته بوده است
🔹
بقائی: آسیب زیست محیطی فقط متوجه به ایران نیست بلکه همه کشورهای همسایه جنوبی ما را درگیر خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/681924" target="_blank">📅 12:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نمونه‌ای از غذای در حال سرو در آبراهام لینکلن
🔹
یک ملوان حاضر در ناو جنگی آبراهام لینکلن، تصویری از غذاهای سرو شده در این ناو را برای یکی از اعضای خانواده‌اش ارسال کرد و گفت که این غذا شامل مقدار کمی از همه چیز موجود بود، نه غذاهایی که به طور شخصی انتخاب…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/681923" target="_blank">📅 12:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa81ae3723.mp4?token=mHyjpxq2t0bh7MXjdR0gxUBv41Foy3mpglcRhScPedzNs40we4-AT-l_VGRcpju0m13P_cs5mw4QjructrbFft4kJEyvq8i2ouXD7vK6bT9Ro1LBDxFosvDmDsuDE0RIjC7RjharrnREUNQJaJnx_CzctzSoy_m3EGvOy-jSbpsP0bVx9iRf5_3xyPph4T6KTH2MCPmUd8jgw-Ro9JbyIyyIGi6jdqwBuTG-N1_UF3sCo-CtGwZvlSe0OOth9-sc8YpHiTLLsVfHAPBalebcq5r5P8WvElFrbT-s9wvlPOquFY7IS62gfWDqgAWAva-g_p2IzzAjcIjQ9f6zQgTdqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa81ae3723.mp4?token=mHyjpxq2t0bh7MXjdR0gxUBv41Foy3mpglcRhScPedzNs40we4-AT-l_VGRcpju0m13P_cs5mw4QjructrbFft4kJEyvq8i2ouXD7vK6bT9Ro1LBDxFosvDmDsuDE0RIjC7RjharrnREUNQJaJnx_CzctzSoy_m3EGvOy-jSbpsP0bVx9iRf5_3xyPph4T6KTH2MCPmUd8jgw-Ro9JbyIyyIGi6jdqwBuTG-N1_UF3sCo-CtGwZvlSe0OOth9-sc8YpHiTLLsVfHAPBalebcq5r5P8WvElFrbT-s9wvlPOquFY7IS62gfWDqgAWAva-g_p2IzzAjcIjQ9f6zQgTdqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیمه گمشده واقعا وجود داره؟  #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/681922" target="_blank">📅 12:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dm3sAKeXz7lYEUpouhRTSP9yHXgLcdrnAyEYhj4bZ-FiA6wI_9ApoFAPvr3bBLTgbynuQDlpwUtcMN5LoxgBa0Wux1rfNKfXlCNvDX8YnK_m1JfiRz9sjQVx5Ut93E8CW7bALjkCoVjieu29CYS1l7uS-N8RsSvNWH-VQCfr-a7SgSsDz5g4kDLqBKalxcbfowwv68p9NaS_CfeA_GyXvASouZgzN6lBA-Kfx2TpvjSRYHx6s__H82abbIa3F4YjyAM0AOVrGbPsbvQx4GcazShp7pVVqi2THeB6fcsJwY6iGC2JPGDrAaxgw3z-dOZWhx5E3X2fzrixh77N3pGmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
کلینیک ایران نوین قدیمی‌ترین و بزرگ‌ترین مرکز کاشت مو
کاشت مو (Nanograft) با ۵۰٪ تخفیف جشنواره تابستان
💰
قیمت نهایی: از ۳۷.۵ تا ۴۷.۵ میلیون تومان (متناسب با وسط طاسی)
شرایط پرداخت:
۱۲.۵ میلیون پیش‌پرداخت + ۵ قسط ۵ میلیونی (اقساط بدون سود)
⚠️
ظرفیت این جشنواره بسیار محدود است!
اینجا کلیک کن
👇
@clinic_irannovin</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/681921" target="_blank">📅 12:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867a2e48ac.mp4?token=CM7tEggiU09FAQdAOamejqFUlhshJGfbkAZWrChrgLZyvudu0m2sju5vJRo-hbB-MyBXVW6kBkaJNhf_iZRRO-WSrVZ1jqKKrYIn4QZUgZopebeI_UCyDvadbr6ETs1Lw4DLsHLMiZ9fPBGemXFdC0qGH19FxwXHw_hcu7OCmQ9iSzf9YAXy1NWjMcqpc6IItqAlJAhhslYS82nWeoGU9q7vgzgWMzvYFvBlLxDyTxKIaR4yFVPJ2g7JT5J91z6DI9zUyzwdVGa0dQNKnpnoBWQAKfjsdDG7jY9NwSrtZC_m0_txdNU4zifyrSH1BsJXFIc9advXB8W48UeayMU-Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867a2e48ac.mp4?token=CM7tEggiU09FAQdAOamejqFUlhshJGfbkAZWrChrgLZyvudu0m2sju5vJRo-hbB-MyBXVW6kBkaJNhf_iZRRO-WSrVZ1jqKKrYIn4QZUgZopebeI_UCyDvadbr6ETs1Lw4DLsHLMiZ9fPBGemXFdC0qGH19FxwXHw_hcu7OCmQ9iSzf9YAXy1NWjMcqpc6IItqAlJAhhslYS82nWeoGU9q7vgzgWMzvYFvBlLxDyTxKIaR4yFVPJ2g7JT5J91z6DI9zUyzwdVGa0dQNKnpnoBWQAKfjsdDG7jY9NwSrtZC_m0_txdNU4zifyrSH1BsJXFIc9advXB8W48UeayMU-Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شگفت‌انگیز پرواز کفشدوزک؛ تصویری جذاب از دنیای حشرات
🐞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/681920" target="_blank">📅 11:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdcloPhs4OEN5OuQMXkqxV94pK3Z_QrOkvS9H040qfb12X83vcETs5In2GzCgmApGiO2t46_JJBdbaTPIvR4srSuKgKHn1ySMffl_aposZ0iEFklsIPeL0YfIuFPuZJompf8VlYcCRpsMKA6qm1xj2f3zGLB2mSX2gDb5hVfQT3tn94qCIz_xc_qZv_yZl1ZC7cbc8m5uOTm_yRBHhz7TMxrBy4q4spIcIMj28Jm10fRJid_zGKNxxE4LjNs7xbOsfI4DQ5WMJSnc_-JpBxiusgBZK9LcVtcDUsDOKfZeWEXRRoJXyQiDlWWRtXe5K-fN_KBaugwLFJK9v7JLmLjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: توقف مذاکرات با ایران، تردد در هرمز را به‌شدت کاهش داد و ریسک نفت را بالا برد
🔹
رویترز گزارش داد با متوقف ماندن مذاکرات ایران و آمریکا، عبور کشتی‌های تجاری از تنگه هرمز به‌شدت افت کرده؛ به‌طوری‌ که طبق داده‌های کپلر، شنبه فقط ۵ کشتی کالایی عبور کرده و یکشنبه هیچ عبوری ثبت نشده است.
🔹
این رسانه افزود تهران بازگشت عادی کشتیرانی را به تحقق شروط خود از سوی واشنگتن گره زده و همین مسئله دوباره «ریسک ژئوپلیتیکی» را به بازار نفت برگردانده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/681919" target="_blank">📅 11:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c373cc23.mp4?token=tfSN-NzzVUG3T4W_nXd4KOUU1aMGMPJi3mPAFhXUXdEf-0vh25O3TlIIHoSPCu3MdoXGJOkGQ5VhYzTou9xW80FlVTHN49pW-eX_FvDCG1KR6uM7VUBBKhQ6obH_VM1H9Hi92zanvvBRMxNiHMAefXZKuzJ193KaYxX0ElnPKoayn37xLfzgz1BmwnDDhPPkScCnEa2EuLD8yGyaXs01TgerZF-zjt8j1STHSGSuE7oTw2HiCBK3YNM38MyxJmOK0QB6yJNEQDm8qjrkDrr7vQ4ZT185FhsbzmiQMGr_U52K-NLUw3LsfOMPdmIEYOZNncSd5qBCbpD53a5jbitz1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c373cc23.mp4?token=tfSN-NzzVUG3T4W_nXd4KOUU1aMGMPJi3mPAFhXUXdEf-0vh25O3TlIIHoSPCu3MdoXGJOkGQ5VhYzTou9xW80FlVTHN49pW-eX_FvDCG1KR6uM7VUBBKhQ6obH_VM1H9Hi92zanvvBRMxNiHMAefXZKuzJ193KaYxX0ElnPKoayn37xLfzgz1BmwnDDhPPkScCnEa2EuLD8yGyaXs01TgerZF-zjt8j1STHSGSuE7oTw2HiCBK3YNM38MyxJmOK0QB6yJNEQDm8qjrkDrr7vQ4ZT185FhsbzmiQMGr_U52K-NLUw3LsfOMPdmIEYOZNncSd5qBCbpD53a5jbitz1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هزاران مهاجر مراکشی تنها دو هفته پس از هجوم گسترده قبلی، دوباره تلاش می‌کنند وارد منطقه سئوتا اسپانیا شوند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681916" target="_blank">📅 11:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
واکنش ایران به تهدید آمریکا برای تحریم‌های جدید   بقایی:
🔹
از مدتها قبل ارزیابی‌هایی داشتیم پیش‌بینی‌های لازم در خصوص اقدامات آمریکا انجام شده و ایران از تمام ظرفیت‌های خود برای ناکام گذاشتن شرارت‌های جدید استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681915" target="_blank">📅 11:38 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681914">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmi3eAmRAbhqsanypqnj8sowvqQSUt3MY7Ze13Kx34dtYVJjwGsSasKQjbJriKjx31DoGHqHtOyRncw7cTgky-yH3hcb1Ovs_9jjFFsXFUWzwDq7Mc-aGaMVMAzVnhj6-plGRaR1cVkES8iY0DRJetMleajNt-nRQxcE42vtVxZn6Ar46v5g95errN57jcAWYptdAnBAyVjz6coSvr-7v8ZNqygxZUlQkpt8GzZIhILlO9nKcv12XHcBspnL5f79D7w164hnpC34vhCoodUJsrFVFt4Y8lz53Ho0w2kSeyTpmYix_os5qAYQOY4gwwe901xiAAig5RLL-izDRUPZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔹
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681914" target="_blank">📅 11:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
حمله پهپادی به دفتر نخست وزیر اقلیم کردستان عراق
🔹
خبرگزاری رسمی عراق به نقل از نهاد مبارزه با تروریسم کردستان اعلام کرد دو پهپاد دفتر نخست‌وزیر حکومت اقلیم و محل اقامت مدیر اداره امنیت را هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681913" target="_blank">📅 11:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33947fa495.mp4?token=UUW5s3uqoe7BI4s23hLIFvBhRE-wl0hndfTrD0Jqvc1rURxrUWibl_1trHmkS7mqpmUzh_utzbkx8jFRlfZ7qpYVT4mKFYQ4bjN_VL1_Cg8vKyTzfk6wQqzReLgrJe-HUflN5LCVTTYY0aukZuO56h-2pmcZzd50KvFiljV34Z5-OAkUvGsvPRFCHQSHnYywnaBFbV2qWBu0FB7UiH7rYMlST8FBbGL4hXYRUVGklaNKRU5kqLHtttbPBogKIndAkBnPhHgXZs4Cx4sPpQeFVZb-TyUaV6RqF0kbQZ0Nn9t9CJDmB2NUTd5tPkuoIZmTvBTtr4cI-0ofryb0vx5G_nkrihVuRKCNZ-CiieRIoPAMv6XrihBNzgFnWR3V8ThoVltzUjXnNV1C1HKblsIPyE2XRkBolHHr488thdjFnba065eBPl1s4DuQleWkE03l7e_cKkD_L_Z7HGlemcfsOhY08SuhCSKi1FherhPmXdMWBqjCGb7kaGhJWoIG6xtef9RaRtG9sn5lUA6uVWKfzCphQ8v9Pe19Op4YAkR-5P_69wExICEi63-OloEGeTAKV6S_uVbVa-eO8KHRq0kuPQWb9ntt7oRF0jLl68xTXGM7DzqJQrm0Wl4lCsPcwhHufXDhkj4yqOoisz2rRl6KX0OArcnNFhmIsOqVAI2HkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33947fa495.mp4?token=UUW5s3uqoe7BI4s23hLIFvBhRE-wl0hndfTrD0Jqvc1rURxrUWibl_1trHmkS7mqpmUzh_utzbkx8jFRlfZ7qpYVT4mKFYQ4bjN_VL1_Cg8vKyTzfk6wQqzReLgrJe-HUflN5LCVTTYY0aukZuO56h-2pmcZzd50KvFiljV34Z5-OAkUvGsvPRFCHQSHnYywnaBFbV2qWBu0FB7UiH7rYMlST8FBbGL4hXYRUVGklaNKRU5kqLHtttbPBogKIndAkBnPhHgXZs4Cx4sPpQeFVZb-TyUaV6RqF0kbQZ0Nn9t9CJDmB2NUTd5tPkuoIZmTvBTtr4cI-0ofryb0vx5G_nkrihVuRKCNZ-CiieRIoPAMv6XrihBNzgFnWR3V8ThoVltzUjXnNV1C1HKblsIPyE2XRkBolHHr488thdjFnba065eBPl1s4DuQleWkE03l7e_cKkD_L_Z7HGlemcfsOhY08SuhCSKi1FherhPmXdMWBqjCGb7kaGhJWoIG6xtef9RaRtG9sn5lUA6uVWKfzCphQ8v9Pe19Op4YAkR-5P_69wExICEi63-OloEGeTAKV6S_uVbVa-eO8KHRq0kuPQWb9ntt7oRF0jLl68xTXGM7DzqJQrm0Wl4lCsPcwhHufXDhkj4yqOoisz2rRl6KX0OArcnNFhmIsOqVAI2HkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ناوشکن موشک‌انداز آمریکا منطقه را ترک کرد
🔹
ناوشکن موشک‌انداز یو‌اس‌اس مک‌فال دریای عرب را به مقصد پایگاه دریایی نورفولک ترک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681912" target="_blank">📅 11:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSm2uZanxW2Tg81W7UuJX7fReHcLR2ukPnw2NnD_zr6w_QlNNkulOc1hbrVAOBBM0qK6UpfyMOtemoeSUIJoujzDbB2DzNenRoOyKYodGNRbj6w-Ik1OnhIckcSdKXgz1GMDAn25MEh0UsUSxLmIzxmBqcvRW5tgbz6pelocUa8HKcPlQs45BgjC4lAyc_JxsAPQ3CZoN3YLYykZtNOdvLH9N99b7p9jlkf_kL1T4M20YwER_k5ExXQpkkTCzQnRltu3j5G0zngwXcF1IpbN15Nk2_lAAEUIQrvkznK3X6xbbi2dTK3EIAmcnP1EboSx35QxgR4O-6V_Ry5r2UhwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارسیان ورق را برگرداند/ اعداد ۱۴۰۵ چه می‌گویند؟
🔹
آخرین صورت‌های مالی بانک پارسیان نشان می‌دهد در شرایطی که درآمد تسهیلات ۸۸ درصد، درآمد عملیاتی ۸۳ درصد و سود خالص بیش از ۳۷ برابر شده و همزمان سود ناخالص بانک نیز از زیان به سود رسیده و منابع سپرده‌ای، سود انباشته و حقوق مالکانه نیز افزایش یافته‌اند، یعنی شاهد تداوم تغییر مسیر در درآمدزایی و سودآوری بانک پارسیان در سال ۱۴۰۵ هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681911" target="_blank">📅 11:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044d99e17.mp4?token=DZezobq7BPCuFju1Qhowk7R7OeA3tkJYmJA5GqfOKfZdlyxJ-Fb8W3DYro0gk2MeqHsQLY1FBq9YkP9swNNwWy-Hr15aaot4_P9EDs92HlVDgHaZ7HKASrBoJbh-Jenr_UT_903QlOcL8KYndFT6VAju5wvgX1pcSBDo8CZpis-ZVTy4lBkVNrUC6FdOQsB3YnW2r8wn-27RfPf3rx5wyBmLan5ovl6kxqiGDOvIvfuVPURfinzRnHFcfSh5wpyMMIjwxpJhO-Zz2Zft_-lqeSC0TaVnGa_78FNPVPPMFnON4J0OtQq7TqCXfqMU041G-houyjd7blR-As81QiyoSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044d99e17.mp4?token=DZezobq7BPCuFju1Qhowk7R7OeA3tkJYmJA5GqfOKfZdlyxJ-Fb8W3DYro0gk2MeqHsQLY1FBq9YkP9swNNwWy-Hr15aaot4_P9EDs92HlVDgHaZ7HKASrBoJbh-Jenr_UT_903QlOcL8KYndFT6VAju5wvgX1pcSBDo8CZpis-ZVTy4lBkVNrUC6FdOQsB3YnW2r8wn-27RfPf3rx5wyBmLan5ovl6kxqiGDOvIvfuVPURfinzRnHFcfSh5wpyMMIjwxpJhO-Zz2Zft_-lqeSC0TaVnGa_78FNPVPPMFnON4J0OtQq7TqCXfqMU041G-houyjd7blR-As81QiyoSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/681910" target="_blank">📅 11:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681909">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دیوان محاسبات: قصور در تکمیل و تحویل حداقل ۸۰ هزار واحد مسکن مهر در حال رسیدگی است
🔹
سپاه اصفهان: احتمال شنیدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز
🔹
۳ هزار میلیارد تومان خسارت به فرودگاه ایرانشهر در پی حمله دشمن وارد شد.
🔹
حماس: رژیم اشغالگر باید به تمامی تعهداتش در آتش‌بس عمل کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/681909" target="_blank">📅 11:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
منابع سعودی مدعی حمله موشکی به باب‌المندب شدند
🔹
برخی منابع خبری از حمله موشکی ارتش یمن به یک کشتی در باب‌المندب خبر می‌دهند. هنوز ارتش یمن در این زمینه واکنشی نشان نداده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/681908" target="_blank">📅 11:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168b84c809.mp4?token=Q2YRmiinE2KH9V4qTejvSH5zUQQ_SxX6MJqwl0tDiVcqmjDIWAh9RMfqbuiDMODwpNjHNGRvhwcHyEtWlcanFKlVtFMcc-TsI92tJ8culz4nwmqMQO6tKejHTRBO3rO-Fgr7aIEwwYAqtx-3wvEbd0P-ADAsWEdyXaYKSb8xY6Fnm3ZOxlmtFwASLW3I4Sz2b4vQArNoRREtDSmeoS20ZXa6GxyW5OYgUtvwIp32HYkyP1ZlE7Kfd5XttvrPtn-HnuycYG0vqZDKrrqGJ4v7gd2OQLtW36fy-tMJ1jDZnUYVvTgwZ6c-Kuz5-yoZW8Vp7eY7NjkBK6gnRDUD04xf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168b84c809.mp4?token=Q2YRmiinE2KH9V4qTejvSH5zUQQ_SxX6MJqwl0tDiVcqmjDIWAh9RMfqbuiDMODwpNjHNGRvhwcHyEtWlcanFKlVtFMcc-TsI92tJ8culz4nwmqMQO6tKejHTRBO3rO-Fgr7aIEwwYAqtx-3wvEbd0P-ADAsWEdyXaYKSb8xY6Fnm3ZOxlmtFwASLW3I4Sz2b4vQArNoRREtDSmeoS20ZXa6GxyW5OYgUtvwIp32HYkyP1ZlE7Kfd5XttvrPtn-HnuycYG0vqZDKrrqGJ4v7gd2OQLtW36fy-tMJ1jDZnUYVvTgwZ6c-Kuz5-yoZW8Vp7eY7NjkBK6gnRDUD04xf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش ایران به تهدید آمریکا برای تحریم‌های جدید
بقایی:
🔹
از مدتها قبل ارزیابی‌هایی داشتیم پیش‌بینی‌های لازم در خصوص اقدامات آمریکا انجام شده و ایران از تمام ظرفیت‌های خود برای ناکام گذاشتن شرارت‌های جدید استفاده خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/681907" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
پیش‌پرداخت ۳۰۰ میلیونی حج آینده
رئیس حج و زیارت:
🔹
تا نرخ ارز مشخص نشود، رقم نهایی هزینۀ حج آینده قابل اعلام نیست. این درحالی است که بسیاری از زائران منتظر قیمت نهایی هستند که بدانند می‌توانند حاجی شوند یا نه.
🔹
متوسط هزینۀ حج گذشته حدود ۴۰۰ میلیون بود اما گفته می‌شود علی‌الحساب حج ۱۴۰۶ به حدود ۳۰۰ میلیون رسیده و زائران باید از ماه آینده پرداخت کنند. براساس برآورد کارشناسان هزینۀ نهایی حدود ۶۰۰ میلیون است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/681906" target="_blank">📅 11:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5ca0ffc7.mp4?token=jGlNiH3SMxgDQHg2Gml47rRxk-C4JSeOiD6K9AYjNHkxhJMHKc_fkotAVJoma81-UxMUYcA7zMY21Beb2PIEJXQVjjxismWBjfAVg5Cj3h_RkmUMpCOfAME2yovQwoN4ItA1Z6DSobOPl_4HGgTF8z3peS7-OWK3v2fHldaLJ504uzltaQ-hTv2kCNJPBE5bZ0W-0QcusJlXO88lEVSpZoKCXSUt_DNMG0UfJLNNsBgur_5ku7--Pyy4JiJ8Da0ibdPF5IyqaM6yx6mXrdxO_4cbD3gbSx8NFdNgM947aZSpPSPSWPOiOru3Ep2r6aTWw1P7Hd9YsBhkIvZXTp-o8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5ca0ffc7.mp4?token=jGlNiH3SMxgDQHg2Gml47rRxk-C4JSeOiD6K9AYjNHkxhJMHKc_fkotAVJoma81-UxMUYcA7zMY21Beb2PIEJXQVjjxismWBjfAVg5Cj3h_RkmUMpCOfAME2yovQwoN4ItA1Z6DSobOPl_4HGgTF8z3peS7-OWK3v2fHldaLJ504uzltaQ-hTv2kCNJPBE5bZ0W-0QcusJlXO88lEVSpZoKCXSUt_DNMG0UfJLNNsBgur_5ku7--Pyy4JiJ8Da0ibdPF5IyqaM6yx6mXrdxO_4cbD3gbSx8NFdNgM947aZSpPSPSWPOiOru3Ep2r6aTWw1P7Hd9YsBhkIvZXTp-o8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشکان خطیبی: نمی‌دانم تا سه ماه آینده بتوانم اجاره خانه‌ام را بپردازم یا نه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/681905" target="_blank">📅 11:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f63dfbc1.mp4?token=a_jmeclXayUcX-_I43PVF1ADT9vlVrneQ-LiAUTz4ygV86NFhRc4toUvzU3GT4jJ_vwvw3o0uXIdmIRdQwufJzqPlNFcWRhRVniOrY5aSi8MyQtaFwmk04i5AGrIqONh-LoeeLgNuweozfiHDk7I8eefKKut42fkC2uk75zMiAWU7igV3UX3Do1X4Mr0Hz-zKMlvAL239RTgDnt6JS2VSY5-rmmcXpsJAaN6bR_Nmx2SBLR8w3kkGYeh8PtKMQ8jqU_RUNKOkFnGd3GzMiQ_9F-k-xRqDNSppw_6D4q8WdXfupHvhekKsBj-kGpmaHrNxfiIyDFHRfS-aYMxkeIYPRyOkxwoLclEq2zaFfIeJalKjT66iPUSAVDk4OFEP24kr3wYWRyIM9Euvk5OWRReVBFnGYB7TJJrSoR1fv-HhZwUIM4n5Nn1FKBoMs8qV6sxTxLlTH-DTJImsVDIaHtT95nbM3urffQNL5hpUE5sshWlG_s0fp8GoSrq4y-p_E0pfq6-XIH5A8qL6PWxUJCPU2nOp8c1AotHDU71dk1wtFchanuRzDE6vERMbcM7PFSljcdlgWf221P07gKA_EuLHR-lVMoyp9kSFLBPUbfoqrOcmZBmyh_2yWgQQYekJz97sJ3ky1ADm98xx3MCiSXskZG5Jva44ivhsrqGB0IUmH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f63dfbc1.mp4?token=a_jmeclXayUcX-_I43PVF1ADT9vlVrneQ-LiAUTz4ygV86NFhRc4toUvzU3GT4jJ_vwvw3o0uXIdmIRdQwufJzqPlNFcWRhRVniOrY5aSi8MyQtaFwmk04i5AGrIqONh-LoeeLgNuweozfiHDk7I8eefKKut42fkC2uk75zMiAWU7igV3UX3Do1X4Mr0Hz-zKMlvAL239RTgDnt6JS2VSY5-rmmcXpsJAaN6bR_Nmx2SBLR8w3kkGYeh8PtKMQ8jqU_RUNKOkFnGd3GzMiQ_9F-k-xRqDNSppw_6D4q8WdXfupHvhekKsBj-kGpmaHrNxfiIyDFHRfS-aYMxkeIYPRyOkxwoLclEq2zaFfIeJalKjT66iPUSAVDk4OFEP24kr3wYWRyIM9Euvk5OWRReVBFnGYB7TJJrSoR1fv-HhZwUIM4n5Nn1FKBoMs8qV6sxTxLlTH-DTJImsVDIaHtT95nbM3urffQNL5hpUE5sshWlG_s0fp8GoSrq4y-p_E0pfq6-XIH5A8qL6PWxUJCPU2nOp8c1AotHDU71dk1wtFchanuRzDE6vERMbcM7PFSljcdlgWf221P07gKA_EuLHR-lVMoyp9kSFLBPUbfoqrOcmZBmyh_2yWgQQYekJz97sJ3ky1ADm98xx3MCiSXskZG5Jva44ivhsrqGB0IUmH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا توافق ایران و عمان درباره تنگه هرمز طولانی شده است؟
🔹
قرار بود تفاهم خرداد شروعی برای کاهش تنش باشد که آمریکا با پیمان‌شکنی جلوی آن را گرفت. گفت‌وگوها با عمان برای رسیدن به بیانیهٔ مشترک دربارهٔ سازوکار ادارهٔ تنگهٔ هرمز ادامه دارد.
🔹
نامه‌ای با منشاء وزارت امور خارجه خطاب به مجلس برای مسکوت گذاشتن طرح اعمال مدیریت ایران بر تنگه هرمز وجود ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/681904" target="_blank">📅 11:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a987f247.mp4?token=ezI1QT2AOm5uuDjMte3u8zuvA-cAxMriov0tuxd1lHG6OtC0IL104lpOtoIvhjLs5OQJ6TDvFHk13pu8_UDKqSdzA1n8FXYstAUUU4sdMGzocJQRLdbwmRyguqB283Q6lboSs_tMSOUMu_ULrxU7OtFflCzoKxUmPbHn0bEeEy3zI22Inq9bC7bORi5hi7CY--drLTZO3jYKpugFbj4Ap8kP0YQj2sSa61fZDThqEjPnA2ysBF_Rug5y_ox0G7JY02B_o835K2uEkU3thtAO8zCZyb_cVu4YscirjDv_9_jmen9q2UG8_8M6Y19Ycc7rLAObzUYYxyZEOo3VsO9RjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a987f247.mp4?token=ezI1QT2AOm5uuDjMte3u8zuvA-cAxMriov0tuxd1lHG6OtC0IL104lpOtoIvhjLs5OQJ6TDvFHk13pu8_UDKqSdzA1n8FXYstAUUU4sdMGzocJQRLdbwmRyguqB283Q6lboSs_tMSOUMu_ULrxU7OtFflCzoKxUmPbHn0bEeEy3zI22Inq9bC7bORi5hi7CY--drLTZO3jYKpugFbj4Ap8kP0YQj2sSa61fZDThqEjPnA2ysBF_Rug5y_ox0G7JY02B_o835K2uEkU3thtAO8zCZyb_cVu4YscirjDv_9_jmen9q2UG8_8M6Y19Ycc7rLAObzUYYxyZEOo3VsO9RjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: میانجی موضوعات ایران و آمریکا، پاکستان و قطر هستند
🔹
ما میانجی جدیدی میان مذاکرات با آمریکا نداریم.
🔹
دیدار مخفی بین آمریکا و ایران در اربیل عراق انجام نشده است و این خبر ساختگی است/ تیم مذاکره‌کننده مورد تایید همه ارکان نظام علی‌الخصوص بخش دفاعی کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/681903" target="_blank">📅 11:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivSbWcdT-gTylUljp1xHcZloIy04RpxynxP6fPGjUB4_Z485zkYAgEaPNNwjUnx7jZHitnVjvbHa0NdHgHvGwK6qPoVvm1L0RyeJSq704QQQ7HMhMSMwPDJtF83bfMn-2se-sWcZxC8ppyTv0McnXBuWvP5XcZx4R_rfMA6Klu2aATZq_6y-E_GH1BKyB41xK7m1g2Tu1hkM_hq55qE9S34FDbO1i2RZc7eceWexh6ug-N-26Op3Xn8EyrrvwyxjY8udvRWYqmZveqkyvcXHkHpk6fqEvsX5gN2PItMZHt2pkmLv5K3TTroMoI0QmVe9cVn84jihzjSataIag7aAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/681902" target="_blank">📅 11:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e09640ba.mp4?token=R2a0R44TXS_xYjn8g2ULP28uWd0yVfoBwNNC-N9idoMDnlUkp3j7IuN3wRuhpSiZxZ2slfjDkF-zEiENJwcTN6oYfUxTd8X-X2GqFU_QqzmknJ5JZmokdHnLHTuA-4WsNyX_zdFN3cjB5ymYTft6L5s-M9ZJr_z3-Ekmqjv-qfAfdfiuTwu47zgaKQXCnafoahy5hHuj-5CHCuaynbmCVzEduzXw6DUjwxFue5NJ66NUUQ2qOwXnGqYH9SB2JLfDEwc0ohqLBS9l0VJAuxdUOs_wDWv_JApdQnNApSuah4mY8mduR3kMv7bF7nkh_zJ6gV6Q20I-6BuJZMYRwd_qUIAnaUgwKO6Fe6UzCJR72QZ_fWx1uIgA1PN4XgJj3wbLYBS-mBo1wJjqKAg07B9xo4meGjWvJwfUsOnyhpCOdwzxwvh1GiHjHITFuGRNoMPl07EDWYRgC6kynDwAizSrKB6OF66zoTOvIxLhpalt5n82qC3kNRHQ7F38C20puu7hASLaslnngEsoE-P0WYGxjYiz7jEr6K94u4LSkTzJOQfQcuI6Bbt0cKqrU4FrDyj1T3Eh2BJJ7Z7B0vYGzDy6iC1wC3hRBiKZy3QOuaYrho6fPvdEWt4ezrk0aGNCtX-PsvAsHyVKRvR-3K21mftzAklj1wCbeGN8IGgLgErArSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e09640ba.mp4?token=R2a0R44TXS_xYjn8g2ULP28uWd0yVfoBwNNC-N9idoMDnlUkp3j7IuN3wRuhpSiZxZ2slfjDkF-zEiENJwcTN6oYfUxTd8X-X2GqFU_QqzmknJ5JZmokdHnLHTuA-4WsNyX_zdFN3cjB5ymYTft6L5s-M9ZJr_z3-Ekmqjv-qfAfdfiuTwu47zgaKQXCnafoahy5hHuj-5CHCuaynbmCVzEduzXw6DUjwxFue5NJ66NUUQ2qOwXnGqYH9SB2JLfDEwc0ohqLBS9l0VJAuxdUOs_wDWv_JApdQnNApSuah4mY8mduR3kMv7bF7nkh_zJ6gV6Q20I-6BuJZMYRwd_qUIAnaUgwKO6Fe6UzCJR72QZ_fWx1uIgA1PN4XgJj3wbLYBS-mBo1wJjqKAg07B9xo4meGjWvJwfUsOnyhpCOdwzxwvh1GiHjHITFuGRNoMPl07EDWYRgC6kynDwAizSrKB6OF66zoTOvIxLhpalt5n82qC3kNRHQ7F38C20puu7hASLaslnngEsoE-P0WYGxjYiz7jEr6K94u4LSkTzJOQfQcuI6Bbt0cKqrU4FrDyj1T3Eh2BJJ7Z7B0vYGzDy6iC1wC3hRBiKZy3QOuaYrho6fPvdEWt4ezrk0aGNCtX-PsvAsHyVKRvR-3K21mftzAklj1wCbeGN8IGgLgErArSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: نقشه مسیر تردد دریایی با عمان با جدیت در حال تدوین است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/681900" target="_blank">📅 11:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681899">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بقائی: ایران حقوق حاکمیتی خود در خلیج‌فارس را با جدیت پیگیری می‌کند
سخنگوی وزارت امور خارجه:
🔹
جایگاه مجلس در قانون اساسی شفاف و روشن است و وزارت امور خارجه خود را موظف می‌داند در تمامی روندهای مربوط به قانون‌گذاری، همکاری‌های لازم را با مجلس انجام دهد.
🔹
در خصوص مباحث مرتبط با حقوق حاکمیتی جمهوری اسلامی ایران در خلیج‌فارس، تنگه هرمز و دریای عمان، قوانین پیشین موجود است و وزارت امور خارجه در مواضع مطرح‌شده، همواره هم قوانین کنونی و هم تحولات روز را مد نظر قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/681899" target="_blank">📅 11:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681897">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b678ed152d.mp4?token=r1kS8fWZIN9eOUZebaaM1tgAFqdgH5TrEoxqVxYZdM3t1K-OYOHiwrhIhkTkouBRPRdB-6JVgI5_RLKBGRX2vgFNX0tVX6StvZPqd4CCBVHbbMt0SRyx4SXs0htU72Cxw-eTXSDI4j5XmAtii5yIdEWCSF9Xyd5OT3zEg_0Gfx5wr4glCrctrPvrIlyliVTIYIHS8Igv4OuTD0K2ptb1eK9TpsZnXMMkOlEAAs7RELNPqAXGlYHDizgKFozKhjCklqA4ByR6TvhT7MGnzGi7wyY5yx_d9UuIdJEDEQjqCyBWx6HyA5S0KGuPVxKCkNgpFO5aflFaY4XN4qpifvzUJTHib_GmbyS5-wLAEm-flmXoAei6PXGqoAxLqos7vepwwq4cicMU_ezRPaAR4ZalYKdvrLk2jQW3Pr_-dagvN3O7Ej0tyOAgy9-Y2XnmymhY-vmgejf14ETxGfnYEzg9TOwoaqpYJ4DbPl_gjIunEYiZXFq6dcvPuTsD7R1uYIaMtXKTz8nUE6NOtA9d9DSUlqhHTKJFdkzTrp-f2U3KY0WqZtZkAPUhgxo-wf-7ATVKNW3w3aoJ92ya323bgILUEAT02iz7IYzniL_vP1R2aB7egxVyy31l3l7KwhtnfJjAu9O7rMrZhtMfDwOBevZeWZfW0jY3BvNJDWOMNpj1yHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b678ed152d.mp4?token=r1kS8fWZIN9eOUZebaaM1tgAFqdgH5TrEoxqVxYZdM3t1K-OYOHiwrhIhkTkouBRPRdB-6JVgI5_RLKBGRX2vgFNX0tVX6StvZPqd4CCBVHbbMt0SRyx4SXs0htU72Cxw-eTXSDI4j5XmAtii5yIdEWCSF9Xyd5OT3zEg_0Gfx5wr4glCrctrPvrIlyliVTIYIHS8Igv4OuTD0K2ptb1eK9TpsZnXMMkOlEAAs7RELNPqAXGlYHDizgKFozKhjCklqA4ByR6TvhT7MGnzGi7wyY5yx_d9UuIdJEDEQjqCyBWx6HyA5S0KGuPVxKCkNgpFO5aflFaY4XN4qpifvzUJTHib_GmbyS5-wLAEm-flmXoAei6PXGqoAxLqos7vepwwq4cicMU_ezRPaAR4ZalYKdvrLk2jQW3Pr_-dagvN3O7Ej0tyOAgy9-Y2XnmymhY-vmgejf14ETxGfnYEzg9TOwoaqpYJ4DbPl_gjIunEYiZXFq6dcvPuTsD7R1uYIaMtXKTz8nUE6NOtA9d9DSUlqhHTKJFdkzTrp-f2U3KY0WqZtZkAPUhgxo-wf-7ATVKNW3w3aoJ92ya323bgILUEAT02iz7IYzniL_vP1R2aB7egxVyy31l3l7KwhtnfJjAu9O7rMrZhtMfDwOBevZeWZfW0jY3BvNJDWOMNpj1yHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران وجود هرگونه مهلت ۶۰ روزه در تفاهم‌نامه را رد ‌می‌کند
/
نقض فاحش تفاهم‌نامه از سوی آمریکا گفتگوها را متوقف کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/681897" target="_blank">📅 11:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d904e99ae.mp4?token=CDX9bRWIpT2ky5j4CqkDh0bZgaW5n8XPoV3Co9UimslTP4Fo5Jso_LP_RKz2EOgPV0OQ-5YNnmMjjumi8BpKyPAyzI6i14iiIYViXaMyJsa0uIEhjSR48gfRbJmQOr-Kxg9O5SS5seYOX5OqEeH_4YAX1dqptD09wjBOwWsk7lSbbKDH0_omABmZfbTLWLnReb_qmE81GxrpfBI_McEWf4jnCBKVFVxhwN2suxh8zJnxcVU1-7k8dlIpfJxaHUrlEiyjMRIMfWshpqjrSv8Ph9iKmk186-yKyirU7M7Wo-hwgGw_OTTuqYY9l1Ii9iCdS1k0FKO1-Mdk5I5hw214lrivy8RFuZBQ_QeoFgqkYxBEvzX-RCNVvR1F_-rK2XNi_mJuNCjI51eWUfQdOJhGyNfTnNxIanBfT_mekmzos10pGplfBHzDWqA9xQE9Y_IEwVKrDxgFUbjt5K9J9ExZ6o1SU1czX7R7Wm8uahIwOUTYks_c85fgQB4JETxsP0d4WR7oSIbQD8LGtJSCYT3dlrp_FVMzqAvSkt9HqdVttpw3x1Yyo8KDKmAJbllTBlGuM2kFrtgPj3f9AslK1T1UCKGAeG0fGdEwjpzGShqRS8s6GkZktKThwaGjdtqBC3KF5JIgvqumrUcaKti4zczdR5gX9fVCCRJPpAfwJz9iJ5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d904e99ae.mp4?token=CDX9bRWIpT2ky5j4CqkDh0bZgaW5n8XPoV3Co9UimslTP4Fo5Jso_LP_RKz2EOgPV0OQ-5YNnmMjjumi8BpKyPAyzI6i14iiIYViXaMyJsa0uIEhjSR48gfRbJmQOr-Kxg9O5SS5seYOX5OqEeH_4YAX1dqptD09wjBOwWsk7lSbbKDH0_omABmZfbTLWLnReb_qmE81GxrpfBI_McEWf4jnCBKVFVxhwN2suxh8zJnxcVU1-7k8dlIpfJxaHUrlEiyjMRIMfWshpqjrSv8Ph9iKmk186-yKyirU7M7Wo-hwgGw_OTTuqYY9l1Ii9iCdS1k0FKO1-Mdk5I5hw214lrivy8RFuZBQ_QeoFgqkYxBEvzX-RCNVvR1F_-rK2XNi_mJuNCjI51eWUfQdOJhGyNfTnNxIanBfT_mekmzos10pGplfBHzDWqA9xQE9Y_IEwVKrDxgFUbjt5K9J9ExZ6o1SU1czX7R7Wm8uahIwOUTYks_c85fgQB4JETxsP0d4WR7oSIbQD8LGtJSCYT3dlrp_FVMzqAvSkt9HqdVttpw3x1Yyo8KDKmAJbllTBlGuM2kFrtgPj3f9AslK1T1UCKGAeG0fGdEwjpzGShqRS8s6GkZktKThwaGjdtqBC3KF5JIgvqumrUcaKti4zczdR5gX9fVCCRJPpAfwJz9iJ5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایران وضعیت خلبانان ارتش را از مجاری دیپلماتیک پیگیری می‌کند
سخنگوی وزارت امور خارجه:
🔹
از روز اول که مطلع وضعیت خلبانان شدیم پیگیر آنها هستیم. ۲۵ اسفند اولین مکاتبه با صلیب سرخ در خصوص پیگیری خلبانان را انجام دادیم
🔹
مطالبه روشن کردن وضعیت خلبانان ایرانی بسیار جدی است. مادامی که وضعیت سه خلبان ما روشن نشده، به معنای این است که به اسارت درآمده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/681895" target="_blank">📅 11:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVaxDGG-OG4NA17uUWBJSmzkkLuDQu1TC3053Hjqi8PqIHJxFROFl2-pe3qMfv7i7p7BLNOlD_6wX18W2xHINS9hpZHXDhuIQQZS9qW61cQHVtpJAbBUVwNBw8wjHNDYangzkdv5iaM8lYOWmDUcwDGio2OBKkPBcTjGSwKZkdO7xgDfgJdXQ1lu_xZmfnkSt0yhH9Rftw9SPw3XBHLGLU1vErdffFuWLyZG1JMzwaMGnqC0okH2MD4C2ZKeTF2AZ3gAnySc0_dxl02aQQ80ucWtdA4fJM75CUDeHfv2wbH-mE-i-e7RoUGxRG2DLDIwOlsBgzYnGFVlMT3yTAUHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/fast/37832/180124/</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/681894" target="_blank">📅 11:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تصاویری از بقایای جنگنده اف۱۵ و پهپادهای منهدم شده آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681893" target="_blank">📅 10:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
منابع سعودی مدعی حمله موشکی به باب‌المندب شدند
🔹
برخی منابع خبری از حمله موشکی ارتش یمن به یک کشتی در باب‌المندب خبر می‌دهند. هنوز ارتش یمن در این زمینه واکنشی نشان نداده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/681892" target="_blank">📅 10:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dca5abbd.mp4?token=Y6kwbXjMG7pcVnNVkTdOqjmOF3GzYCAaWDYBsZKMpMN7YRwWSlY47odNiFfIOX1KvMcGuMC4nMUKeDdwNjvsUQwl6yiOUIs3P8DCEriri5jxv9DXUmhAr5oeHQivkvo1CKb35p9rRrBufP_HUFbeQZDeunSoA3cy76IMvPRBn9xzfl__QcCecjSlYzaIlx1y4sH2SumepDH6Tft3By5iX3NQdBjXVJHiElsbFJHy6aWy2GkGNFM_EiJzcIOe3VAb8LlEzpyFv7-ClbIUatnPiQEh4tig0cCQrLAU-RlHJzROPgINIXJZjdbAgLpNoZA01FlNrFRiFQM86oYjYJ4bYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dca5abbd.mp4?token=Y6kwbXjMG7pcVnNVkTdOqjmOF3GzYCAaWDYBsZKMpMN7YRwWSlY47odNiFfIOX1KvMcGuMC4nMUKeDdwNjvsUQwl6yiOUIs3P8DCEriri5jxv9DXUmhAr5oeHQivkvo1CKb35p9rRrBufP_HUFbeQZDeunSoA3cy76IMvPRBn9xzfl__QcCecjSlYzaIlx1y4sH2SumepDH6Tft3By5iX3NQdBjXVJHiElsbFJHy6aWy2GkGNFM_EiJzcIOe3VAb8LlEzpyFv7-ClbIUatnPiQEh4tig0cCQrLAU-RlHJzROPgINIXJZjdbAgLpNoZA01FlNrFRiFQM86oYjYJ4bYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: همه دیدند ایران امروز با تجربه انباشته از استقامت و مقاومت از چند دهه گذشته، اراده جدی برای دفاع از حاکمیت و عزت خودش دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/681891" target="_blank">📅 10:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbS3lri4guEmNg8Ki7BFvWreUtGryf8cHnHNc_85VIoO7eSdGenaMsg5VahaLFu__CQdwMJh50o7vmlPZdPHy8iWATTz04kca20LS9jDwkblHv2zR8_tQGUg5PEm-Ix7ECCmdemuNNEK9axGAp_JpX9pSaNPckH1qBbS4muvDTi6zXreKo-Dh0GzdSY4-kNjWBqU11a3DhY8_42B8d96zcraTte25qAFqeJSZU3Mu_oT6420fOqKbkt0a1rbsR8LSO565NzPQldBcwrCk1hOyyqoaxWbUtHGszzDwQXJA7n-HikVKqVJeT3bVno9YEAIe0IRRqOPtCONgN2yX8EDbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا و رژیم صهیونیستی در جنگ شناختی، به دنبال ایجاد «ناامیدی» و «درماندگی» با تزریق اخبار منفی، بزرگ‌نمایی مشکلات و القای این حس که «هیچ راه حلی وجود ندارد» هستند. در برابر این ماجرا دو راهکار فوق گره‌گشاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/681890" target="_blank">📅 10:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=oUBFKdMjvqD40wNbbGkwrd6Q-2YF7Sqa4jElZ0uEoB4mPNMxUfjqZ0E8jqgeXCuVpv1efFofBPeTGlDi45NB9vTb2ErFmBNPFowMPrfiPSOmb9wMITraIJgbSN1dj24EM6nG560Y79OuvwzsMjTNJ5jIq0RYauo9NQG5RLjZowZSuxl4HjjD3q403kpnq12PUk-SJunfoyPwc-l_gbwLx8omoVv1yGikE54S8nT3K97nkC4HwqqQTJZ4mqTiwP4ZoZlw-dYEA-Tcinq2beYsi4KHpsjwL07-MewVRxlJ131kqaHFk5P7UFNWYv78qvVFR1C6nC7SqDxBxwCV0uOAF0ke10BGe4_Dgn42tcDAIIX6ucYy0M2TxfrF0htcD8ME5VTM3gebSBkmYatlyJFr8Q41IxRbwY46NWoEvhClrkVTs73VqpOpeRkcFtEpcXbVJwAb3vYqgcsL4X33nTb5QznCQpFvNPQLEDfNcK07iOQ5Mey0oSAytWhbAled6dVADLtzAyuiBKFphdD5_hDtImVDiD2xVOX-NRvMREF6HtB3paGyOSHHbq0SXqNVqgPJFqoSrbTOz9opKDSd6I5dVascFdKJKQBGr2I5kDt13QOrXbxSJD3TNkS_d3e-n01qCeClAYs56VKG0Mc6SlCwZOwKSY86ZtLzQsaPt-SeFuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=oUBFKdMjvqD40wNbbGkwrd6Q-2YF7Sqa4jElZ0uEoB4mPNMxUfjqZ0E8jqgeXCuVpv1efFofBPeTGlDi45NB9vTb2ErFmBNPFowMPrfiPSOmb9wMITraIJgbSN1dj24EM6nG560Y79OuvwzsMjTNJ5jIq0RYauo9NQG5RLjZowZSuxl4HjjD3q403kpnq12PUk-SJunfoyPwc-l_gbwLx8omoVv1yGikE54S8nT3K97nkC4HwqqQTJZ4mqTiwP4ZoZlw-dYEA-Tcinq2beYsi4KHpsjwL07-MewVRxlJ131kqaHFk5P7UFNWYv78qvVFR1C6nC7SqDxBxwCV0uOAF0ke10BGe4_Dgn42tcDAIIX6ucYy0M2TxfrF0htcD8ME5VTM3gebSBkmYatlyJFr8Q41IxRbwY46NWoEvhClrkVTs73VqpOpeRkcFtEpcXbVJwAb3vYqgcsL4X33nTb5QznCQpFvNPQLEDfNcK07iOQ5Mey0oSAytWhbAled6dVADLtzAyuiBKFphdD5_hDtImVDiD2xVOX-NRvMREF6HtB3paGyOSHHbq0SXqNVqgPJFqoSrbTOz9opKDSd6I5dVascFdKJKQBGr2I5kDt13QOrXbxSJD3TNkS_d3e-n01qCeClAYs56VKG0Mc6SlCwZOwKSY86ZtLzQsaPt-SeFuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشاورزی: قیمت اغلب کالاهای اساسی و مواد غذایی نسبت به هفتهٔ گذشته و نسبت به ماه گذشته رو به پایین است
🔹
مرغ سال گذشته ۱۴۰ هزار تومان بود الان بیش از ۳۷۰ هزار تومان است که دلایل خود را دارد.
🔹
جنگ روی افزایش قیمت‌ها تاثیر گذاشته و قیمت‌های جهانی ۱۰ تا ۲۰ درصد افزایش پیدا کرده و کرایه‌های حمل بین‌المللی ۱۲۰ تا ۲۰۰ درصد افزایش پیدا کرده است.
🔹
نان پرمصرف‌ترین ماده غذایی در کشور است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/681889" target="_blank">📅 10:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681886">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41942480a7.mp4?token=gwmWNWKt4CZalXsg8fhHVOjzfj-iuzwJTybdgFMzvAay0GvULhzotWQytEPdgfDTlcnxp8FGeujhzygJjwkOgqwXgvMRlE9LlaGQ6NvDPGk1tZfFtYAdZfV5spD9tHyu5dM65vIBhmKA6zDhyEwO91FJZbn47-YyEwwynKbPGYkltvrd76CZQLoXG9u8aQVcoTa4_9c2ePnvm8FH4gNxCOusuuOdok2lWT8rKPrOU4XoxRo1uV5eZ3aRW-f9ad5WYRWnDRZ74NjbGAphaCBv0sVokP2SUoaEDF2SePIFpe0x1HABpyM94-A1ioyScilecxhDOWUhm_2bx5sjzNBhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41942480a7.mp4?token=gwmWNWKt4CZalXsg8fhHVOjzfj-iuzwJTybdgFMzvAay0GvULhzotWQytEPdgfDTlcnxp8FGeujhzygJjwkOgqwXgvMRlE9LlaGQ6NvDPGk1tZfFtYAdZfV5spD9tHyu5dM65vIBhmKA6zDhyEwO91FJZbn47-YyEwwynKbPGYkltvrd76CZQLoXG9u8aQVcoTa4_9c2ePnvm8FH4gNxCOusuuOdok2lWT8rKPrOU4XoxRo1uV5eZ3aRW-f9ad5WYRWnDRZ74NjbGAphaCBv0sVokP2SUoaEDF2SePIFpe0x1HABpyM94-A1ioyScilecxhDOWUhm_2bx5sjzNBhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«سردار جوانی» معاون سیاسی سپاه: تنگه هرمز زمانی باز می‌شود که آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد عمل کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681886" target="_blank">📅 10:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681885">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من چطوری می‌تونم پرچم وطنم رو پاره کنم؟!
🔹
۲۶ مرداد، سالروز درگذشت عزت‌الله انتظامی. او از حاجی واشنگتن و سکانسی می‌گوید که باید به پرچم ایران بی‌حرمتی می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681885" target="_blank">📅 10:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681884">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
همتی، رئیس بانک مرکزی: مطالبات ایران از بغداد پیگیری می‌شود
🔹
پاکسازی لکه‌های نفتی سواحل هرمزگان به پایان رسید
🔹
رئیس پلیس فتا فراجا: ادعای فروش سؤالات کنکور کلاهبرداری است.
🔹
مسئول سیاست خارجی اتحادیه اروپا: این اتحادیه در حال آماده‌سازی «گسترده‌ترین بسته تحریمی» خود علیه روسیه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681884" target="_blank">📅 10:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681883">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
آیا آمریکا به دنبال تدوین چارچوب جدیدی برای مذاکرات با ایران است؟
احمد الرهید، خبرنگار الجزیره در واشنگتن:
🔹
آمریکا به‌جای تهدید نظامی، بر تشدید تحریم‌ها برای بازگرداندن ایران به مذاکرات متمرکز شده است.
🔹
ترامپ درباره پایان مهلت تفاهم‌نامه سکوت کرده و استقرار نظامی در منطقه به‌عنوان اهرم فشار ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681883" target="_blank">📅 10:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصلش تموم نشده حتما این دسر لایه‌ای‌ انبه رو درست کنید که خیلی خوشمزست
🥭
مواد لازم:
🔹
انبه دو عدد
🔹
خامه صبحانه: ۳۰۰ گرم (یک پاکت و نصف)
🔹
پنیر ۱۵۰ گرم
🔹
بیسکوییت پتی بور دو بسته
🔹
پودر قند ۶ قاشق غذا خوری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/681882" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZm7XL63E8xsTMFRG705eRnD7VE4E1Pa053x-NkB2qErlWalSLuG5vkdJ1Qz_Arc0dmCa2yGDvb9hMo7LvB-2Z4Uz5ZFErcQK8OHD-bBZQ7AjwF2rpZTuiGkGDUZwbpgoyQsifzojH3ioBecdHN74tsZHMjjUi7DbFQZSyrYo8vGPOWsG3j6nGZDuVPMr93N2RVc-VPQaIWeI1GfWxplW5xQ0s0Ffkq8MuVbcvBqrHT4DVv3tM5WdBjn8Du2qyD2SFmeAq_vCWBCB0hLzMqZPWmtaBQ5ERY5bkoJTft-Szv9BM3l6QMplY-ROgN6LkReARt4telbE5kSIh391sZznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه در حال ایجاد پایگاه‌های پهپادی مخفی در نزدیکی خاک ناتو است
ادعای تلگراف:
🔹
روسیه حداقل ۱۰ پایگاه جدید پهپادی با ۵۹ ریل پرتاب در مرز بلاروس و اوکراین ساخته است
🔹
پهپادهای دوربرد پیشرفته، قابلیت رسیدن به لهستان را دارند، نگرانی از تهدید زیرساخت‌های ناتو در درگیری‌های آینده./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681881" target="_blank">📅 09:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
وزیر جهادکشاورزی: به خاطر محاصره دریایی، جنگ با شدت ادامه دارد
🔹
در امنیت غذایی کشور و موجودی کالاها مشکلی نداریم؛ اما قبول دارم به خاطر جنگ و محاصره دریایی هزینه‌ها بالا رفته است
🔹
دولت طی دو سال گذشته هیچ روز آرامی نداشته و هر لحظه درگیر یک حادثه بوده است/ از همه چالش‌ها عبور کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681880" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coIxzxfAaJHZe6ukP3-tjERmmKgZhKPMEuVrcVX71O9qRBVbf8J9QSmlc-DyoO56h2pJmDlExWYbF7EUHCXDPg4BQxpH4tHaKQBJ-gfnm0wr9zqzRtyCL_WnwvgBpW4Jqne_IrYHDfc32uR7_Jnc2-105y5bgBevdp1mKg7KnQBv_nF2m8el6hELJHihQfjiCDE7rBOA2yQlnDVmXI6OPllQcwe3-LPbt15padpNxvHuDjzZeRn9u3GU5egJYCpJIYem4nQmuT8Bjx_1MywdJkjAyha1l5RWc-CwnbV-YGC6frN1PJfJpYD2MPWIXr6qKdfE4cEKpvH_4Tndjjx4sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس در آستانه ۵.۹ میلیونی شدن
🔹
شاخص کل بورس با افزایش ۱۲۸ هزار واحدی به تراز ۵ میلیون و ۸۵ ۹۴ هزار واحد صعود کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/681879" target="_blank">📅 09:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
کشت غیرمجاز خشخاش در کشور محدود است
معاون مبارزه با مواد مخدر ستاد مبارزه با مواد مخدر:
🔹
کشت خشخاش و شاه‌دانه در ایران ممنوع است و موارد مشاهده‌شده بسیار محدود و در مناطق صعب‌العبور بوده است.
🔹
با کاهش کشت خشخاش در افغانستان، قاچاق به محموله‌های خرد و مواد صنعتی مانند شیشه تغییر مسیر داده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681878" target="_blank">📅 09:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqD3NkXFFRwN-ihcP9Ui0Ya_o4IpeHdvuNxk4i4kayLdbV8anlN0IrK8Xl3RewuBVRrnvKLisNZtCOriBGhdWP9wfV69_yu9Yd0_LgXWob3aeclllF6gPKHOfojrfi_4D1S_Plxbp2QkNj-9WwWH_bzRHj1jQ6s4OLm0Of-_rcI-UeoUc_dADdPKm3Y03Wjw1ozxT9lOolk0MW9J7Xq2xUOIGdSIfAmFVqhMetfHSio-KhtL7512p0NKpJq1_o6URin2rw6LNzoW5BCX4A8g5IfuW-KOkpPEYN7qKoryc6IRqZd4IRZO7gqy-8fpleHL65iYiKrZ-_AVaMWUb0te9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه سی‌ان‌بی‌سی: گزارش‌های متعدد حکایت از آن دارد که شهریه تعداد زیادی از دانشگاه‌ها و مؤسسات آموزش عالی در آمریکا به بیش از ۱۰۰ هزار دلار در سال رسیده و آموزش عالی را برای بسیاری از جوانان غیرممکن کرده است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681877" target="_blank">📅 09:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681876" target="_blank">📅 09:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqlrsmm46evoSyyirpmgDme5mJ8h6u-oUBeWCytJTduWmoxa7H9Bgtm1HAinALtyPE3KwmayU1z95eLDOA0d257sv3qr0A8SLp2YyvHvJaHTXzyCrqddgu4yan-LTocGdozzgXFYN1CydtWCiFT280HcSjAQlJZ1LZZmVL6DHEMCP4GhP4ukEkJ2qz9DdGUsWTm5b0Un9vzTemQCHZc2EvuY8RFeJ_a_mPQTxmQDl6cbYjAmvzism5EkUzgaDp1HfLg8aFnRaIut5DdnjhmPiu6eJPp5g-FWgGp_1Ta-0DT35aHTrxQeel7LItYnW59lnT47qEi4LJAFFY7PmpP1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت با انقضای تفاهم اسلام‌آباد گران شد؛ هر بشکه برنت ۸۹.۴۰ دلار
🔹
توقف تردد در تنگه هرمز و بن‌بست مذاکرات، قیمت را بالا برد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681875" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
اختلال در سامانه‌های فروش بلیت قطارهای مسافری
🔹
درحالی فروش بلیت قطارهای مسافری از ۸:۳۰ امروز آغاز شده که کاربران از اختلال گسترده سامانه‌های فروش خبر می‌‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681874" target="_blank">📅 09:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
قائم‌پناه: ناچاریم به دلال‌ها نفت بدهیم اما هدفمان جمع‌کردن کاسبی تحریم است
معاون اجرایی رئیس‌جمهوری:
🔹
در زمینه نفتی که ناچاریم برای فروش به تریدرها یا دلالان بدهیم، پرسش‌هایی همچون زمان فروش، چگونگی بازگشت پول و تامین سلامت محموله تا بارگیری مطرح است که این شرایط می‌تواند زمینه کاسبی تحریم را فراهم کند، هرچند دولت در پی برچیدن تحریم‌هاست تا دیگر کاسبی وجود نداشته باشد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681873" target="_blank">📅 09:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaYcH-7AjisJUHn6mLTVupuFO7taZLDoQmwlJH0t0ilON6zBHtroxnH7UR9IZSLSDC__L3U86amtq8PVRRh-w8Aoio9TsCDlWGXpXibmvUH8anXE43lbzvxKDiUtWPh1fQRDGXL2UWSuXVw8lVmqnwsEqIpgKblvSV3rbQA0qRgzgm4mZW2I4GxsgSGDKTBiMWC4N-3vXlnN2oLaYYrp4J6WsZu9Ogot-xPkfUIJWn39j7Go38TsyAkOgqLizkHJhvnyMfJQkrmBbP8XKPjOgUKGFWIGxbzk9DFB5D2K-_lZwkS5bC59iEOl-uCXNvcvUVQH4UBmKvvnegzuTkF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دریافت کارت ورود به جلسه کنکور از امروز / چگونه کارت آزمون دریافت کنیم؟
🔹
توزیع کارت ورود به جلسه کنکور ۱۴۰۵ از امروز آغاز شده و تا چهارشنبه ۲۸ مرداد ادامه دارد.
🔹
داوطلبان باید مشخصات فردی و آدرس حوزه امتحانی را روی کارت بررسی کنند، مسیر حوزه را از…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/681872" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH37QUxeXoCk5V4iFGjiXkS9VnxeYgAjswyBpZYsQA4VB95APxQPPFYvkpUs0A5CWnRnb9K4Wxyv0HYak4r1m976bbkBT2s26tfAqC1TH_I_JvhesPgivMvEbstXnivRxFyfxmCx_jgBY3G2ijIK4Zg2sd3hPbnvVD3CzFAW8XgNwL9z-RO5roLlJ1XvNGeXSG1gvzeJ-b5SuWp0d-z13JM29o0633I1ioIs2j-tc-aPb7UY6acx1a8Bu28l4Cv-FDGEfL3DqJUzBC8T5cGl2oo0TsD6_gMG3pJLkixtNDDQgsJyGX7apPoXvYVpnCGNtgPSoIobnLLqmomZL7183g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی المپیاد جغرافیای ایران اول جهان شد
🔹
برای نخستین بار در رقابت‌های جهانی؛ تیم ملی المپیاد جغرافیای ایران در بخش Poster جایگاه اول را کسب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681871" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دریافت سالانه ۱۱ هزار درخواست سقط جنین قانونی در کشور
مدیر کل امور معاینات بالینی پزشکی قانونی:
🔹
موارد مجاز: خطر برای سلامت مادر یا ناهنجاری جنین که موجب حرج غیرقابل تحمل برای مادر شود.
🔹
رضایت مادر شرط اصلی است؛ آگاهی پدر لازم است اما رضایت او شرط نیست.
🔹
سقط قانونی فقط تا قبل از ۴ ماهگی جنین امکانپذیر است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/681870" target="_blank">📅 09:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
شمارش معکوس برای پایان آتش‌بس ایران و آمریکا/ جنگ به «جنگ اقتصادی» تبدیل شد
نیویورک تایمز به نقل از منابع آگاه:
🔹
مهلت ۶۰ روزه توافق اسلام‌آباد بدون نتیجه پایان یافت و جنگ وارد مرحله فرسایشی اقتصادی شده است.
🔹
واشنگتن خواستار بازگشایی هرمز است و ایران آزادسازی دارایی‌هایش را شرط آن می‌داند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/681869" target="_blank">📅 08:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اردوغان، رئیس جمهور ترکیه: هرمز باید بدون عوارض و هزینه قابل تردد باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/681868" target="_blank">📅 08:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعمال قدرت ایران در بحرین!
کارشناسان آمریکایی:
🔹
حمله ایران به پایگاهی آمریکایی در بحرین به یکی از هاب‌های اصلی پشتیبانی و لجستیک ناو لینکلن آسیب زد و کار به جایی رسیده که برای مثال یک ملوان در پیامی به همسر خود گفته فشار شرایط دارد مرا از پا درمی‌آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681867" target="_blank">📅 08:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نقل قول دکتر لیلاز از شهید لاریجانی هم از جهت تشخیص و پیش‌بینی اوضاع هم تلاش نظام برای جلوگیری از جنگ بسیار حائز اهمیت است.
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/681866" target="_blank">📅 08:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScYmwk3_56i3MaGKJFZEoEReCDOhr5vWLsKzBoxvVfiJ6D0VI0ynKkjko_9AvLvnERQCma4ZI2Vu-x2PNE_jQm5D9KAwg5qBZCdJuL-feVPG0ZZag83cQT1jINh8ly-tGHTlV2rx72354WRPOrkxPpGKri-4cwZWh8pDGoSMbVUzmjGIQh411SYuJNagfmOoK3dX55OaDqQjfkusfoNXT0GNhLj-lO30MTOB-ZI0tqdBvYhPW0cMMvny1pgce2GBSV2i8zyHpx4oAafZSiJbkY7XOGF5WSxbTQmtefVqNIYIupo02EYjGoZEwd3hyge-8aClTSAFZVoWb_rZdXw7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوگین، نظریه‌پرداز روس: ایران پرچم‌دار مبارزه با اسرائیل است؛ ظهور مهدی نزدیک است
🔹
الکساندر دوگین، نظریه‌پرداز روس، با تمجید از آنچه «وحدت و آمادگی ملت ایران برای فداکاری» خواند، از کشورهای اسلامیِ در تعامل با اسرائیل انتقاد کرد.
🔹
او همچنین با طرح ادعاهایی درباره «جهاد علیه دجال» و «پرچم سیاه خراسان»، از مسلمانان جهان خواست از ایران حمایت کنند و گفت:
«معتقد هستم ظهور مهدی نزدیک است.»
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/681865" target="_blank">📅 08:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b5d98ea0.mp4?token=RM4vpsW_4vi5bzFyVF5GdKjDhtWIcQza7vijfhA9l6n6onIejmiFmucCu2UL6qvOUVU-XC4UCO2qKty3fDn5-H_BalfapwQYRvOVed6rSLr0Ecq2jdNd3OEoUTxEQuITv-LIHgEk8vJnWUf1hHtsYcc-a8TSfpPz56X4if-nUexaaKg06jncam8rUruJsHzJ07oI0CHX2zNnrJA7yAlJxeCK-fCZt9xx2gxpu0tPppK07yUl7IaL2nEU5-GMyrH3XXWV1rDBv9g4qIPEERHw5l2MH4u3c-MD3dsNpvc3sA8oRk2UY0LBzaUrhDsY5CNX_EGjepLfvsBovxUl0fIdNXiYfPVMkR0hUTYPMgZ1K4DioHunTpboZyJVNnuTt07BkuuE2lxxeOpmAWdc6Ws4rsBHppywDb1I6ESNz1LhRug-SU2B3PTFHdISOaaAKKY603t-EwgFehW7xOSez0UxtwjJwAoll_Zx6lmX0OiJe1W6XU2R19kRyeQLeTdyyO6-k7Ezo_07GUEAzfkuD6WJXEhxRCLgEFFsYCVgEoZLvKaM_t9NdqrTdyoGJ3wWp3CpnALPQdSRcwXfeNEIopqjBcssqgrG7fH6lWveKZrh_urDURaK9LCSaCmcHa_eLFq9UhVHWJjvyu0GygTL_Dp7xHwwGgs6KvPojACkZtO2yNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b5d98ea0.mp4?token=RM4vpsW_4vi5bzFyVF5GdKjDhtWIcQza7vijfhA9l6n6onIejmiFmucCu2UL6qvOUVU-XC4UCO2qKty3fDn5-H_BalfapwQYRvOVed6rSLr0Ecq2jdNd3OEoUTxEQuITv-LIHgEk8vJnWUf1hHtsYcc-a8TSfpPz56X4if-nUexaaKg06jncam8rUruJsHzJ07oI0CHX2zNnrJA7yAlJxeCK-fCZt9xx2gxpu0tPppK07yUl7IaL2nEU5-GMyrH3XXWV1rDBv9g4qIPEERHw5l2MH4u3c-MD3dsNpvc3sA8oRk2UY0LBzaUrhDsY5CNX_EGjepLfvsBovxUl0fIdNXiYfPVMkR0hUTYPMgZ1K4DioHunTpboZyJVNnuTt07BkuuE2lxxeOpmAWdc6Ws4rsBHppywDb1I6ESNz1LhRug-SU2B3PTFHdISOaaAKKY603t-EwgFehW7xOSez0UxtwjJwAoll_Zx6lmX0OiJe1W6XU2R19kRyeQLeTdyyO6-k7Ezo_07GUEAzfkuD6WJXEhxRCLgEFFsYCVgEoZLvKaM_t9NdqrTdyoGJ3wWp3CpnALPQdSRcwXfeNEIopqjBcssqgrG7fH6lWveKZrh_urDURaK9LCSaCmcHa_eLFq9UhVHWJjvyu0GygTL_Dp7xHwwGgs6KvPojACkZtO2yNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک مهاجر از شوک‌های زندگی در اروپا؛ وقتی واقعیت با تصویر «بهشت غرب» فرق دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/681864" target="_blank">📅 08:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681863">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
کالابرگ مردادماه برای ۳ گروه حذف شد
🔹
از مردادماه زمان شارژ کالابرگ تغییر کرده؛ گروه اول پانزدهم، گروه دوم بیست‌وپنجم و گروه سوم پنجم ماه بعد می‌توانند از یارانه غیرنقدی استفاده کنند.
🔹
در نتیجه، سرپرستان خانواری با رقم پایانی کد ملی ۷، ۸ و ۹ کالابرگ مردادماه…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/681863" target="_blank">📅 08:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681862">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
آغاز دریافت کارت ورود به جلسه کنکور از امروز / چگونه کارت آزمون دریافت کنیم؟
🔹
توزیع کارت ورود به جلسه کنکور ۱۴۰۵ از امروز آغاز شده و تا چهارشنبه ۲۸ مرداد ادامه دارد.
🔹
داوطلبان باید مشخصات فردی و آدرس حوزه امتحانی را روی کارت بررسی کنند، مسیر حوزه را از روز قبل پیدا کرده و وسایل مجاز آزمون را آماده کنند تا از استرس و اتلاف وقت در روز کنکور جلوگیری شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/681862" target="_blank">📅 08:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ad9c2ab7.mp4?token=G8njM0GLLn1Qy8HxZIzDZLNQBxuZovdHyDFE5bVu8l4Na8HABub7mrF4HNYT6rswp0LdfmTdquxqAUbVhUGiSyCN18VwtNFCV4MKhd4yFqBlm6n9syWTK-0aXe1XIvzIr0833bly0HWSxx9IkX-BObFwb3KB3I7O2bs8Sjt9UdjU1cVpHKb6hgToF71etgNa7ZSLzIJLC7DwoysnmoOw_q0BbctC8_v1hlM2VwE4VHNQdafzoZJZ2FNv1OVSjCcf7iPXh5nKK985OEQ_lu_XCavor_IllliE4t_3nlNr5EGZ-_yjhX7ER-s5lXySriU6CQUJIuA0q5A3ke-ltj66KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ad9c2ab7.mp4?token=G8njM0GLLn1Qy8HxZIzDZLNQBxuZovdHyDFE5bVu8l4Na8HABub7mrF4HNYT6rswp0LdfmTdquxqAUbVhUGiSyCN18VwtNFCV4MKhd4yFqBlm6n9syWTK-0aXe1XIvzIr0833bly0HWSxx9IkX-BObFwb3KB3I7O2bs8Sjt9UdjU1cVpHKb6hgToF71etgNa7ZSLzIJLC7DwoysnmoOw_q0BbctC8_v1hlM2VwE4VHNQdafzoZJZ2FNv1OVSjCcf7iPXh5nKK985OEQ_lu_XCavor_IllliE4t_3nlNr5EGZ-_yjhX7ER-s5lXySriU6CQUJIuA0q5A3ke-ltj66KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌نوازی متفاوت مهراد هیدن با نوازنده آثار هانس زیمر
🔹
مهراد هیدن در حال نواختن یکی از قطعه‌های فیلم
Interstellar
در کنار راجر سیمور؛ نوازنده موسیقی‌های این فیلم که توسط هانس زیمر ساخته شده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/681860" target="_blank">📅 08:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf7ebe59b.mp4?token=hFtndmPpC3EKSXRL_Ek6xuH6pJCx5PWt9Yv7ei5r_-nDneEUaEYBkqfs-l3E3wEbBZ-M4dpQc8BBrJ1OJJPtgEnyx2BPz-Ky-BCKpR57XpDPHa7lHqZqGGHUaUt41ICkSrN2rdtP6lQGcsWm455AUXnUz5h-V7vDSzYIPYBfDAiOKEiksGT2MbI9guIps9-XHRNwyWOjXNgOgzlb0ysfbuOB2zpUhVu2al2e4JkWOAdT2wyifWVgc2EayWarHtILV1M79RVjvRsHgPEiFknDL2BpEscGBsD-kLB89JLiAVOiq64TKi-fqsFflgnkXQitKMiVbzYxXfTbXzaxEPL1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf7ebe59b.mp4?token=hFtndmPpC3EKSXRL_Ek6xuH6pJCx5PWt9Yv7ei5r_-nDneEUaEYBkqfs-l3E3wEbBZ-M4dpQc8BBrJ1OJJPtgEnyx2BPz-Ky-BCKpR57XpDPHa7lHqZqGGHUaUt41ICkSrN2rdtP6lQGcsWm455AUXnUz5h-V7vDSzYIPYBfDAiOKEiksGT2MbI9guIps9-XHRNwyWOjXNgOgzlb0ysfbuOB2zpUhVu2al2e4JkWOAdT2wyifWVgc2EayWarHtILV1M79RVjvRsHgPEiFknDL2BpEscGBsD-kLB89JLiAVOiq64TKi-fqsFflgnkXQitKMiVbzYxXfTbXzaxEPL1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر روز صبح چند دقیقه وقت بزارید این چندتا حرکت رو بزنید و معجزه‌شو ببینید
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/681859" target="_blank">📅 08:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQKrpZt8lArmKc45VjlBJ7dFSaT_qe35nwDg1MIAMmNavRwsFoVnP4uSV_WLwQNMYajFeqmquCoEJJput8bZcdE3lblDY8xn3oBUzYkROuD0dpQzAE123xnQZ1V0J3jZ-40MEmwjRx4PG0xwIknxbREyDLF1aLhSutGhnG44R7r7rO9Gis8rD6m1CYqW9sLL23I6JFIxQy1uXQF0iRqP9CCxEend1nDC7uhRE53rt0K6WqtB2wm-pRrTICVUt2CEbsZ3IlKgmO54xyXAsdg5CG5PVB-Wem1wUe2RxSKWXTdbS2KGnFGRf06LjfhdHrjrkboOeu5PhPXDMv-5PiqX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر امریکایی در واکنش به هلاکت رسیدن سربازان آمریکایی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/681858" target="_blank">📅 08:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omsSvL1EsqibtiHrEcThrKZO2dkTgC3kZe_0w103Ll3PyDbF4XwdhG625i7PxH5EHEySvTjTmlwgpGwaWCSTfsnV4_QmZyHBDrz9NWFgRZIG4idflNLvRILSvrrN-T8f-AZ4gTXFMx-MIwndC8ZPGve3Z_s-dRXUP1ir6U7bGfxGg_ESEiBB7AZryw5LRCBBsl81DvUoiJT6vO_j7exWLGQX4K4r0vCyTNGYZRFXc19WdSDk0AklYw_PX0FgRfLm_goWCqxIizmukjmj_mQZkN6KC0weUblAXGjLdkwzdfUiE-hNZ1u1WC5vwIiIqJpaJ8A2cRHDgVJK7mULycU3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با کنترل این ۳ عامل، مغزتان را سالم‌تر نگه دارید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/681857" target="_blank">📅 07:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681853">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
۱۲ میلیون جوان در سن ازدواج؛ ۱.۲ میلیون مجرد قطعی در کشور
🔹
مجردان قطعی؛ زنان بالای ۴۵ و مردان بالای ۵۰ سال
🔹
تجرد قطعی طی دو دهه حدود ۷ برابر شده، فاصله ازدواج تا تولد فرزند اول به میانگین ۴ سال رسیده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/681853" target="_blank">📅 07:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1jbnmy4R0huHoM4akPrHnG6hcJhn2U6nf7hAdGzd7RScHjZsTdslPT_bUadH1h9K1sX3ulOWaYgJen1J3QS0wyymYH7J4HqC5SmlTp0v26OC2wjavEe2xbjxl8XZCJt9grpKU9t0yTjHOvGdLk2jmuQKmv-87WFk3DFTdbgUyD8WYYmLGgAE3OpnPDOKhTkK68tRVU1bCPKczQuFk9_787oK4O6H_EbVbPv2GkFOneVwsxavUcVVN3Iyz1r0zUN9o9dBF-0MnH3FA2M4uxfC6_P4Q1hYD3qvZ6Xz2zmZdT0_xMsKyitEv1t9bBkEysimjZ3ECoynUVji83HrTMBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۶ مرداد ماه
۴ ربیع‌الأول ‌‌۱۴۴۸
۱۷ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681850" target="_blank">📅 07:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taXJDbgsCzKZZBj_XcbH34yzo3MBTFzsQvVoQn0hNGLer4EyhS4lvzbx5VMNH0fuB66AWx1x1j2WMMevs4PZ-quvt6a5OE5YPgCAjXIKJJw9PVdOxTmnK7CcjtfWZH8DIvBgcH9XLd2bSAZP86xhervhBJ1eKGQIeRAc0h1cvfEHK8i8fYZe2hXQfXrn0chgVSU8LwjvtadYMkPinKEW_hBtioWFxAyu8rb-NcN1j2d-ZQOad4W81VcSrwQ_XVKbWNDXZsC4fFD_Q15gazqYFWBRJm_WM_Hu11u7wHQRcXkxUaDB69qQlz4e10huuCxNq1eYxQ7q9A1RYbokYrct5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
هر خانواده یک وام تا سقف ۵۰۰ میلیون
✅
بدون سود
✅
بدون ضامن
✅
بازپرداخت تا ۱۴ ماه
برای انجام ایمپلنت و سایر خدمات دندانپزشکی
برای دریافت اطلاعات بیشتر کلیک کنید
👇🏻
👇🏻
👇🏻
👇🏻
https://t.me/arameshdental
https://t.me/arameshdental</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/681849" target="_blank">📅 02:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: اتفاقات خوبی خیلی زود رخ خواهد داد
🔹
دونالد ترامپ در خصوص ایران مدعی شد: اتفاقات خوبی خیلی زود رخ خواهد داد. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/681848" target="_blank">📅 02:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تسنیم گزارش می‌دهد: تراستی‌ها؛ ابزار دور زدن تحریم یا گلوگاه جدید ارزی؟
🔹
واژه «تراستی» در سال‌های اخیر از یک اصطلاح تخصصی و کم‌استفاده، به یکی از واژه‌های پرکاربرد در ادبیات اقتصاد تحریم‌زده ایران تبدیل شده است؛ واژه‌ای که در ظاهر، از سازوکاری برای مدیریت دارایی و انجام مأموریت مشخص حکایت دارد، اما در عمل، در اقتصاد ایران به شبکه‌ای از واسطه‌های مالی و تجاری اطلاق می‌شود که مأموریت اصلی آنها فروش نفت، میعانات نفتی و فرآورده‌های پتروشیمی در شرایط انسداد کانال‌های رسمی بانکی بوده است.
🔹
شکاف در حکمرانی؛ اختیار در دست کیست؟
ریشه اصلی بحران تراستی‌ها را باید در دوگانگی میان مرجع صدور مجوز و مرجع پاسخگویی جست‌وجو کرد. در سال‌های گذشته، بخش‌هایی از فرآیند صدور مجوز یا واگذاری مأموریت‌ها در مسیرهایی انجام می‌شد که لزوماً با سازوکار سیاست‌گذاری ارزی بانک مرکزی هم‌راستا نبود، اما در زمان بروز مشکل، این بانک مرکزی بود که باید پاسخگوی آثار ارزی، نوسانات بازار و کمبود منابع می‌بود.
🔹
راهکار چیست؟ برای اصلاح این وضعیت، نخست باید اختیار و مسئولیت در یک نقطه متمرکز شود؛ یعنی بانک مرکزی تنها مرجع سیاست‌گذاری، صدور مجوز و نظارت بر این‌گونه سازوکارها باشد تا امکان پاس‌کاری مسئولیت از بین برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/681843" target="_blank">📅 01:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681840">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری شگفت انگیز از تصویرسازی ابرها در آسمان نیوجرسی
🔹
ساکنان ایالت نیوجرسی آمریکا، تصاویری از این پدیده عجیب را منتشر کردند که ممکن است نشانه‌ای از بادهای شدید، باران شدید و رعد و برق باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/681840" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681839">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک‌سوم مبتلایان به آنفلوانزا زیر ۱۵ سال سن دارند
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
بر اساس نظام دیده‌بانی عفونت‌های تنفسی مرکز مدیریت بیماری‌های واگیر، ۴.۴ درصد مراجعان سرپایی و ۵.۷ درصد مراجعان بستری، دارای علائم عفونت‌های تنفسی بوده‌اند.
🔹
تست آنفلوانزا در ۰.۷ درصد و تست کووید-۱۹ در ۲.۹ درصد افراد دارای علائم تنفسی مثبت بوده است اما هر دو بیماری در سطح پایینی قرار دارند.
🔹
۸۰ درصد آنفلوانزاهای در گردش از نوع B هستند و نزدیک به ۳۴ درصد مبتلایان زیر ۱۵ سال سن دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/681839" target="_blank">📅 01:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681838">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: هنوز نمی‌دانیم چرا با ایران وارد جنگ شدیم
روبن گالگو، سناتور آمریکایی:
🔹
ما از سربازان آمریکایی حمایت می‌کنیم که تلاش دارند ما را از این جنگ بیرون بکشند. اما رئیس‌جمهور هیچ طرح و برنامه‌ای نداشته و معلوم نکرده این جنگ چقدر گسترده است، چطور پیش می‌رود و چطور قرار است تمام شود. مأموریت ما دقیقاً چیست؟ ما هنوز نمی‌دانیم اصلاً چرا با ایران وارد جنگ شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/681838" target="_blank">📅 00:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681837">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv2HkcIlK8S7TMtzOLCmoSOaWiD6KWrOegwC0a64yxQs_UNhT3QvTrEir2612bNPjgwuGYo-Oz6n2uNNj0PUHdTnPx2PAIBER3SGDtXEiPcAGf5A3NGGcXZ2wQWY8-lFAfg9I-BFKq2Xg8xkezmA3234sOKS6dXWDElURddtOX-pmaVA05JOt6muAE5KWFCYo_op5SC3omRlGYH9Ls0M82rCTNN6dJzWC9D8Yd5DQIa0oB1wcFF95RkXLXMT1736BgoHGKQJ0z_uSWO-2O-p3mSOdLrCkvKG091PaE1ukcHDLNd6BH6mpvp5lX-0yim3fdHfnza4J8l2XKHCSO6X_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناراحتی ترامپ از رزمایش مشترک نظامی با کره جنوبی
🔹
با توجه به روابط بسیار خوبم با کیم جونگ اون، رهبر کره شمالی، از این واقعیت که ایالات متحده مدت‌ها پیش موافقت کرده در رزمایش‌های نظامی مشترک با کره جنوبی شرکت کند، راضی نیستم. این رزمایش‌ها نه تنها پرهزینه هستند، که بخش زیادی از این هزینه‌ها توسط ایالات متحده آمریکا (طبق معمول!) پرداخت می‌شود، بلکه پیامی کاملا نامناسب و خصمانه به کشوری می‌فرستند که تا زمانی که دونالد ترامپ رئیس جمهور بوده، غیرتهدیدآمیز و محترمانه رفتار کرده است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/681837" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b38253a8.mp4?token=UwXdD0VtsgUE9q7Qet5UuQS2m_U_5qXMuvIhry565P7L9oxBXyZ1tpMZ3oaq0X5eLoYzGXyN5xe0-RPzpH2jpAcRAZ0bMvzHXsq8n-AZtsgoU039OJwFI61qcs98eLoPy2YonwJ0fh63mCdKku_HAP_rs3al6FPZOGWnJDW-wc4W3wiOXeoXWou4WQEO1RGivV6IqskWV-zTE3fQq7PcoNwKBedhjQvd7UZ_5BnUwwErRMqMCefDVrRCL-fyRe4_v89P4ZwZLOZsg4zq0cV032XoZ79mrgY7UqLvnPFdv-nlJlYCCmtX50BP-oDFMtbv3fFY1YnYsl3XYwkhEGVxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b38253a8.mp4?token=UwXdD0VtsgUE9q7Qet5UuQS2m_U_5qXMuvIhry565P7L9oxBXyZ1tpMZ3oaq0X5eLoYzGXyN5xe0-RPzpH2jpAcRAZ0bMvzHXsq8n-AZtsgoU039OJwFI61qcs98eLoPy2YonwJ0fh63mCdKku_HAP_rs3al6FPZOGWnJDW-wc4W3wiOXeoXWou4WQEO1RGivV6IqskWV-zTE3fQq7PcoNwKBedhjQvd7UZ_5BnUwwErRMqMCefDVrRCL-fyRe4_v89P4ZwZLOZsg4zq0cV032XoZ79mrgY7UqLvnPFdv-nlJlYCCmtX50BP-oDFMtbv3fFY1YnYsl3XYwkhEGVxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند قلم ساده دستگاهی برای سوخته کاری بر روی چوب بساز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/681835" target="_blank">📅 00:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر خوب؛ ۸۰ درصد سطح دریاچه ارومیه آب دارد
محمد کوهانی، دبیر ملی شبکه های محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سال گذشته در تصاویر ماهواره‌ای صرفا یک لکه آبی از دریاچه ارومیه دیده می‌شد، اما امسال بیش از ۸۰ درصد سطح دریاچه آب دارد و حجم آب آن به ۲.۵ تا ۳ میلیارد مترمکعب می‌رسد.
🔹
در سال ۹۸ حجم آب دریاچه ارومیه به حدود ۵ الی ۶ میلیارد مترمکعب می‌رسید. تجربه این سال نشان داد حتی اگر سال پرآبی داشته باشیم، بدون وجود برنامه انسان‌محور در سال‌های آتی مجددا دریاچه را از دست خواهیم داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/681832" target="_blank">📅 00:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
۶ دانشگاه ایرانی در جمع ۱۰۰۰ دانشگاه برتر جهان
🔹
تازه‌ترین رتبه‌بندی شانگهای ۲۰۲۶ منتشر شد و ۶ دانشگاه ایرانی در جمع ۱۰۰۰ دانشگاه برتر جهان قرار گرفتند.
🔹
دانشگاه تهران و دانشگاه علوم پزشکی تهران مشترکاً در بازه ۵۰۱ تا ۶۰۰، صدرنشین دانشگاه‌های ایران شدند.
🔹
دانشگاه صنعتی امیرکبیر نیز در بازه ۸۰۱ تا ۹۰۰ جای گرفت. همچنین دانشگاه علوم پزشکی شهید بهشتی، دانشگاه صنعتی شریف و دانشگاه تربیت مدرس در بازه ۹۰۱ تا ۱۰۰۰ قرار گرفتند. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/681830" target="_blank">📅 00:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c891f09.mp4?token=k4p9qQruifrbVpi_dr5DhzOZhUnUngugiNa9Gil7R7lpYHgW3gd9qVeQNs2_zVbZPdlRGXdzmxVGANxUWZMdqQEzGpsov8go3YiVcoYk5ZvZ8JuKVUMQ2-1q5ZUvfyIMksrNRhwdSnFVS5kRJTVL0vh6uwo8_l_pDwTavFyBWZg-x0iIIyMsjT5l9M_IjrV1Z1DIE2HlQ-Mbud9E3aHsZg_zMK8OUA_b8o8V9SuXbWcduSbUwk_jJVaxV9jK5iMydL7UtkIHEAEmgonAfvp1B4lHkKmHj7GL1qLZ0ys_WMMaUMNslpnUiJMJa5EkfLozgAhh_os9qzoxIbklDnqv3iyRmR_yOZYqmcpBoCeaRuE6R5E2ozRF3AHrKnmmJeuyQBCT1n5b_Y6k7G1J2xz8HfeTb7HmTIJGZUuxwlKH6abYPclgfktoUoJBqBnHtqLWTZrquaG81nx8RzXZgguVizy2Y3YR_9y6Rys8cpZx2uSRczCOMG1rWjpNJaCAwvOxw4V7TCbo7C21ZB-rCazqVFsNZteQuM504pFmkEikpZdx6uHkCdvzsATuLK0u7Z0_K6Lla_WHQ5G_nkPzP_UnNvzMaDpWxPKU_rLL1itfOt__f9fk5t9JZgYVCwsTxjsc5QIV3NfQ6vqcAtE3JYOyMw49l07PmERh22h3sfDva2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c891f09.mp4?token=k4p9qQruifrbVpi_dr5DhzOZhUnUngugiNa9Gil7R7lpYHgW3gd9qVeQNs2_zVbZPdlRGXdzmxVGANxUWZMdqQEzGpsov8go3YiVcoYk5ZvZ8JuKVUMQ2-1q5ZUvfyIMksrNRhwdSnFVS5kRJTVL0vh6uwo8_l_pDwTavFyBWZg-x0iIIyMsjT5l9M_IjrV1Z1DIE2HlQ-Mbud9E3aHsZg_zMK8OUA_b8o8V9SuXbWcduSbUwk_jJVaxV9jK5iMydL7UtkIHEAEmgonAfvp1B4lHkKmHj7GL1qLZ0ys_WMMaUMNslpnUiJMJa5EkfLozgAhh_os9qzoxIbklDnqv3iyRmR_yOZYqmcpBoCeaRuE6R5E2ozRF3AHrKnmmJeuyQBCT1n5b_Y6k7G1J2xz8HfeTb7HmTIJGZUuxwlKH6abYPclgfktoUoJBqBnHtqLWTZrquaG81nx8RzXZgguVizy2Y3YR_9y6Rys8cpZx2uSRczCOMG1rWjpNJaCAwvOxw4V7TCbo7C21ZB-rCazqVFsNZteQuM504pFmkEikpZdx6uHkCdvzsATuLK0u7Z0_K6Lla_WHQ5G_nkPzP_UnNvzMaDpWxPKU_rLL1itfOt__f9fk5t9JZgYVCwsTxjsc5QIV3NfQ6vqcAtE3JYOyMw49l07PmERh22h3sfDva2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/681829" target="_blank">📅 00:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681827">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ae3291b3.mp4?token=AA5nppeA3WFQAaX_q6A3KlxJ6bOASbjJI0n9mrzjkohlmmoWClpSzVTI07xMZABsSkZr94RRwhwLvDaewI5ndA-l4WQBUoHdYD0zwEjMZkJePlT8ou3hejEFCVi2JvFz2MuL6ldIPzTe66VNXWzeU3wTYXHFxeGKeQr01bZWlRbApqQnwfHxrl0OIDuktoltQg-f6V5q2u-7U7cherb40X4UYGNTYfGj9l0CnbdNkitida1xx7JSPl9N1QGrQEYpKF-eMndrmttQDfRi0QEWQcZfEl20Yjrx4lixWsCX1VMRDySQSSze7ZDWl-bOXFA12oMcPTjrYpSZw7SIykp3Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ae3291b3.mp4?token=AA5nppeA3WFQAaX_q6A3KlxJ6bOASbjJI0n9mrzjkohlmmoWClpSzVTI07xMZABsSkZr94RRwhwLvDaewI5ndA-l4WQBUoHdYD0zwEjMZkJePlT8ou3hejEFCVi2JvFz2MuL6ldIPzTe66VNXWzeU3wTYXHFxeGKeQr01bZWlRbApqQnwfHxrl0OIDuktoltQg-f6V5q2u-7U7cherb40X4UYGNTYfGj9l0CnbdNkitida1xx7JSPl9N1QGrQEYpKF-eMndrmttQDfRi0QEWQcZfEl20Yjrx4lixWsCX1VMRDySQSSze7ZDWl-bOXFA12oMcPTjrYpSZw7SIykp3Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش اردوغان به جنگ احتمالی ترکیه با اسرائیل
رئیس جمهور ترکیه:
🔹
ما در مورد جنگ صحبت نمی‌کنیم، ما در مورد صلح صحبت می‌کنیم.
🔹
اما اگر کسی قصد حمله به ترکیه را داشته باشد، ترکیه در آن جنگ تردید نخواهد کرد و از آن فرار نخواهد کرد.
🔹
من این را با وضوح و صراحت کامل می‌گویم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/681827" target="_blank">📅 00:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681826">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زندگی بدون سقف/ روایتی از زنان بی‌خانمان
🔹
زیرپوست شهر  زنانی زندگی می کنند که تنها سقفشان، آسمانِ شب است. این مستند، روایتی بی پرده از زنانی است که نه از روی انتخاب بلکه از جبرِ حوادث، خانه و امنیت خود را از دست داده‌اند و حالا در حاشیه  شهر، در نبرد با سرما و گرما و تنهایی به سر می‌برند. شاید تماشای این ویدیو، پنجره‌ای باشد به دنیایی که این روزها کمتر دیده می‌شود./ خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/681826" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681825">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a31969da.mp4?token=E0aPyRbqrhb4-_bTg1e_6F-Cg0cLJsGQo6hcsXP0XWZn5oP7pxbd1ajAKk73z13PhhW1WSTy27rGggHRx7tamWXD0vL8PjH13wFSS0ViNmHXaCQcY7unQWss4P9yp8tff9Ptfj9E_Fx22SBz3K_VIsNhUfqXELcAKZn_j8jnNq2WU9W_hhsTKNa_00lYzGXaUP3RCLS-BO6MI_UbQljCuRHMV9yMvFwoPge3tyLuEHstYetrsdk2Kqnwe2A3QLRzVyvg20GaXvT2-7yX-D9FxDcr5xGvOaf7F4l7iaaf-8wG4mU7yqsLayqshhkIwDmuZ1K-9dpEcbxpAE1ogp_hqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a31969da.mp4?token=E0aPyRbqrhb4-_bTg1e_6F-Cg0cLJsGQo6hcsXP0XWZn5oP7pxbd1ajAKk73z13PhhW1WSTy27rGggHRx7tamWXD0vL8PjH13wFSS0ViNmHXaCQcY7unQWss4P9yp8tff9Ptfj9E_Fx22SBz3K_VIsNhUfqXELcAKZn_j8jnNq2WU9W_hhsTKNa_00lYzGXaUP3RCLS-BO6MI_UbQljCuRHMV9yMvFwoPge3tyLuEHstYetrsdk2Kqnwe2A3QLRzVyvg20GaXvT2-7yX-D9FxDcr5xGvOaf7F4l7iaaf-8wG4mU7yqsLayqshhkIwDmuZ1K-9dpEcbxpAE1ogp_hqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راحت ترین و سریع ترین راه برای درست کردن دسر با قهوه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/681825" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681824">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای هیل: گزینه دیگر تسلیحات هسته‌ای ایران بمب‌های پلوتونیومی است
پایگاه خبری هیل مدعی شد:
🔹
ایران بیش از ۱۵ سال است که رآکتور بوشهر را اداره می‌کند. مانند همه رآکتورها، پلوتونیوم به عنوان محصول جانبی عملیات عادی، درون سوخت مصرف‌شده رآکتور به دام افتاده و انباشته شده است.
🔹
این پلوتونیوم هرگز قرار نبود در ایران باشد.  بیش از ۲۰ سال پیش، روس‌ها که رآکتور بوشهر را ساختند و سوخت آن را تأمین کردند قول دادند که سوخت مصرف‌شده را پس از خنک‌شدن و ایمن‌شدن برای حمل‌ونقل، خارج کنند. اما ایرانی‌ها این پیشنهاد را رد کردند.
🔹
اکنون، حدود ۲۱۰ تن سوخت مصرف‌شده حاوی بیش از ۲ تن پلوتونیوم در یک استخر نگهداری می‌شود. این مقدار برای ساخت بیش از ۲۰۰ سلاح نسل اول کافی است.
🔹
این پلوتونیوم یک مشکل بسیار پیچیده ایجاد می‌کند. نمی‌توان آن را بمباران کرد، زیرا این کار می‌تواند باران رادیواکتیوی با عواقبی در مقیاس قاره‌ای ایجاد کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/681824" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681823">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5DfIkl2wVTB0qyHNK5nK9r9F-Y9pcgQb5Kom5LYjAABCrQGJC_aFp0souN0EVlgzh3VwfHRdBj68mGjh7-c4viDU8A3C_jPWpeBVNVwo6gfp6aDrzFfV76qar9VDhZO3UNpaa1V6p3qjgVUglZ5KsmxeR5xgvQYdfh3ipVeZN3l_FwAy-5h-ypGXhZD3gdB3boPvNDA6vxtdTipohNguiXaFADsZh_yUZRY97rjlhv4gyicGSCqoStQyd6SYUcta6tAoyNJJTLiHe0sCEZI1TYR-heyxLJ4d5_G6iAy31XaBDPSc2K5b5oXLKI35BmnQp5ttLQm3DYxMXJVZNfbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت وزیر خزانه داری آمریکا از تحریم های آتی علیه ایران با هدف افزایش انزوای اقتصادی خبر داد
🔹
این اقدامات در کنار ادامه محاصره دریایی ایالات متحده در تنگه هرمز عمل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/681823" target="_blank">📅 00:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681820">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q07vmieI57J91-4xDGASCElFQQ-5cR-KWdtxFr_BFmE1KkKED5-qjaL6i3blP_MgKLB87QE3or6Oex-BT49DAg9TyqL2Pw9yge-jOiN7Dsf2aPdJeaEfIls3qBseR1kRYpZZgUQ45yg2wGaSEOFC6_LnEr7NUWk-Vrt_aZY-gxAYQe-XFcThh2sf1VhLocOG1jEy4wrwbvdsZuJyX8Q79ai-ECvmYnHbKlZHmIW33VoEE9x4b3Vxjm5sTvKSoPiQ_gaSDeYEGZuzu4exeTrsyouFcU8raHP8VEWHjKyRfGV_4CuXm6jAy7G1LTJV4VyM81UD_uJ_PQUOvlRm1whnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/681820" target="_blank">📅 00:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681817">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2201eaa6.mp4?token=uqMLO9wgWtymsDLz-1zBL5huzNdrlFYpBc-jC91q2xBfLXwArUw4O7SXt5LyhblTTeIz8ORahX1YwxzziVLnRkkj4JrQqoAJT5o-ls1QDaW4O8z0ZIJU7FyuMIrR_oP_t8TQ-IcpRxlzh0ZiQ4-c2CsCzFsHw2NM3Sn2HLVRI5BotU93UvnnmGDHvfaGqCC0x1iPOYqoFfb2qCT7kz3Zhe99-4tEcL7_JBbuo_4DVlhR3mHvc4O4RaCBKw3x3AOdWVPqCqW7AF0Dw7j0QOvNtGJaoFBbI5bsCUf_eYVgK7XhA98tjOIa22eFRYnMIO5QyOvEHQqlvkEg_LX9RjC5LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2201eaa6.mp4?token=uqMLO9wgWtymsDLz-1zBL5huzNdrlFYpBc-jC91q2xBfLXwArUw4O7SXt5LyhblTTeIz8ORahX1YwxzziVLnRkkj4JrQqoAJT5o-ls1QDaW4O8z0ZIJU7FyuMIrR_oP_t8TQ-IcpRxlzh0ZiQ4-c2CsCzFsHw2NM3Sn2HLVRI5BotU93UvnnmGDHvfaGqCC0x1iPOYqoFfb2qCT7kz3Zhe99-4tEcL7_JBbuo_4DVlhR3mHvc4O4RaCBKw3x3AOdWVPqCqW7AF0Dw7j0QOvNtGJaoFBbI5bsCUf_eYVgK7XhA98tjOIa22eFRYnMIO5QyOvEHQqlvkEg_LX9RjC5LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش کاربردی برای تمیز نگه داشتن لوله‌ سینک ظرفشویی، که با استفاده از یک بطری پلاستیکی انجام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/681817" target="_blank">📅 23:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fba1d673c.mp4?token=fTQ4utrf3JK_QR0rIGIPkn757oW7Dr_V5CtbabNz8ifuHUPdvNl1vkIBs9L5w7N3hk8A0500f33QpYHdEHNpMYSoLHCOUExlyMB49tZt7eKhqFhoTZC_oTOC2moWvIRdwQoQAMHJAe5V8uLo-a-fUCPt_pSbQICVrxbmD54QbtnveWQFR4PUGEgJuSGie-I63HGsjt9-WclcPjywzxNVWScFy5-4RitxFCfgcQvkO4jdaxlLa11LJsktihgTWa66Tv71u2NSKrY4G0XKEoYo7DF5RyraSR48rywyY3xYk38ParA0DVNI3uweYVcRORmmgFzvjkd7SYjCAsC9rZq4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fba1d673c.mp4?token=fTQ4utrf3JK_QR0rIGIPkn757oW7Dr_V5CtbabNz8ifuHUPdvNl1vkIBs9L5w7N3hk8A0500f33QpYHdEHNpMYSoLHCOUExlyMB49tZt7eKhqFhoTZC_oTOC2moWvIRdwQoQAMHJAe5V8uLo-a-fUCPt_pSbQICVrxbmD54QbtnveWQFR4PUGEgJuSGie-I63HGsjt9-WclcPjywzxNVWScFy5-4RitxFCfgcQvkO4jdaxlLa11LJsktihgTWa66Tv71u2NSKrY4G0XKEoYo7DF5RyraSR48rywyY3xYk38ParA0DVNI3uweYVcRORmmgFzvjkd7SYjCAsC9rZq4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین هواپیمای برقی جهان برای اولین بار به پرواز درآمد
🔹
شرکت سوئدی-آمریکایی Heart Aerospace با موفقیت هواپیمای نمایشی X۱، یک هواپیمای تمام برقی با طول بال ۳۲ متر و وزن برخاست بیش از ۱۱ تن را آزمایش کرد.
🔹
این پرواز در شهر نیویورک انجام شد، ۲۷ دقیقه طول کشید و به ارتفاع تقریبی ۳۳۵ متر رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/681816" target="_blank">📅 23:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: راهی که ترامپ می‌خواهد را خدا برا او بسته است
🔹
وقتی ملت ایران حق جهاد در راه خدا را ادا کرده، خدا هم راه سلطۀ کفار بر ملت ایران را می‌بندد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/681815" target="_blank">📅 23:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
ثانیه‌شمار کانال ۱۴ اسرائیل برای لغو تفاهم‌نامه تهران و واشنگتن
👇
khabarfoori.com/fa/tiny/news-3238221
🔹
تصاویر خلبانان ایرانی که در اسارت قطر هستند
👇
khabarfoori.com/fa/tiny/news-3238159
🔹
ترامپ دلیل کناره‌گیری سخنگوی کاخ‌سفید را اعلام کرد
👇
khabarfoori.com/fa/tiny/news-3238218
🔹
ماجرای خیانت همسر مهستی به او/ دوست صمیمی اش زندگی او را نابود کرد
👇
khabarfoori.com/fa/tiny/news-3238192
🔹
خواننده زن ایرانی در ۷۶ سالگی درگذشت
👇
khabarfoori.com/fa/tiny/news-3238031
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/681814" target="_blank">📅 23:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681808">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtqOk0yf_3yxhNT1VkiPFQj3kFDNSSsmsay4Co-HNsLH946kocmHh5x85ae_kGEfo8F5XHVuYpZfZUh8eMieWCWmUyr6xS0GZatTq30YCeD3fAB4RrfNyDEK8VJkE5QADGWMB33U3RtfiPvFIHbabO6rerB6PPGNMvmTpJZjSjX1Mvepfgb5vKS3WcE-y8ifurs3gpdnQVkrUxua4yxuo2XwQ-EOKHnOzs24sDruHh9Zs0iWuGq8SM1keyNWgF4Bpia2lyfF-6b7zQu-jjmjTYRfdp5pryb02hMIz3OUSxZZKf1unm-EOpPgKP8OYgLWTTzhN9fvjBOqfY6CtLCrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPaDjZ8mR8b1jSYupnW7mnSkUpB0Pgeos27lAc_dvrXTnOAAC9BC__Zc3iK3N__ZR_BpaVhyCEaWKryVhAAgAbopAmy0fQN-n2a47MPaceEkUoq5Tcst_lP-VZz4lLPA7HTNpf0gir31gQ4W5SDarJYZR-sa183MH1d2yFL4EvLASBQSuvgNsiLUmRTvATMvEzpdu7lOhXJALX406XRB8nDDZIaznlCEnbpSLkvW9-gVwzCjVRBc7giKkLligiX7rwcc2QlVxXTUxQgHlcgm_8RYzShazyuP2mZHL8V-oA4mSjzffEAUZLEtBoqOuj2YKW1pPUbn2KD_LWSg70Sdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfo47jPGcqTvkvA1uRnCnBEnQAOfPwn1lyfOXBL6Adr1Z97BsyNMUg_fbY5Hrw8olHno6kfNKsKIgeFebGO5QKPHum-O8buZgv0uf1p-tZhg_UrX2_JvtP0ehS3kpkk00w4WI79h3tRqPREx1ybkYuDF0NrcSqOfU_xwSCuvqfbWygY7tY1fdK_EuZBTeHFMzdK8bkzs1cdRdZ02LxHxvTMm3MKvOmt6jUuREyrp4N764-DTAq1kUFK2zchkzI4I91ao28xnMTaeDyt5P65s7JC9qgDpdTLjRA_4YnVu8AvU9Z2FUhaesbq7EtIABfWb1oJLvpZZKTmuFJKMXmvYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrQVOZogatYlQym5-Sc8KtFOi5asA-E6fFdOEcu7m8mr7ZLKBgbT3HCp0r4t9FlRlSe2pqkYrWSUOCy7O9tyq3s92jmmzoTZ-wL0f5jW-bra3smhm1sMlU2dY7DA1UOLdvkkJtwnu7iX0Wym5kmLy-TQHu5n_ruWzFantRH-Vnl-8KSoCNdO04VDZOJDpGt_teUZPSy2l2YYddMSDQ1AgqB8MV_HgPrRdM2wEUPLlq6CtxFGx_e9O-wcb8n9IxPG6vhBsitO5Dq2tUs9nCHkxxy5v1QnrSNgVB7flUnAcJYYvHAAgpZdKpW1e_iRjQS4DtXaoSG0Y52toNI02nB6sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYpkR_nhMeNxyDq5BAlRetF758M2X4G50qvrhsAQakx-5GG0SdZnA1MBiVUOGYArqh2p8ovKh4kJxtN7J0XlqPjYAddHUsCffHS4TPT2B4BZLMwVTgrZXmmLv0Lj13vIWIGIuVKmOlG2EEQQFOAS2Ya7S8MfkywFSzUJVIF6KEkoY1O82v_BLYvX-Avs8ZEGDIjDIEq-ntJSSnNKG6WLsmIDhEIEbC1k7KR-1V3Z7i219U4pycQZg7MyZDiEvwdOKhqGDZJFauEVPqOM3srHSSdHojgtlnvBQh2I8pjkHRA3c2sddCbDdnR5lc_XTZrQ9TOIrIoTJoh7Hk2Imps2-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عددهایی که ترامپ را می‌ترساند
🔹
جنگ ایران فقط میدان نبرد را تغییر نداده؛ قیمت نفت و بنزین را بالا برده و حمایت آمریکایی‌ها از ترامپ را هم به سرعت کاهش داده است.
🔹
اعدادی که در این اسلایدها می‌بینید برای ترامپ خطرناک است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/681808" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681807">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=C5VfAmXGngFiTTx34bQMopEnexowGzMWj4g8N9RjqAO36_PDj5mC0pg3BOb85KOHWZlr4kA3vSir96BgoCDeZXzHz1ujMwGlB2Ex9FRlBo6_uiK5qUsFR79FkOhjk1Lmkp5JcUv9qATSKA1qJGvpliyKUcEUGvnCp5JyA52Voz_aw9AEkBSGs1E1ISvphy7Jndy5PxjL8rgDeoaNtdCB7Np-2ynZ0hG7_Xoz51aOuHzLpMEMRIyUc2fhou70M7u4XdOcfuC6SspTimhikvHSVVYDg0bTWKnqidcbQVHP-xwiEjajG9xKPGpqfzeN3VDm-pGGbN1thER5eNdYkEpX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=C5VfAmXGngFiTTx34bQMopEnexowGzMWj4g8N9RjqAO36_PDj5mC0pg3BOb85KOHWZlr4kA3vSir96BgoCDeZXzHz1ujMwGlB2Ex9FRlBo6_uiK5qUsFR79FkOhjk1Lmkp5JcUv9qATSKA1qJGvpliyKUcEUGvnCp5JyA52Voz_aw9AEkBSGs1E1ISvphy7Jndy5PxjL8rgDeoaNtdCB7Np-2ynZ0hG7_Xoz51aOuHzLpMEMRIyUc2fhou70M7u4XdOcfuC6SspTimhikvHSVVYDg0bTWKnqidcbQVHP-xwiEjajG9xKPGpqfzeN3VDm-pGGbN1thER5eNdYkEpX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حضور یک شهروند ناشنوا در تجمعات شبانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/681807" target="_blank">📅 23:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681806">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4940f4d822.mp4?token=dW6rv9gNuMm2rc4LbvxSSdxqu-Ed5F02qLBa1lMDMZU6KoSmeM3huiAfFnz1BnIeQq2p3FbzX6l_p0-fxT_ho7uId6XMiytmBi4vBLQcP20NEB3qwE7C5Efya1OxdWyS9D11n8vg2x7bbD9BDT54qecpc4hQ_8yqYr5ARNNdohNotaWs6vf7ZWXJ0-Bu4EPdaTjlmTAbB2Tity70Puhqxujuv9vhS20LjDR5Ta4QKg8YaHtKGXoXMOE8Snh-W4apLJ0fE4Kt5u7xaaUSsNcxEHny274Uo72E1eXjnCxBNxkkghbQMI7-9azbnwxivgDUWA0a5KcG7cgh7DBhUdkQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4940f4d822.mp4?token=dW6rv9gNuMm2rc4LbvxSSdxqu-Ed5F02qLBa1lMDMZU6KoSmeM3huiAfFnz1BnIeQq2p3FbzX6l_p0-fxT_ho7uId6XMiytmBi4vBLQcP20NEB3qwE7C5Efya1OxdWyS9D11n8vg2x7bbD9BDT54qecpc4hQ_8yqYr5ARNNdohNotaWs6vf7ZWXJ0-Bu4EPdaTjlmTAbB2Tity70Puhqxujuv9vhS20LjDR5Ta4QKg8YaHtKGXoXMOE8Snh-W4apLJ0fE4Kt5u7xaaUSsNcxEHny274Uo72E1eXjnCxBNxkkghbQMI7-9azbnwxivgDUWA0a5KcG7cgh7DBhUdkQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هند نخستین پهپاد تهاجمی بومی خود را با موفقیت آزمایش کرد
🔹
منابع خبری گزارش دادند که شرکت فناوری پهپاد هندی «کاوا یوایوی» اولین پهپاد تهاجمی خود به نام «دیویاسترا ام‌کی۳» را با موفقیت آزمایش کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/681806" target="_blank">📅 23:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681804">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
امروز مردم ۳ هزار میلیاردتومان پول به بورس تزریق کردند
🔹
در جریان معاملات امروز، حقیقی‌ها بیش از ۳ هزار میلیارد تومان پول تازه به بازار سهام تزریق کردند و ارزش معاملات خرد به حدود ۳۹ همت رسید.
🔹
هم‌زمان، صندوق‌های درآمد ثابت با تراز نقدینگی منفی ۱.۸ همتی مواجه شدند و صندوق‌های طلا نیز ۲۳۴ میلیارد تومان ورود پول ثبت کردند؛ نشانه‌ای از افزایش تقاضا برای دارایی‌های ریسکی و طلا. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/681804" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681803">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae83786da.mp4?token=v1CJN6cUrY4Wab5_ZZJnYyNT9jfhrUOkMeX8PbrN5gt5rrMICaM3vQ963Oy-7hUOS0BdPcUQsgk8jfKKPH7VPposGst-R_K9HLeWBbG_cuDrd6ZG29w3zesyQG_FxCO8IC61sYhYE2j0-uefTGYbvmM7RuzK5nZCXB0WcZfu7NISltes6VVSvCEc58R6JnivommjgjSffgQGwvzIeXnFE34sBXEh0sFWfHQMIaHeS1z4ZHeZbz3ZP5eif_Wa0Gd2gow5ifwf2Gpso3GXUn_-a4vATXy2pz0i3YY_Sa8bjDLJxWK6jPbICizMq_GZIMfHKIQQkPxqpHVaG7UyB-mp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae83786da.mp4?token=v1CJN6cUrY4Wab5_ZZJnYyNT9jfhrUOkMeX8PbrN5gt5rrMICaM3vQ963Oy-7hUOS0BdPcUQsgk8jfKKPH7VPposGst-R_K9HLeWBbG_cuDrd6ZG29w3zesyQG_FxCO8IC61sYhYE2j0-uefTGYbvmM7RuzK5nZCXB0WcZfu7NISltes6VVSvCEc58R6JnivommjgjSffgQGwvzIeXnFE34sBXEh0sFWfHQMIaHeS1z4ZHeZbz3ZP5eif_Wa0Gd2gow5ifwf2Gpso3GXUn_-a4vATXy2pz0i3YY_Sa8bjDLJxWK6jPbICizMq_GZIMfHKIQQkPxqpHVaG7UyB-mp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: راهی که ترامپ می‌خواهد را خدا برا او بسته است
🔹
وقتی ملت ایران حق جهاد در راه خدا را ادا کرده، خدا هم راه سلطۀ کفار بر ملت ایران را می‌بندد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/681803" target="_blank">📅 23:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681801">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=RqeqNp1Mw7bvUZ3mDvZwkoiFSjSTOPNc89dIvCV38XJrPrtenS_6ftbyh8KtKFUoMmGBcO9HMWosqFe7MJxmpOXuXCjhoxzKA2bmP2tgS6T3QdItFGRcRNIj2HG1MyNxwOlKR2kWhkvnKoMnxE5RxNLtHbp2_bQPx6EfSAnYracL4weNrVu9d4G7LEHvdog-Xlyr5Eig0ZjHPn9p_KN24n7Uj-A3O5UNJmXq6OW-wkTb6kMHVnOD2rpBYzLbNclcTmuGqhy0hvYBNM_4jzD6f8fFuUHRkM4j8RgS4VK3vYrX0uYHn9WR6F2DK82z4pOxL2MEXlT6B3ykgXUmuI59Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=RqeqNp1Mw7bvUZ3mDvZwkoiFSjSTOPNc89dIvCV38XJrPrtenS_6ftbyh8KtKFUoMmGBcO9HMWosqFe7MJxmpOXuXCjhoxzKA2bmP2tgS6T3QdItFGRcRNIj2HG1MyNxwOlKR2kWhkvnKoMnxE5RxNLtHbp2_bQPx6EfSAnYracL4weNrVu9d4G7LEHvdog-Xlyr5Eig0ZjHPn9p_KN24n7Uj-A3O5UNJmXq6OW-wkTb6kMHVnOD2rpBYzLbNclcTmuGqhy0hvYBNM_4jzD6f8fFuUHRkM4j8RgS4VK3vYrX0uYHn9WR6F2DK82z4pOxL2MEXlT6B3ykgXUmuI59Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جوانی که با دست‌سازه‌هایش یاد شهدای کودک و نوجوان جنگ را زنده نگه‌ می‌دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/681801" target="_blank">📅 23:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee142e9f9.mp4?token=kM-gmF-iZ6kK8THI2VcqfjwXqp-J0-G3vqCs5_7Gy33YVwN7Q6u-fyql5w29gtk8SwDR2pENsPb3rwGUDDlWh9Erg6cIfMf-tatas4UCehxp3NswTzCMhDPiLk6pHvw8SnLyFU-1bA3ksZArWnbMwvW5zFHj62RU7xBX3dIj6HJJWrJZHiY_ntkpFhKuLnNdNT67luV4f7r-v-NKshai76OpK9xLFjTsWA9oynqsO-DvQSgcbMjSFl73IPU0notTz246FjSfW5tX9vGewioExwVm102hJUw_-2fUnd6RwkHUkaxcr0Yu1SJeAYkhGiPOOy_hBm1OYGV4szRly71DLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee142e9f9.mp4?token=kM-gmF-iZ6kK8THI2VcqfjwXqp-J0-G3vqCs5_7Gy33YVwN7Q6u-fyql5w29gtk8SwDR2pENsPb3rwGUDDlWh9Erg6cIfMf-tatas4UCehxp3NswTzCMhDPiLk6pHvw8SnLyFU-1bA3ksZArWnbMwvW5zFHj62RU7xBX3dIj6HJJWrJZHiY_ntkpFhKuLnNdNT67luV4f7r-v-NKshai76OpK9xLFjTsWA9oynqsO-DvQSgcbMjSFl73IPU0notTz246FjSfW5tX9vGewioExwVm102hJUw_-2fUnd6RwkHUkaxcr0Yu1SJeAYkhGiPOOy_hBm1OYGV4szRly71DLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم  رئیس مجلس:
🔹
ملت ما در یک جنگ ناجوانمردانه، مقابل دشمن آمریکایی و صهیونیستی شجاعانه ایستاد.
🔹
به‌عنوان یک خدمتگزار که به جزئیات آشنا هستم، با همه وجود می‌گویم ما در این جنگ، در بُعد نظامی و بُعد سیاسی، به معنای…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/681799" target="_blank">📅 23:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
پزشکیان: این که سخنرانی کنید، بنشینید پشت تریبون فقط حرف بزنید و فکر کنید به این راحتی است، نیست، اگر راحت بود حل شده بود
🔹
ما به دنبال آدم‌هایی هستیم که باور و علم داشته باشند و بخواهند علم‌شان را در خدمت مردم قرار دهند؛ دعوا هم نکنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/681795" target="_blank">📅 23:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681792">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSnQ_tzOHNjl3E5PQNcVAANVaNAYaBe_VjvA1nRXOdyiHUki3fWPNrf2To7FRiJvnyuBgnnhkm5gUJdIEd-w4mg6VDDxlNomkKrTbN6STmlnvzIKQf9w_wV2XC4bvQaUPNiVrW9yNPTEwbLbatuvskmQfXtdLAiXPchM7-1rLQKq6z1Gx-LVTzez6LpaY2rNyQpgqnpyHjC5yaAe6KS5vZ70ItOm73_5BRHyg9JLxD7tD-1pAO8B5hH-TSL7qM3gIiaRd5-W5mgtOFPqGdR-zscWLLY5NZXDhDmnwtSEBUtkXwUH4w9yTUyW0PngkK1LvR0VYLqy94cb3Z3RXW9vxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«هم‌پی» راهکار پیشتازانه بانک اقتصادنوین برای آنکه چرخ تولید متوقف نشود!
🔹
بانک اقتصاد نوین همزمان با بیست‌وپنجمین سال فعالیت خود، طرح «هم‌پی» را برای پاسخ به مهم‌ترین نیازهای مالی تولیدکنندگان و فعالان اقتصادی ارائه کرده است؛ از تأمین حقوق و مواد اولیه تا فروش اعتباری و تأمین تجهیزات نیروگاه‌های خورشیدی
🔹
«هم‌پی» تلاشی است برای عبور از چالش نقدینگی و کمک به تداوم فعالیت و رشد کسب‌وکارها.
برای اطلاعات بیشتر:
https://enbank.ir/s/mfa9aC
☎️
02162740</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/681792" target="_blank">📅 22:56 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
