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
<img src="https://cdn4.telesco.pe/file/QpmZhgW3Oo61YG57OTGI19WIx3K8XlK3z1QpG-rhYy2ndHUDgbGgVVlzQeqpZOu5C_RRKsEvkrVCand1HpKUyKydVHFK-xPZDEYail3zpYBMKFj76lYopZsNWmF3-y1g0LvWwt4luOBY0aO98KDqit3zpcumvntSXYy0YeALRAq_nW4hNPgxGBx5iVRz08cMTu4DsioFoMKF5hxH_LVyOD8VoQneQzB31ChGjd843hySFuVLX0fCOx3z24US8QXKjX8isnCVuy6Rt8bDpi0DoBz6YO-h4obbIalDXloRrL8HWEEEIaiWu34ylSp4OEDPC_yN13-4JYq_scK_wQRSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-670022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع خبری از شنیده‌شدن انفجارهای شدید در کویت و بحرین خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/670022" target="_blank">📅 08:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZf4VVy6b56ynEsZsYw08oFDJICVPob7Z49D5_ldSTnWvVAmjY-sPGiYh6BG-TnzlwKbZj1_n6YClf0jFzcqiYY2O1XyUIHekW_Ioc7osnG8NLSsmi5ozBOoOKqAGu80AxX1qSAerWXdez0tvfiQklE1pjzPUOVoVy60Sk924sZEi0SUTS8owtqc6K8HCpDszYjOSGXPYCOdo5KqWqHZy9Xuy2DwG8NCBVOmLGz4Glcrt-P94IMhAssvY7UI0kjQawkAW0eMdpwX8xW8vI4-mBOl2k67kqQVd37YhusfImLETIALladFO_07PrM57LD4CWD8l4YSakWIVULjiZTYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیر سابق قطر درگذشت
🔹
دیوان قطری اعلام کرد که شیخ حمد بن خلیفه آل ثانی، امیر سابق، درگذشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/670021" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
منابع قطری: حملات شبیه روزهای اول جنگ است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670020" target="_blank">📅 08:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670019">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e1a10341.mp4?token=a1J91gUCkyYo9xN9x-qmsMGcSWkh4he0XakPVL3w9n-Wq7e6_9-TKKoXZMxn4LwOHxzkicm4nsnSDe0sHkaaHEcBFpZ2wyTEiM4WuoOTnR5u0K8CwCw3xObbNIxQPsGSdgo8yBmLxL5ibgtl7j3pMZnUUbczh3RB4gN_ttvP1NehYSFNVxXfMXzmyi3uUXt3GzRbaNHnlUd8rt1af_E3QvKrKK7ImUPjZz_7zzmBtR31xxeJ6_KgERpqhicfEIPmdxvHnaSG35FChnvDiwze0ETpKHDWJPsZmX8oT0k9WM_-Tvr5pk8Iu5x7hru2acnKRxRBEDDn7FgtJG7arAn6Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e1a10341.mp4?token=a1J91gUCkyYo9xN9x-qmsMGcSWkh4he0XakPVL3w9n-Wq7e6_9-TKKoXZMxn4LwOHxzkicm4nsnSDe0sHkaaHEcBFpZ2wyTEiM4WuoOTnR5u0K8CwCw3xObbNIxQPsGSdgo8yBmLxL5ibgtl7j3pMZnUUbczh3RB4gN_ttvP1NehYSFNVxXfMXzmyi3uUXt3GzRbaNHnlUd8rt1af_E3QvKrKK7ImUPjZz_7zzmBtR31xxeJ6_KgERpqhicfEIPmdxvHnaSG35FChnvDiwze0ETpKHDWJPsZmX8oT0k9WM_-Tvr5pk8Iu5x7hru2acnKRxRBEDDn7FgtJG7arAn6Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکرمی‌نیا: سخنگوی ارتش: به مداخلات دشمن پاسخ کوبنده دادیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/670019" target="_blank">📅 08:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670018">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ea758fdb.mp4?token=DPSTNd3Ne9dZtjwzBi6PBmeNnSKgZvIVYriMlfSINfkWPBzbmUMYpOVSHhB9XfwrG83zoWcZEoBRoFWPHjbvoQP3_DCmEyMsnxjb41SSqgYzw08Eu4s7OzOWxTmTzpWIJef3y1qrXqJCFYchuZRnhz3uLF5Iy4P3ZZkACNgSFwdc7_wbsRaApbo0BZQM3PCmsnXmn-PjBfYa3qtLYuHqy6R1zwy0Rds-PsG8oFl81SuVjgGZjBQxIgxE4tb7FvtG4exnWG0LuKWg7kbOJ4QD11KrVcDs1uVoBcZFrVEwkXqrQQ4MXdrkUzGcXdbjX2HaVV-GMPnW2PwU4JPbvFniiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ea758fdb.mp4?token=DPSTNd3Ne9dZtjwzBi6PBmeNnSKgZvIVYriMlfSINfkWPBzbmUMYpOVSHhB9XfwrG83zoWcZEoBRoFWPHjbvoQP3_DCmEyMsnxjb41SSqgYzw08Eu4s7OzOWxTmTzpWIJef3y1qrXqJCFYchuZRnhz3uLF5Iy4P3ZZkACNgSFwdc7_wbsRaApbo0BZQM3PCmsnXmn-PjBfYa3qtLYuHqy6R1zwy0Rds-PsG8oFl81SuVjgGZjBQxIgxE4tb7FvtG4exnWG0LuKWg7kbOJ4QD11KrVcDs1uVoBcZFrVEwkXqrQQ4MXdrkUzGcXdbjX2HaVV-GMPnW2PwU4JPbvFniiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدون وسیله شکم و بدن‌ات رو فرم بده
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/670018" target="_blank">📅 08:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069e8a600e.mp4?token=ET7w4YGdL_lnnA_orIri3SfIDB6Q4MwfZbb7iOIkmtz8ekNGFlhH_heUl4VnUZ56GT4QOBfNks9EFfAJtTkg0rCvpUBUN7FylWJRlaYj0OMWpnCAQrIXT0UMoDDOrbXWfvr7yCo5bXaJx4qnnBSR3MKV_1vBTj9jZifal9pFVUZ-IZiwfLZiDIxqAQHiY-XVZPNo_aAhwx-att7d3afQ2fOA4VLTU9ckO-rhrDMfwE6vKHuH16EdxRrcXJBMI1hMCpmvBGwkSZCN-VodoryqaadoaNY4yUPvzgOGlkHIUHrGMfL4ER4rVcv7huum0mM-75yVuYT_m_jYlb_OfJVApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069e8a600e.mp4?token=ET7w4YGdL_lnnA_orIri3SfIDB6Q4MwfZbb7iOIkmtz8ekNGFlhH_heUl4VnUZ56GT4QOBfNks9EFfAJtTkg0rCvpUBUN7FylWJRlaYj0OMWpnCAQrIXT0UMoDDOrbXWfvr7yCo5bXaJx4qnnBSR3MKV_1vBTj9jZifal9pFVUZ-IZiwfLZiDIxqAQHiY-XVZPNo_aAhwx-att7d3afQ2fOA4VLTU9ckO-rhrDMfwE6vKHuH16EdxRrcXJBMI1hMCpmvBGwkSZCN-VodoryqaadoaNY4yUPvzgOGlkHIUHrGMfL4ER4rVcv7huum0mM-75yVuYT_m_jYlb_OfJVApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم آرژانتین به سوئیس/ آرژانتین در مسیر تاریخ‌سازی، سوئیس را به خانه فرستاد و حریف انگلیس در نیمه‌نهایی شد
🇦🇷
2️⃣
🏆
1️⃣
🇨🇭
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/670017" target="_blank">📅 08:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf0663d3a.mp4?token=C-sOIn0LmJVZNykFTclJ2tOn-WtdfFGMsm4QKv40EuQuc2EaTu5E-OTLs-JINXUZtviJqYs2mbVP_Dgz2EPPZoAOCm-jYNc6HfiTE82wNUJwgc2flMYNeo2vFGMk08LUHYdZAOz1QZEDxfy3IYulqPhMrDjWrQbwf5APf8nmNezl4Xkz3ZeSs3xn4kdEYr7uMJ7l5zjimvbSvPdg-toVPg1XMzUIW55a5gI2oykv5PTrE5xT39GQ1Jg_GPozapjvGPOSHC5o3ytwoKtV88FcrBwtTrGMaxza7r_Q0EMBHuL9fomwx4UxIlP9hs5lr2HF648X265f0_AEHGf_qOdbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf0663d3a.mp4?token=C-sOIn0LmJVZNykFTclJ2tOn-WtdfFGMsm4QKv40EuQuc2EaTu5E-OTLs-JINXUZtviJqYs2mbVP_Dgz2EPPZoAOCm-jYNc6HfiTE82wNUJwgc2flMYNeo2vFGMk08LUHYdZAOz1QZEDxfy3IYulqPhMrDjWrQbwf5APf8nmNezl4Xkz3ZeSs3xn4kdEYr7uMJ7l5zjimvbSvPdg-toVPg1XMzUIW55a5gI2oykv5PTrE5xT39GQ1Jg_GPozapjvGPOSHC5o3ytwoKtV88FcrBwtTrGMaxza7r_Q0EMBHuL9fomwx4UxIlP9hs5lr2HF648X265f0_AEHGf_qOdbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دشمن در شهر بوشهر ۷ پرتابه در پایگاه‌های نظامی و در شهرستان دیر ۵ پرتابه و در عسلویه ۴ پرتابه شلیک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/670016" target="_blank">📅 08:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d713fb7371.mp4?token=vWIHFBWfvoPz1Ui6jyanq7d09CDKj26-S342avGwsdriGMUh1-lY1qu7l4sLcqhZTS6JQsywkvjtLjXe6m8xNHo48tCYcBFLSlcTozbI82Y1sS4h70TOs4hRpb6RyiJRi2ecfUhtCasbf8KoPKXfVtNTzwlWMn-ZxprVE9AbkFIrx-5FJMR0QrO6eA9QmTHB00VeV1bUwq8O7LB_zoL5TJOU6k7kuyGJF6Sno9Ncy-qW8mT4IhrUxG4ASkOa2gXtKTQHVeT3QeNah_lDBN_5R4WvalpC6fQGC7hrZPKTAsIDAnbAFaHGG__l437K-DSvpjDGgA2bXySdAdC8btJgxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d713fb7371.mp4?token=vWIHFBWfvoPz1Ui6jyanq7d09CDKj26-S342avGwsdriGMUh1-lY1qu7l4sLcqhZTS6JQsywkvjtLjXe6m8xNHo48tCYcBFLSlcTozbI82Y1sS4h70TOs4hRpb6RyiJRi2ecfUhtCasbf8KoPKXfVtNTzwlWMn-ZxprVE9AbkFIrx-5FJMR0QrO6eA9QmTHB00VeV1bUwq8O7LB_zoL5TJOU6k7kuyGJF6Sno9Ncy-qW8mT4IhrUxG4ASkOa2gXtKTQHVeT3QeNah_lDBN_5R4WvalpC6fQGC7hrZPKTAsIDAnbAFaHGG__l437K-DSvpjDGgA2bXySdAdC8btJgxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلند شدن دود از پایگاه آمریکا در بحرین، پس از حملۀ جدید ایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/670015" target="_blank">📅 08:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ناوهای آمریکا از ترس موشکهای ایران عقب‌نشینی کردند؛ فرماندهان پنتاگون دستور فرار صادر کردند
فاکس نیوز:
🔹
فرمانده ارتش و هگست در حال دستور برای عقب نشینی ناوهای آمریکا هستند تا مورد حملات موشکی قرار نگیرند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/670014" target="_blank">📅 08:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزارت کشور قطر از ادامه‌دار بودن حملات موشکی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/670013" target="_blank">📅 08:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حمله هوایی به شهر ویسیان در لرستان
معاون سیاسی امنیتی و اجتماعی استاندار لرستان:
🔹
صبح امروز یکشنبه، شهر ویسیان از توابع شهرستان چگنی دو بار مورد حمله هوایی دشمن قرار گرفت.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/670012" target="_blank">📅 08:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cebf40c099.mp4?token=gT6_d4kXL0L8sIO9dmZDgoz_LPZZ73-lDhamQBRKWHczT2bnXA6i6QeoHYWATxQJ1YSNQP5jfTDixLiTpbWnJ82v-KzbUrNPmTyUtpcnOqzq7bszWozh-f38TUWM7o-0Kkja4KWDwW1c9a6IMmexY8gDD85B4CRghjUTg2-TcrUDWl70NyEJGOY2GKkNNS3FKWcUNoe1RzGPK9r1KFL5abQHvUcT5FnmoVVbTrhujcpRrRHI0S1O5vTWJJ-vkVSIMpisFEjW8Ke6GV1iVwY3DP7GZXwGFVHSTGcqjR-rZ2da2fsDs8dzQiZDawSagf0hr6X0AswGWde4UkExov4fhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cebf40c099.mp4?token=gT6_d4kXL0L8sIO9dmZDgoz_LPZZ73-lDhamQBRKWHczT2bnXA6i6QeoHYWATxQJ1YSNQP5jfTDixLiTpbWnJ82v-KzbUrNPmTyUtpcnOqzq7bszWozh-f38TUWM7o-0Kkja4KWDwW1c9a6IMmexY8gDD85B4CRghjUTg2-TcrUDWl70NyEJGOY2GKkNNS3FKWcUNoe1RzGPK9r1KFL5abQHvUcT5FnmoVVbTrhujcpRrRHI0S1O5vTWJJ-vkVSIMpisFEjW8Ke6GV1iVwY3DP7GZXwGFVHSTGcqjR-rZ2da2fsDs8dzQiZDawSagf0hr6X0AswGWde4UkExov4fhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به سوئیس توسط خولین آلوارس
🇦🇷
2️⃣
🏆
1️⃣
🇨🇭
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/670011" target="_blank">📅 08:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5QxNoRDdQ1t7zwfvdEsNbmkPI4JWfOXF4Hh3BWuWjxx46jKfdOmeG9kK8pzJk1fzLr0fHmSBcl-JMa8rBcjA3oKs-FVIvPjkP1Zkc4LVzfQ1yyymQeNvdH46zrQ9gOaAKgPsBRauLs1ZEvfKdsvB7Ci6tlh_hPL7c9O5SMoE9NuJPfLzOyDRBzMbux4Jl4EBBdWwxEXAdxozcIMxxsM8p9zisfOC6EvMNjZoPsIo9Euemc6HEXrG6PwpL76N6BWGBvr9b6fVh0I61hiZ6hzm6bAMB0iqiABBSciEjmqXSkGp0DvNinJGbdElIIuMMsep95gAI0OoBx3_5NP2A7nSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: دوران توافقات یک طرفه تمام شده است؛ به تعهدات خود عمل می‌کنید یا بهای عمل نکردن را می‌پردازید
رئیس هیأت مذاکره:
🔹
دوران توافقات یک‌طرفه به پایان رسیده است. به شما گفته بودیم: به قول و تعهداتتان عمل کنید، وگرنه باید بهایش را بپردازید. حالا باید با واقعیت روبرو شوید.
🔹
قالیباف همچنین بخشی از بند پنجم تفاهمنامه ۱۴ بندی را که در آن بر بازگشایی تنگهٔ هرمز با رعایت «ترتیبات ایرانی» تاکید شده است،  در ضمیمه توییت خود منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/670010" target="_blank">📅 08:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS7OwHtZhVe-_eVCLJCWE6a0MXGq7ucu96SK-sw4um20AqkH0fjEcTd9uGX80KHuE87GSI8zr8G3YADzl5EtNsF1O62eIb1oJ__ZQudtLAanwLcw-8jY8mCbWbqXJrcXcS9js9u_M_H0Pq_E6ITegvzIHE3vh4yPfbmqt-v_dSq10an88K0v2KxIDJB2XvCWcHD_BFTz_0UGeEqrUmE2JvWoHSlFxdHCLjkc9cIqk4yEo1F6GFaz0pex7Nm7lDjgcDOUZqZqiVnAYi2bD2pVAc0eHXiuZxvUNRfEvWMrkkDpvIviDsuf-vD9SFvuWfteF6g-bdPFIyBOIdFj3eLOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود
🔹
کویت حمله موشکی جدید به این کشور را تائید کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/670009" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670008">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">شنیده‌شدن صدای انفجار مجدد در بحرین
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/670008" target="_blank">📅 08:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670004">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ارتش به آمریکا: تفاهم‌نامه را تمکین کنید/ مداخلات شما در تنگه هرمز ناامن‌کننده است
سخنگوی ارتش:
🔹
مداخلات آمریکا برای ایجاد مسیر غیرقانونی در تنگه هرمز باعث ناامنی شده است.
🔹
نیروهای مسلح مقتدرانه از حقوق مردم ایران در تنگه هرمز دفاع می‌کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/670004" target="_blank">📅 08:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670003">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود
🔹
کویت حمله موشکی جدید به این کشور را تائید کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/670003" target="_blank">📅 07:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670002">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92140e47c5.mp4?token=KPlACI77hqG8cDDrNZDuqZqkPsd6cxQ-PFZ5l1lZRHJcAd-JbpvR112kXtl3GJzN9G85WIa36ImLKmflpqVZWhMHo0Ss5uvtxlixQ23C5tEKF54Ez47UA1DX_URDzuIDOnOazgil8Ka6LT6Cs-rfkFLZF6BeFTrLij3ekmStxLVTnoqWI9KkUWBKapnlbVvnxWC5D1J_nSUJs5g7V84HrP-Om2TNyAPmfJtzGDT7ALmyi1Gsb-zs4jSQwX5gBfEV9AMrVsKrAXPnsYY6bCV3AKCkKGBxplEuTvO8ymPNAM6FToqUquMhhwJ_OCua9lvctwcxc4l83NRPM6v1NGA_ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92140e47c5.mp4?token=KPlACI77hqG8cDDrNZDuqZqkPsd6cxQ-PFZ5l1lZRHJcAd-JbpvR112kXtl3GJzN9G85WIa36ImLKmflpqVZWhMHo0Ss5uvtxlixQ23C5tEKF54Ez47UA1DX_URDzuIDOnOazgil8Ka6LT6Cs-rfkFLZF6BeFTrLij3ekmStxLVTnoqWI9KkUWBKapnlbVvnxWC5D1J_nSUJs5g7V84HrP-Om2TNyAPmfJtzGDT7ALmyi1Gsb-zs4jSQwX5gBfEV9AMrVsKrAXPnsYY6bCV3AKCkKGBxplEuTvO8ymPNAM6FToqUquMhhwJ_OCua9lvctwcxc4l83NRPM6v1NGA_ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول سوئیس به آرژانتین توسط اندویه
🇦🇷
1️⃣
🏆
1️⃣
🇨🇭
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/670002" target="_blank">📅 07:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670001">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار در قطر و بحرین هم‌چنان شنیده می‌شود
🔹
کویت حمله موشکی جدید به این کشور را تائید کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/670001" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670000">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a7f25c49.mp4?token=A5wbipsxJOGpvM0FlalWkptDz3JjtR7U91c8xGeWXMTswmp53b8qcolw3wEtsr8LdlKTEsoL1-LNAB9ZoKjZdfBIkJlrtrJOnwEARB98RodiFAzI8teLvKFKtjI3UxqQPyxVMiMrtwFsvRFcS6OVVnu9l7FTjqIyQAbAMA5QOEHlGxbcD_GVO60Czx-Oe7ZNViPmk9P0CULcwOYzyXi3WFtpSO8mKUOL2NmDTxKFeEMLo7O7qDhRzUghHWMZikWHSw2RNYDLE1k2cattMxu7MHbPLCYeoo9Vd7x29cMuY9g1_WvKV9YcN98uKYLjulrmgDVTwsPBHs01w0o5OgTG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a7f25c49.mp4?token=A5wbipsxJOGpvM0FlalWkptDz3JjtR7U91c8xGeWXMTswmp53b8qcolw3wEtsr8LdlKTEsoL1-LNAB9ZoKjZdfBIkJlrtrJOnwEARB98RodiFAzI8teLvKFKtjI3UxqQPyxVMiMrtwFsvRFcS6OVVnu9l7FTjqIyQAbAMA5QOEHlGxbcD_GVO60Czx-Oe7ZNViPmk9P0CULcwOYzyXi3WFtpSO8mKUOL2NmDTxKFeEMLo7O7qDhRzUghHWMZikWHSw2RNYDLE1k2cattMxu7MHbPLCYeoo9Vd7x29cMuY9g1_WvKV9YcN98uKYLjulrmgDVTwsPBHs01w0o5OgTG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به سوئیس توسط مک‌آلیستر
🇦🇷
1️⃣
🏆
0️⃣
🇨🇭
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/670000" target="_blank">📅 07:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669999">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای جدید در کویت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/669999" target="_blank">📅 07:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669998">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چندین انفجار پی‌درپی در قطر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/669998" target="_blank">📅 07:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669997">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8c23df8c.mp4?token=jUj0AIKhrj_m1YEvptarL4ep10m2hDxOb9pvMTJ1GECtY8AMpZ0a1Js8I3KMc3p3c3lSqsWMYjDTVc4-aVG04pOLH8L12aJPT4asR1-bwzM0jSRhIw3wSm_LxRXOg3fvPAM_58a81UcjqkXSl4QZcSUXAucg6gG4J21RmPQZ0xyJgDuuj8I2dh3ZYx2lVM7V5gCOpMnRbfPq7sZZ4KsZFYKmb6wRBrYjttMl27kNx442HoMPB7OBzyCuxM3rOt-u__IkjKA9MM9kJ_eu9MF5Xw-zLJe5dhW-uT1bwTThf0jRLkjFnEGegNKNxrJyP9iVxl75wg8Tvv7Oi7kttJbYGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8c23df8c.mp4?token=jUj0AIKhrj_m1YEvptarL4ep10m2hDxOb9pvMTJ1GECtY8AMpZ0a1Js8I3KMc3p3c3lSqsWMYjDTVc4-aVG04pOLH8L12aJPT4asR1-bwzM0jSRhIw3wSm_LxRXOg3fvPAM_58a81UcjqkXSl4QZcSUXAucg6gG4J21RmPQZ0xyJgDuuj8I2dh3ZYx2lVM7V5gCOpMnRbfPq7sZZ4KsZFYKmb6wRBrYjttMl27kNx442HoMPB7OBzyCuxM3rOt-u__IkjKA9MM9kJ_eu9MF5Xw-zLJe5dhW-uT1bwTThf0jRLkjFnEGegNKNxrJyP9iVxl75wg8Tvv7Oi7kttJbYGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم انگلیس به نروژ توسط بلینگام/ بلینگام پاروی وایکینگ‌ها را شکست و انگلیس را به نیمه‌نهایی رساند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
2️⃣
🏆
1️⃣
🇳🇴
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/669997" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669996">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Ljk3RQY8EXQiQQRpq3jAFh8uIQva1hfCrBMHF9Xmvb9IllX8_QzakzTN6RnNYc7qK_YVhGMeDR2K4OZAVWVlhIJh-Y0Ptn-ctPZA4TC9OgH6yQ2Rcj64XiRhnl2u8wFgv0-IET2P_dBhoCVmFzDLeV-66RquvtLOyEQh93G7K5Wk2xeoAZG1tgfebr2XBr3NLa9Zk5shB5rgU-JdTemTGZIjky5OjKYYDCq0JIgTZldpWr5J2-0z76Mxxf-DIuxC4MhaseB1wkvKcEshENcclgb5NdgBOzKL29pRAKU5tUvA5iiPuNYY9QpO4YM96LiO2-5vHgzcz3qFJbtsDfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۱ تیر ماه
۲۷ محرم ۱۴۴۸
۱۲ جولای ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/669996" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669995">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حمله به پایگاه امریکا در عمان
روابط عمومی سپاه:
🔹
مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیما بر آمریکایی در بندر دُقم عمان با یک حمله سنگین و غافلگیرانه در هم کوبیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/669995" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669994">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
منابع خبری از شلیک موشک به سمت ناوهای آمریکایی در دریای عمان خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669994" target="_blank">📅 07:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669993">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253e6bb57d.mp4?token=sBIDYwSZojKwj-6g6k57q4DCOvo_VvuT84bU84BT1EZ1fIhsw10eYs0R7CafmplBNK7z6wf2oKKMQ1866rS_erAhj15kEXF8auJCq9Sy8kbtj3zWR14-K25_gdJo_XDbsu_wQGn9qzYDOk_5rbZwRvkoXXm7jnIay9GqTdxh6_HBljiF08h8C2ileK4aq84yYkFZ01i9aCCyCGFDoKo9mgh1QGBbcN8qjA7zIu3WOLRxOdeni5lwDega-uHI65K6AQWD9RpbwV3j-6LANW0IEF-CLQcB-R-jAFxktEegQsDMFo8m9t37csO0JSEuXI2ZdC0gdmiaJ7K0RJLe8x4vtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253e6bb57d.mp4?token=sBIDYwSZojKwj-6g6k57q4DCOvo_VvuT84bU84BT1EZ1fIhsw10eYs0R7CafmplBNK7z6wf2oKKMQ1866rS_erAhj15kEXF8auJCq9Sy8kbtj3zWR14-K25_gdJo_XDbsu_wQGn9qzYDOk_5rbZwRvkoXXm7jnIay9GqTdxh6_HBljiF08h8C2ileK4aq84yYkFZ01i9aCCyCGFDoKo9mgh1QGBbcN8qjA7zIu3WOLRxOdeni5lwDega-uHI65K6AQWD9RpbwV3j-6LANW0IEF-CLQcB-R-jAFxktEegQsDMFo8m9t37csO0JSEuXI2ZdC0gdmiaJ7K0RJLe8x4vtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول انگلیس به نروژ توسط بلینگام
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669993" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669992">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0968545801.mp4?token=qKaB2R1L7E0YqDpiE2TDHjCjEZbqwFDom3GiubRhdrGVRK1tFv9lCYveVnLA3lFY4iOL4bL5YiJaRoS9--Wi1Uz8vAvnQgj5Cpi-jnIWX21YBjwxh1GvEspr1QPj-Nlfxn4m2Ibl5-fH6YHA8RH_vfJ6AhtP2wU8eIQZj0oeTtBQxQLd71kAoCVSNCdZkM0hIRzxRcERi9qHwigjGcmozFIs3XY8c9kaDfiY6Qd8xgQbnhJpqHIdTB0z5tIfzMsUlUvS3KkOK29C8vx5esggpLjd8UKYjQTuKAd-ABEDF9SR6wjURXjfOWxpvwmrFr15FVZoIkeN549LNbv2LV9fOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0968545801.mp4?token=qKaB2R1L7E0YqDpiE2TDHjCjEZbqwFDom3GiubRhdrGVRK1tFv9lCYveVnLA3lFY4iOL4bL5YiJaRoS9--Wi1Uz8vAvnQgj5Cpi-jnIWX21YBjwxh1GvEspr1QPj-Nlfxn4m2Ibl5-fH6YHA8RH_vfJ6AhtP2wU8eIQZj0oeTtBQxQLd71kAoCVSNCdZkM0hIRzxRcERi9qHwigjGcmozFIs3XY8c9kaDfiY6Qd8xgQbnhJpqHIdTB0z5tIfzMsUlUvS3KkOK29C8vx5esggpLjd8UKYjQTuKAd-ABEDF9SR6wjURXjfOWxpvwmrFr15FVZoIkeN549LNbv2LV9fOYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول نروژ به انگلیس توسط شلدروپ در دقیقه ۳۵
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/669992" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669991">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
منابع خبری از شنیده‌ شدن صدای انفجار در قطر خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/669991" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669990">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIMzFayCe6pmLyeo8Wd35it_F0psZDNxy46IA19ZgUwXgX7E-jdGxPSYo_OhHrp-nN6oc_6tkZgG810980Sp524j95NT2JCLbzALqxpop7Cfl0tp7IxDI6GCOvQHtQ4_r8U1ALxD2Cbv8-JDUGRJ8EkH3VQsSbbzyxAn7A09b9lVMGpi9R6eZxq_ubgHMduo-0HgELmUQJl4VUyMEan0umZeblmIlmzNdNw_ypFV6idR7If8Fe5uJFeJQcOnt9HI_lM4Qfqwu9m9CWe-vCmIB_lONLl1ISx0R_fQphCAZdMhX49B66rEQWTcF9RThnTneqDPOxP0TMAzBSoHX60tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بروزرسانی نمودار مرحله حذفی جام جهانی ۲۰۲۶ پس از پایان مسابقات یک‌چهارم
🔹
تکمیل نیمه‌نهایی با فرانسه - اسپانیا و انگلیس - آرژانتین
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669990" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669989">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVp6yicBDSDAJyf-I5s0rKdm7WhdOtBya4jBlaA9zmlHjY_z3owlnEdzXu4Ep8bvdTMryyZKsRE_48FB9KSkS_7DrmauI_uReIlkaX5jZoGcqUV90LgYpriU8xvl4ktv21gW0NBLTc5NMAycWt6rKJaIrRKiKN1GawsqtbycXvQBz002RxVZRkHlDTL-_T_9He5AQDsLmR4LzoSnj4CsiYdaPgspHHaERLWFsGqvFjUrKOISrq82g-XI8HVx8WNuQIzeefvqYTQN9L8hJosylgiATa8uxO7GkDe3dZ2OPbGVxG6aOlfGKQ5xxf2bhjUY0il7gdcNpkdN0B-shW3OtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام ۲۰۲۶/ پازل نیمه‌نهایی با صعود آرژانتین تکمیل شد
🔹
سوئیس ۱ - آرژانتین ۳
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/669989" target="_blank">📅 07:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669988">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سنتکام: حملات ما در ایران پایان یافت
🔹
سازمان تروریستی «ستاد فرماندهی مرکزی آمریکا» اعلام کرد: تازه‌ترین دور حملات ما در ایران به پایان رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/669988" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669987">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سازمان دریانوردی انگلیس: خدمۀ کشتی مورد هدف در خلیج‌فارس، برای حفظ جان خود کشتی را رها کرده و در حال حاضر سوار بر قایق نجات هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/669987" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669986">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
روابط عمومی سپاه: دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز تعمیرات و نگهداری جنگنده‌ها و مرکز فرماندهی و کنترل  پایگاه العدید قطر در هم کوبیده شد
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
🔹
در پاسخ به ادامه تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگه هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحله دوم عملیات مقابله به مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های و مرکز فرماندهی این پادگان در هم کوبیده شد.
🔹
دشمن امریکایی - صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت. بجنگ تا بجنگیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/669986" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669983">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
موج حملات پهپادی ارتش به پایگاه های آمریکا در منطقه
روابط عمومی ارتش:
🔹
در پاسخ به ادامه تجاوزات آمریکای جنایتکار به مناطقی از جنوب کشور، ارتش جمهوری اسلامی ایران، از ساعاتی قبل، با پهپادهای انهدامی خود، سامانه پاتریوت، انبار مهمات و سایت رادار ارتش تروریستی آمریکا در کویت را  هدف حملات پهپادهای قرار داد.
🔹
همچنین در موج دیگری از حملات پهپادی ارتش جمهوری اسلامی ایران، سامانه ارتباطی و سایت راداری ارتش کودک کش آمریکا در بحرین هدف قرار گرفت.
🔹
ارتش جمهوری اسلامی ایران هشدار داد: عواقب اینگونه حرکات و ناامنی در منطقه بر عهده دشمن آمریکایی صهیونی خواهد بود و در صورت تکرار این حملات،پاسخ های شدیدتری خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/669983" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669982">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
‌تنگۀ هرمز بسته شد
نیروی دریایی سپاه:
🔹
با توجه به بروز ناامنی به سبب مداخلۀ غیرقانونی بیگانگان، تنگۀ هرمز تا اطلاع ثانوی و تا پایان مداخلات آمریکا در این منطقه بسته و هیچ شناوری اجازه تردد نخواهد داشت.
🔹
اگر دشمن متجاوز به بهانۀ این حادثه که خود مسبب آن بوده است، خطایی کند و تجاوز جدیدی علیه ما داشته باشد با شدت پاسخ داده خواهد شد و پایگاه های جدیدی از دشمن در منطقه مورد هدف قرار خواهد گرفت.
🔹
عواقب چنین مداخله‌ای بر عهدۀ دشمن آمریکایی-صهیونی و کشورهایی است که خاک خود را برای این تهدیدات در اختیار پایگاه دشمن گذاشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/669982" target="_blank">📅 06:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669981">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a3efe80de.mp4?token=KcCzm5hBpDwwMOIIWQ1q-ha8wd63evGPbNORsyggMc33gKV-AFOJhsZVVlTd255N-ydNYZx_09y6zL6o-GjcoHTGAnsNfWklMTFdK0I-8xmhPWTVt9pgS1tbt95S75atiop4N62cXzk5nPKzq3in3JD4TVhiv99g1_imOR5_FgA5Y24cM2iZ9USt-bIJ8DKSKsGZ-UFVvL4tHGZP3g2tE21JPF-Qo0_cQ8TToy7RxsKf8lMEAhTir2klWzZt-uzU160vRYrVIhQOHqbGiDivuMMBhRR_J5rjkHmuhz1SmafPdXtU-mdqfSgh8c3DYxBzQcc4hoSlCQ-qQwUeN7BZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a3efe80de.mp4?token=KcCzm5hBpDwwMOIIWQ1q-ha8wd63evGPbNORsyggMc33gKV-AFOJhsZVVlTd255N-ydNYZx_09y6zL6o-GjcoHTGAnsNfWklMTFdK0I-8xmhPWTVt9pgS1tbt95S75atiop4N62cXzk5nPKzq3in3JD4TVhiv99g1_imOR5_FgA5Y24cM2iZ9USt-bIJ8DKSKsGZ-UFVvL4tHGZP3g2tE21JPF-Qo0_cQ8TToy7RxsKf8lMEAhTir2klWzZt-uzU160vRYrVIhQOHqbGiDivuMMBhRR_J5rjkHmuhz1SmafPdXtU-mdqfSgh8c3DYxBzQcc4hoSlCQ-qQwUeN7BZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلند شدن دود از پایگاه دریایی آمریکا در بحرین در پی حملات ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/669981" target="_blank">📅 06:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669980">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سپاه: آشیانه پهپادهای MQ-۹ آمریکا در اردن را منهدم کردیم
🔹
سپاه پاسداران، مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ۹ در پایگاه آمریکایی پرنس حسن اردن را منهدم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/669980" target="_blank">📅 06:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669979">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
شلیک‌ِ اخطار نیروی دریایی سپاه به کشتی متخلف
نیروی دریایی سپاه:
🔹
در اطلاعیۀ قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی‌ها در تنگۀ هرمز، برخورد قاطع ما را به‌دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.
🔹
ساعاتی قبل، این تذکرات نادیده گرفته شد و با تحریک بیگانگان چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی‌اعتنایی کردند.
🔹
به ناچار یک فروند از کشتی‌ها که با خاموش کردن سامانه‌های خود امنیت دریایی را به مخاطره افکنده بود؛ مورد اصابت شلیک‌ِاخطار واقع و متوقف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669979" target="_blank">📅 06:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669978">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89348bd4a8.mp4?token=NyWajnOGs0DLZ7DV2vS-2l6kX8hjjtYCEiQocu14xc2MfJRWHC2m0YrrPcHJvOOjhoZ6FfbO1yQVlX6T7YZPTxp4zPf8XCsNQy3Iq3VfA61IjFArigy5olhZhbCQi45N8N7WqQWiPGHDUdaQ28OYN5E8LuWpovdUH8cbLJC07zrbfBd7D6QbwfCa6-coxmqrhMIYZbBoZkURc9b82vYZvw44kJIIe776ZDts4e1FNEkJE8trkCXJSwVe0b6rSZF8sAr8eCjLAyIWNS4Da3Iay-EQxj_THlgdkXzAhwK4av5j9Kc7HAZcKymzDx8rTHYoPHHWf8ECBLtQHkfSRrSL-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89348bd4a8.mp4?token=NyWajnOGs0DLZ7DV2vS-2l6kX8hjjtYCEiQocu14xc2MfJRWHC2m0YrrPcHJvOOjhoZ6FfbO1yQVlX6T7YZPTxp4zPf8XCsNQy3Iq3VfA61IjFArigy5olhZhbCQi45N8N7WqQWiPGHDUdaQ28OYN5E8LuWpovdUH8cbLJC07zrbfBd7D6QbwfCa6-coxmqrhMIYZbBoZkURc9b82vYZvw44kJIIe776ZDts4e1FNEkJE8trkCXJSwVe0b6rSZF8sAr8eCjLAyIWNS4Da3Iay-EQxj_THlgdkXzAhwK4av5j9Kc7HAZcKymzDx8rTHYoPHHWf8ECBLtQHkfSRrSL-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از هدف قرار گرفتن مقر فرماندهی ناوگان پنجم نیروی دریایی آمریکا و وقوع آتش سوزی در آن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/669978" target="_blank">📅 06:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669977">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9181ac0230.mp4?token=ZJZpK-oWLe_oqXYGrdzeDMXLVqGaecsjhU5HmpPhewJt4CMpOMam2Xexzh43IB9eTYAzpio7_wWq6womQQBTe09esJ56Gf5LRg-yMMSKboT3_8HKmdJmOszyz7nB-RNUWqdRjQIYBiZSIDzUlQLsY9F1EH9wHjrDITKRCrjSjz6-HMiRH6xcjuiBMYCyEfktpaNKOdB2cr5dFWjPgpSXzzOXhT6K9ojiAhzdLJWNjYL_UEtwGkCa4xPH2yNg8jYK1aMg4WS-4HHw9MxS9O5znN7cjvjkRhUOmFSUdidlxZSY2u0wJBormFPTCwwltulmpo7HuKLx8I5dH4ydHXt0wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9181ac0230.mp4?token=ZJZpK-oWLe_oqXYGrdzeDMXLVqGaecsjhU5HmpPhewJt4CMpOMam2Xexzh43IB9eTYAzpio7_wWq6womQQBTe09esJ56Gf5LRg-yMMSKboT3_8HKmdJmOszyz7nB-RNUWqdRjQIYBiZSIDzUlQLsY9F1EH9wHjrDITKRCrjSjz6-HMiRH6xcjuiBMYCyEfktpaNKOdB2cr5dFWjPgpSXzzOXhT6K9ojiAhzdLJWNjYL_UEtwGkCa4xPH2yNg8jYK1aMg4WS-4HHw9MxS9O5znN7cjvjkRhUOmFSUdidlxZSY2u0wJBormFPTCwwltulmpo7HuKLx8I5dH4ydHXt0wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/669977" target="_blank">📅 06:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669976">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
مرکز فرماندهی و کنترل و آشیانه‌های پهپادهای MQ9 در پایگاه آمریکایی پرنس حسن اردن منهدم شد
روابط عمومی سپاه:
🔹
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
رژیم جنایتکار آمریکا با تحمیل اراده خود به حکومت پادشاهی عمان، شب گذشته تلاش کرد بار دیگر آزموده را بی آزماید و با تحریک چند شناور در مسیر غیرقانونی در جنوب تنگه هرمزد ایجاد کند، که با پاسخ قاطع نیروی دریایی متوقف شد.
🔹
ارتش کودک‌کش آمریکا برای جبران این شکست دست به حمله هوایی علیه تعدادی از پایگاه‌های ساحلی و دکل‌های مخابراتی در سواحل جنوبی زد. همانطور که وعده داده بودیم بلافاصله پاسخ کوبنده تجاوز خود را دریافت کرد.
🔹
رزمندگان غیور هوافضای سپاه پایگاه‌های نظامی آمریکا را هدف قرار دادند. در مرحله اول این پاسخ زیرساخت‌ها و تاسیسات مهم نظامی در پایگاه هوایی پرنس حسن اردن را هدف قرار دادند و مرکز فرماندهی و کنترل این پایگاه و آشیانه های پهپادهای MQ9 را با چند فروند موشک بالستیک در هم کوبیدند.
🔹
ادامه تجاوز آمریکای عهدشکن پاسخ های شدیدتر را به دنبال خواهد داشت.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/669976" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669975">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
انفجارهای شدید در بحرین
🔹
منابع عربی از اصابت دقیق موشک‌های ایرانی به پایگاه آمریکا در بحرین خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/669975" target="_blank">📅 06:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669974">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وزارت دفاع امارات حمله موشکی و پهپادی به این کشور را تائید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/669974" target="_blank">📅 06:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669973">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در دوحه قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/669973" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
منابع عربی: انفجارهای شدیدی دوباره امارات را به لرزه درآورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669972" target="_blank">📅 06:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
امارات هم از فعال شدن سامانه پدافندی در این کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/669971" target="_blank">📅 06:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
گزارش‌های از وقوع انفجار در امارات و قطر
🔹
منابع محلی از شنیده‌شدن صدای چندین انفجار در پایگاه‌های نظامی آمریکایی در قطر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/669970" target="_blank">📅 06:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وزرات کشور بحرین از فعال شدن آژیر هشدار در این کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/669969" target="_blank">📅 06:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669968">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
صدای انفجار در بحرین
🔹
منابع محلی از شنیده‌ شدن صدای انفجار در پایگاه‌های آمریکایی در بحرین خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/669968" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669967">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت
🔹
برخی منابع خبری گزارش می‌دهند که اهداف و منافع آمریکا در کشور کویت هدف حمله موشکی قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/669967" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
فعال شدن سامانه پدافندی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/669966" target="_blank">📅 05:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
حمله موشکی از ایران
🔹
شلیک موشک‌های کروز و پهپادهای انتحاری به سمت ناوگان دریایی آمریکا در دریای عمان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/669965" target="_blank">📅 05:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
۳ شهرستان خوزستان مورد اصابت پرتابه‌های دشمن قرار گرفت
معاون امنیتی استانداری خوزستان:
🔹
شهرستانهای هندیجان، ماهشهر و ابادان مورد اصابت پرتابه‌های دشمن قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/669964" target="_blank">📅 05:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
هم‌اکنون؛ شنیده شدن صدای دو انفجار دیگر در بندر جاسک هرمزگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/669963" target="_blank">📅 04:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
انفجاری در روستای شاه عبدالله در جنوبی‌ترین نقطه استان خوزستان و در ورودی شهرستان دیلم و استان بوشهر گزارش شده و تلفاتی نداشته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/669962" target="_blank">📅 04:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUDLnapEyWA95wrYtmpoht0bl677WRm3Ax1FiF0NgCIif7JUM6vpSLM7PDqgsijx_w1qqH-061Re2uXwfnc4mbf8FjgrXoulCImkrqcl4hs0QfWadP--fcGf-Nb7FMyMuGBULQZlkNbrwso-lxeuSEfsS0_qbHWLCVeEARCZWE-2TloPs8TQnzotVzuSKXhaW4CNze9YJbyMwrMqozq7gPI7Z68-cMygX9j0sMMauXXd2hhwe-nnZrmoZI9Cii3YFfdtc_RbJDxHUxOf2wGScV3mDKFfOPHaOIbymEkCdghtzJ0dI1NIF9uK04rkNQva0gry8vUxnefiqYF30f1EFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در حملات بامداد امروز، تمرکز آمریکا بر نواحی جنوب و خط ساحلی ایران بوده است
🔹
آکسیوس مدعی شده که تمام اهداف در این حملات نظامی است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/669961" target="_blank">📅 04:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: هم اکنون وضعیت در بندرعباس، سیریک و جاسک آرام گزارش شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/669960" target="_blank">📅 04:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
معاون سیاسی امنیتی و اجتماعی استاندار بوشهر: در حملات دشمن تروریستی امریکایی - صهیونی به شهرهای استان بوشهر شامل شهرهای بوشهر، عسلویه و دیر تاکنون تلفاتی گزارش نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/669959" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669957">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
دستور نتانیاهو برای آمادگی جهت عملیات نظامی مستقل علیه ایران
وزیر جنگ رژیم صهیونسیتی:
🔹
ارتش این کشور با دریافت دستور از نخست‌وزیر نتانیاهو، موظف به انجام تدارکات لازم برای اجرای یک عملیات نظامی مستقل علیه ایران شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/669957" target="_blank">📅 04:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669955">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
شنیده‌ شدن صدای چندین انفجار در جاسک
🔹
دقایقی پیش مردم جاسک صدای چندین انفجار شنیدند، که منشأ آن هنوز مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/669955" target="_blank">📅 04:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
در یک ساعت گذشته صدای ۱۲ انفجار در نقاط مختلف استان بوشهر شنیده شد
🔹
صدای ۵ انفجاد در بندر دیر، ۴ انفجار در عسلویه و ۳ انفجار هم در شهر بوشهر به گوش رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/669954" target="_blank">📅 04:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669953">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ایرنا: بیشترین انفجار از جاسک گزارش شده. بیش از ۱۰ انفجار. محل دقیق حمله مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/669953" target="_blank">📅 04:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c4cc5f76.mp4?token=NasKkjUrpPaZ8Z8hhHB5xfbTiycXMIgcXfeo48VEdUdjBGhfpGue2lAMF1MB_BnwrvPKOoi9Xv-_43C9jt06ensK8tQrSkKdoj4v9PT5lVuHAdoqY-0zQaNncYDl_MJv8A0dT9LY2MLYGoXNtWvVwmurfVQpTlPBUPcyCGm44dCGClIQ9kV7MX9E3-Fv4YG18UUFGYlY2sqXvRZJmWs7fqRl2MK5fkZKfyyhJWRh-FLyzXXGVuWDOl15ndR0qz0sOTk64MokEynd75pE9UnabH4tIaiJZbtgWSd1D3EU7WbLsrnojMWHbmWK4Pc0kD61RiX_Y4JZWyUMyj37kAkm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c4cc5f76.mp4?token=NasKkjUrpPaZ8Z8hhHB5xfbTiycXMIgcXfeo48VEdUdjBGhfpGue2lAMF1MB_BnwrvPKOoi9Xv-_43C9jt06ensK8tQrSkKdoj4v9PT5lVuHAdoqY-0zQaNncYDl_MJv8A0dT9LY2MLYGoXNtWvVwmurfVQpTlPBUPcyCGm44dCGClIQ9kV7MX9E3-Fv4YG18UUFGYlY2sqXvRZJmWs7fqRl2MK5fkZKfyyhJWRh-FLyzXXGVuWDOl15ndR0qz0sOTk64MokEynd75pE9UnabH4tIaiJZbtgWSd1D3EU7WbLsrnojMWHbmWK4Pc0kD61RiX_Y4JZWyUMyj37kAkm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک‌‌های زمین‌ به‌ زمین از کویت به سوی ایران توسط مردم عراق پخش شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/669952" target="_blank">📅 04:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669951">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V22bWVU5De7Hv3RVLA30OTf5TrMePCvtBVEE9NCprLOHVB5futgZ8u8WjLhp6VUKJISQoZth71kwv39EONg_MYC-Ivx_AUiZeku16jniMDNH4erDtq78nD9HRNbxFNVgMqWW4lltsCO0gbr_YMKNSNzy_c-4imEvTaVcwuhSN2k4O8sZ1kIFUC9Y-kNHrryO8E8xRxobSQtWBa1EqCYgPIy7ze6rdVi_Q8wv3qekTALcO0mBTyeVhoyuYANeAKphnOU_d7UL1LQxeZEqHzdRABNWqLJ-eB-JkVHC644kXfKGCsJXguDw4WvZPkQivJFlvoIUnyVvPVeEdV27qfBPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شلیک موشک‌های آمریکایی از کویت به سمت خاک کشورمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/669951" target="_blank">📅 04:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669950">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک مقام آمریکایی: کشتی باری که توسط سپاه پاسداران هدف قرار گرفت، در حال عبور از مسیر جنوبی بود که سلطان‌نشین عمان پیشنهاد بازگشایی بدون محدودیت آن را داده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/669950" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669949">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
در یک ساعت گذشته صدای ۱۲ انفجار در نقاط مختلف استان بوشهر شنیده شد
🔹
صدای ۵ انفجاد در بندر دیر، ۴ انفجار در عسلویه و ۳ انفجار هم در شهر بوشهر به گوش رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/669949" target="_blank">📅 03:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669948">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در جاسک: شنیده شدن صدای بیش از ۱۰ انفجار در جاسک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/669948" target="_blank">📅 03:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669947">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در جاسک
🔹
منابع محلی از شنیده‌ شدن صدای انفجارهایی طی بامداد یکشنبه در شهر جاسک خبر داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/669947" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669946">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تسنیم: شنیده شدن صدای سه انفجار در بندرعباس و دو انفجار در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/669946" target="_blank">📅 03:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669945">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رسانه‌های عربی: موج‌ جدید حملات از بحرین به سوی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/669945" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669944">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75c50fdb1.mp4?token=bYifl7e6ETYGXrNifai59ARDkcFCPYAf__1_EpMYx8ZdFhfOD1_p2i4QXQS-xFs049C4EMIGhKdHywEPfXpAcbLz4CN2NiLsW9B2jYAh4KtIs-9KkoGUOHquwyP87jUW7b0FW1GwZN-u4TzgaE9XyE0HWUPW_2zMEUSgp7zee4uLWowYIdiT6pxZXRBU0UaetVArzBVIWuxsw59E59dTSUJbw4GVf5mwB_PRsZQEUqgGWg8EHaEXYhJ5iU0tCZE-_LmlwRF-8YuEix9RpvMY1mkhSzyq4PgYN7NaGL_j5vMTbLLVDd3kAuHDvkSrnjEkuGx6c_uiTZoancas-ZqJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75c50fdb1.mp4?token=bYifl7e6ETYGXrNifai59ARDkcFCPYAf__1_EpMYx8ZdFhfOD1_p2i4QXQS-xFs049C4EMIGhKdHywEPfXpAcbLz4CN2NiLsW9B2jYAh4KtIs-9KkoGUOHquwyP87jUW7b0FW1GwZN-u4TzgaE9XyE0HWUPW_2zMEUSgp7zee4uLWowYIdiT6pxZXRBU0UaetVArzBVIWuxsw59E59dTSUJbw4GVf5mwB_PRsZQEUqgGWg8EHaEXYhJ5iU0tCZE-_LmlwRF-8YuEix9RpvMY1mkhSzyq4PgYN7NaGL_j5vMTbLLVDd3kAuHDvkSrnjEkuGx6c_uiTZoancas-ZqJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن انفجارهای متعدد در چهار شهرستان استان بوشهر؛ هدف قرار گرفتن پادگان‌های نظامی و تأسیسات اقتصادی در کنگان، عسلویه و دیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/669944" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669943">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
گزارش‌ها از فعال شدن پدافند هوایی در ماهشهر
🔹
بامداد یکشنبه سامانه پدافند هوایی در بندر ماهشهر، واقع در استان خوزستان، فعال شده است. تا زمان انتشار این خبر، مقام‌های رسمی هیچ توضیحی درباره علت فعالیت پدافند، محل دقیق آن یا احتمال وقوع هرگونه حادثه ارائه نکرده‌اند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/669943" target="_blank">📅 03:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669942">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
صداهای شنیده شده در چابهار مربوط به حمله دشمن تروریستی آمریکا به یک منطقه در کنارک بوده است/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/669942" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669941">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
شنیده شدن‌ صدای دو‌ انفجا‌ر هم اکنون در اطراف چابهار
🔹
صدای ۵ انفجار هم در دیر استان بوشهر شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/669941" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669940">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
انگلیس با برتری ۲ بر ۱ برابر نروژ، به نیمه‌نهایی جام‌جهانی صعود کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/669940" target="_blank">📅 03:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669939">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تکذیب شایعه حمله به اهواز و آبادان
🔹
معاون امنیتی استانداری خوزستان اخبار منتشر شده مبنی بر وقوع انفجار در شهرهای اهواز و آبادان را به شدت تکذیب کرد و آن را شایعه‌ای بی‌اساس و ناشی از عملیات روانی رسانه‌های معاند دانست.
🔹
وی با تأکید بر پایداری کامل امنیت در استان، اظهار داشت: نیروهای امنیتی و نظامی در آماده‌باش کامل هستند و هیچ رخداد خاصی در استان تا این لحظه گزارش نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/669939" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669938">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
شنیده شدن‌ صدای دو‌ انفجا‌ر هم اکنون در اطراف چابهار
🔹
صدای ۵ انفجار هم در دیر استان بوشهر شنیده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/669938" target="_blank">📅 03:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669937">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار از سواحل هرمزگان
🔹
دقایقی پیش مردم از سمت نوار ساحلی سیریک و میناب و بندرعباس صدای چند انفجار شنیدند. هنوز منشا انفجارها مشخص نیست و اخبار تکمیلی متعاقبا منتشر می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/669937" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669936">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
حادثه دریایی در ۹ مایلی شرق عمان
🔹
سازمان تجارت دریایی بریتانیا (UKMTO) از  حادثه‌ دریایی در ۹ مایلی ساحل شرق عمان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/669936" target="_blank">📅 03:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=owvrrlMavAvJCiWVy8Nv8z7bC4rONCYrfsLtrCLhjjW1ztY31NA4KnpUVqdWj-r3peI9b0hiQvhMV0E5oyzZyBLzHNX73bt0MINITynh6NFVdpZj40aAmJhnDXContSRYKzG3rvCYZBqxq_40t7064HKFGG1LW3x7RiFkbjV3AiBdAFh3XgAGLjcpSjr5kwU6CqRkFHgxbPTnvZZaQwLz_rlC1E59kus-U8Bi9ABcYtidk-HNaTBbFGc6BWQ4xuQlALjbXNRjBCe1jhPGGaPkVmfS0DeSE7VevR0CAlOo_Si8r7PL4qoI9OAw7gia60zKf-W7i6HSGe4wzD27dGb2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=owvrrlMavAvJCiWVy8Nv8z7bC4rONCYrfsLtrCLhjjW1ztY31NA4KnpUVqdWj-r3peI9b0hiQvhMV0E5oyzZyBLzHNX73bt0MINITynh6NFVdpZj40aAmJhnDXContSRYKzG3rvCYZBqxq_40t7064HKFGG1LW3x7RiFkbjV3AiBdAFh3XgAGLjcpSjr5kwU6CqRkFHgxbPTnvZZaQwLz_rlC1E59kus-U8Bi9ABcYtidk-HNaTBbFGc6BWQ4xuQlALjbXNRjBCe1jhPGGaPkVmfS0DeSE7VevR0CAlOo_Si8r7PL4qoI9OAw7gia60zKf-W7i6HSGe4wzD27dGb2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🔹
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/669935" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: اگر وضعیت کنونی توسط میانجی‌ها مهار و کنترل نشود، تنگه هرمز می‌تواند به نقطه آغاز یک جنگ جدید تبدیل شود
🔹
به نظر می‌رسد ایران پس از پایان مراسم تشییع، دیگر از آن محدودیت‌ها عبور کرده و اکنون بر مبنای آمادگی برای همه سناریوهای احتمالی عمل می‌کند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/669934" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
فرماندار قشم: تا این لحظه اصابتی در قشم گزارش نشده است
🔹
دقایقی قبل صدای انفجار در قشم شنیده شد که با توجه به اظهار نظر فرماندار این جزیره ممکن است، صدای از سوی دریا باشد./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/669933" target="_blank">📅 03:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669932">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرنگار صدا و سیما در عسلویه:
صدای ۴ انفجار در این منطقه شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/669932" target="_blank">📅 03:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669931">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaoJ44N068gSz71R1E1V-QwHp-nguIlcxdgT2OS4S5Uf0ZfjD6CgQjMnP7LlCs3cnOvJeNJS13l59Oy_7l_f_kwjg2Nmkipl27YbuhgEhCKdmSYsuWbRB0JrRvHHqUwJ4qesx02nfpk7rdJoDR09DHH-U3FQn_CRuVD_jUwLxiWrJbZfUYSlyCbVF-jACqCr2gHcAXO8T4GUfhXAEjY1fZap4lAO30Nl5aZeSjCeB8s4bRxFO1C_Gh2gxMSN7e45MR-trhbFJy5LeqyZinL_Kr_44cPhHnqlgt2Mc9OQCGLdCzJReRVyfP9qTSqjICFKDN5IvEizabGMApiVGl0oSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری/ پیت هگزت وزیر جنگ آمریکا: ایران انتخاب نادرستی انجام داد. اکنون آن‌ها باید عواقب آن را بپردازند.
اخبار لحظه‌ای جنگ
👇
khabarfoori.com/fa/tiny/news-3229601</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/669931" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669930">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تسنیم: شنیده شدن صدای سه انفجار در بندرعباس و دو انفجار در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/669930" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669929">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Twq2GMKOvtEAYbm17C4IZvocfeCoy-r4sbUwng8fq-s3VTfnR7WMNnXTW7AYCEZlxHNO_A8vgVtv9O9z0ozd92kHib7iwZFXELDh5ov5zSD5JKWaa2g_xSSl57EiQXDZla4Fzv_RnHuTr-T9NI7e4YebX8TdHvo3wpBd7wAyMXLUcMUeaoBGbZ1QWCHPeuGWzpGdOizzrYKdAbfH7covra8EfCee6C_r029GdqOrAndK0p_QVVG9v7LT-1E9lKls5jGyYmFHT-gXXrZJM9CQkLimUv8JEJW-v7ntQVL9vtxQFrxhi5vKN4b4G9fNOsYyGjri0YdHQJNLNubFIOmSOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام از حمله به ایران خبر داد
🔹
سنتکام اعلام کرد به دستور ترامپ حملاتی را علیه ایران آغاز کرده تا توانایی ایران را در اعمال مدیریت بر تنگهٔ هرمز کاهش دهد‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/669929" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669928">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
گزارش هایی از شنیده شدن صدای انفجار در، عسلویه، بوشهر ، دیر و کنگان شنیده شده است.
احتمالا اسکله دیر مورد حمله قرار گرفته است./هم‌میهن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/669928" target="_blank">📅 02:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669927">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فوری/ گزارشات تایید نشده از پرتاب موشک از بحرین به سوی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/669927" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5NmJ65Dz5kBiYR2eVPUC2VaWAtIJ8YjqVbc4HjZkbBmq02FQUWagwhDBbmMZ2xqnBbsCk7oCA4vRXxz0ewsfGIomI6L4m4vlAnVyK3AroRMVs_5uVCsj9B7HVhd8eH4NATsuHc2gcpLqLu-nhnBt6kau9-lfBDYLgx-sZNijrv0y376bN_GDPCSIsgs-z2mQxzOFEPz4qQG2iJoGzy68t5ngzqRZ8Sasgth1r5lQdesFDgvzxe7ZpnLtLw7ULgJenWH-6Y05s1j1UpHYDJrjtBNZFBOlTuH0U7I1ohC9nkcBEo78MdocVs8FHnlOzEYa5uZh0GFbYxks0lEN3gFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/669925" target="_blank">📅 01:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
شنیده شدن انفجار مهیب در غزه
🔹
برخی منابع محلی فلسطینی از وقوع انفجار مهیب در شهر غزه خبر می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/669924" target="_blank">📅 00:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2UXh6NlLmornz2iCgMNbcfY8ADeP0lqzV9Pdog_rflRQvGFOzQ87AqxN53-6QJf_UdLwNuDizDLON4I2TF5iw3iZY9EFbzWQBPE98nIWCYNZ4Tz3oKNeNYTNGK_jNiQsGOxVeeNE-oOeE8DlwE1fCCtLuIIiFQv-D5c-wqwcvfBo5c0Z9jHQ7n9KQ6N9Uv2KnCEwKx6FBCGKj4poUeCsNmx3qOTgZx1W74mf0exA6w9SGiVppphP5sLxxutmwV5Vuq3i_WPe6zp_CZ5ACyJTDzFogsx4TziGrJLfiaXPDH0FBXlO26TMEXgYZaKhKSkIdUOIrAmLVPUX6GenaoH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شگفتی خبرنگار آمریکایی از سرعت بازسازی زیرساخت‌های ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/669923" target="_blank">📅 00:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e17dd7a.mp4?token=vwxegqZzHh6wvEgdpKVCZL9k0SrLWF_MRXoH_0GxMy0cFc7d3oaUD10vtJEw6xC7wKqWUOPu5wsOb2E9TUkQaoCpo_iK9G_mpjoijGhDxNl6LnJhUv-NKsk9Fo2dsseNRgYOsebid_7-Yy8S5qQzklvtuwkX2SP5HiBpb72kceeMENNlhRt1Ft11Cfdwu0rxCvLlnaTYzR5970EAAfQODsMkHKE5CNKR-zMy9tawLwcUZsgDNRwYtvWgHUbrLYcM7KEarhF-RHNa7-kWrif3XpNyEkpSXD2BjnVV4hfFweIHdVBMcuDYIqkhuwBMsas_mDL5rciswZagrgykE6juYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e17dd7a.mp4?token=vwxegqZzHh6wvEgdpKVCZL9k0SrLWF_MRXoH_0GxMy0cFc7d3oaUD10vtJEw6xC7wKqWUOPu5wsOb2E9TUkQaoCpo_iK9G_mpjoijGhDxNl6LnJhUv-NKsk9Fo2dsseNRgYOsebid_7-Yy8S5qQzklvtuwkX2SP5HiBpb72kceeMENNlhRt1Ft11Cfdwu0rxCvLlnaTYzR5970EAAfQODsMkHKE5CNKR-zMy9tawLwcUZsgDNRwYtvWgHUbrLYcM7KEarhF-RHNa7-kWrif3XpNyEkpSXD2BjnVV4hfFweIHdVBMcuDYIqkhuwBMsas_mDL5rciswZagrgykE6juYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو هایی با هوش مصنوعی که بدون حضور بازیگران و کارگردانی ساخته می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/669922" target="_blank">📅 00:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
مردم بحرین برای دومین روز متوالی، با وجود تهدیدهای رژیم آل خلیفه، در سوگ آقای شهید ایران به عزاداری پرداختند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/669921" target="_blank">📅 00:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تداوم تجاوزات صهیونیست‌ها به خاک لبنان
🔹
رسانه‌های لبنانی گزارش دادند یک فروند پهپاد متجاوز اسرائیلی، بمبی صوتی بر فراز شهرک «حداثا» در شهرستان بنت‌جبیل واقع در جنوب لبنان پرتاب کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/669920" target="_blank">📅 00:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWM8R9bTEyhhB44wqwomBR7-luQS1UD9bOkdAM9RqddmYpJtuCuT9vPqTFRcsQuIdPr8179HQ8LsFQTWznJafpNlNgPuxZ8p2JGTz9dqRt4k2rO8GVftXgJrQ_S3cNcARKpHW_o3Qgj8yxlHxY1LNIaIZuXQbfx-OP_tbtYKCbRXyLJPEVUt7dhaGS6j8gJSZMX0aXErMCoU1XC5xCzAUYGtO9CMmLZZbAuQnsen5tGgbfllY5E3HBl5EPYNS2GQZmZSvf2haCofKD5uqs7yZ7JzU132GwkaRjddfXX4AvGejQFknqjzWfED6O8iweKHmmNxFGLVYgSzLzrANHVnkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/669919" target="_blank">📅 00:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqOA3DQs3F2GEBJ1R061StTivfygiUbbD1Tpwo14VfKmvlgqaUeKb88oM2qfG0qZFR3MuJzRtLGIeo4Sf4nkB6g1bokfAsEY8AY8dSgAB6zIdUpbWcapGyUsy_hftOc2MzGIivBLh9aTBwqWK7fe1dSLTS-3pLO74gtPooBQKmiz8p19z6SliHRE7eZ0Uf2eyTjA00TgeJM9GW9Q389hWchaFb28w9JylsR9oiODp-AvjvuJ5uocrrdSoZVFB0nU0yPBFXFDrpKbGw9mEF9IqzBBbuiZ6gWD0AkcdQDLaiDXbHdgZIK5F2ZO_gvLno9lvjhOz4sO8Js8IxKklgeSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معروف‌ترین نمادهای جواهرات که بدون لوگو هم معرف برندشون هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/669918" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4165199f.mp4?token=AWaNiT6owN1alPdB54BgSPn1d0EyH0_aLRuwbBGOF1ytdggGHJkfpP9GJ74qJf-gFnpp31wFa3ESTXCSgQGz8Yd_AdNiAKLlxPvEMvQ4ujjVZB9nhu9DJMbyOc0GfH7do2uJhBcC2VLSVsDrOVcz0WwQaivQKdxeBRm4_917Pi5L8fzWlDQSXhG3HNFMWm46nDHJhmjK1LLUakEGG20vxgKWTZ1g2_0PXD6b57mWRljJv6ieI7MxQ8xECldwm8PKE3T0aBlAfYhgNJuj3Kz1j2xd0z37iGpOK7OgHY-DcQ0mjLPVX7GahPIbNZQL2LchgpykHqMNjcJ6b3R_Em1pUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4165199f.mp4?token=AWaNiT6owN1alPdB54BgSPn1d0EyH0_aLRuwbBGOF1ytdggGHJkfpP9GJ74qJf-gFnpp31wFa3ESTXCSgQGz8Yd_AdNiAKLlxPvEMvQ4ujjVZB9nhu9DJMbyOc0GfH7do2uJhBcC2VLSVsDrOVcz0WwQaivQKdxeBRm4_917Pi5L8fzWlDQSXhG3HNFMWm46nDHJhmjK1LLUakEGG20vxgKWTZ1g2_0PXD6b57mWRljJv6ieI7MxQ8xECldwm8PKE3T0aBlAfYhgNJuj3Kz1j2xd0z37iGpOK7OgHY-DcQ0mjLPVX7GahPIbNZQL2LchgpykHqMNjcJ6b3R_Em1pUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کولاک نوجوان گیلانی با تقلید از مداحی معروف حسین ستوده درباره ایران در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/669917" target="_blank">📅 23:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">«فوکوس»
؛
صریح، بی‌پرده و متفاوت
🔹
وقتی سؤال‌ها تعارف ندارند، پاسخ‌ها هم متفاوت می‌شوند...
🔹
ویژه برنامه «فوکوس» برنامه گفت‌وگوص محور جدید خبرفوری با حضور چهره‌های سیاسی، اجتماعی و اقتصادی کشور
🔹
گفت‌وگوهایی که قرار است حرف‌های ناگفته را به قاب تصویر بیاورند.
♦️
به زودی پخش از طریق رسانه‌های خبرفوری در شبکه‌های اجتماعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/669916" target="_blank">📅 23:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddb7774bd4.mp4?token=Yx9CHsvT094OK2x54fuHuPFXKYhj4_0Vl0Ter9ulIf5FTIxT5Dzh2VUHDA0Q4q3G99hrplMfA6VDYRveyfhOFYgymt7Geouo6wkfT-V8tdVMQR6JJMUYIfiKkT1-DdW-OVlhWKY1tz2KCGHAU9BKhZY5-FUe3iXNrytw8SlGs0jhw8uGSfClpo92YPrbVKJU7P4ihC9o8ACuc16M2VIs6lGK_s_l8m29X1cv0Xlg_C9mDp07CCksoHGpXTZP50RpZGa2WIjjvVg4qVOeNgx23qWPGjvtaKYkvz3StMWlCQVCIykbIfbcVKmI6ZmmNO4wuZ6t3rbNGl9pjYnzrlIU_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddb7774bd4.mp4?token=Yx9CHsvT094OK2x54fuHuPFXKYhj4_0Vl0Ter9ulIf5FTIxT5Dzh2VUHDA0Q4q3G99hrplMfA6VDYRveyfhOFYgymt7Geouo6wkfT-V8tdVMQR6JJMUYIfiKkT1-DdW-OVlhWKY1tz2KCGHAU9BKhZY5-FUe3iXNrytw8SlGs0jhw8uGSfClpo92YPrbVKJU7P4ihC9o8ACuc16M2VIs6lGK_s_l8m29X1cv0Xlg_C9mDp07CCksoHGpXTZP50RpZGa2WIjjvVg4qVOeNgx23qWPGjvtaKYkvz3StMWlCQVCIykbIfbcVKmI6ZmmNO4wuZ6t3rbNGl9pjYnzrlIU_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید خاکشیر از زبون خودش بشنوید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/669915" target="_blank">📅 23:35 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
