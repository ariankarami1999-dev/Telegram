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
<img src="https://cdn4.telesco.pe/file/fZnbjiToV5ruyywVWxuEEifhIqMzYxKQ-Brh1J-UFdNg5l_aX25_ON8NG8Cpm3X8rl74khPXG_8jtuPbMHI9M08EPXJvMmZNscd6j2cMQfpcH7zfFKrLjeDG0idWkqvvOrCGqxe_x1WtVxnlIf4942A-QiG30OoVLAV8AHGC0_Kfb_BBni4PQ5aAYctNVJzptynPjHbVePTsM2rKIPOBjrCSVKqJc29x-LcBzgVsqmwOyIqZIvZf4xn_TL2Db2g1i_dxQEz3-O-puvWj3qXjl5IR9WZblGt9CeTF7TmRe0GqHYWTxaOrCe9z0H3PsrvnhkFh9hThLuatKbGULUdexw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=HF7KxQZ4LVAg6EnE9z2D-iFq1ZHEpR6iqfpS_1b5ppBLWE8jS7MQBwAjHsG1WLtdBoD5FgVbzS-iCxvej1xeVHCsoVzE8qe1Uy-59zBCMLn3bs9O6CTUMRyl6oSum9YCwLNopcSxuYKhi1lXlcJHnmsJ1NX-1OjvLS0EqcZerWkAEKVivr1MrG6YyK9CEsMbkvE37NcPbEWIFUCl4qMnSXMYmLCXs1zDJkxyKWJAOrOlcJCcxP6XExIMzkaKT9l5aUn54_27qwpPD-wIwdAWzIEcX74qwW7uuxWNmF3_y97HU0IHYS2uFv9VuAnOh8ZWQ9Y1UVAFRIPzYy_GAHNDfx0nLI4Nnq-ry4yhLw21pAdOam9ZspcGHJV7waaK9pBlesTAb8yqnEBWc2wAEToYY8iXobTRYbwgyDv4r1p0Pk3tV2_blOqkHAtYMIzr3S9hsF07NNOFv2rJGVZcX0aFu2Y_VbZg5H3LOeU4zbUQLcmAD3XEs86B5EvN1yDZr4PcTJt9Yo4oLnzQXTqQkYntpdYz3SOR4lQkClNDYvhyDwHj14zrxNozGl2CS9NAHj-ywDo-xicAB9kg_YzDyNTbuqmmySVMxtsOwXbLXRaQDyj1-aF9AcM9vGCrQ3M9AEMvt2dKv-zDVtvxDle3M_8g_5Pj4HTDPJL6LSXSjsiDJf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=HF7KxQZ4LVAg6EnE9z2D-iFq1ZHEpR6iqfpS_1b5ppBLWE8jS7MQBwAjHsG1WLtdBoD5FgVbzS-iCxvej1xeVHCsoVzE8qe1Uy-59zBCMLn3bs9O6CTUMRyl6oSum9YCwLNopcSxuYKhi1lXlcJHnmsJ1NX-1OjvLS0EqcZerWkAEKVivr1MrG6YyK9CEsMbkvE37NcPbEWIFUCl4qMnSXMYmLCXs1zDJkxyKWJAOrOlcJCcxP6XExIMzkaKT9l5aUn54_27qwpPD-wIwdAWzIEcX74qwW7uuxWNmF3_y97HU0IHYS2uFv9VuAnOh8ZWQ9Y1UVAFRIPzYy_GAHNDfx0nLI4Nnq-ry4yhLw21pAdOam9ZspcGHJV7waaK9pBlesTAb8yqnEBWc2wAEToYY8iXobTRYbwgyDv4r1p0Pk3tV2_blOqkHAtYMIzr3S9hsF07NNOFv2rJGVZcX0aFu2Y_VbZg5H3LOeU4zbUQLcmAD3XEs86B5EvN1yDZr4PcTJt9Yo4oLnzQXTqQkYntpdYz3SOR4lQkClNDYvhyDwHj14zrxNozGl2CS9NAHj-ywDo-xicAB9kg_YzDyNTbuqmmySVMxtsOwXbLXRaQDyj1-aF9AcM9vGCrQ3M9AEMvt2dKv-zDVtvxDle3M_8g_5Pj4HTDPJL6LSXSjsiDJf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7gqU3ULP2sy-0jSq621mDqLF1zZ_QTWFjXwmruynD1j9HXl6e49RuLfRZuKnmOhCKiAW7BGQCtVZoBPHRS_OhKQPo_WwbOLeXOL_qdYpjFl5YefwoFLzuIZd2BlOGsoJMkzznIyrc7Y5YlVDKv6pFl4DjrZ_9GznBH1aSewWCuVkU0nWmTmPb1ZTCNZBkZtLK4Gwjy5jhPRC-v2TPbZ_kzf2AP5Ek5qQNTTs8jmCoIt9dim2kWLYyhQbTMoa0jrYiL7Owy2d7Eg6QtMMrzi9ZhDTdiKITX_GrseDHoDUnoyhLBmZXz7NeStbs7FUjkytYKW20oRCUPkSOwk4i_CcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccjqiSeI4PphVloDoJe9gFWPSLS8fCtwXOhd1WKQJ_-aKhcaTBYAA5Z1CZ3YB_dZ39mLGvCxapFQZ_F3HXz29O7cLuSpNP0wdzAnC8-BkVSQQE0cxIDYCwnxTgoZmQ9LxUPpOUaigda60hNBxSbwzJELXYCkz-BzjnXLKT_OYKUXQjZTLAsc4eQ5kOI5XtutAMSeUMzxf0LklMTt-H_OqTq1qw2NqowizjflEZMmF0iRg8HwQr_NRuLY3uds8dC6lXLGW6tSAXgowuyRhz4Urx5XI2kahhDlhV5mCXDEW0JqeoZR9xp_UyZu6riZnMk9JVxiFa5FcZsVyKjz2BdP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
میلیارد ریال جایزه‌ی تورنومنت  جدید Winro
🥇
تورنومنت‌های هفتگی و ماهانه
وینرو
رو از دست نده
🔥
جوایز شگفت‌انگیز و فوق‌العاده
🎟
⭐
بدون محدودیت تعداد شرکت‌کننده
💳
با مبلغ ورودی دلخواه
🔝
بالاترین بونوس‌ها در سایت وینرو
🎯
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
ضرایب ویژه و رقابتی
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش مسابقات
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
G3
🅰
همین الان وارد شو و در تورنومنت‌های فوق‌العاده‌ی وینرو شرکت کن
🎯
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/78653" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=ajlOGFPN-Vn3904g7T2l-tY8hS2_KM2yXlV1UBSKYdqf5AKAyUcKuOLojzNsHkVzQZzCiUFf97KKk5JNzkHc6G2nuaK99xMXqtLuY5zE3YWMDIPta1umLMj3idfQnEtq76lprHmR8MHDLmY8Mtn0JnFj5i3nuCRLvjKRntPPNnubCZI5l-hRpkduaXrVgDNcInJYUim0un-TWByjDWCi2VXPyqVsIWbCxMdNxozFdGElMAM1BZxky7dDp1mU4lIO63xUeWMdo_xQc-XahJ8HSNxrBni2JqfezRfFX9qbD5Gze1zOIEjFGVbiy0WRYn2m9oLP-hVI3nmrVCwF6j-AQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=ajlOGFPN-Vn3904g7T2l-tY8hS2_KM2yXlV1UBSKYdqf5AKAyUcKuOLojzNsHkVzQZzCiUFf97KKk5JNzkHc6G2nuaK99xMXqtLuY5zE3YWMDIPta1umLMj3idfQnEtq76lprHmR8MHDLmY8Mtn0JnFj5i3nuCRLvjKRntPPNnubCZI5l-hRpkduaXrVgDNcInJYUim0un-TWByjDWCi2VXPyqVsIWbCxMdNxozFdGElMAM1BZxky7dDp1mU4lIO63xUeWMdo_xQc-XahJ8HSNxrBni2JqfezRfFX9qbD5Gze1zOIEjFGVbiy0WRYn2m9oLP-hVI3nmrVCwF6j-AQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmRnwRLTy4qSVVRIXfcag51vOktAhsCBGqytgpRyYhdpuM5IcciZHd--IefMRJq6krTsz6OjMGB9l112qKmNmgZOdrai9qvjQASHcere2Axr46_L4SxtsZwuX7wKFyEYA3bWbQJAf5GZJSEjgpLQJS5N9JNNPoaEJriAqWpMeHAbqvoz59U2EGgZ7F6qu_An4UXY3viK1bdDaKHm0_NcLw6R0jF9lgUYG7gI66EqpuAUHM_a5X8eOg7Sxbb9dV5klA7r-_AwGwJk2sb1Lp5yZ3YEyAD7hyrozD5G_lFYSi9FcvWCteBRE3r56diD_J4N6-d75UMlQbiFr3vVf68TJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsqhyV2MWCP7Rmj5ZeK7FuZ6AedsFvSboSbNIUjED4y6V7tOcRrMPDTMkCh7m4M1RZWa6TPBFECNCydLP_yxDJD0t0iB-KWPSg9RADpP_D90izjPPpYitcV_lCbW5ajY2_dRt6CEkkQ1FoD1i-01Z_euiR97W_djkKkHeIzI8nbVN-w3bdrdo8fj8dYd7Zz8Q4fNDsgznIZ5PnofNyXEgF8E1KM-nnU7frkvZq6ZdKj9N4C4RnUQ1Zaqhw-_yiLrrqL8XmKjV5skEskMD9ADla404matQsPvaLwBsL5YBCqhJGIwzTGnZXzf6bHXh9w3O-QxARy7qlca5zA-AtC1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyRzsINNhA3GSDM5O5W7eeLJDFCmKsJiVWtM4EU-GeYwEeo2_dKJ-uzEHE4UDop886KXlfRZML5G_O82dXdQKBqxvxHNuiTTP_B3ZPEi-YrgZ_VLRGnsQSbSHH3mbIC9Bao0UzgIXsyPZ-O0pmK6WddLqGP9Zm5R0YE4nfsWMKoHeTYtCSrhh4zxtMw0KOiCRJWFdTPkfzDcFLpbCgGUwWEgBdTSvmLGyqSGSkD5-s2dv1MfiTlh50DrofaV4L5qblDa_ybcvhXJ0zWCOukAPFTLUnzvBVFJnJrgOd-x5FjvdyT01u8zIJE8eN65odLi01S4dBV-Pu2rbwY-4qgumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcHT-T8q8NUtlOU-brVYGLh8u_F1DGWVXkZvb7aG-7sS0WdJPbVcSjdf7lbAHnDPErVlyzrOONF9lVVdE4PLYDTGwqoh1SBSFDFVUqfP2_IAhdcKH8--OOx9XX8JJYysUXRyUS8bqqPA3L9GxbV75uwa0tFGwVLwSdnEanLszyu_icwEKxdKAYBIf2e4ojp9kHGYd5YYgPKGIqp6o6Ry_LLiqQSYT4ySDcljmJUT6YbvkC5XVwDTMS4i1kMq3mhMw7RGDLwmExD-Ufn8ZEyfzQ5uEwNTD7TqbPJiZe5KEP-ctjFU_uoeFJWMF4plG9eJ6cURkJpFRWXC3G4vxPxX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxJcQSee8T50ct3V495lPxA169ssMlM_qWUmQdq2cz42lSDHeB18d8XJLDWKMioPEZhruRvH6-LJqAwnVGr38-Lzf9uyVmyUevPw5uzMoHhrfLW42DgEjxMFiKKA-NU2XmItYgcpzIedXy9CHZFQMOzDjn8_P07r1e6dliPFqt_-0YkuRnUWoDKVsG_gXqM4t1Ee-N1PNjXjQjkCIM2_7wgxoZseXQCYSDLGK7d-XdP4e7B4rIXFqxRK8u-JeiUqhGUJHs_gaS8rPZ_fsRBdLQnenhsCK4XG6buHKv9PM4MVZFy4F8TzNX14GGnzs1Oq5viExdGk-XLut67Le5A_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر شمارشو برای ژنرال گیر بیارید
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78641" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78640" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3umHJcp5JmUCmwbtclp85HXwd2ZuD1cS7gZ3hvPremkbMUw5SRsYJhqH5qmKNLd700ZIoHXN90ztRIcFSsZ8MkhSFvJYl-Ou0t9AlzdLUnDK0Kw8qvoaIm9nEik9wj4fXnh9qEpV7PcGc8sh8IYsoDZdRbW3V3uCl34u-Bd4g1JpQOj5wnHgpMTLNkiSwiqhwzkdIhla8MVI2hnxEkl0BDWk2Bgw02NcPIPsBXqIhtMyubOIRr5x3ZeeT95XPenkVAKmYq7OUcP_BSFO4vF0di5x_2QwAq-yLwJWbzfQYWNRudhW6zew7rab6ugh9zdweOnjo76DoYvocYgUCG2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R3
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78639" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">و تمام
انگلیس موفق شد غنای آماده کارلوس کیروش رو متوقف کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78638" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توخل از سبک بازی کیروش کلش کیری شده</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78636" target="_blank">📅 01:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بزرگ‌ترین اشتباه تاریخ فدراسیون فوتبال ایران قطع همکاری با کیروش بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78634" target="_blank">📅 00:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETPN8DH6cVgyeEZZYM-iYaydmj-kPef5AczDTSEeDvOgfigKR-pQX9ecoTcgsmj4XgGp4T3AXYkswAd0z0UjH9dP70mTa4ihxZPfSH74J9OEkMhLYRH9Lme4a0GJl-pu51wuj4kXUt7REd4AvEXp4bynQJkG2ZWbRqIDUswSarvywIXxrCwemHOlk3Cp5I4Z2PGfr7upL2DCX19CAMzMQX0FH5nFaKKXZYutJof-i5njXYFJwwvbB2B_uIMOf0ziwo10KIlDx2ix4dhakge8SZ10BsJqKnapWdUi_9HqxR3qBmUs19poBsejSjAPxb-mGGP384PooQsR6zlkxQsPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد ۳۹ سالگی بزرگ‌ترین، بهترین و با ابهت ترین بازیکن تاریخ فوتبال هست
مردی که با وجود خودش به فوتبال شخصیت و اعتبار داد
تولد لیونل آندرس مسی بر‌تمامی فوتبال دوستان عزیز مبارک باد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78633" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کیروش عجب تیم سفتی ساخته دمش گرم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78632" target="_blank">📅 23:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=iXU-VUFxc6ClcPdHVzP2oTS2BTDIY0h4k-1XoyUVvOVypc3mrKDTXvwZY1eu_liHWdmZn-TSCAb_1UjNkvUtLiLTHHChg-5vV9by1EnFLtq_jfjaePM9W6sgBpdiHsagf-e9KJ0d-4nu3iYALd3GqSufaohC0IWnqXml8Fy7zlDijHaJHjNEuMOl8vNdO0VvLEXuTajf2MEMWlhUxtX9Gu5I9sW2BEssJl49a2teY4cdQW3j26KF_IaNgK3NP8XALXIHukjllgkyDmcbUWZIedxzuI0zy01etKdvoBtq0vsZYIKrwxUYnE339TsPocNBfoZ1daGLyBDkxfpwshl2_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d974a39da8.mp4?token=iXU-VUFxc6ClcPdHVzP2oTS2BTDIY0h4k-1XoyUVvOVypc3mrKDTXvwZY1eu_liHWdmZn-TSCAb_1UjNkvUtLiLTHHChg-5vV9by1EnFLtq_jfjaePM9W6sgBpdiHsagf-e9KJ0d-4nu3iYALd3GqSufaohC0IWnqXml8Fy7zlDijHaJHjNEuMOl8vNdO0VvLEXuTajf2MEMWlhUxtX9Gu5I9sW2BEssJl49a2teY4cdQW3j26KF_IaNgK3NP8XALXIHukjllgkyDmcbUWZIedxzuI0zy01etKdvoBtq0vsZYIKrwxUYnE339TsPocNBfoZ1daGLyBDkxfpwshl2_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهره هوشی:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78631" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">واقعا افتخاری که تیم ملی نروژ به اصالت و تاریخشون میکنن رو میبینم حسودیم میشه بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78630" target="_blank">📅 22:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این سری کیروش کمتر از ۶ تا گل از انگلیس میخوره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78629" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شانس اصلی رو پرسپولیس آورد که کاناوارو به اورونوف بازی نداد وگرنه درجا تمام تیم های بزرگ دنیا مشتریش میشدن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78628" target="_blank">📅 22:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بازی تموم شد مبارک رونالدو فنا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78627" target="_blank">📅 22:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پرتغال امروز با پرتغال مقابل کنگو 180 درجه فرق داره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78626" target="_blank">📅 22:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خوسانوف از کنعانی و شجاع  هم کیری تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78625" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1m5w39BRWyuaBzx1OuY6LGettpZHoTxHvfGspp0aCaLh_xDQHr-9lQluCVnByowAPo4mo-HMxN07xh8oQ6U4VApAnN7EFnUAVTPsd653-N0pc6tn27kqrd41zXcBrliNveBSZQoMReBqfvtiJZ1stXOf85aSmIcv194HVEaVTKZ18Z1Fqu4-jkhJVOqP8PFoHnvdjTT5FyCtw2exqda6diSpTlrMNqN1r5oBdL3MGWkwI_VLQr0OL3Lfy8gIOb37Wmp1LA7Za2v_a-zlz66ozlyMMUUT91O76Dxc-6B-d_XxPFr6Xnd8tMMpoW99qsqMw_DQxovb-d-PrM_6PKBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مسعود دکترای افتخاری دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78615" target="_blank">📅 21:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3RmVBAQnebzetWbUoxuMYNvbUxpHV4bFDZ7R7DT-hFaWvmKDTY2d6i71gA36IrtVKEZGT6zehmsKdAqQ0fl7Y0ZOTu-J1C-4GQjDYQJohexHNFslhof3RKGT8ELGd3R18dmRlnrkmg8DOdzLyF8w6-C1GLIKvvmrn2hE6DsyJw_HYK-vQ6CY6J-OS2QFmOkp5cT8Pa5CPk7JpXMPNf9653pW7n07V_1rMn8KjpZhkYQhrJ7DQEFPhXbEZHe0L9WvFYi4Vbh7t9PvJn48ahBE-1PxKS06QZUCZpNUiinZkU_AsL4H0nF1_0gadkeIndwxiDEVoc-oorvIsHXNy1pZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو بعد گلش سایز کیر ترامپ رو نشون داد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78596" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امشب تعداد گل های کریس تو جام جهانی دو رقمی میشه؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78595" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEOSVrrBvLXD7MLaCpBGk870mpS_6KgAh8PJuUl3TYKv_Yn0RjfZfLt8FoV24He3S2T7P-ZSX3wKfTPcBpu7QEcKDfnrGIdKBne2fE5vxiI9s_Svv9u86AzdBiLzcoDnwJJ7vXwr3CGsXybuAIjL3dp-8kQMEGYR11igprtqj9c7uA81AP2aYWi8XWwB0rLC9Oi-6HzbWvr6zcsgGDCMrIQRE9x1_jzN7NeMrDwyPLOJZmYs7ZlLGX4zx5yWnHyiJVFskZm_AnPvlI3KVdQXK7rCvytw5Pwivur_aB8aAxxi2pB8noIn0O1FfEbGM-PTWvUB478C4WrspCR-x4ukkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو نوسو بغل کرد
😂</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78589" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نخست‌وزیر پاکستان: آیت‌الله سیدمجتبی خامنه‌ای، رهبر ایران، را تحسین می‌کنم که در این شرایط حساس ایران را رهبری کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78588" target="_blank">📅 19:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره  بماند به یادگار  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78587" target="_blank">📅 19:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسپویل:
رونالدو امشب با پنالتی گل میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78586" target="_blank">📅 19:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پرتغال احتمالا با اختلاف دو گل بازی رو میبره
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78585" target="_blank">📅 19:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTg8TM_vpw0lIWDSuiLipMvZp4E1anzIEJ-yKq2pXdap32e3_rPrsyZ44HfLFogVPCuttGpDsWnPS3vrer1SUxu4-uKuXaDt7-28kl5Eg0Qm5wIqG1CxwyoYllLiVrnmmM9IT7ChwtVmUl84mzzkhlYE-S9E6giip6R818PQr7119h6MN0HWs5OsijNgDYOAI_VkiGIigMNx58bhHeiJKv9visEj3hAjkvy26GXRa1nUr4l8bhf5vi_-3Um_tMGeEVKHVLMzgrk4trcbyqhOA9cgXukBkFxF9l4BA8A5-yxN13x-KIGSDQeaRB9PuFYp-A6PDi1nKaIlHF6ScHHFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jj7e9whDb2uBAhqXHMu6SKXS0XdpmrGMTFb57dgHf_QJ3_sxVh8JQgbm3rg2dbFImtEJW5oVZP4wG1ehJpOLBo4j7oFZggudlCDexu6GVei0vA1s8nL84Be31o38ybUyCWYxg-X01kPxHpLoh-YtRzYxwSIKVMI0W2u9gk782V3A6SQgD864FfK-kI9961P-C5xbH_uz1srgJ1j51NXY37sd6xLwjYjBQ_Je5YAM_T31hQmFmXmBDSYxyfV2tYvu4_PyDqLzoGfmaaTn2OhEr83328lmkJhiilDf9KumqSBV6Ri21kV3VFOXKTCF5wzCfbDU9NDZxoZs2jXEeF279g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب پرتغال و ازبکستان برای بازی امشب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78583" target="_blank">📅 19:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=EPGIwzA0_RXHe3wflzT-JpMun4vGV1s2Q4iNSp74DMoBca2BNkbeFmv0O03D-OjKHojMXyxZztsL2qrPuLBOLJ0UJlWCBV7M0c9lE7Y7h6JLwWVcGOgfBogB0-Az4uQ8pU183_3KXtNXGp_p6eXwxAzqquOa-242KbhAxAZL5i-Wlvxy73W4i1TW3MSXPTU66sTagon93-o7tlWce8BQ2JEzBZGbEXruG8rMwIyg715tf1Sj69XuCTgyttGH3V1mu-xUrCp0nfKwYwxpM2cOi8sBSDpILOD5fCghJqhsqu5BOq_0ZKTAV3XfaX7S18QFCX2gOKPKN3xk2C-XNUMzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b3fc8bec.mp4?token=EPGIwzA0_RXHe3wflzT-JpMun4vGV1s2Q4iNSp74DMoBca2BNkbeFmv0O03D-OjKHojMXyxZztsL2qrPuLBOLJ0UJlWCBV7M0c9lE7Y7h6JLwWVcGOgfBogB0-Az4uQ8pU183_3KXtNXGp_p6eXwxAzqquOa-242KbhAxAZL5i-Wlvxy73W4i1TW3MSXPTU66sTagon93-o7tlWce8BQ2JEzBZGbEXruG8rMwIyg715tf1Sj69XuCTgyttGH3V1mu-xUrCp0nfKwYwxpM2cOi8sBSDpILOD5fCghJqhsqu5BOq_0ZKTAV3XfaX7S18QFCX2gOKPKN3xk2C-XNUMzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سریالی که دکی قبل نوشتن ترک نگاه کرده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78582" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhA-dl7VhsluPw9ktO0EUlsLDAuclvGH7oGnsKuPq4IZ7CaSE6ZUmgVstb4WIPFb69BYi0paLJEnDmc4GzMuXBM9OlQZSWBrKILzfAp1uYr8RI1PoxTtRpTWIji9WJL-4N9s0ayKPbSRhQcZ4_tyIQBqYZDGPJgv6PGDoP6QECE1jcmqcOZzJXzJcNVcQVA-jwW4CUOZfHSVeATzypxL_Uj4pVSK4uCjzTnH9BULm9KgX20drIBi8B1acYSGqKTuVVE6vCL7bVRorzi7QwpXkrP72019YYRBktRZYAN4wx1CDAr2pZFTOWcYV83gRRmftvDZ5Yg2ABbd5cwNW7Odyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
برای اولین بار در ایران
🇮🇷
تا
0️⃣
0️⃣
1️⃣
🔣
سود اضافه روی شرط‌های ترکیبی
🤩
ده تا بازی میکس کن، سودت رو
2️⃣
برابر کن
⏩
فقط کافیه بازی‌های موردنظرت رو توی یک میکس قرار بدی. هرچی تعداد انتخاب‌هات بیشتر باشه، درصد بیشتری به سود بردت
اضافه میشه
🛍
🆗
تا
0️⃣
3️⃣
🔣
سود بیشتر با 3
انتخاب
🆗
تا
0️⃣
5️⃣
🔣
سود بیشتر با 9 انتخاب
🆗
تا
0️⃣
0️⃣
1️⃣
🔣
سود بیشتر با 10 انتخاب
همون برد، پول بیشتر!
میکس حرفه‌ای بچین و از ACCA Boost
نهایت استفاده رو ببر
💵
💵
📺
تلویزیون لایو برای پوشش بازی ها
🅰
g2
💳
واریز و برداشت مستقیم و سریع
بدون واسطه، بدون معطلی
🛫
تسویه در سریع‌ترین زمان ممکن
🎰
همین الان وارد شو و اولین شرط ترکیبی‌ت رو بساز
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78579" target="_blank">📅 18:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7Wp5yEHouUOem0JHe24ozkdHapI78NAihFEinjshzne0xpJRTwD3HVJHdXltX8rWHZth58LrVIsobQBi-tgAW0qHK4oDyA-bExGldUdYO-yuAEmZWM1m41ufWNknqfopzU4g2lSeYmv4xWTv6lYdSKwajRBDSQuEv159tQvFxEF54EHG_zBm2h7O7lA0j0RpdeYot7djY2ltUD4LJOmLIDO8TH1XnswYdz23Mun6Y5KbW8TZh0dsXC4wJztjavvHxEouyAxJPk_wuYNY682rMyCtB4_3OXTWZpCSW-iD_9IQEHT1GUW-5WcTYMC3c2RIkiPTo_vs2cFIYph8irn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeSHe5CrcX7solTDeXsYH_MvDWEVGbBaeHDKt7uHrSxJSuHjMKECAk7TVYprAQrC7hD1UjEelbcwxjTayBO5PyOdsdubTeFT9tNYoDsGLSDqWLGBpqyW2B18ncl-WSo3dacU231RvhwWih8F2cDWvg9pmHiyGI6df4MLkNoam_aIaBwAfOLirvn_cJlKruuJW0liLT77yECGyrvsvoUVixdWO0EGqARMV9CaXkpkyrv2yX0uklTQbBuo7pyz0f2FA-eJD-aqnQie7_RqFJAyxmDKDb5JznlZHFyAiB2kMrr6wLx7nIf3M72r3jT4DgvqekBmL0cCkqkKv5E-i5cUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbD3kEG5ke6QbLeTdF_DDkNbd-he-OTq9mRM0InS1otJAEvTdciIx-DLWe43-BkJLhd2HsDdwbR3cZs-lyC056gFKW_-JwK0giKwLeOp_hCm0POUOd40vR8ile3SAdubEY8QupRRY_RquvZGSePUoYQFqM-lgyevRVwPFfuUbeIqxv0cGDzCcoSwDKbt6SoX4jTtQPqe9EXlSyhctfjtFzJDxonDHdRk3A2fbEgMp11rRxAyWEILmf1nwUvyoqtssA5FuBORpgzkWkfHMz8JYCpiLZEmuymT3RUoQS__jwLTv5zoCmIW_kjWBFTjEkq1NSflafGjcErP7icCXMSKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnqTz1_LV5YDf2gfoaI_ne9H4EerlYALVXcpwqwIoSkesXGuxLacr1zFJNgG-I9lNSFJEXU3teGP_qFJAJd1BOapY-bOgAP3-pmrzvldkAQhAo6r02JWxwuiTijzu849PpB2GrRyNlWoFgSGra4KJobXKRs7NARo7Tev1HM4DjE9NFlCgYsAlDYCf9eQyRDfRkE6gUWYtlBbi2MvASUKMHfyjx0EpfGrKW6pGPhpW4ELib-rKZsN4PkU_D_J9yeDvSHnYJbdpvc9SQ1lC-G72exmvLBGF8UsyxunAyhDFJexz644zUaWAbFdRsTLEHbhmfJLDilCQ5uiis4yABUEXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78565" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAHaE5IwRsRc0hQkrIlUmSmn2U9qpsvMyqq-Q7Vveabgz3Ewri7FKf86ZWhFV7EEug3fk8qQ0FJNj9OGPfnADMLsH7NlcYszPnyDTx5156a8xTtdAizRWlkXuvD-RelF-LcDxCGL3EvpCsTCdcmS4cvz7Q-okbOgbwhojHQzy2J-CNyogCCVIfWnc5uVLbTnvzLtN8Cxt5G1yeCpT2NK83YWMe78TekLrbyxZAx43UHvMtFu7jTuwNsINzyjzn5e5hMOXTyVhxE9LFebbMDKK1nZT0lCOrH4xRjSPrBsl924FYz_7WNYR2vhaipiDlx6FwF0bDDnNB3xIbajLE5Gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78564" target="_blank">📅 17:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کونی رو ترک عاشقانه این چه اسمیه گذاشتی</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78563" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دکی کونی موقع ماشین شستن من چه وقت ترک دادنه</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78562" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تنها چیزی که اَ بابام میخوام عشقه فقط
من برا بابام قیمه میبرم من من عرضشو دارم
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78561" target="_blank">📅 16:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCVQ619R0MXfYT1hsaS5kp8OERnpCJ5AJUl_nssA8LF3fRaslkL469cMwnfz2urElZSy6QBtK8ZFgLvo4T94VlCz8KF9MPqJIUJpW2wDYSlwTebEX7bFXSwv7TFOkSSJEdGRlLBUaxdD7X16zvuIgq244TzEatvEcOIEO2j3_yatuq-TiMQ6xomJJ9vLO2Llny89l-sb5ISzwDmrPpXgDBEGDf7XaB46QhYwBG5a1sL4I2EMNcUCjDkvtlLnfH2CN494jSU5CxjEgahVepVr55b9pe6dLhwuv-obX46A-N_5bX_VnjZ5hY4ncglddlRiCpLI-GLVoBhfhwgUXCvYhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو رسانه‌های آمریکا به جز فاکس‌نیوز کلا یدونه نیویورک پست برا ترامپ مونده بود که اونم کیرشو کرد دهن ترامپ و توافقش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78560" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FORkF-eYhor1L7t0hErwsnLWtHkMmU54Ov_WFRWUMM5C1jSrhxqeorqHhEwOgrrmCPszdYAH-CzJ3TSEcqfrkmuZFc-GaYYsCIGq9apFWTMa8mu3nZFfkfLX1d7-W0ufhdOh7Oo88hRfnOcpAq8klZugNM4mxWYavWT5Qt_4TAnDiQIs1XfFnhpUYgWC_-dIXVFPQFopM_hAW_OPexH-9e1ZP9LAnFsynEpsuPUUJJWaUYlxU4YGrzS3sPljW_5c63syIOHaNtud_CdCt8kRc2UgvVm_PIiBzJpyY8gpTzbwrs7VNCIf127YR2tUs4dobMyB2hCT0DVAwcX7173hbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا با دست مسعود روی شهبازو کاری ندارم
چتر چی میگه اونجا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78559" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پزشکندر و عراقچی رسیدن اسلام آباد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78558" target="_blank">📅 15:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">علی گرامی بخدا خصومت شخصی باهات ندارم به عنوان یه شخص بی طرف دارم میگم، یه آدم رندومو تو خیابون نگه دارم بگم بیا رو این بیت رپ بخون از تو بهتر میخونه، روی این مسئله شرط میبندم، پس لطفا فاز نقش اصلی سریالو تو یکی نگیر بزار یه نفر این کارو کنه که بهش میاد
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78557" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مسی و رونالدو جان جدتون زودتر خدافظی کنید فناتون مغز مارو گاییدن
هر سری یکیشون گل میزنه فناش مثل زامبیا تا یه ماه میوفتن تو گپو چنلا سوراخمون میکنن که ابر ستاره تاریخ فوتبال گل زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78556" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuZgHywyDQzzZC-H3MDvFORJ6BmP0N02p4v-qIC_Xk_rh7dvcyLm0DsoJloH-Qks6Mut0-0sCoJ82GZL7nwEcGnqbryFdeUkUlfjD-ugVCHXIcgq_d1D6N-N9H1E2Fm3VxGFrmeDbujXnDWAh2XHF4NJtp7cN-O9MseEBdqNylspSc55TBgznuClzvnIrHycIkfhUvNgX1twWpw5LaASBW7_PdOcv9uD68NpydUQOcMqEmTMocX5GvYXUUH8HrrNYg0ovJNhjT1Wh6U8calhKt8kBZf2vsdz7Nh1KtSYb9iRo0WdOjNDJVO2M5Y3D8Ew81kLG5_w5IN71AWCHPX-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78555" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">من ک میدونم بانک هارو بگا دادن تا حواسارو از عروسی دختر شمخانی پرت کنن ولی نمیتونم ثابت کنم:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78554" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مثل اینکه اکثر بانک های کشور بگا رفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78553" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آلوارز گفته از سبک بازی اتلتیکو خوشم نمیاد، اتلتیکو چی گفته باشه خوبه؟ گفته خب بیا برو آرسنال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78552" target="_blank">📅 12:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حمید سحری عزیزم تو ویدیو هاش به کصشر ترین تیمای جام هم اشاره کرده ولی به ایران نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78551" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrBgSE6yCHfNDWL4ENktYGRhFTrhaxn-eb22sc9KTobN5Je6Q65AzAOomUQDFe80uCEYPkXKJvXIcdnBKG-uFqEovIYlGliwlPirg2jsL4bpOIF5KhTjTek8OOxe3IDd0aOGYS9kCGl_ewspX2wh4lTEk2rxrKq2z5u2jFjmCvyBs5t5oYHlxc7DtsPgeaXco8VvYETLG5M9KDuaGhuPpqvJAdJU9QIgWczL-tMTtt0uuTcxvzTPAxbhnB7mfO7C8bjfLKpxhL8AMXw69VhQHbSoSxQ26RX8j4sOBzwGz_6NPO0tg9VVLziS_IqZxIY-ieKDz2Zub2g5ZSc_OfMcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78550" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TimaGrHr_mgn_bMUM-UMomSNDC6zTylzuA5RD2mU1XO6mXVJ5Z-gGh9HYVb5I6sFPcAsX22q6YbDdjkooOLXu6Tn5BDgxGZpX8D94-JZ0jczLZsKIs8VU3MjBIe4wWBvrTmexwBfvkAwh0dLJsnaFehacq_TYyjhfGnK0q33k8JPEwA3zEy9gU7r5uasE0DR6-PDSJwvFg0pLD9Ez0YkM7ZZciVIIWGR7YafVGojCIcoZk-jt4-uo2s8lQsMGBXOaKVgUpcu4zv0a_QZsXnBLe5Bny1SsyPJcdKeMySD3ie_37ZPhpEEJGAuIoDp8oV667w7HXv8bH0Qu7u7ar3jIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان از ارث محروم میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78549" target="_blank">📅 11:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FbNKfKq7Sp7UI9KDJ7ebv-IXHFmFE9Om_2UPjjD9Pq9aORaOW7SxtK8zfIUBQ3ejdGGXqiH2ODYNpi86teMja51JvVgPHR7orl_WMWFTomEs2RnFwq3CaMtkHKZwPt-CtbvRAqMmFO0k5mWrBK__TQOtlJyTmOIQQNLz3jx5JXR3-6bJBhZ_oHd-MehVSkAQJ41_mwDcPb5pwM0i4Sz7YEjRbPc2EtBz2tR_aNKnqYuDp1K73JpOg4J_xnT-_vwkY0V4IZXDscKIedwHE-wOxbxJUvXqrc6GxzKzDQHiMkFOT_opzMVtvEC8WJimqXJ3LgxUdTnK8r0T2IcrqPkt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ هالند: راستش بازی با فرانسه زیاد برام مهم نیست چی میشه؛ احتمالاً اونا ما رو میبرن و حتی احتمالاً قهرمان تورنمنت میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78548" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78547" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foFdr-TK0A-nL7I4KmFe89RZfjlfzs4Zt8Rl8-fX_P__GM09nqSjp_mI0M8QPCw9IcWE9KhluA0MjgOPxcwqIBqs7w8zj0p6I-5E3vwz5JfQ2sL0eW0gl0Xf4nsHVa2as9i3RO4YJMixYCjvmW9IJuF8L1jXI7HxQaxANnANrK1ifVjQpFfWD7Mx8JN5Fef5Bw8bNjewnwZETK-TTSm9w-hphhz5Mp6lsWbNiMTKoG758wsRIaOc2y7mNjSLzkWEjPpNuk7Jpk-n9cOJyFZah71wIwDTuU4cY9W-qjWp7mXOthvhUWWKqrEeLz4POP022FG1rDZSQfNZ8JqZaO9Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
R2
🅰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78546" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc9G5VcQZGhxouP4nFtIGVbMc7jeUsfI1islCcVWj0GaheU-I7GC-4E6dPkTrpEiZ952__b6hIj32CgC7KDup6ZvrFYUz2oZ5QKPy7HTjZ60dNlXYS9GGPKHrdHmoPXzCgfMNaARBF02I7_3OJdRmjzSgDhqluNjIoVXGU7MUHb1ZFfniETswWxFV9s8sbPeYLyxHWp-urz-Xpw1KfiNJeM1Tpds9DQyvlzqMmeVtdWPBW0SfC8qSXwqj9wcRqxRn4n592nhfw4xdNIBlXBT37CELjZQSIx9PS0LeYjOyxPLXi-SjY6KVjxudpkJONHkNrx5yI0M4t5q5LBfuEYaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این الان تو حالت طبیعی به وانتونز و ویناک گفت فید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78545" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78544" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l582G30mgLUKWJk7oCs6IhEnZPosk6u1fNu8D4oBnh4IPEikUxN9ydIlpPmO0vUwtmre-DWBRQg_S8y_wZUvlQe-9TybF4qLwHWWqMIQqBVYTZn8tNFbjT153paCo7lw0_vB4ZOXnHtEyTzXIY2N1rbjv5KbaEi3bGnEDnQ4VGHEPNNZ3XaQlU-MlY3W6ugjueZAiBCB-WCPJOudDFOyk972ox0b5vsW198G4SoiMddkNvcMisjl7OhByHZgBgEtBY810odBXN4AdKF-ZqDAM-cr6SdzQsiXLlFUYzaJ8Jgnp4a7gkMV4otsfB7Zx9EvVSbnaMjPGSoWHTMsBA8lEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون مسی رو ول کنید کصکشا مثلا بزرگتونه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78543" target="_blank">📅 10:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBUZt2n4LX6bgocj4FW9wpnQW48cdvMP52Cu0KRFYU2FomTQkzXXZFcZI0YDLBMsJvZ0oCAIlVWk51VsDyK-RgTzokULXyHuIwpJW8D421zxMkdVHMKXPD6KBnmgaUKb2rSzV7m4DBJWzmYhanEKML5yaFps7ANG2L8PT-stq3bWGJpa6VWBz7DhT1poAcJgoHqx25H_hYoyHXFTNUjSIU2V6KOtV9B6AWLlcjcgD2i8U_pTMkjfU5-1nWv8IscaprHIr9ppuwum7L6qW9v_x8ndiMRVHkrwVxQzugrL9A6vR2zyLgvS9t88xXJMUwCXqeV6_pxV9s9umhJhGPWAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی رئال اولیسه رو بگیره کون بارسا تا چندسال پارس
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78542" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بعد اون همه کارزار گذاشتن و اعتراضات دانش‌آموزان پایه یازدهم و دوازدهم، آموزش پرورش امروز گفت حتی یک روز هم امتحانات نهایی رو عقب نمیندازیم و سر تایمش شروع می‌شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78541" target="_blank">📅 10:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛ یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78540" target="_blank">📅 10:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=aPNMyqeAdRolCCpi-9CgAysfPBEge56MwoB2CQHjimBO2ff-XzaJ448ZmGHRU8EqqgowG9ysLuCfPLhXRWkefTe1vcRUWCa7fKS2mIxVd-nhdKBtZ2EYinpQFdW1pOqxVCmNpgROPXV5sQ_a36c9BZQy1LG9I0mkfjyGepS5BE4slGMCnCeth6BeFhJ8GXFta3hgxdJ0SWdrwUCmHCHLIODTwrqhC4r5ikjFJdv0SPMmc3gN-s3_fBM9tWUVP-qLqTOmMnCd3AOtW_v7iCOr4Nltx1ZVv28H4C96f0n0j46fhG0XJkhx8-7P7yfmyKdTWr6X-8J_aTMKegKULUw8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=aPNMyqeAdRolCCpi-9CgAysfPBEge56MwoB2CQHjimBO2ff-XzaJ448ZmGHRU8EqqgowG9ysLuCfPLhXRWkefTe1vcRUWCa7fKS2mIxVd-nhdKBtZ2EYinpQFdW1pOqxVCmNpgROPXV5sQ_a36c9BZQy1LG9I0mkfjyGepS5BE4slGMCnCeth6BeFhJ8GXFta3hgxdJ0SWdrwUCmHCHLIODTwrqhC4r5ikjFJdv0SPMmc3gN-s3_fBM9tWUVP-qLqTOmMnCd3AOtW_v7iCOr4Nltx1ZVv28H4C96f0n0j46fhG0XJkhx8-7P7yfmyKdTWr6X-8J_aTMKegKULUw8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛
یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی
یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78539" target="_blank">📅 09:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78538" target="_blank">📅 01:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=HQ6LI-HS1hoSojDWBGU1SY_W9O9b4FECosprz4s0s1xMndQzWJ2ozukpOvKv4FhKByCpaGEe8h0OdZghBVFzsf9J2QBCeduxmdioRz324U7pYwKCQqzbWZEM2x0a3a0G9jeeQyW6aGoM6SLCzwREvStjaf8sWfz5BdmMPOgorQu5qkyCqBIRgjzqAGjhUErb9a_0SvCW-w8K973B33DwJUAn9i8KlpBCTh5Whx4BJ0QAlgxJRNDddzKzcLUP_H0LKZZJ6fTzXsQG24po0GKNvqyJA6vo_9NwBF9OeWLHkw1KBV6YmHuFfFzWO4Cg0x1D-wCAG44kGdRBcl33-5t3dA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=HQ6LI-HS1hoSojDWBGU1SY_W9O9b4FECosprz4s0s1xMndQzWJ2ozukpOvKv4FhKByCpaGEe8h0OdZghBVFzsf9J2QBCeduxmdioRz324U7pYwKCQqzbWZEM2x0a3a0G9jeeQyW6aGoM6SLCzwREvStjaf8sWfz5BdmMPOgorQu5qkyCqBIRgjzqAGjhUErb9a_0SvCW-w8K973B33DwJUAn9i8KlpBCTh5Whx4BJ0QAlgxJRNDddzKzcLUP_H0LKZZJ6fTzXsQG24po0GKNvqyJA6vo_9NwBF9OeWLHkw1KBV6YmHuFfFzWO4Cg0x1D-wCAG44kGdRBcl33-5t3dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78537" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHL13Nt7VrpRlOsWK6uxVDfRJfGpXO2QpHfD4NJQ54qpX9v9uQICBhXfmgOoFz4zI3FDw-VrWOa6M9Irb42UgPUcpihu5y6XtaSIT2TqgRCEUcXhgT0rHSeZ7Ruef5TGJ4JteUKJcQ_sVDi8zh-BVpPe-9b9f9up0YNpzzMRqVIfLG3hkc6lyrm5--ohOHNYtepWHGNTlW7CA6i8FduRVAmzNd21sBAuIJPGYCv6LYKZslBS0huh-leiqmN5j0I9_0RY_HNYsJoNvtnm9_qdX-Qdyt607BPpot06dpi-T8YgoY15aNv5haymjmgO1fx9KlNHK5urpmstaV9_KX8bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان هشدار تخلیه برای تماشاگران ورزشگاه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78536" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78535" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78534" target="_blank">📅 01:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78533" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امباپه احتمال زیاد موقع پایان کریرش بهترین بازیکن تاریخ جام های جهانی باشه جلوتر از پله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78532" target="_blank">📅 00:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کصکشا اینارو من ۴ سال پیش دیدم، چیز جدید ارائه بدید</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78531" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امباپه چی زد خارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78529" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imn9H3e0e5k0k4ZRdziE8eixboWBqS5g5UcHOm5kgFlOCc8VpIZgNVqDb1rYYI9jZB3TndYi05EkEphoAgzWgLE42TwlVsEHNmSsUt3x9A6dN7WQrAMPzr4y0MmaATP3dan2IqvDyHtzxwFOI_UnsFr0fYvxrKBzflc-zLeT3ddyNBU6S5WKk2yC83Y4dfGXZlsL1N7O1lxbVskEl3uhAYiBoZvJ7AfIECrByGvj0l_nl946vwWSsw1KIerxn6mnshSyOtx6U1MKTFXDU9I76yFtVVPaudLa53c5x2iuLSSADxh45VrgaK4oHAkdyTjvTNBeOqh6vMljq-_Byggopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی جدی مجلس چهارماهه که کامل بسته‌ست تا کسی نباشه که جلوی باقرشاه و پزشکیان رو بگیره.
یه سری از نماینده‌ها هم علنی دارن صحبت از کودتا می‌کنن و برا یکشنبه آینده فراخوان دادن که برن جلو در مجلس، اگه باز شد که برن تو و اگر هم نشد همون تو خیابون جلسه برگزار کنن درمورد روند مذاکرات و جنگ و اینا تصمیم گیری کنن.
یه سری حرفای ضد و نقیض هم درمورد تصمیم نماینده ها برای استیضاح فوری عراقچی و حتی پزشکیان و باقرشاه وجود داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78528" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دالگخیز:
پسفردا به ناتو اتک دادن کیرمم نیس چون زمانی که ما به ایران حمله کردیم کیرشونم نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78527" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427abb0164.mp4?token=DUUapldZyFuGcnHPJ77Q5LiV_qG1N6Vzq0VhmsBFfoUXW0Ch0rSdwh-thys500QEuhp5YyFy-QstRg_-pRzLnR8cz-O354HFVQ8RtxHTnQugGxO2uZQMS1sbtb3t_F4yGBzY_aN3KLQwWs0DSJqeXd3yjUvmW4T1LPxX3rKonkssPIoeXkI0XtTuwKm0ZrQNDk57LYHdfEbiDiWo_N1M7Vd_D-ao8ZR1824fSdbCbbeO5KgOxoqrpxMj0oQMf4S0h0CjRakj9WnEcG39RwyyeNcyYNuUlpP80Dieu68WgEZL-X0bJBaknThMRaO_SlD3ZUrTI701paLYTcUw9X_l5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427abb0164.mp4?token=DUUapldZyFuGcnHPJ77Q5LiV_qG1N6Vzq0VhmsBFfoUXW0Ch0rSdwh-thys500QEuhp5YyFy-QstRg_-pRzLnR8cz-O354HFVQ8RtxHTnQugGxO2uZQMS1sbtb3t_F4yGBzY_aN3KLQwWs0DSJqeXd3yjUvmW4T1LPxX3rKonkssPIoeXkI0XtTuwKm0ZrQNDk57LYHdfEbiDiWo_N1M7Vd_D-ao8ZR1824fSdbCbbeO5KgOxoqrpxMj0oQMf4S0h0CjRakj9WnEcG39RwyyeNcyYNuUlpP80Dieu68WgEZL-X0bJBaknThMRaO_SlD3ZUrTI701paLYTcUw9X_l5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناکیا چیه دیگه کیرم دهنت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78526" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگه این جمهوری اسلامیه از آمریکا مواد غذایی میگیره میده دست بابک زنجانی که صادر کنه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78525" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ: دارایی‌های آزاد شده نزد ایران برای خرید مواد غذایی از کشاورزان ما استفاده خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78524" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78523" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78522" target="_blank">📅 23:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پسرا رو برد فرانسه میبندن مردا رو برد مساوی عراق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78521" target="_blank">📅 23:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTMDkJo8JXyiIEdUYFOe0AKraRh3-mHA7X0wi2gscM9joWaXsm9ivC-cwIryL4UEmM3JrobmmKu7q893POMLZq-aIZsLPg-xIUlfvPxEKeLyZGva0gxvaPIBzHXWJCKKWg-Pl9BqH2nLR3hMkLojUqzSXbf0nZolw482sNFzM_mp-ckMMHKFiBKfsuoqwNNyrZvwdW4UqetuXGItY1i_yCsh__is7bNcV1xqISwVNFsAeWEpdx6uqQaaJQR5iI7qC1uEAdATU2c4A8txCM6FaZBL5HeAwS1XDebKVu2qvgoRdb8JCqHuDTCwa8FzjKS8Tb3GlzuL9nFKyWYUOsRu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب رسمی فرانسه واس بازی امشب
اگه ببرن میرن مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78520" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تا الان صعود این تیما به مرحله بعدی قطعی شده:
آلمان، امریکا، ژنرال، مکزیک، النصر، آرژانتین.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78519" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
