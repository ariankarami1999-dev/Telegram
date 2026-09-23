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
<img src="https://cdn4.telesco.pe/file/KVJmVVMvGxE_cIvCwsou34InN-tKimzrVg4jeze_6Z3DB2NGfPLzHAPoSlndf3vfKL6zIXWCHfIPh3QFeeI_yyGC6N3jB0_gh1rVdnS3EmufVZ4K2cVCK4CSJR5mUtLGZe_Uw4rT4KqkX8WJrEr5Ol7s5drh4jAh_odA9jJnekMGlNae0q9N4euogr3yTkAlg2Q7R6ZCC5pnYjhLLHjD26WnDKwUs0jirs_l0PpWrRxCaD1imNcDsfnHcqeSbhJLjdz629xi1hgDgx7mFBzq9uxcadwrIEJnDp_m8C-3q22Td0X7lj74pwAtH-GndMkyhgcDkMwJu8UbGyJYRZpmKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 22:38:16</div>
<hr>

<div class="tg-post" id="msg-72145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=uKTPb8sLwm2wzLev0EklKdPjcN2EaUqRfsHNLspVpVeR1JTmwa2Axw7X0rIHGxkbVbLLOW6NAkvFQUpCt9bsPkeyI0aZmkynEz1N9tNgD2LRVWYnMJXOJplo_rf0eTl7jWDPSXAMrMDpi-CUPH0rfD1DvGEphh9iVDJIGet7w5NofgWKvW7BcrGNqRSRicr29CKFieK914nz-P1riMHaUhtuqMi6O_b_Zs7XkZUi1eatC6J6v5Ezph2L-NXOn-Em3lqjCHfV9WWvS0ts4evC7qwpprDq-bFwm89cmUKNiXDypkTrs3rUzIBRQbh9UoG3YhXrDt3EuD1V52zcYa2vZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=uKTPb8sLwm2wzLev0EklKdPjcN2EaUqRfsHNLspVpVeR1JTmwa2Axw7X0rIHGxkbVbLLOW6NAkvFQUpCt9bsPkeyI0aZmkynEz1N9tNgD2LRVWYnMJXOJplo_rf0eTl7jWDPSXAMrMDpi-CUPH0rfD1DvGEphh9iVDJIGet7w5NofgWKvW7BcrGNqRSRicr29CKFieK914nz-P1riMHaUhtuqMi6O_b_Zs7XkZUi1eatC6J6v5Ezph2L-NXOn-Em3lqjCHfV9WWvS0ts4evC7qwpprDq-bFwm89cmUKNiXDypkTrs3rUzIBRQbh9UoG3YhXrDt3EuD1V52zcYa2vZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواننده رپ آرمین رابر، برگزار کننده میتینگ های خیابانی رپ در اطراف تهران بازداشت شده است. او پیش تر نیز به دلیل اجرای قطعه آقازاده بازداشت و به حبس و جریمه نقدی محکوم شده بود...
@News_Hut</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/news_hut/72145" target="_blank">📅 22:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تسنیم گرفت رو عراقچی:
تعامل عباس عراقچی، وزیر امور خارجه، با استیو ویتکاف، نماینده آمریکا، بدون مجوز یا هماهنگی با مقامات ذی‌ربط ایرانی، از جمله شورای عالی امنیت ملی، صورت گرفته است.
ادعاهایی مبنی بر اینکه این تعامل از پیش به تأیید نهادهای سیاست‌گذار ایران رسیده بوده، نادرست است.
بر این اساس ضروری است که آقای عراقچی درباره این اقدام غلط که مخالف مصالح و‌ منافع ملی است به نهادهای مربوط و ملت ایران پاسخگو باشد که با چه محاسبه‌ای این خطای بزرگ را مرتکب شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/72144" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=hoMFc582Lc5UqUg6oy_zrPi9gEuh4XyynJUeK1zS62dceXX15n60-3FDA2DMpha-An5aTCCuD8NUOoWq8vrYHsnQkesAXCGP3_tWZxlMYgADy-DlcdzQhSQlFzncj-xnr-td7LBjZa0Mahl4dKKZ6G3ArlmwlkKVYQiCWXPCfy3qw6n9GLLe_dY-0u3ItZJVwgO-6aA8d8m98vxesBR7J55kudxX4It11oAotpNnbwKCZk0SNKbuRhYfG-CcR1HuRGXuDkisNy-TcLMCSfA0gw3r1Hee6p82zWbafXN_27gHEXvZo3jETKeTGd4TaWsdCT76foKEByTR4fqHmbJ5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=hoMFc582Lc5UqUg6oy_zrPi9gEuh4XyynJUeK1zS62dceXX15n60-3FDA2DMpha-An5aTCCuD8NUOoWq8vrYHsnQkesAXCGP3_tWZxlMYgADy-DlcdzQhSQlFzncj-xnr-td7LBjZa0Mahl4dKKZ6G3ArlmwlkKVYQiCWXPCfy3qw6n9GLLe_dY-0u3ItZJVwgO-6aA8d8m98vxesBR7J55kudxX4It11oAotpNnbwKCZk0SNKbuRhYfG-CcR1HuRGXuDkisNy-TcLMCSfA0gw3r1Hee6p82zWbafXN_27gHEXvZo3jETKeTGd4TaWsdCT76foKEByTR4fqHmbJ5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون ۶ مورد دیگر از فایل هایی که در آن اشیا پرنده و ناشناس به اصطلاح UFO دیده میشه رو منتشر کرد که دو مورد اولی در خاورمیانه ثبت شده هست.
@News_Hut</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/news_hut/72143" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=LYffGtNxJCH9xFu8xlhBENBVsEKLRy4JOf7L6qLcibbhaeZyzzf-qFC3zq3chfYEMtRkiwDSragm7J-I4TKVo8eiIULgoWv-Pd2cPWH37tlr05Kl1gPhyyY22Kp6w8NUyDmsImGyFEIE9O_BCatPejRtV7jZchOgVhDoR2FQTuDbl87WeZUkgLEGiXWJSJhD36RiZ1Rr3Ttw-JIFZGXrfzEg047NXljArdtX5C40BDuUE5H87glYQVml9SZjgxouddTt4G_sOU0iIGs9-0vXYDc7n1J2nvD0-AZvK1swDsHRUHqN0XO_MfmfYdBrsVsGKzf6nSoYVps1XsXFyqtuNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=LYffGtNxJCH9xFu8xlhBENBVsEKLRy4JOf7L6qLcibbhaeZyzzf-qFC3zq3chfYEMtRkiwDSragm7J-I4TKVo8eiIULgoWv-Pd2cPWH37tlr05Kl1gPhyyY22Kp6w8NUyDmsImGyFEIE9O_BCatPejRtV7jZchOgVhDoR2FQTuDbl87WeZUkgLEGiXWJSJhD36RiZ1Rr3Ttw-JIFZGXrfzEg047NXljArdtX5C40BDuUE5H87glYQVml9SZjgxouddTt4G_sOU0iIGs9-0vXYDc7n1J2nvD0-AZvK1swDsHRUHqN0XO_MfmfYdBrsVsGKzf6nSoYVps1XsXFyqtuNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هموطن‌ها رفته یه مرسدس بنز خریده؛
همه منتظر بودن از خریدش ذوق کنه ولی صحبت‌هایی که بعدش کرد، جالب بود :
@News_Hut</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/72142" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/news_hut/72141" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYLbhtuH7M8iwb5CHV9-E0RlWzy-Qld76KPv-mg6YXuEaDx7RGNvIdyv620zwV11a0mxmCPOLKxxXgd44AGmeT0k1o2vaj03i9-gUmG7QZcKrn7Z9Q_5CB4-6M_x4ApKD2yNIWt-W4_UMIEtZMXrI0Suc_Q8528uzGpEU-H7jdvuW4BdiILUaek0i6RYTaQsNh-bMybNbj8wihkg7bmpuPVmVMZTOI9N6uFxAX3x5Af4qoU1RSLLBtjzgZYLMQWpQTTJScZP0uNOE1PS98Jdb_3HDEFJWQNxwY6lmvQJi4Cl2a9TqJyFAdcdx3AkeGUq3fWpiIY-1EgcEraABX4n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/news_hut/72140" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=H0rRRxVG5ndWb_ZYG0UlmxOpcQBUd_BnsD9WupEtx1E2BsDyo0KiyWYpdvtoWs7tRKDbVyrnTyCzjo1tTVxN4aMo5zedgBJPqO3uAB__8CTzM80iuzGbkho6PB0DYdU_Fcp1uhhTMjEvApXxdj5-D54MFyqo9n8AxeaOfOFuBXsi7k_-wztLMcTl-_X0oyagIULvuT1uEVUHqtnshvbAQiYltSeUwi1J0l6pYMsaQj0WYApXGQjhOXwtuloXjj9ID4q_fUf0G7ZHrXluZ8YnVpWTusWImHPEaeQoIICYGrhr6zKhm-2rTFyHmI8MqwuhqZbfe2C3t6fw5oWbQoS2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=H0rRRxVG5ndWb_ZYG0UlmxOpcQBUd_BnsD9WupEtx1E2BsDyo0KiyWYpdvtoWs7tRKDbVyrnTyCzjo1tTVxN4aMo5zedgBJPqO3uAB__8CTzM80iuzGbkho6PB0DYdU_Fcp1uhhTMjEvApXxdj5-D54MFyqo9n8AxeaOfOFuBXsi7k_-wztLMcTl-_X0oyagIULvuT1uEVUHqtnshvbAQiYltSeUwi1J0l6pYMsaQj0WYApXGQjhOXwtuloXjj9ID4q_fUf0G7ZHrXluZ8YnVpWTusWImHPEaeQoIICYGrhr6zKhm-2rTFyHmI8MqwuhqZbfe2C3t6fw5oWbQoS2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/news_hut/72139" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پزشکیان:
تو منطقه هیچ کشوری به تنهایی امنیت نخواهد داشت، یا باهم امنیت رو می‌سازیم یا باهم تو ناامنی زندگی می‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/72138" target="_blank">📅 20:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15be798879.mp4?token=MkL48lL5k60hV9Q12H6IpKA2606Jp8VDyA0Sik5FOr4gBB_BUODqL55Ib0hgJLmYUktXF4I6l3LRAgx1qbDZBIqMMrYZWD5stAulh06D8HK_C5v88aFCcdx37IbdTXiGR_mMzIYaqMQw2BqR1pDOvuU1IYsEobxZ3pNndv3A6fJ79oH9zoIIvf1Rsq_0UdNwKB9sg4Y5FKMcHNfsEkwos-RHcmhE56PCADyc-7Gp9-_0vaFu1N0Px1qUEnARGv6PkZjO9zguwVn-BSQe7AHZjwRS9mDU96zKTziFm52um2lbzVNNvTLl2Z2QCJwGu4xS6mOS-Whc4tFZt2T6iJNRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15be798879.mp4?token=MkL48lL5k60hV9Q12H6IpKA2606Jp8VDyA0Sik5FOr4gBB_BUODqL55Ib0hgJLmYUktXF4I6l3LRAgx1qbDZBIqMMrYZWD5stAulh06D8HK_C5v88aFCcdx37IbdTXiGR_mMzIYaqMQw2BqR1pDOvuU1IYsEobxZ3pNndv3A6fJ79oH9zoIIvf1Rsq_0UdNwKB9sg4Y5FKMcHNfsEkwos-RHcmhE56PCADyc-7Gp9-_0vaFu1N0Px1qUEnARGv6PkZjO9zguwVn-BSQe7AHZjwRS9mDU96zKTziFm52um2lbzVNNvTLl2Z2QCJwGu4xS6mOS-Whc4tFZt2T6iJNRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم معلم قبل از شروع مدارس، برگشته به اولیای دانش‌آموزا میگه؛
بعضی از دانش‌آموزا هستن که پدر، مادر یا هر دو رو ندارن ؛
پس وقتی میاید بچه‌تون رو از مدرسه بردارید انقد قربون صدقه‌ش نرید که دل اون بچه یتیم بشکنه، برید یه جای خلوت‌تر بهش ابراز محبت کنید
@News_Hut</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/news_hut/72137" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72136">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=laK-Dz9J7sg8MCR6jEgClvPX0cIgJiEQlP5R5udyNux2Lwwk5K09jneX0VkM3FbV2PFHkg1k-gWLn5qHvKEtbFSS3Xt0LOMqjbuUEWcfrDUFYNPUEhJcPxFwnIkHiEhR3pl_ouC8Sn5lPUlBJISwSL6bBkGBgTghIn5eK6rqvzcw3MefAOIykF6HC-w57akx3f3HkJXfv6b4lus_L340UaUrMPGOQUjPLL00-fhG_uheG8mHRXNwPLPwr_zPR9CSxrs7Bj3CUwxHu-lrNOQWhmQbP5SNwEPQSWIduyo-4n8aOcWvY-LLiJl1qkjpYnntMYrkWCNekbmk_t48GV0Q4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=laK-Dz9J7sg8MCR6jEgClvPX0cIgJiEQlP5R5udyNux2Lwwk5K09jneX0VkM3FbV2PFHkg1k-gWLn5qHvKEtbFSS3Xt0LOMqjbuUEWcfrDUFYNPUEhJcPxFwnIkHiEhR3pl_ouC8Sn5lPUlBJISwSL6bBkGBgTghIn5eK6rqvzcw3MefAOIykF6HC-w57akx3f3HkJXfv6b4lus_L340UaUrMPGOQUjPLL00-fhG_uheG8mHRXNwPLPwr_zPR9CSxrs7Bj3CUwxHu-lrNOQWhmQbP5SNwEPQSWIduyo-4n8aOcWvY-LLiJl1qkjpYnntMYrkWCNekbmk_t48GV0Q4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه با شوهرش رفته بود خرید که شوهرش این حرکتو زد و آبرو برای زنش نذاشت :))
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72136" target="_blank">📅 19:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72135">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
آقای ترامپ و کسانی که به دنبال زورگویی به ما هستند، باید ایران را بشناسند:
اینکه ما آماده گفتگو، دیپلماسی و مذاکره هستیم، اما زبان زور را نمی‌پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72135" target="_blank">📅 18:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=r4whk5DPI0lGQexs0KJI2CCD-peSfJs9XsHjjDNtVpl3tcjC8B4qnhMOfg4Kh8j212KC3F1SMbVTkloz2Il8gy8Uk8KRnxJl5BcKYxdlcVnj1rj9dBr0pXcVupYn24lEF5cfqeRjhf9HGnrz6nSKS1u9lrJfsLZ_mZzTraKM67m_jl403Tq4Gsex7p_XHSHHxEFZ9DXSSseI-q_jSEBuL-eZIln_pnTuEsho2_IpkYcELnAGJt_53CGwdHWNLkmVTz3kSPGDJ82XY2goEz7uS9wyValMj6DFzABVPlcmYW9wgFevxfYmDdPrw-VJeoCbnEuL2QhOv9Mxmuvr8QN7zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=r4whk5DPI0lGQexs0KJI2CCD-peSfJs9XsHjjDNtVpl3tcjC8B4qnhMOfg4Kh8j212KC3F1SMbVTkloz2Il8gy8Uk8KRnxJl5BcKYxdlcVnj1rj9dBr0pXcVupYn24lEF5cfqeRjhf9HGnrz6nSKS1u9lrJfsLZ_mZzTraKM67m_jl403Tq4Gsex7p_XHSHHxEFZ9DXSSseI-q_jSEBuL-eZIln_pnTuEsho2_IpkYcELnAGJt_53CGwdHWNLkmVTz3kSPGDJ82XY2goEz7uS9wyValMj6DFzABVPlcmYW9wgFevxfYmDdPrw-VJeoCbnEuL2QhOv9Mxmuvr8QN7zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ باید بداند که مقاومت ملت ایران در برابر تحریم‌ها، افزایش فشارها و زورگویی‌ها، تنها بیشتر خواهد شد.
ما هرگز سر فرود نخواهیم آورد و زانو نخواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72134" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مسعود پزشکیان:
بمب‌های اتمی و هسته‌ای در اختیار رژیم اسرائیل است، اما از بازرسان خواسته می‌شود که به ایران بیایند.
اسرائیل بیش از ۷۰ هزار انسان بی‌گناه را در غزه به شکلی وحشیانه به قتل رسانده است، اما ایران در حالی که پای میز مذاکره بود، هدف بمباران قرار گرفت.
اسرائیل بمب و سلاح‌های کشتار جمعی در اختیار دارد، عضو «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) نیست و در طول حیات ننگین خود حتی اجازه یک مورد بازرسی را هم نداده است؛ با این حال، همه امکانات لازم در اختیارش قرار می‌گیرد تا بتواند هر پایتختی در منطقه را که بخواهد، بمباران کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72133" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DlGruuGYxRtTgFdV4-1mGciYUNEPGpN15P_UOEzL3gL3DTstlwUCspyPlRF_X2_YYNdc4F-Ty_-N4sMYReWhrQOkEBAsKgfwKnrQKbRXPB0gksWe6976I12N27G41-rJDa_vSrgZ5gtywlNXkMeFkET9R479jOtGa09JOkotMRIWO6hEpJNBg5o-3oDSA5m2BVpyB51RqMZPxnYLzv8x9Pd0ntF71wS9yBpIBQ_taOy1ULxVg9Yu78YCUcLj9sliSH8927JJSG9616QyocHK8AeQRt6WLX6MbKoaTd34QwIgiIzK39AltMQaoJcC7pNA3oLfRODbJPmVQJfZv2inbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DlGruuGYxRtTgFdV4-1mGciYUNEPGpN15P_UOEzL3gL3DTstlwUCspyPlRF_X2_YYNdc4F-Ty_-N4sMYReWhrQOkEBAsKgfwKnrQKbRXPB0gksWe6976I12N27G41-rJDa_vSrgZ5gtywlNXkMeFkET9R479jOtGa09JOkotMRIWO6hEpJNBg5o-3oDSA5m2BVpyB51RqMZPxnYLzv8x9Pd0ntF71wS9yBpIBQ_taOy1ULxVg9Yu78YCUcLj9sliSH8927JJSG9616QyocHK8AeQRt6WLX6MbKoaTd34QwIgiIzK39AltMQaoJcC7pNA3oLfRODbJPmVQJfZv2inbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مسائل منطقه‌ای ما باید در درون منطقه و به دست کشورهای منطقه حل‌وفصل شود، بدون آنکه به ابزاری در دست متجاوزان خارجی بدل گردد.
هیچ‌گونه رابطه‌ای با یک قدرت خارجی نباید به ابزاری برای تهدید کشورهای همسایه در منطقه تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72132" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72131">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=DOa2DSnRBVx4zawXnqgEe7nKA77RMcc-Tk-PusN30X-86G8nsq8ObowD-IreeretwjttzTnMyG5iTobYW2qlVRkdOpo7Uoq1uAaDo0nOOC5CZP4vrsTiVNd-GDXWo-zaNl1xc18gr9ZpagKoYW9IDztLJaAvOLxtv3Lph6D90VBdOL2wHbB9awUBOjzV8lHYSr-32VnioOlx4mA7nIP1ZtP2GoP2UyK7Rn88quQ8BR6S17kH_DEr1qA9xUPmQYc7tb1zl9Zpgy81bJcUN8KDwZ0VoBUp3bZ3H1xXIUi3pQS87VacuDRWhab2xYOtjaLBphQzSmAnzisidepqDMadAgmVYGoC9d8wC3JbR10-NNtdZ9MCagNM-FYoLajM_qq2sAqWtTkKCw5NmpurM86IvA2oMJBSyJyryRXeiInFUIZBH4xX43BHa1Zr8cwXyzzw0I8nUz95LGZHOXSHwh5HxOWzQJRVOYI9MBbT7y67eOO4zGiYlmesDtQ9cA10eg0AceptRoSKGHzJj8tq8y1IfWmxpmZXK5r6iIBIwjyeXW_7bYKeuPeWcvxbx1hv1-s-HMjqgkxgs8zGeRfnN0gtAoxBdklaxpGAts73FFkki1Wq-Ntdc9f3E1YkIE9WWsOpiT4pb1rYUXXhGAO1RJMrVL4m7Xi1Il2aS-WaV7qm3lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=DOa2DSnRBVx4zawXnqgEe7nKA77RMcc-Tk-PusN30X-86G8nsq8ObowD-IreeretwjttzTnMyG5iTobYW2qlVRkdOpo7Uoq1uAaDo0nOOC5CZP4vrsTiVNd-GDXWo-zaNl1xc18gr9ZpagKoYW9IDztLJaAvOLxtv3Lph6D90VBdOL2wHbB9awUBOjzV8lHYSr-32VnioOlx4mA7nIP1ZtP2GoP2UyK7Rn88quQ8BR6S17kH_DEr1qA9xUPmQYc7tb1zl9Zpgy81bJcUN8KDwZ0VoBUp3bZ3H1xXIUi3pQS87VacuDRWhab2xYOtjaLBphQzSmAnzisidepqDMadAgmVYGoC9d8wC3JbR10-NNtdZ9MCagNM-FYoLajM_qq2sAqWtTkKCw5NmpurM86IvA2oMJBSyJyryRXeiInFUIZBH4xX43BHa1Zr8cwXyzzw0I8nUz95LGZHOXSHwh5HxOWzQJRVOYI9MBbT7y67eOO4zGiYlmesDtQ9cA10eg0AceptRoSKGHzJj8tq8y1IfWmxpmZXK5r6iIBIwjyeXW_7bYKeuPeWcvxbx1hv1-s-HMjqgkxgs8zGeRfnN0gtAoxBdklaxpGAts73FFkki1Wq-Ntdc9f3E1YkIE9WWsOpiT4pb1rYUXXhGAO1RJMrVL4m7Xi1Il2aS-WaV7qm3lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما سر خم نخواهیم کرد و از حقی که ذاتاً متعلق به ماست، دست نخواهیم کشید.
صریح می‌گوییم: نه سلاح هسته‌ای و نه هیچ‌گونه محدودیتی برای فناوری صلح‌آمیز هسته‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72131" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72130">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2213909800.mp4?token=bD6yq27gDQ8OM3UDuud_314V2IsyzJOArxAAwXzs_3OX9dOUdUw98dRaSrCYWC62mPdiLC6-5kM6vJewGFszARJc2zUp-sD1UYWfNyq-4UwYNIIwb25SCySZ5MigiOP86nJhT5tzzrTJwBC968RNCL41HlpkDL41fP4s8E114cHFPOJCzjwIMWNeyh-DHWnXxvxgNr7FQxYYwrZaCjkWUGU_8dosb8r7_xBCqCyhMLy-BTCY0VnZDq-NG8AKXVyrXb9gJ_cSGBoqMA7Mf9KWgwPF0f4mWHto_GQ5lxgfhIeGT9fgyq293ihEWIW1tGZyuHclro3W9ZHMifjeBM8hYlh3woes6oNZdas-avMwy1TxZE2kAIbAujL6rQmDV4FMg3G7uvgFzFfr9GEWjxkSo_Gwbb_TyZAlffKYt8JsuMjOzefprZbCBVJ6_nEVkv8UZujKCHcOKHi59dG2lGhxjb8tySodIH6y663YH6Jol-m4q33BMlXMgqXqLsgdIglh4T0IHfnukEl7KBkUx4XklaJPL6UzW_tOGzTEo-ilJ0zusgOdql49J5H8SBWHCvtG_nIBrrR_j8UWSsG5kyd2rw-KrGPxrena4w5BUr-expHBHPpeuaH4tsbSifHTqGHAFtzmaVJZsTgPGu-MVZLEdVwt-uA_OnBy_Uy67QeLDQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2213909800.mp4?token=bD6yq27gDQ8OM3UDuud_314V2IsyzJOArxAAwXzs_3OX9dOUdUw98dRaSrCYWC62mPdiLC6-5kM6vJewGFszARJc2zUp-sD1UYWfNyq-4UwYNIIwb25SCySZ5MigiOP86nJhT5tzzrTJwBC968RNCL41HlpkDL41fP4s8E114cHFPOJCzjwIMWNeyh-DHWnXxvxgNr7FQxYYwrZaCjkWUGU_8dosb8r7_xBCqCyhMLy-BTCY0VnZDq-NG8AKXVyrXb9gJ_cSGBoqMA7Mf9KWgwPF0f4mWHto_GQ5lxgfhIeGT9fgyq293ihEWIW1tGZyuHclro3W9ZHMifjeBM8hYlh3woes6oNZdas-avMwy1TxZE2kAIbAujL6rQmDV4FMg3G7uvgFzFfr9GEWjxkSo_Gwbb_TyZAlffKYt8JsuMjOzefprZbCBVJ6_nEVkv8UZujKCHcOKHi59dG2lGhxjb8tySodIH6y663YH6Jol-m4q33BMlXMgqXqLsgdIglh4T0IHfnukEl7KBkUx4XklaJPL6UzW_tOGzTEo-ilJ0zusgOdql49J5H8SBWHCvtG_nIBrrR_j8UWSsG5kyd2rw-KrGPxrena4w5BUr-expHBHPpeuaH4tsbSifHTqGHAFtzmaVJZsTgPGu-MVZLEdVwt-uA_OnBy_Uy67QeLDQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ایران در دو قرن گذشته به هیچ کشور یا سرزمینی حمله نکرده، اما همواره با صلابت از خود دفاع کرده است.
با این حال، اکنون ما به ایجاد بی‌ثباتی در منطقه متهم می‌شویم و برچسب تروریست به ما می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72130" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72129">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مسعود پزشکیان:
کسانی که خود تروریست هستند و تروریست‌ها را آموزش داده و از آن‌ها حمایت می‌کنند، ما را تروریست می‌خوانند. ما تنها از خود دفاع کرده‌ایم؛ ما تروریست نیستیم.
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با نهایت قدرت از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/72129" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72128">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=nC3A9F2bOaVKbDgvUO4JVVGot3E6oEaj_Z8pHVi0C2KNhLY50u2fb9lPGe9RvihMjWmQufiQKCCZjDA_nTQZ-pi5m42Vkxd1Anjy6WgKoN5ilTUvz5kG8GTDZeabwzFp68-0jG5mm25kptd5lJSU1xX8vyuCFMb64-k9EIHgB3Y5gxLlM0y9GpRqq6dg12TxX3mhI7Zp6JhRl_KNCgLDZcRUBqzVkMKeltGwKYWAgZEPw7QdpUmk-1Mey8d-4rJk_VPSnw-_DxkXmhjNxUCSv2Cb8l66xG2a8aN0MAGItFz_reYNc5D1YH5JpPjEoer177vETM7s6VCVFR3FDCk56zY4liE-3OovDMI9MevTGM-cjZaYbH7cGNZr6WMgTmUyyvhwdqHEjJAsRN1KFTB-aVUPvNATJhEo0mQqo2jcJxCkYVuCX1yDkzh5igF0pFlBcJfDWYVb3DzQogNAiqFE3Yr4masOUByJOqdLq7yoByspx8Cmosq9cmx51AEXMX8PjXjSG7GjXGkQOIvs7WtfzbzfNBvuStO8F7EMm_295rEdfjVqJ5tFjZru7gwuVOlfIV44TetLtGOWK75_JW6cWE5MJZLzhc2Aks5FQG4Vly1yRvL0n8sezAqsNpdcaFlreKHecL7zp0CCYLQs7j3mX74bD4lpIY6iWcqUGbldWhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=nC3A9F2bOaVKbDgvUO4JVVGot3E6oEaj_Z8pHVi0C2KNhLY50u2fb9lPGe9RvihMjWmQufiQKCCZjDA_nTQZ-pi5m42Vkxd1Anjy6WgKoN5ilTUvz5kG8GTDZeabwzFp68-0jG5mm25kptd5lJSU1xX8vyuCFMb64-k9EIHgB3Y5gxLlM0y9GpRqq6dg12TxX3mhI7Zp6JhRl_KNCgLDZcRUBqzVkMKeltGwKYWAgZEPw7QdpUmk-1Mey8d-4rJk_VPSnw-_DxkXmhjNxUCSv2Cb8l66xG2a8aN0MAGItFz_reYNc5D1YH5JpPjEoer177vETM7s6VCVFR3FDCk56zY4liE-3OovDMI9MevTGM-cjZaYbH7cGNZr6WMgTmUyyvhwdqHEjJAsRN1KFTB-aVUPvNATJhEo0mQqo2jcJxCkYVuCX1yDkzh5igF0pFlBcJfDWYVb3DzQogNAiqFE3Yr4masOUByJOqdLq7yoByspx8Cmosq9cmx51AEXMX8PjXjSG7GjXGkQOIvs7WtfzbzfNBvuStO8F7EMm_295rEdfjVqJ5tFjZru7gwuVOlfIV44TetLtGOWK75_JW6cWE5MJZLzhc2Aks5FQG4Vly1yRvL0n8sezAqsNpdcaFlreKHecL7zp0CCYLQs7j3mX74bD4lpIY6iWcqUGbldWhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با تمام توان از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72128" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72127">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مسعود پزشکیان:
دیروز ترامپ ما را تروریست خواند؛ در حالی که ما خود قربانی تروریسم بوده‌ایم.
من از ایرانی می‌آیم که در آن، رهبر عالی‌قدر ما بدون هیچ‌گونه مبنای قانونی یا دلیلی ترور شد.
من از ایرانی می‌آیم که در آن، مدرسه‌ای بمباران شد. این کودکان را می‌بینید؟ این کودکان بر اثر بمباران با تسلیحاتی که توسط آمریکا و اسرائیل به کار گرفته شده بود، جان باختند.
آن‌ها بی‌گناه بودند و هیچ جرمی مرتکب نشده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72127" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72126">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=hk4CGH_2eJE12xp88s5D7bRQieGy1R-jrcWwjOxUZuaPEh0VDXSTuHPTawJLCi2gzthS3lDIRJ1RDVYzlFzrfyn50CB4MEkr4IsT6DuUQq6fkRQb8FgXlBMSB9dLznxGdWiMYDkUSshPHHAgjdb8fHIu_wmKJR7gm3K_OA-cK6uTk-I3JUdkvWdWbH37OIrpfCTceTBgNzkQzWpfWojcPal0XaYbQstm-iXnCaClsS6XQmRGt6furiPzzfBtL1HBufq_QhtoEo9vhtnXVLv2ZcBFSvzX4RYzeduG6wvDLFs72MRWnalPdgzYVuglxevj8NMiGrB3gCxpjgkgYA6P-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=hk4CGH_2eJE12xp88s5D7bRQieGy1R-jrcWwjOxUZuaPEh0VDXSTuHPTawJLCi2gzthS3lDIRJ1RDVYzlFzrfyn50CB4MEkr4IsT6DuUQq6fkRQb8FgXlBMSB9dLznxGdWiMYDkUSshPHHAgjdb8fHIu_wmKJR7gm3K_OA-cK6uTk-I3JUdkvWdWbH37OIrpfCTceTBgNzkQzWpfWojcPal0XaYbQstm-iXnCaClsS6XQmRGt6furiPzzfBtL1HBufq_QhtoEo9vhtnXVLv2ZcBFSvzX4RYzeduG6wvDLFs72MRWnalPdgzYVuglxevj8NMiGrB3gCxpjgkgYA6P-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت نمایندگی ایالات متحده هم‌زمان با سخنرانی رئیس‌جمهور ایران، پزشکیان، صحن مجمع عمومی سازمان ملل را ترک می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72126" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72125">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72125" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/72125" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72124">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK3df6nuFNFO3s__nNultZAWE19qSm6QUYsMoTyepVCpzlXi7WowPF2iVjycTzTNuOIUUoUbB0OTPDmvoRta4wD_7BoyyoZ_caTmSHWkOmbDjYwW-IFZbpnxzXoBTbTQJEy-tZB_O_PGBR9lF51WxnXPJtJ4Zw7gZaIx8pjV_GQFI5An8SDnwnIed4SRcm5QK5cSJbAX3PUcGG7G_ud1oULmf731A4PtnXx4s_wXEz6ssyCFI23YmKHr_xknwoD07dlnCsNvQAPKNnBBUYfdvOKR-yMO3h68mmB1BrvEbITg69SE2vMP0tGLaTTeoW0WQG_iQl9EyBjhltxABhG-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72124" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72123">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=Y4tpMLV6VSaBC0XrRWEP4i9s-NfRRx21NVKOpJvusyyuCPp-6ZwpigYB8PqVcxbIN1W66BRppHdH8to6JgCR3vdqzs0oddREnyklVo-F7ZQBnGkT5_AX10RE8zEU9FeEFZZQkynoTEG2eIMZArmQPpNZ0_c0Iwpqck0X9WEfrJgQJSDeTJDOmYFWg0r8isQcv_DOMNeljCAPOGdgJs7jFlNsLxcUilgJAar5KUZaHY26fYs0keFHYjr27LZnWHGHLMes8BmR70TbxpFhYGZA_MiGKgxD0EI1Nr2Xj0Bl4g3hVtwMloXJgqoCL_1RnDb7b8vyfbPi3bB-upVIYZ0nVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=Y4tpMLV6VSaBC0XrRWEP4i9s-NfRRx21NVKOpJvusyyuCPp-6ZwpigYB8PqVcxbIN1W66BRppHdH8to6JgCR3vdqzs0oddREnyklVo-F7ZQBnGkT5_AX10RE8zEU9FeEFZZQkynoTEG2eIMZArmQPpNZ0_c0Iwpqck0X9WEfrJgQJSDeTJDOmYFWg0r8isQcv_DOMNeljCAPOGdgJs7jFlNsLxcUilgJAar5KUZaHY26fYs0keFHYjr27LZnWHGHLMes8BmR70TbxpFhYGZA_MiGKgxD0EI1Nr2Xj0Bl4g3hVtwMloXJgqoCL_1RnDb7b8vyfbPi3bB-upVIYZ0nVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت کوکائین در تهران چند؟
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد .
این کوکایین ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است.
گویا داداشی ها سهم  مامورا رو ندادن اونا هم بار رو لو دادن
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/72123" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72122">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=EBhPmvo3eNO9waFhn_4lJRsRi-uWbh4jL6osvqs1851coVsHZNGUcLuMiyZuZNJJ8HupCuO8IyS77p_LB45C17GkaYO5r2-l0JzoSRPTv1Ail3Ms4Y5CZ5Uzf0FphPbWbhEiAtNOGZFba92RYeeMP3tKhVUUHNa5nQA_StKjxQAQ8fvaxZGs3HUTJATfDtWcg8C0JOZCkqVjFSElaEatfysYNorUYr05QA4SZiwp_9-EiSwIajINFBIYGiUs-cMNO9URNUfm5Ic5KAge1Z7a-xR2zE___cqq8xU0d5x2dn61LEbNtdQUkYDuE6ob6sXdzwn9-y12i0Kdk0ik8_9U7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=EBhPmvo3eNO9waFhn_4lJRsRi-uWbh4jL6osvqs1851coVsHZNGUcLuMiyZuZNJJ8HupCuO8IyS77p_LB45C17GkaYO5r2-l0JzoSRPTv1Ail3Ms4Y5CZ5Uzf0FphPbWbhEiAtNOGZFba92RYeeMP3tKhVUUHNa5nQA_StKjxQAQ8fvaxZGs3HUTJATfDtWcg8C0JOZCkqVjFSElaEatfysYNorUYr05QA4SZiwp_9-EiSwIajINFBIYGiUs-cMNO9URNUfm5Ic5KAge1Z7a-xR2zE___cqq8xU0d5x2dn61LEbNtdQUkYDuE6ob6sXdzwn9-y12i0Kdk0ik8_9U7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مادر توی کمد لباسای دخترش، کاستوم مخصوص سکس پیدا کرده، بعد دختره هم به این شکل مامانشو قانع کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72122" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72121">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAkI8k3zoQXiLmEOfa4WSYk23fFVLWsTiKkcEXHjynqX13VTlYrfuGl-AMpTu_m-F-xveYsGEDYt-xhR8CQ7z6tbu00eihb6hcvlUM3eroxyn2AD5rC-XqR7EucnnnFAWZ_frbGaYmibVS8CZExGeJQTWG-QTk65ygaNYM96Y8DEQ0xKB5ZC9zGPGivYj7ojdlNOwdXQ-eJMkrZMZKuv8HeCqqrMUpYDJOiFOU1mb4x4DwVXYPeTZ-WJpPm6miiTzpZji_ttNkjdHpJnr8jcQ-EfBgUoWVFow5lUwrtNXofNjDCYtB6nwgs98AhYPWDU63LxobOLlCpo7sW9zAfZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک کشتی باری در تنگه هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
این کشتی دچار آتش‌سوزی شده و بر روی آب سرگردان است. خدمه کشتی تخلیه شده‌اند و گزارش‌هایی از دو مورد تلفات منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72121" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72119">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056cf75693.mp4?token=ailiX5nH3XKieGhKxIXAWNqB2Wof8K15SE7YByYmNAh4RO4aWO8Bn0apRnwR9rgMA4-ghFmY8eHh0mf8b3bzIDzavvVzUltNCjVP1Imz5eFILQLznM5lNONeAtP3uPwrgkE05LU4QZmJlhZNSCQlGfvL8dTF8J2D0jbmnHhhFVZskp6zGSNEiT5UkneWiCdQ3sFyLrIZa4SZweiDlMydzAwf3T22IPABJAa1qAQjoDG4degS_CdgcjDXoDf0lLU-I3gO7DiJiwezx87CQ1FuWjVjySDahv24dQuOqnzRMSp4QDUlVUQsxWbzge5fM8k8Y2yKVH3B5BEVZLHHJLi9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056cf75693.mp4?token=ailiX5nH3XKieGhKxIXAWNqB2Wof8K15SE7YByYmNAh4RO4aWO8Bn0apRnwR9rgMA4-ghFmY8eHh0mf8b3bzIDzavvVzUltNCjVP1Imz5eFILQLznM5lNONeAtP3uPwrgkE05LU4QZmJlhZNSCQlGfvL8dTF8J2D0jbmnHhhFVZskp6zGSNEiT5UkneWiCdQ3sFyLrIZa4SZweiDlMydzAwf3T22IPABJAa1qAQjoDG4degS_CdgcjDXoDf0lLU-I3gO7DiJiwezx87CQ1FuWjVjySDahv24dQuOqnzRMSp4QDUlVUQsxWbzge5fM8k8Y2yKVH3B5BEVZLHHJLi9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانیال عیوضی، مجروح کشتار کرج، پس از ماه‌ها تحمل درد و جراحات، در دی‌ماه ۱۴۰۴ ترکیه را به مقصد اروپا ترک کرد و امروز خود را به سازمان ملل رساند تا درباره مشاهداتش از کشتار و برخورد مأموران امنیتی جمهوری اسلامی شهادت دهد.
هیئت ایرانی تلاش کرد سخنان او را مغرضانه و تند جلوه دهد و مانع ادامه صحبت‌هایش شود؛ اما با دستور رئیس جلسه، عیوضی به سخنان خود ادامه داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72119" target="_blank">📅 15:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72118">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=Pec3uk-3vV2yYusdaSEcIvs2XS8M61uM9m_lqilfMsP-n4puyT8SBjkvbra_iTSAmgHgKV6q_8MCZ621iEKEhXhthWmblLZ4_W3RFyrd_1RF-p8IwA1HYwy_9-HpljxnI91R8hi59a543uOa7E5LIunxDhEgxDBzqu50XZRXrge8HJmmFjDLV1ngbK-Yc_3rrLUjwWP0qrZ2bPMD_jFRq1fc2I0I4XyRso-BLKraiwQxFQkbHx0xb0Aht8JqK1eG7QLB8wd8RHWOIzpS3lLmwr4gTbyqKJ5idc5I-B1GR7kMLKwZWxpJqomY0N-GCCvnEqQGTBpTZJAw52pnin00_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=Pec3uk-3vV2yYusdaSEcIvs2XS8M61uM9m_lqilfMsP-n4puyT8SBjkvbra_iTSAmgHgKV6q_8MCZ621iEKEhXhthWmblLZ4_W3RFyrd_1RF-p8IwA1HYwy_9-HpljxnI91R8hi59a543uOa7E5LIunxDhEgxDBzqu50XZRXrge8HJmmFjDLV1ngbK-Yc_3rrLUjwWP0qrZ2bPMD_jFRq1fc2I0I4XyRso-BLKraiwQxFQkbHx0xb0Aht8JqK1eG7QLB8wd8RHWOIzpS3lLmwr4gTbyqKJ5idc5I-B1GR7kMLKwZWxpJqomY0N-GCCvnEqQGTBpTZJAw52pnin00_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقرار پدافند هوایی روسیه وسط بزرگراه رو دریابید
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72118" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72115">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mn4xbYJQsACO_VMOpNqRhVTFD58SSOa41WV_l_NARCUxT9AqXVeFgDOCZukWcTmfnuFfO-4WnDNs9kg0U1nHp7hBTzPaSSTk9IdCC-InZJmR9jmCDgNbIRmCPLWuinLg4FnmkD5_vqRJO3RsDBZJRchDovYnSkbmUKbB8KQ9ebCn1A5x5y31BHh604M623r6RS1S3twqVxxDAesXXdq1GoXSMkaKkc0jBxDx3diA8x29gnIVGdNU0bhMrunzcCTmwRigl0OlkTL_TUNdAMaW8dFf5DEZtR3ZRKFbTQN2rx1ZljThdqY6WJ44USgQkdBu5RVfj5gOcshSi6ou3HhzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmHXXNDNOLaqePx1Th-lTC8PmwHDhWcHg7a6L1e7Xb0kB268paPUUKhnLw5oEiwcHv35BqhgHVjodnB0vlYwtNSiwfPN1puMr0pbJQrAfzIgHSvzl4ndn_ESNcEZyjzN57tZ6sl7kIRmG5IfhCrwjPvsDy-2n4MvzEVuozCzGJjK1mgfDyJpRZIZhXGGCPSEjpl8ZJhlaN2eLLCHERdbaFTmLPgvGNhAmq13rCMgHxQq8clFe6cb2pOB4MN3lpXs3dXwhJXtDvkSgyM1jrUCgV_gcgXjZIBPLMDGu1PaXTNZkv_Nes6BXeWRaF94oY7RJrS0x3J5LbMnG8n1a0xMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1KBaUTrsuWrFZbnfT4Z47zjW954uMd3plI2agqXQEUFAP2lFMQDgjVojhDuUjug5uKn6MRuNywnLwqAv_lREVBEYLzUOHXfVi33A06DLZRAp8euWZ2UNwvsyXAuLNfSkdUtsQL31JYYEChiDm60YzebxGkNjb2fTyFouCxIrCnT96Wg1XoalTM8XZDZ8XW2xetobdtwDnA9049b8c0DYbUCOOacGpz1b6u3ZiQONbiZo9smy3nPjIX1dX-sVkGT1AWechC4_G4b_lfcUpbZBILbY7Gi00nhv9TBugIuui-AE0cMWl_iuSyoIHY1Hg3AF8AlRiltcHzKq9HS14JChg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این بیلی آیلیش هم روز به روز داره خوشگل تر و جذاب تر میشه هرشاتی از خودش منتشر می‌کنه کلی لایک میگیره :)
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72115" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72114">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه بخش هوانوردی ایران، چندین کشور را بر آن داشته است تا پروازهای ایران را محدود کنند.
محدودیت‌های تأیید/گزارش‌شده:
🇬🇪
گرجستان — ممنوعیت کلیه پروازهای ایران از ۲۱ سپتامبر.
🇦🇿
آذربایجان — ممنوعیت فعالیت شرکت‌های هواپیمایی ایرانی از ۲۲ سپتامبر.
🇮🇶
عراق — تعلیق پروازهای ایران به بغداد؛ احتمال تغییر مسیر برخی پروازها به نجف.
🇴🇲
عمان — توقف پروازهای ایران به مسقط.
🇶🇦
قطر — گزارش‌هایی مبنی بر تعلیق پروازها از مبدأ ایران.
🇹🇷
ترکیه — اعمال محدودیت‌های عمده.
برخی مسیرها همچنان فعال هستند:
🇨🇳
چین
🇦🇲
ارمنستان
🇦🇪
دبی/امارات
🇮🇶
نجف
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72114" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72113">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZ0uBGVXfc4yVBymTJ9OFg8rDFslmH1mbECxWek44iGWPfL86BdKcNt5A-HN6JYMUC9DX9V-YAacIZD94KYG90LXPBzG08LPZjKlElUa6h8Rm_wM4LcWtGzKUTL3jrqqHEeolZMr5AwrXrjDVv9D-VhSrVI8crRq1ECo1eg9Gm5dxzQivguquIg--C2A63MkOF0SL46fOwQZktLrRJrAlNlxaBbh2oz6k1Rmnw2H1gfHk9fHkGpP6u94FrACgMqvYBjqpgI46aoNC7er5us1Q912tTqvZzM7LpWwoI7HIonB07H3KX_XOFma_BvtXYOtJ7EDqjj6qYsHVwDwWFCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72113" target="_blank">📅 13:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72112">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foADMWJC8ZipsZ_fhlX-ND1ald90TeqN9vObvN9QdwuRGUcQd0Tr0nV8DgToKeHp9tMNCdJVStDDXgiQMnAEYFur75N-Wf7vXkFPv_6rv5X3W9QDbGIUkrZHSayPTcdCu58WWzL0oc_rAdJx4AGz7izp20oYzpPJ27YhgfAgW2M0jSTuo4UVusUWwIMsAEF-jDasbm8TdtVAE5kXcQCge4Z7D2K3G6Gcquk2WNT9-zhZqYch198cH2Rp7kVzduIRVySXjIGm6gP1XzFtj1d82ESZ8DjsUycwsy2azOs5TfTO_W_ziFjpl4I3rPgDQy0xFDVwTjnrwt2y3jZTlbUl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌ و هوای یکی از دانش‌آموزان در جشن شروع سال تحصیلی جدید:
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72112" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72111">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل:
ما می‌دانیم رهبران ایران کجا پنهان شده‌اند. ما می‌دانیم آن‌ها چه کار می‌کنند و چه می‌گویند.
به گمانم جانشان برایشان اهمیت دارد. آن‌ها دریافته‌اند که اگر به اسرائیل حمله کنند، تنها چند روز طول می‌کشد تا سراغشان برویم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72111" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72110">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز یکم مهر ماه، بچه‌های میناب دیگه نیستن که برن مدرسه...
اما جاشون پیش خواهر برادرای بزرگترشون امنه
🤍
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72110" target="_blank">📅 11:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72109">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات روته دبیر کل ناتو درباره ایران:
چرا برای از بین بردن توانمندی هسته‌ای ایران، حضور ایالات متحده ضروری بود؟ چرا اکنون در ماجرای حوثی‌ها در دریای سرخ، همه نگاه‌ها به ایالات متحده دوخته شده است؟
زیرا اروپایی‌ها به نوعی از توانمندی کافی برای انجام این کار به تنهایی برخوردار نبودند. آنجا حیاط خلوت اروپا محسوب می‌شود، نه حیاط خلوت ایالات متحده.
در آینده، دستاوردِ داشتنِ یک ناتوی قوی‌تر این خواهد بود که اروپایی‌ها می‌توانند خودشان به امور حیاط خلوتشان رسیدگی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72109" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72108">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اظهارات روته دبیر‌کل ناتو درباره ایران:
می‌توان گفت که اجرای عملیات «Epic Fury» بدون بهره‌گیری از اروپا به عنوان سکویی برای اعمال قدرت ایالات متحده، غیرممکن می‌بود.
از ۲۸ فوریه سال جاری تاکنون، ۵۰۰۰ فروند هواپیما در پشتیبانی از عملیات «Epic Fury» از پایگاه‌های اروپایی به پرواز درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72108" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72107">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72107" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72107" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72106">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMwKJtxdI5XbA3k0yXXB44o2l-8K-4y6tkIsAjaHKrI_9cZo61sOmi3H0WX8H-h9s0Wu1eAvkTQtWugNVIjrUsYt5RzzxHRAJu9J6dwFeC1tZ9MQ8NwfZOIwU00KbzQWdrtb-Gfes8hMW_z4gd32X_YZ-PYVynX1BXBt4pFuDGAEZkuwn4YRvpflrEPNYTd-mIzTcHjuHES1-nDR5vImy7OH_lBynDBzxrB7O_uFlFxOveMu7GVFiYfp4m1ji03TyTxaYnIPjqfShQMwYn8iG8dIBSooJcNWFfrr6un5N4Vhq43LTU9GG9MTW6ZJbKNJkT3RKdaA9TvREp_QBiQaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72106" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72105">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72105" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72104">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=fm-NKwYEJYgJu-ukOa9LUg7FdvRwiyP28xAsTZKZRNOWURgNfRi-Nt--krg4UFxiHXFa_STzYQBFFsTxdrBJI9MooFyo-anZP-rcbrim5X2CvrMuoiF5ERMF6e67tlxvCO0b1R0tFgmtC7-huoy7pVXyVhvtuCCOUV-35FFUDycsOutRWr7zWCS_j7-rx-xS0WDF9UOL3nswz4rBYXzmKRCGPZINiYIPtPHg6Lk1-zSX45SQs617_8EAbo1AGcPpfXIv7j8Lugkb-fXDw6-Ol7xup3JopBddMbvt99ClujHS6205H4Lr06wqCMXGBLgEeuSiXJio4VUT4g1Lnml3MmmkVOlYw24iL6cri8H6hF_dmFnCWOFCwCSj7Kia7zDQI1ojZTawC6nmEhn7Tj5GJ55NhByILJFIqcmqrNqCL9cg_Bjb2LbIIiRIGjrphXuNn0dCS2X785SsZbxlvMCFVLJhtePU0XxZ3u91AkmysuNZmYsttvcorb_xVUUixQ8EqRmBhU4NvYpNCnTuH2LfXGPydOLle9TwKW2B84lDaaDC1OIPNQmJ71F7dPsfipGpc4EFLW195RZB8rEbBqhPn-EwqIuNQ7cP65PdN76bXwwrpYgr7Q2ExEI58YHK_LxKvdYhCZX-spTnzi696AppbcNZ-rU4Qg358k33Ca7XWNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=fm-NKwYEJYgJu-ukOa9LUg7FdvRwiyP28xAsTZKZRNOWURgNfRi-Nt--krg4UFxiHXFa_STzYQBFFsTxdrBJI9MooFyo-anZP-rcbrim5X2CvrMuoiF5ERMF6e67tlxvCO0b1R0tFgmtC7-huoy7pVXyVhvtuCCOUV-35FFUDycsOutRWr7zWCS_j7-rx-xS0WDF9UOL3nswz4rBYXzmKRCGPZINiYIPtPHg6Lk1-zSX45SQs617_8EAbo1AGcPpfXIv7j8Lugkb-fXDw6-Ol7xup3JopBddMbvt99ClujHS6205H4Lr06wqCMXGBLgEeuSiXJio4VUT4g1Lnml3MmmkVOlYw24iL6cri8H6hF_dmFnCWOFCwCSj7Kia7zDQI1ojZTawC6nmEhn7Tj5GJ55NhByILJFIqcmqrNqCL9cg_Bjb2LbIIiRIGjrphXuNn0dCS2X785SsZbxlvMCFVLJhtePU0XxZ3u91AkmysuNZmYsttvcorb_xVUUixQ8EqRmBhU4NvYpNCnTuH2LfXGPydOLle9TwKW2B84lDaaDC1OIPNQmJ71F7dPsfipGpc4EFLW195RZB8rEbBqhPn-EwqIuNQ7cP65PdN76bXwwrpYgr7Q2ExEI58YHK_LxKvdYhCZX-spTnzi696AppbcNZ-rU4Qg358k33Ca7XWNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود. امروز، تولید ناخالص داخلی کره جنوبی پنج برابر ایران است.
وضعیت اقتصاد ایران قابل تداوم نیست؛ پایدار نیست و در آستانه انفجار قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72104" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72103">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=pLcacgW7Eb7vi9eCX05qoTtGIzBa5Ys4PgTlAroZ1NUrpQnyWpk8hmzzYdBUI7ibeFasRvpnPTk_tynuCC7JAM7GR4tVog6hR_Gf9ASkWWDEddfaJgiaMWSdvtuwgSUZ3co7NhG45A4MdaRgr49WaDiTOP-DQ5SuyPVx9Al6WrOM33hJYYKJbuqdEaAjvF1n4hHe9otrr6v7kpgAQRONFAPYbU26YfePeDHoL2sb2XthKVZp_BNFAmvyVEbgbXsZl9BatFXX2lXon9_V49PSaW4BjoVcX57crDeTyWGfWvtgMsde8_TUdlAMlzo1iCw6njHHLxPM4hhkEuO6hUiJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=pLcacgW7Eb7vi9eCX05qoTtGIzBa5Ys4PgTlAroZ1NUrpQnyWpk8hmzzYdBUI7ibeFasRvpnPTk_tynuCC7JAM7GR4tVog6hR_Gf9ASkWWDEddfaJgiaMWSdvtuwgSUZ3co7NhG45A4MdaRgr49WaDiTOP-DQ5SuyPVx9Al6WrOM33hJYYKJbuqdEaAjvF1n4hHe9otrr6v7kpgAQRONFAPYbU26YfePeDHoL2sb2XthKVZp_BNFAmvyVEbgbXsZl9BatFXX2lXon9_V49PSaW4BjoVcX57crDeTyWGfWvtgMsde8_TUdlAMlzo1iCw6njHHLxPM4hhkEuO6hUiJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگان هواپیماهای باری نظامی، از جمله هواپیماهای «آنتونوف ۱۲۴» در حال فعالیت از فرودگاه لایپزیگ/هاله در آلمان مشاهده شده‌اند.
فرودگاه لایپزیگ/هاله یکی از مراکز مهم لجستیکی ناتو است که برای انتقال تجهیزات نظامی و محموله‌های فوق‌سنگین مورد استفاده قرار می‌گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72103" target="_blank">📅 11:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72102">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=VtSyj_658B3fEXxX3fVKHrPt4xJn-kEdbAUvIA5Y9aUDgu-IafHN7d9bh1Djjfrmt9zZjtR3hIv_xlVuOqNT_aVccBS_7eZqYPt_WpNsxTrOKKgTPPOeiagTJ6HNNSbaTMi-Q5e_1NHfjvv982gIr-nntC-m0fIzSxR_q978CjseJoNaCHGloRCj968h7lxLmkqqdJkMEkLkS2uLcZMGUkS2vXtrO0c_djup1EKByk6xIiTNN543l_drINcC8idy0Wzmx__SxK4WoUI_k_DDJXKVkkGWAWzSsPY86rMqjxISafzV04q2tlY0qhp2DFy2tKmk6sA6xpJOdtvoYBnnvA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=VtSyj_658B3fEXxX3fVKHrPt4xJn-kEdbAUvIA5Y9aUDgu-IafHN7d9bh1Djjfrmt9zZjtR3hIv_xlVuOqNT_aVccBS_7eZqYPt_WpNsxTrOKKgTPPOeiagTJ6HNNSbaTMi-Q5e_1NHfjvv982gIr-nntC-m0fIzSxR_q978CjseJoNaCHGloRCj968h7lxLmkqqdJkMEkLkS2uLcZMGUkS2vXtrO0c_djup1EKByk6xIiTNN543l_drINcC8idy0Wzmx__SxK4WoUI_k_DDJXKVkkGWAWzSsPY86rMqjxISafzV04q2tlY0qhp2DFy2tKmk6sA6xpJOdtvoYBnnvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌ کم ربات‌های جای انسان‌ها رو دارن میگیرن....
برای اولین بار تو تاریخ، یه مبارزه رسمی بین انسان و ربات برگزار شد؛ که در آخرش ربات با یه لگد سنگین حریفشو انداخت رو زمین و ناک اوتش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72102" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72101">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=mJJa8bIP63VZ6R3j9wdt1z6vnNwJxHDz6dLY2rUDU9kbJe2bs6p3vs_9dl_2Cf-J4BDO8GRxaFdUGWhnei4M36t581hLQXGf2TPXX22D1U9Q12kthhMXT71j0rYCGe4sIUblmmL8Y8dU4aYbzl8mRrD5jcN1TVl1YlS6LRbWDq6wQnVTJ8epYEEkGqX-I_lhHIQdLJmtqPw1YpSp6l0-YX8YD3qCwf7sO9UGcsoES1dz2DHGtqmyCYo2jH7C3LbR7Qps8O3H_7-mJhsIBvAHJReaEZYsHJqQBe9BWPcwRqTHBWKdW4RvN2lGu2BbcZOEYFwayaapo2HTwc4zGkF8AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=mJJa8bIP63VZ6R3j9wdt1z6vnNwJxHDz6dLY2rUDU9kbJe2bs6p3vs_9dl_2Cf-J4BDO8GRxaFdUGWhnei4M36t581hLQXGf2TPXX22D1U9Q12kthhMXT71j0rYCGe4sIUblmmL8Y8dU4aYbzl8mRrD5jcN1TVl1YlS6LRbWDq6wQnVTJ8epYEEkGqX-I_lhHIQdLJmtqPw1YpSp6l0-YX8YD3qCwf7sO9UGcsoES1dz2DHGtqmyCYo2jH7C3LbR7Qps8O3H_7-mJhsIBvAHJReaEZYsHJqQBe9BWPcwRqTHBWKdW4RvN2lGu2BbcZOEYFwayaapo2HTwc4zGkF8AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لمس ممه‌های دوس دخترتون واقعا زندگی شمارو نجات میده! این یه شوخی جنسی نیست، از لحاظ علمی این موضوع کاملا ثابت شده و اینکار مثل معجزه عمل می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72101" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72100">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=k-afO3qZjkqITv35LmZhXMCRvWGsCd7mS1vtr9nvac2RlAiEIqrTInhrBH-UxKZl-FBSSA7DA1DK8eQIdnPDK8nye0ToKjT4tnDWjYua8tkev7VXm3SO6jWKKUHNd2eM1FQPKjud7KiGiR9n9nLAVILeIZg6PdcxJqSiObLW7hA9O592sIaCPTnj8sqdfhHVrA97UL6Vdcyhyo0XjrKkis80iniSteD5yryRvPhPAa5ZUs181SMP6R17IUsquwveEfGlmCLsgsU4ya8KwlH2tKnuRT1jEvxfuUhV9KQhYpYNM0xm16tmyiaA1DVTi713Jy88kDWv354UjCzppRvWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=k-afO3qZjkqITv35LmZhXMCRvWGsCd7mS1vtr9nvac2RlAiEIqrTInhrBH-UxKZl-FBSSA7DA1DK8eQIdnPDK8nye0ToKjT4tnDWjYua8tkev7VXm3SO6jWKKUHNd2eM1FQPKjud7KiGiR9n9nLAVILeIZg6PdcxJqSiObLW7hA9O592sIaCPTnj8sqdfhHVrA97UL6Vdcyhyo0XjrKkis80iniSteD5yryRvPhPAa5ZUs181SMP6R17IUsquwveEfGlmCLsgsU4ya8KwlH2tKnuRT1jEvxfuUhV9KQhYpYNM0xm16tmyiaA1DVTi713Jy88kDWv354UjCzppRvWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مشهد یه خانم حامی حکومت تو اتوبوس، به یه دختر بخاطر حجاب حمله‌ور شد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72100" target="_blank">📅 09:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72099">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیو فاکس‌نیوز با مارتا مک‌کالوم:
«وقتی من میلیون‌ها ایرانی را در ۳۱ استان کشور به آمدن به خیابان‌ها فراخواندم، آن‌ها به صورت میلیونی حاضر شدند و ضمن اعلام حمایت، شعار پایان دادن به این رژیم را سر دادند.
آن‌ها از تمامی اقشار جامعه ایران، اقوام، ادیان و گروه‌های اجتماعی گوناگون بودند؛
این جلوه‌ای عالی از اتحاد و تنوع است.
بنابراین، هر کس که ادعا می‌کند پس از ما ایران دچار جنگ داخلی خواهد شد [باید بداند که] عامل اصلی این تفرقه و اختلاف، همین رژیم است.
همه ایرانیان می‌دانند که این رژیم بذر دشمنی و خصومت را کاشته است.
اما ایرانیان دریافته‌اند که پس از دستیابی به آزادی، قادرند دوباره برخیزند؛ درست همان‌طور که قرن‌ها فارغ از تفاوت‌های قومی یا مذهبی، در صلح و آرامش در کنار یکدیگر زندگی کرده‌اند.
و انقلاب «شیر و خورشید» در راه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72099" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72098">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس سالانه «کنکوردیا» (Concordia)، پرسشی را مطرح کرد که دهه‌هاست در سیاست بین‌الملل نادیده گرفته شده است: چرا مردم ایران در کانون گفتگوها قرار ندارند؟
جمهوری اسلامی با مذاکرات بی‌پایان یا سیاست مماشات تغییر نخواهد کرد. ایرانیانی که به دست این رژیم قتل‌عام شدند، خواهان آزادی بودند، نه توافق هسته‌ای یا کنترل تنگه هرمز.
انتخاب روشن است: یا همچنان بر روی رژیمی سرمایه‌گذاری کنیم که عامل بی‌ثباتی و تروریسم است، و یا در کنار مردم ایران بایستیم؛ کسانی که شرکای طبیعی جهان آزاد برای ساختن آینده‌ای سرشار از صلح، امنیت و فرصت‌های اقتصادی بی‌سابقه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72098" target="_blank">📅 07:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72097">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrOY9lWAR46FQimYdFuFuN6sPH9hJSMuNdI8haVYDzgAfwHxhG3K9SukDpLf389mEZ8gJKO96_AxLXPKl4v-ehlNqbSu26qDxB0y4yq9dcNP_VdgTrX57juUL2RR5h002BuLYfCl4AUYXvWJmXgyLKcqV5Fwl0iMSN2bi_lAkB1v9C6AGvH5h-Y5_QqTRg7fiaKLsQ49RpAUZL-bUR-E6mIU6oE1BSmX9VUAz7UB-cpqk1GVPi83uL2QDZVOLUZPNCXDNFWoGn7YLOqB0kSz_xWfnT4H0sMYYJqeH5tZa-BBl1PkvmrL89uTH8TtYNTLKg8Dvnct40TNopw_GmUEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛یک منبع آمریکایی به العربیه:
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت.
فرصت‌های دست‌یابی به توافق محدود است.
اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72097" target="_blank">📅 07:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72096">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjYjFGnGC49Hw0a8CusGDqcAoPT8AJo1Ey3th4Ej7T0pBLGXygL0nN0u5dDjF7_FABud29XvCMbx-ya0TIzGaSemdImQ_dalvVqp-pzK63_XVWbbaad3WwaMfsLStYSpffcAxK7ovkP2pDjYmtggYt35ku0tnkel7jM8rhX0ThqhsyjUTmbVzG0g0_nEFvdRNMdL2VxBBt5PGYiONDdYSSDjcouqnh98qEid-5beqfs9gglQRQF4pIWg0L7_S71-_KEaRaBR5ycRqn-l4Ylgk-DGB2RpMiUx11rQrj3DPCHGHwmbX_6cK9-YmkaayAjyAgoymC7xBqwNANkmHnfalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف:
امروز در حاشیه مجمع عمومی سازمان ملل، از طریق میانجی‌هایی که در طول روز میان دو طرف در رفت‌وآمد بودند، گفتگوهای مفصلی با هیئت ایرانی انجام دادیم.
آن‌ها یک دور از مذاکرات را با موفقیت به پایان رساندند؛ مذاکراتی که امیدواریم سازنده و نویدبخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72096" target="_blank">📅 06:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72095">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود هم رسید نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72095" target="_blank">📅 06:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72094">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72094" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدای دوانفجار جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72092" target="_blank">📅 01:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9hBLQ0OUp9NshyNk4OUpf0443A9sdDUFafZTYxXTGlOKs6Om6RCQdtkFwijtIIH-LNOu4ckNNzRMAR-3RIrSO38TjZXMZ92NIjSQd-S1N68RRODWG9h0M11LLGIigV8iOCsDJ9x8bqlUexcwdana7KbIpGTJVIjhUntxH4rrFR8WXFTHyMgBMdobcX4RPFLY3PNGpoMdmpcDfD0jwBJzxDPEoUori2GC0Mnsa7j5I7d9D2l0MLtjmvQdLWW5S45UL7EU0zPzsdF9bQJZauTP2judPsIplmXrhuxL9dMbyj-fs4YavcI_1rvPHfddHjb7SdGDL-l1ezUaK9_dHhl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای‌نت:
انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.
هیئت نمایندگی اسرائیل همچنین خود را برای احتمال مزاحمت یا خروج هماهنگ‌شده در طول سخنرانی آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72091" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ایرنا: صدای انفجار در حوالی جزیره قشم به گوش رسید
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72090" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=S0TRTH3tsUloB5AdPwv9D1N4wH1uFWcwCOO-w31_GxTs6dDXk1xObvrqCKjBZFhYrUg07LjMbbYqYNBuqPR46Dx7n9iFhxn3Jc1sW42tDV6tDA9Z8SlV37XrZ5oXuVLhyZbRYbiFSKFSiIlboNUNDgV0NmHRaECACJVN3itP7ev8zhNspgT5Pmmql9qOUEXRKPhogL8-rFZ8cc63VhH-K5kqA2kSediZ3DJpxd4f1mE1Mb8vK8ewdKH8qZljIEaZnkaBS9MtyK0XU6cjHJVKXSna1GPFDejyvGGoJMRAKDYQWc3w0hvqK44jx5R9twL6Hk1HZStMow9AUV-uFbNUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=S0TRTH3tsUloB5AdPwv9D1N4wH1uFWcwCOO-w31_GxTs6dDXk1xObvrqCKjBZFhYrUg07LjMbbYqYNBuqPR46Dx7n9iFhxn3Jc1sW42tDV6tDA9Z8SlV37XrZ5oXuVLhyZbRYbiFSKFSiIlboNUNDgV0NmHRaECACJVN3itP7ev8zhNspgT5Pmmql9qOUEXRKPhogL8-rFZ8cc63VhH-K5kqA2kSediZ3DJpxd4f1mE1Mb8vK8ewdKH8qZljIEaZnkaBS9MtyK0XU6cjHJVKXSna1GPFDejyvGGoJMRAKDYQWc3w0hvqK44jx5R9twL6Hk1HZStMow9AUV-uFbNUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت
ترامپ:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72089" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oK8lE73_aEX49Lbd53eXu-4rIqTPKAkmI0zmrAvvnbAxBtFF4DHs3gxAzbCSGWpLNRyWZUsW0DLy2mvKkQXXbsdnw8MGkZ3oQCJFQbA8AQuARrfZiStwWxMh9xAEbw7JkUBY396zTWyKt8sQwUyj2wbz4bbtZpR7JvfSNudM1gbIP1gq243nkNMlJAmSb5zsV8Yk4kKGC_XoHyMf_oaaUxEBLPffn4bm2RimP3vZHcdrj60Cpj-ttZ3vYQWL_hKRffLONO2upSyVhYPYIUrKPr8XfoM8wgmo8Y6i1i76YGs-1JgKD60kg66_InPxKYOIXNzBFglFbG4GqqZvKXB7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که تندروهای جمهوری اسلامی از پزشکیان تو نشست سازمان ملل دارن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72088" target="_blank">📅 01:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72087">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تابستون هم تموم شد و رسما وارد پاییز شدیم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72087" target="_blank">📅 00:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ساعت ۰۰:۴۷ بامداد چهارشنبه؛ یک انفجار در محدوده تنگه هرمز رُخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72086" target="_blank">📅 00:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=Jl7v4NjzVB-7XMTO8wadoFO5s3niy_T5gWK6puXdLG79M4-Ptua8gH63eFm9k1i6pAsSN7qCBKPAAunh7CXTUkfh8tvNM6uh-OS16vVUspekFqNZZlE4DTQsDmsIrKphS6eg-f9hsNtPyMzv5wPzqCyoKf8wuepg6juj62uzqtVGZarOV9apRBuUZDBXq-vhioh678WJg12ntou3sZcX65DWp0xPbFKEWMz6-Jj57uQ6Qn-PwRBPIRjlkuzGm6soCka__ZZ7asKoVpCFb_QJE5ZcRSz6Z7c-T5fWFEzw36TsF94QhZP8lMGHsN6akc42wik8g6_IyPe-V6r1Ud36pDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=Jl7v4NjzVB-7XMTO8wadoFO5s3niy_T5gWK6puXdLG79M4-Ptua8gH63eFm9k1i6pAsSN7qCBKPAAunh7CXTUkfh8tvNM6uh-OS16vVUspekFqNZZlE4DTQsDmsIrKphS6eg-f9hsNtPyMzv5wPzqCyoKf8wuepg6juj62uzqtVGZarOV9apRBuUZDBXq-vhioh678WJg12ntou3sZcX65DWp0xPbFKEWMz6-Jj57uQ6Qn-PwRBPIRjlkuzGm6soCka__ZZ7asKoVpCFb_QJE5ZcRSz6Z7c-T5fWFEzw36TsF94QhZP8lMGHsN6akc42wik8g6_IyPe-V6r1Ud36pDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
استیو و جرد امروز جلسه بسیار پرباری با میانجی‌های ایران داشتند. باید دید در ادامه چه پیش می‌آید.
به گمانم انگیزه و شتاب زیادی برای دستیابی آن‌ها به توافق وجود دارد؛ این همان چیزی است که از همه می‌شنویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72085" target="_blank">📅 00:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72084">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=ANzOAfun4ePiU9RFjwbGGebZR89IbfIT9ib3j_GqVNpCE6PrhIHee0RRBtiTBBQ5qHXeZK-p890LR1-SWu6xG5YqR7KAiRHk7GvoYrd4qXmmYDdzV439_U-nSA8F0O0hdhCW4x6WY_xhYAd7qmMYqkHRoczza-FvwGWH9VRMJU5SqX004lTYcEi4OQJb7BKP9RcA53-a8S6vQJ0D5BY43340II1w6b42X9o_Q6rinN5FUL4vOB19WsbxF6gEm9acAVUAOW9EfRX7suI0r45SrNrI1QCNtRT7J2kQZ--PQ-gALwz_mvXbThJzdKMPObEIbuHeokBBzfrxUOoy-cK5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=ANzOAfun4ePiU9RFjwbGGebZR89IbfIT9ib3j_GqVNpCE6PrhIHee0RRBtiTBBQ5qHXeZK-p890LR1-SWu6xG5YqR7KAiRHk7GvoYrd4qXmmYDdzV439_U-nSA8F0O0hdhCW4x6WY_xhYAd7qmMYqkHRoczza-FvwGWH9VRMJU5SqX004lTYcEi4OQJb7BKP9RcA53-a8S6vQJ0D5BY43340II1w6b42X9o_Q6rinN5FUL4vOB19WsbxF6gEm9acAVUAOW9EfRX7suI0r45SrNrI1QCNtRT7J2kQZ--PQ-gALwz_mvXbThJzdKMPObEIbuHeokBBzfrxUOoy-cK5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند.
می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72084" target="_blank">📅 00:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72083">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تسنیم:
دیدار استیو ویتکوف، نماینده آمریکا، با عباس عراقچی، وزیر امور خارجه ایران، در حاشیه مجمع عمومی سازمان ملل متحد، پس از درخواست‌های مکرر طرف آمریکایی برگزار شد.
ایران اعلام کرد که از این جلسه برای بیان شرایط خود برای بازگشایی تنگه هرمز، از جمله لغو فوری محاصره دریایی، آزادسازی دارایی‌های مسدود شده ایران و پایان جنگ در همه جبهه‌ها، استفاده کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72083" target="_blank">📅 00:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72082">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=MBCSqcJE00WZ_H_2J2RogT6m3N8QCT7u4Q33uj5kvY8SywUxKEuml_oibVN3XzlMamT4MQe1PtWNX1ZZm0RcpkKtW_K4Sw0hEp4QLSv0fATgg0sCpYhXMOrINX0mcF-eT9btrSn1ZfJAWh0E41WjqyW9RfsoaEyfQYimrnv2DPR0DVnXAjSUW7FIALlv2XsOVz3vMyp-Z9n9lk7QUn36JWrlA1m6t-8oK7_Yc8da8j-JSGGZCdBJPi5w9iDPBU1vnn7dv6QCV9RkuWii1uO8qozfeW0c37qvO1IPlaz26jHCOe9vbvZRHiQdgW9orkIHjTATupYGGo0Gzd_n0g5VaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=MBCSqcJE00WZ_H_2J2RogT6m3N8QCT7u4Q33uj5kvY8SywUxKEuml_oibVN3XzlMamT4MQe1PtWNX1ZZm0RcpkKtW_K4Sw0hEp4QLSv0fATgg0sCpYhXMOrINX0mcF-eT9btrSn1ZfJAWh0E41WjqyW9RfsoaEyfQYimrnv2DPR0DVnXAjSUW7FIALlv2XsOVz3vMyp-Z9n9lk7QUn36JWrlA1m6t-8oK7_Yc8da8j-JSGGZCdBJPi5w9iDPBU1vnn7dv6QCV9RkuWii1uO8qozfeW0c37qvO1IPlaz26jHCOe9vbvZRHiQdgW9orkIHjTATupYGGo0Gzd_n0g5VaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز یک نشست فوق‌العاده و مثبت بین کوشنر و ویتکاف با نمایندگان ایرانی داشتیم
واقعا در مسیر خوبی حرکت می‌کنیم اونا خیلی میخان توافق کنن اینو همه میگن
شتاب قابل توجهی برای مذاکره داشتیم
اقتصاد ایران رو منزوی کردیم اقتصاد اونارو نابود کردیم این خیلی خوبه
تنگه هرمز رو از مین ها پاکسازی کردیم و نفت جریان داره همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72082" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72081">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=XzTFW2Hj4hx8WurZEae3nKiH_ViC3sj-_D7usLjz_-gB8p1ShRmxMttWR-8GVOb_NDBf7kHUS4Fq-qHs5Vx9pitkOlNKDAWodww_XLvqj4-8kjgKHaARC1j7OLD1G75eftkJU9jMgcyR3DR7KQ9FzV7QiKH03wPhZ34gciQN3SmucObtKzoemaE63GalWQdk6HNBXr6lsgRPWpV1ZNk43CT3492WdLDVHNjeVD4g_uxjGTMXTU4rOsL9WZ5PJCjhkYX8ckP1dX7iDzZnSZMVvzRW0cdEQO3w8hl-heV3Ud7IpqYZo_VU-ChCNkeSo4svBqFNzFfesNpQFlSa6Y67vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=XzTFW2Hj4hx8WurZEae3nKiH_ViC3sj-_D7usLjz_-gB8p1ShRmxMttWR-8GVOb_NDBf7kHUS4Fq-qHs5Vx9pitkOlNKDAWodww_XLvqj4-8kjgKHaARC1j7OLD1G75eftkJU9jMgcyR3DR7KQ9FzV7QiKH03wPhZ34gciQN3SmucObtKzoemaE63GalWQdk6HNBXr6lsgRPWpV1ZNk43CT3492WdLDVHNjeVD4g_uxjGTMXTU4rOsL9WZ5PJCjhkYX8ckP1dX7iDzZnSZMVvzRW0cdEQO3w8hl-heV3Ud7IpqYZo_VU-ChCNkeSo4svBqFNzFfesNpQFlSa6Y67vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا داره آب خلیج فارس رو می‌ریزه تو امارات تا تنگه هرمز خشک بشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72081" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72080">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=pLIldMLH5PIhldn6tGpghnrbmd97I7BKb7-1RBf5--Il0QLNdngytQN3TtiLlFe8f1465XXj1MT4Y9DB7el_YyEmE6smrw1hzhs7NmH1SppTCkr51QybqGqWl9kxhyhdiXmquoYqMVoYX7TLQjcuEIp_Eku-3Ahzk9mTIMgTZ8bcHboEvEFHGHgN3BoYKYOMimTzpaYKW84DSjZB8FEE_idn-2ZKwjSMVSJBBtghf0roUO_LpfB5zZpOap6ue8DZ3CzEu_HEN52AEYbOdNiHtElfRWYZ_yBJF_YCyDe7V7NqQVYcyO7AcUctK4Xa5M0kPYhO_arY0O5NI3RnOtwbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=pLIldMLH5PIhldn6tGpghnrbmd97I7BKb7-1RBf5--Il0QLNdngytQN3TtiLlFe8f1465XXj1MT4Y9DB7el_YyEmE6smrw1hzhs7NmH1SppTCkr51QybqGqWl9kxhyhdiXmquoYqMVoYX7TLQjcuEIp_Eku-3Ahzk9mTIMgTZ8bcHboEvEFHGHgN3BoYKYOMimTzpaYKW84DSjZB8FEE_idn-2ZKwjSMVSJBBtghf0roUO_LpfB5zZpOap6ue8DZ3CzEu_HEN52AEYbOdNiHtElfRWYZ_yBJF_YCyDe7V7NqQVYcyO7AcUctK4Xa5M0kPYhO_arY0O5NI3RnOtwbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72080" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72079">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=GHvS1Hc39wsMagIBy4kVXt_nBUYszi1YvFrZjz1AZuUQcTWAG5l6dmgMO9dOsns85fthiqB0TUSp6G43vUpUW5aWTTkIRFKg7EgTIFMPEdN3PXoqRNRq3VCJYAYpc0DMb-lYbi9ZL7OSMlAKQkPR7dnAe5RpHxxLNrdkZBkELFmPPcQPw8wBt0thlqjld-CPSWEeKmSPxno8Ey33wJOMEU1QNFmDemHzsdlidp0sT2ZoFQd-fFUB8yRhJePuwtvKBxlXSquiuJ-hv7JS0cynXUJUs2XyJJN1kzUZly_0KN1GfsfSKD2JgXoYinue2iqpFRMUul1lkJ9PkihthB1AuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=GHvS1Hc39wsMagIBy4kVXt_nBUYszi1YvFrZjz1AZuUQcTWAG5l6dmgMO9dOsns85fthiqB0TUSp6G43vUpUW5aWTTkIRFKg7EgTIFMPEdN3PXoqRNRq3VCJYAYpc0DMb-lYbi9ZL7OSMlAKQkPR7dnAe5RpHxxLNrdkZBkELFmPPcQPw8wBt0thlqjld-CPSWEeKmSPxno8Ey33wJOMEU1QNFmDemHzsdlidp0sT2ZoFQd-fFUB8yRhJePuwtvKBxlXSquiuJ-hv7JS0cynXUJUs2XyJJN1kzUZly_0KN1GfsfSKD2JgXoYinue2iqpFRMUul1lkJ9PkihthB1AuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی فروتن، عمو فیتیله‌ای:
این روزا وقتی دختر، پسرا میخوان باهم دوست بشن، خیلی برای همدیگه لاف میزنن!
معیار انتخابم که شده پول، قیافه، خوش گذرونی و... به نظرتون گند نزدیم به عشق و عاشقی؟
یه زمانی آدما دنبال کسی بودن که نه تنها حرفشون، بلکه سکوتشون هم بفهمه. به خودت احترام بذار و با هرکسی وارد رابطه نشو.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72079" target="_blank">📅 22:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72078">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امیر قطر در مورد غزه:  اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند: توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72078" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72077">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=MZ5lXz9BIVOzKz4FGnjchLtb08PPGatpkO5Maabq0KGFV6CO2hTLkdWd4bn50RkW1NZwKi0Z382-cluW-1O8C7XIXGbn0xdDuBzxhfullqFmqPm-6WJ3MBbSiPIfUjmhKNcYHRNicquNqP0JWL6RZ8x6nW9nJ0db9E0oSlhR8qViUwYQEAapdwlvrzP9x7sQPAlzQOuL-ihjqD_UrmEEv8pADWhd3roe5D_jtQluKE5vdhka6YjRCYpH6C7FjTRu1YC9vzk38tqvqir7_KCHHcFMdPAlDZ5zwp9buooz4xlBUMj73dD2TLPILmhB_qf9c-7vLpzMx7ajRggI9C2GBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=MZ5lXz9BIVOzKz4FGnjchLtb08PPGatpkO5Maabq0KGFV6CO2hTLkdWd4bn50RkW1NZwKi0Z382-cluW-1O8C7XIXGbn0xdDuBzxhfullqFmqPm-6WJ3MBbSiPIfUjmhKNcYHRNicquNqP0JWL6RZ8x6nW9nJ0db9E0oSlhR8qViUwYQEAapdwlvrzP9x7sQPAlzQOuL-ihjqD_UrmEEv8pADWhd3roe5D_jtQluKE5vdhka6YjRCYpH6C7FjTRu1YC9vzk38tqvqir7_KCHHcFMdPAlDZ5zwp9buooz4xlBUMj73dD2TLPILmhB_qf9c-7vLpzMx7ajRggI9C2GBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قطر در مورد غزه:
اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند:
توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72077" target="_blank">📅 21:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72076">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=bG7CsS0d5hq3b8V7YOJ3FW0YBWTml2O9U9pr56ilOJNO2NapHjSrNMUX3EYHGvMkcF5iEBxZaP4NBDLKKBvaiFECW-NaX-mf7CWfLUW1oMBpr2TtNd0g20jymlUNS_CggwYBC-gP_7vipc2oyLNaTGExHZdBLWxNpD0ghixVMtM6UkO-R5aVHjb8o_6u9qsJ1Doi_eQXimXnOh6eKjEEwE5JhHPP9TGPys4w3WJ5gN8DNaobl4zoCaZTuX7cVYZFb9NOKynVfoSGAerdaypc85o-BQ_zQFni9bUJKOBsaML4nyQMB7snInPj9dHhTjtU0iv7oSCjZ4Rk6OUfM1hmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=bG7CsS0d5hq3b8V7YOJ3FW0YBWTml2O9U9pr56ilOJNO2NapHjSrNMUX3EYHGvMkcF5iEBxZaP4NBDLKKBvaiFECW-NaX-mf7CWfLUW1oMBpr2TtNd0g20jymlUNS_CggwYBC-gP_7vipc2oyLNaTGExHZdBLWxNpD0ghixVMtM6UkO-R5aVHjb8o_6u9qsJ1Doi_eQXimXnOh6eKjEEwE5JhHPP9TGPys4w3WJ5gN8DNaobl4zoCaZTuX7cVYZFb9NOKynVfoSGAerdaypc85o-BQ_zQFni9bUJKOBsaML4nyQMB7snInPj9dHhTjtU0iv7oSCjZ4Rk6OUfM1hmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیداری بسیار خوب و سازنده داشتند. دیدار دیگری نیز برای آینده‌ای بسیار نزدیک برنامه‌ریزی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72076" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847d96020.mp4?token=EwKCtyF5oqS6wBhMWDheWGwCCWJ6Jvr6T7rSWlGnY70cNNuEPNW2pp7b45A3dCKo2Od7lGBG2CdCEiU2wxkB513zW5YNMMDaF1iCjG59J7FzjB9qmB1m0K0YaSPxB2wHOTG7auqCkrI13CboVK0h0iJBAiSL8vz8pehwgzMSzLdHYUT6WcHKudIxa6ARm13Avfx-sMy84Js7wdUbtWwnLNYhEqNyY7B7rRCFPJaUiejV9otyt4LKFCdnu0EtK7RsOBgATTA-ADN-xmfpmQ_WVPRdkjxUbhNh8nFQPhtVgx300OzhiLfOOlGAPzdB5T5wEMCj8tEfqOjJsGeGbQF06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847d96020.mp4?token=EwKCtyF5oqS6wBhMWDheWGwCCWJ6Jvr6T7rSWlGnY70cNNuEPNW2pp7b45A3dCKo2Od7lGBG2CdCEiU2wxkB513zW5YNMMDaF1iCjG59J7FzjB9qmB1m0K0YaSPxB2wHOTG7auqCkrI13CboVK0h0iJBAiSL8vz8pehwgzMSzLdHYUT6WcHKudIxa6ARm13Avfx-sMy84Js7wdUbtWwnLNYhEqNyY7B7rRCFPJaUiejV9otyt4LKFCdnu0EtK7RsOBgATTA-ADN-xmfpmQ_WVPRdkjxUbhNh8nFQPhtVgx300OzhiLfOOlGAPzdB5T5wEMCj8tEfqOjJsGeGbQF06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز، حدود یک ساعت پیش، گفتگویی انجام شد. گفتگو بسیار خوب پیش رفت و یک ساعت پیش به پایان رسید.
این نشستی بود که سه ساعت به طول انجامید.
مسئله، عظمت — یا عظمتِ بالقوه — و یا نابودی است.
در یک حالت، صحبت از نابودی است؛ و گزینه دیگر، عظمتِ بالقوه است. [ایران] می‌تواند کشوری بزرگ باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72075" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=KD8wE4ESSrQwbuxoEKVkn4YxCVloO0Y32EhQLl4LH8Zg6E4RtwfTtUqXiVOrOc7lFKWu4slUVt-W8HrV5ByIc0tw_4TDW1bzcDqUkQcnh91n9zDEwok-j6Y35v9xoaqs93mszW3upx9voMmhDNH-JHGXUjMldF1TdMMB2T9NfT0-widXr1g6j6nRHo4tQVaNjNGd7IrD_Wv4RG1UDb3-CSoqXrDFoHL6A7SXa7qhLrefl7jMCQJ2pEjd26uRDYTaFpf2rdF_I6df0OREbKP01PK_5naGtFKbkhUfg79W2ht1kKhacnACoXrcPVcomaEnUaW4VRfUBaf2irF4fvdy7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=KD8wE4ESSrQwbuxoEKVkn4YxCVloO0Y32EhQLl4LH8Zg6E4RtwfTtUqXiVOrOc7lFKWu4slUVt-W8HrV5ByIc0tw_4TDW1bzcDqUkQcnh91n9zDEwok-j6Y35v9xoaqs93mszW3upx9voMmhDNH-JHGXUjMldF1TdMMB2T9NfT0-widXr1g6j6nRHo4tQVaNjNGd7IrD_Wv4RG1UDb3-CSoqXrDFoHL6A7SXa7qhLrefl7jMCQJ2pEjd26uRDYTaFpf2rdF_I6df0OREbKP01PK_5naGtFKbkhUfg79W2ht1kKhacnACoXrcPVcomaEnUaW4VRfUBaf2irF4fvdy7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گفته خانم دکتر؛
مردهایی که به‌طور مداوم رابطه جنسی دارن، طول عمرشون تا 50 درصد افزایش پیدا می‌کنه و همچنین خطر ابتلا به بیماری‌های قلبی هم تا 45 درصد کاهش پیدا می‌کنه.
-در زنان هم باعث میشه سرطان سینه و کیست تخمدان نگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72074" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=Mm5a00ljxW6929hmrnU0qiAXLEoHPFEtGMI2mqwT4PfYnlfaI8Lu9f-i84xQr5fu_Hy0Li6rAoShNDswRNoGUBXz5G5iAoE2LlDW6TokXLqHXKenurza2om7-QJ653-_SpKE56WVBKppvkzFeGOw8vlCz7HPY3HUI9au8krOmdROykTYpZs7qJGaxzEtlkeeE8FgXhwyiIBHpgnfLII6BIYJ-cjEYqIXRS0acmzCpm6kezVS30i-dZ3dm1JHosS6K2WzRyU5iHQQ-gnNVJzoH9ZluHYRcmJGCviAqFo2UwBbH4HxtlClnyvGcc61j8lXhZubFMh02HHW9Limidnxiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=Mm5a00ljxW6929hmrnU0qiAXLEoHPFEtGMI2mqwT4PfYnlfaI8Lu9f-i84xQr5fu_Hy0Li6rAoShNDswRNoGUBXz5G5iAoE2LlDW6TokXLqHXKenurza2om7-QJ653-_SpKE56WVBKppvkzFeGOw8vlCz7HPY3HUI9au8krOmdROykTYpZs7qJGaxzEtlkeeE8FgXhwyiIBHpgnfLII6BIYJ-cjEYqIXRS0acmzCpm6kezVS30i-dZ3dm1JHosS6K2WzRyU5iHQQ-gnNVJzoH9ZluHYRcmJGCviAqFo2UwBbH4HxtlClnyvGcc61j8lXhZubFMh02HHW9Limidnxiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بانوی اول ما کجاست؟ یک جایی همین اطراف است.
ملانیا:
👋
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72073" target="_blank">📅 20:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس:
چند کشور عربی در تلاش‌اند زمینه برگزاری یک دیدار سطح‌بالا میان دونالد ترامپ و مقام‌های ایرانی را در حاشیه مجمع عمومی سازمان ملل در نیویورک فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72072" target="_blank">📅 20:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72067">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=anZ7h5NgGXCvKntSiPNJ-XbFKOtFnwB6lhxWN_Hy1ZIGZAMHTbCH9gnZy-be70cKUCI6tzNhMLbzCHLnJV__u1j5GtydDiUWNUuH2RCgZPIigIxkr1RXlrNOOgBvNrpQ4D_HAxSXtH7m-tDL18p8TAIlybxzEyEfsVFBEEs9XJf71XWoH6_u-cJYThP2NPkTzeGjXGsjMwftDuf_ceYmisrs493CQdLxe-V6EFmjhnKrDgbhpazPkJvawNja2JDqFWeCIQr57mPNQ8VKnS1Rq3-oKR2cOjnRnqfCBZVv0x_UBe-8A_i8Kti_hHrBOJlz6D-rCtEmKOC6D7VPm_SdMA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=anZ7h5NgGXCvKntSiPNJ-XbFKOtFnwB6lhxWN_Hy1ZIGZAMHTbCH9gnZy-be70cKUCI6tzNhMLbzCHLnJV__u1j5GtydDiUWNUuH2RCgZPIigIxkr1RXlrNOOgBvNrpQ4D_HAxSXtH7m-tDL18p8TAIlybxzEyEfsVFBEEs9XJf71XWoH6_u-cJYThP2NPkTzeGjXGsjMwftDuf_ceYmisrs493CQdLxe-V6EFmjhnKrDgbhpazPkJvawNja2JDqFWeCIQr57mPNQ8VKnS1Rq3-oKR2cOjnRnqfCBZVv0x_UBe-8A_i8Kti_hHrBOJlz6D-rCtEmKOC6D7VPm_SdMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در پایانه لجستیکی شرکت «نووا پوشتا» (Nova Poshta) در حومه روستای اوساتوو (Usatovo) در منطقه اودسا اوکراین، پس از حمله موشکی.
علاوه بر این، ممکن است انبارهای متعلق به شرکت‌های دیگر در آن نزدیکی نیز دچار حریق شده باشند؛ چرا که مجموعه‌ای کامل از انبارها در آن منطقه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72067" target="_blank">📅 20:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72066">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keuQhbAu5dKymnfL2ESgLNkvKSHYf62SkgmpQFSKoqlGtkOGxm8QikvSlnl9VoySTmd1p5md64KZQJXsH0fucTYC_bSrOFyJtun7ikOZQVNHNs4EKlsdKis9jcOlmez_bkvoQTyZ2upiPgxm7ZnNyNxPNh5lOcfbxEb0AA6HhvYqMI002GEFUZr1asw2hG0jZNcYWTDdPa74DG5_riYveTK-yf_S6ER_4us6H0w5ManKo-jGK3zza3tsRhsOtH6ua-VSy5RwbHmMGI5JT0SmoT6oMdVItZV5Vgwu_WbamQLizPPePmktGAjiewXgZ-YX_HMwp9V6f38WEwE4b8IhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی وارد نیویورک شده است؛ ایشان قرار است در «اجلاس کونکوردیا» سخنرانی کرده و دیدارهای خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد داشته باشد.
با این حساب دونالد ترامپ، بنیامین نتانیاهو، مسعود پزشکیان و شاهزاده رضاپهلوی هم‌زمان توی نیویورک هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72066" target="_blank">📅 19:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72065">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فعالیت مدارس استان هرمزگان ۲ هفته مجازی شد؛
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از مجازی شدن فعالیت آموزشی تمامی مدارس استان در همه مقاطع تحصیلی از شنبه به مدت دو هفته، با هدف صیانت از سلامت دانش‌آموزان و حفظ کیفیت فرآیند آموزشی خبر داد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72065" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72064">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72064" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72063">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=RgBaIKllL_T9A1q4PkjGBpbUPIzxAhp2SGsjNr2IfyYK_DNCa_iRVDIkZGQ1oWOocuBtDrucbmtJrW9lIRv_PelJxWKrOD2K8Rf6pE54sN1iG-2rShHY0Yl7pn1O1_vdy78PRHWIDN88lrO8ecfI3_tmTG5dAiWVr8OU0f0PVDiig9QSWikRmvr1tTEMoL0vbXDG6DIzj8CzURzgBUChYqwIhrtOKV3-g_dD150KdJ1-TrmJz5SXlcupTUtG7KKmGeQf0X3HxDItxbyqOXcm3rmsaGbbvYWmus3cbtWyJU_7lpRqMLbBudtEeC9l5vfEh0qn-Do_3PX1vb4R-swJkSqbNERQtvE76sg_qGh3U9_FkrYzTpphWTkoF2iW5gaye1c4i9J640AXnhXahOy-Gaqu0keQYpgG2SSrifM5s5eZ1QtTcbc7zU9syMdCN1w0z_z4weNmT7no1YQs8pjAOu_1S1McTEnvaHAmC38X8bACKEx8NLDLpNU-QlmCN7ksTbcDmV2T8sVGG9tHeR48POd7xGIS7cIF_NHh48wFeOj7J-TAhPD4rPt64Y7vnM7PtgY5MZZkA8A2vkJtS5AB-HcCzFTcH-kZt6b87aAK2Uz1hSrAZZCBA5eVFcjKhDRX6iraQa7vDzT0CKMjUWQ04vhhWlhOQb4Yj3zI9qi5S2I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=RgBaIKllL_T9A1q4PkjGBpbUPIzxAhp2SGsjNr2IfyYK_DNCa_iRVDIkZGQ1oWOocuBtDrucbmtJrW9lIRv_PelJxWKrOD2K8Rf6pE54sN1iG-2rShHY0Yl7pn1O1_vdy78PRHWIDN88lrO8ecfI3_tmTG5dAiWVr8OU0f0PVDiig9QSWikRmvr1tTEMoL0vbXDG6DIzj8CzURzgBUChYqwIhrtOKV3-g_dD150KdJ1-TrmJz5SXlcupTUtG7KKmGeQf0X3HxDItxbyqOXcm3rmsaGbbvYWmus3cbtWyJU_7lpRqMLbBudtEeC9l5vfEh0qn-Do_3PX1vb4R-swJkSqbNERQtvE76sg_qGh3U9_FkrYzTpphWTkoF2iW5gaye1c4i9J640AXnhXahOy-Gaqu0keQYpgG2SSrifM5s5eZ1QtTcbc7zU9syMdCN1w0z_z4weNmT7no1YQs8pjAOu_1S1McTEnvaHAmC38X8bACKEx8NLDLpNU-QlmCN7ksTbcDmV2T8sVGG9tHeR48POd7xGIS7cIF_NHh48wFeOj7J-TAhPD4rPt64Y7vnM7PtgY5MZZkA8A2vkJtS5AB-HcCzFTcH-kZt6b87aAK2Uz1hSrAZZCBA5eVFcjKhDRX6iraQa7vDzT0CKMjUWQ04vhhWlhOQb4Yj3zI9qi5S2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
هر کس در حوزه هوش مصنوعی پیروز شود — باید این نکته را به خاطر داشته باشید — و حالا می‌گویم هر کس در حوزه «هوش برتر» (SI) پیروز شود، برنده نهایی است.
آن‌ها همان گروهی هستند که پیروز می‌شوند.
و ما در حال حاضر با اختلاف زیادی نسبت به چین و سایر کشورها پیشتاز هستیم. ما این وضعیت را حفظ خواهیم کرد؛ مسیری بسیار مستقیم و موضعی بسیار قدرتمند را در پیش خواهیم گرفت.
من نمی‌خواهم مانع رشد پدیده‌ای شوم که ابعاد آن از انقلاب صنعتی هم فراتر خواهد رفت.
بسیاری می‌گویند این تحول حتی از انقلاب صنعتی یا خودِ اینترنت هم بزرگ‌تر خواهد بود. و ما بسیار محتاط عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72063" target="_blank">📅 18:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72062">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=JYoyVSSR_l4kJE8db3L2tvmQ1kDQp_pUb_rEh-GQY91H49QzE-sM1XOWhLXU_QZ5P2pEqYW5AospNhLDAymGbVu7XAnNTJAhAcnYeLSyD9lY01Ge1uEN5COtOslrLLg0JrucpQcw0En-7uGdAilidk2q8zsFkfiDxCFA0C6T7emgMFu5Zhysuh43KN6mXQJqimuooFflhzWXhCWW2No8wORJ31f4UJ0LY-N2g1OGyIwJK3SUgmAs3hzaMaDNxKgDlOO8D-sgWX4RZjsT4lThEIo_AGmvMeQA2Dg2-TRn9xuFs5OU-rYXv0z2rVwNVKS4fYT-mN_TzEBoN3o4ZtOFImVsBS9fdpDxF_qfGz577FwLq9jUBF-wrJC8-7W1kTRjzEqkJMlt8BgRFexqUeAkhvoJ4pmrhym_B2sSG2Ug6dXizD6KLR6dJ3Y6I1tGrLFfMmi0DV_M9FXd5wCRkaoAONl9gRurEsusQpc33hthJOy1LpxBd05pD9roq9NLFJUJXMFABx6TObBxoVxKun1T14ASGrR_wGq0Z43VcaGLthdmMbmKVotYYwq1zxj7B5M0gfoCCir1SZRgtqmmSxTxpDUoNSdFUuXAS5ri376v7rlhLjM1tR2X9gbdfPzq6zBPNAJNaC8ovDMDC8izTo7VvKxoWCAfq4wHJZVkUccrO10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=JYoyVSSR_l4kJE8db3L2tvmQ1kDQp_pUb_rEh-GQY91H49QzE-sM1XOWhLXU_QZ5P2pEqYW5AospNhLDAymGbVu7XAnNTJAhAcnYeLSyD9lY01Ge1uEN5COtOslrLLg0JrucpQcw0En-7uGdAilidk2q8zsFkfiDxCFA0C6T7emgMFu5Zhysuh43KN6mXQJqimuooFflhzWXhCWW2No8wORJ31f4UJ0LY-N2g1OGyIwJK3SUgmAs3hzaMaDNxKgDlOO8D-sgWX4RZjsT4lThEIo_AGmvMeQA2Dg2-TRn9xuFs5OU-rYXv0z2rVwNVKS4fYT-mN_TzEBoN3o4ZtOFImVsBS9fdpDxF_qfGz577FwLq9jUBF-wrJC8-7W1kTRjzEqkJMlt8BgRFexqUeAkhvoJ4pmrhym_B2sSG2Ug6dXizD6KLR6dJ3Y6I1tGrLFfMmi0DV_M9FXd5wCRkaoAONl9gRurEsusQpc33hthJOy1LpxBd05pD9roq9NLFJUJXMFABx6TObBxoVxKun1T14ASGrR_wGq0Z43VcaGLthdmMbmKVotYYwq1zxj7B5M0gfoCCir1SZRgtqmmSxTxpDUoNSdFUuXAS5ri376v7rlhLjM1tR2X9gbdfPzq6zBPNAJNaC8ovDMDC8izTo7VvKxoWCAfq4wHJZVkUccrO10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
از این پس، تمام اسناد ایالات متحده — و به امید خدا اسناد سراسر جهان — تغییر خواهند کرد تا به جای واژه «مصنوعی» (Artificial)، از اصطلاح بسیار دقیق‌ترِ «اَبَر» (Super) استفاده شود.
به عبارت دیگر، به دنیای جدید «اَبَر-هوش» (Superintelligence) یا همان SI خوش آمدید.
باید دید این ایده چه بازخوردی خواهد داشت؛ هرچه باشد، خیلی بهتر به نظر می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72062" target="_blank">📅 18:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=ZreTy1JE7B9jjolx_v-7ry7h52oFQkekHbMnKwyT_EJmK_GPcty7BzfQXM292k1G9epr9BTM6J2dC_UX5zUGKo_9k9rrW95w3YCdpoU8EbGIAApP9-ywS5SqAhk0HMmEKeYSOB-BaW2dteUjYVYMqFIUtSQDY_zMEzSYRu8_CzG-O2fYJsZt4r-ucji-h1M_qct0Lj-d3YG2LiGka7ttN40XZFvFdBY4PHzHbU3Ue_Mx9RxJhXtef7VeHmG631rjFd1JvDjfAaIUvoOtnEUD4ls5LokvWZaxyRYPWyKvz26gFe2UavShAy5y_O4G383DutK68RSj_u-ZGd7HbA3zCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=ZreTy1JE7B9jjolx_v-7ry7h52oFQkekHbMnKwyT_EJmK_GPcty7BzfQXM292k1G9epr9BTM6J2dC_UX5zUGKo_9k9rrW95w3YCdpoU8EbGIAApP9-ywS5SqAhk0HMmEKeYSOB-BaW2dteUjYVYMqFIUtSQDY_zMEzSYRu8_CzG-O2fYJsZt4r-ucji-h1M_qct0Lj-d3YG2LiGka7ttN40XZFvFdBY4PHzHbU3Ue_Mx9RxJhXtef7VeHmG631rjFd1JvDjfAaIUvoOtnEUD4ls5LokvWZaxyRYPWyKvz26gFe2UavShAy5y_O4G383DutK68RSj_u-ZGd7HbA3zCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام «هوش مصنوعی» (AI) را به «اَبَر‌هوش» (SI) تغییر می‌دهد.
او می‌گوید استفاده از واژه «مصنوعی» باعث می‌شود که هوش، «ساختگی» به نظر برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72061" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72060">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156037c15c.mp4?token=kzBsrMvDVDQxTy3ZeFFFl29PsGFjoo07bmo0082FAVJDehWrdxd-xDS_f_pwV7Qd_Gs6oiTr8Lb7lB-HOpVvHLDAkfZaJyihvo-gzeYfNVebZVSLTR8_neeUdt4YsFKR4sRT7wLxs-A7MSjci5iyJ0p4ODG2PSfb2BU51Flh4SR6614LDoV7xRbWSPu5tByovj2TvkgOWS6j-YR6pXinl72c_Dzycdk8XdZibNeIdMRVMzBpJLhIzCUBxyYW1XJy7HB_z82XO50si3hO_LwCYT2ZVRYpbQn6jGMD6OIfnXWq8yQg7nJ5Tjk-safkQPnj4rIkv8Uigexkw_Cw_6TcAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156037c15c.mp4?token=kzBsrMvDVDQxTy3ZeFFFl29PsGFjoo07bmo0082FAVJDehWrdxd-xDS_f_pwV7Qd_Gs6oiTr8Lb7lB-HOpVvHLDAkfZaJyihvo-gzeYfNVebZVSLTR8_neeUdt4YsFKR4sRT7wLxs-A7MSjci5iyJ0p4ODG2PSfb2BU51Flh4SR6614LDoV7xRbWSPu5tByovj2TvkgOWS6j-YR6pXinl72c_Dzycdk8XdZibNeIdMRVMzBpJLhIzCUBxyYW1XJy7HB_z82XO50si3hO_LwCYT2ZVRYpbQn6jGMD6OIfnXWq8yQg7nJ5Tjk-safkQPnj4rIkv8Uigexkw_Cw_6TcAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
نیروی دریایی ایالات متحده اخیراً بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت و عبور داده است و حجم نفت در حال عبور، بیش از هر زمان دیگری از آغاز جنگ است.
ما هر روز و هر شب، به ترتیب ۲۲، ۲۵، ۳۰، ۳۲ و ۳۷ کشتی را [از این مسیر] عبور می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72060" target="_blank">📅 18:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=p2idjL4-S_MsL9zjXOK321306iRLGDuRev-MeXnvAhM1zlyov1ooKSbMxf5nzOBaJ1Nz3RgrHc7fm_Y8Bnv17vzJjlFVpt7fXIEWiqEw-pMoNQtu9fZGni-vkwr0EPxabmJ7yt-UzBHhBMVVWK20PLpa2nc4yl6BQlpr-_sNIjgtVl_YMUuVfevI6USDk-NbGK5UaV8btRiP3xod5Cf7dFdr5oTaoZ2Wj5WXhTx3fWvKMqaBcMmDDfkHlurZIrsTpOqHN-K3DWYEim2zbY5SDrZdjTuzsehZul5PsPTGRAL_OLJlSoAjKkhtSIqMmLDLyu7efyJrCOsAKlJMiG9qcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=p2idjL4-S_MsL9zjXOK321306iRLGDuRev-MeXnvAhM1zlyov1ooKSbMxf5nzOBaJ1Nz3RgrHc7fm_Y8Bnv17vzJjlFVpt7fXIEWiqEw-pMoNQtu9fZGni-vkwr0EPxabmJ7yt-UzBHhBMVVWK20PLpa2nc4yl6BQlpr-_sNIjgtVl_YMUuVfevI6USDk-NbGK5UaV8btRiP3xod5Cf7dFdr5oTaoZ2Wj5WXhTx3fWvKMqaBcMmDDfkHlurZIrsTpOqHN-K3DWYEim2zbY5SDrZdjTuzsehZul5PsPTGRAL_OLJlSoAjKkhtSIqMmLDLyu7efyJrCOsAKlJMiG9qcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایالات متحده و ایران قطعاً این کار را به سرانجام خواهند رساند. ما به هر طریقی که شده، این کار را انجام خواهیم داد. این کار انجام خواهد شد.
این کار به‌سرعت انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72059" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=WCpd12KJsN6qrLHDAnT9HNf9i7c-zcwT4ERzo694D1sbO9ovflFkLjF0HYFdeCnEzFcg3Yndrrbaoi3M9UzFK6HEz6YEYVKo4n8ZpdDbajgjMjDbReBgDxJSwTpDba2650iO-axuz7FIOanyIUlMaa-YroeXH0mczIWqjZs80KcBp_2bvgNWjLVJoZ0uz_7116cZdU15hRYd7UyhIuImc0oACzb_v4l6fD59mbS_HrVqpthwUgvSu3Wy4MOaVxnckMbqz9SfKpMb4RVI00H8sFQ14f__d6yUshNp8GE0i5-ONSqDrJ1irb-cE5o8XOaexfM66WZ0U_ZG0HDliCelpqLuShK2xv0HekrOr_7_NnD_l9B_h9s954ClH58bod6-GI8_q_hRLRumFDGIx7WFWKw2BlsoMCw8L6Km55cSXBfz4ZCMVWEl5ARRSuP7FDJ4f8_1U9m4dpafA-paTc4RvOZJaPVhy6skYh9P_Nb6UFng6z_LfBCtQPlsY-ZBNdnvLNXrG0n4Md-AMZoliySumARXiJjeDE4A2U_NJ2JTSdHHzd969Krae0E5_B4w2YYDgglM5xoQjV1GTMzMIhHnvEgBK0oEjwdLKzEGNc-XUNlAVM3rswD5W39GfHNGbMO_2cJcHsZBs-DzF9KE2j9KMpbjZy2929LBzd_TqmOba-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=WCpd12KJsN6qrLHDAnT9HNf9i7c-zcwT4ERzo694D1sbO9ovflFkLjF0HYFdeCnEzFcg3Yndrrbaoi3M9UzFK6HEz6YEYVKo4n8ZpdDbajgjMjDbReBgDxJSwTpDba2650iO-axuz7FIOanyIUlMaa-YroeXH0mczIWqjZs80KcBp_2bvgNWjLVJoZ0uz_7116cZdU15hRYd7UyhIuImc0oACzb_v4l6fD59mbS_HrVqpthwUgvSu3Wy4MOaVxnckMbqz9SfKpMb4RVI00H8sFQ14f__d6yUshNp8GE0i5-ONSqDrJ1irb-cE5o8XOaexfM66WZ0U_ZG0HDliCelpqLuShK2xv0HekrOr_7_NnD_l9B_h9s954ClH58bod6-GI8_q_hRLRumFDGIx7WFWKw2BlsoMCw8L6Km55cSXBfz4ZCMVWEl5ARRSuP7FDJ4f8_1U9m4dpafA-paTc4RvOZJaPVhy6skYh9P_Nb6UFng6z_LfBCtQPlsY-ZBNdnvLNXrG0n4Md-AMZoliySumARXiJjeDE4A2U_NJ2JTSdHHzd969Krae0E5_B4w2YYDgglM5xoQjV1GTMzMIhHnvEgBK0oEjwdLKzEGNc-XUNlAVM3rswD5W39GfHNGbMO_2cJcHsZBs-DzF9KE2j9KMpbjZy2929LBzd_TqmOba-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من از همه کشورها خواستم تا در اعمال
انزوای کامل اقتصادی ایران با ما همراه شوند؛ تا زمانی که آن‌ها حملات خود به کشتی‌های تجاری را متوقف کنند، از جاه‌طلبی‌های هسته‌ای خود دست بردارند و به حمایت از تروریسم پایان دهند.
این رژیم تروریستی نه به این دلیل که قدرتمند و با اعتمادبه‌نفس است، بلکه به این خاطر که ضعیف و درمانده است، چنین رفتار نامناسبی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72058" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72057">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415b898f05.mp4?token=lVrSIFyT3aZfMdYGXMaNbi6XH0T8ksZ1whPZA3b6iVbXWJeOTQjCm82KNcjYbgGpOZo-1R5T0qZ48456hJJ-e3Htf6P_1reWRU4SGWorDFs5PHdt7JrWLvo-WjreJ_K-0GUoYwdOt0THIpbBJVV93hx_ngqLJNU9GAgM-jwfT_CdJr8YGsU2oxr3eQ4pbDTsYLQwIrnFmWcxaMMzdwKRAEivQ7b4OZxchaog6t7nS21N3kt3fIU0sTVoBwDekAAx6QBiFq7QR18Rs8O7E42aU4pI0olNk5532i2ko2P8G9_6VJ8TVkimP-Qc3pfbLM9H1GhTRBw_ifv3wo7xdZ5bbyDzBvhFT9qLDEy3ewNkPJ9hi3t6lmPnai6mUIYka-tw2zsYc-VvMkeO-iM_x4V-maVS-9-bSvzCR8BSu0IPqtn9-UwrRNcnFC4po8RfqaZMAUEw0mSr1Nlwma_tKLxBS7jdoEbEh_zx3JP-qilIzxU0Ay1OXHOBM1tc0lZ-ne-8wEIpYNk4dqn_FhX3WxYudW82VGRAF2GUHqrwB3uQ2CeCFJg-tcT4BGx5XodD9aefC2FSsGm8gREuSl12ujsVf5zHTHoHkJo-LKQ71fZIY8e6pHNzMPDnGvemRRCcC95XgeIdBj74WyuGQhhfhAN5Pwg7gQFc9P4hmmC9lSZ-qe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415b898f05.mp4?token=lVrSIFyT3aZfMdYGXMaNbi6XH0T8ksZ1whPZA3b6iVbXWJeOTQjCm82KNcjYbgGpOZo-1R5T0qZ48456hJJ-e3Htf6P_1reWRU4SGWorDFs5PHdt7JrWLvo-WjreJ_K-0GUoYwdOt0THIpbBJVV93hx_ngqLJNU9GAgM-jwfT_CdJr8YGsU2oxr3eQ4pbDTsYLQwIrnFmWcxaMMzdwKRAEivQ7b4OZxchaog6t7nS21N3kt3fIU0sTVoBwDekAAx6QBiFq7QR18Rs8O7E42aU4pI0olNk5532i2ko2P8G9_6VJ8TVkimP-Qc3pfbLM9H1GhTRBw_ifv3wo7xdZ5bbyDzBvhFT9qLDEy3ewNkPJ9hi3t6lmPnai6mUIYka-tw2zsYc-VvMkeO-iM_x4V-maVS-9-bSvzCR8BSu0IPqtn9-UwrRNcnFC4po8RfqaZMAUEw0mSr1Nlwma_tKLxBS7jdoEbEh_zx3JP-qilIzxU0Ay1OXHOBM1tc0lZ-ne-8wEIpYNk4dqn_FhX3WxYudW82VGRAF2GUHqrwB3uQ2CeCFJg-tcT4BGx5XodD9aefC2FSsGm8gREuSl12ujsVf5zHTHoHkJo-LKQ71fZIY8e6pHNzMPDnGvemRRCcC95XgeIdBj74WyuGQhhfhAN5Pwg7gQFc9P4hmmC9lSZ-qe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به اتمام است، اما این حرف صحت ندارد.
ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و با سرعتی بی‌سابقه مشغول تولید آن‌ها هستیم. ما با سرعتی بیش از هر زمان دیگری در حال افزایش ذخایر خود هستیم؛ آن هم با تجهیزاتی که در بالاترین سطح کیفی قرار دارند.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. هم‌اکنون ۱۸ کارخانه از این دست توسط برترین شرکت‌های دفاعی جهان در حال ساخت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72057" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=cqJPym3HaXTPWbEj5bFhKPayvTNb4nyRFsEYwWxTVwDkm5ThrupUetuNheVV6Ok7X9rftNKOkOeGMmPnJxBh3tvowOr9KOi73M1tBOjfA9NcdMChhMIZTTGsanGS14Ie6Jt0imjFNFQWTHlbOTN7yhE9a5rLyeqH9yZ30Hi4UyhMB_D4jOdeCxrn_NW987jphhuztCd-wjryVxYP5CSJCjFJiJnTIPOdPJW-8uVy5WTbk7foAG6y0pm0RYAOlq16T0Z2LTFOzegN6sPwY_T-wMEvTf9SSnNrouHW2QX-eR1t4ub0_rZVM6C9sjNGlS8kAxnh0JCVmyZHAWQJXEmKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=cqJPym3HaXTPWbEj5bFhKPayvTNb4nyRFsEYwWxTVwDkm5ThrupUetuNheVV6Ok7X9rftNKOkOeGMmPnJxBh3tvowOr9KOi73M1tBOjfA9NcdMChhMIZTTGsanGS14Ie6Jt0imjFNFQWTHlbOTN7yhE9a5rLyeqH9yZ30Hi4UyhMB_D4jOdeCxrn_NW987jphhuztCd-wjryVxYP5CSJCjFJiJnTIPOdPJW-8uVy5WTbk7foAG6y0pm0RYAOlq16T0Z2LTFOzegN6sPwY_T-wMEvTf9SSnNrouHW2QX-eR1t4ub0_rZVM6C9sjNGlS8kAxnh0JCVmyZHAWQJXEmKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من برای انتخابات در مورد ایران مطلقاً هیچ اعتباری قائل نبوده‌ام و نخواهم بود؛ این موضوع حتی به ذهنم هم خطور نمی‌کند.
تنها چیزی که اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72056" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:باید تصمیم بزرگی بگیرم.
آیا توافقی با ایران صورت خواهد گرفت که به آن‌ها اجازه دهد کشورشان را بازسازی کنند و کشوری بسیار بزرگ‌تر از آنچه پیش‌تر بود بسازند؛ شاید حتی یکی از بزرگ‌ترین کشورهای خاورمیانه یا حتی جهان؟
یا اینکه جمهوری اسلامی را نابود کنم—آن هم به سرعت—و هرگز به آن‌ها فرصتی ندهم که دوباره دست به کشتار و ویرانی مردم و کشورها بزنند؟
آیا آن‌ها را به جهنم بفرستم، بدون هیچ شانس بقا و بدون هیچ امیدی به عظمت در نسل‌های آینده؟
اما معتقدم که بلافاصله پس از انتخابات به توافق خواهیم رسید، چرا که تن ندادن به آن برایشان منطقی نیست.
آن‌ها منتظرند ببینند عملکرد من در انتخابات میان‌دوره‌ای چگونه خواهد بود. چیزی که متوجه نیستند این است که من اصلاً نامزد آن انتخابات نیستم. من آن کار را قبلاً انجام داده و با اکثریتی قاطع پیروز شده‌ام.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72055" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=Iu-AoKtYyg5GI5UxtXqWjOcL-_zQkNr3vNQiyxsx3LSsn8E0UPrXvMaObfcoyHKl_3Vp6B1rGwqTkC71qwqD1aeD2Mdg_Se1X8-qrT9kd-WHzdgSfkX2IzvAktb_BSTTSe7wIpQGMQbdElLTzMR_WbzOHYhM58g5Tf7an75_mGlGzNcYdFm5eDzlqkBCp_8JwGywj8spinj5Og6kQNZUbQ2Jx7iv22gvmmCA3fEC5P4wWgKp2H90sd6u4oMH3tARSDuCWyzYFgbuXE06ZiXMqhJPqLnNUrWJrjyC-f___qjOyrejH4w9AGgkB11J6HEOg6Ga3cvBJ3ZEqqjgHj_m9Xv1fO_ZDAHqzOd-miA8tkag7DXH4yIg1rjhzk05ntBcB1JiNQhDZFidbPPNsLMWlvqQsI_Euw5ExVpgNCkb7Jp96geOkoEyZGOjuS7wHDpKomc5rX9Hs8fyRfmUXRqhM3GvK2peRJsfRRitDOAWndejJD_ULEPlc6LXBHt7yxRwTT6xt6vms8MBrUq184eAxvaPkPIXKaEUCMVnXijPg1lOct2PGixsxa5T_XAvToJHGWESx1d_Lu_SxCtvH4lOXW6aBjBGxqxjmfqpE9cpPC4NPWuZ-B5jcoAVSWJdqga0Q6j48CPlwq9Xu6BdxpZTqnJc6Wl2Amu99VKY_QW0vuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=Iu-AoKtYyg5GI5UxtXqWjOcL-_zQkNr3vNQiyxsx3LSsn8E0UPrXvMaObfcoyHKl_3Vp6B1rGwqTkC71qwqD1aeD2Mdg_Se1X8-qrT9kd-WHzdgSfkX2IzvAktb_BSTTSe7wIpQGMQbdElLTzMR_WbzOHYhM58g5Tf7an75_mGlGzNcYdFm5eDzlqkBCp_8JwGywj8spinj5Og6kQNZUbQ2Jx7iv22gvmmCA3fEC5P4wWgKp2H90sd6u4oMH3tARSDuCWyzYFgbuXE06ZiXMqhJPqLnNUrWJrjyC-f___qjOyrejH4w9AGgkB11J6HEOg6Ga3cvBJ3ZEqqjgHj_m9Xv1fO_ZDAHqzOd-miA8tkag7DXH4yIg1rjhzk05ntBcB1JiNQhDZFidbPPNsLMWlvqQsI_Euw5ExVpgNCkb7Jp96geOkoEyZGOjuS7wHDpKomc5rX9Hs8fyRfmUXRqhM3GvK2peRJsfRRitDOAWndejJD_ULEPlc6LXBHt7yxRwTT6xt6vms8MBrUq184eAxvaPkPIXKaEUCMVnXijPg1lOct2PGixsxa5T_XAvToJHGWESx1d_Lu_SxCtvH4lOXW6aBjBGxqxjmfqpE9cpPC4NPWuZ-B5jcoAVSWJdqga0Q6j48CPlwq9Xu6BdxpZTqnJc6Wl2Amu99VKY_QW0vuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
ما در آمریکا به‌تازگی بیست‌ و پنجمین سالگرد بدترین حمله تروریستی تاریخ، یعنی ۱۱ سپتامبر را پشت سر گذاشتیم؛ حمله‌ای که جان سه هزار نفر را گرفت. درست در همین نزدیکی‌ها.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های تحت حمایت مالی ایران، ۱۲۰۰ غیرنظامی کاملاً بی‌گناه — از جمله ده‌ها آمریکایی و بسیاری از نوزادان؛ نوزادانی کوچک، ظریف و زیبا — را شکنجه کردند، مثله کردند و به قتل رساندند.
رهبر عالی ایران آن کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72054" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9289304.mp4?token=dNJG22d6d8slrwCjJjHUZw7mvE45R5KRXaZw6Y6MZCeMbhk1pemSK1CYnAtxFwbHmEgpcDLYEUPLt4V6rWDW_Tt0EEeyK973rSvj8PrPbyTNKoCQ-i89NuS6ycNcvcqIqW463haodFPTs21NmQT7uWlO09z3W9IeL3f8MUVmH5UNndpKyb8JEkx3HS8cU_lML-QsG4QH7m2aqcB2ncdkBTzYovPdk-3O1CKIZZ4lRDiGaTc3goWyCSlfrmjvGtTz3CSL68jaUqP0_1DZBwlEH7Jcb0jwljTi6T41CNhWx88HLFd2oiO8IoopObgD3rnAs3O3lMG-tWcpqCZqYZKOdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9289304.mp4?token=dNJG22d6d8slrwCjJjHUZw7mvE45R5KRXaZw6Y6MZCeMbhk1pemSK1CYnAtxFwbHmEgpcDLYEUPLt4V6rWDW_Tt0EEeyK973rSvj8PrPbyTNKoCQ-i89NuS6ycNcvcqIqW463haodFPTs21NmQT7uWlO09z3W9IeL3f8MUVmH5UNndpKyb8JEkx3HS8cU_lML-QsG4QH7m2aqcB2ncdkBTzYovPdk-3O1CKIZZ4lRDiGaTc3goWyCSlfrmjvGtTz3CSL68jaUqP0_1DZBwlEH7Jcb0jwljTi6T41CNhWx88HLFd2oiO8IoopObgD3rnAs3O3lMG-tWcpqCZqYZKOdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این رژیم امسال بیش از ۷۲ هزار تن از شهروندان خود را به خاک و خون کشید.
تصور کنید چنین رژیم پلیدی قدرت آن را داشته باشد که از پشتِ سپرِ هسته‌ای، دست به حملات تروریستی گسترده بزند.
این واقعیتی بود که باید با آن روبرو می‌شدیم؛ واقعیتی که بسیاری ترجیح دادند آن را نادیده بگیرند. همه آن‌ها آن را نادیده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72053" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=oQqYpaEnDhFzYTzKhwPiOTOJyoNlEAiLygaiYSBGIGCKNbqve8u2gBvUlR3O6FQvjKMQ478qiBaheQjowR2-LxjacUzcyXEayhQ6C-VQkcOzwKMkVN4erJNRFx4hKyT7DSkghLXYprVcY3B_2GBZZy_XyCAj9S8RNftAHLkFcz2x5SD-xx1KyM_d0o5SCI4nnls5gERM4xbgXw_PMP3j3TfVE6kcJifGk6ZJZX4PWBEahY3jTm_K1sCDgugUsgLBAxYF75noqL_kp5Jg4zblvKA_sCf_UYWRnQK734LOWBo4QB7jbu8VGE9M2mTDCQnvx-A5h4N1JNv2RzmoppW-Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=oQqYpaEnDhFzYTzKhwPiOTOJyoNlEAiLygaiYSBGIGCKNbqve8u2gBvUlR3O6FQvjKMQ478qiBaheQjowR2-LxjacUzcyXEayhQ6C-VQkcOzwKMkVN4erJNRFx4hKyT7DSkghLXYprVcY3B_2GBZZy_XyCAj9S8RNftAHLkFcz2x5SD-xx1KyM_d0o5SCI4nnls5gERM4xbgXw_PMP3j3TfVE6kcJifGk6ZJZX4PWBEahY3jTm_K1sCDgugUsgLBAxYF75noqL_kp5Jg4zblvKA_sCf_UYWRnQK734LOWBo4QB7jbu8VGE9M2mTDCQnvx-A5h4N1JNv2RzmoppW-Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها موشکی ساختند که قادر به هدف قرار دادن اروپا بود و به آن بسیار افتخار می‌کردند. امیدوارم اروپایی‌ها متوجه این موضوع باشند.
هدف ایران این بود که در پناهِ سپرِ موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.
اگر آن‌ها موفق می‌شدند، آن رژیم شرور آزاد بود که تا ابد به گسترش وحشت و مرگ بپردازد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72052" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=baGit6XGqRZGZF5bAW_U095aRNujY_ZFEq42DJaOmWAdkH2e89bc-onQQMWGkI4A-lT-8yp4G7U35MI0ShZDqqOQBJlO1pNYLKShmRWhRyCbns0Ng1Be-kgfqJK-4Nlcdj81_N6MI5X3QO6rAqDE2oklG_4vLGxHs0N59vUXl2A2irYT-kyfVZM8IFV1qHMPnPJ5spbX9ArQv88w1cxf6rHbSfGWJuAJOKXxnobGzw4Q0aYyAKkRc_kTLl5_QFXY5ru-EZ2mn3ClFzVA8J57Axdv3MbZB8VFAkAvc54UPIjmLkPko9Xxdd_Rjh2JBlr0WXqRC9Xn0OF1cbfOp4ESEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=baGit6XGqRZGZF5bAW_U095aRNujY_ZFEq42DJaOmWAdkH2e89bc-onQQMWGkI4A-lT-8yp4G7U35MI0ShZDqqOQBJlO1pNYLKShmRWhRyCbns0Ng1Be-kgfqJK-4Nlcdj81_N6MI5X3QO6rAqDE2oklG_4vLGxHs0N59vUXl2A2irYT-kyfVZM8IFV1qHMPnPJ5spbX9ArQv88w1cxf6rHbSfGWJuAJOKXxnobGzw4Q0aYyAKkRc_kTLl5_QFXY5ru-EZ2mn3ClFzVA8J57Axdv3MbZB8VFAkAvc54UPIjmLkPko9Xxdd_Rjh2JBlr0WXqRC9Xn0OF1cbfOp4ESEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
سال گذشته، پس از آغاز به کار، مذاکراتی را با ایران آغاز کردم و به آن‌ها پیشنهاد دادم که در ازای پایان دادن به برنامه هسته‌ای و حمایتشان از تروریسم، از همکاری کامل اقتصادی برخوردار شوند.
اما آن‌ها نپذیرفتند. این اشتباه بزرگی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72051" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=AZsjyPg3_mYlcWxhoRaL74vCuxUP5x8mksL-qJtIu3Bcdqh8tjM0DDa5t_LMps7Z2rtoXIxo9dFGVDtEwjn4HM0u1rdeSZCvOtnhp8t2cd2639ab9Tweh_JCpXow5_cuA62x2rGryXaI2SWSBlPDZkW-qxsE4WONGXs22qvnByhO3LhxMGzctFXu7UFbim5ANQn5KZr8Y8qMkFszkhKVYLE6tzwl1Sf9kNGxZpCdLT2C2CXc_KcUiCL9EsJtZgE6w9tDX5lUDqfHYfJdjG3wQWaKNmiYk32YO1gjxyheEhHQC-8y02NjLt-J4MDyPnihTSx2G3Q7ANP9LmDDBrksAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=AZsjyPg3_mYlcWxhoRaL74vCuxUP5x8mksL-qJtIu3Bcdqh8tjM0DDa5t_LMps7Z2rtoXIxo9dFGVDtEwjn4HM0u1rdeSZCvOtnhp8t2cd2639ab9Tweh_JCpXow5_cuA62x2rGryXaI2SWSBlPDZkW-qxsE4WONGXs22qvnByhO3LhxMGzctFXu7UFbim5ANQn5KZr8Y8qMkFszkhKVYLE6tzwl1Sf9kNGxZpCdLT2C2CXc_KcUiCL9EsJtZgE6w9tDX5lUDqfHYfJdjG3wQWaKNmiYk32YO1gjxyheEhHQC-8y02NjLt-J4MDyPnihTSx2G3Q7ANP9LmDDBrksAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند.
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد  ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72050" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=Pu_Utxd-Zl16Pz1PIhWYoK0_2kZnzWxAhH2c8NmtFSWoz46BjBbfxcuysH9YIyZ6c5y_MXhlSL3JtihkhYe1GeEDpaQ59rmrmgzI5wxQR_cxhfsRFuV9suxd9-_tSuQdGcd2bMU9VJy42RfNDXfuh07nCq-DUNmL65PLrlUAIglUGrdCByKfECZ1GbRhuo-SXI_wv6_xRMWe3NoFzENzupNsz1yMG5uUPHjg1JgZcdNHjMz3OGuGURCVg4-4eZb0LbJ9FM2szJ_cmK92nxsrkLWjSDlCjx6D6fScp2v0GBodeMzYe0X51qy0rpcrPtkOMexR3kVMLI4qVZDzYBS-1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=Pu_Utxd-Zl16Pz1PIhWYoK0_2kZnzWxAhH2c8NmtFSWoz46BjBbfxcuysH9YIyZ6c5y_MXhlSL3JtihkhYe1GeEDpaQ59rmrmgzI5wxQR_cxhfsRFuV9suxd9-_tSuQdGcd2bMU9VJy42RfNDXfuh07nCq-DUNmL65PLrlUAIglUGrdCByKfECZ1GbRhuo-SXI_wv6_xRMWe3NoFzENzupNsz1yMG5uUPHjg1JgZcdNHjMz3OGuGURCVg4-4eZb0LbJ9FM2szJ_cmK92nxsrkLWjSDlCjx6D6fScp2v0GBodeMzYe0X51qy0rpcrPtkOMexR3kVMLI4qVZDzYBS-1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من هیچ تمایلی ندارم که اجازه دهم خطرات، حتی یک روز دیگر هم رشد کنند. من به اینکه بگذاریم مشکلات وخیم‌تر شوند، اعتقادی ندارم؛ چرا که حل آن‌ها دشوارتر می‌شود.
بنابراین، در حالی که دیگران حرف می‌زدند، من عمل کردم.
در حالی که دیگران از صلح سخن می‌گفتند، من صلح را محقق ساختم.
در حالی که دیگران تهدیدها را نادیده می‌گرفتند، من با آن‌ها مقابله کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72049" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=XHd_TjGjwEisLIo2xWwwUTm8beK9n7cTgUDPslKS6B76ZW4FJ1fx0FEQYjIRTitKoySfetn69cWwboHOOuhBoDUozP9CgryIniu88LDNvs4C0eTT32rRmrduARargBbJmjskBKsgNiMHn_CTM2BRlRfK2wmYoBTpbGcUNU89Y98GOzfS7XLIoOyXbDqpVMDwquZPP-6KutIdCtdamtVOaNFzpD9z6jYj1b-EhMjIdr7dQduHd5hen5o6St5rIzS1tvHVJZPrFJiTXpdteWJX0fPkCSpjCQQu-o1fZ_T6Ak1kTtPZq7gH9hnGcuC3TYXPPixP1e3sjwC2kBLGlFUuNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=XHd_TjGjwEisLIo2xWwwUTm8beK9n7cTgUDPslKS6B76ZW4FJ1fx0FEQYjIRTitKoySfetn69cWwboHOOuhBoDUozP9CgryIniu88LDNvs4C0eTT32rRmrduARargBbJmjskBKsgNiMHn_CTM2BRlRfK2wmYoBTpbGcUNU89Y98GOzfS7XLIoOyXbDqpVMDwquZPP-6KutIdCtdamtVOaNFzpD9z6jYj1b-EhMjIdr7dQduHd5hen5o6St5rIzS1tvHVJZPrFJiTXpdteWJX0fPkCSpjCQQu-o1fZ_T6Ak1kTtPZq7gH9hnGcuC3TYXPPixP1e3sjwC2kBLGlFUuNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
با افتخار به شما اعلام می‌کنم که آمریکا بازگشته است و کشور ما امروز قوی‌تر از هر زمان دیگری است.
اقتصاد ما مایه غبطه جهانیان است. ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما بی‌همتاست و ما تقریباً در همه زمینه‌ها پیشتاز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72048" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنرانی دونالد ترامپ درمجمع عمومی سازمان ملل متحد در نیویورک آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72047" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دیدم که مراد ویسی گفته احتمال اینکه پزشکیان و عراقچی رو تو آمریکا مثل مادورو دستگیر کنند غیرممکن نیست
آدم می‌مونه به این تحلیلگر چی بگه
😐
🧠
#hjAly‌</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72046" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=ipmgyK06bAKElA-CT3NsEEozB6IdXMZkymN9TjASkE8c5NAdZ8ldtXfloWeC-a6f9FzPl1EdcvNBr4k_wuo-wk_rnUtznmUVkpi9UmAzrUwSsXeUcop_qfZXToZhXroskYlRdHX6XDeFmMixdHft1pOZAvznzzM69ejkhR_64KNAEGijPvn5KUAaJL4Xhvy-j9HAh9vu9-zKR3jPLpVxNut414xqwMxMvc9sLAPDF4GBvocHm1dxH-IVhdffaGHrD-3-317377wNo1JmaKq4AWy1W3460oxn0DxINd2DJiLqXgQ-hZLSPJs6dsXZAVphDJ7USKVH48R8G2OyN8ZKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=ipmgyK06bAKElA-CT3NsEEozB6IdXMZkymN9TjASkE8c5NAdZ8ldtXfloWeC-a6f9FzPl1EdcvNBr4k_wuo-wk_rnUtznmUVkpi9UmAzrUwSsXeUcop_qfZXToZhXroskYlRdHX6XDeFmMixdHft1pOZAvznzzM69ejkhR_64KNAEGijPvn5KUAaJL4Xhvy-j9HAh9vu9-zKR3jPLpVxNut414xqwMxMvc9sLAPDF4GBvocHm1dxH-IVhdffaGHrD-3-317377wNo1JmaKq4AWy1W3460oxn0DxINd2DJiLqXgQ-hZLSPJs6dsXZAVphDJ7USKVH48R8G2OyN8ZKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:پیامی که می‌خواهید به پوتین منتقل کنید، چیست؟
ترامپ: این جنگ را متوقف کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72045" target="_blank">📅 17:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=q-MSMKriNj5LEv9y7d8EN34e0Enf4hwdQslL-YjkxOi5YaTRnvWVHqUbLQPwV5ogT5hXc4BnvTdO7TL-3r_2K5u4DLqnoVFasJTVnaWwnIzGyE5ApksoWB9I-Ohjb-tpIK1-Mce_7Ah0zEE2yg7jcf5C-M28RAkqmLLYlbWJrZR38qsUek4OTJRxZnVtXs1WEs3OPnvacfzmpjPrdC2zDOi0G-zNI7g5cArTgZz9fuoHvWyU9NwCxTLBBNNTnax93k1KvdHfjGX2LN1WaEhM2Aa6uOuS_OdFRJ3NM-WJ1KEzaRzUkXPYnQ5lEfKl-V74oQSEAhf62Al6lBoSrgvC7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=q-MSMKriNj5LEv9y7d8EN34e0Enf4hwdQslL-YjkxOi5YaTRnvWVHqUbLQPwV5ogT5hXc4BnvTdO7TL-3r_2K5u4DLqnoVFasJTVnaWwnIzGyE5ApksoWB9I-Ohjb-tpIK1-Mce_7Ah0zEE2yg7jcf5C-M28RAkqmLLYlbWJrZR38qsUek4OTJRxZnVtXs1WEs3OPnvacfzmpjPrdC2zDOi0G-zNI7g5cArTgZz9fuoHvWyU9NwCxTLBBNNTnax93k1KvdHfjGX2LN1WaEhM2Aa6uOuS_OdFRJ3NM-WJ1KEzaRzUkXPYnQ5lEfKl-V74oQSEAhf62Al6lBoSrgvC7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ورود به مجمع عمومی سازمان ملل خطاب به سی‌ان‌ان:
تعجب می‌کنم که سی‌ان‌ان اینجاست تا اخبار مربوط به مرا پوشش دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مرا پوشش دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72044" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72043" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbzbrZaCETDpTBEWRRHEmrOtwh8zaydO7_nIG8wEZb_zKyZnrp7pbpNN1Uj3I9y0-UNQz4GC5fALk7jjIxFFjQn_r9XkqJoUbYe0NO06dVkAob4LhFD9xchFpVJ6BM3d-GzC-iRR12MaaUeFUsRKHxhYz54Wc--P1aJP7lxxfPZVggCBrSWQ1OYFKmBo1i9Ut5liKPLy8FJYnivZmEwG-AivLfPV5k47hmBoQAD0pbLc80lXjpWchlgpUDhEjDC4BG11Eno3wPn2O4nB-CiHFqsie2O2KNOZdmreHl2IVzz7T2Tgxq-L5CTKkUrsKRSNmrqIwcE2RDByNLoWE-HmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72042" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=hVR77yWrnZL4rvD6S-IwB844mKxurNN59wuyoWgxwSRRnfM_iUDhIicWKwEBxX2VK1pUlOJKiScYympmiRpXsXn7PcerJx1YRdWvVtvc6F9fPSC_FiaAaaKpArRccs2QBz9oD75r1J7MPkUESJFjx0xntWxHLv-arUJvnQlra__UC4vibdhZbyyRWjGReKgLQypw1BZlP8_DdAez2ciSdTgG2zo5ktM9W4qYTILtwe8qMfIzSNJLUABnthnGbKUWVpa9jCetpyeGtNe4ctjVbiFujV2m5A67aNLWvAZzwOwDdRWiyXVge8u9KrY2O_lr-pT0aC3yP7zsOTJ5sypDZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=hVR77yWrnZL4rvD6S-IwB844mKxurNN59wuyoWgxwSRRnfM_iUDhIicWKwEBxX2VK1pUlOJKiScYympmiRpXsXn7PcerJx1YRdWvVtvc6F9fPSC_FiaAaaKpArRccs2QBz9oD75r1J7MPkUESJFjx0xntWxHLv-arUJvnQlra__UC4vibdhZbyyRWjGReKgLQypw1BZlP8_DdAez2ciSdTgG2zo5ktM9W4qYTILtwe8qMfIzSNJLUABnthnGbKUWVpa9jCetpyeGtNe4ctjVbiFujV2m5A67aNLWvAZzwOwDdRWiyXVge8u9KrY2O_lr-pT0aC3yP7zsOTJ5sypDZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره چندین دوس پسر داشته ده ها بار باهاشون رابطه ی جنسی داشته حالا اومده پیش متخصص زنان تا گواهی بگیره به نامزدش نشون بده پردش ارتجاعی بوده و سر اون پسر بیچاره کلاه بذاره.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72041" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=WsSp6mc_x1sJuD91yB3HJbBfbygrt6mANwxvS1TILCXYZRZFVkjj4hma9dELY7703jCYqEKHU6VHJJg_32QdcXSvAcY4II9rORaMQOPax2op3_gMRn66djSu4S2ps10Vqx6qY1Ygj26gWV8ard2tR3MfLqnez89Jtg2pEQ6TVd8fE6Bu3sv1svFFXBEDVNcSxY-WKw4SkXBxoe9ONcSjDjBwq7N_9hdOnDSs6SRBgl_CnDm9N7RUi2cGquTEhQ09BUOphQ_7wRf5uOBjjf7jHz01hTBh0xA3Ljn0szmaJ0R3FJcvg9GUgagHaMNpL_HFEmgmfuJfLN0-n1L-HLEK5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=WsSp6mc_x1sJuD91yB3HJbBfbygrt6mANwxvS1TILCXYZRZFVkjj4hma9dELY7703jCYqEKHU6VHJJg_32QdcXSvAcY4II9rORaMQOPax2op3_gMRn66djSu4S2ps10Vqx6qY1Ygj26gWV8ard2tR3MfLqnez89Jtg2pEQ6TVd8fE6Bu3sv1svFFXBEDVNcSxY-WKw4SkXBxoe9ONcSjDjBwq7N_9hdOnDSs6SRBgl_CnDm9N7RUi2cGquTEhQ09BUOphQ_7wRf5uOBjjf7jHz01hTBh0xA3Ljn0szmaJ0R3FJcvg9GUgagHaMNpL_HFEmgmfuJfLN0-n1L-HLEK5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو تحلیلگر و افسر سابق سیا؛
اسرائیل با پرداخت مبالغی در حدود ۱۰۰ دلار، هزاران شهروند افغان را در ایران برای فعالیت‌های جاسوسی به خدمت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72040" target="_blank">📅 17:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تو نمایشگاه خودروی تهران که تازگی تموم شد، تنها کاری که مردم نکردن بازدید از خودروها بوده ؛
جکِ ماشین رو برداشتن، با خودکار رو کاور ماشین کشیدن، با مشت زدن رو کاپوت G700، کارت استارت ولوو رو بردن، شید سقف ماشین رو خراب کردن، خار دستگیره در رو گاییدن، دوربین جلوی ماشین رو کندن، جکِ کاپوت رو کندن، با خودکار رو صندلی ماشین خط انداختن، دکمه صندلی رو شکوندن...
‌
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72039" target="_blank">📅 16:34 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
