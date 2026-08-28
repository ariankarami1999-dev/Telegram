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
<img src="https://cdn4.telesco.pe/file/ZEA21uWy6n3MfH1OqXrKVl65sgu9XL6_bqYWCqkGc7j4DhF4U9ZDAr-X6uIjs-NY2vZq4_SMoIFm78M_pbg1GZJezDSAsKJkvRCEsv8rFmbg6x1hz_nTH4ktD0mXMyTEuQDbnyEmS9_xNrRfeK2zTctc5Ar9pnTzaBWclzCMmpe7aa9AhC8rTv953JKTKz_fNTXydGcCZHv-llZKFYIYDITjxENe727i_0ytX1-zoy-H6MuysUH_4gdc-WZUAKAtUXoKEjkZ5svIwz0FWxQmOY3kXzYuLf5l_5NgQprl8I4plqkmeOsMJyvhgZaiLK0w0q2Z4Dh890DUF-OQA0GrcA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 972K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-144166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6eVDvX_-GXqDHRD38iPuqkRUqhVYVO_JftMk6HI3cONN3Hi00Egxjrgoj9eofHXLRckp6nQkoeKyxm_qQRRbT4klU_42bXC6FyZ6_d1CM9GfFwM4LkhIiBq0gI3WVtbjtLkm6WqA_YYx-7wQPy71LIuDWJBZF4r795HfJ7gPEnFDS7MAzAaYaPBfD3i2QJYFxXu1-Qu1WVlbRI20As4Eq48L3vl4D_BHweScpuUATKludQc-r9iNm4oI04E23ScBopz6PykRVgbHNzfjNJH3cnQgko0XGmuGJv0aTzRLiW_ikzaCyyzdbFkbHF0tL0EVRAJ9iFsjYfX1CAcQ6br8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، فهرستی از رتبه‌بندی روسای جمهور آمریکا را منتشر کرد و خود را به عنوان "بزرگترین" در این فهرست قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144166" target="_blank">📅 01:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W5m4GNZUiuA1h1qMxyStMKiiHQGfkVm4LFk69Q5h0a3AFImy_-6xnwXSVg4A8cta3iT7hCBKhadwL_D-_YAzJF_orGF65W7BngmSy_perhOG7wlbS7H3K6UpjvBtaop7eCilXui0JE8S-qt5JMTsygx1Nb7zRk8ZUP-ICPanwGZjzkl7zVF26M27qEV7oBcLNCkaTUQwd1WRzLn0T0l3b_wPEsaWMv50eSz-Usc8EZurPFsJNZCGf8zivkkxGM1SzVcbKH2iZ1XGV3ksyxotIuH0kAE4zbRn0Zb21GaG3lPr-h8BXNCIyxY2sBu0niXWGuQhmRyeu4x5qIsh-9iFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار تور افغانستان گردی برای مردم ایران موجود کردن تو مملکت
🔴
قیمت تور ۷ روزه‌ هم ناقابل ۵۰ میلیون تومنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/alonews/144165" target="_blank">📅 01:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144164">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JinEhrZlJraX3ewM3eIWNIUoITKW9pkjAIOzDDh8QsbdmnNDXh3j1pRxyDD5DxCM8R0TQhxFkJZLs0ke3g1SgLYjcVmdETZwnPB6jA2ihAtBv_Wbl96V5rDSAYsrZCsJx87Q3vGh4Psw9UQIHz7s4g5IFLpYwY0PM902ASyLXxAG1p-i47mEfI6wI7XdoWOqQeOilN16yKB4qN4ttY9vXaNHo87u3_VfU6f46aKbdTEQij72mkHSl5sJFrqZD2KcHn8M8TAH0oW8TYyIh-gttBdkiGZ8U3_zTOoYRzL6PYAVCEy9D6ub3mxM-UIezBB0Imlpuq8y8aQ9_-Yhd0E4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیراحمد کاظمی؛ کارشناس اقتصاد:
اثر واقعی محاصره دریایی آمریکا هنوز شروع نشده. گندم؛ ذرت؛ سویا؛ برنج؛ شکر؛ شیرخشک و کلی کالای حجیم دیگه در مقیاس موردنیاز ایران عملاً به حمل دریایی وابسته‌ان.
دریا که قفل بشه؛ فقط کشتی‌ها متوقف نمیشن؛ بلکه زنجیره تأمین قفل میشه. اول کرایه و بیمه میره بالا؛ بعد واردات کند میشه؛ بعد موجودی انبارها آب میره و در نهایت قیمت‌ها میتونن منفجر بشن.
اگر محاصره طول بکشه داستان از «اختلال واردات» میتونه به «بحران عرضه» تبدیل بشه. آخر مهر آغاز موج بشدت گسترده گرونی کالا هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/144164" target="_blank">📅 00:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNWsvAg93_yx6uQZLWuqO7dFFXg2D6sy6zZPH2Uud4y0pIdQ-A2TRKBjXzobe3wgpzLF7BoCczK5Gz_Bynmk8kTR0HvT6F31FfH24kc8uy8PiR0KIPJo2sXMKMD428501eo6uqeAvTEdZNL_hUIyJtFlyOVs712lIywBLkSvpQTLRlEScgg4Z90rm2km5o5rh6SOnwZM0bUKDxjcCKcGdEhyMFyikH9CqIk4P9phOG-djmnVJx97ZnE3S4acsq1YP_p5QwBbWfv5ik5AeRd4-Rbjr_IP8YCOff4jOCzSya5eYe6XdZGCrruMudP2dZnBrkZ9LNczwl-foE_I2KJFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال: جنوب لبنان خط قرمز ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/144163" target="_blank">📅 00:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
تریلر کامل GTA VI منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/144162" target="_blank">📅 00:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144161">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال ماهان رو بخون هر خبری درمورد تورم و گرونی هست اول اینجا میزاره
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/144161" target="_blank">📅 00:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144160">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390cb79159.mp4?token=In6hkYtvvO_F9tY4_Z3lRaKnVeljuhtc09wD1WxDGNosjErABLguux31THBT_QmoecE16dNK4Nqs4405TMXuM0XTIt353E6IblzJreH7zF2aX74VStEthmRJ7zT7aEOGyU6CHCApYydPGkX4e-q-9zHSrsGGyy7plSEGpH9inzTxlx7E1-bXUPRRYphc-1pH37nT3x1mm6gY9DEZNC-c2iLdoNHEIcGzdh9vysG61NbAjQ03KPLaXTs3Z9fqFEvQEUivJQe_LIYU_Cztw4RUju5MeDOAsqNmBm_X0bmwz80bhbzqY8PFwNRyYuX-C5Jkb7CpvgixjDPC_U_NzSrRNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390cb79159.mp4?token=In6hkYtvvO_F9tY4_Z3lRaKnVeljuhtc09wD1WxDGNosjErABLguux31THBT_QmoecE16dNK4Nqs4405TMXuM0XTIt353E6IblzJreH7zF2aX74VStEthmRJ7zT7aEOGyU6CHCApYydPGkX4e-q-9zHSrsGGyy7plSEGpH9inzTxlx7E1-bXUPRRYphc-1pH37nT3x1mm6gY9DEZNC-c2iLdoNHEIcGzdh9vysG61NbAjQ03KPLaXTs3Z9fqFEvQEUivJQe_LIYU_Cztw4RUju5MeDOAsqNmBm_X0bmwz80bhbzqY8PFwNRyYuX-C5Jkb7CpvgixjDPC_U_NzSrRNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو : هر کسی میخواد برقش قطع نشه میتونه از بورس برق با قیمت آزاد خریداری کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144160" target="_blank">📅 00:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144159">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کویت و پاکستان توافق‌نامه همکاری دفاعی و نظامی امضا کردند
🔴
این توافق‌نامه بر تبادل تجربیات و ارتقای آمادگی نیروهای مسلح دو کشور تمرکز دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/144159" target="_blank">📅 23:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144158">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ایران فهرستی از شروط خود را برای انتقال به آمریکایی‌ها آماده کرده
🔴
ایران در حال حاضر یک مسیر موقت و مشخص برای عبور کشتی‌ها در وسط تنگه را مجاز دانسته است، به شرطی که آینده تردد در آن منوط به تفاهمنامه با واشنگتن باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/144158" target="_blank">📅 23:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144157">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4699eef4cb.mp4?token=Vahy7L91skn9GIv_vI73IDFtMgJ2Jl1Ey6mwN-pPlq_XYER2LB8GPTc0aEsWc_aenRH3eaUZLuoF3WvqJ5LlD9856fE9eVMcnK_WRquCgiepFQsyuyWmSETJEzrkpXMg-Z4O2lihU5d4vAas1yEuSXJiJS3RmOf3GIv2K4su--vUumr5t2n_pyKQlc2W9etvOxg8KwLwpyFQBIyD4to79rCTKFj8R1co_W2aKmL7ajpKydHUlTVYsCjS4mDWhJ_bNtnhmMGwYAQ7oLZTZw5bXoOzvsp4WnTNc-y1x2hbhUAf1fS8JCR_Kpf0q9uItscoqyQUss2UZyO3qr4lMHJU_A1OpgVNnD63xrkGdZtZLmR4EGOW2cMrg_CyYFjDmRje7Tr03H6-CE6LK-6QCS92M5EjKMFThuor0pdpY4nuXTV30klXrZ0qCTb0RuJzFCxHLHn34art8IdHJFcnttFUubL8GjpNjeDlPVkq6eqzAW9p-dhL0sDU8o1vZrUmetf3awWy3Hn2_13nKUCjhvIj9qBkY1JTIt--nOwKNpf9-QfS7yVbxISV4mOvFE8Mb3a2pVOwhafkA6StWrqzO2gs-GEoiTli9oJbVZWm_pk5f2VzgnKQ870xQpptex9ef4ppomPg80nVddT2OjNUe5kEqEcVIJt1ENlUIRCcWnce8Ls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4699eef4cb.mp4?token=Vahy7L91skn9GIv_vI73IDFtMgJ2Jl1Ey6mwN-pPlq_XYER2LB8GPTc0aEsWc_aenRH3eaUZLuoF3WvqJ5LlD9856fE9eVMcnK_WRquCgiepFQsyuyWmSETJEzrkpXMg-Z4O2lihU5d4vAas1yEuSXJiJS3RmOf3GIv2K4su--vUumr5t2n_pyKQlc2W9etvOxg8KwLwpyFQBIyD4to79rCTKFj8R1co_W2aKmL7ajpKydHUlTVYsCjS4mDWhJ_bNtnhmMGwYAQ7oLZTZw5bXoOzvsp4WnTNc-y1x2hbhUAf1fS8JCR_Kpf0q9uItscoqyQUss2UZyO3qr4lMHJU_A1OpgVNnD63xrkGdZtZLmR4EGOW2cMrg_CyYFjDmRje7Tr03H6-CE6LK-6QCS92M5EjKMFThuor0pdpY4nuXTV30klXrZ0qCTb0RuJzFCxHLHn34art8IdHJFcnttFUubL8GjpNjeDlPVkq6eqzAW9p-dhL0sDU8o1vZrUmetf3awWy3Hn2_13nKUCjhvIj9qBkY1JTIt--nOwKNpf9-QfS7yVbxISV4mOvFE8Mb3a2pVOwhafkA6StWrqzO2gs-GEoiTli9oJbVZWm_pk5f2VzgnKQ870xQpptex9ef4ppomPg80nVddT2OjNUe5kEqEcVIJt1ENlUIRCcWnce8Ls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: چیزی که در تفاهم‌نامه نوشتیم و امضا کردیم به نظر من سند افتخار جمهوری اسلامی است
‏
🔴
بارها گفتم همه عزیزان شورای امنیت از این تفاهم‌نامه با قدرت دفاع کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/144157" target="_blank">📅 23:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144156">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF6x8DmpxRIyeiKCgrRRNYwTCJ2V7QS2BaGLmHEOiPun9bnU7se3LtMHZRAqbrqb5DgvqkLu3S8KKEWJ0FqjGfgDr1s9J7-HaedsWZhlfWE-eRg7qvqpwYoMnoPPhWDWksz46orkAuE3LYt-rOHC4zuhT9BVfiJTmKZ-M1PUpa8t4Re88Bk_doTuNsr4LilxxZHseDt5qbA4wR3X6ofZeqUPbtIamcrGUOhj-7NSf5jnDmgD2mqsKSRPn2JU9-PhjYJJw_gHfoDi_rJpzwSV4mNc6r2bmy9XVA16Di79pmeRmjo1bAZwuMouc6Ps01eRbLaWEjzj-cOwfYd2kSVmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در Truth Social: خبر فوق‌العاده! شرکت Micron، یکی از داغ‌ترین شرکت‌های جهان، به‌تازگی از یک سرمایه‌گذاری عظیم ۱۰ میلیارد دلاری برای ساخت آزمایشگاه‌های تحقیقاتی جدید، همین‌جا در آمریکا، خبر داده است.
🔴
این شرکت کمک می‌کند آمریکا در هوش مصنوعی و رایانش پیشرفته همچنان در خط مقدم مطلق باقی بماند!
🇺🇸
🔴
به‌دلیل سیاست‌های عالی ما، شرکت‌ها در حال سرمایه‌گذاری تریلیون‌ها دلار هستند.
🔴
من کاملاً روشن کرده‌ام که آمریکا راه را به‌سوی یک عصر طلایی جدید در علم رهبری خواهد کرد. نتایج خودشان گویای همه‌چیز هستند: در دوران دولت من، شرکت‌ها تریلیون‌ها دلار سرمایه‌گذاری می‌کنند، چون می‌دانند آمریکا بهترین مکان جهان برای ساختن، اختراع کردن و رشد کردن است.
🔴
ما در حال تقویت اقتصادمان هستیم و خیلی بزرگ پیروز می‌شویم!
🔴
عصر طلایی آمریکا همین حالا اینجاست. MAGA!
🇺🇸
🇺🇸
🇺🇸
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144156" target="_blank">📅 23:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144155">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5uLhYFX3Nu89OHx0ZtizUgzcCduDVO3zU07MGMIZ4m1kespeeHMgYiGiG3scr_MrxB36klXxZZ51qMwQqrv8wdU4HVVRtxGJIXZ-nceuGRfq7jj9O3vqIid9Bshs5t9PYhg045zFGdpipE0F97uk0r7WAbYmwdud5A443VXDG09geUJYN5L0B5owAjzcv3MwA-ga7MuhvY7bVbuWFq_7MifxoNduXZ_tWT_xrUFejYwupTX-UZ4Pr3W0n6eUCmmPEf_EdBcEHjYPt4J6EoWyfnNR9PTrQGwsjfu_WMRgDQjrXdiM0jm16nZeXlRVQlDhaI-1RHiMcXzz_sYFL5_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ر
ئیس کمیسیون امنیت ملی: تنها مسیر نجات آمریکا، بازگشت به تفاهم‌نامه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/144155" target="_blank">📅 23:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144154">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
محسن رضایی: اگر محاصره ادامه پیدا کند، ما منافع اقتصادی آمریکا را صد در صد و با شدت و قدرت هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/144154" target="_blank">📅 23:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144153">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ضاحیه و بیروت خط قرمز جمهوری اسلامی هستن و اگه اسرائیل این مناطق لبنان رو بزنه بهش حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/144153" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وال استریت ژورنال : ترامپ منتظر نتایج تاثیر جنگ اقتصادی علیه ایران است. ترامپ دیگر اهمیتی برای یادداشت تفاهم با ایران قائل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/144152" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ضاحیه و بیروت خط قرمز جمهوری اسلامی هستن و اگه اسرائیل این مناطق لبنان رو بزنه بهش حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144151" target="_blank">📅 23:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه مصر و روسیه درباره پیشنهاد مشترک ایران و عمان برای ایجاد یک کریدور موقت دریایی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144150" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ایران ۸۰ میلیون بشکه نفت در دوره آتش‌بس صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/144149" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
این وسط کافه بابک زنجانی پلمپ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144148" target="_blank">📅 22:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c42582d38c.mp4?token=G5x3GAMVnXfJhC7QMqGMXZVMasw_ti1Jpy74WtILMpwKIGionUaOUmO58UmRZXTAGtvbF9_-zTq3kr8MYJudc7uTQH7h6v22j1UwjstG1KRjzCSV9sLBNqzo8IdyGIn-q8JB6nc4EuCVOhMLdn-uP9IwsjbqZCC0UmRGBgiGQrlw-r9TeFP3xaWvoUnBeCmRUAWR_hbqzdpmmCIQZzSlwCznMe5GAIJEp9ExpCnacDCjlSkDrmi9YvL6zxtHCJ2IgIpbWQB61Bl3Zo0QglhT6lkkfgcS9wGl_Eivlw5dFp2CaX7n3HBmJNAg14QfHrCjEGg0qo46_mSdvAFF3lDJ4AGdKxjOtbfJ_p58lBaTsOAyXQ2qvUjpou-XiXrLLHKiRvArILjkFcoZQhq4cVJGag8NFSOv3Qra0RNX4ykbr3iBz1vGelaxxSv6dxzMwx7L5VUTC7OBXTuOaj0nLnHrmvp7-6NGI4beKeP7mWhTxyrZFwonlj0zLMyO6-FjJhGz1Ehr3ZWD0vAXso3JSqmDV_RdrdoRD-txo5SrgH2HKrdbx8BcxyxviXBrTMllrMqL_-GkSICjk_3i3WzXLHfuXqyXU1e0x7WoPbD3J2qocJAXHnJNezDJxBJN1QJT_KptcjLUtQtpAcHxBSozgjIEYU-eOggQz-AgMCBbSz0rtMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c42582d38c.mp4?token=G5x3GAMVnXfJhC7QMqGMXZVMasw_ti1Jpy74WtILMpwKIGionUaOUmO58UmRZXTAGtvbF9_-zTq3kr8MYJudc7uTQH7h6v22j1UwjstG1KRjzCSV9sLBNqzo8IdyGIn-q8JB6nc4EuCVOhMLdn-uP9IwsjbqZCC0UmRGBgiGQrlw-r9TeFP3xaWvoUnBeCmRUAWR_hbqzdpmmCIQZzSlwCznMe5GAIJEp9ExpCnacDCjlSkDrmi9YvL6zxtHCJ2IgIpbWQB61Bl3Zo0QglhT6lkkfgcS9wGl_Eivlw5dFp2CaX7n3HBmJNAg14QfHrCjEGg0qo46_mSdvAFF3lDJ4AGdKxjOtbfJ_p58lBaTsOAyXQ2qvUjpou-XiXrLLHKiRvArILjkFcoZQhq4cVJGag8NFSOv3Qra0RNX4ykbr3iBz1vGelaxxSv6dxzMwx7L5VUTC7OBXTuOaj0nLnHrmvp7-6NGI4beKeP7mWhTxyrZFwonlj0zLMyO6-FjJhGz1Ehr3ZWD0vAXso3JSqmDV_RdrdoRD-txo5SrgH2HKrdbx8BcxyxviXBrTMllrMqL_-GkSICjk_3i3WzXLHfuXqyXU1e0x7WoPbD3J2qocJAXHnJNezDJxBJN1QJT_KptcjLUtQtpAcHxBSozgjIEYU-eOggQz-AgMCBbSz0rtMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر سابق اسرائیل:
دخترم ابیگیل، زمانی که افکار عمومی علیه ما شروع به تغییر کرده بود، در شهری در کرواسی بود.
🔴
او در صف بستنی ایستاده بود. فروشنده بستنی را برایش آماده کرده بود، اما بعد از او پرسید: "از اسرائیل هستی؟"
🔴
دخترم گفت: "بله."
🔴
فروشنده بستنی را برداشت، گفت: "اسرائیل؟ نه" و آن را دور انداخت.
🔴
دخترم به او نگاه کرد و گفت: "Fu*k you." من واقعاً به او افتخار می‌کنم. خیلی زیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/144147" target="_blank">📅 22:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عراقچی: کشورهای منطقه نباید اجازه استفاده آمریکا از خاک خود علیه ایران را بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/144146" target="_blank">📅 22:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144145">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/359a9e5dcb.mp4?token=GRDwPNA2THryTvt04lxbDFntlgS4KSUPN76gMbhQNi7eeq2hR3oHYG6FqNZE9bil4hMb6keHlEgOyMJx_jinsdcWbzrpu681lzF2XHr4VQE6IuZJ3acoSHWHoWN8FkW-d-dmWrUtd3uHpy-06vBerREiecUPlRcJ-oTxMEzFk27MDwgV2coNcCHsnzppPaQMpCgWbppLimIAVzMJrPqXrZAtgIIR2zbnFMpHKYgxl06-AEttkINq9qlsAUIlr75LjiT3cZ-1JPfLfk_gbQTKNQxefD5cdeIyMmkRg1eEEQo9SnlGuhcUtbyx09novSrelUIXsSFUyAlW7FAKKYERhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/359a9e5dcb.mp4?token=GRDwPNA2THryTvt04lxbDFntlgS4KSUPN76gMbhQNi7eeq2hR3oHYG6FqNZE9bil4hMb6keHlEgOyMJx_jinsdcWbzrpu681lzF2XHr4VQE6IuZJ3acoSHWHoWN8FkW-d-dmWrUtd3uHpy-06vBerREiecUPlRcJ-oTxMEzFk27MDwgV2coNcCHsnzppPaQMpCgWbppLimIAVzMJrPqXrZAtgIIR2zbnFMpHKYgxl06-AEttkINq9qlsAUIlr75LjiT3cZ-1JPfLfk_gbQTKNQxefD5cdeIyMmkRg1eEEQo9SnlGuhcUtbyx09novSrelUIXsSFUyAlW7FAKKYERhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سلاح ضد پهپاد جدید اوکراین برای مقابله با کوادهای FPV
🔴
این گجت جیبی یک پرتابگر تور است که تا ۲۵ متر برد دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/144145" target="_blank">📅 22:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/980d347019.mp4?token=Moxv-XQnPus98isXfU7vhdhpKLiDRDyt_JVhUoxlMmCjEC3qxoHe1vFsAl450lg-x7_CeaniQLuySryxjIdweS4oLijmDx1WfaGyhvAme0YnuTCi4vayHM4S5ExL9-rjacnDZXNSC44Xyl1CD4Gkl0YPTqaBqELQWlQXBMNa3aqgqKnYFLQdE5ykmjrhDsWovR_30vsS5F84_-zPPzSW_A7waqvDk9-8tE1lmg-3WnrVmXuk3E9lcpB60uIU_rseXBmY-l6j0__9I6Gk5dGvZPO_lNHvhy6z4SXSSgcoLO72Jd4tZJTWsrvbp_Md3zBD4Z_h6r9UR-t7fRawl_jbZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/980d347019.mp4?token=Moxv-XQnPus98isXfU7vhdhpKLiDRDyt_JVhUoxlMmCjEC3qxoHe1vFsAl450lg-x7_CeaniQLuySryxjIdweS4oLijmDx1WfaGyhvAme0YnuTCi4vayHM4S5ExL9-rjacnDZXNSC44Xyl1CD4Gkl0YPTqaBqELQWlQXBMNa3aqgqKnYFLQdE5ykmjrhDsWovR_30vsS5F84_-zPPzSW_A7waqvDk9-8tE1lmg-3WnrVmXuk3E9lcpB60uIU_rseXBmY-l6j0__9I6Gk5dGvZPO_lNHvhy6z4SXSSgcoLO72Jd4tZJTWsrvbp_Md3zBD4Z_h6r9UR-t7fRawl_jbZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر دانمارک، مت فریدریکسن:
ما باید مرزهای خود را امن کنیم. اخیراً دوباره شاهد بودیم که مهاجرت تهدیدی جدی و ملموس برای اروپا ایجاد می‌کند.
🔴
کاملاً حیاتی است که کنترل مرزهای خود را در دست داشته باشیم و متحد بمانیم تا از ایمنی و امنیت جوامع و شهروندان خود اطمینان حاصل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/144144" target="_blank">📅 21:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHsPJBdc9l4ZeNW_sIv4alP7kNBiAZ24ZkLyQQiOZXEedHuSmyUDO9oIESRsjSfYSIoBDbWvdMf_ldLxuzQgJ62fYF0AKDfq6l5G9TYWHbZqaYIYgx7REsR123nBx8rui6JeFRVvwjWfa6zbSa80skXGtx8wDEonPDlMFWMeGP_nGaJeHxZTgY3bZ1KpJk964EFaAqpIsyzLWdPFo-XxNkbHjmyBKd0Bn5QDHMKEvlry3mHfO5t9w4br2_Qx7GVyEXyIzLBD35xsXsPx5lfQOKBKiOz2t6Y9J6SK1r7_GimcIbEz2AolVXbyH9W46bnDLd5YH3GWBdFUADkWl7Cq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفتکش گاز مایع «سیگیت» که تحت تحریم‌های آمریکا قرار دارد، از مسیر تعیین‌شده ایران عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/144143" target="_blank">📅 21:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d6a27a6a.mp4?token=Vzlggo0Xv-pzwKnkB9As1e1cvukIhqFN48E5EW8NUxG5jTNHOg8PbCa4kajNWZB5_9t6_YAqiIfnc1efU0C0nA8o535B8tzGqIVf6ARXbt9MzWBBNkE--zi3zx7TcLqfCnlzUCO2g8n-oP2LOQ3zyZBbpgvgWYRIU7Xzpa9bFaC4zvwLFptwcSSocJvATbbb-3kSAsq2dAEPUaHg-rlr-sKvBAQ4OYmbySt5tEJ0iZJ6ZoGC-3Jh0adG8iJgD5tWbT4xvFXL65K9FGtseAD9cJKiK62a1KiOarQDUnzpRT-htQ1UENur37uaHdRBomY0bf3QQ2xv_H7z_meZ_P7SfgGfXT65Y0cE_SUMnBAMfYsHOyyYD-nRZMblaMlVqQBwaryApfZZBtme54WBUWnoZdTJaPIGLhpzqOF0xSWhrNl3CkzMdDb5YuQBN36VLxnv-7Mf0dMJ-XkRMcwZrdQiy6dFFOEvsf8jXjwbng4GWGZLaWqCT6yE699zYRrw8zvi1yDedQDOkwXwPPxBMwt87jO7-OdOxtkIy52r8upjAZdixDz2drEHwkuUtjvvTXjtY-hM1VG0w8hijruQilQJCk3rK22x8pYtFyrd7QYQ4SSGJ5e8Y3FrwCK-UYgepg6Eza6v0jW5DgvG99OHavHA8s9gIjlav9mRBiALfhpq9N0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d6a27a6a.mp4?token=Vzlggo0Xv-pzwKnkB9As1e1cvukIhqFN48E5EW8NUxG5jTNHOg8PbCa4kajNWZB5_9t6_YAqiIfnc1efU0C0nA8o535B8tzGqIVf6ARXbt9MzWBBNkE--zi3zx7TcLqfCnlzUCO2g8n-oP2LOQ3zyZBbpgvgWYRIU7Xzpa9bFaC4zvwLFptwcSSocJvATbbb-3kSAsq2dAEPUaHg-rlr-sKvBAQ4OYmbySt5tEJ0iZJ6ZoGC-3Jh0adG8iJgD5tWbT4xvFXL65K9FGtseAD9cJKiK62a1KiOarQDUnzpRT-htQ1UENur37uaHdRBomY0bf3QQ2xv_H7z_meZ_P7SfgGfXT65Y0cE_SUMnBAMfYsHOyyYD-nRZMblaMlVqQBwaryApfZZBtme54WBUWnoZdTJaPIGLhpzqOF0xSWhrNl3CkzMdDb5YuQBN36VLxnv-7Mf0dMJ-XkRMcwZrdQiy6dFFOEvsf8jXjwbng4GWGZLaWqCT6yE699zYRrw8zvi1yDedQDOkwXwPPxBMwt87jO7-OdOxtkIy52r8upjAZdixDz2drEHwkuUtjvvTXjtY-hM1VG0w8hijruQilQJCk3rK22x8pYtFyrd7QYQ4SSGJ5e8Y3FrwCK-UYgepg6Eza6v0jW5DgvG99OHavHA8s9gIjlav9mRBiALfhpq9N0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
البرایج ای. کالبی، معاون وزیر جنگ در امور سیاست: ایالات متحده از این قاره خارج نخواهد شد. همچنین، از این ائتلاف نیز خارج نخواهد شد.
🔴
ما به ریشه‌های اصلی ناتو باز خواهیم گشت، جایی که اروپا نقش رهبری را ایفا خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/144142" target="_blank">📅 21:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
گزارشگر: چرا این کارها را با متحدان آمریکا انجام می‌دهید به جای دشمنان آمریکا؟
🔴
پرزیدنت ترامپ: مقامات کانادایی افراد بدجنسی هستند. آن‌ها با ما بسیار بدرفتاری کردند.
🔴
بدترین کشور برای مذاکره در زمینه تجارت کیست؟ کانادا. آن‌ها احساس حق دارند. ما نمی‌توانیم این را بپذیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/144141" target="_blank">📅 21:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/وال استریت ژورنال:  کاخ سفید پیشنهاد بازگشت به تفاهم‌نامه اسلام‌آباد که توسط پاکستان ارائه شده بود را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/144140" target="_blank">📅 21:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c02d4935.mp4?token=I5fXFV6lAZPuVc8lbCQdoijYDkKoQNjbMgCSoP_IyFaeSQNTXOe1GoAZJ-YoU6INDH2Z4tOAM-sKtnM2ECFRwtYauUso2C2KjNt9B3Qucyl6n04V3EVxj3ZQDhu_IzgcWoQsV225Nr91V6xZWlPOINM4oSlzEkeckJU3Ie1mBCDu5TaBbbVyBS33SM0FH_1YmaHFTcRnvkU41jwQEH9P1QLMXPuTzuBM6M2ttplFNozD-BMqH6CDoEhROWMhig94LHDhSUlUWMoaYdqLhAY7wvDuIzzBxiCPE6LucAHqA-gXV7wNU8hkwehaLvzSQJZx2JEY1XyRJl5F5JN3F7lH7z9xATUK55qU_yKSvPjf3J1OV8l9TOOp9udFnGbyFfa9ZmM0YVHiCHlBVZD3O9Gw1kF85n3IFn9qKqqvNqDScg6slez5w5b1M1cvvB4GKgyXybgW8XPjHDY5DbBtpxqphVluaUIz4iVRGsuRCZX5nCAvPx1n_yjZq8_lTcD99doXUFK5z90L6BTUTMseAhNX3pohxwyhhmPlL6CEtiu749a0MQfw3EET7bqwUYYjC9bFm3eIhV4cuFEpaLEVFaucsNme2xolBVgiqkOKe7FsGFxlfnGwhAPdXkGLJ8Ypqt589R9edlrDllITLKAMsfmW6cytffOVPwXtqdb9cKcvr3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c02d4935.mp4?token=I5fXFV6lAZPuVc8lbCQdoijYDkKoQNjbMgCSoP_IyFaeSQNTXOe1GoAZJ-YoU6INDH2Z4tOAM-sKtnM2ECFRwtYauUso2C2KjNt9B3Qucyl6n04V3EVxj3ZQDhu_IzgcWoQsV225Nr91V6xZWlPOINM4oSlzEkeckJU3Ie1mBCDu5TaBbbVyBS33SM0FH_1YmaHFTcRnvkU41jwQEH9P1QLMXPuTzuBM6M2ttplFNozD-BMqH6CDoEhROWMhig94LHDhSUlUWMoaYdqLhAY7wvDuIzzBxiCPE6LucAHqA-gXV7wNU8hkwehaLvzSQJZx2JEY1XyRJl5F5JN3F7lH7z9xATUK55qU_yKSvPjf3J1OV8l9TOOp9udFnGbyFfa9ZmM0YVHiCHlBVZD3O9Gw1kF85n3IFn9qKqqvNqDScg6slez5w5b1M1cvvB4GKgyXybgW8XPjHDY5DbBtpxqphVluaUIz4iVRGsuRCZX5nCAvPx1n_yjZq8_lTcD99doXUFK5z90L6BTUTMseAhNX3pohxwyhhmPlL6CEtiu749a0MQfw3EET7bqwUYYjC9bFm3eIhV4cuFEpaLEVFaucsNme2xolBVgiqkOKe7FsGFxlfnGwhAPdXkGLJ8Ypqt589R9edlrDllITLKAMsfmW6cytffOVPwXtqdb9cKcvr3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: تد کروز بارها به یک نامزدی احتمالی برای انتخابات ریاست‌جمهوری ۲۰۲۸ اشاره کرده است.
🔴
ترامپ
:
او بسیار با استعداد است. فکر می‌کنم ممکن است این کار را انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/144139" target="_blank">📅 21:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=uN8srm8-KncDwtu9awGbFM4oZSCPMua4tNX29dmkvQlqEo41yzcmgXduUErqoYkrvs_bo1oWLkmFA2vRRTAFrfD_vA3SmkdqmAUneF1HojAD25KDm58PFwW3koQsW-PfA9DsLLTmVIuIDFBER6McYz5JnyNci5yWFbJg_8rmc5QXeK0BIKXj3_FopQAZJmdp9ebVZCA5GqK34VjyBsHrc7j_kLC1ZnSzv8gtkv0EDez4CgEuGrVQgLmkbqQOOTyZBq49i-KSYoVSvkZzcSqewfNhR3aqvOSKSjNUU45RZeZbJZGer8yFQyYciWBbRnBXV_P2Plq7zqh7EGhGvB3MRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=uN8srm8-KncDwtu9awGbFM4oZSCPMua4tNX29dmkvQlqEo41yzcmgXduUErqoYkrvs_bo1oWLkmFA2vRRTAFrfD_vA3SmkdqmAUneF1HojAD25KDm58PFwW3koQsW-PfA9DsLLTmVIuIDFBER6McYz5JnyNci5yWFbJg_8rmc5QXeK0BIKXj3_FopQAZJmdp9ebVZCA5GqK34VjyBsHrc7j_kLC1ZnSzv8gtkv0EDez4CgEuGrVQgLmkbqQOOTyZBq49i-KSYoVSvkZzcSqewfNhR3aqvOSKSjNUU45RZeZbJZGer8yFQyYciWBbRnBXV_P2Plq7zqh7EGhGvB3MRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
ما یک خلیج داریم. ما یک دریاچه داریم. حالا به یک اقیانوس نیاز داریم.
پس شاید مجبور شویم نام اقیانوس اطلس یا اقیانوس آرام را تغییر دهیم.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/144138" target="_blank">📅 21:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
طلای 40میلیونی
😳
⁉️
تحلیل ترسناک نوستراداموس ایران
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/144137" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
آکسیوس: آمریکا و ونزوئلا به توافقی عظیم درباره نفت نزدیک شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/144136" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرنگار: «چرا بانک‌های چینی را که با ایران تجارت می‌کنند تحریم نمی‌کنید؟»
🔴
ترامپ: «چه کسی گفته من این کار را نمی‌کنم؟ شما نمی‌دانید که آیا دارم این کار را انجام می‌دهم یا نه. من مجبور نیستم همه‌چیز را اعلام کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/144135" target="_blank">📅 21:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e815d502.mp4?token=a9LW0j4rpLSY4C9V_2pmjZQfTUMGKCfA729DqCLRk7uiLcOIn5iDtZDMWgPAkHLYjv3HYzWpwm22jrqfPvQ0zYw4IUTxM2Uzq_3uAOrquYJstWCeLHvXV3wfXPm_b4_KibeSOHuDP1gVkxO684oPxuNFq_Qg8AqP-KnHonbJhEZ8KX3uZqK3eZE_owIe6jVf3Z57fjP2QdDNrjT3suVM-m5ZtxzK89gsrq6DRHx7sOKsmGNziQS2n6CqMWoTTeiYmOUaL4uN0ACliGtqv-V-O9J3l6VLTax8-ZQjrQO0NgmQXOYOTTQze3vFFtItrdm-uAvqTe46r92d1XIfvXHrjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e815d502.mp4?token=a9LW0j4rpLSY4C9V_2pmjZQfTUMGKCfA729DqCLRk7uiLcOIn5iDtZDMWgPAkHLYjv3HYzWpwm22jrqfPvQ0zYw4IUTxM2Uzq_3uAOrquYJstWCeLHvXV3wfXPm_b4_KibeSOHuDP1gVkxO684oPxuNFq_Qg8AqP-KnHonbJhEZ8KX3uZqK3eZE_owIe6jVf3Z57fjP2QdDNrjT3suVM-m5ZtxzK89gsrq6DRHx7sOKsmGNziQS2n6CqMWoTTeiYmOUaL4uN0ACliGtqv-V-O9J3l6VLTax8-ZQjrQO0NgmQXOYOTTQze3vFFtItrdm-uAvqTe46r92d1XIfvXHrjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
تاکنون، فکر می‌کنم روسیه رفتار بسیار خوبی داشته است، در ارتباط با تنگه هرمز.
🔴
برای هر کاری که آن‌ها انجام می‌دهند، ما نیز انجام می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144134" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde5f4e82e.mp4?token=nRsXzoMprYGAk0Yp2tfDrsgZ5znXsEcg8vywmDYjxipeT-9H8OyBkLxN-Q73F8kpUTe5LLneySI3r7uMxbR8SbASrLlVZ_rPhD3dq2xeoH1xP_BOWoIuS1zNxy94Vbbr4mXzP9pt6L-0Y41lgb08H_TJYn5fevpnMsM-kR5I0VwVUyMipWcOyUkKTJ_91wmXQXKQ60S5k_pyjcZKbcvQDiEjG7fRnRxsaaKr3Sg5EjBw-4aKakcJyrZA6uxfunnuqRJOXv2TD9LN1EiF3L5nYKLJzHmxY0KjUSjjkh6xRsfwzNS8nD46yecxQVjB47Sw305ghQiD1s9Xt3Pjxmh1BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde5f4e82e.mp4?token=nRsXzoMprYGAk0Yp2tfDrsgZ5znXsEcg8vywmDYjxipeT-9H8OyBkLxN-Q73F8kpUTe5LLneySI3r7uMxbR8SbASrLlVZ_rPhD3dq2xeoH1xP_BOWoIuS1zNxy94Vbbr4mXzP9pt6L-0Y41lgb08H_TJYn5fevpnMsM-kR5I0VwVUyMipWcOyUkKTJ_91wmXQXKQ60S5k_pyjcZKbcvQDiEjG7fRnRxsaaKr3Sg5EjBw-4aKakcJyrZA6uxfunnuqRJOXv2TD9LN1EiF3L5nYKLJzHmxY0KjUSjjkh6xRsfwzNS8nD46yecxQVjB47Sw305ghQiD1s9Xt3Pjxmh1BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا
:
ما کانادا را بدون هیچ بهایی دفاع می‌کنیم. چیزی به دست نمی‌آوریم.
🔴
آن‌ها به ما پولی برای دفاع از کانادا نمی‌دهند، اما ما کانادا را دفاع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/144133" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144132">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_rQ90fEtXfaVH2aoDdLAzVGfTpdDqLzjGNXfm7H2RmMvlGNYpDjtvvBLLURhTO3vB0k_t1zqhHlQzl0PEeNOPogkHBDKfaqtcyo1v0wOJzpZA_z8fjImtAijFR8vHi0zzV7PDQkDnt-2ubpxXfkC46oMY7cAYhRkKlJtbAWKBSdVBmtHMvQvDp1hvrDPlwDOfmWD6ECfrX9l6D1oHUwmId2ppMgETQany0sfBXwLvEvRkKW9THeLckg9UnovUd7Lt7ZZ7sInV-HHZpda45_0VLDQau7opbOBR_vpnCdzS9Aix_UYZFuVpZkV0EPMb4PwmH1waTpR5mUPZCjpesZch6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=QWN62fuv2Ra02hTcRAsKnirR2Gc5iHOGMEzEr4QNGDwwbPCwAbqAK2rj9V5EPgvufArotbPhnBHBAGGsCWoJ4JVc8OFu_T-lIQ9WhhiKzjD1Wsr2bV7EdNWx1PCCPDoz9wVvv4wkRwnD-ui7fnrDBlSGXyvbMn3jYC2XLhviFFbANjyEJP0d82EErlws_52ogNPeF15g9asXW89CSqNE_Tu-eA4VbKjY4CjJa61XN6alkOkujIoXjZmZeyP_nCHX8X5rscgJIuDWYMBMBpmIW-rP0I8eaLyD-J5vSxFR5uL6GH3vcTLv1QEnsRF_ilzuJWFrdnGLjbZ6WCAWnMBR_rQ90fEtXfaVH2aoDdLAzVGfTpdDqLzjGNXfm7H2RmMvlGNYpDjtvvBLLURhTO3vB0k_t1zqhHlQzl0PEeNOPogkHBDKfaqtcyo1v0wOJzpZA_z8fjImtAijFR8vHi0zzV7PDQkDnt-2ubpxXfkC46oMY7cAYhRkKlJtbAWKBSdVBmtHMvQvDp1hvrDPlwDOfmWD6ECfrX9l6D1oHUwmId2ppMgETQany0sfBXwLvEvRkKW9THeLckg9UnovUd7Lt7ZZ7sInV-HHZpda45_0VLDQau7opbOBR_vpnCdzS9Aix_UYZFuVpZkV0EPMb4PwmH1waTpR5mUPZCjpesZch6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ فرمان اجرایی‌ای برای «تغییر» نام دریاچه انتاریو به دریاچه آمریکا امضا می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/144132" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144131">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b824f45c5.mp4?token=lmxksu1glKiIPMZQKt5vd27UylaG2TRq4ZdrmJEwKksBdx-hg1mhQJfNjZ-D33sq1jzW5iuJcRZ6NNlshPD-p8WS9Ugpr0QBCAVmRVvMqpw5Ube9zVmygNpsfVQio6BUxD0sEdtSXWirDSH8dVl3O13_Agm-6LDLmQarwZpHly8q8qFOI74XVfsG-qbTpIY-iXWyqmO2m9nxTWvKM4aJ79r_2CkBci60C6ruQnjJA3BGW4iMX5nlumpWKh_mvsg80msfRU-AKyibjozH6s5BYvR1LGqTePYFmttCxvJ4rdn9Qnmw678vjV7pk0qdBlXJRicA-cfIJ6ZfbAsFD2NKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b824f45c5.mp4?token=lmxksu1glKiIPMZQKt5vd27UylaG2TRq4ZdrmJEwKksBdx-hg1mhQJfNjZ-D33sq1jzW5iuJcRZ6NNlshPD-p8WS9Ugpr0QBCAVmRVvMqpw5Ube9zVmygNpsfVQio6BUxD0sEdtSXWirDSH8dVl3O13_Agm-6LDLmQarwZpHly8q8qFOI74XVfsG-qbTpIY-iXWyqmO2m9nxTWvKM4aJ79r_2CkBci60C6ruQnjJA3BGW4iMX5nlumpWKh_mvsg80msfRU-AKyibjozH6s5BYvR1LGqTePYFmttCxvJ4rdn9Qnmw678vjV7pk0qdBlXJRicA-cfIJ6ZfbAsFD2NKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: با چه رهبرانی در مورد قطع روابط با ایران صحبت کرده‌اید؟
🔴
ترامپ: چیز زیادی برای گفتن وجود ندارد. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه [هرمز] باز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/144131" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144130">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم
🔴
نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/144130" target="_blank">📅 21:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144129">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3d09aa98d.mp4?token=JpFM-nxVrfEAy-IvVTxBZAbwbDrwZ03pS2or85nAGrvfx4Q-ZiNjVbokyNO9j1R2fSU9Vi5F-92XhNUB7Cmz8HIm4k8NW79-BLzE0ouCCpySY6xfwBu3vsijrTRs1Nigr0IOiQ40BQ08vVpo3waoffEdl7rmi0PYhCbwL-cQQ1yR-6Z5dy7FPNb88z5fAVZwkjItIm6rverlj0BWvfZ_yHxyKyXab0VlaDRrje6WWBJAiBqqGTtPa_b8Wf3ESMHApYgyZeItL_R-qc5ELiLf4NZpiyPpeDEraOnuKPqmKlkFit63uCPdzGiExUVYaLxfXrT3VYxssFUKMIdsmqvFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3d09aa98d.mp4?token=JpFM-nxVrfEAy-IvVTxBZAbwbDrwZ03pS2or85nAGrvfx4Q-ZiNjVbokyNO9j1R2fSU9Vi5F-92XhNUB7Cmz8HIm4k8NW79-BLzE0ouCCpySY6xfwBu3vsijrTRs1Nigr0IOiQ40BQ08vVpo3waoffEdl7rmi0PYhCbwL-cQQ1yR-6Z5dy7FPNb88z5fAVZwkjItIm6rverlj0BWvfZ_yHxyKyXab0VlaDRrje6WWBJAiBqqGTtPa_b8Wf3ESMHApYgyZeItL_R-qc5ELiLf4NZpiyPpeDEraOnuKPqmKlkFit63uCPdzGiExUVYaLxfXrT3VYxssFUKMIdsmqvFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دریاچه مشترک با کانادا:
ما قرار است نام دریاچه انتاریو را به دریاچه آمریکا تغییر دهیم، با اثرگذاری فوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/144129" target="_blank">📅 21:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144128">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دونالد ترامپ در گفتگو با آکسیوس: نگران حمله روسیه به ناتو نیستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144128" target="_blank">📅 21:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxBrtvGkXtoZukTBuF61KhLvUpKosQTCO1T8TuBu4osQWj9F22XECLgmC-HrbuzCVkkd4HB2Xtd-0GTz6yEly_SMJPfaETX6113hmTIN9xBNbw0R5oW8nHBp-2gXBbUZkVwLv__JkFbqth3x8r7erxvXOv6ULhRCWQkU53ZkHj41oLheKV7RIgIL6IDwPsdmj9mxMyyUpJNc4P0QJen0TUzM1TQ92ElBqNY0BqC2itsJ2cD3PaS2H9dX2EkU3A_PGVqfr9DfKyF5O2-GvokBpunH3ZTSSj279fwo0ULNVvYZXV2_NGc0LPoF0nLaD9wKxU0ForNoA3MQOCc8L1C0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف، اسکات بسنت (وزیر خزانه‌داری ایالات متحده) رو اسکاتی خطاب کرد و در جواب توئیت او نوشت:
🔴
این امپراتوری رو به زوال به جای اینکه میلیاردها دلار را به نیابت تروریستی خود، اسرائیل، و ۷۵۰ پایگاه سرازیر کند، می‌توانست آن پول را صرف مردم خودش کند، اما نه، این برای این رژیم زیادی منطقی است.
🔴
اسکاتی، مرد [؟]، اعتبارت در خطر است. کاری بکن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/144127" target="_blank">📅 20:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عراق برای نخستین بار از زمان آغاز جنگ علیه ایران، به خریداران نفت خام خود این امکان را ارائه می‌کند که محموله‌های نفتی را خارج از خلیج فارس تحویل بگیرند
🔴
خریداران می‌توانند محموله‌ها را از طریق انتقال کشتی‌ به کشتی در نزدیکی سواحل عمان دریافت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/144126" target="_blank">📅 20:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه های عبری: اسرائیل به آمریکا اطلاع داده که از عملکرد ارتش لبنان در مقابله با حزب‌الله ناراضی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/144125" target="_blank">📅 20:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTk0Udr1q3kdzveNFM3gYL56HqVONw_mUDeJkvddZJXRddWs7jG2k0EVV3M2wuSd2KshFQxj1YUSp60QMXdZR2OSpoBHKII5BChNnWwbr-RmLd68LbRTNbzi92KovX8AM5G8LzR5Jz-4AaVXqR0X4cJ_07U-d6I_Y8oBmzYJDQDFklWyUn5xNM6Scwn_bj3GR7B9tzRB9xXLPuHJsvJl1n-6HL4Lbh7qw35zREunjDrP-KFWpDnedo--iHc2GyCkPuKK5TMxIkDAErUMeo9lWvUy9MW1U3QsJTKc9p0DzsOFShxdqK_RKI4ivzqlvKRHRoaGO1nFfrRy5Mqs9BAIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امشب یه ماه‌گرفتگی تقریباً کامل که بهش می‌گن ماه خونین (Blood Moon)، از سراسر آمریکای شمالی و جنوبی قابل دیدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/144124" target="_blank">📅 20:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ادعای ایسلامیک مارشال محسن رضایی: آمریکا شرارت کند بلایی سرشان می‌آوریم که در تاریخ ثبت شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144123" target="_blank">📅 20:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144121">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef01d16472.mp4?token=vYWG7C8aDerStAVo9Et8DgzTSuDV0C6QwftpGwZgo6h68fW4iNRPXgfVV0781MOhW2AX8tvfq16Rd00h0A_35EAWR2hbfR0SAnEGG7Ci60NEsDNfnoVJS0rZYDxLYOxp75eLKp95aDbwhOGnw4NDHO9v5pt-qO-lwdY7o-5DpDXYQjF9HS4UiQmWm2FhsQBY770wnfyDjHm-ejEPwmza5syFB_-2SUS24NGQ1pEd5jTOY-SIRPsTm2ZvGkNBW1RcUGZjUJYkG4KqauhYlx56X1YfU8tgAL-y417hMYAmZoF54p-C-Tul53gH-Qxu3DIcs2OT1YvpLVcoAvlSjl8zmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef01d16472.mp4?token=vYWG7C8aDerStAVo9Et8DgzTSuDV0C6QwftpGwZgo6h68fW4iNRPXgfVV0781MOhW2AX8tvfq16Rd00h0A_35EAWR2hbfR0SAnEGG7Ci60NEsDNfnoVJS0rZYDxLYOxp75eLKp95aDbwhOGnw4NDHO9v5pt-qO-lwdY7o-5DpDXYQjF9HS4UiQmWm2FhsQBY770wnfyDjHm-ejEPwmza5syFB_-2SUS24NGQ1pEd5jTOY-SIRPsTm2ZvGkNBW1RcUGZjUJYkG4KqauhYlx56X1YfU8tgAL-y417hMYAmZoF54p-C-Tul53gH-Qxu3DIcs2OT1YvpLVcoAvlSjl8zmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب یک ارزشی در حرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/144121" target="_blank">📅 20:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144120">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udNFQO-wkSA-bHFfRcHWGqvItobz1vW1HfouYSx2oE1LTY1DP8KP4mfTQlhTJDQPV60stR8wI0awVgXnA4wOYzoeOE6QNxZDH91TvHCgzFSqYM1advxFD2Go1jMpKUpzrKYhfogyfrYXVoDK48Enk1tfPQDAELs5VsKOQIGoJWEgXTKvTX6kcmmfmOWHCMbsmVBVjGlZ4toY-h4aogO6w722cnIlqkao_OBSwoSBP194EdNI4JVYQSxPUUpgRRnTawlUUPZzaTNZISddpvdLlUoOkcNgmgZBiAWcWKnggR0GYG-GRVra2M2ZNUxrldGnJ0k1GixPheUb80y2bfec5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان UKMTO تایید کرد که تانکر نفتی کویتی به نام "السسلام ۲" دیروز در حین عبور از تنگه هرمز مورد اصابت قرار گرفت، که به احتمال بسیار زیاد این کار توسط نیروی دریایی سپاه انجام شده است
🔴
این کشتی پس از آن در جزیره تواککل کشور عمان پهلو گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/144120" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144119">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
اینروزا این پسره حسابی سر و صدا کرده با سیگنالاش
🔥
هرچی گفته سود کردن مردم
😐
الانم یه تحلیل خفن از طلا زده
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144119" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144118">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
منبع آمریکایی به الجزیره: هیچ مذاکره‌ای با ایران در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144118" target="_blank">📅 20:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144117">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
منبع آمریکایی به الجزیره: هیچ مذاکره‌ای با ایران در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/144117" target="_blank">📅 20:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144116">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PW6IPQZyT6-Q5BYireJnq9kyfxJl06deiqXYRRej5atzaGuo3vnGndQ697FnWgh53_Yd6mhneyza3myan-iyZkg2a1TOwfMU68tyfWKijt5crreQ4VhHUmvQpyiWM9GKOccvFbiGB0YEAkMFJRfIPVBA5pkzMe1T5mBsrsOKZhdvvqPb7I7VjaDMBy_apJe_3wcuFCGz8fRyCi_s53wMa32Ngx0Rf1RXTOqH1iRzfamDSCfksKBgQwq8PpejceC6JeSq8KxKD0QXy89PAPSbX3VlwwVeIb4hOlrhx39yfJW4xUv7up99wvr9lTODdQvCi-Mf99HW5Mt4jEdv0FDPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط کافه بابک زنجانی پلمپ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144116" target="_blank">📅 19:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144114">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
پزشکیان: منطق حکم می‌کند اجرای تفاهم‌نامه به همان شیوه گذشته از سر گرفته شود و مسائل از مسیر گفت‌وگو حل‌وفصل گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/144114" target="_blank">📅 19:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144113">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDqvuuEXC0299cC5giX_n9XXxf9fThHaeeacV1KI-j4SGAKSOsakGpxblzJl3vg1_RZDrbgTymLUmf5BTdE4cAcSeyaWi6V9FZhGw9WJ434c5QQLMzfKAX-DsLRQsAFnbfE9-yR8KZa_qAVUMLNIxL0RYuS-Gp2jtHFyjVvUaBsoc4rTHAeYVGdDYyq7MXH_jHBRoaQY_GA_MDyB0qriGmuU7AES2bRsVPuhVDK1Gs-3ToZ55CUvVCgHcqqugSbgkGrAlZg4Lmw4CPb-FQWx7zRbvMoaWXHcSj8kC3tJ0C0FmMrI1A75CE79Fx3im9HZzEgmXnMce244DrpXy2-kHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی: همه چیز تحت کنترله
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/144113" target="_blank">📅 19:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144112">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6kQ5SwAvNIYIqACLZlhTRlpShpdSeGO7HfTNcYjhbyH_dsrivssxsRcC3C949EnR_roAkvb_skX9az9muJmeRTDLf3eo9RjRocBTeHguqjZtLKsFIQMVEf_702dXE2DcRwkZg2wukwpCOawx_2iBKNKMsIZ57HnBKkKl9s7SVXt0FbYFvB3DjiEwgX72REi2aYrQggW0QmvRSXLmG3AeHh6_3PnRnzeCB1I5uP3igK5vJsSmPSUrFrHkrv56f1d3jVTepvArKd7fPFjdzAFx8RH1KNIYKV8FRSe-f091gVP9yUJ5JbAjEIDOu0kog0CUch_Jwj-0krjLLlR2ZFJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رکنا: زهرا متقی، دختر ۱۲ ساله اهل لشکرآباد هشتگرد که ۸ روز پیش ناپدید شده بود، در شهرستان چهارباغ پیدا شد و به خونوادش تحویل داده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/144112" target="_blank">📅 19:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144111">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به فاکس نیوز:
توافق ایران و عمان برای ما اهمیتی ندارد؛ فشار اقتصادی را ادامه خواهیم داد و مذاکره‌ای با ایران نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/144111" target="_blank">📅 19:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144110">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر خارجه قطر در دیدار با پزشکیان:
روزهای آینده پرکار و پرفشار خواهد بود و تیم قطری از فردا فعالیت خود را آغاز خواهد کرد.
🔴
امیدواریم تلاش‌ها به نتایج مطلوب منجر شود و با بازگشت به فضای دیپلماسی، راه‌حل‌های عملی مورد بررسی قرار گیرد.
🔴
اطمینان داریم رئیس‌جمهور ایران از تلاش‌ها و تحرکات دیپلماتیک حمایت خواهد کرد.
🔴
درباره موضوع خلبانان نیز درهای قطر به روی ایران باز است و مسائل مربوط به برادران ایرانی با صداقت پیگیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144110" target="_blank">📅 19:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144109">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر خارجه قطر در دیدار با پزشکیان:
شیخ تمیم، رئیس‌جمهور ایران را همچون برادر می‌داند
.
باوجود تمام اتفاقات رخ‌داده، احترام عمیق و صادقانه میان دو کشور پابرجاست.
🔴
قطر به دنبال بازگرداندن ثبات به منطقه است و دست گشوده ایران به سوی کشورهای منطقه و تلاش جمهوری اسلامی برای تأمین امنیت و آرامش را به‌خوبی می‌بیند. امیدواریم با ادامه این رویکرد، مشکلات پیش‌رو برطرف شود.
🔴
مردم ایران برادران دینی ملت قطر هستند. جنگ از داخل منطقه آغاز نشد و از بیرون به منطقه تحمیل شد، اما هزینه‌های جنگ را همه کشورهای منطقه می‌پردازند. شرایط کنونی مسئولیتی مشترک بر دوش ملت‌های منطقه قرار داده است تا امنیت، توسعه و پیشرفت را برای همه فراهم کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/144109" target="_blank">📅 19:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144108">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پزشکیان در دیدار با وزیر خارجه قطر:
اتفاقاتی رخ داد که قابل قبول نبود، اما همچنان بر این باوریم که ایران و قطر دو کشور دوست و برادر هستند و می‌توان مسائل پیش‌آمده را با تفاهم حل کرد.
🔴
اتفاقاتی رخ داد که قابل قبول نبود، اما همچنان بر این باوریم که ایران و قطر دو کشور دوست و برادر هستند و می‌توان مسائل پیش‌آمده را با تفاهم حل کرد.
🔴
مسئولان آمریکایی باید صداهایی را که برای جلوگیری از بازگشت آرامش به منطقه تلاش می‌کنند، نادیده بگیرند. منافع عده‌ای در ادامه جنگ است، اما جمهوری اسلامی ایران معتقد است صلح و امنیت به سود ایران، منطقه و جهان خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/144108" target="_blank">📅 19:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144107">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXetL2MD8jpMv1-kisxmej_r1z8oGrR8pTmzLGSMKXkaXGUJC3t4T6sK7XKQaSt-c2h7RabrzsZ0myE1mEKQtWKBDsMOAJhGH3H0Gg0dpUjApHRsMdZiwFl_2VVX9l8_hoKmzagvlY_QJkQaCOTw5ix8q3FOL-8m36cDTmpf3-aCzITCBTj7Ex7QEv2PKm59koXS_akWJn_94EU34HaCvHLs7UdOl8pYeM6PvzTAD50uWTXEh05J9YSt6Op0arqmhT5quqcsswuxANpD-cIT8oR0-46tBEIU2veHsD3dpB7DevpCorHnILbH4jDro8AN4M_GD_dlTqjxLl0Ko8wGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اعلام اداره راهداری البرز، عملیات روکش آسفالت کنارگذر پل B1 آغاز شده و طی چند روز آینده به پایان می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/144107" target="_blank">📅 19:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144106">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
علی الزیدی نخست‌وزیر عراق با فرستاده رئیس جمهور مصر دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/144106" target="_blank">📅 18:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-WScbCGysEBq7BaeT_lnQS20HvGHH395_gwFog64aQzRD_zah37TJOhZUJci3XKln528E8xFrpjvYjdaxg2XgWjcFZ7J6miQWeQOsCB7TsI7dazKKVXjw3dbHU6nUVNJYTqeqYGAOK6JHRbSO0Fe8-odeXkcirwai3nrW9mZsJZEDzteoTVbbgG1YMrF_Kqh0kxSxkNfRQyQ7dzwGrexZ5adoNyBlK36yXLtgRcgcv6uiq82spCHXQpZPUZ4cThjcs1Yt9c-YsEzZLLodsG-qPIM75_N6tJU4paYFU4fApH5Twr0InD762KBlDBOm4cwh7rk-TIuqK2b3gl8m5WGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): نیروهای دفاعی اسرائیل فرماندهی حماس را که در اسارت ادان الکساندر، ماتان زنگاوکر و آورا منگیستو در نوار غزه مشارکت داشت، از بین برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/144105" target="_blank">📅 18:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144104">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZESZSKbs-xtihGjpv7frkOtp74vCTdybEu2NrLQoImZwfk7qp1uBUVMSq8BpFhTRidJR0mA8GJ3wPnLNKBO-gFP2x699Eg4ynUpXCes9XYpJ7kpeCP3qrs-oXHxy3v4Ure38Dunhk3ygnV76qcYosGfNtIm6fQtxtycf5_Evc-4obokwplDPJl8rDFH8LJEbZOxz_MgC_uQz_5Kk_Q_WD6__p5s-DLwWnlA-5SPzx2fix_yTJdNL8mih3D4ZaHRg5n7FIDShdLS2CJBtTTF2xkhgHbVH_Xg1XgLyLnJ2cKG-PhhTclmNQ6Aj-n1eTYvrqHDBEPPDZnv33Kds56Rxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه قطر با پزشکیان دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/144104" target="_blank">📅 18:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: به ایرانی‌ها گفتیم می‌توانند با همکاری با ما، برای تولید برق انرژی هسته‌ای داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/144103" target="_blank">📅 18:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
حجم بسته اینترنت "نامحدود" شبانه همراه اول از ۱۰۰ گیگ شد ۸۰ گیگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/144102" target="_blank">📅 18:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144100">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqlOv3Yk0fz9g4LYmoZ0PkSda_f1iA4_1q2ltl5uz5tNVjPfqc34V_YO1vAWETUzEvFy1oD22MFLnvtgjIQSvbmUrullqexM3shFZg7pw-71MYhpo6OAZGagLXhg_TS5q17tbMOnhhvH4LOteVlGXVqYgRGCGeQ2qVd4r72eGz3q0W6ZPk1npBDrHc6CViTnQFZPCC9CbZNvx5XA9-Lm3VgJzul3Fxdmicx88qI7N4XaAlT3oMmY0gIhBJ9ZDLQRGgMfovoLff4Yjuf0fXN7dJIsMoKb1DYptr8QSDn2OnxgwpEB11Em65Qbehntz8W6a8NHsKrGIc3p9fBMDAAfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سارقان حرفه‌ای در یک عملیات فوق‌العاده سریع و حساب‌شده، موفق شدند تنها در چهار دقیقه، گنجینه گران‌بهای عصر برنز اسپانیا را از موزه «ویلنا» به سرقت ببرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/144100" target="_blank">📅 18:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144099">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۷۵ کشتی تجاری را به مسیر دیگری هدایت کرده، ۳ کشتی را غیرفعال نموده و برای اطمینان از رعایت مقررات، ۲ کشتی را بازرسی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/144099" target="_blank">📅 18:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144098">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68c118693.mp4?token=GtfTrue-zp_Arnv7-cpYeAd-wphxwJQz_VGnmPm9s37PYr5JQmHVBFOtheWJuvEOcfrlbg0I047uEgQAjb4CrVVz6Gykx6Wp1B8enGHhiI5feeBx0vBeRqxzgsIxKChDRws1BwJYo0SYZCYEb5euqAfi2HnzJZWADH-HdaFPBWP0Baxm1IO0w9GA5AmVMySi-c4dI0JVSHmPuG1x46s8Q7CyYlkut17_8mznp7bdHrAR1_SAUJIRg0foNMqnKF9xHwmjfVGaI1HpNF5lcwbtSMA8in7xYGw-QW1tGi4eqc5ZiT_JrPL6fKJiwGGeBEv-sq-WrjQcv7V8GNZFiEI5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68c118693.mp4?token=GtfTrue-zp_Arnv7-cpYeAd-wphxwJQz_VGnmPm9s37PYr5JQmHVBFOtheWJuvEOcfrlbg0I047uEgQAjb4CrVVz6Gykx6Wp1B8enGHhiI5feeBx0vBeRqxzgsIxKChDRws1BwJYo0SYZCYEb5euqAfi2HnzJZWADH-HdaFPBWP0Baxm1IO0w9GA5AmVMySi-c4dI0JVSHmPuG1x46s8Q7CyYlkut17_8mznp7bdHrAR1_SAUJIRg0foNMqnKF9xHwmjfVGaI1HpNF5lcwbtSMA8in7xYGw-QW1tGi4eqc5ZiT_JrPL6fKJiwGGeBEv-sq-WrjQcv7V8GNZFiEI5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی سودان، یک انبار سوخت و تجهیزات متعلق به نیروهای پشتیبانی سریع (RSF) که از سوی امارات متحده عربی حمایت می‌شوند، را در شهر مرزی آدیکونگ، واقع در منطقه دارفور، منهدم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/144098" target="_blank">📅 18:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144097">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpZMq8hII5aE3ugVJkGCerwLrBvndCt9Pq6aA3YtZUztO-w7GzfPxRaPu_-eco76ub33MxvPXaxJyqrqMUrMeykd_ZEaLxh4hUcPL5gi2kFjKUbRzYgQ40KheUX6xTkxjZKoQn5EKUR6p3S9aXbiiW0vVJ0ctVN9TYNqNGNistOWDtAywgaP3gfTzFXa8GByTyfXfuK9SyhCHg6D-Z9lR-J5oKcoboRA-RyKwJJb_ezg6zhd9sUwmoXzGzBQGS4B1cVge-JdTq0IgbUp5d9mN8V-KC9c1ov56LAO2AT-tLmNTtmvRZQXgjpp1N4o6ozc7fgWwXTL9yJZcllKRdSZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیلا ابوالحسنی ۴۳ ساله و مادر دو دختر نوجوان تو شاهین شهر که تو دی ماه از یک مغازه ای که درحال سوختن بود فیلمبرداری کره بود توسط دادگاه انقلاب اصفهان به اعدام محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/144097" target="_blank">📅 17:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144096">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUWxQNBwq2NA49O3kuDfDyCkxbkti18ZBv87AAPUqGQ4Ne1A9l0za6mm5riq6n1_eIsZyrHL8OJuctBtnt9NIflEV_csHz0fvkUOIru0IR3zx1GEUN0NqiTiuBA15TNxiirWOjiwPOUP9dc2_yvi16EsNSAGUyLihGXxEOZoMM3QspCXgUQ0Jic-fS0lVKN1ox1LtqoJTexixfLh73qjbX5liIEbvqjx2fsZNWaKNU7CEJFsL4Em1Z_r4gWQHtWbqTcpTDtmkld8h2AzhcZWH-sFG03snXlMFmDKPVfiyFrx369uP4cVuAJQogHUvxVvQ2F_L0irFM9MzbSxwMHmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود تلاش می‌کنند، رژیم فاسد به هدر دادن مبالغ هنگفتی در خارج از کشور ادامه می‌دهد.
به جای اینکه میلیاردها دلار را به گروه‌های تروریستی خود اختصاص دهد، این رژیم باید آن پول را برای مردم خود هزینه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/144096" target="_blank">📅 17:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144095">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
قالیباف: چپ و راست داریم پیروز میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/144095" target="_blank">📅 17:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144094">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نتانیاهو و کاتز وزیر جنگ اسرائیل بیانیه دادند: تا زمانی که حماس خلع سلاح نشود و تمام سلاح‌های غزه برچیده نشود، اجازه هیچ بازسازی در غزه را نمی‌دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/144094" target="_blank">📅 17:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144093">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ادعای وزیر نفت: هنوزم نفت رو صادر میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/144093" target="_blank">📅 17:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144092">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
با اعلام اداره محیط زیست مشهد، سگ گردانی در بوستان های این شهر ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/144092" target="_blank">📅 16:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144091">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XVXFveSRSjhLaz_OVOX3SfRzfVZ9COgsGS5QQBVVv2lfjAOrrd-SQwhU7Wb_e9wHB9X5pPQKJRWJ3bj_oO0K59KAsZVaf4-a34o8ZTIi3JA7qcuYJDtYtmYc7bGr-t_nCQb9VbbRKKFkMs7R9HI-yjg_vHisKHMVYFPmtp-g3TqGUhgJWBqKnM57u6j3tt2lfZw6fzeejxaB-OiLy7f7YW9YujEfqcVg5nXwN0M6jkiJX7IOspzUu-lBtSvHHmt54P6QK4NxlEnH1BcoNcjXEUnXyThsQ6bcqbVPv-a3hpPQT2AjV2pBDgsnA8lioDFvM2x9gneseEuzTQtuXKdQ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: داده‌های کپلر نشان می‌دهد که چین در سال ۲۰۲۶ روزانه حدود ۱.۲ میلیون بشکه نفت ایرانی دریافت کرده است که اندکی کمتر از سال گذشته است. شرکت‌های دولتی به دلیل ارتباطات بانکی با غرب از خرید آن خودداری کردند، اما پالایشگاه‌های خصوصی «چای‌ساز» نفت خام تخفیف‌دار را برای سوخت داخلی خریداری کردند. این پالایشگاه‌های کوچک‌تر برای واشنگتن تحت فشار قرار دادن دشوار است، زیرا آن‌ها با یوان یا ارز دیجیتال معامله می‌کنند و وابستگی محدودی به سیستم‌های مالی بین‌المللی دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/144091" target="_blank">📅 16:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144090">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd5eb8afce.mp4?token=c1aJJuQtJnqW5kTuEUmbbTXmMxJXW2KhgcxRVFmFZ6kf4y0Ez0VqT2WGu8oocPFxj8oKLeRWqjGkYMAED-cyL5WbpAunhpgftyc0SaOTZbmn6H1CpPQ9L4r9X49f1-7MAHKjkF73pwtwYGdGYoSsbGUmt5kTknzHYoBmwYjHX0FiKA7FJkkiQ4rjcoq-C-fqbzBBAa1HEojA3-oCbA8qODFp9OzI7A9eq_P0umcfDwVDY9t_k3j4jQsTFhpJwcRwSxVk43TlQxy52txC08WeCa5lSoWrvggshFXqwzO37fBHFB0ciTWjQKxQv-fjxtf_In11tzv1js3anIqp_mttxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd5eb8afce.mp4?token=c1aJJuQtJnqW5kTuEUmbbTXmMxJXW2KhgcxRVFmFZ6kf4y0Ez0VqT2WGu8oocPFxj8oKLeRWqjGkYMAED-cyL5WbpAunhpgftyc0SaOTZbmn6H1CpPQ9L4r9X49f1-7MAHKjkF73pwtwYGdGYoSsbGUmt5kTknzHYoBmwYjHX0FiKA7FJkkiQ4rjcoq-C-fqbzBBAa1HEojA3-oCbA8qODFp9OzI7A9eq_P0umcfDwVDY9t_k3j4jQsTFhpJwcRwSxVk43TlQxy52txC08WeCa5lSoWrvggshFXqwzO37fBHFB0ciTWjQKxQv-fjxtf_In11tzv1js3anIqp_mttxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند عقب افتاده توی روضه بچه رو آورده پای منبر و اتقدر فشارش میده تا گریه کنه و بعدم میگه داره روضه میخونه
#جهل
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/144090" target="_blank">📅 16:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144089">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQWULDiaJuXJqYgCzlGwI72xbxrYqSjrV_WdT78Xf-pMN5LWI97Jq4OBGc0gTVPgSa0wkOw3_LNovnDjADFoc96YgiMGgOfXZXxf9k5zDbIRn2VMOhp1J2k-HkAg4nUpJuRrwo4HG-QVshqPfda1vC2kL6Y24_-o87nrt-yql529I89l9O0LoPwll-bH6ZnvO6Q8cY_NlCBXg_BfFiQoo5XrgInPUoVsgn4ZbGdmknCactt4H1PCkBMMTtMtI-cJlYPAhoUHFEbN9pGURc9GGDGiO8VGlVvHHZ9mwpKBTKGxQmZ1SwMU2Tj7eUQ-1pezCII4f3aw16cjsg0dM5itkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک توپخانه اسرائیل به جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/144089" target="_blank">📅 16:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144088">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 250 میلیون
‼️
🔴
دلار به زودی 210 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/144088" target="_blank">📅 16:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=vULkTj_sX8gS7qfQorw6zNP0cvwD2GXWwL6xBnvmoxMtUJHjeOi8UYWm_mo9bDNNGNPfV7Wh4nMUSy8IiHepukplcAQQlu-MIrZzZZloQpjOGC-8468A3dRY9N1N4iJGx7S2Yf7VNctaTK858jHeFUZpAaJ__jAtU3TUXK7vIaFjFkvbkaoMFcTf-2E3ouLuSksv9jdvSfBKa8aKEIroD5lMEEYpW6pZoR3KF-Thvr-LEZLfwEQModL0k9X1RcM7qqyajqsdMMsy9AaaMpofkEK23jX7BuHjuIItb4OYu4Cs6iWarE15a0A-O4LsEGGbnn2sDAKLwhFU2LsbuWSFiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=vULkTj_sX8gS7qfQorw6zNP0cvwD2GXWwL6xBnvmoxMtUJHjeOi8UYWm_mo9bDNNGNPfV7Wh4nMUSy8IiHepukplcAQQlu-MIrZzZZloQpjOGC-8468A3dRY9N1N4iJGx7S2Yf7VNctaTK858jHeFUZpAaJ__jAtU3TUXK7vIaFjFkvbkaoMFcTf-2E3ouLuSksv9jdvSfBKa8aKEIroD5lMEEYpW6pZoR3KF-Thvr-LEZLfwEQModL0k9X1RcM7qqyajqsdMMsy9AaaMpofkEK23jX7BuHjuIItb4OYu4Cs6iWarE15a0A-O4LsEGGbnn2sDAKLwhFU2LsbuWSFiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارولین لویت، سخنگوی کاخ سفید:
در حال حاضر، هیچ مذاکره‌ای با ایران در جریان نیست.
🔴
این وضعیت تا زمانی ادامه خواهد داشت که آقای ترامپ احساس کند که شاید آنها به شکلی جدی و سازنده وارد مذاکرات شوند.
🔴
ما هنوز شاهد چنین اتفاقی نبوده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/144087" target="_blank">📅 16:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144086">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
حمله موشکی نیروهای حوثی های یمن به مواضع عربستان سعودی در منطقه المخا
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/144086" target="_blank">📅 16:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144083">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1S3WAAPH6ztoWWoSB9TvOfhlPVAiaUMAPE1OJHLahmoAU2E92eM-3Q2TbmTAtoZjSfRFu3MhRhFmlQzUdhoNVkMVKwCqSpvGtWimP8Shev4W3dtEQz8dPQHzDf3U_RZYM8FLBVQmayTk5uo788JwdIqA-kCqZnarBBfOBAgmlyIl5S5h-qlNYxXEdZ_SzAf4Xybbzywi-8kjP0p0bz0lOjmiawy6kYlMTpKFhwZIN4lSSI4uc015rnc3CmJnQtYOgSt8rhLJK8xFt_n6DUNpZ9WNTbyOF9rC597HLQ9tUV61gMhO0hnCijK_t10CkSA8-NHMTsF0iNaac6NN95i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJiSz_RZ3TN9ncLvjvxAuAYjkckT1TWNZzxcENEoDaKflxf_0UPzy3d7TTZ1oZBUgRbEOZwVJtdIn9T48IyOuTfVyZ6pbnNmjPYYyEBYIm3F6cLyY54bluyNUcHvgf78vaPwVRo99f2JbrqaybdatI0qT1dARWhywJwQbNObsmzl5pFjS069_-LA4BIcADv66Rg1W1Ro60OhmYFADFnd7M3YIrQDZ50q5-2EJpdlpR78YhjWC0TU8SKGnMXKhVc353V3s1-tln-gaK7IDi2YIyZlmVWW23RthrXfBSJNLAMxdUm5Bt-Y7v3Bjwj-dpRR4q83mjMgY9NzqUyxdDAjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbCecDIiiLdbB8RHH9m3PoWOYSeeC63LMrtLmTz4ETLKeaXzgWCufhpOWX0-8eIkNXNt4pTqqk6Fa2sRtx6bboBtKry_yPZZBdLE8NZ_6BBA0cxm0S17_RaPLrk66nODisWkb3BKfNpfy71_R1ULTu_AN8wJxYpZgJ2gaCfpBvclNVN2iesCnEOdyq-ua-r-b8-tULcHCk08BLdvfA2fprbLUIivkd9X_Pp-ByxQequCk6a4iyYicX9z3k764996hp_57jra2hIZcQmu7dZR_4C6cVdC7-tLF9y2pjynwoP2RR75X-D0WEL2c_hlinja__Sj1iJ1txxOPP8-JlDT8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر نبطیه لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/144083" target="_blank">📅 15:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144082">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
دقایقی پیش حملات هوایی شدید جنگنده های اسرائیلی ، نبطیه در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/144082" target="_blank">📅 15:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144081">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
شهرداری مشهد ممنوعیت سگ‌گردانی در بوستان‌های ۱۳گانه شهر را ابلاغ کرد و تاکنون بیش از ۲۰۰ تابلوی اطلاع‌رسانی نصب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/144081" target="_blank">📅 15:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa8eb8b15.mp4?token=TlcbVF7InOyoDvuuc0QlKGF2Tw6nsSJcrkEqKgvy_SQaBGJGw_69OamzrGGt1Kpb5uWDJJha2eQlFkrren7a4eVrSGeRtFPzqK3CVi7t_u3l1hPioQJE33f_PUz1NgfVhD7qAX7tWq_VmSYu8qX2zR98fThoaLzwyQSDLp1kF2KnOJCdFAyqjA2TYnG9OrcNq74IQBw09uwEZJ_nlgJG6a6j66irKrbmCW52CeGOwoqiHwVQOYp17VWtMojUoCKI_vkuFp6dPrdv52kcLrUajvInnDqyskpBi1_3nTJISqAHLWGEZl2s0ERV1NDX3eSbYWOualPgMGLfj_DaoQpTog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa8eb8b15.mp4?token=TlcbVF7InOyoDvuuc0QlKGF2Tw6nsSJcrkEqKgvy_SQaBGJGw_69OamzrGGt1Kpb5uWDJJha2eQlFkrren7a4eVrSGeRtFPzqK3CVi7t_u3l1hPioQJE33f_PUz1NgfVhD7qAX7tWq_VmSYu8qX2zR98fThoaLzwyQSDLp1kF2KnOJCdFAyqjA2TYnG9OrcNq74IQBw09uwEZJ_nlgJG6a6j66irKrbmCW52CeGOwoqiHwVQOYp17VWtMojUoCKI_vkuFp6dPrdv52kcLrUajvInnDqyskpBi1_3nTJISqAHLWGEZl2s0ERV1NDX3eSbYWOualPgMGLfj_DaoQpTog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان شدید در مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/144079" target="_blank">📅 15:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
به گزارش سی‌بی‌اس نیوز، ایران در شرایط تشدید فشارهای اقتصادی آمریکا از طرحی مشترک با عمان برای ازسرگیری عبور کشتی‌ها از تنگه هرمز خبر داده است.
🔴
تهران اعلام کرده اکنون گام بعدی به تصمیم دونالد ترامپ، رئیس‌جمهور آمریکا، بستگی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/144078" target="_blank">📅 15:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آخوند طائب: اگر اقتصاد ایران را به‌هم بریزند، اقتصاد جهان رو به هم میریزیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/144077" target="_blank">📅 15:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8e83a74d6.mp4?token=u2HcEyIkLCu9vQc6w1KWFOCVJfa0ByCoFf7AkEHftKVvem3RquRHJoZSQ6wy8mv6grmptlz-5SWFBEVmi4wee-z5Y_r5ejqAz0h1BDfUwZkaksCYsQ8Fg1AgHLrAkULk_t8JUpOYgQDNLh7kMsoV5bERwyVnozRyD7Rl4ZuaJNQIV4uOJNdqm5-wWadRbXhKfU_hWIrV8A6T8ip3KB4bcqpl7OP-28QlIzfAKF8jT3-eVe_DGzWj3CX3kq2np2_dzafhBiTQu_uwxNGUzYf0qrScMkUAR-3OJulXt3R59HNR2OJsD1im0LYrQ-mjIztd80_4f3DnBm4gq_6J2xT1-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8e83a74d6.mp4?token=u2HcEyIkLCu9vQc6w1KWFOCVJfa0ByCoFf7AkEHftKVvem3RquRHJoZSQ6wy8mv6grmptlz-5SWFBEVmi4wee-z5Y_r5ejqAz0h1BDfUwZkaksCYsQ8Fg1AgHLrAkULk_t8JUpOYgQDNLh7kMsoV5bERwyVnozRyD7Rl4ZuaJNQIV4uOJNdqm5-wWadRbXhKfU_hWIrV8A6T8ip3KB4bcqpl7OP-28QlIzfAKF8jT3-eVe_DGzWj3CX3kq2np2_dzafhBiTQu_uwxNGUzYf0qrScMkUAR-3OJulXt3R59HNR2OJsD1im0LYrQ-mjIztd80_4f3DnBm4gq_6J2xT1-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم حمله هوایی اسرائیل به شهر عرب سلیم در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/144076" target="_blank">📅 15:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فایننشال تایمز: جنگ ایران در حال نزدیک شدن به بن‌بستی شبیه به جنگ اوکراین است
🔴
در ۶ ماه نخست جنگ اوکراین، بسیاری می‌گفتند درگیری خیلی زود متوقف خواهد شد، چون برای اروپا ناکارآمد است که از روسیه انرژی دریافت نکند، اما مشخصاً اشتباه ارزیابی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/144075" target="_blank">📅 15:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
روسیه از تصرف شهرک شوچنکوفسکویه خبر داد
🔴
وزارت دفاع روسیه اعلام کرد، شهرک شوچنکوفسکویه در منطقه زاپروژیا توسط نیروهای مسلح روسیه آزاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/144074" target="_blank">📅 15:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohqJGuJMQPLw104CS-vR5-QH9hcFPhUtz1eNmBuXWiUuwXd9c1g9FMtA5dcWH_s4Q8QRDqkZy6ppaWMMuOwpVZkkzMJpFgY22YUZx8RXYSoyfGhwScmnhzWv7weYnZopV5-OrFTkmM2hEZXwUfym2bsGH-mQwClbG_9l-FmGAyx5S3R0c2155wkibAXUATnd0XCasEP5VersoUkwsbDC6-mkQVqiopXHCr4g-BeS_lYjhSErfVHnrC_ddE58Ua988IDzFNby_i_S6enhpnLmhbtsTMJnjlASU5LSfa_AfqnP66BCwsV9vwtfwFYR0bbNDN-xhcZC3GpqS_zq8oWL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144073" target="_blank">📅 15:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت دفاع ترکیه از اسرائیل خواسته فوراً به حملات علیه خاک سوریه پایان دهد.
🔴
آنکارا همزمان تأکید کرده حمایت‌های نظامی خود از ارتش سوریه را ادامه خواهد داد.
🔴
این موضع، نشانه دیگری از افزایش تنش میان ترکیه و اسرائیل بر سر تحولات سوریه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/144072" target="_blank">📅 15:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر علوم: دانشگاه‌ها از آغاز مهرماه به صورت حضوری شروع میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/144071" target="_blank">📅 14:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ارتش اسرائیل: حزب‌الله دوباره دیشب با دو پهپاد نیروهای ما را در منطقه تپه الطاهر در جنوب لبنان هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/144070" target="_blank">📅 14:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نخست‌وزیر عراق: آمریکا برای خارج کردن نیروهای ائتلاف بین‌المللی تحت رهبری خود از عراق، نهایتاً تا ۳۰ سپتامبر مهلت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/144069" target="_blank">📅 14:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز : یک سیستم دفاع هوایی متعلق به نیروهای یونانی مستقر در عربستان سعودی، تعدادی از پهپادهایی که توسط حوثی‌ها به سمت شهر جده (ینبع) پرتاب شده بودند را امروز هدف قرار داد. این سومین باری است که نیروهای یونانی از سامانه‌های دفاعی خود در عربستان سعودی از زمان آغاز جنگ با ایران استفاده می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/144068" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lei1GjB3kgOFLqmNRvnOJTnqIN-EQlQkNF6XRdXXp1dDQoTfBKOV8wU8Qz2yU10LNvP2FLMbXG2aCHQnY7Bk6EEjblsy8QctkmKoL7xEPDGyMgqoi5dH8JHL8QEFJoeB5178-u5JFIVtTb5jeLUB9gmzLz22Y10srPccPp8I2o6kMck6vzYj6FIuM0ysd10I0mJTLwF_lWAsDw612BSxis8bjXr8FotuuCwMCphUsfbWpP1Uea-8i4t0N1AGJ2ZTdWz6viX9C29x5VStoxRSyfSkBDGmlbPUVaIJPFiUnEyrYLA1pH5pPsnAk0mcHtJN2P4Gu4PF-KCcVRHoO5Ljdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک تانکر در تنگه هرمز مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/144067" target="_blank">📅 14:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPlv3XOztEorAGdJ1YCNrBZuRj3Mtg_PccBxLMwWSAlmwolidy3Bldj-iabUQmXgu8hSOEWFd1GoZ6yBj1mpJ4x1PHC3fm52qTAPNERca85qlmxR2WS6VpFIN9_oQLOiQqzq1yr6QAfW9j2mFxV40AVtxGKQ3ctPUM_hhkV1iXHlbICxwqRukj_7IrqZ3tcxWvrR8At8IIhLHrbNcZt-PYAT5zRP4YLnmzrTzL8EflF1yaEDjvy5EQXL2r_JuapLdEvczs4uFy3e9yGvlo_nR28guNjFUaxG3z30JGxK1KUZlsKiO9Ejoodof4SRfHSb50N5QUNhpb5TdphjY9wtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش
The Hill
، پیت هگست، وزیر جنگ آمریکا، شان پارنل، سخنگوی ارشد خود، را به‌عنوان گزینه‌ای احتمالی برای جانشینی دن دریسکول، وزیر ارتش، در نظر گرفته است؛ گفته می‌شود دریسکول قصد دارد طی ماه‌های آینده پنتاگون را ترک کند.
پارنل که یکی از مشاوران ارشد هگست نیز هست، به‌طور خصوصی علاقه خود را به این سمت ابراز کرده و در فهرست گزینه‌های هگست قرار دارد.
گفته می‌شود دریسکول پس از ماه‌ها کشمکش بر سر نفوذ و قدرت با هگست، در حال بررسی ترک سمت خود در حوالی پایان سال است.
همچنین گفته می‌شود او آماده است حوالی
روز کارگر (Labor Day)
استعفا دهد، هرچند کاخ سفید می‌خواهد او دست‌کم تا پس از انتخابات میان‌دوره‌ای نوامبر در سمت خود باقی بماند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/144066" target="_blank">📅 14:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسکوت شکنان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbsJNEP_JPUBU2QPci05X4JkLThf1SZ5cHU_eQPMyXzcQkrc2P2NOqblLixMGvSL1iOpHXQVMYs2IevNlEmjgZYKhBj4zxebO6su9OtfuTqUUzzvt_727ubgfhqQxAJ3dt_fysprN-Q6EO0wBI9rDlYVYCXdkqo7lHwbkCNL00L9Ga_XsDb5U5ZmZqQlMVRGwVvVdL0Uf8l-PzwlnQCzxONLdBnFppPrr-VWOtfEBQTO9jMbBi901UvZqNnBIYvC9fffjVViDnAcQjMWS5LfZY_eaqAY4dox5eW72b_B92EXxj33kYN5pHzrb6hwum9vCmtjC4Dmtu_0dO5q38tePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با داشتن ذخایر بزرگ نفت و گاز، حالا برای مدیریت بحران به سراغ مردم رفته است. مسئولان با راه‌اندازی یک کارزار پرهزینه در تلگرام، از مردم خواسته‌اند در مصرف منابع صرفه‌جویی کنند؛ در حالی که این سؤال مطرح است که چرا کشوری با این حجم از منابع، برای عبور از بحران به صرفه‌جویی مردم نیاز دارد؟</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/144065" target="_blank">📅 14:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vo4fyZ-F7awE-dpoeiXSFb760Emtk82uwrBIb35kpeYqJ1uovqTMADylHXoYoS1Ltv1rkCGkl0XmIxMPep4JzrdyHcit1grxHdL_zUS5Hy2YqySkqIKZ2zfmAY9LXLgRhsEIBUG0R3_4kBAChkFLcgGvIvj-OADdCxN6ZA4YYt2L2vrVGpEjFMeXUKHb6_sg5orGyNw1jPifpYBw445OSXHVfpbk0xjOFkkWjxQOrFeGetjGJ2jYcwJYrhDMZaPXcU4nD5W33C6sMYOksdEJFVFtOy9BgNNqGHYgYebLlF-4lgKHqop5ejnzs_AtrRjRn4ZeMUuyCSWoSW8dxqzydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ورود نخست‌وزیر قطر به تهران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/144064" target="_blank">📅 14:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رئیس پلیس‌راه اصفهان: مأموران پلیس‌راه جرقویه-ابرکوه حین ظارت بر تردد خودروها، یک دستگاه نیسان را که توسط دختری ۱۱ ساله هدایت می‌شد، متوقف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/144063" target="_blank">📅 14:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر بهداشت: قیمت دارو افزایش پیدا کرده، زیرا در حمل و نقل مشکل ایجاد شده؛ مواد اولیه‌ای که با کشتی به کشور می‌آوردیم را الان به اجبار با هواپیما می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/144062" target="_blank">📅 14:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144060">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c886e053.mp4?token=nW4-8ORqDGDSTaimqfOHDfVWjBrXyAfN_HGfr49QUUAxP4xOn_5ADie3CRXEsaEotLKlsLN-_LVTm0LQUEAJo1XpIh44oSikeW0RXH9jSc0ZeEr2_BHj_xb7pD5ASruXd8FmDy4U6hDPZJ3KRG7BbIDbGt8QCjzppVTL6sgsEArQChrBr_CN0jNDBzDUHf5N_1l4D6VGm3yjsjp8jalN8Pl2DIWO3Y2DHFqj4ruFSgrhS8uD8T0KWZu9mVHaht5xg6Nn_0hsEsGriEQbVSxctXjonJPmXKikgUWbFRZoo1aFLIHfQS3kPoc9R74GyiPaRF7nN-KrHYkD_cdIdIpHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c886e053.mp4?token=nW4-8ORqDGDSTaimqfOHDfVWjBrXyAfN_HGfr49QUUAxP4xOn_5ADie3CRXEsaEotLKlsLN-_LVTm0LQUEAJo1XpIh44oSikeW0RXH9jSc0ZeEr2_BHj_xb7pD5ASruXd8FmDy4U6hDPZJ3KRG7BbIDbGt8QCjzppVTL6sgsEArQChrBr_CN0jNDBzDUHf5N_1l4D6VGm3yjsjp8jalN8Pl2DIWO3Y2DHFqj4ruFSgrhS8uD8T0KWZu9mVHaht5xg6Nn_0hsEsGriEQbVSxctXjonJPmXKikgUWbFRZoo1aFLIHfQS3kPoc9R74GyiPaRF7nN-KrHYkD_cdIdIpHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز در یکی از پمپ بنزین های رفسنجان بجای بنزین، آب عرضه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/144060" target="_blank">📅 13:55 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
